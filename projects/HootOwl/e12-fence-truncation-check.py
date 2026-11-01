"""Replicate Mu1Proto.convexEnclosing(point:) exactly, against the real shipped fences.

Swift under test:
    let edgeX  = Int(next.longitude) - curr.longitude     // both already Int(wgs84.longi)
    let edgeY  = Int(next.latitude)  - curr.latitude
    let pointX = Int(point.longitude) - curr.longitude
    let pointY = Int(point.latitude)  - curr.latitude
    let cross  = edgeX * pointY - edgeY * pointX
    sign = cross > 0 ? 1 : (cross < 0 ? -1 : 0)
    if prevSign == 0 { prevSign = sign } else if sign != prevSign && sign != 0 { return false }
    -> return true
"""
import json
import math

BASE = ('/private/tmp/claude-501/-Users-jimhsu-developer-farms/'
        '228d44de-ef98-4c29-a81d-cf2632652cfc/scratchpad/dd/Build/Products/'
        'Debug-iphonesimulator/hootowl.app/fences')


def trunc(x):
    """Swift Int(Double) truncates toward zero."""
    return int(x)


def load(name):
    d = json.load(open(f'{BASE}/{name}.json'))
    return [(p['wgs84']['longi'], p['wgs84']['latit']) for p in d['points']]


def convex_enclosing(fence, point):
    n = len(fence)
    if n <= 2:
        return False
    prev_sign = 0
    plon, plat = point
    for i in range(n):
        curr_lon, curr_lat = fence[i]
        next_lon, next_lat = fence[(i + 1) % n]
        edge_x = trunc(next_lon) - trunc(curr_lon)
        edge_y = trunc(next_lat) - trunc(curr_lat)
        point_x = trunc(plon) - trunc(curr_lon)
        point_y = trunc(plat) - trunc(curr_lat)
        cross = edge_x * point_y - edge_y * point_x
        sign = 1 if cross > 0 else (-1 if cross < 0 else 0)
        if prev_sign == 0:
            prev_sign = sign
        elif sign != prev_sign and sign != 0:
            return False
    return True


def encloses(fence, point):
    """The correct one already in the codebase: ray casting in real degrees."""
    plon, plat = point
    inside = False
    j = len(fence) - 1
    for i in range(len(fence)):
        alon, alat = fence[i]
        blon, blat = fence[j]
        if (alat > plat) != (blat > plat):
            x = (blon - alon) * (plat - alat) / (blat - alat) + alon
            if plon < x:
                inside = not inside
        j = i
    return inside


fences = {'taipei': load('taipei'), 'newTaipeiCity': load('newTaipeiCity')}

print('=== what truncation does to the vertices ===')
for name, f in fences.items():
    lat_lo, lat_hi = min(p[1] for p in f), max(p[1] for p in f)
    lon_lo, lon_hi = min(p[0] for p in f), max(p[0] for p in f)
    lattice = sorted({(trunc(lon), trunc(lat)) for lon, lat in f})
    print(f'{name:14} {len(f):2} vertices  lat {lat_lo:.3f}..{lat_hi:.3f}  '
          f'lon {lon_lo:.3f}..{lon_hi:.3f}')
    print(f'{"":14} collapse to {len(lattice)} distinct whole-degree points: {lattice}')

PLACES = [
    ('Taipei 101',            121.5645, 25.0340),
    ('Taipei Main Station',   121.5170, 25.0478),
    ('Banqiao, New Taipei',   121.4628, 25.0143),
    ('Keelung',               121.7392, 25.1283),
    ('Taoyuan',               121.3010, 24.9937),
    ('Taichung',              120.6736, 24.1477),
    ('Tainan',                120.2270, 22.9999),
    ('Kaohsiung',             120.3010, 22.6273),
    ('Hualien',               121.6015, 23.9871),
    ('Kenting (far south)',   120.7980, 21.9480),
    ('Tokyo',                 139.6917, 35.6895),
    ('Seoul',                 126.9780, 37.5665),
    ('Manila',                121.0244, 14.5995),
    ('Shanghai',              121.4737, 31.2304),
    ('New York',              -74.0060, 40.7128),
    ('London',                 -0.1276, 51.5074),
    ('Sydney',                151.2093, -33.8688),
    ('Cape Town',              18.4241, -33.9249),
]

print('\n=== convexEnclosing (shipping) vs encloses (correct) ===')
print(f'{"place":24} {"convexEnclosing":>22}   {"encloses":>18}')
for label, lon, lat in PLACES:
    cv = [n for n, f in fences.items() if convex_enclosing(f, (lon, lat))]
    en = [n for n, f in fences.items() if encloses(f, (lon, lat))]
    flag = '  <-- WRONG' if bool(cv) != bool(en) else ''
    print(f'{label:24} {",".join(cv) or "-":>22}   {",".join(en) or "-":>18}{flag}')

print('\n=== how often they disagree over a wide grid ===')
agree = disagree = 0
false_pos = 0
lat = -60.0
while lat <= 70.0:
    lon = -180.0
    while lon <= 180.0:
        cv = any(convex_enclosing(f, (lon, lat)) for f in fences.values())
        en = any(encloses(f, (lon, lat)) for f in fences.values())
        if cv == en:
            agree += 1
        else:
            disagree += 1
            if cv and not en:
                false_pos += 1
        lon += 1.0
    lat += 1.0
total = agree + disagree
print(f'grid points tested : {total}')
print(f'disagree           : {disagree} ({disagree * 100 / total:.1f}%)')
print(f'  of which the shipping test says "covered" and the correct one says no: {false_pos}')
