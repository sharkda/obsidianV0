I add this readme, and see if this fit the GitHub Expection


Two pieces: a **shell script** that does the sync safely, and a **`launchd` agent** that runs it on a timer. launchd is the right tool on macOS (cron is deprecated). Your earlier passphrase-free SSH key is what makes the push non-interactive — that's the prerequisite, and you already have it.

**1. The sync script** — save as `~/bin/vault-sync.sh`, then `chmod +x ~/bin/vault-sync.sh`:

bash

```bash
#!/bin/zsh
export PATH="/opt/homebrew/bin:/usr/bin:/bin"
VAULT="/path/to/your/vault"
cd "$VAULT" || exit 1

git add -A
# commit only if something changed
if ! git diff --cached --quiet; then
  git commit -m "auto: vault backup $(date '+%Y-%m-%d %H:%M')"
fi

# pull remote first (keeps two Macs in sync), then push
git pull --rebase --autostash origin main
git push origin main
```

**2. The LaunchAgent** — save as `~/Library/LaunchAgents/com.jim.vaultsync.plist` (edit the username path):

xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>com.jim.vaultsync</string>
  <key>ProgramArguments</key>
  <array>
    <string>/Users/YOURNAME/bin/vault-sync.sh</string>
  </array>
  <key>StartInterval</key>
  <integer>1800</integer>
  <key>RunAtLoad</key>
  <true/>
  <key>StandardOutPath</key>
  <string>/tmp/vaultsync.log</string>
  <key>StandardErrorPath</key>
  <string>/tmp/vaultsync.err</string>
</dict>
</plist>
```

**3. Load it:**

bash

```bash
launchctl load ~/Library/LaunchAgents/com.jim.vaultsync.plist
```

That runs every 30 minutes (`1800` sec) and once at login. Logs go to `/tmp/vaultsync.log` so you can verify it's working.

Three things worth knowing:

The `git pull --rebase --autostash` line is what keeps your two MacBooks safe — each Mac pulls the other's changes before pushing, so timer-driven syncs from both don't reject each other. The one scenario it can't auto-resolve is the _same note edited on both Macs_ between syncs — that leaves a rebase conflict and the script stops. Rare for a personal vault, but it's why you'll want to glance at the log occasionally at first.

Run it on **both** MacBooks (same script, same plist) so each pushes its own changes and pulls the other's.

Tune the interval to taste — `300` (5 min) feels near-live; `3600` (hourly) is gentler. Since git is discrete snapshots, none of this touches the MCP gateway throttling problem.

Want a guard that pauses syncing while Obsidian is mid-write, or is the timer enough?