```
default	09:45:20.553740+0800	hootowl	[ {"framework": "Photos", "swizzle":[ {"class":"PHAsset", "methods": { "prefixes":["fetch","enumerate"] }, "duplicate detection type":"AllFrames", "antipattern type":["XPC on main thread"], "performance issue type":["hang"] }, {"class":"PHFetchResult", "methods": { "prefixes":["fetch","enumerate"] }, "duplicate detection type":"AllFrames", "antipattern type":["XPC on main thread"], "performance issue type":["hang"] } ] }, {"framework": "CoreLocation", "swizzle":[ {"class":"CLLocationManager", "instance methods": { "names":["authorizationStatus", "monitoredRegions", "accuracyAuthorization"] }, "class methods": { "names":["locationServicesEnabled"] }, "duplicate detection type":"AllFrames", "antipattern type":["XPC on main thread", "XPC on main thread"], "performance issue type":["hang", "launch"] } ] }, {"framework":"CoreImage", "swizzle":[ {"class":"CIContext", "instance methods": { "names":["createCGImage:fromRect:", "initWithOptions:"] }, "duplicate detection type":"NonSystemFramesOnlyFrameworkSupplemented", "antipattern type":["IO on main thread", "IO on main thread"], "performance issue type":["hang", "launch"] } ] }, {"framework":"HealthKit", "swizzle":[ {"class":"HKHealthStore", "instance methods": { "names":["authorizationStatusForType:"] }, "duplicate detection type":"AllFrames", "antipattern type":["XPC on main thread", "XPC on main thread"], "performance issue type":["hang", "launch"] } ] }, {"framework":"CoreData", "swizzle":[ {"class":"NSManagedObjectContext", "instance methods": { "names":["performBlockAndWait:", "executeFetchRequest:error:", "mergeChangesFromContextDidSaveNotification:","save:", "countForFetchRequest:error:"] }, "duplicate detection type":"NonSystemFramesOnlyFrameworkSupplemented", "antipattern type":["Database access on main thread", "Database access on main thread"], "performance issue type":["hang", "launch"] } ] }, {"framework":"CoreML", "swizzle":[ {"class":"MLModel", "class methods": { "names":["modelWithContentsOfURL:error:"] }, "duplicate detection type":"AllFrames", "antipattern type":["IO on main thread", "IO on main thread"], "performance issue type":["hang", "launch"] } ] }, {"framework":"Foundation", "swizzle":[ {"class":"NSOperation", "instance methods": { "names":["waitUntilFinished", "waitUntilFinishedOrTimeout:"] }, "duplicate detection type":"AllFrames", "antipattern type":["waiting for operation completion on main thread", "waiting for operation completion on main thread"], "performance issue type":["hang", "launch"] }, {"class":"NSThread", "class methods": { "names":["sleepForTimeInterval:"] }, "duplicate detection type":"AllFrames", "antipattern type":["Sleep", "Sleep"], "performance issue type":["hang", "launch"] }, {"class":"NSBundle", "instance methods": { "names":["bundlePath", "bundleIdentifier", "loadAndReturnError:"] }, "class methods": { "names":["bundleWithIdentifier:", "allFrameworks", "allBundles", "pathForResource:ofType:inDirectory:"] }, "duplicate detection type":"NonSystemFramesOnlyFrameworkSupplemented", "antipattern type":["IO on main thread", "IO on main thread"], "performance issue type":["hang", "launch"] }, {"class":"NSKeyedArchiver", "class methods": { "names":["archivedDataWithRootObject:", "archivedDataWithRootObject:requiringSecureCoding:error:", "archiveRootObject:toFile:"] }, "duplicate detection type":"NonSystemFramesOnlyFrameworkSupplemented", "antipattern type":["IO on main thread", "IO on main thread"], "performance issue type":["hang", "launch"] }, {"class":"NSKeyedUnarchiver", "class methods": { "names":["unarchiveTopLevelObjectWithData:error:", "decodeObjectForKey:", "unarchiveObjectWithData:"] }, "duplicate detection type":"NonSystemFramesOnlyFrameworkSupplemented", "antipattern type":["IO on main thread", "IO on main thread"], "performance issue type":["hang", "launch"] }, {"class":"NSFileManager", "methods": { "prefixes":["remove", "create", "move", "copy"] }, "duplicate detection type":"NonSystemFramesOnlyFrameworkSupplemented", "antipattern type":["IO on main thread", "Excessive IO on any thread", "IO on main thread"], "performance issue type":["hang", "disk write", "launch"] }, {"class":"NSFileManager", "instance methods": { "names":["synchronouslyGetFileProviderServicesForItemAtURL:completionHandler:"] }, "duplicate detection type":"NonSystemFramesOnlyFrameworkSupplemented", "antipattern type":["IO on main thread", "IO on main thread"], "performance issue type":["hang", "launch"] }, {"class":"NSData", "methods": { "prefixes":["initWithContents", "dataWithContents"] }, "instance methods": { "names":["enumerateByteRangesUsingBlock:"] }, "duplicate detection type":"NonSystemFramesOnlyFrameworkSupplemented", "antipattern type":["IO on main thread", "IO on main thread"], "performance issue type":["hang", "launch"] } ] }, {"framework":"AVFCore", "swizzle":[ {"class":"AVAsset", "class methods": { "names":["assetWithURL:"] }, "duplicate detection type":"NonSystemFramesOnly", "antipattern type":["IO on main thread", "IO on main thread"], "performance issue type":["hang", "launch"] }, {"class":"AVAsset", "instance methods": { "names":["mediaSelectionGroupForMediaCharacteristic:"] }, "duplicate detection type":"AllFrames", "antipattern type":["Conditional waiting on main thread", "Conditional waiting on main thread"], "performance issue type":["hang", "launch"] }, {"class":"AVAsset", "instance methods": { "names":["tracksWithMediaType:"] }, "duplicate detection type":"AllFrames", "antipattern type":["XPC on main thread", "XPC on main thread"], "performance issue type":["hang", "launch"] }, {"class":"AVURLAsset", "instance methods": { "names":["tracks"] }, "duplicate detection type":"AllFrames", "antipattern type":["XPC on main thread", "XPC on main thread"], "performance issue type":["hang", "launch"] } ] }, {"framework":"AVFAudio", "swizzle":[ {"class":"AVAudioSession", "instance methods": { "names":["setActive:withOptions:error:", "category", "setCategory:mode:options:error:", "setCategory:mode:routeSharingPolicy:options:error:", "setCategory:withOptions:error:", "setCategory:error:", "currentRoute", "outputVolume", "setAllowHapticsAndSystemSoundsDuringRecording:error:", "isPiPAvailable"] }, "duplicate detection type":"AllFrames", "antipattern type":["XPC on main thread", "XPC on main thread"], "performance issue type":["hang", "launch"] } ] }, {"framework":"StoreKit", "swizzle":[ {"class":"SKPaymentQueue", "class methods": { "names":["canMakePayments"] }, "duplicate detection type":"AllFrames", "antipattern type":["Semaphore on main thread", "Semaphore on main thread"], "performance issue type":["hang", "launch"] }, {"class":"SKPaymentQueue", "instance methods": { "names":["storefront"] }, "duplicate detection type":"AllFrames", "antipattern type":["XPC on main thread", "XPC on main thread"], "performance issue type":["hang", "launch"] } ] }, {"framework":"CoreTelephony", "swizzle":[ {"class":"CTCellularPlanProvisioning", "instance methods": { "names":["supportsCellularPlan"] }, "duplicate detection type":"AllFrames", "antipattern type":["Semaphore on main thread", "Semaphore on main thread"], "performance issue type":["hang", "launch"] } ] }, {"framework":"Vision", "swizzle":[ {"class":"VNImageRequestHandler", "methods": { "prefixes":["performRequest"] }, "duplicate detection type":"AllFrames", "antipattern type":["Computer vision tasks on main thread", "Computer vision tasks on main thread"], "performance issue type":["hang", "launch"] } ] } ]
fault	09:45:20.918803+0800	hootowl	__delegate_identifier__:Performance Diagnostics__:::____message__:{"message":"Performing I/O on the main thread can cause slow launches.","antipattern trigger":"dlopen","message type":"suppressable","issue type":4,"category type":17,"subcategory type":3,"show in console":"0"}'1B 52 60 20 2D E0 3C 65 91 22 F1 17 75 49 D6 9A 30 4F 00 00 1B 52 60 20 2D E0 3C 65 91 22 F1 17 75 49 D6 9A 00 47 00 00 1B 52 60 20 2D E0 3C 65 91 22 F1 17 75 49 D6 9A D8 43 00 00 0F 8D 35 B6 55 6F 3E 34 8E AA 80 AB 54 04 7D C5 1C 4C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
default	09:45:22.328089+0800	hootowl	[0x1054bd340] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon.system
default	09:45:22.328228+0800	hootowl	[0x1054bd480] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	09:45:22.852262+0800	hootowl	networkd_settings_read_from_file_locked initialized networkd settings by reading plist directly
default	09:45:22.852509+0800	hootowl	networkd_settings_read_from_file_locked initialized networkd settings by reading plist directly
default	09:45:22.858026+0800	hootowl	Task <80D33321-F751-4689-823A-9070C09CBDD2>.<1> resuming, timeouts(60.0, 604800.0) qos(0x19) voucher((null)) activity(00000000-0000-0000-0000-000000000000)
default	09:45:22.859160+0800	hootowl	-[SOConfigurationClient init]  on <SOConfigurationClient: 0x1481bdbe0>
default	09:45:22.859263+0800	hootowl	[0x148270000] activating connection: mach=true listener=false peer=false name=com.apple.AppSSO.service-xpc
default	09:45:22.859328+0800	hootowl	<SOServiceConnection: 0x1481bdb80>: new XPC connection
default	09:45:22.867993+0800	hootowl	Initializing connection
default	09:45:22.868268+0800	hootowl	Removing all cached process handles
default	09:45:22.868341+0800	hootowl	Sending handshake request attempt #1 to server
default	09:45:22.868350+0800	hootowl	Creating connection to com.apple.runningboard
default	09:45:22.868452+0800	hootowl	[0x1482703c0] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	09:45:22.869447+0800	hootowl	Handshake succeeded
default	09:45:22.869570+0800	hootowl	Identity resolved as app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>
default	09:45:22.870515+0800	hootowl	Task <6CD5524D-F067-4C09-A823-5B80B55C7B03>.<2> resuming, timeouts(60.0, 604800.0) qos(0x19) voucher((null)) activity(00000000-0000-0000-0000-000000000000)
default	09:45:22.933753+0800	hootowl	{"msg":"CLLocationManager", "event":"activity", "_cmd":"initWithEffectiveBundleIdentifier:bundlePath:websiteIdentifier:delegate:silo:", "self":"0x1483580a0", "identifier":"", "bundlePath":""}
default	09:45:22.939687+0800	hootowl	Initializing NSHTTPCookieStorage singleton
default	09:45:22.939717+0800	hootowl	Initializing CFHTTPCookieStorage singleton
default	09:45:22.939841+0800	hootowl	Creating default cookie storage with default identifier
default	09:45:22.943351+0800	hootowl	Cache loaded with 6309 pre-cached in CacheData and 80 items in CacheExtra.
default	09:45:22.943439+0800	hootowl	{"msg":"client allocated", "client":"0x1054c55d0"}
default	09:45:22.943505+0800	hootowl	{"msg":"_CLClientCreateConnection", "event":"activity", "client":"0x1054c55d0"}
default	09:45:22.943595+0800	hootowl	{"msg":"Sending cached messages to daemon", "event":"activity"}
default	09:45:22.943608+0800	hootowl	[0x148270780] activating connection: mach=true listener=false peer=false name=com.apple.locationd.registration
default	09:45:22.954449+0800	hootowl	Requesting container lookup; class = 13, identifier = com.apple.nsurlsessiond, group_identifier = systemgroup.com.apple.nsurlstoragedresources, create = 1, temp = 0, euid = 501, uid = 501
default	09:45:22.955741+0800	hootowl	_container_query_get_result_at_index: success
default	09:45:22.955945+0800	hootowl	container_system_group_path_for_identifier: success
default	09:45:22.956118+0800	hootowl	Initializing AlternativeServices Storage singleton
default	09:45:22.956142+0800	hootowl	kExcludedFromBackupXattrName set on path: /var/mobile/Containers/Data/Application/9C61D988-8BEB-42B6-A397-1E3A058F7BB4/Library/HTTPStorages/com.sharkda.hootowl
default	09:45:22.958678+0800	hootowl	{"msg":"CLLocationManager", "event":"activity", "_cmd":"setDelegate:", "self":"0x1483580a0", "delegate":"0x148270140"}
default	09:45:22.958760+0800	hootowl	{"msg":"CLLocationManager", "event":"activity", "_cmd":"setDesiredAccuracy:", "self":"0x1483580a0", "accuracy":"100.000000"}
default	09:45:22.958935+0800	hootowl	{"msg":"CLLocationManager", "event":"activity", "_cmd":"setDistanceFilter:", "self":"0x1483580a0", "distance":"100.000000"}
default	09:45:22.969527+0800	hootowl	[0x148270a00] activating connection: mach=true listener=false peer=false name=com.apple.storekitd
default	09:45:22.974668+0800	hootowl	Garbage collection for alternative services
default	09:45:22.985342+0800	hootowl	Connection 0: creating secure tcp or quic connection
default	09:45:22.986128+0800	hootowl	Task <6CD5524D-F067-4C09-A823-5B80B55C7B03>.<2> waiting for setup of Connection 1
default	09:45:22.986176+0800	hootowl	Connection 1: enabling TLS
default	09:45:22.986196+0800	hootowl	Connection 1: starting, TC(0x0)
default	09:45:22.986222+0800	hootowl	[C1 C821D611-DBE6-4952-B979-8DDAD1E7ACFE tcgbusfs.blob.core.windows.net:443 quic-connection, url: https://tcgbusfs.blob.core.windows.net/blobtcmsv/TCMSV_allavailable.json, definite, attribution: developer, context: com.apple.CFNetwork.NSURLSession.{D8375FAB-BCC3-47F6-9F42-2CD36CF9484B}{(null)}{Y}{2}{0x0} (private), proc: 1B526020-2DE0-3C65-9122-F1177549D69A, delegated upid: 0] start
default	09:45:22.986277+0800	hootowl	[C1 tcgbusfs.blob.core.windows.net:443 initial parent-flow ((null))] event: path:start @0.000s
default	09:45:22.986861+0800	hootowl	[C1 tcgbusfs.blob.core.windows.net:443 waiting parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.000s, uuid: 4EF0F4B7-61B0-4B3A-8D98-C51CFCBB1A3B
default	09:45:22.986979+0800	hootowl	[C1 tcgbusfs.blob.core.windows.net:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_connect @0.000s
default	09:45:22.986985+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C1] reporting state preparing
default	09:45:22.987031+0800	hootowl	[C1 tcgbusfs.blob.core.windows.net:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_child @0.000s
default	09:45:22.987248+0800	hootowl	[C1.1 tcgbusfs.blob.core.windows.net:443 initial path ((null))] event: path:start @0.000s
default	09:45:22.987827+0800	hootowl	[C1.1 tcgbusfs.blob.core.windows.net:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.001s, uuid: 4EF0F4B7-61B0-4B3A-8D98-C51CFCBB1A3B
default	09:45:22.987994+0800	hootowl	[C1.1 tcgbusfs.blob.core.windows.net:443 in_progress transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: transform:start @0.001s
default	09:45:22.988104+0800	hootowl	[C1.1.1 tcgbusfs.blob.core.windows.net:443 initial path ((null))] event: path:start @0.001s
default	09:45:22.988353+0800	hootowl	[C1.1.1 tcgbusfs.blob.core.windows.net:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.002s, uuid: BDAC7359-EDBA-4B51-8BBA-C231C76B9C2A
default	09:45:22.988414+0800	hootowl	[C1.1.1 tcgbusfs.blob.core.windows.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:start_dns @0.002s
default	09:45:22.988440+0800	hootowl	[0x148270f00] activating connection: mach=true listener=false peer=false name=com.apple.dnssd.service
default	09:45:22.991643+0800	hootowl	[0x148271180] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	09:45:22.991669+0800	hootowl	Task <80D33321-F751-4689-823A-9070C09CBDD2>.<1> setting up Connection 1
default	09:45:22.995719+0800	hootowl	    SessionCore_Create.mm:99    Created session 0x148358180 with ID: 0x77c67d3
default	09:45:23.001435+0800	hootowl	[0x1482712c0] activating connection: mach=true listener=false peer=false name=com.apple.coremedia.routediscoverer.xpc
default	09:45:23.001465+0800	hootowl	<<<< AVInputDeviceDiscoverySession >>>> -[AVInputDeviceDiscoverySession setFastDiscoveryEnabled:]: called (session=0x1481bf000, setFastDiscoveryEnabled=NO)
default	09:45:23.001481+0800	hootowl	<<<< AVInputDeviceDiscoverySession (FigRouteDiscoverer) >>>> -[AVFigRouteDiscovererInputDeviceDiscoverySessionImpl inputDeviceDiscoverySessionFastDiscoveryDidChange:]: Setting fastDiscoveryEnabled to NO (client: hootowl) for session=0x148304870
default	09:45:23.003168+0800	hootowl	<<<< AVOutputDeviceDiscoverySession >>>> -[AVOutputDeviceDiscoverySession setFastDiscoveryEnabled:]: called (session=0x148358290, setFastDiscoveryEnabled=NO)
default	09:45:23.003731+0800	hootowl	<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> -[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl outputDeviceDiscoverySessionFastDiscoveryDidChange:]: Setting fastDiscoveryEnabled to NO (client: hootowl) for session=0x148358290
default	09:45:23.003806+0800	hootowl	Municipal+Cyclops 93
🎨 model refreshed — obs:49424s car:2 thread:main 🆔 8064324136773232350
default	09:45:23.004256+0800	hootowl	ATAudioSessionClientImpl.mm:134   initWithSession
default	09:45:23.004307+0800	hootowl	ATAudioSessionClientImpl.mm:172   setClientConfiguration
default	09:45:23.004336+0800	hootowl	ATAudioSessionClientImpl.mm:193   No Interruption listener provided
default	09:45:23.004359+0800	hootowl	Municipal+Cyclops 93
🎨 model refreshed — obs:49424s car:2 thread:main 🆔 8064324136773232350
default	09:45:23.013696+0800	hootowl	Municipal+Cyclops 93
🎨 model refreshed — obs:49424s car:2 thread:main 🆔 8064324136773232350
default	09:45:23.015003+0800	hootowl	nw_endpoint_resolver_update [C1.1.1 tcgbusfs.blob.core.windows.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Adding endpoint handler for 20.150.22.100:443
default	09:45:23.015290+0800	hootowl	[C1.1.1 tcgbusfs.blob.core.windows.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:receive_dns @0.028s
default	09:45:23.015649+0800	hootowl	[C1.1.1.1 20.150.22.100:443 initial path ((null))] event: path:start @0.029s
default	09:45:23.016139+0800	hootowl	[C1.1.1.1 20.150.22.100:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.029s, uuid: B8A11390-9624-446D-B4E0-95DD59AACEAC
default	09:45:23.016290+0800	hootowl	[C1.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_nexus @0.029s
default	09:45:23.016654+0800	hootowl	[C1.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:receive_nexus @0.030s
default	09:45:23.017007+0800	hootowl	user_tcp_init_all_block_invoke g_tcp_nw_assert_context is false value -1
default	09:45:23.018168+0800	hootowl	[C1.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_connect @0.031s
default	09:45:23.018404+0800	hootowl	tcp_output [C1.1.1.1:3] flags=[SEC] seq=3673465353, ack=0, win=65535 state=SYN_SENT rcv_nxt=0, snd_una=3673465353
default	09:45:23.115663+0800	hootowl	tcp_input [C1.1.1.1:3] flags=[S.E] seq=4177267291, ack=3673465354, win=65535 state=SYN_SENT rcv_nxt=0, snd_una=3673465353
default	09:45:23.115684+0800	hootowl	nw_flow_connected [C1.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Transport protocol connected (tcp)
default	09:45:23.115781+0800	hootowl	[C1.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_transport @0.129s
default	09:45:23.116270+0800	hootowl	boringssl_session_apply_protocol_options_for_transport_block_invoke_2(2367) [C1.1.1.1:2][0x148289be0] TLS configured [server(0) min_version(0x0303) max_version(0x0304) name(tcgbusfs.blob.core.windows.net) tickets(false) false_start(false) enforce_ev(false) enforce_ats(false) ats_non_pfs_ciphersuite_allowed(false) cc_mode_enforced(false) ech(false) pqtls(true), pake(false) skip_ats_trust(false)]
default	09:45:23.116293+0800	hootowl	boringssl_context_info_handler(2806) [C1.1.1.1:2][0x148289be0] Client handshake started
default	09:45:23.116379+0800	hootowl	boringssl_context_info_handler(2823) [C1.1.1.1:2][0x148289be0] Client handshake state: TLS client enter_early_data
default	09:45:23.116445+0800	hootowl	boringssl_context_info_handler(2823) [C1.1.1.1:2][0x148289be0] Client handshake state: TLS client read_server_hello
default	09:45:23.125919+0800	hootowl	kExcludedFromBackupXattrName set on path: /var/mobile/Containers/Data/Application/9C61D988-8BEB-42B6-A397-1E3A058F7BB4/Library/Application Support/GoogleMobileAds/Settings
default	09:45:23.214195+0800	hootowl	[Default] Finished iterating transaction batches
default	09:45:23.219501+0800	hootowl	[0x148270a00] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	09:45:23.219559+0800	hootowl	AAFService connection invalidated
default	09:45:23.221004+0800	hootowl	[0x148270a00] activating connection: mach=true listener=false peer=false name=com.apple.storekitd
default	09:45:23.222260+0800	hootowl	kExcludedFromBackupXattrName set on path: /var/mobile/Containers/Data/Application/9C61D988-8BEB-42B6-A397-1E3A058F7BB4/Library/Application Support/GoogleMobileAds/storage
default	09:45:23.224006+0800	hootowl	cannot migrate AudioUnit assets for current process
default	09:45:23.322026+0800	hootowl	[Default] Finished iterating transaction batches
default	09:45:23.322206+0800	hootowl	boringssl_context_info_handler(2823) [C1.1.1.1:2][0x148289be0] Client handshake state: TLS 1.3 client read_hello_retry_request
default	09:45:23.322251+0800	hootowl	kExcludedFromBackupXattrName set on path: /var/mobile/Containers/Data/Application/9C61D988-8BEB-42B6-A397-1E3A058F7BB4/Library/Application Support/GoogleMobileAds/AdapterSettings
default	09:45:23.322942+0800	hootowl	boringssl_context_info_handler(2823) [C1.1.1.1:2][0x148289be0] Client handshake state: TLS 1.3 client send_second_client_hello
default	09:45:23.322992+0800	hootowl	boringssl_context_info_handler(2823) [C1.1.1.1:2][0x148289be0] Client handshake state: TLS 1.3 client read_server_hello
default	09:45:23.323220+0800	hootowl	[0x148271540] activating connection: mach=true listener=false peer=false name=com.apple.lsd.advertisingidentifiers
default	09:45:23.323806+0800	hootowl	[0x148270a00] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	09:45:23.324132+0800	hootowl	AAFService connection invalidated
default	09:45:23.324208+0800	hootowl	Registering for 'transactionsupdated' daemon notification
default	09:45:23.324232+0800	hootowl	Requesting container lookup; class = 13, identifier = (null), group_identifier = systemgroup.com.apple.configurationprofiles, create = 1, temp = 0, euid = 501, uid = 501
default	09:45:23.325126+0800	hootowl	_container_query_get_result_at_index: success
default	09:45:23.325150+0800	hootowl	container_system_group_path_for_identifier: success
default	09:45:23.325158+0800	hootowl	Got system group container path from MCM for systemgroup.com.apple.configurationprofiles: /private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles
default	09:45:23.334393+0800	hootowl	[0x1482717c0] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	09:45:23.396816+0800	hootowl	[C:1] Alloc com.apple.frontboard.systemappservices
default	09:45:23.396898+0800	hootowl	[0x148271900] activating connection: mach=false listener=false peer=false name=(anonymous)
default	09:45:23.399657+0800	hootowl	boringssl_context_info_handler(2823) [C1.1.1.1:2][0x148289be0] Client handshake state: TLS 1.3 client read_encrypted_extensions
default	09:45:23.401068+0800	hootowl	boringssl_context_info_handler(2823) [C1.1.1.1:2][0x148289be0] Client handshake state: TLS 1.3 client read_certificate_request
default	09:45:23.401220+0800	hootowl	boringssl_context_info_handler(2823) [C1.1.1.1:2][0x148289be0] Client handshake state: TLS 1.3 client read_server_certificate
default	09:45:23.401302+0800	hootowl	boringssl_context_info_handler(2823) [C1.1.1.1:2][0x148289be0] Client handshake state: TLS 1.3 client read_server_certificate_verify
default	09:45:23.511137+0800	hootowl	Creating new assertion because there is no existing background assertion.
default	09:45:23.511261+0800	hootowl	Creating new background assertion
default	09:45:23.511272+0800	hootowl	Created new background assertion <BKSProcessAssertion: 0x1482b98b0>
default	09:45:23.511435+0800	hootowl	    AVAudioSession_iOS.mm:996   Activated session 0x77c67d3
default	09:45:23.511604+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c67d3 posting AVAudioSessionAvailableOutputsChangeNotification
default	09:45:23.512185+0800	hootowl	created connimpl 0x1482cc1e0: <connection: 0x148271e00> { name = com.apple.audio.AudioQueueServer, listener = false, pid = 0, euid = 4294967295, egid = 4294967295, asid = 4294967295 }
default	09:45:23.512229+0800	hootowl	               AQ_API.cpp:58    client conn <connection: 0x148271e00> { name = com.apple.audio.AudioQueueServer, listener = false, pid = 0, euid = 4294967295, egid = 4294967295, asid = 4294967295 }
default	09:45:23.512276+0800	hootowl	[0x148271e00] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioQueueServer
default	09:45:23.512367+0800	hootowl	Incrementing reference count for background assertion <BKSProcessAssertion: 0x1482b98b0>
default	09:45:23.512545+0800	hootowl	Created background task <_UIBackgroundTaskInfo: 0x1481ca740>: taskID = 1, taskName = Launch Background Task for Coalescing, creationTime = 771914 (elapsed = 0).
default	09:45:23.512593+0800	hootowl	Realizing settings extension _UIApplicationSceneKeyboardSettings on FBSSceneSettings
default	09:45:23.513129+0800	hootowl	Realizing settings extension <_UISceneOcclusionSettings> on FBSSceneSettings
default	09:45:23.513694+0800	hootowl	Realizing settings extension <_UISceneInterfaceProtectionSettings> on FBSSceneSettings
default	09:45:23.514440+0800	hootowl	Realizing settings extension _UISceneLayoutPreferencesHostSettingsExtension on FBSSceneSettings
default	09:45:23.514682+0800	hootowl	Realizing settings extension _UISceneSafeAreaSettingsExtension on FBSSceneSettings
default	09:45:23.515171+0800	hootowl	Realizing settings extension _UISceneLayoutPreferenceClientSettingsExtension on FBSSceneClientSettings
default	09:45:23.516244+0800	hootowl	Realizing settings extension <_UIHomeAffordanceHostSceneSettings> on FBSSceneSettings
default	09:45:23.516417+0800	hootowl	Realizing settings extension _UISystemShellSceneHostingEnvironmentSettings on FBSSceneSettings
default	09:45:23.516474+0800	hootowl	Realizing settings extension _UISceneRenderingEnvironmentSettings on FBSSceneSettings
default	09:45:23.516673+0800	hootowl	Deactivation reason added: 10; deactivation reasons: 0 -> 1024; animating application lifecycle event: 0
default	09:45:23.516804+0800	hootowl	activating monitor for service com.apple.frontboard.open
default	09:45:23.516871+0800	hootowl	activating monitor for service com.apple.frontboard.workspace-service
default	09:45:23.516928+0800	hootowl	Realizing settings extension <_UISceneRenderingEnvironmentClientSettings> on FBSSceneClientSettings
default	09:45:23.517034+0800	hootowl	FBSWorkspace registering source: com.apple.frontboard.systemappservices
default	09:45:23.517051+0800	hootowl	Realizing settings extension <_UISceneTransitioningHostSettings> on FBSSceneSettings
default	09:45:23.517366+0800	hootowl	Realizing settings extension <_UISceneFocusSystemSettings> on FBSSceneSettings
default	09:45:23.517446+0800	hootowl	FBSWorkspace connected to endpoint : <BSServiceConnectionEndpoint: 0x148ce5200; target: com.apple.frontboard.systemappservices; service: com.apple.frontboard.workspace-service>
default	09:45:23.517488+0800	hootowl	Realizing settings extension _UISceneOrientationSettingsExtension on FBSSceneSettings
default	09:45:23.517524+0800	hootowl	<FBSWorkspaceScenesClient:0x1481a6bc0 com.apple.frontboard.systemappservices> attempting immediate handshake from activate
default	09:45:23.517584+0800	hootowl	<FBSWorkspaceScenesClient:0x1481a6bc0 com.apple.frontboard.systemappservices> sent handshake
default	09:45:23.517755+0800	hootowl	Realizing settings extension _UISceneOrientationClientSettingsExtension on FBSSceneClientSettings
default	09:45:23.517848+0800	hootowl	Added observer for process assertions expiration warning: <_RBSExpirationWarningClient: 0x148ce5700>
default	09:45:23.518503+0800	hootowl	Realizing settings extension _UISceneWindowingControlClientSettings on FBSSceneClientSettings
default	09:45:23.518543+0800	hootowl	Evaluated capturing state as 0 on <UIScreen: 0x148272080> for initial
default	09:45:23.519097+0800	hootowl	Evaluated capturing state as 0 on <UIScreen: 0x148272080> for CADisplay KVO
default	09:45:23.519133+0800	hootowl	Realizing settings extension <_UISceneHostingContentSizePreferenceClientSettings> on FBSSceneClientSettings
default	09:45:23.519221+0800	hootowl	Realizing settings extension _UISceneHostingTraitCollectionPropagationSettings on FBSSceneSettings
default	09:45:23.519934+0800	hootowl	Realizing settings extension <_UISceneHostingSheetPresentationSettings> on FBSSceneSettings
default	09:45:23.520255+0800	hootowl	Realizing settings extension <_UISceneHostingSheetPresentationClientSettings> on FBSSceneClientSettings
default	09:45:23.520360+0800	hootowl	Realizing settings extension <_UISceneHostingEventDeferringSettings> on FBSSceneSettings
default	09:45:23.520884+0800	hootowl	Realizing settings extension <UIKit__UITypedKeyValueSceneSettings> on FBSSceneSettings
default	09:45:23.520982+0800	hootowl	Realizing settings extension <UIKit__UITypedKeyValueSceneSettings> on FBSSceneClientSettings
default	09:45:23.521178+0800	hootowl	Realizing settings extension <_UISceneHostingViewControllerPreferencePropagationClientSettings> on FBSSceneClientSettings
default	09:45:23.521428+0800	hootowl	Realizing settings extension <_UISceneZoomTransitionSettings> on FBSSceneSettings
default	09:45:23.522726+0800	hootowl	Realizing settings extension FBSSceneSettingsCore on FBSSceneSettings
default	09:45:23.524225+0800	hootowl	Realizing settings extension FBSSceneClientSettingsCore on FBSSceneClientSettings
default	09:45:23.525049+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c67d3 posting AVAudioSessionAvailableInputsChangeNotification
default	09:45:23.525129+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c67d3 posting AVAudioSessionAvailableOutputsChangeNotification
default	09:45:23.525161+0800	hootowl	boringssl_context_evaluate_trust_async(2249) [C1.1.1.1:2][0x148289be0] Performing external trust evaluation
default	09:45:23.525286+0800	hootowl	boringssl_context_evaluate_trust_async_external(2234) [C1.1.1.1:2][0x148289be0] Asyncing for external verify block
default	09:45:23.525430+0800	hootowl	UIMutableApplicationSceneSettings setting counterpart class: UIApplicationSceneSettings
default	09:45:23.525471+0800	hootowl	UIMutableApplicationSceneClientSettings setting counterpart class: UIApplicationSceneClientSettings
default	09:45:23.525522+0800	hootowl	Realizing settings extension FBSSceneTransitionContextCore on FBSSceneTransitionContext
default	09:45:23.527719+0800	hootowl	Read CategoryName: per-app = 1, category name = (null)
default	09:45:23.528222+0800	hootowl	Read CategoryName: per-app = 0, category name = UICTContentSizeCategoryXXXL
default	09:45:23.528309+0800	hootowl	Connection 1: asked to evaluate TLS Trust
default	09:45:23.528575+0800	hootowl	Task <80D33321-F751-4689-823A-9070C09CBDD2>.<1> auth completion disp=1 cred=0x0
default	09:45:23.528767+0800	hootowl	(Trust 0x148269e00) No pending evals, starting
default	09:45:23.529472+0800	hootowl	System Keychain Always Supported set via feature flag to disabled
default	09:45:23.529503+0800	hootowl	[0x148272800] activating connection: mach=true listener=false peer=false name=com.apple.trustd
default	09:45:23.529617+0800	hootowl	[0x148272940] activating connection: mach=true listener=false peer=false name=com.apple.trustd
default	09:45:23.529719+0800	hootowl	(Trust 0x148269e00) Completed async eval kickoff
default	09:45:23.546531+0800	hootowl	(Trust 0x148269e00) trustd returned 4
default	09:45:23.547202+0800	hootowl	System Trust Evaluation yielded status(0)
default	09:45:23.547684+0800	hootowl	(Trust 0x148269680) No pending evals, starting
default	09:45:23.548645+0800	hootowl	[0x148272a80] activating connection: mach=true listener=false peer=false name=com.apple.trustd
default	09:45:23.548711+0800	hootowl	(Trust 0x148269680) Completed async eval kickoff
default	09:45:23.549592+0800	hootowl	[0x148272940] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	09:45:23.555433+0800	hootowl	(Trust 0x148269680) trustd returned 4
default	09:45:23.555529+0800	hootowl	Connection 1: TLS Trust result 0
default	09:45:23.555551+0800	hootowl	boringssl_context_evaluate_trust_async_external_block_invoke_3(2148) [C1.1.1.1:2][0x148289be0] Returning from external verify block with result: true
default	09:45:23.555700+0800	hootowl	boringssl_context_certificate_verify_callback(2430) [C1.1.1.1:2][0x148289be0] Certificate verification result: OK
default	09:45:23.555706+0800	hootowl	boringssl_context_info_handler(2823) [C1.1.1.1:2][0x148289be0] Client handshake state: TLS 1.3 client read_server_finished
default	09:45:23.555790+0800	hootowl	boringssl_context_info_handler(2823) [C1.1.1.1:2][0x148289be0] Client handshake state: TLS 1.3 client send_end_of_early_data
default	09:45:23.555799+0800	hootowl	boringssl_context_info_handler(2823) [C1.1.1.1:2][0x148289be0] Client handshake state: TLS 1.3 client send_client_encrypted_extensions
default	09:45:23.555807+0800	hootowl	boringssl_context_info_handler(2823) [C1.1.1.1:2][0x148289be0] Client handshake state: TLS 1.3 client send_client_certificate
default	09:45:23.555814+0800	hootowl	boringssl_context_info_handler(2823) [C1.1.1.1:2][0x148289be0] Client handshake state: TLS 1.3 client complete_second_flight
default	09:45:23.555829+0800	hootowl	boringssl_context_info_handler(2823) [C1.1.1.1:2][0x148289be0] Client handshake state: TLS 1.3 client done
default	09:45:23.555941+0800	hootowl	boringssl_context_info_handler(2823) [C1.1.1.1:2][0x148289be0] Client handshake state: TLS client finish_client_handshake
default	09:45:23.555949+0800	hootowl	boringssl_context_info_handler(2823) [C1.1.1.1:2][0x148289be0] Client handshake state: TLS client done
default	09:45:23.555957+0800	hootowl	boringssl_context_info_handler(2812) [C1.1.1.1:2][0x148289be0] Client handshake done
default	09:45:23.557951+0800	hootowl	nw_protocol_boringssl_signal_connected(895) [C1.1.1.1:2][0x148289be0] TLS connected [server(0) version(0x0304) ciphersuite(TLS_AES_256_GCM_SHA384) group(0x0018) signature_alg(0x0804) alpn(nil) resumed(0) offered_ticket(0) in_early_data(0) early_data_accepted(0) false_started(0) ocsp_received(1) sct_received(0) connect_time(440ms) flight_time(282ms) rtt(205ms) write_stalls(0) read_stalls(10) pake(0x0000)]
default	09:45:23.558000+0800	hootowl	nw_flow_connected [C1.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (CFNetworkConnection-4283075305)
default	09:45:23.558062+0800	hootowl	[C1.1.1.1 20.150.22.100:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.570s
default	09:45:23.558115+0800	hootowl	[C1.1.1 tcgbusfs.blob.core.windows.net:443 ready resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.570s
default	09:45:23.558186+0800	hootowl	[C1.1 tcgbusfs.blob.core.windows.net:443 ready transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.570s
default	09:45:23.558238+0800	hootowl	[C1.1.1.1 20.150.22.100:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.570s
default	09:45:23.558263+0800	hootowl	[C1.1.1 tcgbusfs.blob.core.windows.net:443 ready resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.570s
default	09:45:23.558279+0800	hootowl	[C1.1 tcgbusfs.blob.core.windows.net:443 ready transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.570s
default	09:45:23.558295+0800	hootowl	nw_flow_connected [C1 20.150.22.100:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (endpoint_flow)
default	09:45:23.558316+0800	hootowl	[C1 20.150.22.100:443 ready parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_connect @0.571s
error	09:45:23.669281+0800	hootowl	138	assessFences(l2d:)	no fences are availabe
default	09:45:23.669663+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C1] reporting state ready
default	09:45:23.669750+0800	hootowl	[C1 20.150.22.100:443 ready parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.683s
default	09:45:23.669764+0800	hootowl	nw_connection_send_viability_changed_on_nw_queue [C1] viability_changed_handler(true)
default	09:45:23.670151+0800	hootowl	[0x148272a80] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	09:45:23.670372+0800	hootowl	Connection 1: connected successfully
default	09:45:23.670378+0800	hootowl	Connection 1: TLS handshake complete
default	09:45:23.670429+0800	hootowl	Connection 1: ready C(N) E(N)
default	09:45:23.670510+0800	hootowl	Task <80D33321-F751-4689-823A-9070C09CBDD2>.<1> now using Connection 1
default	09:45:23.670576+0800	hootowl	Connection 1: received viability advisory(Y)
default	09:45:23.670711+0800	hootowl	Task <80D33321-F751-4689-823A-9070C09CBDD2>.<1> sent request, body N 0
default	09:45:23.670869+0800	hootowl	Connection 2: enabling TLS
default	09:45:23.670914+0800	hootowl	Connection 2: starting, TC(0x0)
default	09:45:23.670929+0800	hootowl	[C2 7162D2BB-8A88-4463-93E0-DE8625890B51 tcgbusfs.blob.core.windows.net:443 tcp, url: https://tcgbusfs.blob.core.windows.net/blobtcmsv/TCMSV_alldesc.json, tls, definite, attribution: developer, context: com.apple.CFNetwork.NSURLSession.{D8375FAB-BCC3-47F6-9F42-2CD36CF9484B}{(null)}{Y}{2}{0x0} (private), proc: 1B526020-2DE0-3C65-9122-F1177549D69A, delegated upid: 0] start
default	09:45:23.671020+0800	hootowl	[C2 tcgbusfs.blob.core.windows.net:443 initial parent-flow ((null))] event: path:start @0.000s
default	09:45:23.671262+0800	hootowl	[C2 tcgbusfs.blob.core.windows.net:443 waiting parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.000s, uuid: BDAC7359-EDBA-4B51-8BBA-C231C76B9C2A
default	09:45:23.671369+0800	hootowl	[C2 tcgbusfs.blob.core.windows.net:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_connect @0.000s
default	09:45:23.671390+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C2] reporting state preparing
default	09:45:23.671459+0800	hootowl	[C2 tcgbusfs.blob.core.windows.net:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_child @0.000s
default	09:45:23.671570+0800	hootowl	[C2.1 tcgbusfs.blob.core.windows.net:443 initial path ((null))] event: path:start @0.000s
default	09:45:23.671809+0800	hootowl	[C2.1 tcgbusfs.blob.core.windows.net:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.000s, uuid: BDAC7359-EDBA-4B51-8BBA-C231C76B9C2A
default	09:45:23.671854+0800	hootowl	[C2.1 tcgbusfs.blob.core.windows.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:start_dns @0.000s
default	09:45:23.689070+0800	hootowl	Task <6CD5524D-F067-4C09-A823-5B80B55C7B03>.<2> setting up Connection 2
default	09:45:23.689104+0800	hootowl	nw_endpoint_resolver_update [C2.1 tcgbusfs.blob.core.windows.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Adding endpoint handler for 20.150.22.100:443
default	09:45:23.689181+0800	hootowl	[C2.1 tcgbusfs.blob.core.windows.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:receive_dns @0.018s
default	09:45:23.689237+0800	hootowl	[C2.1.1 20.150.22.100:443 initial path ((null))] event: path:start @0.018s
default	09:45:23.689312+0800	hootowl	[C2.1.1 20.150.22.100:443 waiting path (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.018s, uuid: B8A11390-9624-446D-B4E0-95DD59AACEAC
default	09:45:23.689342+0800	hootowl	[C2.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_nexus @0.018s
default	09:45:23.690220+0800	hootowl	[C2.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:receive_nexus @0.018s
default	09:45:23.690682+0800	hootowl	[C2.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_connect @0.019s
default	09:45:23.690830+0800	hootowl	tcp_output [C2.1.1:3] flags=[SEC] seq=3020160393, ack=0, win=65535 state=SYN_SENT rcv_nxt=0, snd_una=3020160393
default	09:45:23.768080+0800	hootowl	Task <80D33321-F751-4689-823A-9070C09CBDD2>.<1> received response, status 200 content K
default	09:45:23.773794+0800	hootowl	tcp_input [C2.1.1:3] flags=[S.E] seq=2412420305, ack=3020160394, win=65535 state=SYN_SENT rcv_nxt=0, snd_una=3020160393
default	09:45:23.773868+0800	hootowl	nw_flow_connected [C2.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Transport protocol connected (tcp)
default	09:45:23.773973+0800	hootowl	[C2.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_transport @0.097s
default	09:45:23.775181+0800	hootowl	boringssl_session_apply_protocol_options_for_transport_block_invoke_2(2367) [C2.1.1:2][0x14828b760] TLS configured [server(0) min_version(0x0303) max_version(0x0304) name(tcgbusfs.blob.core.windows.net) tickets(false) false_start(false) enforce_ev(false) enforce_ats(false) ats_non_pfs_ciphersuite_allowed(false) cc_mode_enforced(false) ech(false) pqtls(true), pake(false) skip_ats_trust(false)]
default	09:45:23.775243+0800	hootowl	boringssl_context_info_handler(2806) [C2.1.1:2][0x14828b760] Client handshake started
default	09:45:23.775269+0800	hootowl	boringssl_context_info_handler(2823) [C2.1.1:2][0x14828b760] Client handshake state: TLS client enter_early_data
default	09:45:23.775315+0800	hootowl	boringssl_context_info_handler(2823) [C2.1.1:2][0x14828b760] Client handshake state: TLS client read_server_hello
fault	09:45:23.778736+0800	hootowl	__delegate_identifier__:Performance Diagnostics__:::____message__:{"message":"Performing I/O on the main thread can cause slow launches.","antipattern trigger":"dlopen","message type":"suppressable","issue type":4,"category type":17,"subcategory type":3,"show in console":"0"}'FF 77 AB D1 15 84 38 80 88 51 C0 F3 AD 15 F7 7D 58 9D 00 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 A0 73 00 00 FF 77 AB D1 15 84 38 80 88 51 C0 F3 AD 15 F7 7D D4 9A 00 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 A0 73 00 00 FF 77 AB D1 15 84 38 80 88 51 C0 F3 AD 15 F7 7D 24 41 00 00 FF 77 AB D1 15 84 38 80 88 51 C0 F3 AD 15 F7 7D 44 40 00 00 FF 77 AB D1 15 84 38 80 88 51 C0 F3 AD 15 F7 7D B0 3E 00 00 FF 77 AB D1 15 84 38 80 88 51 C0 F3 AD 15 F7 7D 4C 37 00 00 FF 77 AB D1 15 84 38 80 88 51 C0 F3 AD 15 F7 7D 3C 31 00 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 3C 63 0D 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 4C 76 34 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 44 66 34 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 FC 57 34 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 48 57 34 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 A0 73 00 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 54 58 34 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 54 82 36 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 AC 8C 36 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 38 CC 02 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 14 8C 36 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 C0 8C 36 00 0F 8D 35 B6 55 6F 3E 34 8E AA 80 AB 54 04 7D C5 1C 4C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
default	09:45:23.930449+0800	hootowl	boringssl_context_info_handler(2823) [C2.1.1:2][0x14828b760] Client handshake state: TLS 1.3 client read_hello_retry_request
default	09:45:23.930875+0800	hootowl	boringssl_context_info_handler(2823) [C2.1.1:2][0x14828b760] Client handshake state: TLS 1.3 client send_second_client_hello
default	09:45:23.930953+0800	hootowl	boringssl_context_info_handler(2823) [C2.1.1:2][0x14828b760] Client handshake state: TLS 1.3 client read_server_hello
fault	09:45:23.933918+0800	hootowl	__delegate_identifier__:Performance Diagnostics__:::____message__:{"message":"Performing I/O on the main thread can cause hangs.","antipattern trigger":"-[NSData initWithContentsOfFile:]","message type":"suppressable","issue type":1,"category type":17,"subcategory type":3,"show in console":"0"}'73 84 1A A3 BF DD 32 2D 8D C2 E5 18 5A 14 DE E1 FC 86 18 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 58 74 30 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 6C 6E 30 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 70 F4 2F 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 C0 F3 2F 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 A0 73 00 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 CC F4 2F 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 C8 83 36 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 AC 8C 36 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 38 CC 02 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 14 8C 36 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 C0 8C 36 00 0F 8D 35 B6 55 6F 3E 34 8E AA 80 AB 54 04 7D C5 1C 4C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
default	09:45:24.025893+0800	hootowl	boringssl_context_info_handler(2823) [C2.1.1:2][0x14828b760] Client handshake state: TLS 1.3 client read_encrypted_extensions
default	09:45:24.026129+0800	hootowl	boringssl_context_info_handler(2823) [C2.1.1:2][0x14828b760] Client handshake state: TLS 1.3 client read_certificate_request
default	09:45:24.026179+0800	hootowl	boringssl_context_info_handler(2823) [C2.1.1:2][0x14828b760] Client handshake state: TLS 1.3 client read_server_certificate
default	09:45:24.026205+0800	hootowl	boringssl_context_info_handler(2823) [C2.1.1:2][0x14828b760] Client handshake state: TLS 1.3 client read_server_certificate_verify
default	09:45:24.026534+0800	hootowl	boringssl_context_evaluate_trust_async(2249) [C2.1.1:2][0x14828b760] Performing external trust evaluation
default	09:45:24.027364+0800	hootowl	boringssl_context_evaluate_trust_async_external(2234) [C2.1.1:2][0x14828b760] Asyncing for external verify block
default	09:45:24.027473+0800	hootowl	Connection 2: asked to evaluate TLS Trust
default	09:45:24.027721+0800	hootowl	Task <6CD5524D-F067-4C09-A823-5B80B55C7B03>.<2> auth completion disp=1 cred=0x0
default	09:45:24.028003+0800	hootowl	(Trust 0x14826aa00) No pending evals, starting
fault	09:45:24.028107+0800	hootowl	__delegate_identifier__:Performance Diagnostics__:::____message__:{"message":"Performing I/O on the main thread can cause slow launches.","antipattern trigger":"-[NSData initWithContentsOfFile:]","message type":"suppressable","issue type":4,"category type":17,"subcategory type":3,"show in console":"0"}'73 84 1A A3 BF DD 32 2D 8D C2 E5 18 5A 14 DE E1 FC 86 18 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 58 74 30 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 6C 6E 30 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 70 F4 2F 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 C0 F3 2F 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 A0 73 00 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 CC F4 2F 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 C8 83 36 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 AC 8C 36 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 38 CC 02 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 14 8C 36 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 C0 8C 36 00 0F 8D 35 B6 55 6F 3E 34 8E AA 80 AB 54 04 7D C5 1C 4C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
default	09:45:24.028445+0800	hootowl	[0x148272580] activating connection: mach=true listener=false peer=false name=com.apple.trustd
default	09:45:24.028655+0800	hootowl	(Trust 0x14826aa00) Completed async eval kickoff
default	09:45:24.030163+0800	hootowl	[FBSDisplaySource 1-1] silently connecting raw configuration: <FBSDisplayConfiguration: 0x1481de800; Main; mode: "393x852@3x 120Hz p3 SDR">
default	09:45:24.031622+0800	hootowl	Display settings after update from FB configuration: AXMDisplay<0x148d40150>: Backing:FrontBoardServices (dynamic) Name:LCD scale:3 size:[1179.00 2556.00] orientation:0 (AXMPhysicalDisplayOrientationPortrait) refBounds:[0.00 0.00 393.00 852.00] deepColor:1
default	09:45:24.031758+0800	hootowl	Display settings after update from CADisplay.mainDisplay: AXMDisplay<0x148d40690>: Backing:CoreAnimation Name:LCD scale:3 size:[1179.00 2556.00] orientation:0 (AXMPhysicalDisplayOrientationPortrait) refBounds:[0.00 0.00 393.00 852.00] deepColor:0
default	09:45:24.063874+0800	hootowl	Registering for test daemon availability notify post.
default	09:45:24.063970+0800	hootowl	notify_get_state check indicated test daemon not ready.
default	09:45:24.063976+0800	hootowl	notify_get_state check indicated test daemon not ready.
default	09:45:24.063988+0800	hootowl	notify_get_state check indicated test daemon not ready.
default	09:45:24.064207+0800	hootowl	Deactivation reason added: 11; deactivation reasons: 1024 -> 3072; animating application lifecycle event: 0
default	09:45:24.064294+0800	hootowl	Deactivation reason removed: 10; deactivation reasons: 3072 -> 2048; animating application lifecycle event: 0
default	09:45:24.064471+0800	hootowl	{"msg":"CLLocationManager", "event":"activity", "_cmd":"onClientEventRegistration:", "self":"0x1483580a0", "clientKey":"icom.sharkda.hootowl:"}
default	09:45:24.064699+0800	hootowl	{"msg":"#CLLocationManager invoking #delegate", "self":"0x1483580a0", "delegate":"0x148270140", "selector":"locationManagerDidChangeAuthorization:", "authorizationStatus":"AuthorizedWhenInUse", "limitsPrecision":0, "isAuthorizedForWidgetUpdates":0}
default	09:45:24.064953+0800	hootowl	Event Timing Profile for Touch: ok, path="/System/Library/EventTimingProfiles/D83.Touch.plist"
default	09:45:24.064960+0800	hootowl	Event Timing Profile for Pencil: not found, path="/System/Library/EventTimingProfiles/D83.Pencil.plist"
default	09:45:24.064975+0800	hootowl	Selected display: name=LCD (primary), id=1
default	09:45:24.065232+0800	hootowl	[0x1482726c0] activating connection: mach=true listener=false peer=false name=com.apple.storekitd
default	09:45:24.066323+0800	hootowl	alm_acquire_pageins_recording_assertion: acquired pageins recording assertion!
default	09:45:24.066349+0800	hootowl	Deactivation reason added: 5; deactivation reasons: 2048 -> 2080; animating application lifecycle event: 1
default	09:45:24.067251+0800	hootowl	Should send trait collection or coordinate space update, interface style 1 -> 1, <UIWindowScene: 0x148378200> (83FF55F6-7B28-4BFD-8825-33CB43E5D162)
default	09:45:24.079576+0800	hootowl	Not push traits update to screen for new style 1, <UIWindowScene: 0x148378200> (83FF55F6-7B28-4BFD-8825-33CB43E5D162)
default	09:45:24.096688+0800	hootowl	Initializing: <_UIHomeAffordanceSceneNotifier: 0x148e9ad10>; with scene: <UIWindowScene: 0x148378200>
default	09:45:24.096743+0800	hootowl	0x1482eced0 setDelegate:<0x1482ecde0 _UIBacklightEnvironment> hasDelegate:YES for environment:sceneID:com.sharkda.hootowl-83FF55F6-7B28-4BFD-8825-33CB43E5D162
default	09:45:24.096869+0800	hootowl	Not push traits update to screen for new style 1, <UIWindowScene: 0x148378200> (83FF55F6-7B28-4BFD-8825-33CB43E5D162)
default	09:45:24.096913+0800	hootowl	[0x148e9b4f0] Initialized with scene: <UIWindowScene: 0x148378200>; behavior: <_UIEventDeferringBehavior_iOS: 0x148e44de0>; availableForProcess: 1, systemShellManagesKeyboardFocus: 1
default	09:45:24.097426+0800	hootowl	[C:2] Alloc com.apple.backboard.hid-services.xpc
default	09:45:24.097449+0800	hootowl	[0x148273980] activating connection: mach=false listener=false peer=false name=(anonymous)
default	09:45:24.097456+0800	hootowl	policyStatus:<BKSHIDEventDeliveryPolicyObserver: 0x148e4c060; process scope; status: none> was:none
default	09:45:24.097476+0800	hootowl	BKSHIDEventObserver - connection activation
default	09:45:24.097481+0800	hootowl	Setting default evaluation strategy for UIUserInterfaceIdiomPhone to LastOneWins
default	09:45:24.097948+0800	hootowl	Not push traits update to screen for new style 1, <UIWindowScene: 0x148378200> (83FF55F6-7B28-4BFD-8825-33CB43E5D162)
default	09:45:24.098763+0800	hootowl	Not push traits update to screen for new style 1, <UIWindowScene: 0x148378200> (83FF55F6-7B28-4BFD-8825-33CB43E5D162)
default	09:45:24.103632+0800	hootowl	Not push traits update to screen for new style 1, <UIWindowScene: 0x148378200> (83FF55F6-7B28-4BFD-8825-33CB43E5D162)
default	09:45:24.109440+0800	hootowl	(Trust 0x14826aa00) trustd returned 4
default	09:45:24.111696+0800	hootowl	System Trust Evaluation yielded status(0)
default	09:45:24.111818+0800	hootowl	(Trust 0x14826a880) No pending evals, starting
default	09:45:24.112782+0800	hootowl	[0x148eb8640] activating connection: mach=true listener=false peer=false name=com.apple.trustd
default	09:45:24.112986+0800	hootowl	(Trust 0x14826a880) Completed async eval kickoff
default	09:45:24.113249+0800	hootowl	[0x148272580] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	09:45:24.122375+0800	hootowl	(Trust 0x14826a880) trustd returned 4
default	09:45:24.122716+0800	hootowl	Connection 2: TLS Trust result 0
default	09:45:24.122730+0800	hootowl	boringssl_context_evaluate_trust_async_external_block_invoke_3(2148) [C2.1.1:2][0x14828b760] Returning from external verify block with result: true
default	09:45:24.123044+0800	hootowl	boringssl_context_certificate_verify_callback(2430) [C2.1.1:2][0x14828b760] Certificate verification result: OK
default	09:45:24.123332+0800	hootowl	boringssl_context_info_handler(2823) [C2.1.1:2][0x14828b760] Client handshake state: TLS 1.3 client read_server_finished
default	09:45:24.123413+0800	hootowl	boringssl_context_info_handler(2823) [C2.1.1:2][0x14828b760] Client handshake state: TLS 1.3 client send_end_of_early_data
default	09:45:24.123437+0800	hootowl	boringssl_context_info_handler(2823) [C2.1.1:2][0x14828b760] Client handshake state: TLS 1.3 client send_client_encrypted_extensions
default	09:45:24.123536+0800	hootowl	boringssl_context_info_handler(2823) [C2.1.1:2][0x14828b760] Client handshake state: TLS 1.3 client send_client_certificate
default	09:45:24.123773+0800	hootowl	boringssl_context_info_handler(2823) [C2.1.1:2][0x14828b760] Client handshake state: TLS 1.3 client complete_second_flight
default	09:45:24.123883+0800	hootowl	boringssl_context_info_handler(2823) [C2.1.1:2][0x14828b760] Client handshake state: TLS 1.3 client done
default	09:45:24.124089+0800	hootowl	boringssl_context_info_handler(2823) [C2.1.1:2][0x14828b760] Client handshake state: TLS client finish_client_handshake
default	09:45:24.124241+0800	hootowl	boringssl_context_info_handler(2823) [C2.1.1:2][0x14828b760] Client handshake state: TLS client done
default	09:45:24.124259+0800	hootowl	boringssl_context_info_handler(2812) [C2.1.1:2][0x14828b760] Client handshake done
default	09:45:24.126981+0800	hootowl	nw_protocol_boringssl_signal_connected(895) [C2.1.1:2][0x14828b760] TLS connected [server(0) version(0x0304) ciphersuite(TLS_AES_256_GCM_SHA384) group(0x0018) signature_alg(0x0804) alpn(nil) resumed(0) offered_ticket(0) in_early_data(0) early_data_accepted(0) false_started(0) ocsp_received(1) sct_received(0) connect_time(353ms) flight_time(253ms) rtt(159ms) write_stalls(0) read_stalls(7) pake(0x0000)]
default	09:45:24.127131+0800	hootowl	nw_flow_connected [C2.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (CFNetworkConnection-4283075305)
default	09:45:24.127404+0800	hootowl	[C2.1.1 20.150.22.100:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.456s
default	09:45:24.127979+0800	hootowl	[C2.1 tcgbusfs.blob.core.windows.net:443 ready resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.456s
default	09:45:24.128123+0800	hootowl	[C2.1.1 20.150.22.100:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.456s
default	09:45:24.128150+0800	hootowl	[C2.1 tcgbusfs.blob.core.windows.net:443 ready resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.457s
default	09:45:24.128170+0800	hootowl	nw_flow_connected [C2 20.150.22.100:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (endpoint_flow)
default	09:45:24.128287+0800	hootowl	[C2 20.150.22.100:443 ready parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_connect @0.457s
default	09:45:24.128324+0800	hootowl	<UIWindowScene: 0x148378200> (83FF55F6-7B28-4BFD-8825-33CB43E5D162) Scene updated orientation preferences: none -> ( Pu Ll Lr )
default	09:45:24.130179+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C2] reporting state ready
default	09:45:24.132041+0800	hootowl	[C2 20.150.22.100:443 ready parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.458s
default	09:45:24.132100+0800	hootowl	nw_connection_send_viability_changed_on_nw_queue [C2] viability_changed_handler(true)
default	09:45:24.132184+0800	hootowl	[0x148eb8640] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	09:45:24.132343+0800	hootowl	Connection 2: connected successfully
default	09:45:24.132483+0800	hootowl	Connection 2: TLS handshake complete
default	09:45:24.132493+0800	hootowl	Connection 2: ready C(N) E(N)
default	09:45:24.132513+0800	hootowl	Task <6CD5524D-F067-4C09-A823-5B80B55C7B03>.<2> now using Connection 2
default	09:45:24.132591+0800	hootowl	Connection 2: received viability advisory(Y)
default	09:45:24.132651+0800	hootowl	Task <6CD5524D-F067-4C09-A823-5B80B55C7B03>.<2> sent request, body N 0
default	09:45:24.133440+0800	hootowl	Key window API is scene-level: YES
default	09:45:24.133490+0800	hootowl	UIWindowScene: 0x148378200: Window became key in scene: UIWindow: 0x1481fc400; contextId: 0xF4D9041F: reason: UIWindowScene: 0x148378200: Window requested to become key in scene: 0x1481fc400
default	09:45:24.133527+0800	hootowl	Key window needs update: 1; currentKeyWindowScene: 0x0; evaluatedKeyWindowScene: 0x148378200; currentApplicationKeyWindow: 0x0; evaluatedApplicationKeyWindow: 0x1481fc400; reason: UIWindowScene: 0x148378200: Window requested to become key in scene: 0x1481fc400
default	09:45:24.133588+0800	hootowl	Window did become application key: UIWindow: 0x1481fc400; contextId: 0xF4D9041F; scene identity: com.apple.frontboard.systemappservices/FBSceneManager:sceneID%3Acom.sharkda.hootowl-83FF55F6-7B28-4BFD-8825-33CB43E5D162
default	09:45:24.133640+0800	hootowl	[0x148e9b4f0] Begin local event deferring requested for token: 0x148e4c240; environments: 1; reason: UIWindowScene: 0x148378200: Begin event deferring in keyboardFocus for window: 0x1481fc400
default	09:45:24.133827+0800	hootowl	[0x148e9b4f0] [keyboardFocus] Start observing context for local target window: 0x1481fc400; contextId: 0xF4D9041F
default	09:45:24.133908+0800	hootowl	[0x148e9b4f0] [keyboardFocus] Began tracking context for local target window: 0x1481fc400; contextId: 0xF4D9041F
default	09:45:24.134217+0800	hootowl	BKSHIDEventDeliveryManager - connection activation
default	09:45:24.134694+0800	hootowl	Not push traits update to screen for new style 1, <UIWindowScene: 0x148378200> (83FF55F6-7B28-4BFD-8825-33CB43E5D162)
default	09:45:24.135396+0800	hootowl	sceneOfRecord: sceneID: sceneID:com.sharkda.hootowl-83FF55F6-7B28-4BFD-8825-33CB43E5D162  persistentID: 83FF55F6-7B28-4BFD-8825-33CB43E5D162
default	09:45:24.135421+0800	hootowl	Ignoring already applied deactivation reason: 5; deactivation reasons: 2080
default	09:45:24.135498+0800	hootowl	Deactivation reason added: 12; deactivation reasons: 2080 -> 6176; animating application lifecycle event: 1
default	09:45:24.136162+0800	hootowl	{"msg":"CLLocationManager", "event":"activity", "_cmd":"onWillEnterForeground:", "self":"0x1483580a0", "notification":"NSConcreteNotification 0x148e46b40 {name = UIApplicationWillEnterForegroundNotification; object = <_TtC7SwiftUIP33_ACC2C5639A7D76F611E170E831FCA49118SwiftUIApplication: 0x148378000>}"}
default	09:45:24.136229+0800	hootowl	Deactivation reason removed: 11; deactivation reasons: 6176 -> 4128; animating application lifecycle event: 1
default	09:45:24.136245+0800	hootowl	Realizing settings extension <_UISceneIntelligenceSupportSettings> on FBSSceneSettings
default	09:45:24.136450+0800	hootowl	establishing connection to agent
default	09:45:24.137979+0800	hootowl	[0x148d490e0] Session created.
default	09:45:24.138008+0800	hootowl	[0x148d490e0] Session created from connection [0x148f19680]
default	09:45:24.138453+0800	hootowl	[0x148f19680] activating connection: mach=true listener=false peer=false name=com.apple.uiintelligencesupport.agent
default	09:45:24.139373+0800	hootowl	Not push traits update to screen for new style 1, <UIWindowScene: 0x148378200> (83FF55F6-7B28-4BFD-8825-33CB43E5D162)
default	09:45:24.139384+0800	hootowl	[0x148d490e0] Session activated
fault	09:45:24.146173+0800	hootowl	__delegate_identifier__:Performance Diagnostics__:::____message__:{"message":"Performing I/O on the main thread can cause hangs.","antipattern trigger":"+[NSKeyedArchiver archivedDataWithRootObject:requiringSecureCoding:error:]","message type":"suppressable","issue type":1,"category type":17,"subcategory type":3,"show in console":"0"}'D4 8C 7E F8 2B B4 38 1E A7 DF B4 C6 4A 7A 2C 23 98 86 00 00 D4 8C 7E F8 2B B4 38 1E A7 DF B4 C6 4A 7A 2C 23 1C 86 00 00 DC 4F 50 56 DB E7 36 8A 99 ED A6 79 F2 C1 4F B0 00 75 02 00 DC 4F 50 56 DB E7 36 8A 99 ED A6 79 F2 C1 4F B0 30 74 02 00 DC 4F 50 56 DB E7 36 8A 99 ED A6 79 F2 C1 4F B0 CC 73 02 00 DC 4F 50 56 DB E7 36 8A 99 ED A6 79 F2 C1 4F B0 38 AB 00 00 DC 4F 50 56 DB E7 36 8A 99 ED A6 79 F2 C1 4F B0 68 5F 00 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 3C E9 22 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 54 B2 22 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 40 A2 22 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 D0 25 22 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 90 25 22 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 A0 73 00 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 2C 26 22 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 2C 84 36 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 AC 8C 36 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 38 CC 02 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 14 8C 36 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 C0 8C 36 00 0F 8D 35 B6 55 6F 3E 34 8E AA 80 AB 54 04 7D C5 1C 4C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
fault	09:45:24.149014+0800	hootowl	__delegate_identifier__:Performance Diagnostics__:::____message__:{"message":"Performing I/O on the main thread can cause slow launches.","antipattern trigger":"+[NSKeyedArchiver archivedDataWithRootObject:requiringSecureCoding:error:]","message type":"suppressable","issue type":4,"category type":17,"subcategory type":3,"show in console":"0"}'D4 8C 7E F8 2B B4 38 1E A7 DF B4 C6 4A 7A 2C 23 98 86 00 00 D4 8C 7E F8 2B B4 38 1E A7 DF B4 C6 4A 7A 2C 23 1C 86 00 00 DC 4F 50 56 DB E7 36 8A 99 ED A6 79 F2 C1 4F B0 00 75 02 00 DC 4F 50 56 DB E7 36 8A 99 ED A6 79 F2 C1 4F B0 30 74 02 00 DC 4F 50 56 DB E7 36 8A 99 ED A6 79 F2 C1 4F B0 CC 73 02 00 DC 4F 50 56 DB E7 36 8A 99 ED A6 79 F2 C1 4F B0 38 AB 00 00 DC 4F 50 56 DB E7 36 8A 99 ED A6 79 F2 C1 4F B0 68 5F 00 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 3C E9 22 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 54 B2 22 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 40 A2 22 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 D0 25 22 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 90 25 22 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 A0 73 00 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 2C 26 22 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 2C 84 36 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 AC 8C 36 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 38 CC 02 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 14 8C 36 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 C0 8C 36 00 0F 8D 35 B6 55 6F 3E 34 8E AA 80 AB 54 04 7D C5 1C 4C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
fault	09:45:24.244098+0800	hootowl	__delegate_identifier__:Performance Diagnostics__:::____message__:{"message":"Performing I/O on the main thread can cause hangs.","antipattern trigger":"-[NSBundle bundleIdentifier]","message type":"suppressable","issue type":1,"category type":17,"subcategory type":3,"show in console":"0"}'26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 54 5E 07 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 A0 73 00 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 FC 5F 07 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 E0 79 07 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 5C 87 1D 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 4C 76 1D 00 E1 18 0F C2 AA 2B 3F E3 B2 6E D4 52 27 36 44 57 18 6E 00 00 E1 18 0F C2 AA 2B 3F E3 B2 6E D4 52 27 36 44 57 AC 6D 00 00 E1 18 0F C2 AA 2B 3F E3 B2 6E D4 52 27 36 44 57 D0 8C 00 00 E1 18 0F C2 AA 2B 3F E3 B2 6E D4 52 27 36 44 57 7C 3A 00 00 E1 18 0F C2 AA 2B 3F E3 B2 6E D4 52 27 36 44 57 0C 2E 00 00 E1 18 0F C2 AA 2B 3F E3 B2 6E D4 52 27 36 44 57 AC 2F 00 00 E1 18 0F C2 AA 2B 3F E3 B2 6E D4 52 27 36 44 57 E4 90 00 00 E1 18 0F C2 AA 2B 3F E3 B2 6E D4 52 27 36 44 57 48 86 00 00 E1 18 0F C2 AA 2B 3F E3 B2 6E D4 52 27 36 44 57 C0 21 00 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 6C 6F 1D 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 C4 A2 22 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 D0 25 22 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 90 25 22 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 A0 73 00 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 2C 26 22 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 2C 84 36 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 AC 8C 36 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 38 CC 02 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 14 8C 36 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 C0 8C 36 00 0F 8D 35 B6 55 6F 3E 34 8E AA 80 AB 54 04 7D C5 1C 4C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
fault	09:45:24.248296+0800	hootowl	__delegate_identifier__:Performance Diagnostics__:::____message__:{"message":"Performing I/O on the main thread can cause slow launches.","antipattern trigger":"-[NSBundle bundleIdentifier]","message type":"suppressable","issue type":4,"category type":17,"subcategory type":3,"show in console":"0"}'26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 54 5E 07 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 A0 73 00 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 FC 5F 07 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 E0 79 07 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 5C 87 1D 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 4C 76 1D 00 E1 18 0F C2 AA 2B 3F E3 B2 6E D4 52 27 36 44 57 18 6E 00 00 E1 18 0F C2 AA 2B 3F E3 B2 6E D4 52 27 36 44 57 AC 6D 00 00 E1 18 0F C2 AA 2B 3F E3 B2 6E D4 52 27 36 44 57 D0 8C 00 00 E1 18 0F C2 AA 2B 3F E3 B2 6E D4 52 27 36 44 57 7C 3A 00 00 E1 18 0F C2 AA 2B 3F E3 B2 6E D4 52 27 36 44 57 0C 2E 00 00 E1 18 0F C2 AA 2B 3F E3 B2 6E D4 52 27 36 44 57 AC 2F 00 00 E1 18 0F C2 AA 2B 3F E3 B2 6E D4 52 27 36 44 57 E4 90 00 00 E1 18 0F C2 AA 2B 3F E3 B2 6E D4 52 27 36 44 57 48 86 00 00 E1 18 0F C2 AA 2B 3F E3 B2 6E D4 52 27 36 44 57 C0 21 00 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 6C 6F 1D 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 C4 A2 22 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 D0 25 22 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 90 25 22 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 A0 73 00 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 2C 26 22 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 2C 84 36 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 AC 8C 36 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 38 CC 02 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 14 8C 36 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 C0 8C 36 00 0F 8D 35 B6 55 6F 3E 34 8E AA 80 AB 54 04 7D C5 1C 4C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
default	09:45:24.254432+0800	hootowl	[0x148f18f00] activating connection: mach=true listener=false peer=false name=com.apple.geod
fault	09:45:24.255902+0800	hootowl	__delegate_identifier__:Performance Diagnostics__:::____message__:{"message":"Performing I/O on the main thread can cause hangs.","antipattern trigger":"-[NSBundle bundleIdentifier]","message type":"suppressable","issue type":1,"category type":17,"subcategory type":3,"show in console":"0"}'26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 30 F4 4C 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 B4 F3 4C 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 A0 73 00 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 9C F3 4C 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 04 C3 53 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 78 C6 53 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 88 84 36 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 AC 8C 36 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 38 CC 02 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 14 8C 36 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 C0 8C 36 00 0F 8D 35 B6 55 6F 3E 34 8E AA 80 AB 54 04 7D C5 1C 4C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
default	09:45:24.256903+0800	hootowl	[0x148f18dc0] activating connection: mach=true listener=false peer=false name=com.apple.geod
default	09:45:24.257616+0800	hootowl	[0x148f188c0] activating connection: mach=true listener=false peer=false name=com.apple.geod
fault	09:45:24.262660+0800	hootowl	__delegate_identifier__:Performance Diagnostics__:::____message__:{"message":"Performing I/O on the main thread can cause slow launches.","antipattern trigger":"-[NSBundle bundleIdentifier]","message type":"suppressable","issue type":4,"category type":17,"subcategory type":3,"show in console":"0"}'26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 30 F4 4C 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 B4 F3 4C 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 A0 73 00 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 9C F3 4C 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 04 C3 53 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 78 C6 53 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 88 84 36 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 AC 8C 36 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 38 CC 02 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 14 8C 36 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 C0 8C 36 00 0F 8D 35 B6 55 6F 3E 34 8E AA 80 AB 54 04 7D C5 1C 4C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
fault	09:45:24.268245+0800	hootowl	__delegate_identifier__:Performance Diagnostics__:::____message__:{"message":"Performing I/O on the main thread can cause hangs.","antipattern trigger":"-[NSFileManager createDirectoryAtURL:withIntermediateDirectories:attributes:error:]","message type":"suppressable","issue type":1,"category type":17,"subcategory type":3,"show in console":"0"}'26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 20 86 53 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 04 FD 49 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 74 FC 49 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 A0 73 00 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 5C FC 49 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 7C C3 53 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 78 C6 53 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 88 84 36 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 AC 8C 36 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 38 CC 02 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 14 8C 36 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 C0 8C 36 00 0F 8D 35 B6 55 6F 3E 34 8E AA 80 AB 54 04 7D C5 1C 4C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
fault	09:45:24.279201+0800	hootowl	__delegate_identifier__:Performance Diagnostics__:::____message__:{"message":"Performing I/O on the main thread can cause slow launches.","antipattern trigger":"-[NSFileManager createDirectoryAtURL:withIntermediateDirectories:attributes:error:]","message type":"suppressable","issue type":4,"category type":17,"subcategory type":3,"show in console":"0"}'26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 20 86 53 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 04 FD 49 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 74 FC 49 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 A0 73 00 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 5C FC 49 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 7C C3 53 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 78 C6 53 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 88 84 36 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 AC 8C 36 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 38 CC 02 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 14 8C 36 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 C0 8C 36 00 0F 8D 35 B6 55 6F 3E 34 8E AA 80 AB 54 04 7D C5 1C 4C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
fault	09:45:24.289463+0800	hootowl	__delegate_identifier__:Performance Diagnostics__:::____message__:{"message":"-[NSFileManager createDirectoryAtURL:withIntermediateDirectories:attributes:error:] is performing excessive I/O which will reduce the health of storage devices.","antipattern trigger":"-[NSFileManager createDirectoryAtURL:withIntermediateDirectories:attributes:error:]","message type":"suppressable","issue type":2,"category type":17,"subcategory type":8192,"show in console":"0"}'26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 20 86 53 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 04 FD 49 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 74 FC 49 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 A0 73 00 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 5C FC 49 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 7C C3 53 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 78 C6 53 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 88 84 36 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 AC 8C 36 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 38 CC 02 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 14 8C 36 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 C0 8C 36 00 0F 8D 35 B6 55 6F 3E 34 8E AA 80 AB 54 04 7D C5 1C 4C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
fault	09:45:24.300798+0800	hootowl	__delegate_identifier__:Performance Diagnostics__:::____message__:{"message":"-[NSFileManager createDirectoryAtPath:withIntermediateDirectories:attributes:error:] is performing excessive I/O which will reduce the health of storage devices.","antipattern trigger":"-[NSFileManager createDirectoryAtPath:withIntermediateDirectories:attributes:error:]","message type":"suppressable","issue type":2,"category type":17,"subcategory type":8192,"show in console":"0"}'73 84 1A A3 BF DD 32 2D 8D C2 E5 18 5A 14 DE E1 C4 D8 0C 00 73 84 1A A3 BF DD 32 2D 8D C2 E5 18 5A 14 DE E1 C8 FD 0C 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 20 86 53 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 04 FD 49 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 74 FC 49 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 A0 73 00 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 5C FC 49 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 7C C3 53 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 78 C6 53 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 88 84 36 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 AC 8C 36 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 38 CC 02 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 14 8C 36 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 C0 8C 36 00 0F 8D 35 B6 55 6F 3E 34 8E AA 80 AB 54 04 7D C5 1C 4C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
default	09:45:24.304785+0800	hootowl	Task <6CD5524D-F067-4C09-A823-5B80B55C7B03>.<2> received response, status 200 content K
fault	09:45:24.307079+0800	hootowl	__delegate_identifier__:Performance Diagnostics__:::____message__:{"message":"Performing I/O on the main thread can cause hangs.","antipattern trigger":"-[NSFileManager createDirectoryAtURL:withIntermediateDirectories:attributes:error:]","message type":"suppressable","issue type":1,"category type":17,"subcategory type":3,"show in console":"0"}'26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 20 86 53 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 84 FB 49 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 A0 73 00 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 68 FF 49 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 74 FC 49 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 A0 73 00 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 5C FC 49 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 7C C3 53 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 78 C6 53 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 88 84 36 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 AC 8C 36 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 38 CC 02 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 14 8C 36 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 C0 8C 36 00 0F 8D 35 B6 55 6F 3E 34 8E AA 80 AB 54 04 7D C5 1C 4C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
default	09:45:24.308758+0800	hootowl	[0x148f197c0] activating connection: mach=true listener=false peer=false name=com.apple.fontservicesd
fault	09:45:24.352936+0800	hootowl	__delegate_identifier__:Performance Diagnostics__:::____message__:{"message":"Performing I/O on the main thread can cause slow launches.","antipattern trigger":"-[NSFileManager createDirectoryAtURL:withIntermediateDirectories:attributes:error:]","message type":"suppressable","issue type":4,"category type":17,"subcategory type":3,"show in console":"0"}'26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 20 86 53 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 84 FB 49 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 A0 73 00 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 68 FF 49 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 74 FC 49 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 A0 73 00 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 5C FC 49 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 7C C3 53 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 78 C6 53 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 88 84 36 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 AC 8C 36 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 38 CC 02 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 14 8C 36 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 C0 8C 36 00 0F 8D 35 B6 55 6F 3E 34 8E AA 80 AB 54 04 7D C5 1C 4C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
fault	09:45:24.355870+0800	hootowl	__delegate_identifier__:Performance Diagnostics__:::____message__:{"message":"-[NSFileManager createDirectoryAtURL:withIntermediateDirectories:attributes:error:] is performing excessive I/O which will reduce the health of storage devices.","antipattern trigger":"-[NSFileManager createDirectoryAtURL:withIntermediateDirectories:attributes:error:]","message type":"suppressable","issue type":2,"category type":17,"subcategory type":8192,"show in console":"0"}'26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 20 86 53 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 84 FB 49 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 A0 73 00 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 68 FF 49 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 74 FC 49 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 A0 73 00 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 5C FC 49 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 7C C3 53 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 78 C6 53 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 88 84 36 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 AC 8C 36 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 38 CC 02 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 14 8C 36 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 C0 8C 36 00 0F 8D 35 B6 55 6F 3E 34 8E AA 80 AB 54 04 7D C5 1C 4C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
default	09:45:24.366029+0800	hootowl	Not observing PTDefaults on customer install.
fault	09:45:24.368357+0800	hootowl	__delegate_identifier__:Performance Diagnostics__:::____message__:{"message":"-[NSFileManager createDirectoryAtPath:withIntermediateDirectories:attributes:error:] is performing excessive I/O which will reduce the health of storage devices.","antipattern trigger":"-[NSFileManager createDirectoryAtPath:withIntermediateDirectories:attributes:error:]","message type":"suppressable","issue type":2,"category type":17,"subcategory type":8192,"show in console":"0"}'73 84 1A A3 BF DD 32 2D 8D C2 E5 18 5A 14 DE E1 C4 D8 0C 00 73 84 1A A3 BF DD 32 2D 8D C2 E5 18 5A 14 DE E1 C8 FD 0C 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 20 86 53 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 84 FB 49 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 A0 73 00 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 68 FF 49 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 74 FC 49 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 A0 73 00 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 5C FC 49 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 7C C3 53 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 78 C6 53 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 88 84 36 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 AC 8C 36 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 38 CC 02 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 14 8C 36 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 C0 8C 36 00 0F 8D 35 B6 55 6F 3E 34 8E AA 80 AB 54 04 7D C5 1C 4C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
fault	09:45:24.375865+0800	hootowl	__delegate_identifier__:Performance Diagnostics__:::____message__:{"message":"-[NSFileManager createDirectoryAtURL:withIntermediateDirectories:attributes:error:] is performing excessive I/O which will reduce the health of storage devices.","antipattern trigger":"-[NSFileManager createDirectoryAtURL:withIntermediateDirectories:attributes:error:]","message type":"suppressable","issue type":2,"category type":17,"subcategory type":8192,"show in console":"0"}'73 84 1A A3 BF DD 32 2D 8D C2 E5 18 5A 14 DE E1 9C 2F 0B 00 73 84 1A A3 BF DD 32 2D 8D C2 E5 18 5A 14 DE E1 50 3B 0B 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 20 89 4E 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 D8 8F 4E 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 90 8D 4E 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 70 8C 4E 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 A0 73 00 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 54 8C 4E 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 EC FD 4C 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 44 45 00 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 D8 D5 03 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 90 7B 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 88 84 01 00 34 B4 47 44 BC 64 38 6E AB 90 EE E8 6B 23 AC 46 74 13 00 00 34 B4 47 44 BC 64 38 6E AB 90 EE E8 6B 23 AC 46 C0 08 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
fault	09:45:24.379973+0800	hootowl	__delegate_identifier__:Performance Diagnostics__:::____message__:{"message":"-[NSFileManager createDirectoryAtPath:withIntermediateDirectories:attributes:error:] is performing excessive I/O which will reduce the health of storage devices.","antipattern trigger":"-[NSFileManager createDirectoryAtPath:withIntermediateDirectories:attributes:error:]","message type":"suppressable","issue type":2,"category type":17,"subcategory type":8192,"show in console":"0"}'73 84 1A A3 BF DD 32 2D 8D C2 E5 18 5A 14 DE E1 C4 D8 0C 00 73 84 1A A3 BF DD 32 2D 8D C2 E5 18 5A 14 DE E1 C8 FD 0C 00 73 84 1A A3 BF DD 32 2D 8D C2 E5 18 5A 14 DE E1 9C 2F 0B 00 73 84 1A A3 BF DD 32 2D 8D C2 E5 18 5A 14 DE E1 50 3B 0B 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 20 89 4E 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 D8 8F 4E 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 90 8D 4E 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 70 8C 4E 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 A0 73 00 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 54 8C 4E 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 EC FD 4C 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 44 45 00 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 D8 D5 03 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 90 7B 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 88 84 01 00 34 B4 47 44 BC 64 38 6E AB 90 EE E8 6B 23 AC 46 74 13 00 00 34 B4 47 44 BC 64 38 6E AB 90 EE E8 6B 23 AC 46 C0 08 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
fault	09:45:24.398459+0800	hootowl	__delegate_identifier__:Performance Diagnostics__:::____message__:{"message":"-[NSFileManager createDirectoryAtURL:withIntermediateDirectories:attributes:error:] is performing excessive I/O which will reduce the health of storage devices.","antipattern trigger":"-[NSFileManager createDirectoryAtURL:withIntermediateDirectories:attributes:error:]","message type":"suppressable","issue type":2,"category type":17,"subcategory type":8192,"show in console":"0"}'73 84 1A A3 BF DD 32 2D 8D C2 E5 18 5A 14 DE E1 9C 2F 0B 00 73 84 1A A3 BF DD 32 2D 8D C2 E5 18 5A 14 DE E1 50 3B 0B 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 20 89 4E 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 B8 CA 50 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 C0 C9 50 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 A0 73 00 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 A8 C9 50 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 60 EF 4C 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 50 F3 4C 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 A0 73 00 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 3C F3 4C 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 94 8C 4E 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 A0 73 00 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 54 8C 4E 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 EC FD 4C 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 44 45 00 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 D8 D5 03 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 90 7B 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 88 84 01 00 34 B4 47 44 BC 64 38 6E AB 90 EE E8 6B 23 AC 46 74 13 00 00 34 B4 47 44 BC 64 38 6E AB 90 EE E8 6B 23 AC 46 C0 08 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
fault	09:45:24.402705+0800	hootowl	__delegate_identifier__:Performance Diagnostics__:::____message__:{"message":"-[NSFileManager createDirectoryAtPath:withIntermediateDirectories:attributes:error:] is performing excessive I/O which will reduce the health of storage devices.","antipattern trigger":"-[NSFileManager createDirectoryAtPath:withIntermediateDirectories:attributes:error:]","message type":"suppressable","issue type":2,"category type":17,"subcategory type":8192,"show in console":"0"}'73 84 1A A3 BF DD 32 2D 8D C2 E5 18 5A 14 DE E1 C4 D8 0C 00 73 84 1A A3 BF DD 32 2D 8D C2 E5 18 5A 14 DE E1 C8 FD 0C 00 73 84 1A A3 BF DD 32 2D 8D C2 E5 18 5A 14 DE E1 9C 2F 0B 00 73 84 1A A3 BF DD 32 2D 8D C2 E5 18 5A 14 DE E1 50 3B 0B 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 20 89 4E 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 B8 CA 50 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 C0 C9 50 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 A0 73 00 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 A8 C9 50 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 60 EF 4C 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 50 F3 4C 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 A0 73 00 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 3C F3 4C 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 94 8C 4E 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 A0 73 00 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 54 8C 4E 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 EC FD 4C 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 44 45 00 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 D8 D5 03 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 90 7B 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 88 84 01 00 34 B4 47 44 BC 64 38 6E AB 90 EE E8 6B 23 AC 46 74 13 00 00 34 B4 47 44 BC 64 38 6E AB 90 EE E8 6B 23 AC 46 C0 08 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
fault	09:45:24.412975+0800	hootowl	__delegate_identifier__:Performance Diagnostics__:::____message__:{"message":"Performing I/O on the main thread can cause hangs.","antipattern trigger":"-[NSData initWithContentsOfURL:options:error:]","message type":"suppressable","issue type":1,"category type":17,"subcategory type":3,"show in console":"0"}'26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 64 03 4A 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 AC FE 49 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 74 FC 49 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 A0 73 00 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 5C FC 49 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 7C C3 53 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 78 C6 53 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 88 84 36 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 AC 8C 36 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 38 CC 02 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 14 8C 36 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 C0 8C 36 00 0F 8D 35 B6 55 6F 3E 34 8E AA 80 AB 54 04 7D C5 1C 4C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
fault	09:45:24.417428+0800	hootowl	__delegate_identifier__:Performance Diagnostics__:::____message__:{"message":"Performing I/O on the main thread can cause slow launches.","antipattern trigger":"-[NSData initWithContentsOfURL:options:error:]","message type":"suppressable","issue type":4,"category type":17,"subcategory type":3,"show in console":"0"}'26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 64 03 4A 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 AC FE 49 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 74 FC 49 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 A0 73 00 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 5C FC 49 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 7C C3 53 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 78 C6 53 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 88 84 36 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 AC 8C 36 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 38 CC 02 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 14 8C 36 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 C0 8C 36 00 0F 8D 35 B6 55 6F 3E 34 8E AA 80 AB 54 04 7D C5 1C 4C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
fault	09:45:24.441191+0800	hootowl	__delegate_identifier__:Performance Diagnostics__:::____message__:{"message":"-[NSFileManager createDirectoryAtURL:withIntermediateDirectories:attributes:error:] is performing excessive I/O which will reduce the health of storage devices.","antipattern trigger":"-[NSFileManager createDirectoryAtURL:withIntermediateDirectories:attributes:error:]","message type":"suppressable","issue type":2,"category type":17,"subcategory type":8192,"show in console":"0"}'73 84 1A A3 BF DD 32 2D 8D C2 E5 18 5A 14 DE E1 9C 2F 0B 00 73 84 1A A3 BF DD 32 2D 8D C2 E5 18 5A 14 DE E1 50 3B 0B 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 20 89 4E 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 5C 48 4C 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 50 43 4C 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 14 42 4C 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 A0 73 00 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 F4 41 4C 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 00 FE 4C 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 44 45 00 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 D8 D5 03 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 90 7B 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 88 84 01 00 34 B4 47 44 BC 64 38 6E AB 90 EE E8 6B 23 AC 46 74 13 00 00 34 B4 47 44 BC 64 38 6E AB 90 EE E8 6B 23 AC 46 C0 08 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
fault	09:45:24.444283+0800	hootowl	__delegate_identifier__:Performance Diagnostics__:::____message__:{"message":"-[NSFileManager createDirectoryAtPath:withIntermediateDirectories:attributes:error:] is performing excessive I/O which will reduce the health of storage devices.","antipattern trigger":"-[NSFileManager createDirectoryAtPath:withIntermediateDirectories:attributes:error:]","message type":"suppressable","issue type":2,"category type":17,"subcategory type":8192,"show in console":"0"}'73 84 1A A3 BF DD 32 2D 8D C2 E5 18 5A 14 DE E1 C4 D8 0C 00 73 84 1A A3 BF DD 32 2D 8D C2 E5 18 5A 14 DE E1 C8 FD 0C 00 73 84 1A A3 BF DD 32 2D 8D C2 E5 18 5A 14 DE E1 9C 2F 0B 00 73 84 1A A3 BF DD 32 2D 8D C2 E5 18 5A 14 DE E1 50 3B 0B 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 20 89 4E 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 5C 48 4C 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 50 43 4C 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 14 42 4C 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 A0 73 00 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 F4 41 4C 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 00 FE 4C 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 44 45 00 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 D8 D5 03 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 90 7B 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 88 84 01 00 34 B4 47 44 BC 64 38 6E AB 90 EE E8 6B 23 AC 46 74 13 00 00 34 B4 47 44 BC 64 38 6E AB 90 EE E8 6B 23 AC 46 C0 08 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
fault	09:45:24.459074+0800	hootowl	__delegate_identifier__:Performance Diagnostics__:::____message__:{"message":"Performing I/O on the main thread can cause hangs.","antipattern trigger":"-[NSBundle bundleIdentifier]","message type":"suppressable","issue type":1,"category type":17,"subcategory type":3,"show in console":"0"}'1F 9E 58 05 E3 E9 36 33 80 71 44 2B C0 1B D2 88 C4 9F 02 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC C4 D1 08 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 A0 73 00 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC A0 D1 08 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 68 C2 08 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 9C D3 08 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 44 C1 08 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 70 05 03 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D F4 D0 02 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 48 CC 02 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 14 8C 36 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 C0 8C 36 00 0F 8D 35 B6 55 6F 3E 34 8E AA 80 AB 54 04 7D C5 1C 4C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
fault	09:45:24.463401+0800	hootowl	__delegate_identifier__:Performance Diagnostics__:::____message__:{"message":"Performing I/O on the main thread can cause slow launches.","antipattern trigger":"-[NSBundle bundleIdentifier]","message type":"suppressable","issue type":4,"category type":17,"subcategory type":3,"show in console":"0"}'1F 9E 58 05 E3 E9 36 33 80 71 44 2B C0 1B D2 88 C4 9F 02 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC C4 D1 08 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 A0 73 00 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC A0 D1 08 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 68 C2 08 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 9C D3 08 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 44 C1 08 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 70 05 03 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D F4 D0 02 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 48 CC 02 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 14 8C 36 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 C0 8C 36 00 0F 8D 35 B6 55 6F 3E 34 8E AA 80 AB 54 04 7D C5 1C 4C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
default	09:45:24.491136+0800	hootowl	Ending background task with UIBackgroundTaskIdentifier: 1
default	09:45:24.491216+0800	hootowl	Ending task with identifier 1 and description: <_UIBackgroundTaskInfo: 0x1481ca740>: taskID = 1, taskName = Launch Background Task for Coalescing, creationTime = 771914 (elapsed = 1), _expireHandler: (null)
default	09:45:24.491271+0800	hootowl	Decrementing reference count for assertion <BKSProcessAssertion: 0x1482b98b0> (used by background task with identifier 1: <_UIBackgroundTaskInfo: 0x1481ca740>: taskID = 1, taskName = Launch Background Task for Coalescing, creationTime = 771914 (elapsed = 1))
default	09:45:24.491333+0800	hootowl	Will invalidate assertion: <BKSProcessAssertion: 0x1482b98b0> for task identifier: 1
fault	09:45:24.507402+0800	hootowl	__delegate_identifier__:Performance Diagnostics__:::____message__:{"message":"Performing I/O on the main thread can cause slow launches.","antipattern trigger":"dlopen","message type":"suppressable","issue type":4,"category type":17,"subcategory type":3,"show in console":"0"}'49 5A A3 53 AA 50 32 32 A8 9D 65 E7 DE 92 DB 71 24 DE 00 00 49 5A A3 53 AA 50 32 32 A8 9D 65 E7 DE 92 DB 71 70 DD 00 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 A0 73 00 00 49 5A A3 53 AA 50 32 32 A8 9D 65 E7 DE 92 DB 71 AC DC 00 00 49 5A A3 53 AA 50 32 32 A8 9D 65 E7 DE 92 DB 71 1C DD 00 00 49 5A A3 53 AA 50 32 32 A8 9D 65 E7 DE 92 DB 71 F4 C5 00 00 49 5A A3 53 AA 50 32 32 A8 9D 65 E7 DE 92 DB 71 E4 C4 00 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC A8 05 13 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 A0 73 00 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 78 09 0D 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 88 07 0D 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 9C 6D 22 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 6C B1 11 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 A0 73 00 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC D8 67 01 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC A4 66 01 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 54 67 01 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 20 83 11 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC A8 BA 11 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 38 86 11 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 14 8D 11 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 3C 89 11 00 79 4F D2 56 8A 8D 3C 8D 91 AA AA C2 7E F3 51 2C C0 3F 02 00 79 4F D2 56 8A 8D 3C 8D 91 AA AA C2 7E F3 51 2C 44 32 02 00 79 4F D2 56 8A 8D 3C 8D 91 AA AA C2 7E F3 51 2C 10 2E 02 00 79 4F D2 56 8A 8D 3C 8D 91 AA AA C2 7E F3 51 2C 2C 71 00 00 79 4F D2 56 8A 8D 3C 8D 91 AA AA C2 7E F3 51 2C E4 38 00 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 18 82 09 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 90 3A 0A 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 10 76 11 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC A0 74 11 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 2C 71 11 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 78 7A 11 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 A0 73 00 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 18 2D 09 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 90 B4 0A 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC E4 D6 08 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 44 C1 08 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 70 05 03 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D F4 D0 02 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 48 CC 02 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 14 8C 36 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 C0 8C 36 00 0F 8D 35 B6 55 6F 3E 34 8E AA 80 AB 54 04 7D C5 1C 4C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
default	09:45:24.586153+0800	hootowl	Task <80D33321-F751-4689-823A-9070C09CBDD2>.<1> response ended
default	09:45:24.586580+0800	hootowl	Task <80D33321-F751-4689-823A-9070C09CBDD2>.<1> done using Connection 1
default	09:45:24.586656+0800	hootowl	[0x1499e2d00] activating connection: mach=true listener=false peer=false name=com.apple.mobilegestalt.xpc
default	09:45:24.586711+0800	hootowl	[C1] event: client:connection_idle @1.600s
default	09:45:24.586838+0800	hootowl	nw_protocol_tcp_notify [C1.1.1.1:3] nw_protocol_notification_type_connection_idle is true
default	09:45:24.586904+0800	hootowl	Task <80D33321-F751-4689-823A-9070C09CBDD2>.<1> summary for task success {transaction_duration_ms=1723, response_status=200, connection=1, protocol="http/1.1", domain_lookup_duration_ms=26, connect_duration_ms=540, secure_connection_duration_ms=440, private_relay=false, request_start_ms=807, request_duration_ms=0, response_start_ms=885, response_duration_ms=837, request_bytes=337, request_throughput_kbps=58589, response_bytes=473060, response_throughput_kbps=4519, cache_hit=true}
default	09:45:24.586961+0800	hootowl	nw_protocol_tcp_set_connection_idle [C1.1.1.1:3] os_nexus_flow_set_connection_idle returned 0
default	09:45:24.587055+0800	hootowl	[C1] event: client:connection_idle @1.600s
default	09:45:24.587171+0800	hootowl	nw_protocol_tcp_notify [C1.1.1.1:3] nw_protocol_notification_type_connection_idle is true
default	09:45:24.587181+0800	hootowl	[0x1499e2e40] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	09:45:24.587236+0800	hootowl	nw_protocol_tcp_set_connection_idle [C1.1.1.1:3] os_nexus_flow_set_connection_idle returned 0
default	09:45:24.587263+0800	hootowl	[0x1499e2d00] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	09:45:24.588788+0800	hootowl	Task <80D33321-F751-4689-823A-9070C09CBDD2>.<1> finished successfully
default	09:45:24.621532+0800	hootowl	Create activity from XPC object <nw_activity 50:1 [31E16363-B2E4-420C-9B36-077529992770] (reporting strategy default)>
default	09:45:24.621589+0800	hootowl	Create activity from XPC object <nw_activity 50:2 [EA7A4D16-5D7D-4603-9D2C-80DDCF872A85] (reporting strategy default)>
default	09:45:24.621623+0800	hootowl	Set activity <nw_activity 50:1 [31E16363-B2E4-420C-9B36-077529992770] (reporting strategy default)> as the global parent
default	09:45:24.621634+0800	hootowl	AggregateDictionary is deprecated and has been removed. Please migrate to Core Analytics.
default	09:45:24.621999+0800	hootowl	Target list changed: <CADisplay:LCD primary>
default	09:45:24.622159+0800	hootowl	sceneOfRecord: sceneID: sceneID:com.sharkda.hootowl-83FF55F6-7B28-4BFD-8825-33CB43E5D162  persistentID: 83FF55F6-7B28-4BFD-8825-33CB43E5D162
default	09:45:24.624871+0800	hootowl	Not push traits update to screen for new style 1, <UIWindowScene: 0x148378200> (83FF55F6-7B28-4BFD-8825-33CB43E5D162)
default	09:45:24.630172+0800	hootowl	[0x149b34000] activating connection: mach=true listener=false peer=false name=com.apple.storekitd
default	09:45:24.636274+0800	hootowl	-[NWConcrete_nw_resolver initWithEndpoint:parameters:path:log_str:] [R1] created for www.google.com:0 using: generic, attribution: developer
default	09:45:24.636286+0800	hootowl	nw_path_evaluator_start [DD04CFF6-F000-41D0-9F5C-1430552B9311 <NULL> generic, multipath service: handover, attribution: developer]
	path: satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good
default	09:45:24.636475+0800	hootowl	Task <C2039A11-85CB-4491-A2C8-C0CC08B408EC>.<1> resuming, timeouts(60.0, 180.0) qos(0x19) voucher((null)) activity(00000000-0000-0000-0000-000000000000)
default	09:45:24.636487+0800	hootowl	nw_resolver_set_update_handler_block_invoke [R1] started
default	09:45:24.636502+0800	hootowl	nw_path_evaluator_start [1E314C49-2F25-4E68-9B36-B5759BC255D7 www.google.com:0 generic, attribution: developer]
	path: satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good
default	09:45:24.657464+0800	hootowl	[0x149b35540] activating connection: mach=true listener=false peer=false name=com.apple.commcenter.coretelephony.xpc
default	09:45:24.659161+0800	hootowl	Task <334043C8-A557-4E46-B7B4-FF53031998B9>.<2> resuming, timeouts(60.0, 180.0) qos(0x19) voucher((null)) activity(00000000-0000-0000-0000-000000000000)
default	09:45:24.659168+0800	hootowl	Connection 0: creating secure tcp or quic connection
default	09:45:24.659507+0800	hootowl	Connection 3: enabling TLS
default	09:45:24.659516+0800	hootowl	Connection 3: starting, TC(0x0)
default	09:45:24.659533+0800	hootowl	[C3 22B5ADF9-1FB3-4EF6-80B1-F90A62077EB6 googleads.g.doubleclick.net:443 quic-connection, url: https://googleads.g.doubleclick.net/mads, definite, attribution: developer, context: com.apple.CFNetwork.NSURLSession.{0422B723-995A-474E-BE35-F711BDF3384C}{(null)}{Y}{2}{0x0} (private), proc: 1B526020-2DE0-3C65-9122-F1177549D69A, delegated upid: 0] start
default	09:45:24.659600+0800	hootowl	[C3 googleads.g.doubleclick.net:443 initial parent-flow ((null))] event: path:start @0.000s
default	09:45:24.659607+0800	hootowl	71	addMu1Proto(p0:)	1
default	09:45:24.659658+0800	hootowl	[ATTrackingManager] trackingAuthorizationStatus API call invoked.
default	09:45:24.660624+0800	hootowl	[0x149b36080] activating connection: mach=true listener=false peer=false name=com.apple.managedappdistributiond.xpc
default	09:45:24.661011+0800	hootowl	71	addMu1Proto(p0:)	2
default	09:45:24.661046+0800	hootowl	[C3 googleads.g.doubleclick.net:443 waiting parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.001s, uuid: 8DEA39AC-CA18-47A4-817E-7774DE7A72C6
default	09:45:24.661112+0800	hootowl	[C3 googleads.g.doubleclick.net:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_connect @0.002s
default	09:45:24.661127+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C3] reporting state preparing
fault	09:45:24.661200+0800	hootowl	Reading from public effective user settings.
default	09:45:24.661215+0800	hootowl	[C3 googleads.g.doubleclick.net:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_child @0.002s
default	09:45:24.661330+0800	hootowl	[C3.1 googleads.g.doubleclick.net:443 initial path ((null))] event: path:start @0.002s
default	09:45:24.661545+0800	hootowl	[C3.1 googleads.g.doubleclick.net:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.002s, uuid: 8DEA39AC-CA18-47A4-817E-7774DE7A72C6
default	09:45:24.661601+0800	hootowl	[C3.1 googleads.g.doubleclick.net:443 in_progress transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: transform:start @0.002s
default	09:45:24.661668+0800	hootowl	[C3.1.1 googleads.g.doubleclick.net:443 initial path ((null))] event: path:start @0.002s
default	09:45:24.663753+0800	hootowl	[C3.1.1 googleads.g.doubleclick.net:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.003s, uuid: 8DEA39AC-CA18-47A4-817E-7774DE7A72C6
default	09:45:24.663866+0800	hootowl	[C3.1.1 googleads.g.doubleclick.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:start_dns @0.004s
default	09:45:24.663909+0800	hootowl	Task <C2039A11-85CB-4491-A2C8-C0CC08B408EC>.<1> setting up Connection 3
default	09:45:24.664307+0800	hootowl	[ATTrackingManager] Performing TCC Access Preflight Request.
default	09:45:24.664391+0800	hootowl	[0x149b36940] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	09:45:24.666908+0800	hootowl	Sending selectors to server: (
    "regDataModeChanged:dataMode:",
    "carrierBundleChange:",
    "currentDataServiceDescriptorChanged:"
)
default	09:45:24.684494+0800	hootowl	[0x149b36940] invalidated after the last release of the connection object
default	09:45:24.690210+0800	hootowl	Read Per-App on Init: Smart invert = (null)
default	09:45:24.690392+0800	hootowl	[FBSDisplaySource 1-8] silently connecting raw configuration: <FBSDisplayConfiguration: 0x1494e7400; Main; mode: "393x852@3x 120Hz p3 SDR">
default	09:45:24.691329+0800	hootowl	[ATTrackingManager] Returning from trackingAuthorizationStatus - 0
default	09:45:24.692089+0800	hootowl	Realizing settings extension SBUISecureRenderingSettingsExtension on FBSSceneSettings
default	09:45:24.693265+0800	hootowl	Not push traits update to screen for new style 1, <UIWindowScene: 0x148378200> (83FF55F6-7B28-4BFD-8825-33CB43E5D162)
default	09:45:24.693284+0800	hootowl	Not push traits update to screen for new style 1, <UIWindowScene: 0x148378200> (83FF55F6-7B28-4BFD-8825-33CB43E5D162)
default	09:45:24.693291+0800	hootowl	sceneOfRecord: sceneID: sceneID:com.sharkda.hootowl-83FF55F6-7B28-4BFD-8825-33CB43E5D162  persistentID: 83FF55F6-7B28-4BFD-8825-33CB43E5D162
default	09:45:24.693341+0800	hootowl	Deactivation reason removed: 12; deactivation reasons: 4128 -> 32; animating application lifecycle event: 1
default	09:45:24.693588+0800	hootowl	Send setDeactivating: N (-DeactivationReason:SuspendedEventsOnly)
default	09:45:24.695091+0800	hootowl	Deactivation reason removed: 5; deactivation reasons: 32 -> 0; animating application lifecycle event: 0
default	09:45:24.695097+0800	hootowl	Creating hang event with BundleID: com.sharkda.hootowl
default	09:45:24.695118+0800	hootowl	Updating event->rollingFGTimestamp from INVALID_FOREGROUND_TIMESTAMP to 18525979946064
default	09:45:24.695410+0800	hootowl	Updating configuration of monitor M46045-1
default	09:45:24.695472+0800	hootowl	[0x149539cc0] activating connection: mach=true listener=false peer=false name=com.apple.hangtracermonitor
default	09:45:24.695507+0800	hootowl	Skip setting user action callback for 3rd party apps
default	09:45:24.695688+0800	hootowl	{"msg":"CLLocationManager", "event":"activity", "_cmd":"onDidBecomeActive:", "self":"0x1483580a0", "notification":"NSConcreteNotification 0x149634540 {name = UIApplicationDidBecomeActiveNotification; object = <_TtC7SwiftUIP33_ACC2C5639A7D76F611E170E831FCA49118SwiftUIApplication: 0x148378000>}"}
default	09:45:24.695944+0800	hootowl	Creating side-channel connection to com.apple.runningboard
default	09:45:24.696185+0800	hootowl	[0x149539cc0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	09:45:24.696198+0800	hootowl	[0x149539e00] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	09:45:24.696543+0800	hootowl	Hit the server for a process handle 18f442f0000b3dd that resolved to: [app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>:46045]
default	09:45:24.696707+0800	hootowl	Received state update for 46045 (app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>, unknown-NotVisible
default	09:45:24.698642+0800	hootowl	Connection 0: creating secure tcp or quic connection
default	09:45:24.698683+0800	hootowl	Connection 4: enabling TLS
default	09:45:24.698812+0800	hootowl	Connection 4: starting, TC(0x0)
default	09:45:24.699163+0800	hootowl	[C4 732818BF-A9B1-4912-88B6-B7C7FE826DEB pubads.g.doubleclick.net:443 quic-connection, url: https://pubads.g.doubleclick.net/gampad, definite, attribution: developer, context: com.apple.CFNetwork.NSURLSession.{0422B723-995A-474E-BE35-F711BDF3384C}{(null)}{Y}{2}{0x0} (private), proc: 1B526020-2DE0-3C65-9122-F1177549D69A, delegated upid: 0] start
default	09:45:24.699280+0800	hootowl	[C4 pubads.g.doubleclick.net:443 initial parent-flow ((null))] event: path:start @0.000s
default	09:45:24.700304+0800	hootowl	[C4 pubads.g.doubleclick.net:443 waiting parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.001s, uuid: 7CF2FF01-4B92-45FA-A5C4-81DD637FF6D5
default	09:45:24.701172+0800	hootowl	[C4 pubads.g.doubleclick.net:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_connect @0.002s
default	09:45:24.705813+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C4] reporting state preparing
default	09:45:24.707551+0800	hootowl	[C4 pubads.g.doubleclick.net:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_child @0.004s
default	09:45:24.707705+0800	hootowl	[C4.1 pubads.g.doubleclick.net:443 initial path ((null))] event: path:start @0.005s
default	09:45:24.708337+0800	hootowl	[C4.1 pubads.g.doubleclick.net:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.006s, uuid: 7CF2FF01-4B92-45FA-A5C4-81DD637FF6D5
default	09:45:24.708530+0800	hootowl	[C4.1 pubads.g.doubleclick.net:443 in_progress transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: transform:start @0.006s
default	09:45:24.708565+0800	hootowl	Municipal+Lifecycle 33
▶️ app → active: resuming GPS + 2 active proto timer(s)
default	09:45:24.708617+0800	hootowl	{"msg":"CLLocationManager", "event":"activity", "_cmd":"startUpdatingLocation", "self":"0x1483580a0"}
default	09:45:24.711848+0800	hootowl	[C4.1.1 pubads.g.doubleclick.net:443 initial path ((null))] event: path:start @0.007s
default	09:45:24.749303+0800	hootowl	Task <FB88A5E1-B6B9-48DF-8603-A675C36CFDA7>.<4> resuming, timeouts(60.0, 604800.0) qos(0x15) voucher((null)) activity(00000000-0000-0000-0000-000000000000)
default	09:45:24.764863+0800	hootowl	[C4.1.1 pubads.g.doubleclick.net:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.017s, uuid: 7CF2FF01-4B92-45FA-A5C4-81DD637FF6D5
default	09:45:24.766588+0800	hootowl	[C4.1.1 pubads.g.doubleclick.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:start_dns @0.020s
default	09:45:24.766627+0800	hootowl	Task <5100FD16-E95C-47E4-8962-4D6E52C0122F>.<3> resuming, timeouts(60.0, 604800.0) qos(0x15) voucher((null)) activity(00000000-0000-0000-0000-000000000000)
default	09:45:24.767460+0800	hootowl	{"msg":"#CLLocationManager invoking #delegate", "self":"0x1483580a0", "delegate":"0x148270140", "selector":"locationManager:didUpdateLocations:", "location":{"floor":2147483647,"lifespan":-1,"rawLat":25.0007528808197,"integrity":0,"referenceFrame":"Unknown","lon":121.56465855825979,"speed":-1,"type":"GPS","altitude":0,"rawCourse":-1,"confidence":100,"suitability":"Any","ellipsoidalAltitude":0,"timestamp":810265523.62722194,"rawReferenceFrame":"Unknown","lat":25.0007528808197,"verticalAccuracy":-1,"rawLon":121.56465855825979,"horizontalAccuracy":5,"speedAccuracy":-1,"courseAccuracy":-1,"fromSimulationController":true,"course":-1}, "eventType":"kCLConnectionMessageLocation"}
default	09:45:24.769292+0800	hootowl	    AVAudioSession_iOS.mm:996   Activated session 0x77c67d3
default	09:45:24.771548+0800	hootowl	[0x149614000] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	09:45:24.772674+0800	hootowl	[0x149614000] invalidated after the last release of the connection object
default	09:45:24.774146+0800	hootowl	[0x149614000] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	09:45:24.774368+0800	hootowl	[0x149614000] invalidated after the last release of the connection object
default	09:45:24.774910+0800	hootowl	Task <334043C8-A557-4E46-B7B4-FF53031998B9>.<2> setting up Connection 4
default	09:45:24.800811+0800	hootowl	[0x1496143c0] activating connection: mach=true listener=false peer=false name=com.apple.webprivacyd
default	09:45:24.800925+0800	hootowl	0x149bbc008 - WebsiteDataStore::WebsiteDataStore sessionID=1 identifier=null
default	09:45:24.800951+0800	hootowl	0x149bbcc88 - PageConfiguration::delaysWebProcessLaunchUntilFirstLoad() -> false because of associated processPool value
default	09:45:24.800970+0800	hootowl	0x149780508 - WebProcessPool::createWebPage: Not delaying WebProcess launch
default	09:45:24.801060+0800	hootowl	0x1310740c0 - [PID=0] WebProcessProxy::constructor:
default	09:45:24.801327+0800	hootowl	nw_endpoint_resolver_update [C3.1.1 googleads.g.doubleclick.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Adding endpoint handler for 142.250.77.194:443, tracker
default	09:45:24.801829+0800	hootowl	Successfully created a sandbox extension for '/private/var/containers/Bundle/Application/2290ADA6-FC62-4EB4-863B-0C67EBF31518/hootowl.app'
default	09:45:24.802148+0800	hootowl	[0x149614640] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	09:45:24.802357+0800	hootowl	+[AVPictureInPicturePlatformAdapter isPictureInPictureSupported]_block_invoke isPictureInPictureSupported YES
default	09:45:24.802864+0800	hootowl	Successfully created a sandbox extension for '/private/var/mobile/Containers/Data/Application/9C61D988-8BEB-42B6-A397-1E3A058F7BB4/Library/WebKit/WebsiteData/MediaKeys/v1'
default	09:45:24.802901+0800	hootowl	0x131030120 - [PID=0, throttler=0x131074150] ProcessThrottler::Activity::Activity: Starting foreground activity / 'Process initialization'
default	09:45:24.803004+0800	hootowl	Task <FB88A5E1-B6B9-48DF-8603-A675C36CFDA7>.<4> finished successfully
default	09:45:24.803013+0800	hootowl	0x148ec1518 - [pageProxyID=7, webPageID=8, PID=0] WebPageProxy::constructor, site isolation enabled 0
default	09:45:24.803293+0800	hootowl	PlaybackSessionManagerProxy::PlaybackSessionManagerProxy(2906663760)
default	09:45:24.803324+0800	hootowl	PlaybackSessionManagerProxy::VideoPresentationManagerProxy(2906663760)
default	09:45:24.803333+0800	hootowl	[0x1496152c0] activating connection: mach=true listener=false peer=false name=com.apple.accessibility.mediaaccessibilityd
default	09:45:24.803461+0800	hootowl	0x1310740c0 - [PID=0] WebProcessProxy::addExistingWebPage: webPage=0x148ec1518, pageProxyID=7, webPageID=8
default	09:45:24.803468+0800	hootowl	0x1310500e0 - [PID=0] WebProcessCache::updateCapacity: Cache is disabled by client
default	09:45:24.803492+0800	hootowl	Successfully created a sandbox extension for '/private/var/mobile/Containers/Data/Application/9C61D988-8BEB-42B6-A397-1E3A058F7BB4/Library/Caches/com.apple.WebKit.GPU'
default	09:45:24.803951+0800	hootowl	Successfully created a sandbox extension for '/private/var/mobile/Containers/Data/Application/9C61D988-8BEB-42B6-A397-1E3A058F7BB4/tmp/com.apple.WebKit.GPU'
default	09:45:24.804316+0800	hootowl	[C3.1.1 googleads.g.doubleclick.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:receive_dns @0.137s
default	09:45:24.804459+0800	hootowl	0x131030180 - [PID=0, throttler=0x1310e4270] ProcessThrottler::Activity::Activity: Starting foreground activity / 'Process initialization'
default	09:45:24.805095+0800	hootowl	Conforming to BrowserEngineKit text input protocol
default	09:45:24.807447+0800	hootowl	Launching process with config: bundleID: com.apple.WebKit.WebContent instance ID: Optional([_EXExtensionInstanceIdentifier: A86A11E2-3333-4DD5-9507-34F43D5DAD05])
default	09:45:24.808978+0800	hootowl	Launching process with config: bundleID: com.apple.WebKit.GPU instance ID: Optional([_EXExtensionInstanceIdentifier: EC8A05CE-CDCF-496D-A89C-3C3845A7BB20])
default	09:45:24.809432+0800	hootowl	[C3.1.1.1 142.250.77.194:443 initial path ((null))] event: path:start @0.155s
default	09:45:24.990658+0800	hootowl	[C3.1.1.1 142.250.77.194:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.350s, uuid: A101BF3F-A8AE-480C-9F42-6D7EF2D1609E
default	09:45:24.991080+0800	hootowl	[C3.1.1.1 142.250.77.194:443 in_progress channel-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_nexus @0.350s
default	09:45:24.991101+0800	hootowl	Received product response
default	09:45:24.994740+0800	hootowl	Parsing 1 products in response
error	09:45:24.995155+0800	hootowl	138	assessFences(l2d:)	no fences are availabe
default	09:45:24.996007+0800	hootowl	[C3.1.1.1 142.250.77.194:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:receive_nexus @0.354s
default	09:45:24.997235+0800	hootowl	[0x149b34000] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	09:45:24.998071+0800	hootowl	0x131068100 - ApplicationStateTracker::setIsInBackground: 0
default	09:45:24.998079+0800	hootowl	0x148c16400 - WKApplicationStateTrackingView: View with page [0x148ec1518, pageProxyID=7] was added to a window, _lastObservedStateWasBackground=0, isNowBackground=0
default	09:45:24.998097+0800	hootowl	AAFService connection invalidated
default	09:45:24.999017+0800	hootowl	quic_conn_initialize_inner [C3.1.1.1:2] [-6bc6555c6e5fb672] created QUIC connection (spin bit enabled)
default	09:45:24.999188+0800	hootowl	0x148ec1518 - [pageProxyID=7, webPageID=8, PID=0] WebPageProxy::updateActivityState: view visibility state changed 0 -> 1
default	09:45:24.999325+0800	hootowl	0x148ec1518 - [pageProxyID=7, webPageID=8, PID=0] WebPageProxy::viewIsBecomingVisible:
default	09:45:24.999392+0800	hootowl	[C3.1.1.1 142.250.77.194:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_connect @0.358s
default	09:45:25.999947+0800	hootowl	quic_crypto_new_flow [C3.1.1.1:2] [-6bc6555c6e5fb672] TLS stream is: [C5]
default	09:45:25.092967+0800	hootowl	[C5 B8B8D482-A951-445B-9F93-919EE26AD6FA 142.250.77.194:443 quic-connection, url: https://googleads.g.doubleclick.net/mads, tls, definite, attribution: developer, context: com.apple.CFNetwork.NSURLSession.{0422B723-995A-474E-BE35-F711BDF3384C}{(null)}{Y}{2}{0x0} (private), proc: 1B526020-2DE0-3C65-9122-F1177549D69A, delegated upid: 0, known tracker] start
default	09:45:25.093008+0800	hootowl	[C5 142.250.77.194:443 initial socket-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:start @0.000s
default	09:45:25.093236+0800	hootowl	[C5 142.250.77.194:443 waiting socket-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.000s, uuid: A101BF3F-A8AE-480C-9F42-6D7EF2D1609E
default	09:45:25.093542+0800	hootowl	[C5 142.250.77.194:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_connect @0.000s
default	09:45:25.093601+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C5] reporting state preparing
default	09:45:25.093689+0800	hootowl	nw_flow_connected [C5 142.250.77.194:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Transport protocol connected (quic-connection)
default	09:45:25.093755+0800	hootowl	[C5 142.250.77.194:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_transport @0.000s
default	09:45:25.094444+0800	hootowl	boringssl_session_apply_protocol_options_for_transport_block_invoke_2(2367) [C5:1][0x149a907e0] TLS configured [server(0) min_version(0x0304) max_version(0x0304) name(googleads.g.doubleclick.net) tickets(false) false_start(false) enforce_ev(false) enforce_ats(false) ats_non_pfs_ciphersuite_allowed(false) cc_mode_enforced(false) ech(false) pqtls(true), pake(false) skip_ats_trust(false)]
default	09:45:25.094814+0800	hootowl	boringssl_context_info_handler(2806) [C5:1][0x149a907e0] Client handshake started
default	09:45:25.094887+0800	hootowl	boringssl_context_info_handler(2823) [C5:1][0x149a907e0] Client handshake state: TLS client enter_early_data
default	09:45:25.094907+0800	hootowl	boringssl_context_info_handler(2823) [C5:1][0x149a907e0] Client handshake state: TLS client read_server_hello
default	09:45:25.095053+0800	hootowl	Screen Time has updated to use the system shield for any blocked URL.
default	09:45:25.095088+0800	hootowl	0x148ec1518 - [pageProxyID=7, webPageID=8, PID=0] WebPageProxy::updateThrottleState: UIProcess is taking a foreground assertion because the view is visible
default	09:45:25.095170+0800	hootowl	0x131030240 - [PID=0, throttler=0x131074150] ProcessThrottler::Activity::Activity: Starting foreground activity / 'View is visible'
default	09:45:25.095381+0800	hootowl	Starting death monitoring for handle [xpcservice<com.apple.WebKit.WebContent([app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>:46045])>{vt hash: 71395982}[uuid:A86A11E2-3333-4DD5-9507-34F43D5DAD05]{definition:com.apple.WebKit.WebContent[extension][client]}:46063]
default	09:45:25.095799+0800	hootowl	Starting death monitoring for handle [xpcservice<com.apple.WebKit.GPU([app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>:46045])>{vt hash: 223737757}[uuid:EC8A05CE-CDCF-496D-A89C-3C3845A7BB20]{definition:com.apple.WebKit.GPU[extension][client]}:46064]
default	09:45:25.096188+0800	hootowl	RemoteLayerTreeDrawingAreaProxy(10)::hideContentUntilPendingUpdate
default	09:45:25.099739+0800	hootowl	0x148d71000 (pageProxyID=7) -[WKWebView _endLiveResize]
default	09:45:25.100636+0800	hootowl	0x148ec1518 - [pageProxyID=7, webPageID=8, PID=0] WebPageProxy::loadRequest:
default	09:45:25.100661+0800	hootowl	0x148ec1518 - [pageProxyID=7, webPageID=8, PID=0] WebPageProxy::loadRequestWithNavigationShared:
default	09:45:25.100696+0800	hootowl	0x131114190 - NetworkProcessProxy::NetworkProcessProxy
default	09:45:25.100764+0800	hootowl	Successfully created a sandbox extension for '/private/var/mobile/Containers/Data/Application/9C61D988-8BEB-42B6-A397-1E3A058F7BB4/Library/WebKit/WebsiteData/ResourceLoadStatistics'
default	09:45:25.100790+0800	hootowl	Successfully created a sandbox extension for '/private/var/mobile/Containers/Data/Application/9C61D988-8BEB-42B6-A397-1E3A058F7BB4/Library/Caches/WebKit/NetworkCache'
default	09:45:25.100886+0800	hootowl	Successfully created a sandbox extension for '/private/var/mobile/Containers/Data/Application/9C61D988-8BEB-42B6-A397-1E3A058F7BB4/Library/Caches/WebKit/HSTS'
default	09:45:25.100914+0800	hootowl	Successfully created a sandbox extension for '/private/var/mobile/Containers/Data/Application/9C61D988-8BEB-42B6-A397-1E3A058F7BB4/Library/WebKit/WebsiteData/ResourceMonitorThrottler'
default	09:45:25.100929+0800	hootowl	Successfully created a sandbox extension for '/private/var/mobile/Containers/Data/Application/9C61D988-8BEB-42B6-A397-1E3A058F7BB4/Library/WebKit/WebsiteData/LocalStorage'
default	09:45:25.100934+0800	hootowl	Successfully created a sandbox extension for '/private/var/mobile/Containers/Data/Application/9C61D988-8BEB-42B6-A397-1E3A058F7BB4/Library/WebKit/WebsiteData/IndexedDB'
default	09:45:25.100941+0800	hootowl	Successfully created a sandbox extension for '/private/var/mobile/Containers/Data/Application/9C61D988-8BEB-42B6-A397-1E3A058F7BB4/Library/WebKit/WebsiteData/Default'
default	09:45:25.101717+0800	hootowl	Successfully created a sandbox extension for '/private/var/mobile/Containers/Data/Application/9C61D988-8BEB-42B6-A397-1E3A058F7BB4/Library/Caches/WebKit/CacheStorage'
default	09:45:25.102277+0800	hootowl	Successfully created a sandbox extension for '/private/var/mobile/Containers/Data/Application/9C61D988-8BEB-42B6-A397-1E3A058F7BB4/Library/Caches/WebKit/ServiceWorkers'
default	09:45:25.103001+0800	hootowl	Successfully created a sandbox extension for '/private/var/mobile/Containers/Data/Application/9C61D988-8BEB-42B6-A397-1E3A058F7BB4/Library/Caches/WebKit/AlternativeServices'
default	09:45:25.103111+0800	hootowl	Created new process ExtensionProcess: bundleID: com.apple.WebKit.WebContent instance ID: Optional([_EXExtensionInstanceIdentifier: A86A11E2-3333-4DD5-9507-34F43D5DAD05]) pid: 46063.
default	09:45:25.103545+0800	hootowl	Successfully created a sandbox extension for '/private/var/mobile/Containers/Data/Application/9C61D988-8BEB-42B6-A397-1E3A058F7BB4/Library/Cookies'
default	09:45:25.103626+0800	hootowl	Launching process with config: bundleID: com.apple.WebKit.Networking instance ID: Optional([_EXExtensionInstanceIdentifier: E7261D30-BFC9-4B17-9F63-341952617F96])
default	09:45:25.103640+0800	hootowl	Successfully created a sandbox extension for '/private/var/mobile/Containers/Data/Application/9C61D988-8BEB-42B6-A397-1E3A058F7BB4/Library/Caches/com.apple.WebKit.Networking'
default	09:45:25.103655+0800	hootowl	Created new process ExtensionProcess: bundleID: com.apple.WebKit.GPU instance ID: Optional([_EXExtensionInstanceIdentifier: EC8A05CE-CDCF-496D-A89C-3C3845A7BB20]) pid: 46064.
error	09:45:25.103672+0800	hootowl	Could not create a sandbox extension for '/var/containers/Bundle/Application/2290ADA6-FC62-4EB4-863B-0C67EBF31518/hootowl.app'
default	09:45:25.103686+0800	hootowl	AssertionCapability::AssertionCapability: taking assertion Foreground
default	09:45:25.103703+0800	hootowl	AssertionCapability::AssertionCapability: taking assertion Foreground
default	09:45:25.103738+0800	hootowl	nw_application_id_create_self Got client UUID=1B526020-2DE0-3C65-9122-F1177549D69A
default	09:45:25.104777+0800	hootowl	0x131030270 - [PID=0, throttler=0x131114220] ProcessThrottler::Activity::Activity: Starting foreground activity / 'Process initialization'
default	09:45:25.104976+0800	hootowl	0x1310501c0 - NavigationState is taking a process network assertion because a page load started
default	09:45:25.105041+0800	hootowl	Taking network activity on WebProcess with PID 0
default	09:45:25.105123+0800	hootowl	0x1310302d0 - [PID=0, throttler=0x131074150] ProcessThrottler::Activity::Activity: Starting background activity / 'Page Load'
default	09:45:25.110661+0800	hootowl	{"msg":"#CLLocationManager invoking #delegate", "self":"0x1483580a0", "delegate":"0x148270140", "selector":"locationManager:didUpdateLocations:", "location":{"floor":2147483647,"lifespan":-1,"rawLat":25.0007528808197,"integrity":0,"referenceFrame":"Unknown","lon":121.56465855825979,"speed":-1,"type":"GPS","altitude":0,"rawCourse":-1,"confidence":100,"suitability":"Any","ellipsoidalAltitude":0,"timestamp":810265524.63123906,"rawReferenceFrame":"Unknown","lat":25.0007528808197,"verticalAccuracy":-1,"rawLon":121.56465855825979,"horizontalAccuracy":5,"speedAccuracy":-1,"courseAccuracy":-1,"fromSimulationController":true,"course":-1}, "eventType":"kCLConnectionMessageLocation"}
default	09:45:25.111378+0800	hootowl	App is being debugged, do not track this hang
default	09:45:25.111442+0800	hootowl	Hang detected: 0.39s (debugger attached, not reporting)
default	09:45:25.111568+0800	hootowl	startConnection
default	09:45:25.111696+0800	hootowl	[0x149614780] activating connection: mach=true listener=false peer=false name=com.apple.UIKit.KeyboardManagement.hosted
default	09:45:25.111999+0800	hootowl	[0x1496148c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	09:45:25.112006+0800	hootowl	[0x149614a00] activating connection: mach=false listener=false peer=false name=(anonymous)
default	09:45:25.126303+0800	hootowl	Creating the shared game controller session...
default	09:45:25.126804+0800	hootowl	policyStatus:<BKSHIDEventDeliveryPolicyObserver: 0x148e4c060; token: com.apple.frontboard.systemappservices/FBSceneManager:sceneID%3Acom.sharkda.hootowl-83FF55F6-7B28-4BFD-8825-33CB43E5D162; status: ancestor> was:none
default	09:45:25.128813+0800	hootowl	policyStatus:<BKSHIDEventDeliveryPolicyObserver: 0x148d392c0; process scope; status: target> was:none
default	09:45:25.128904+0800	hootowl	Mu1Base+Ext 152
taipei 📦 minutely Received 472607 bytes
default	09:45:25.129419+0800	hootowl	Mu1Base+Ext 175
previousHash updated
default	09:45:25.129652+0800	hootowl	Starting death monitoring for handle [xpcservice<com.apple.WebKit.Networking([app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>:46045])>{vt hash: 114736818}[uuid:E7261D30-BFC9-4B17-9F63-341952617F96]{definition:com.apple.WebKit.Networking[extension][client]}:46065]
default	09:45:25.138634+0800	hootowl	    AVAudioSession_iOS.mm:996   Activated session 0x77c67d3
default	09:45:25.142796+0800	hootowl	Created new process ExtensionProcess: bundleID: com.apple.WebKit.Networking instance ID: Optional([_EXExtensionInstanceIdentifier: E7261D30-BFC9-4B17-9F63-341952617F96]) pid: 46065.
default	09:45:25.142946+0800	hootowl	AssertionCapability::AssertionCapability: taking assertion Foreground
default	09:45:25.146786+0800	hootowl	Municipal+Cyclops 93
🎨 model refreshed — obs:0s car:0 thread:main 🆔 8064324136773232350
default	09:45:25.146826+0800	hootowl	Municipal 130
🐎 minutelyAvailable ["newTaipeiCity ⏳04 16:18 ∑1428", "taipei ⏳05 09:45 ∑1172"]
default	09:45:25.147483+0800	hootowl	[C3.1.2 googleads.g.doubleclick.net:443 initial path ((null))] event: path:start @0.498s
default	09:45:25.148534+0800	hootowl	[C3.1.2 googleads.g.doubleclick.net:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.500s, uuid: 5D975A6B-DB8D-41BE-BF7E-772613FCFE8C
default	09:45:25.148725+0800	hootowl	[C3.1.2 googleads.g.doubleclick.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:start_dns @0.500s
default	09:45:25.150104+0800	hootowl	Municipal+Cyclops 93
🎨 model refreshed — obs:0s car:0 thread:main 🆔 8064324136773232350
default	09:45:25.150533+0800	hootowl	StorageAccessPromptQuirkController::didUpdateCachedListData: Loaded 1 storage access prompt(s) quirks from WebPrivacy.
default	09:45:25.150680+0800	hootowl	WebContent[46063] Installed launch log hook
default	09:45:25.150733+0800	hootowl	WebContent[46063] [0x10544f0c0] invalidated after the last release of the connection object
default	09:45:25.150742+0800	hootowl	WebContent[46063] [0x10544f3d0] invalidated because the client process (pid 46063) either cancelled the connection or exited
default	09:45:25.150753+0800	hootowl	[0x149614000] activating connection: mach=false listener=false peer=false name=(anonymous)
default	09:45:25.150777+0800	hootowl	0x1310740c0 - [PID=46063] WebProcessProxy::didFinishLaunching:
default	09:45:25.151295+0800	hootowl	0x131074150 - [PID=46063] ProcessThrottler::didConnectToProcess
default	09:45:25.151350+0800	hootowl	0x131074150 - [PID=46063] ProcessThrottler::setThrottleState: Updating process assertion type to 3 (foregroundActivities=2, backgroundActivities=4)
default	09:45:25.151365+0800	hootowl	AssertionCapability::AssertionCapability: taking assertion Foreground
default	09:45:25.151384+0800	hootowl	[C4.1.2 pubads.g.doubleclick.net:443 initial path ((null))] event: path:start @0.451s
default	09:45:25.151398+0800	hootowl	0x14a3c1300 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	09:45:25.151418+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	09:45:25.151478+0800	hootowl	0x1310740c0 - [PID=46063] WebProcessProxy::didChangeThrottleState: type=2
default	09:45:25.151487+0800	hootowl	0x1310740c0 - [PID=46063] WebProcessProxy::didChangeThrottleState(Foreground) Taking foreground assertion for network process
default	09:45:25.151519+0800	hootowl	0x131030300 - [PID=0, throttler=0x131114220] ProcessThrottler::Activity::Activity: Starting foreground activity / 'Networking for foreground view(s)'
default	09:45:25.151526+0800	hootowl	0x131030330 - [PID=0, throttler=0x1310e4270] ProcessThrottler::Activity::Activity: Starting foreground activity / 'GPU for foreground view(s)'
default	09:45:25.151590+0800	hootowl	0x13113c0c0 - ProcessAssertion::acquireSync Trying to take RBS assertion 'WebProcess Foreground Assertion' for process with PID=46063
default	09:45:25.151643+0800	hootowl	0x131114190 - NetworkProcessProxy::sendXPCEndpointToProcess(0x1310740c0) state = 1 has connection = 1 XPC endpoint message = 0x0
default	09:45:25.151747+0800	hootowl	0x1310e41e0 - GPUProcessProxy::didFinishLaunching:
default	09:45:25.151777+0800	hootowl	0x1310e41e0 - GPUProcessProxy::connectionWillOpen:
default	09:45:25.151890+0800	hootowl	0x1310e4270 - [PID=46064] ProcessThrottler::didConnectToProcess
default	09:45:25.152023+0800	hootowl	0x1310e4270 - [PID=46064] ProcessThrottler::setThrottleState: Updating process assertion type to 3 (foregroundActivities=2, backgroundActivities=1)
default	09:45:25.152030+0800	hootowl	AssertionCapability::AssertionCapability: taking assertion Foreground
default	09:45:25.152049+0800	hootowl	0x131114190 - NetworkProcessProxy::sendXPCEndpointToProcess(0x1310e41e0) state = 1 has connection = 1 XPC endpoint message = 0x0
default	09:45:25.152070+0800	hootowl	Scene target of keyboard event deferring environment did change: 1; scene: UIWindowScene: 0x148378200; scene identity: com.apple.frontboard.systemappservices/FBSceneManager:sceneID%3Acom.sharkda.hootowl-83FF55F6-7B28-4BFD-8825-33CB43E5D162
default	09:45:25.152132+0800	hootowl	[0x148e9b4f0] Scene target of event deferring environments did update: scene: 0x148378200; current systemShellManagesKeyboardFocus: 1; systemShellManagesKeyboardFocusForScene: 1; eligibleForRecordRemoval: 1;
default	09:45:25.152362+0800	hootowl	Scene became target of keyboard event deferring environment: UIWindowScene: 0x148378200; scene identity: com.apple.frontboard.systemappservices/FBSceneManager:sceneID%3Acom.sharkda.hootowl-83FF55F6-7B28-4BFD-8825-33CB43E5D162
default	09:45:25.152395+0800	hootowl	Stack[KeyWindow] 0x1482eeeb0: Migrate scenes from LastOneWins -> SystemShellManaged
default	09:45:25.153239+0800	hootowl	Setting default evaluation strategy for UIUserInterfaceIdiomPhone to SystemShellManaged
default	09:45:25.153532+0800	hootowl	policyStatus:<BKSHIDEventDeliveryPolicyObserver: 0x148d3a1c0; process scope; status: target> was:none
default	09:45:25.153614+0800	hootowl	0x13113c0c0 - ProcessAssertion() Successfully granted capability
default	09:45:25.153629+0800	hootowl	0x13113c180 - ProcessAssertion::acquireSync Trying to take RBS assertion 'GPUProcess Foreground Assertion' for process with PID=46064
default	09:45:25.275599+0800	hootowl	0x13113c180 - ProcessAssertion() Successfully granted capability
default	09:45:25.282190+0800	hootowl	[C4.1.2 pubads.g.doubleclick.net:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.581s, uuid: D94D163F-27E8-412A-9F44-7B417F699421
default	09:45:25.284265+0800	hootowl	[C4.1.2 pubads.g.doubleclick.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:start_dns @0.582s
error	09:45:25.332680+0800	hootowl	138	assessFences(l2d:)	no fences are availabe
default	09:45:25.333029+0800	hootowl	boringssl_context_info_handler(2823) [C5:1][0x149a907e0] Client handshake state: TLS 1.3 client read_hello_retry_request
default	09:45:25.333123+0800	hootowl	boringssl_context_info_handler(2823) [C5:1][0x149a907e0] Client handshake state: TLS 1.3 client read_server_hello
default	09:45:25.373718+0800	hootowl	boringssl_context_info_handler(2823) [C5:1][0x149a907e0] Client handshake state: TLS 1.3 client read_encrypted_extensions
default	09:45:25.376046+0800	hootowl	boringssl_context_info_handler(2823) [C5:1][0x149a907e0] Client handshake state: TLS 1.3 client read_certificate_request
default	09:45:25.376194+0800	hootowl	[0x149616940] activating connection: mach=true listener=false peer=false name=com.apple.GameController.gamecontrollerd.app
default	09:45:25.376447+0800	hootowl	Connected devices changed (0 added, 0 removed) -> [0] {(
)}
default	09:45:25.376528+0800	hootowl	Connected devices changed (0 added, 0 removed) -> [0] {(
)}
default	09:45:25.377161+0800	hootowl	Connected devices changed (0 added, 0 removed) -> [0] {(
)}
default	09:45:25.382045+0800	hootowl	WebContent[46063] getNetworkProcessConnection: Request connection for core identifier 2
default	09:45:25.382179+0800	hootowl	0x131030120 - [PID=46063, throttler=0x131074150] ProcessThrottler::Activity::invalidate: Ending foreground activity / 'Process initialization'
default	09:45:25.382828+0800	hootowl	0x131114190 - NetworkProcessProxy::getNetworkProcessConnection: Taking a background assertion because web process pid 46063 (core identifier 2) is requesting a connection
default	09:45:25.382838+0800	hootowl	0x131114190 - NetworkProcessProxy::sendXPCEndpointToProcess(0x1310740c0) state = 1 has connection = 1 XPC endpoint message = 0x14a32cc00
default	09:45:25.382953+0800	hootowl	0x131114190 - NetworkProcessProxy::sendXPCEndpointToProcess(0x1310e41e0) state = 1 has connection = 1 XPC endpoint message = 0x14a32cc00
default	09:45:25.383039+0800	hootowl	0x131030180 - [PID=46064, throttler=0x1310e4270] ProcessThrottler::Activity::invalidate: Ending foreground activity / 'Process initialization'
default	09:45:25.383244+0800	hootowl	nw_endpoint_resolver_update [C3.1.1 googleads.g.doubleclick.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Adding endpoint handler for 142.250.204.34:443, tracker
default	09:45:25.385694+0800	hootowl	[C3.1.1 googleads.g.doubleclick.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:receive_dns @0.744s
default	09:45:25.385708+0800	hootowl	[ATTrackingManager] trackingAuthorizationStatus API call invoked.
default	09:45:25.385732+0800	hootowl	[ATTrackingManager] Performing TCC Access Preflight Request.
default	09:45:25.446757+0800	hootowl	[ATTrackingManager] Returning from trackingAuthorizationStatus - 0
default	09:45:25.447206+0800	hootowl	nw_endpoint_resolver_update [C4.1.1 pubads.g.doubleclick.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Adding endpoint handler for 142.250.192.130:443, tracker
default	09:45:25.447354+0800	hootowl	[C4.1.1 pubads.g.doubleclick.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:receive_dns @0.754s
default	09:45:25.447979+0800	hootowl	[C3.1.1.2 142.250.204.34:443 initial path ((null))] event: path:start @0.808s
default	09:45:25.448440+0800	hootowl	[C3.1.1.2 142.250.204.34:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.809s, uuid: 5ADB97CE-0A43-4EB9-A7F4-316B156F867E
default	09:45:25.449018+0800	hootowl	[C3.1.1.2 142.250.204.34:443 in_progress channel-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_nexus @0.809s
default	09:45:25.487900+0800	hootowl	[C3.1.1.2 142.250.204.34:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:receive_nexus @0.810s
default	09:45:25.488437+0800	hootowl	quic_conn_initialize_inner [C3.1.1.2:2] [-4f404a5265fed4a6] created QUIC connection (spin bit enabled)
default	09:45:25.488920+0800	hootowl	[C3.1.1.2 142.250.204.34:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_connect @0.849s
default	09:45:25.490406+0800	hootowl	quic_crypto_new_flow [C3.1.1.2:2] [-4f404a5265fed4a6] TLS stream is: [C6]
default	09:45:25.490422+0800	hootowl	[C6 056FA614-F3ED-4C58-BF5C-4A0271450A3B 142.250.204.34:443 quic-connection, url: https://googleads.g.doubleclick.net/mads, tls, definite, attribution: developer, context: com.apple.CFNetwork.NSURLSession.{0422B723-995A-474E-BE35-F711BDF3384C}{(null)}{Y}{2}{0x0} (private), proc: 1B526020-2DE0-3C65-9122-F1177549D69A, delegated upid: 0, known tracker] start
default	09:45:25.490457+0800	hootowl	[C6 142.250.204.34:443 initial socket-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:start @0.000s
default	09:45:25.490473+0800	hootowl	[C6 142.250.204.34:443 waiting socket-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.000s, uuid: 5ADB97CE-0A43-4EB9-A7F4-316B156F867E
default	09:45:25.535460+0800	hootowl	[C6 142.250.204.34:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_connect @0.045s
default	09:45:25.535471+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C6] reporting state preparing
default	09:45:25.536017+0800	hootowl	nw_flow_connected [C6 142.250.204.34:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Transport protocol connected (quic-connection)
default	09:45:25.536061+0800	hootowl	[C6 142.250.204.34:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_transport @0.045s
default	09:45:25.536580+0800	hootowl	boringssl_session_apply_protocol_options_for_transport_block_invoke_2(2367) [C6:1][0x149a796e0] TLS configured [server(0) min_version(0x0304) max_version(0x0304) name(googleads.g.doubleclick.net) tickets(false) false_start(false) enforce_ev(false) enforce_ats(false) ats_non_pfs_ciphersuite_allowed(false) cc_mode_enforced(false) ech(false) pqtls(true), pake(false) skip_ats_trust(false)]
default	09:45:25.536701+0800	hootowl	boringssl_context_info_handler(2806) [C6:1][0x149a796e0] Client handshake started
default	09:45:25.537178+0800	hootowl	boringssl_context_info_handler(2823) [C6:1][0x149a796e0] Client handshake state: TLS client enter_early_data
default	09:45:25.537230+0800	hootowl	boringssl_context_info_handler(2823) [C6:1][0x149a796e0] Client handshake state: TLS client read_server_hello
default	09:45:25.537343+0800	hootowl	boringssl_context_info_handler(2823) [C5:1][0x149a907e0] Client handshake state: TLS 1.3 client read_server_certificate
default	09:45:25.537360+0800	hootowl	boringssl_context_info_handler(2823) [C5:1][0x149a907e0] Client handshake state: TLS 1.3 client read_server_certificate_verify
default	09:45:25.537637+0800	hootowl	boringssl_context_evaluate_trust_async(2249) [C5:1][0x149a907e0] Performing external trust evaluation
default	09:45:25.537687+0800	hootowl	boringssl_context_evaluate_trust_async_external(2234) [C5:1][0x149a907e0] Asyncing for external verify block
default	09:45:25.592422+0800	hootowl	Connection 0: creating secure tcp or quic connection
default	09:45:25.592669+0800	hootowl	Connection 7: enabling TLS
default	09:45:25.592680+0800	hootowl	Connection 7: starting, TC(0x0)
default	09:45:25.592691+0800	hootowl	[C7 B9B949F5-0712-4ED6-BFEC-38E741D950D0 data.ntpc.gov.tw:443 quic-connection, url: https://data.ntpc.gov.tw/api/datasets/e09b35a5-a738-48cc-b0f5-570b67ad9c78/csv/file, definite, attribution: developer, context: com.apple.CFNetwork.NSURLSession.{D8375FAB-BCC3-47F6-9F42-2CD36CF9484B}{(null)}{Y}{2}{0x0} (private), proc: 1B526020-2DE0-3C65-9122-F1177549D69A, delegated upid: 0] start
default	09:45:25.592715+0800	hootowl	[C7 data.ntpc.gov.tw:443 initial parent-flow ((null))] event: path:start @0.000s
default	09:45:25.593177+0800	hootowl	[C7 data.ntpc.gov.tw:443 waiting parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.000s, uuid: A30AD644-B2EC-41FE-9076-B3817A70E286
default	09:45:25.593271+0800	hootowl	[C7 data.ntpc.gov.tw:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_connect @0.000s
default	09:45:25.593281+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C7] reporting state preparing
default	09:45:25.593339+0800	hootowl	[C7 data.ntpc.gov.tw:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_child @0.000s
default	09:45:25.593413+0800	hootowl	Received state update for 46045 (app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>, unknown-NotVisible
default	09:45:25.593560+0800	hootowl	[C7.1 data.ntpc.gov.tw:443 initial path ((null))] event: path:start @0.000s
default	09:45:25.593830+0800	hootowl	[C7.1 data.ntpc.gov.tw:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.001s, uuid: A30AD644-B2EC-41FE-9076-B3817A70E286
default	09:45:25.593858+0800	hootowl	[C7.1 data.ntpc.gov.tw:443 in_progress transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: transform:start @0.001s
default	09:45:25.594053+0800	hootowl	[C7.1.1 data.ntpc.gov.tw:443 initial path ((null))] event: path:start @0.001s
default	09:45:25.666099+0800	hootowl	[C7.1.1 data.ntpc.gov.tw:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.068s, uuid: D1C9AB24-B934-4AB2-A718-9B521D10D72B
default	09:45:25.671652+0800	hootowl	[C7.1.1 data.ntpc.gov.tw:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:start_dns @0.068s
default	09:45:25.671709+0800	hootowl	Task <5100FD16-E95C-47E4-8962-4D6E52C0122F>.<3> setting up Connection 7
default	09:45:25.672020+0800	hootowl	[C4.1.1.1 142.250.192.130:443 initial path ((null))] event: path:start @0.977s
default	09:45:25.672679+0800	hootowl	[C4.1.1.1 142.250.192.130:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.978s, uuid: 670F6F90-7919-43DE-83E6-E591C366577F
default	09:45:25.672739+0800	hootowl	[C4.1.1.1 142.250.192.130:443 in_progress channel-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_nexus @0.978s
default	09:45:25.719266+0800	hootowl	[C4.1.1.1 142.250.192.130:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:receive_nexus @1.026s
default	09:45:25.722018+0800	hootowl	quic_conn_initialize_inner [C4.1.1.1:2] [-032b4ec180156458] created QUIC connection (spin bit enabled)
default	09:45:25.722352+0800	hootowl	[C4.1.1.1 142.250.192.130:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_connect @1.027s
default	09:45:25.723507+0800	hootowl	quic_crypto_new_flow [C4.1.1.1:2] [-032b4ec180156458] TLS stream is: [C8]
default	09:45:25.723515+0800	hootowl	[C8 E72C3567-F862-4F5E-9641-BC36E0A5B202 142.250.192.130:443 quic-connection, url: https://pubads.g.doubleclick.net/gampad, tls, definite, attribution: developer, context: com.apple.CFNetwork.NSURLSession.{0422B723-995A-474E-BE35-F711BDF3384C}{(null)}{Y}{2}{0x0} (private), proc: 1B526020-2DE0-3C65-9122-F1177549D69A, delegated upid: 0, known tracker] start
default	09:45:25.723578+0800	hootowl	[C8 142.250.192.130:443 initial socket-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:start @0.000s
default	09:45:25.723606+0800	hootowl	[C8 142.250.192.130:443 waiting socket-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.000s, uuid: 670F6F90-7919-43DE-83E6-E591C366577F
default	09:45:25.723841+0800	hootowl	[C8 142.250.192.130:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_connect @0.000s
default	09:45:25.723859+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C8] reporting state preparing
default	09:45:25.723906+0800	hootowl	nw_flow_connected [C8 142.250.192.130:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Transport protocol connected (quic-connection)
default	09:45:25.723916+0800	hootowl	[C8 142.250.192.130:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_transport @0.000s
default	09:45:25.724050+0800	hootowl	boringssl_session_apply_protocol_options_for_transport_block_invoke_2(2367) [C8:1][0x149a93c60] TLS configured [server(0) min_version(0x0304) max_version(0x0304) name(pubads.g.doubleclick.net) tickets(false) false_start(false) enforce_ev(false) enforce_ats(false) ats_non_pfs_ciphersuite_allowed(false) cc_mode_enforced(false) ech(false) pqtls(true), pake(false) skip_ats_trust(false)]
default	09:45:25.724158+0800	hootowl	boringssl_context_info_handler(2806) [C8:1][0x149a93c60] Client handshake started
default	09:45:25.724181+0800	hootowl	boringssl_context_info_handler(2823) [C8:1][0x149a93c60] Client handshake state: TLS client enter_early_data
default	09:45:25.724204+0800	hootowl	boringssl_context_info_handler(2823) [C8:1][0x149a93c60] Client handshake state: TLS client read_server_hello
default	09:45:25.724306+0800	hootowl	boringssl_context_info_handler(2823) [C6:1][0x149a796e0] Client handshake state: TLS 1.3 client read_hello_retry_request
default	09:45:25.724343+0800	hootowl	boringssl_context_info_handler(2823) [C6:1][0x149a796e0] Client handshake state: TLS 1.3 client read_server_hello
default	09:45:25.725325+0800	hootowl	boringssl_context_info_handler(2823) [C6:1][0x149a796e0] Client handshake state: TLS 1.3 client read_encrypted_extensions
default	09:45:25.778340+0800	hootowl	boringssl_context_info_handler(2823) [C6:1][0x149a796e0] Client handshake state: TLS 1.3 client read_certificate_request
default	09:45:25.780576+0800	hootowl	boringssl_context_info_handler(2823) [C8:1][0x149a93c60] Client handshake state: TLS 1.3 client read_hello_retry_request
default	09:45:25.780595+0800	hootowl	boringssl_context_info_handler(2823) [C8:1][0x149a93c60] Client handshake state: TLS 1.3 client read_server_hello
default	09:45:25.780878+0800	hootowl	boringssl_context_info_handler(2823) [C8:1][0x149a93c60] Client handshake state: TLS 1.3 client read_encrypted_extensions
default	09:45:25.780932+0800	hootowl	boringssl_context_info_handler(2823) [C8:1][0x149a93c60] Client handshake state: TLS 1.3 client read_certificate_request
default	09:45:25.782696+0800	hootowl	[C3.1.2 googleads.g.doubleclick.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:receive_alternative @1.143s
default	09:45:25.827358+0800	hootowl	[C3.1.2 googleads.g.doubleclick.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:receive_alternative @1.143s
default	09:45:25.827964+0800	hootowl	nw_endpoint_resolver_update [C3.1.2 googleads.g.doubleclick.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Adding endpoint handler for 142.250.204.34:443, tracker
default	09:45:25.828016+0800	hootowl	[C3.1.2 googleads.g.doubleclick.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:receive_dns @1.188s
default	09:45:25.828329+0800	hootowl	Connection 3: asked to evaluate TLS Trust
default	09:45:25.832053+0800	hootowl	Task <C2039A11-85CB-4491-A2C8-C0CC08B408EC>.<1> auth completion disp=1 cred=0x0
default	09:45:25.833811+0800	hootowl	[C4.1.2 pubads.g.doubleclick.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:receive_alternative @1.139s
default	09:45:25.833949+0800	hootowl	[C4.1.2 pubads.g.doubleclick.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:receive_alternative @1.139s
default	09:45:25.833998+0800	hootowl	nw_endpoint_resolver_update [C4.1.2 pubads.g.doubleclick.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Adding endpoint handler for 142.250.192.130:443, tracker
default	09:45:25.834716+0800	hootowl	[C4.1.2 pubads.g.doubleclick.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:receive_dns @1.140s
default	09:45:25.835151+0800	hootowl	[C3.1.2.1 142.250.204.34:443 initial path ((null))] event: path:start @1.195s
default	09:45:25.914222+0800	hootowl	[C3.1.2.1 142.250.204.34:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @1.267s, uuid: 680EA211-334E-4384-A2D2-D5E53C6B8CCC
default	09:45:25.914293+0800	hootowl	[C3.1.2.1 142.250.204.34:443 in_progress channel-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_nexus @1.268s
default	09:45:25.914452+0800	hootowl	[C3.1.2.1 142.250.204.34:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:receive_nexus @1.270s
default	09:45:25.914787+0800	hootowl	[C3.1.2.1 142.250.204.34:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_connect @1.270s
default	09:45:25.914978+0800	hootowl	tcp_output [C3.1.2.1:3] flags=[SEC] seq=3362154437, ack=0, win=65535 state=SYN_SENT rcv_nxt=0, snd_una=3362154437
default	09:45:25.915040+0800	hootowl	boringssl_context_info_handler(2823) [C6:1][0x149a796e0] Client handshake state: TLS 1.3 client read_server_certificate
default	09:45:25.915046+0800	hootowl	boringssl_context_info_handler(2823) [C6:1][0x149a796e0] Client handshake state: TLS 1.3 client read_server_certificate_verify
default	09:45:25.915950+0800	hootowl	boringssl_context_evaluate_trust_async(2249) [C6:1][0x149a796e0] Performing external trust evaluation
default	09:45:25.915999+0800	hootowl	boringssl_context_evaluate_trust_async_external(2234) [C6:1][0x149a796e0] Asyncing for external verify block
default	09:45:25.916093+0800	hootowl	boringssl_context_info_handler(2823) [C8:1][0x149a93c60] Client handshake state: TLS 1.3 client read_server_certificate
default	09:45:25.916101+0800	hootowl	boringssl_context_info_handler(2823) [C8:1][0x149a93c60] Client handshake state: TLS 1.3 client read_server_certificate_verify
default	09:45:25.916208+0800	hootowl	boringssl_context_evaluate_trust_async(2249) [C8:1][0x149a93c60] Performing external trust evaluation
default	09:45:25.916229+0800	hootowl	boringssl_context_evaluate_trust_async_external(2234) [C8:1][0x149a93c60] Asyncing for external verify block
default	09:45:25.916416+0800	hootowl	Connection 3: asked to evaluate TLS Trust
default	09:45:25.916460+0800	hootowl	(Trust 0x148268300) No pending evals, starting
default	09:45:25.916548+0800	hootowl	[0x149563c00] activating connection: mach=true listener=false peer=false name=com.apple.trustd
default	09:45:25.916559+0800	hootowl	(Trust 0x148268300) Completed async eval kickoff
default	09:45:25.973624+0800	hootowl	[C4.1.2.1 142.250.192.130:443 initial path ((null))] event: path:start @1.278s
default	09:45:25.973793+0800	hootowl	[C4.1.2.1 142.250.192.130:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @1.280s, uuid: 05127107-F327-42FB-B534-01637FDDBF5A
default	09:45:25.975672+0800	hootowl	[C4.1.2.1 142.250.192.130:443 in_progress channel-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_nexus @1.280s
default	09:45:25.975924+0800	hootowl	[C4.1.2.1 142.250.192.130:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:receive_nexus @1.281s
default	09:45:25.976181+0800	hootowl	[C4.1.2.1 142.250.192.130:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_connect @1.282s
default	09:45:25.976337+0800	hootowl	tcp_output [C4.1.2.1:3] flags=[SEC] seq=3488196868, ack=0, win=65535 state=SYN_SENT rcv_nxt=0, snd_una=3488196868
default	09:45:25.976511+0800	hootowl	nw_endpoint_resolver_update [C7.1.1 data.ntpc.gov.tw:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Adding endpoint handler for 61.60.98.243:443
default	09:45:25.976548+0800	hootowl	[C7.1.1 data.ntpc.gov.tw:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:receive_dns @0.383s
default	09:45:25.977020+0800	hootowl	Connection 4: asked to evaluate TLS Trust
default	09:45:25.978626+0800	hootowl	Task <334043C8-A557-4E46-B7B4-FF53031998B9>.<2> auth completion disp=1 cred=0x0
default	09:45:25.978650+0800	hootowl	(Trust 0x148268300) trustd returned 4
default	09:45:25.979613+0800	hootowl	System Trust Evaluation yielded status(0)
default	09:45:25.979655+0800	hootowl	(Trust 0x14a337000) No pending evals, starting
default	09:45:25.979726+0800	hootowl	[0x149582440] activating connection: mach=true listener=false peer=false name=com.apple.trustd
default	09:45:25.979923+0800	hootowl	(Trust 0x14a337000) Completed async eval kickoff
default	09:45:25.980057+0800	hootowl	[0x149563c00] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	09:45:26.031487+0800	hootowl	tcp_input [C3.1.2.1:3] flags=[S.] seq=3214497661, ack=3362154438, win=65535 state=SYN_SENT rcv_nxt=0, snd_una=3362154437
default	09:45:26.033495+0800	hootowl	nw_flow_connected [C3.1.2.1 142.250.204.34:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Transport protocol connected (tcp)
default	09:45:26.033601+0800	hootowl	[C3.1.2.1 142.250.204.34:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_transport @1.391s
default	09:45:26.033746+0800	hootowl	boringssl_session_apply_protocol_options_for_transport_block_invoke_2(2367) [C3.1.2.1:2][0x14a464a60] TLS configured [server(0) min_version(0x0303) max_version(0x0304) name(googleads.g.doubleclick.net) tickets(false) false_start(false) enforce_ev(false) enforce_ats(false) ats_non_pfs_ciphersuite_allowed(false) cc_mode_enforced(false) ech(false) pqtls(true), pake(false) skip_ats_trust(false)]
default	09:45:26.041536+0800	hootowl	boringssl_context_info_handler(2806) [C3.1.2.1:2][0x14a464a60] Client handshake started
default	09:45:26.041598+0800	hootowl	boringssl_context_info_handler(2823) [C3.1.2.1:2][0x14a464a60] Client handshake state: TLS client enter_early_data
default	09:45:26.041661+0800	hootowl	boringssl_context_info_handler(2823) [C3.1.2.1:2][0x14a464a60] Client handshake state: TLS client read_server_hello
default	09:45:26.105370+0800	hootowl	[C7.1.1.1 61.60.98.243:443 initial path ((null))] event: path:start @0.502s
default	09:45:26.109190+0800	hootowl	[C7.1.1.1 61.60.98.243:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.513s, uuid: 35A9D9F9-1DE0-4B86-B8FA-EA827DD9D855
default	09:45:26.109658+0800	hootowl	[C7.1.1.1 61.60.98.243:443 in_progress channel-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_nexus @0.514s
default	09:45:26.154340+0800	hootowl	[C7.1.1.1 61.60.98.243:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:receive_nexus @0.560s
default	09:45:26.159107+0800	hootowl	[C7.1.1.1 61.60.98.243:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_connect @0.561s
default	09:45:26.159234+0800	hootowl	tcp_output [C7.1.1.1:3] flags=[SEC] seq=820729279, ack=0, win=65535 state=SYN_SENT rcv_nxt=0, snd_una=820729279
default	09:45:26.159260+0800	hootowl	tcp_input [C4.1.2.1:3] flags=[S.] seq=950012595, ack=3488196869, win=65535 state=SYN_SENT rcv_nxt=0, snd_una=3488196868
default	09:45:26.159286+0800	hootowl	nw_flow_connected [C4.1.2.1 142.250.192.130:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Transport protocol connected (tcp)
default	09:45:26.159329+0800	hootowl	[C4.1.2.1 142.250.192.130:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_transport @1.462s
default	09:45:26.159490+0800	hootowl	boringssl_session_apply_protocol_options_for_transport_block_invoke_2(2367) [C4.1.2.1:2][0x14a465960] TLS configured [server(0) min_version(0x0303) max_version(0x0304) name(pubads.g.doubleclick.net) tickets(false) false_start(false) enforce_ev(false) enforce_ats(false) ats_non_pfs_ciphersuite_allowed(false) cc_mode_enforced(false) ech(false) pqtls(true), pake(false) skip_ats_trust(false)]
default	09:45:26.159512+0800	hootowl	boringssl_context_info_handler(2806) [C4.1.2.1:2][0x14a465960] Client handshake started
default	09:45:26.159537+0800	hootowl	boringssl_context_info_handler(2823) [C4.1.2.1:2][0x14a465960] Client handshake state: TLS client enter_early_data
default	09:45:26.159611+0800	hootowl	boringssl_context_info_handler(2823) [C4.1.2.1:2][0x14a465960] Client handshake state: TLS client read_server_hello
default	09:45:26.159853+0800	hootowl	boringssl_context_info_handler(2823) [C3.1.2.1:2][0x14a464a60] Client handshake state: TLS 1.3 client read_hello_retry_request
default	09:45:26.159950+0800	hootowl	boringssl_context_info_handler(2823) [C3.1.2.1:2][0x14a464a60] Client handshake state: TLS 1.3 client read_server_hello
default	09:45:26.159957+0800	hootowl	boringssl_context_info_handler(2823) [C3.1.2.1:2][0x14a464a60] Client handshake state: TLS 1.3 client read_encrypted_extensions
default	09:45:26.160043+0800	hootowl	boringssl_context_info_handler(2823) [C3.1.2.1:2][0x14a464a60] Client handshake state: TLS 1.3 client read_certificate_request
default	09:45:26.160058+0800	hootowl	boringssl_context_info_handler(2823) [C3.1.2.1:2][0x14a464a60] Client handshake state: TLS 1.3 client read_server_certificate
default	09:45:26.160073+0800	hootowl	boringssl_context_info_handler(2823) [C3.1.2.1:2][0x14a464a60] Client handshake state: TLS 1.3 client read_server_certificate_verify
default	09:45:26.161061+0800	hootowl	boringssl_context_evaluate_trust_async(2249) [C3.1.2.1:2][0x14a464a60] Performing external trust evaluation
default	09:45:26.161122+0800	hootowl	boringssl_context_evaluate_trust_async_external(2234) [C3.1.2.1:2][0x14a464a60] Asyncing for external verify block
default	09:45:26.161523+0800	hootowl	(Trust 0x14987d800) No pending evals, starting
default	09:45:26.161567+0800	hootowl	[0x1495b7d40] activating connection: mach=true listener=false peer=false name=com.apple.trustd
default	09:45:26.161576+0800	hootowl	(Trust 0x14987d800) Completed async eval kickoff
default	09:45:26.205729+0800	hootowl	(Trust 0x14a337000) trustd returned 4
default	09:45:26.208811+0800	hootowl	Connection 3: TLS Trust result 0
default	09:45:26.208941+0800	hootowl	boringssl_context_evaluate_trust_async_external_block_invoke_3(2148) [C5:1][0x149a907e0] Returning from external verify block with result: true
default	09:45:26.209781+0800	hootowl	boringssl_context_certificate_verify_callback(2430) [C5:1][0x149a907e0] Certificate verification result: OK
default	09:45:26.209789+0800	hootowl	boringssl_context_info_handler(2823) [C5:1][0x149a907e0] Client handshake state: TLS 1.3 client read_server_finished
default	09:45:26.209814+0800	hootowl	boringssl_context_info_handler(2823) [C5:1][0x149a907e0] Client handshake state: TLS 1.3 client send_end_of_early_data
default	09:45:26.210004+0800	hootowl	boringssl_context_info_handler(2823) [C5:1][0x149a907e0] Client handshake state: TLS 1.3 client send_client_encrypted_extensions
default	09:45:26.210022+0800	hootowl	boringssl_context_info_handler(2823) [C5:1][0x149a907e0] Client handshake state: TLS 1.3 client send_client_certificate
default	09:45:26.210030+0800	hootowl	boringssl_context_info_handler(2823) [C5:1][0x149a907e0] Client handshake state: TLS 1.3 client complete_second_flight
default	09:45:26.210221+0800	hootowl	boringssl_context_info_handler(2823) [C5:1][0x149a907e0] Client handshake state: TLS 1.3 client done
default	09:45:26.210285+0800	hootowl	boringssl_context_info_handler(2823) [C5:1][0x149a907e0] Client handshake state: TLS client finish_client_handshake
default	09:45:26.210299+0800	hootowl	boringssl_context_info_handler(2823) [C5:1][0x149a907e0] Client handshake state: TLS client done
default	09:45:26.210304+0800	hootowl	boringssl_context_info_handler(2812) [C5:1][0x149a907e0] Client handshake done
default	09:45:26.211852+0800	hootowl	nw_protocol_boringssl_signal_connected(895) [C5:1][0x149a907e0] TLS connected [server(0) version(0x0304) ciphersuite(TLS_AES_256_GCM_SHA384) group(0x11ec) signature_alg(0x0403) alpn(h3) resumed(0) offered_ticket(0) in_early_data(0) early_data_accepted(0) false_started(0) ocsp_received(0) sct_received(0) connect_time(1116ms) flight_time(279ms) rtt(238ms) write_stalls(0) read_stalls(7) pake(0x0000)]
default	09:45:26.211888+0800	hootowl	nw_flow_connected [C5 142.250.77.194:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (tls)
default	09:45:26.211940+0800	hootowl	[C5 142.250.77.194:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_connect @1.118s
default	09:45:26.212244+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C5] reporting state ready
default	09:45:26.212412+0800	hootowl	[C5 142.250.77.194:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @1.118s
default	09:45:26.212450+0800	hootowl	boringssl_context_evaluate_trust_async_external_block_invoke_3(2148) [C6:1][0x149a796e0] Returning from external verify block with result: true
default	09:45:26.212662+0800	hootowl	boringssl_context_certificate_verify_callback(2430) [C6:1][0x149a796e0] Certificate verification result: OK
default	09:45:26.281382+0800	hootowl	boringssl_context_info_handler(2823) [C6:1][0x149a796e0] Client handshake state: TLS 1.3 client read_server_finished
default	09:45:26.281414+0800	hootowl	boringssl_context_info_handler(2823) [C6:1][0x149a796e0] Client handshake state: TLS 1.3 client send_end_of_early_data
default	09:45:26.281421+0800	hootowl	boringssl_context_info_handler(2823) [C6:1][0x149a796e0] Client handshake state: TLS 1.3 client send_client_encrypted_extensions
default	09:45:26.281430+0800	hootowl	boringssl_context_info_handler(2823) [C6:1][0x149a796e0] Client handshake state: TLS 1.3 client send_client_certificate
default	09:45:26.281438+0800	hootowl	boringssl_context_info_handler(2823) [C6:1][0x149a796e0] Client handshake state: TLS 1.3 client complete_second_flight
default	09:45:26.281583+0800	hootowl	boringssl_context_info_handler(2823) [C6:1][0x149a796e0] Client handshake state: TLS 1.3 client done
default	09:45:26.281590+0800	hootowl	boringssl_context_info_handler(2823) [C6:1][0x149a796e0] Client handshake state: TLS client finish_client_handshake
default	09:45:26.281598+0800	hootowl	boringssl_context_info_handler(2823) [C6:1][0x149a796e0] Client handshake state: TLS client done
default	09:45:26.281605+0800	hootowl	boringssl_context_info_handler(2812) [C6:1][0x149a796e0] Client handshake done
default	09:45:26.282488+0800	hootowl	nw_protocol_boringssl_signal_connected(895) [C6:1][0x149a796e0] TLS connected [server(0) version(0x0304) ciphersuite(TLS_AES_256_GCM_SHA384) group(0x11ec) signature_alg(0x0403) alpn(h3) resumed(0) offered_ticket(0) in_early_data(0) early_data_accepted(0) false_started(0) ocsp_received(0) sct_received(0) connect_time(737ms) flight_time(240ms) rtt(186ms) write_stalls(0) read_stalls(7) pake(0x0000)]
default	09:45:26.282505+0800	hootowl	nw_flow_connected [C6 142.250.204.34:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (tls)
default	09:45:26.282535+0800	hootowl	[C6 142.250.204.34:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_connect @0.784s
default	09:45:26.282711+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C6] reporting state ready
default	09:45:26.289947+0800	hootowl	[C6 142.250.204.34:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.784s
default	09:45:26.290167+0800	hootowl	[0x149582440] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	09:45:26.290195+0800	hootowl	0x148d71000 -[WKWebView _updateVisibleContentRects:] finally ran 1.29s after being scheduled
default	09:45:26.290307+0800	hootowl	App is being debugged, do not track this hang
default	09:45:26.290316+0800	hootowl	Hang detected: 0.91s (debugger attached, not reporting)
default	09:45:26.290335+0800	hootowl	WebContent[46063] [0x105452ca0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	09:45:26.290355+0800	hootowl	WebContent[46063] Received Launch Services database
default	09:45:26.290363+0800	hootowl	0x131114190 - NetworkProcessProxy::didFinishLaunching
fault	09:45:26.290388+0800	hootowl	Networking process (0x131114190) took 1.186825 seconds to launch
default	09:45:26.290395+0800	hootowl	0x131114220 - [PID=46065] ProcessThrottler::didConnectToProcess
default	09:45:26.290402+0800	hootowl	0x131114220 - [PID=46065] ProcessThrottler::setThrottleState: Updating process assertion type to 3 (foregroundActivities=2, backgroundActivities=2)
default	09:45:26.310931+0800	hootowl	AssertionCapability::AssertionCapability: taking assertion Foreground
default	09:45:26.311161+0800	hootowl	0x13113c240 - ProcessAssertion::acquireSync Trying to take RBS assertion 'NetworkProcess Foreground Assertion' for process with PID=46065
default	09:45:26.377974+0800	hootowl	0x13113c240 - ProcessAssertion() Successfully granted capability
default	09:45:26.378242+0800	hootowl	[0x1496c4140] activating connection: mach=true listener=false peer=false name=com.apple.storekitd
default	09:45:26.378756+0800	hootowl	(Trust 0x14987d800) trustd returned 4
default	09:45:26.378859+0800	hootowl	System Trust Evaluation yielded status(0)
default	09:45:26.378906+0800	hootowl	(Trust 0x14a337e40) No pending evals, starting
default	09:45:26.378990+0800	hootowl	[0x1496c43c0] activating connection: mach=true listener=false peer=false name=com.apple.trustd
default	09:45:26.379127+0800	hootowl	(Trust 0x14a337e40) Completed async eval kickoff
default	09:45:26.429327+0800	hootowl	[0x1495b7d40] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	09:45:26.493046+0800	hootowl	quic_pmtud_restart [C3.1.1.1:2] [-ebc6555c6e5fb672] PMTUD enabled, max PMTU: 1500, header size: 28, current PMTU 1228
default	09:45:26.493113+0800	hootowl	quic_crypto_tls_ready_inner [C3.1.1.1:2] [-ebc6555c6e5fb672] QUIC connection established in 1494.91 ms, RTT 230.776 ms
default	09:45:26.493204+0800	hootowl	nw_flow_connected [C3.1.1.1 142.250.77.194:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Transport protocol connected (quic-connection)
default	09:45:26.494196+0800	hootowl	[C3.1.1.1 142.250.77.194:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_transport @1.854s
default	09:45:26.494223+0800	hootowl	nw_flow_connected [C3.1.1.1 142.250.77.194:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (CFNetworkConnection-4283075305)
default	09:45:26.494282+0800	hootowl	[C3.1.1.1 142.250.77.194:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @1.854s
default	09:45:26.494443+0800	hootowl	[C3.1.1 googleads.g.doubleclick.net:443 ready resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @1.854s
default	09:45:26.494477+0800	hootowl	[C3.1 googleads.g.doubleclick.net:443 ready transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @1.854s
default	09:45:26.494807+0800	hootowl	nw_protocol_tcp_log_summary [C3.1.2.1:3] 
	[07EB0C38-C4E9-46CC-901F-CEEC29CD6680 192.168.50.191:50792<->142.250.204.34:443]
	Init: 1, Conn_Time: 121.055ms, SYNs: 1, WR_T: 0/0, RD_T: 0/0, TFO: 0/0/0, ECN: 0/1/1, Accurate ECN (client/server): Disabled/Disabled, TS: 1, TSO: 0
	rtt_cache: none, rtt_upd: 2, rtt: 121.000ms, rtt_var: 45.375ms rtt_nc: 121.000ms, rtt_var_nc: 45.375ms base rtt: 121ms
	ACKs-compressed: 0, ACKs delayed: 0 delayed ACKs sent: 0
default	09:45:26.495057+0800	hootowl	nw_path_evaluator_start [28205D7A-6BB0-461C-9498-20DD2C5F39C2 <NULL> generic, multipath service: handover, attribution: developer]
	path: satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good
default	09:45:26.495704+0800	hootowl	quic_frame_write_CONNECTION_CLOSE [C3.1.1.2:2] [-ef404a5265fed4a6] sending CONNECTION_CLOSE, code NO_ERROR, type UNKNOWN, reason <null>
default	09:45:26.495731+0800	hootowl	[C6 056FA614-F3ED-4C58-BF5C-4A0271450A3B 142.250.204.34:443 quic-connection, url: https://googleads.g.doubleclick.net/mads, tls, definite, known tracker, attribution: developer] cancel
default	09:45:26.495898+0800	hootowl	kExcludedFromBackupXattrName set on path: /var/mobile/Containers/Data/Application/9C61D988-8BEB-42B6-A397-1E3A058F7BB4/Library/Application Support/gad
default	09:45:26.495914+0800	hootowl	[C6 056FA614-F3ED-4C58-BF5C-4A0271450A3B 142.250.204.34:443 quic-connection, url: https://googleads.g.doubleclick.net/mads, tls, definite, known tracker, attribution: developer] cancelled
	[C6 5ADB97CE-0A43-4EB9-A7F4-316B156F867E 192.168.50.191:60042<->142.250.204.34:443]
	Connected Path: satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good
	Duration: 1.005s, QUIC @0.045s took 0.000s,  took 0.737s
	bytes in/out: 9397/3805, packets in/out: 9/7, rtt: 0.185s, retransmitted bytes: 0, out-of-order bytes: 1184
	ecn packets sent/acked/marked/lost: 0/2/0/0
default	09:45:26.496526+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C6] reporting state cancelled
default	09:45:26.496751+0800	hootowl	quic_conn_log_summary [C3.1.1.2:2] [-ef404a5265fed4a6] 
	Connection attempts: 1, RETRY received: no, PTOs: 0
	Early data: no, Keep-alives sent/acknowledged: 0/0, ECN state: handshake validation succeeded, L4S: disabled
	RTT: base 185 ms, network 185 ms, latest 185 ms, minimum 185 ms, smoothed 185 ms (variance 69 ms)
	Path MTU: 1280, minimum MSS: 1200
	Migration events: 0, paths validated: 0
	Inbound unidirectional/bidirectional streams: 0/0
	Outbound unidirectional/bidirectional streams: 0/0
	DATA_BLOCKED frames sent/received: 0/0
	STREAM_DATA_BLOCKED frames sent/received: 0/0
default	09:45:26.497231+0800	hootowl	quic_conn_drain [C3.1.1.2:2] [-ef404a5265fed4a6] QUIC Packets:
	snd    0.000s LH<initial, 0>
			CRYPTO[0;999]
			PADDING[-1]
	snd    0.000s LH<initial, 1>
			CRYPTO[999;1500]
			PADDING[-1]
	rcv    0.186s LH<initial, 1>
			ACK[0]
				(0, 0)
	rcv    0.000s LH<initial, 2>
			ACK[1]
				(0, 1)
			PADDING[1156]
	rcv    0.000s LH<initial, 3>
			CRYPTO[0;1118]
			PADDING[42]
	rcv    0.000s LH<initial, 4>
			CRYPTO[1118;1121]
			PADDING[1156]
	rcv    0.000s LH<initial, 5>
			CRYPTO[1121;1178]
			PADDING[1103]
	rcv    0.054s LH<handshake, 6>
			CRYPTO[0;1162]
	rcv    0.000s LH<handshake, 7>
			CRYPTO[1162;2323]
	snd    0.000s LH<initial, 2>
			ACK[5]
				(1, 5)
			PADDING[-1]
	snd    0.000s LH<handshake, 0>
			ACK[7]
				(6, 7)
	rcv    0.133s LH<handshake, 8>
			CRYPTO[2323;3484]
	rcv    0.000s LH<handshake, 9>
			CRYPTO[3484;4332]
	snd    0.001s LH<handshake, 1>
			ACK[9]
				(6, 9)
	snd    0.362s LH<handshake, 2>
			CRYPTO[0;52]
	snd    0.222s LH<handshake, 3>
			CONNECTION_CLOSE[code=0, type=0]
default	09:45:26.497337+0800	hootowl	[C3.1.1.1 142.250.77.194:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @1.857s
default	09:45:26.497396+0800	hootowl	[C3.1.1 googleads.g.doubleclick.net:443 ready resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @1.857s
default	09:45:26.497416+0800	hootowl	[C3.1 googleads.g.doubleclick.net:443 ready transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @1.857s
default	09:45:26.497426+0800	hootowl	nw_flow_connected [C3 142.250.77.194:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (endpoint_flow)
default	09:45:26.497448+0800	hootowl	[C3 142.250.77.194:443 ready parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_connect @1.857s
default	09:45:26.497538+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C3] reporting state ready
default	09:45:26.497545+0800	hootowl	[C3 142.250.77.194:443 ready parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @1.858s
default	09:45:26.497561+0800	hootowl	nw_connection_send_viability_changed_on_nw_queue [C3] viability_changed_handler(true)
default	09:45:26.497596+0800	hootowl	Received state update for 46045 (app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>, unknown-NotVisible
error	09:45:26.539895+0800	hootowl	nw_protocol_instance_set_output_handler Not calling remove_input_handler on 0x1498b4b40:udp
default	09:45:26.539943+0800	hootowl	quic_migration_path_event_block_invoke [C3.1.1.1:2] [-ebc6555c6e5fb672] path 5d5b3dc1515f1522 over en0 received event established
default	09:45:26.540096+0800	hootowl	quic_migration_evaluate_primary [C3.1.1.1:2] [-ebc6555c6e5fb672] promoted path 0x14a32a4c0 over en0 to primary
default	09:45:26.540113+0800	hootowl	quic_migration_path_event_block_invoke [C3.1.1.1:2] [-ebc6555c6e5fb672] path 9bc43684553333e0 over pdp_ip0 received event available
error	09:45:26.540915+0800	hootowl	quic_conn_setup_pmtud [C3.1.1.1:2] [-ebc6555c6e5fb672] unable to query remote endpoint, assuming IPv6
default	09:45:26.541018+0800	hootowl	quic_pmtud_restart [C3.1.1.1:2] [-ebc6555c6e5fb672] PMTUD enabled, max PMTU: 1450, header size: 48, current PMTU 1248
default	09:45:26.541054+0800	hootowl	quic_migration_evaluate [C3.1.1.1:2] [-ebc6555c6e5fb672] evaluating path migration
default	09:45:26.541070+0800	hootowl	quic_migration_evaluate_block_invoke [C3.1.1.1:2] [-ebc6555c6e5fb672] path 9bc43684553333e0 state available (0), ifname pdp_ip0, primary? 0, initial? 0, fallback? 0, preferred? 0 lossy? 0
default	09:45:26.541111+0800	hootowl	quic_migration_evaluate_block_invoke [C3.1.1.1:2] [-ebc6555c6e5fb672] path 5d5b3dc1515f1522 state validated (0), ifname en0, primary? 1, initial? 1, fallback? 0, preferred? 0 lossy? 0
default	09:45:26.541155+0800	hootowl	quic_migration_evaluate [C3.1.1.1:2] [-ebc6555c6e5fb672] current path is usable, no strong fallback or we are probing
default	09:45:26.541173+0800	hootowl	nw_protocol_instance_report_ready [C3.1.1.1:2] Calling notify with interface en0 for flow_registration A8EFDE62-7278-4AD9-9B91-246BACB33BBC
default	09:45:26.541330+0800	hootowl	[C3.1.1.1 142.250.77.194:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:migrated @1.900s, uuid: A101BF3F-A8AE-480C-9F42-6D7EF2D1609E
default	09:45:26.541445+0800	hootowl	[C3.1.1 googleads.g.doubleclick.net:443 ready resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:migrated @1.900s, uuid: 8DEA39AC-CA18-47A4-817E-7774DE7A72C6
default	09:45:26.541469+0800	hootowl	[C3.1 googleads.g.doubleclick.net:443 ready transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:migrated @1.900s, uuid: 8DEA39AC-CA18-47A4-817E-7774DE7A72C6
default	09:45:26.541481+0800	hootowl	[C3 142.250.77.194:443 ready parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:migrated @1.900s, uuid: 8DEA39AC-CA18-47A4-817E-7774DE7A72C6
default	09:45:26.541501+0800	hootowl	quic_stream_create_inbound [C3.1.1.1:2] [-ebc6555c6e5fb672] creating inbound stream 3
default	09:45:26.541650+0800	hootowl	quic_migration_evaluate [C3.1.1.1:2] [-ebc6555c6e5fb672] evaluating path migration
default	09:45:26.541713+0800	hootowl	quic_migration_evaluate_block_invoke [C3.1.1.1:2] [-ebc6555c6e5fb672] path 9bc43684553333e0 state available (0), ifname pdp_ip0, primary? 0, initial? 0, fallback? 0, preferred? 0 lossy? 0
default	09:45:26.541742+0800	hootowl	quic_migration_evaluate_block_invoke [C3.1.1.1:2] [-ebc6555c6e5fb672] path 5d5b3dc1515f1522 state validated (0), ifname en0, primary? 1, initial? 1, fallback? 0, preferred? 0 lossy? 0
default	09:45:26.541769+0800	hootowl	quic_migration_evaluate [C3.1.1.1:2] [-ebc6555c6e5fb672] current path is usable, no strong fallback or we are probing
default	09:45:26.581624+0800	hootowl	Connection 3: connected successfully
default	09:45:26.581650+0800	hootowl	Connection 3: TLS handshake complete
default	09:45:26.581680+0800	hootowl	Connection 3: ready C(N) E(N)
default	09:45:26.582436+0800	hootowl	[ATTrackingManager] trackingAuthorizationStatus API call invoked.
default	09:45:26.582473+0800	hootowl	(Trust 0x14a3340c0) No pending evals, starting
default	09:45:26.582575+0800	hootowl	[ATTrackingManager] Performing TCC Access Preflight Request.
default	09:45:26.582834+0800	hootowl	[ATTrackingManager] Returning from trackingAuthorizationStatus - 0
default	09:45:26.583050+0800	hootowl	[0x1496c4c80] activating connection: mach=true listener=false peer=false name=com.apple.trustd
default	09:45:26.583302+0800	hootowl	(Trust 0x14a3340c0) Completed async eval kickoff
default	09:45:26.656678+0800	hootowl	tcp_input [C7.1.1.1:3] flags=[S.E] seq=2244845253, ack=820729280, win=14520 state=SYN_SENT rcv_nxt=0, snd_una=820729279
default	09:45:26.656841+0800	hootowl	(Trust 0x14a3340c0) trustd returned 4
default	09:45:26.656847+0800	hootowl	nw_flow_connected [C7.1.1.1 61.60.98.243:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Transport protocol connected (tcp)
default	09:45:26.657032+0800	hootowl	[C7.1.1.1 61.60.98.243:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_transport @1.064s
default	09:45:26.657645+0800	hootowl	boringssl_session_apply_protocol_options_for_transport_block_invoke_2(2367) [C7.1.1.1:2][0x14a4656e0] TLS configured [server(0) min_version(0x0303) max_version(0x0304) name(data.ntpc.gov.tw) tickets(false) false_start(false) enforce_ev(false) enforce_ats(false) ats_non_pfs_ciphersuite_allowed(false) cc_mode_enforced(false) ech(false) pqtls(true), pake(false) skip_ats_trust(false)]
default	09:45:26.657691+0800	hootowl	boringssl_context_info_handler(2806) [C7.1.1.1:2][0x14a4656e0] Client handshake started
default	09:45:26.657999+0800	hootowl	[0x1496c4c80] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	09:45:26.658061+0800	hootowl	boringssl_context_info_handler(2823) [C7.1.1.1:2][0x14a4656e0] Client handshake state: TLS client enter_early_data
default	09:45:26.658298+0800	hootowl	boringssl_context_info_handler(2823) [C7.1.1.1:2][0x14a4656e0] Client handshake state: TLS client read_server_hello
default	09:45:26.729940+0800	hootowl	[0x1496c4140] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	09:45:26.730037+0800	hootowl	AAFService connection invalidated
default	09:45:26.730989+0800	hootowl	boringssl_context_info_handler(2823) [C4.1.2.1:2][0x14a465960] Client handshake state: TLS 1.3 client read_hello_retry_request
default	09:45:26.731004+0800	hootowl	boringssl_context_info_handler(2823) [C4.1.2.1:2][0x14a465960] Client handshake state: TLS 1.3 client read_server_hello
default	09:45:26.731190+0800	hootowl	boringssl_context_info_handler(2823) [C4.1.2.1:2][0x14a465960] Client handshake state: TLS 1.3 client read_encrypted_extensions
default	09:45:26.731587+0800	hootowl	boringssl_context_info_handler(2823) [C4.1.2.1:2][0x14a465960] Client handshake state: TLS 1.3 client read_certificate_request
default	09:45:26.731601+0800	hootowl	boringssl_context_info_handler(2823) [C4.1.2.1:2][0x14a465960] Client handshake state: TLS 1.3 client read_server_certificate
default	09:45:26.731611+0800	hootowl	boringssl_context_info_handler(2823) [C4.1.2.1:2][0x14a465960] Client handshake state: TLS 1.3 client read_server_certificate_verify
default	09:45:26.732537+0800	hootowl	boringssl_context_evaluate_trust_async(2249) [C4.1.2.1:2][0x14a465960] Performing external trust evaluation
default	09:45:26.732729+0800	hootowl	boringssl_context_evaluate_trust_async_external(2234) [C4.1.2.1:2][0x14a465960] Asyncing for external verify block
default	09:45:26.787789+0800	hootowl	boringssl_context_new_session_handler(1771) [C5:1][0x149a907e0] Asyncing for session update block
default	09:45:26.787858+0800	hootowl	boringssl_context_new_session_handler(1771) [C5:1][0x149a907e0] Asyncing for session update block
default	09:45:26.787894+0800	hootowl	nw_protocol_boringssl_signal_connected(895) [C5:1][0x149a907e0] TLS connected [server(0) version(0x0304) ciphersuite(TLS_AES_256_GCM_SHA384) group(0x11ec) signature_alg(0x0403) alpn(h3) resumed(0) offered_ticket(0) in_early_data(0) early_data_accepted(0) false_started(0) ocsp_received(0) sct_received(0) connect_time(1116ms) flight_time(279ms) rtt(238ms) write_stalls(0) read_stalls(7) pake(0x0000)]
default	09:45:26.787918+0800	hootowl	nw_flow_connected [C5 142.250.77.194:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (tls)
default	09:45:26.788855+0800	hootowl	[C3] event: client:connection_reused @2.144s
default	09:45:26.789047+0800	hootowl	Task <C2039A11-85CB-4491-A2C8-C0CC08B408EC>.<1> now using Connection 3
default	09:45:26.791167+0800	hootowl	(Trust 0x14a337e40) trustd returned 4
default	09:45:26.791279+0800	hootowl	Connection 4: TLS Trust result 0
default	09:45:26.791294+0800	hootowl	boringssl_context_evaluate_trust_async_external_block_invoke_3(2148) [C8:1][0x149a93c60] Returning from external verify block with result: true
default	09:45:26.791507+0800	hootowl	boringssl_context_certificate_verify_callback(2430) [C8:1][0x149a93c60] Certificate verification result: OK
default	09:45:26.791516+0800	hootowl	boringssl_context_info_handler(2823) [C8:1][0x149a93c60] Client handshake state: TLS 1.3 client read_server_finished
default	09:45:26.791536+0800	hootowl	boringssl_context_info_handler(2823) [C8:1][0x149a93c60] Client handshake state: TLS 1.3 client send_end_of_early_data
default	09:45:26.791568+0800	hootowl	boringssl_context_info_handler(2823) [C8:1][0x149a93c60] Client handshake state: TLS 1.3 client send_client_encrypted_extensions
default	09:45:26.791578+0800	hootowl	boringssl_context_info_handler(2823) [C8:1][0x149a93c60] Client handshake state: TLS 1.3 client send_client_certificate
default	09:45:26.791593+0800	hootowl	boringssl_context_info_handler(2823) [C8:1][0x149a93c60] Client handshake state: TLS 1.3 client complete_second_flight
default	09:45:26.832644+0800	hootowl	boringssl_context_info_handler(2823) [C8:1][0x149a93c60] Client handshake state: TLS 1.3 client done
default	09:45:26.832660+0800	hootowl	boringssl_context_info_handler(2823) [C8:1][0x149a93c60] Client handshake state: TLS client finish_client_handshake
default	09:45:26.832669+0800	hootowl	boringssl_context_info_handler(2823) [C8:1][0x149a93c60] Client handshake state: TLS client done
default	09:45:26.832676+0800	hootowl	boringssl_context_info_handler(2812) [C8:1][0x149a93c60] Client handshake done
default	09:45:26.832782+0800	hootowl	App is being debugged, do not track this hang
default	09:45:26.832798+0800	hootowl	Hang detected: 0.55s (debugger attached, not reporting)
default	09:45:26.835125+0800	hootowl	nw_protocol_boringssl_signal_connected(895) [C8:1][0x149a93c60] TLS connected [server(0) version(0x0304) ciphersuite(TLS_AES_256_GCM_SHA384) group(0x11ec) signature_alg(0x0403) alpn(h3) resumed(0) offered_ticket(0) in_early_data(0) early_data_accepted(0) false_started(0) ocsp_received(0) sct_received(0) connect_time(1111ms) flight_time(57ms) rtt(56ms) write_stalls(0) read_stalls(7) pake(0x0000)]
default	09:45:26.835218+0800	hootowl	nw_flow_connected [C8 142.250.192.130:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (tls)
default	09:45:26.836323+0800	hootowl	[C8 142.250.192.130:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_connect @1.112s
default	09:45:26.836374+0800	hootowl	sceneOfRecord: sceneID: sceneID:com.sharkda.hootowl-83FF55F6-7B28-4BFD-8825-33CB43E5D162  persistentID: 83FF55F6-7B28-4BFD-8825-33CB43E5D162
default	09:45:26.837948+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C8] reporting state ready
default	09:45:26.837999+0800	hootowl	[C8 142.250.192.130:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @1.112s
default	09:45:26.838854+0800	hootowl	[0x1496c43c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	09:45:26.839071+0800	hootowl	tcp_output [C3.1.2.1:3] flags=[F.] seq=3362155974, ack=3214503114, win=2048 state=FIN_WAIT_1 rcv_nxt=3214503114, snd_una=3362155974
default	09:45:26.839082+0800	hootowl	0x131030270 - [PID=46065, throttler=0x131114220] ProcessThrottler::Activity::invalidate: Ending foreground activity / 'Process initialization'
default	09:45:26.844624+0800	hootowl	handleKeyboardChange: set currentKeyboard:N (wasKeyboard:N)
default	09:45:26.844652+0800	hootowl	forceReloadInputViews
default	09:45:26.844686+0800	hootowl	Reloading input views for key-window scene responder: <(null): 0x0; > force:Y
default	09:45:26.892429+0800	hootowl	[0x149614a00] Re-initialization successful; calling out to event handler with XPC_ERROR_CONNECTION_INTERRUPTED
default	09:45:26.892447+0800	hootowl	isWritingToolsHandlingKeyboardTracking:Y (WT ready:Y, Arbiter ready:Y)
default	09:45:26.892453+0800	hootowl	WebContent[0] 0x11206c100 - [sessionID=1] WebProcess::initializeLogForwarding: Debug logging enabled: 1
default	09:45:26.892460+0800	hootowl	WebContent[0] WebProcess::platformInitializeWebProcess
default	09:45:26.892477+0800	hootowl	quic_path_destroy [C3.1.1.2:2] [-ef404a5265fed4a6] destroying path 0x14a32b480
default	09:45:26.892754+0800	hootowl	WebContent[0] [0x10544eee0] Connection returned listener port: 0x1903
default	09:45:26.892883+0800	hootowl	WebContent[0] [0x105451c60] activating connection: mach=false listener=false peer=false name=(anonymous)
default	09:45:26.892891+0800	hootowl	WebContent[0] [0x108dc8000] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0x10544eee0.peer[46063].0x108dc8000
default	09:45:26.893399+0800	hootowl	boringssl_context_new_session_handler_block_invoke(1774) [C5:1][0x149a907e0] Returning from session update block
default	09:45:26.893778+0800	hootowl	boringssl_context_new_session_handler_block_invoke(1774) [C5:1][0x149a907e0] Returning from session update block
default	09:45:26.894059+0800	hootowl	WebContent[0] Application accessibility enabled: 1, (
	0   libAccessibility.dylib              0x00000001943ea920 _AXSApplicationAccessibilitySetEnabled + 84
	1   WebKit                              0x00000001ace77730 C39BD22C-3475-38AF-91BD-0B7574081011 + 12146480
	2   WebKit                              0x00000001ad0d054c C39BD22C-3475-38AF-91BD-0B7574081011 + 14607692
	3   WebKit                              0x00000001ac8f43f4 C39BD22C-3475-38AF-91BD-0B7574081011 + 6366196
	4   WebKit                              0x00000001ad58b714 C39BD22C-3475-38AF-91BD-0B7574081011 + 19568404
	5   WebKit                              0x00000001ad5b23a8 C39BD22C-3475-38AF-91BD-0B7574081011 + 19727272
	6   JavaScriptCore                      0x00000001a68da140 F7906028-1C6D-3B4C-BD93-78C196C83A83 + 692544
	7   JavaScriptCore                      0x00000001a68db6f8 F7906028-1C6D-3B4C-BD93-78C196C83A83 + 698104
	8   CoreFoundation                      0x0000000191073390 101EB2F1-1915-34A0-8BC9-631D03753B84 + 656272
	9   CoreFoundation                      0x000
default	09:45:26.894082+0800	hootowl	Connection 3: received viability advisory(Y)
default	09:45:26.894088+0800	hootowl	WebContent[0] Stored App AX setting: 1
default	09:45:26.894102+0800	hootowl	WebContent[0] AXS AccessibilityEnabled: (app ax: 1), ax settings: 1, cached: 1
default	09:45:26.894522+0800	hootowl	0x14a329518 ID=0 Task <C2039A11-85CB-4491-A2C8-C0CC08B408EC>.<1> sent request, body N 0
default	09:45:26.958640+0800	hootowl	quic_pmtud_restart [C4.1.1.1:2] [-e32b4ec180156458] PMTUD enabled, max PMTU: 1500, header size: 28, current PMTU 1228
default	09:45:26.958690+0800	hootowl	quic_crypto_tls_ready_inner [C4.1.1.1:2] [-e32b4ec180156458] QUIC connection established in 1235.26 ms, RTT 71.083 ms
default	09:45:26.958720+0800	hootowl	nw_flow_connected [C4.1.1.1 142.250.192.130:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Transport protocol connected (quic-connection)
default	09:45:26.958890+0800	hootowl	[C4.1.1.1 142.250.192.130:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_transport @2.263s
default	09:45:26.959170+0800	hootowl	nw_flow_connected [C4.1.1.1 142.250.192.130:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (CFNetworkConnection-4283075305)
default	09:45:26.959330+0800	hootowl	[C4.1.1.1 142.250.192.130:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @2.263s
default	09:45:26.959633+0800	hootowl	[C4.1.1 pubads.g.doubleclick.net:443 ready resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @2.263s
default	09:45:26.959671+0800	hootowl	[C4.1 pubads.g.doubleclick.net:443 ready transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @2.263s
default	09:45:26.961160+0800	hootowl	nw_protocol_tcp_log_summary [C4.1.2.1:3] 
	[1432DF75-F26B-4AE0-B9FD-515FA0DD4ECD 192.168.50.191:50793<->142.250.192.130:443]
	Init: 1, Conn_Time: 179.419ms, SYNs: 1, WR_T: 0/0, RD_T: 0/0, TFO: 0/0/0, ECN: 0/1/1, Accurate ECN (client/server): Disabled/Disabled, TS: 1, TSO: 0
	rtt_cache: none, rtt_upd: 2, rtt: 229.125ms, rtt_var: 165.750ms rtt_nc: 229.125ms, rtt_var_nc: 165.750ms base rtt: 180ms
	ACKs-compressed: 0, ACKs delayed: 0 delayed ACKs sent: 0
default	09:45:26.961534+0800	hootowl	TX focusApplication (peekAppEvent) stealKB:Y scene:com.sharkda.hootowl-83FF55F6-7B28-4BFD-8825-33CB43E5D162
default	09:45:26.961554+0800	hootowl	[C4.1.1.1 142.250.192.130:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @2.264s
default	09:45:26.962070+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:26.962078+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	09:45:26.962222+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1481fc400>; contextId: 0xF4D9041F
default	09:45:26.962244+0800	hootowl	[C4.1.1 pubads.g.doubleclick.net:443 ready resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @2.264s
default	09:45:27.010698+0800	hootowl	[C4.1 pubads.g.doubleclick.net:443 ready transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @2.317s
default	09:45:27.010831+0800	hootowl	nw_flow_connected [C4 142.250.192.130:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (endpoint_flow)
default	09:45:27.010893+0800	hootowl	[C4 142.250.192.130:443 ready parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_connect @2.317s
default	09:45:27.011127+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C4] reporting state ready
default	09:45:27.011137+0800	hootowl	[C4 142.250.192.130:443 ready parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @2.318s
default	09:45:27.011145+0800	hootowl	nw_connection_send_viability_changed_on_nw_queue [C4] viability_changed_handler(true)
error	09:45:27.011480+0800	hootowl	nw_protocol_instance_set_output_handler Not calling remove_input_handler on 0x14a3243c0:udp
default	09:45:27.011521+0800	hootowl	quic_migration_path_event_block_invoke [C4.1.1.1:2] [-e32b4ec180156458] path 82354ac5733a4fe4 over en0 received event established
default	09:45:27.011892+0800	hootowl	quic_migration_evaluate_primary [C4.1.1.1:2] [-e32b4ec180156458] promoted path 0x1499be140 over en0 to primary
default	09:45:27.011913+0800	hootowl	quic_migration_path_event_block_invoke [C4.1.1.1:2] [-e32b4ec180156458] path ecb347eb50b0dcca over pdp_ip0 received event available
error	09:45:27.011996+0800	hootowl	quic_conn_setup_pmtud [C4.1.1.1:2] [-e32b4ec180156458] unable to query remote endpoint, assuming IPv6
default	09:45:27.012029+0800	hootowl	quic_pmtud_restart [C4.1.1.1:2] [-e32b4ec180156458] PMTUD enabled, max PMTU: 1450, header size: 48, current PMTU 1248
default	09:45:27.012073+0800	hootowl	quic_migration_evaluate [C4.1.1.1:2] [-e32b4ec180156458] evaluating path migration
default	09:45:27.012085+0800	hootowl	quic_migration_evaluate_block_invoke [C4.1.1.1:2] [-e32b4ec180156458] path ecb347eb50b0dcca state available (0), ifname pdp_ip0, primary? 0, initial? 0, fallback? 0, preferred? 0 lossy? 0
default	09:45:27.012094+0800	hootowl	quic_migration_evaluate_block_invoke [C4.1.1.1:2] [-e32b4ec180156458] path 82354ac5733a4fe4 state validated (0), ifname en0, primary? 1, initial? 1, fallback? 0, preferred? 0 lossy? 0
default	09:45:27.012100+0800	hootowl	quic_migration_evaluate [C4.1.1.1:2] [-e32b4ec180156458] current path is usable, no strong fallback or we are probing
default	09:45:27.012108+0800	hootowl	nw_protocol_instance_report_ready [C4.1.1.1:2] Calling notify with interface en0 for flow_registration DDEA91A4-0837-4E64-B8E5-40924A8E6DDF
default	09:45:27.012207+0800	hootowl	[C4.1.1.1 142.250.192.130:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:migrated @2.319s, uuid: 670F6F90-7919-43DE-83E6-E591C366577F
default	09:45:27.012341+0800	hootowl	[C4.1.1 pubads.g.doubleclick.net:443 ready resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:migrated @2.319s, uuid: 7CF2FF01-4B92-45FA-A5C4-81DD637FF6D5
default	09:45:27.012361+0800	hootowl	[C4.1 pubads.g.doubleclick.net:443 ready transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:migrated @2.319s, uuid: 7CF2FF01-4B92-45FA-A5C4-81DD637FF6D5
default	09:45:27.012370+0800	hootowl	[C4 142.250.192.130:443 ready parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:migrated @2.319s, uuid: 7CF2FF01-4B92-45FA-A5C4-81DD637FF6D5
default	09:45:27.012418+0800	hootowl	quic_stream_create_inbound [C4.1.1.1:2] [-e32b4ec180156458] creating inbound stream 3
default	09:45:27.012826+0800	hootowl	quic_migration_evaluate [C4.1.1.1:2] [-e32b4ec180156458] evaluating path migration
default	09:45:27.012856+0800	hootowl	quic_migration_evaluate_block_invoke [C4.1.1.1:2] [-e32b4ec180156458] path ecb347eb50b0dcca state available (0), ifname pdp_ip0, primary? 0, initial? 0, fallback? 0, preferred? 0 lossy? 0
default	09:45:27.012867+0800	hootowl	quic_migration_evaluate_block_invoke [C4.1.1.1:2] [-e32b4ec180156458] path 82354ac5733a4fe4 state validated (0), ifname en0, primary? 1, initial? 1, fallback? 0, preferred? 0 lossy? 0
default	09:45:27.012876+0800	hootowl	quic_migration_evaluate [C4.1.1.1:2] [-e32b4ec180156458] current path is usable, no strong fallback or we are probing
default	09:45:27.013251+0800	hootowl	boringssl_context_new_session_handler(1771) [C8:1][0x149a93c60] Asyncing for session update block
default	09:45:27.066179+0800	hootowl	boringssl_context_new_session_handler(1771) [C8:1][0x149a93c60] Asyncing for session update block
default	09:45:27.066323+0800	hootowl	WebContent[46063]: [renderingBackend=11] Created rendering backend for pageProxyID=7, webPageID=8
default	09:45:27.066509+0800	hootowl	WebContent[46063] GPUProcessConnection::create - 0x11208cd20
default	09:45:27.066823+0800	hootowl	nw_protocol_boringssl_signal_connected(895) [C8:1][0x149a93c60] TLS connected [server(0) version(0x0304) ciphersuite(TLS_AES_256_GCM_SHA384) group(0x11ec) signature_alg(0x0403) alpn(h3) resumed(0) offered_ticket(0) in_early_data(0) early_data_accepted(0) false_started(0) ocsp_received(0) sct_received(0) connect_time(1111ms) flight_time(57ms) rtt(56ms) write_stalls(0) read_stalls(7) pake(0x0000)]
default	09:45:27.066874+0800	hootowl	nw_flow_connected [C8 142.250.192.130:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (tls)
default	09:45:27.068125+0800	hootowl	tcp_input [C3.1.2.1:3] flags=[F.] seq=3214503114, ack=3362155975, win=1044 state=FIN_WAIT_1 rcv_nxt=3214503114, snd_una=3362155974
default	09:45:27.068481+0800	hootowl	quic_stream_create_inbound [C3.1.1.1:2] [-ebc6555c6e5fb672] creating inbound stream 7 (out of order)
default	09:45:27.068849+0800	hootowl	quic_stream_create_inbound [C3.1.1.1:2] [-ebc6555c6e5fb672] creating inbound stream 11
default	09:45:27.071080+0800	hootowl	boringssl_context_info_handler(2823) [C7.1.1.1:2][0x14a4656e0] Client handshake state: TLS client read_server_certificate
default	09:45:27.071306+0800	hootowl	boringssl_context_info_handler(2823) [C7.1.1.1:2][0x14a4656e0] Client handshake state: TLS client read_certificate_status
default	09:45:27.071326+0800	hootowl	boringssl_context_info_handler(2823) [C7.1.1.1:2][0x14a4656e0] Client handshake state: TLS client verify_server_certificate
default	09:45:27.072077+0800	hootowl	boringssl_context_evaluate_trust_async(2249) [C7.1.1.1:2][0x14a4656e0] Performing external trust evaluation
default	09:45:27.072566+0800	hootowl	boringssl_context_evaluate_trust_async_external(2234) [C7.1.1.1:2][0x14a4656e0] Asyncing for external verify block
default	09:45:27.073035+0800	hootowl	Connection 4: connected successfully
default	09:45:27.106381+0800	hootowl	Connection 4: TLS handshake complete
default	09:45:27.106602+0800	hootowl	Connection 4: ready C(N) E(N)
default	09:45:27.107064+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:27.107245+0800	hootowl	[C4] event: client:connection_reused @2.414s
default	09:45:27.107316+0800	hootowl	Task <334043C8-A557-4E46-B7B4-FF53031998B9>.<2> now using Connection 4
default	09:45:27.107806+0800	hootowl	tcp_output [C4.1.2.1:3] flags=[F.] seq=3488198402, ack=950018048, win=2048 state=FIN_WAIT_1 rcv_nxt=950018048, snd_una=3488198402
default	09:45:27.108120+0800	hootowl	boringssl_context_new_session_handler_block_invoke(1774) [C8:1][0x149a93c60] Returning from session update block
default	09:45:27.151726+0800	hootowl	Received state update for 46045 (app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>, unknown-NotVisible
default	09:45:27.151782+0800	hootowl	Connection 7: asked to evaluate TLS Trust
default	09:45:27.152277+0800	hootowl	quic_stream_create_inbound [C4.1.1.1:2] [-e32b4ec180156458] creating inbound stream 7 (out of order)
default	09:45:27.152365+0800	hootowl	quic_stream_create_inbound [C4.1.1.1:2] [-e32b4ec180156458] creating inbound stream 11
default	09:45:27.189042+0800	hootowl	tcp_input [C4.1.2.1:3] flags=[F.] seq=950018048, ack=3488198403, win=1045 state=FIN_WAIT_1 rcv_nxt=950018048, snd_una=3488198402
default	09:45:27.189275+0800	hootowl	Connection 4: received viability advisory(Y)
default	09:45:27.189883+0800	hootowl	0x14a329358 ID=0 Task <334043C8-A557-4E46-B7B4-FF53031998B9>.<2> sent request, body N 0
default	09:45:27.190443+0800	hootowl	0x14a329358 ID=0 Task <334043C8-A557-4E46-B7B4-FF53031998B9>.<2> received response, status 404 content U
default	09:45:27.190582+0800	hootowl	[0x1496c5a40] activating connection: mach=true listener=false peer=false name=com.apple.trustd
default	09:45:27.239006+0800	hootowl	[0x1496c5a40] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	09:45:27.239017+0800	hootowl	<nw_activity 50:1 [31E16363-B2E4-420C-9B36-077529992770] (global parent) (reporting strategy default) complete (reason failure)> complete with reason 3 (failure), duration 20359ms
default	09:45:27.239070+0800	hootowl	<nw_activity 50:2 [EA7A4D16-5D7D-4603-9D2C-80DDCF872A85] (reporting strategy default) complete (reason failure)> complete with reason 3 (failure), duration 20360ms
default	09:45:27.239166+0800	hootowl	Unsetting the global parent activity <nw_activity 50:1 [31E16363-B2E4-420C-9B36-077529992770] (global parent) (reporting strategy default) complete (reason failure)>
default	09:45:27.239382+0800	hootowl	Unset the global parent activity
default	09:45:27.239464+0800	hootowl	Task <334043C8-A557-4E46-B7B4-FF53031998B9>.<2> response ended
default	09:45:27.239475+0800	hootowl	alm_release_pageins_recording_assertion: releasing pageins recording assertion
default	09:45:27.239798+0800	hootowl	[C4] event: client:connection_idle @2.547s
default	09:45:27.239881+0800	hootowl	Task <334043C8-A557-4E46-B7B4-FF53031998B9>.<2> done using Connection 4
default	09:45:27.240324+0800	hootowl	boringssl_context_new_session_handler_block_invoke(1774) [C8:1][0x149a93c60] Returning from session update block
default	09:45:27.240407+0800	hootowl	Task <334043C8-A557-4E46-B7B4-FF53031998B9>.<2> summary for task success {transaction_duration_ms=2601, response_status=404, connection=4, protocol="h3", domain_lookup_duration_ms=734, connect_duration_ms=1290, secure_connection_duration_ms=1235, private_relay=false, request_start_ms=2468, request_duration_ms=82, response_start_ms=2550, response_duration_ms=50, request_bytes=158, request_throughput_kbps=15, response_bytes=244, response_throughput_kbps=38, cache_hit=false}
default	09:45:27.240469+0800	hootowl	Task <334043C8-A557-4E46-B7B4-FF53031998B9>.<2> finished successfully
default	09:45:27.240549+0800	hootowl	Task <5100FD16-E95C-47E4-8962-4D6E52C0122F>.<3> auth completion disp=1 cred=0x0
default	09:45:27.240587+0800	hootowl	0x14a329518 ID=0 Task <C2039A11-85CB-4491-A2C8-C0CC08B408EC>.<1> received response, status 404 content U
default	09:45:27.240978+0800	hootowl	[0x1496c5a40] activating connection: mach=true listener=false peer=false name=com.apple.trustd
default	09:45:27.301610+0800	hootowl	[ATTrackingManager] trackingAuthorizationStatus API call invoked.
default	09:45:27.301717+0800	hootowl	[ATTrackingManager] Performing TCC Access Preflight Request.
default	09:45:27.303909+0800	hootowl	[ATTrackingManager] Returning from trackingAuthorizationStatus - 0
default	09:45:27.304017+0800	hootowl	[0x1496c5a40] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	09:45:27.304033+0800	hootowl	Task <C2039A11-85CB-4491-A2C8-C0CC08B408EC>.<1> response ended
default	09:45:27.304127+0800	hootowl	[C3] event: client:connection_idle @2.659s
default	09:45:27.304162+0800	hootowl	Task <C2039A11-85CB-4491-A2C8-C0CC08B408EC>.<1> done using Connection 3
default	09:45:27.304229+0800	hootowl	Task <C2039A11-85CB-4491-A2C8-C0CC08B408EC>.<1> summary for task success {transaction_duration_ms=2661, response_status=404, connection=3, protocol="h3", domain_lookup_duration_ms=133, connect_duration_ms=1499, secure_connection_duration_ms=1494, private_relay=false, request_start_ms=2147, request_duration_ms=109, response_start_ms=2602, response_duration_ms=58, request_bytes=159, request_throughput_kbps=11, response_bytes=94, response_throughput_kbps=12, cache_hit=false}
default	09:45:27.304723+0800	hootowl	Task <C2039A11-85CB-4491-A2C8-C0CC08B408EC>.<1> finished successfully
default	09:45:27.376518+0800	hootowl	Task <6CD5524D-F067-4C09-A823-5B80B55C7B03>.<2> response ended
default	09:45:27.376540+0800	hootowl	Task <6CD5524D-F067-4C09-A823-5B80B55C7B03>.<2> done using Connection 2
default	09:45:27.380984+0800	hootowl	Task <6CD5524D-F067-4C09-A823-5B80B55C7B03>.<2> summary for task success {transaction_duration_ms=4442, response_status=200, connection=2, protocol="http/1.1", domain_lookup_duration_ms=18, connect_duration_ms=438, secure_connection_duration_ms=353, private_relay=false, request_start_ms=1198, request_duration_ms=0, response_start_ms=1371, response_duration_ms=3070, request_bytes=248, request_throughput_kbps=19836, response_bytes=2857501, response_throughput_kbps=7444, cache_hit=false}
default	09:45:27.381203+0800	hootowl	Task <6CD5524D-F067-4C09-A823-5B80B55C7B03>.<2> finished successfully
default	09:45:27.381556+0800	hootowl	(Trust 0x1499d46c0) No pending evals, starting
default	09:45:27.382837+0800	hootowl	[0x1496c5cc0] activating connection: mach=true listener=false peer=false name=com.apple.trustd
default	09:45:27.384145+0800	hootowl	(Trust 0x1499d46c0) Completed async eval kickoff
default	09:45:27.444834+0800	hootowl	[0x1496c5a40] activating connection: mach=true listener=false peer=false name=com.apple.storekitd
default	09:45:27.444884+0800	hootowl	[C2] event: client:connection_idle @3.767s
default	09:45:27.444992+0800	hootowl	nw_protocol_tcp_notify [C2.1.1:3] nw_protocol_notification_type_connection_idle is true
default	09:45:27.445636+0800	hootowl	App is being debugged, do not track this hang
default	09:45:27.445642+0800	hootowl	Hang detected: 0.60s (debugger attached, not reporting)
default	09:45:27.445655+0800	hootowl	0x148ec1518 - [pageProxyID=7, webPageID=8, PID=46063] WebPageProxy::decidePolicyForNavigationAction: frameID=4294967297, isMainFrame=1, navigationID=13
default	09:45:27.445667+0800	hootowl	nw_protocol_tcp_set_connection_idle [C2.1.1:3] os_nexus_flow_set_connection_idle returned 0
default	09:45:27.545938+0800	hootowl	[C2] event: client:connection_idle @3.874s
default	09:45:27.546020+0800	hootowl	nw_protocol_tcp_notify [C2.1.1:3] nw_protocol_notification_type_connection_idle is true
default	09:45:27.546118+0800	hootowl	nw_protocol_tcp_set_connection_idle [C2.1.1:3] os_nexus_flow_set_connection_idle returned 0
default	09:45:27.546127+0800	hootowl	(Trust 0x1499d46c0) trustd returned 4
default	09:45:27.546206+0800	hootowl	System Trust Evaluation yielded status(0)
default	09:45:27.546612+0800	hootowl	(Trust 0x14987c600) No pending evals, starting
default	09:45:27.546633+0800	hootowl	[0x1496c5900] activating connection: mach=true listener=false peer=false name=com.apple.Safari.SafeBrowsing.Service
default	09:45:27.547102+0800	hootowl	[Default] Finished iterating transaction batches
default	09:45:27.626499+0800	hootowl	0x1310b40c0 - SOAuthorizationCoordinator::tryAuthorize
default	09:45:27.626516+0800	hootowl	Fetching native takeover URLs
default	09:45:27.626699+0800	hootowl	[0x1496c4140] activating connection: mach=true listener=false peer=false name=com.apple.ak.authorizationservices.xpc
default	09:45:27.626723+0800	hootowl	[0x1496c7480] activating connection: mach=true listener=false peer=false name=com.apple.trustd
default	09:45:27.626743+0800	hootowl	Successfully created a sandbox extension for '/private/var/mobile/Containers/Data/Application/9C61D988-8BEB-42B6-A397-1E3A058F7BB4/tmp/WebKit/MediaCache'
default	09:45:27.626754+0800	hootowl	Successfully created a sandbox extension for '/private/var/mobile/Containers/Data/Application/9C61D988-8BEB-42B6-A397-1E3A058F7BB4/Library/WebKit/WebsiteData/MediaKeys/v1'
default	09:45:27.626766+0800	hootowl	0x1310e41e0 - GPUProcessProxy is taking a background assertion because a web process is requesting a connection
default	09:45:27.626836+0800	hootowl	URL shouldn't be processed
default	09:45:27.627391+0800	hootowl	[ATTrackingManager] trackingAuthorizationStatus API call invoked.
default	09:45:27.627429+0800	hootowl	[ATTrackingManager] Performing TCC Access Preflight Request.
default	09:45:27.627823+0800	hootowl	[ATTrackingManager] Returning from trackingAuthorizationStatus - 0
default	09:45:27.627974+0800	hootowl	(Trust 0x14987c600) Completed async eval kickoff
default	09:45:27.628022+0800	hootowl	SOAuthorizationCoordinator::tryAuthorize: The requested URL is not registered for AppSSO handling. No further action needed.
default	09:45:27.628035+0800	hootowl	0x148ec1518 - [pageProxyID=7, webPageID=8, PID=46063] WebPageProxy::decidePolicyForNavigationAction: listener called: frameID=4294967297, isMainFrame=1, navigationID=13, policyAction=Use, isAppBoundDomain=0, wasNavigationIntercepted=0
default	09:45:27.628048+0800	hootowl	0x148ec1518 - [pageProxyID=7, webPageID=8, PID=46063] WebPageProxy::receivedNavigationActionPolicyDecision: frameID=4294967297, isMainFrame=1, navigationID=13, policyAction=Use
default	09:45:27.628057+0800	hootowl	[0x1496c5a40] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	09:45:27.630000+0800	hootowl	AAFService connection invalidated
default	09:45:27.630026+0800	hootowl	[0x1496c5cc0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	09:45:27.630191+0800	hootowl	[ATTrackingManager] trackingAuthorizationStatus API call invoked.
default	09:45:27.630456+0800	hootowl	[ATTrackingManager] Call to trackingAuthorizationStatus eligible for rate limiting. Returning 0
default	09:45:27.631578+0800	hootowl	[0x1496c5f40] activating connection: mach=true listener=false peer=false name=com.apple.audio.SystemSoundServer-iOS
default	09:45:27.712012+0800	hootowl	WebContent[46063] 0x11208cd20 - GPUProcessConnection::didInitialize
error	09:45:27.712565+0800	hootowl	WebContent[46063] Could not register system wide server: -25204
error	09:45:27.712572+0800	hootowl	WebContent[46063] _AXAddToElementCache was called even though the element was in the cache: <WKAccessibilityWebPageObject: 0x105452b20>
default	09:45:27.712603+0800	hootowl	WebContent[46063] Read Per-App on Init: Smart invert = (null)
default	09:45:27.713669+0800	hootowl	(Trust 0x14987c600) trustd returned 4
default	09:45:27.714416+0800	hootowl	0x148ec1518 - [pageProxyID=7, webPageID=8, PID=46063] WebPageProxy::decidePolicyForNavigationAction: keep using process 46063 for navigation, reason=Process has not yet committed any provisional loads
default	09:45:27.714442+0800	hootowl	0x1310740c0 - [PID=46063] WebProcessProxy::canTerminateAuxiliaryProcess: returns false (pageCount=1, remotePageCount=0, provisionalPageCount=0, suspendedPageCount=0, m_isInProcessCache=0, m_shutdownPreventingScopeCounter=0)
default	09:45:27.714454+0800	hootowl	0x1310e41e0 - GPUProcessProxy::didCreateContextForVisibilityPropagation: webPageProxyID: 7, pagePID: 8, contextID: 3
default	09:45:27.719182+0800	hootowl	Created visibility propagation interaction <_UIVisibilityPropagationInteraction: 0x148d3a580> for process with PID=46064
default	09:45:27.719602+0800	hootowl	Connection 7: TLS Trust result 0
default	09:45:27.719649+0800	hootowl	boringssl_context_evaluate_trust_async_external_block_invoke_3(2148) [C7.1.1.1:2][0x14a4656e0] Returning from external verify block with result: true
default	09:45:27.719851+0800	hootowl	RemoteLayerTreeDrawingAreaProxy(10)::hideContentUntilPendingUpdate completed
default	09:45:27.719904+0800	hootowl	WebContent[46063]: [webFrameID=4294967297, webPageID=8] WebFrameLoaderClient::dispatchDecidePolicyForNavigationAction: Got policyAction Use from async IPC
default	09:45:27.721322+0800	hootowl	RemoteLayerTreeDrawingAreaProxy(10) Unhiding layer tree
default	09:45:27.721337+0800	hootowl	WebContent[46063] 0x1120e0180 - [pageID=8, frameID=4294967297] PolicyChecker::checkNavigationPolicy: continuing because this policyAction from dispatchDecidePolicyForNavigationAction is Use
default	09:45:27.721366+0800	hootowl	boringssl_context_certificate_verify_callback(2430) [C7.1.1.1:2][0x14a4656e0] Certificate verification result: OK
default	09:45:27.721376+0800	hootowl	WebContent[46063]: [pageID=8 frameID=4294967297 isMainFrame=1] FrameLoader::stopAllLoaders: m_provisionalDocumentLoader=0, m_documentLoader=4614832128
fault	09:45:27.721384+0800	hootowl	The request of a upload task should not contain a body or a body stream, use `upload(for:fromFile:)`, `upload(for:from:)`, or supply the body stream through the `urlSession(_:needNewBodyStreamForTask:)` delegate method.
default	09:45:27.721395+0800	hootowl	WebContent[46063]: [pageID=8, frameID=4294967297, isMainFrame=1] DocumentLoader::stopLoading
default	09:45:27.721405+0800	hootowl	WebContent[46063]: [pageID=8 frameID=4294967297 isMainFrame=1] FrameLoader::setProvisionalDocumentLoader: Setting provisional document loader to 4614852608 (was 0)
default	09:45:27.721415+0800	hootowl	WebContent[46063]: [pageID=8 frameID=4294967297 isMainFrame=1] FrameLoader::continueLoadAfterNavigationPolicy: Setting provisional document loader (m_provisionalDocumentLoader=4614852608)
default	09:45:27.721435+0800	hootowl	WebContent[46063]: [webPageID=8] WebPage::freezeLayerTree: Adding a reason to freeze layer tree (reason=1, new=1, old=0)
default	09:45:27.721448+0800	hootowl	WebContent[46063]: [pageID=8 frameID=4294967297 isMainFrame=1] FrameLoader::setPolicyDocumentLoader: Setting policy document loader to 0 (was 4614852608)
default	09:45:27.721467+0800	hootowl	WebContent[46063]: [pageID=8 frameID=4294967297 isMainFrame=1] FrameLoader::prepareForLoadStart: Starting frame load
default	09:45:27.721483+0800	hootowl	WebContent[46063]: ProgressTracker::progressStarted: frameID 4294967297, value 0.100000, tracked frames 1, originating frameID 4294967297, isMainLoad 1
default	09:45:27.721628+0800	hootowl	WebContent[46063]: [pageID=8, frameID=4294967297, isMainFrame=1] DocumentLoader::startLoadingMainResource: Starting load
default	09:45:27.721673+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:27.721679+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	09:45:27.721693+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1481fc400>; contextId: 0xF4D9041F
default	09:45:27.721723+0800	hootowl	Task <93538818-97EE-404C-8274-265196A34402>.<5> resuming, timeouts(60.0, 604800.0) qos(0x15) voucher((null)) activity(00000000-0000-0000-0000-000000000000)
default	09:45:27.721750+0800	hootowl	boringssl_context_info_handler(2823) [C7.1.1.1:2][0x14a4656e0] Client handshake state: TLS client read_server_key_exchange
default	09:45:27.781868+0800	hootowl	WebContent[46063]: [pageID=8, frameID=4294967297, resourceID=18] ResourceLoader::willSendRequestInternal: calling completion handler
default	09:45:27.781887+0800	hootowl	WebContent[46063]: [pageID=8, frameID=4294967297, resourceID=18 SubResourceLoader::willSendRequestInternal: resource load finished; calling completion handler
default	09:45:27.781929+0800	hootowl	WebContent[46063]: [webPageID=8, frameID=4294967297, resourceID=18] WebLoaderStrategy::scheduleLoad: URL will be scheduled with the NetworkProcess
default	09:45:27.781953+0800	hootowl	WebContent[46063]: [webPageID=8, frameID=4294967297, resourceID=18] WebLoaderStrategy::scheduleLoad: Resource is being scheduled with the NetworkProcess (priority=4, existingNetworkResourceLoadIdentifierToResume=0)
default	09:45:27.781960+0800	hootowl	WebContent[46063]: [webPageID=8, frameID=4294967297, resourceID=18] WebResourceLoader::WebResourceLoader
error	09:45:27.783313+0800	hootowl	WebContent[46063] Service "com.apple.CARenderServer" failed bootstrap look up (1) - (os/kern) invalid address
default	09:45:27.783791+0800	hootowl	<UIWindowScene: 0x148378200> (83FF55F6-7B28-4BFD-8825-33CB43E5D162) Scene updated orientation preferences: ( Pu Ll Lr ) -> ( Pu )
default	09:45:27.784075+0800	hootowl	WebContent[46063] Evaluated capturing state as 0 on <UIScreen: 0x108ec88c0> for initial
error	09:45:27.784110+0800	hootowl	WebContent[46063] Failed to initialize application enviroment context
error	09:45:27.784164+0800	hootowl	WebContent[46063] Failed to load a device context.
error	09:45:27.784187+0800	hootowl	WebContent[46063] Failed to initialize application enviroment context
error	09:45:27.784193+0800	hootowl	WebContent[46063] Failed to load a device context.
default	09:45:27.784213+0800	hootowl	WebContent[46063] Read CategoryName: per-app = 1, category name = (null)
default	09:45:27.784235+0800	hootowl	WebContent[46063] Read CategoryName: per-app = 0, category name = UICTContentSizeCategoryXXXL
default	09:45:27.789110+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:27.789128+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 1
default	09:45:27.790010+0800	hootowl	WebContent[46063]: [webPageID=8, frameID=4294967297, resourceID=18] WebResourceLoader::didReceiveResponse: (httpStatusCode=200)
default	09:45:28.172792+0800	hootowl	boringssl_context_info_handler(2823) [C7.1.1.1:2][0x14a4656e0] Client handshake state: TLS client read_certificate_request
default	09:45:28.173485+0800	hootowl	boringssl_context_info_handler(2823) [C7.1.1.1:2][0x14a4656e0] Client handshake state: TLS client read_server_hello_done
default	09:45:28.173533+0800	hootowl	boringssl_context_info_handler(2823) [C7.1.1.1:2][0x14a4656e0] Client handshake state: TLS client send_client_certificate
default	09:45:28.173605+0800	hootowl	boringssl_context_info_handler(2823) [C7.1.1.1:2][0x14a4656e0] Client handshake state: TLS client send_client_key_exchange
default	09:45:28.173760+0800	hootowl	WebContent[46063] Loading PDFKit
default	09:45:28.174031+0800	hootowl	boringssl_context_info_handler(2823) [C7.1.1.1:2][0x14a4656e0] Client handshake state: TLS client send_client_certificate_verify
default	09:45:28.174094+0800	hootowl	boringssl_context_info_handler(2823) [C7.1.1.1:2][0x14a4656e0] Client handshake state: TLS client send_client_finished
default	09:45:28.174535+0800	hootowl	boringssl_context_info_handler(2823) [C7.1.1.1:2][0x14a4656e0] Client handshake state: TLS client finish_flight
default	09:45:28.174638+0800	hootowl	boringssl_context_info_handler(2823) [C7.1.1.1:2][0x14a4656e0] Client handshake state: TLS client read_session_ticket
default	09:45:28.174647+0800	hootowl	boringssl_context_info_handler(2823) [C7.1.1.1:2][0x14a4656e0] Client handshake state: TLS client process_change_cipher_spec
default	09:45:28.174846+0800	hootowl	[0x1496c7480] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	09:45:28.184750+0800	hootowl	Received state update for 46045 (app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>, unknown-NotVisible
default	09:45:28.186906+0800	hootowl	[C7.1.1 data.ntpc.gov.tw:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:children_stall @2.594s
default	09:45:28.186923+0800	hootowl	Connection 0: creating secure tcp or quic connection
default	09:45:28.187098+0800	hootowl	Connection 9: enabling TLS
default	09:45:28.187109+0800	hootowl	Connection 9: starting, TC(0x0)
default	09:45:28.187119+0800	hootowl	[C9 DD03EAE7-DE74-4954-8C19-3A6BD70FDEE8 us-central1-tataro2.cloudfunctions.net:443 quic-connection, url: https://us-central1-tataro2.cloudfunctions.net/verifyReceipt, definite, attribution: developer, context: com.apple.CFNetwork.NSURLSession.{D8375FAB-BCC3-47F6-9F42-2CD36CF9484B}{(null)}{Y}{2}{0x0} (private), proc: 1B526020-2DE0-3C65-9122-F1177549D69A, delegated upid: 0] start
default	09:45:28.187223+0800	hootowl	[C9 us-central1-tataro2.cloudfunctions.net:443 initial parent-flow ((null))] event: path:start @0.000s
default	09:45:28.188734+0800	hootowl	[C9 us-central1-tataro2.cloudfunctions.net:443 waiting parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.001s, uuid: 8947A3B0-E196-4106-B66C-E7013CF1305C
default	09:45:28.188812+0800	hootowl	[C9 us-central1-tataro2.cloudfunctions.net:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_connect @0.001s
default	09:45:28.188821+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C9] reporting state preparing
default	09:45:28.188925+0800	hootowl	[C9 us-central1-tataro2.cloudfunctions.net:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_child @0.001s
default	09:45:28.189001+0800	hootowl	[C9.1 us-central1-tataro2.cloudfunctions.net:443 initial path ((null))] event: path:start @0.001s
default	09:45:28.189497+0800	hootowl	[C9.1 us-central1-tataro2.cloudfunctions.net:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.001s, uuid: 8947A3B0-E196-4106-B66C-E7013CF1305C
default	09:45:28.189541+0800	hootowl	[C9.1 us-central1-tataro2.cloudfunctions.net:443 in_progress transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: transform:start @0.002s
default	09:45:28.237792+0800	hootowl	[C9.1.1 us-central1-tataro2.cloudfunctions.net:443 initial path ((null))] event: path:start @0.050s
default	09:45:28.238797+0800	hootowl	[C9.1.1 us-central1-tataro2.cloudfunctions.net:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.051s, uuid: 96FDE15E-41A3-4F39-8B32-45B97223B44C
default	09:45:28.238912+0800	hootowl	[C9.1.1 us-central1-tataro2.cloudfunctions.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:start_dns @0.051s
default	09:45:28.239042+0800	hootowl	Task <93538818-97EE-404C-8274-265196A34402>.<5> setting up Connection 9
default	09:45:28.239689+0800	hootowl	boringssl_context_info_handler(2823) [C7.1.1.1:2][0x14a4656e0] Client handshake state: TLS client read_server_finished
default	09:45:28.239947+0800	hootowl	boringssl_context_info_handler(2823) [C7.1.1.1:2][0x14a4656e0] Client handshake state: TLS client finish_client_handshake
default	09:45:28.239978+0800	hootowl	boringssl_context_info_handler(2823) [C7.1.1.1:2][0x14a4656e0] Client handshake state: TLS client done
default	09:45:28.239984+0800	hootowl	boringssl_context_info_handler(2812) [C7.1.1.1:2][0x14a4656e0] Client handshake done
default	09:45:28.240962+0800	hootowl	nw_protocol_boringssl_signal_connected(895) [C7.1.1.1:2][0x14a4656e0] TLS connected [server(0) version(0x0303) ciphersuite(TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256) group(0x0017) signature_alg(0x0401) alpn(nil) resumed(0) offered_ticket(0) in_early_data(0) early_data_accepted(0) false_started(0) ocsp_received(0) sct_received(0) connect_time(1583ms) flight_time(479ms) rtt(411ms) write_stalls(0) read_stalls(6) pake(0x0000)]
default	09:45:28.241065+0800	hootowl	nw_flow_connected [C7.1.1.1 61.60.98.243:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (CFNetworkConnection-4283075305)
default	09:45:28.304397+0800	hootowl	[C7.1.1.1 61.60.98.243:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @2.648s
default	09:45:28.305351+0800	hootowl	[C7.1.1 data.ntpc.gov.tw:443 ready resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @2.711s
default	09:45:28.305433+0800	hootowl	[C7.1 data.ntpc.gov.tw:443 ready transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @2.711s
default	09:45:28.305915+0800	hootowl	[C7.1.1.1 61.60.98.243:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @2.712s
default	09:45:28.306010+0800	hootowl	[C7.1.1 data.ntpc.gov.tw:443 ready resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @2.713s
default	09:45:28.306334+0800	hootowl	[C7.1 data.ntpc.gov.tw:443 ready transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @2.713s
default	09:45:28.306350+0800	hootowl	nw_flow_connected [C7 61.60.98.243:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (endpoint_flow)
default	09:45:28.306405+0800	hootowl	[C7 61.60.98.243:443 ready parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_connect @2.713s
default	09:45:28.307102+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C7] reporting state ready
default	09:45:28.307120+0800	hootowl	[C7 61.60.98.243:443 ready parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @2.713s
default	09:45:28.307176+0800	hootowl	nw_connection_send_viability_changed_on_nw_queue [C7] viability_changed_handler(true)
default	09:45:28.356863+0800	hootowl	Connection 7: connected successfully
default	09:45:28.365653+0800	hootowl	Connection 7: TLS handshake complete
default	09:45:28.365825+0800	hootowl	Connection 7: ready C(N) E(N)
default	09:45:28.366698+0800	hootowl	Task <5100FD16-E95C-47E4-8962-4D6E52C0122F>.<3> now using Connection 7
default	09:45:28.368004+0800	hootowl	Connection 7: received viability advisory(Y)
default	09:45:28.368017+0800	hootowl	Task <5100FD16-E95C-47E4-8962-4D6E52C0122F>.<3> sent request, body N 0
default	09:45:28.413347+0800	hootowl	nw_endpoint_resolver_update [C9.1.1 us-central1-tataro2.cloudfunctions.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Adding endpoint handler for 216.239.36.54:443
default	09:45:28.427038+0800	hootowl	[C9.1.1 us-central1-tataro2.cloudfunctions.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:receive_dns @0.225s
default	09:45:28.427150+0800	hootowl	[C9.1.1.1 216.239.36.54:443 initial path ((null))] event: path:start @0.226s
default	09:45:28.427779+0800	hootowl	[C9.1.1.1 216.239.36.54:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.239s, uuid: B015E773-199E-4856-B998-78344E85AAA6
default	09:45:28.479619+0800	hootowl	[C9.1.1.1 216.239.36.54:443 in_progress channel-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_nexus @0.287s
default	09:45:28.484865+0800	hootowl	[C9.1.1.1 216.239.36.54:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:receive_nexus @0.296s
default	09:45:28.548803+0800	hootowl	quic_conn_initialize_inner [C9.1.1.1:2] [-ca8483eeb705f272] created QUIC connection (spin bit enabled)
default	09:45:28.549726+0800	hootowl	[C9.1.1.1 216.239.36.54:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_connect @0.362s
default	09:45:28.599088+0800	hootowl	MncplCyclopsScreen 78
🏠 body eval — items:6 firstObs:3s firstCar:0
default	09:45:28.602132+0800	hootowl	quic_crypto_new_flow [C9.1.1.1:2] [-ca8483eeb705f272] TLS stream is: [C10]
default	09:45:28.602344+0800	hootowl	[C10 08AB4B03-92AA-4097-BAFD-01AB34E5F482 216.239.36.54:443 quic-connection, url: https://us-central1-tataro2.cloudfunctions.net/verifyReceipt, tls, definite, attribution: developer, context: com.apple.CFNetwork.NSURLSession.{D8375FAB-BCC3-47F6-9F42-2CD36CF9484B}{(null)}{Y}{2}{0x0} (private), proc: 1B526020-2DE0-3C65-9122-F1177549D69A, delegated upid: 0] start
default	09:45:28.602760+0800	hootowl	[C10 216.239.36.54:443 initial socket-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:start @0.000s
default	09:45:28.602806+0800	hootowl	[C10 216.239.36.54:443 waiting socket-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.000s, uuid: B015E773-199E-4856-B998-78344E85AAA6
default	09:45:28.666807+0800	hootowl	[C10 216.239.36.54:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_connect @0.062s
default	09:45:28.667093+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C10] reporting state preparing
default	09:45:28.668428+0800	hootowl	nw_flow_connected [C10 216.239.36.54:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Transport protocol connected (quic-connection)
default	09:45:28.668452+0800	hootowl	[C10 216.239.36.54:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_transport @0.063s
default	09:45:28.682231+0800	hootowl	boringssl_session_apply_protocol_options_for_transport_block_invoke_2(2367) [C10:1][0x14a464060] TLS configured [server(0) min_version(0x0304) max_version(0x0304) name(us-central1-tataro2.cloudfunctions.net) tickets(false) false_start(false) enforce_ev(false) enforce_ats(false) ats_non_pfs_ciphersuite_allowed(false) cc_mode_enforced(false) ech(false) pqtls(true), pake(false) skip_ats_trust(false)]
default	09:45:28.682279+0800	hootowl	boringssl_context_info_handler(2806) [C10:1][0x14a464060] Client handshake started
default	09:45:28.682507+0800	hootowl	boringssl_context_info_handler(2823) [C10:1][0x14a464060] Client handshake state: TLS client enter_early_data
default	09:45:28.682709+0800	hootowl	boringssl_context_info_handler(2823) [C10:1][0x14a464060] Client handshake state: TLS client read_server_hello
default	09:45:28.759500+0800	hootowl	boringssl_context_info_handler(2823) [C10:1][0x14a464060] Client handshake state: TLS 1.3 client read_hello_retry_request
default	09:45:28.759517+0800	hootowl	boringssl_context_info_handler(2823) [C10:1][0x14a464060] Client handshake state: TLS 1.3 client read_server_hello
default	09:45:28.759588+0800	hootowl	boringssl_context_info_handler(2823) [C10:1][0x14a464060] Client handshake state: TLS 1.3 client read_encrypted_extensions
default	09:45:28.759646+0800	hootowl	boringssl_context_info_handler(2823) [C10:1][0x14a464060] Client handshake state: TLS 1.3 client read_certificate_request
default	09:45:28.767476+0800	hootowl	[C9.1.2 us-central1-tataro2.cloudfunctions.net:443 initial path ((null))] event: path:start @0.573s
default	09:45:28.767679+0800	hootowl	[C9.1.2 us-central1-tataro2.cloudfunctions.net:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.575s, uuid: F29B4D6B-0162-4748-8AB8-B006F1A7F2C4
default	09:45:28.768078+0800	hootowl	[C9.1.2 us-central1-tataro2.cloudfunctions.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:start_dns @0.576s
default	09:45:28.768157+0800	hootowl	Task <5100FD16-E95C-47E4-8962-4D6E52C0122F>.<3> received response, status 200 content C
default	09:45:28.899827+0800	hootowl	boringssl_context_info_handler(2823) [C10:1][0x14a464060] Client handshake state: TLS 1.3 client read_server_certificate
default	09:45:28.899878+0800	hootowl	boringssl_context_info_handler(2823) [C10:1][0x14a464060] Client handshake state: TLS 1.3 client read_server_certificate_verify
default	09:45:28.900047+0800	hootowl	boringssl_context_evaluate_trust_async(2249) [C10:1][0x14a464060] Performing external trust evaluation
default	09:45:28.900090+0800	hootowl	boringssl_context_evaluate_trust_async_external(2234) [C10:1][0x14a464060] Asyncing for external verify block
default	09:45:28.905729+0800	hootowl	Task <5100FD16-E95C-47E4-8962-4D6E52C0122F>.<3> response ended
default	09:45:28.905761+0800	hootowl	Task <5100FD16-E95C-47E4-8962-4D6E52C0122F>.<3> done using Connection 7
default	09:45:28.967909+0800	hootowl	Task <5100FD16-E95C-47E4-8962-4D6E52C0122F>.<3> summary for task success {transaction_duration_ms=4201, response_status=200, connection=7, protocol="http/1.1", domain_lookup_duration_ms=315, connect_duration_ms=2152, secure_connection_duration_ms=1583, private_relay=false, request_start_ms=3598, request_duration_ms=0, response_start_ms=3998, response_duration_ms=202, request_bytes=264, request_throughput_kbps=8002, response_bytes=21970, response_throughput_kbps=867, cache_hit=true}
default	09:45:28.968202+0800	hootowl	Connection 9: asked to evaluate TLS Trust
default	09:45:28.968224+0800	hootowl	[C7] event: client:connection_idle @3.374s
default	09:45:28.984055+0800	hootowl	nw_protocol_tcp_notify [C7.1.1.1:3] nw_protocol_notification_type_connection_idle is true
default	09:45:28.984074+0800	hootowl	nw_protocol_tcp_set_connection_idle [C7.1.1.1:3] os_nexus_flow_set_connection_idle returned 0
default	09:45:28.984146+0800	hootowl	[C7] event: client:connection_idle @3.388s
default	09:45:28.984175+0800	hootowl	nw_protocol_tcp_notify [C7.1.1.1:3] nw_protocol_notification_type_connection_idle is true
default	09:45:28.984184+0800	hootowl	nw_protocol_tcp_set_connection_idle [C7.1.1.1:3] os_nexus_flow_set_connection_idle returned 0
default	09:45:28.984210+0800	hootowl	Task <5100FD16-E95C-47E4-8962-4D6E52C0122F>.<3> finished successfully
default	09:45:28.984256+0800	hootowl	Task <93538818-97EE-404C-8274-265196A34402>.<5> auth completion disp=1 cred=0x0
default	09:45:29.035774+0800	hootowl	nw_endpoint_resolver_update [C9.1.2 us-central1-tataro2.cloudfunctions.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Adding endpoint handler for 216.239.36.54:443
default	09:45:29.070671+0800	hootowl	[C9.1.2 us-central1-tataro2.cloudfunctions.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:receive_dns @0.842s
default	09:45:29.075184+0800	hootowl	[C9.1.2.1 216.239.36.54:443 initial path ((null))] event: path:start @0.844s
default	09:45:29.134890+0800	hootowl	[C9.1.2.1 216.239.36.54:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.947s, uuid: BACD1324-A8A9-4274-90B0-BC943A7A7012
default	09:45:29.135899+0800	hootowl	[C9.1.2.1 216.239.36.54:443 in_progress channel-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_nexus @0.947s
default	09:45:29.198735+0800	hootowl	[C9.1.2.1 216.239.36.54:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:receive_nexus @1.002s
default	09:45:29.199203+0800	hootowl	[C9.1.2.1 216.239.36.54:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_connect @1.003s
default	09:45:29.199502+0800	hootowl	tcp_output [C9.1.2.1:3] flags=[SEC] seq=3879884732, ack=0, win=65535 state=SYN_SENT rcv_nxt=0, snd_una=3879884732
default	09:45:29.199579+0800	hootowl	MncplCyclopsScreen 78
🏠 body eval — items:6 firstObs:4s firstCar:0
default	09:45:29.199588+0800	hootowl	(Trust 0x14a639980) No pending evals, starting
default	09:45:29.199713+0800	hootowl	[0x149582940] activating connection: mach=true listener=false peer=false name=com.apple.trustd
default	09:45:29.199804+0800	hootowl	(Trust 0x14a639980) Completed async eval kickoff
default	09:45:29.274611+0800	hootowl	(Trust 0x14a639980) trustd returned 4
default	09:45:29.280232+0800	hootowl	System Trust Evaluation yielded status(0)
default	09:45:29.294713+0800	hootowl	(Trust 0x14a638f00) No pending evals, starting
default	09:45:29.296075+0800	hootowl	[0x1495826c0] activating connection: mach=true listener=false peer=false name=com.apple.trustd
default	09:45:29.296214+0800	hootowl	(Trust 0x14a638f00) Completed async eval kickoff
default	09:45:29.297251+0800	hootowl	[0x149582940] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	09:45:29.297373+0800	hootowl	tcp_input [C9.1.2.1:3] flags=[S.] seq=2148268902, ack=3879884733, win=65535 state=SYN_SENT rcv_nxt=0, snd_una=3879884732
default	09:45:29.297386+0800	hootowl	nw_flow_connected [C9.1.2.1 216.239.36.54:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Transport protocol connected (tcp)
default	09:45:29.297436+0800	hootowl	[C9.1.2.1 216.239.36.54:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_transport @1.110s
default	09:45:29.298831+0800	hootowl	boringssl_session_apply_protocol_options_for_transport_block_invoke_2(2367) [C9.1.2.1:2][0x14a4660e0] TLS configured [server(0) min_version(0x0303) max_version(0x0304) name(us-central1-tataro2.cloudfunctions.net) tickets(false) false_start(false) enforce_ev(false) enforce_ats(false) ats_non_pfs_ciphersuite_allowed(false) cc_mode_enforced(false) ech(false) pqtls(true), pake(false) skip_ats_trust(false)]
default	09:45:29.298943+0800	hootowl	boringssl_context_info_handler(2806) [C9.1.2.1:2][0x14a4660e0] Client handshake started
default	09:45:29.298957+0800	hootowl	MncplCyclopsScreen 78
🏠 body eval — items:6 firstObs:4s firstCar:0
default	09:45:29.299104+0800	hootowl	boringssl_context_info_handler(2823) [C9.1.2.1:2][0x14a4660e0] Client handshake state: TLS client enter_early_data
default	09:45:29.299252+0800	hootowl	boringssl_context_info_handler(2823) [C9.1.2.1:2][0x14a4660e0] Client handshake state: TLS client read_server_hello
default	09:45:29.356578+0800	hootowl	(Trust 0x14a638f00) trustd returned 4
default	09:45:29.357037+0800	hootowl	Connection 9: TLS Trust result 0
default	09:45:29.357059+0800	hootowl	boringssl_context_evaluate_trust_async_external_block_invoke_3(2148) [C10:1][0x14a464060] Returning from external verify block with result: true
default	09:45:29.408162+0800	hootowl	boringssl_context_certificate_verify_callback(2430) [C10:1][0x14a464060] Certificate verification result: OK
default	09:45:29.408406+0800	hootowl	boringssl_context_info_handler(2823) [C10:1][0x14a464060] Client handshake state: TLS 1.3 client read_server_finished
default	09:45:29.411459+0800	hootowl	boringssl_context_info_handler(2823) [C10:1][0x14a464060] Client handshake state: TLS 1.3 client send_end_of_early_data
default	09:45:29.411803+0800	hootowl	boringssl_context_info_handler(2823) [C10:1][0x14a464060] Client handshake state: TLS 1.3 client send_client_encrypted_extensions
default	09:45:29.411854+0800	hootowl	boringssl_context_info_handler(2823) [C10:1][0x14a464060] Client handshake state: TLS 1.3 client send_client_certificate
default	09:45:29.411883+0800	hootowl	boringssl_context_info_handler(2823) [C10:1][0x14a464060] Client handshake state: TLS 1.3 client complete_second_flight
default	09:45:29.417314+0800	hootowl	boringssl_context_info_handler(2823) [C10:1][0x14a464060] Client handshake state: TLS 1.3 client done
default	09:45:29.491131+0800	hootowl	boringssl_context_info_handler(2823) [C10:1][0x14a464060] Client handshake state: TLS client finish_client_handshake
default	09:45:29.492832+0800	hootowl	boringssl_context_info_handler(2823) [C10:1][0x14a464060] Client handshake state: TLS client done
default	09:45:29.492924+0800	hootowl	boringssl_context_info_handler(2812) [C10:1][0x14a464060] Client handshake done
default	09:45:29.494554+0800	hootowl	nw_protocol_boringssl_signal_connected(895) [C10:1][0x14a464060] TLS connected [server(0) version(0x0304) ciphersuite(TLS_AES_256_GCM_SHA384) group(0x11ec) signature_alg(0x0403) alpn(h3) resumed(0) offered_ticket(0) in_early_data(0) early_data_accepted(0) false_started(0) ocsp_received(0) sct_received(0) connect_time(805ms) flight_time(72ms) rtt(71ms) write_stalls(0) read_stalls(14) pake(0x0000)]
default	09:45:29.494734+0800	hootowl	nw_flow_connected [C10 216.239.36.54:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (tls)
default	09:45:29.495239+0800	hootowl	[C10 216.239.36.54:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_connect @0.882s
default	09:45:29.495966+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C10] reporting state ready
default	09:45:29.496000+0800	hootowl	[C10 216.239.36.54:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.883s
default	09:45:29.501287+0800	hootowl	[0x1495826c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	09:45:29.505829+0800	hootowl	MncplCyclopsScreen 149
🪟 MncplCyclopsScreen onAppear — municipal 🆔 8064324136773232350
default	09:45:29.505903+0800	hootowl	MncplCyclopsScreen 78
🏠 body eval — items:6 firstObs:4s firstCar:0
default	09:45:29.506553+0800	hootowl	boringssl_context_info_handler(2823) [C9.1.2.1:2][0x14a4660e0] Client handshake state: TLS 1.3 client read_hello_retry_request
default	09:45:29.508080+0800	hootowl	boringssl_context_info_handler(2823) [C9.1.2.1:2][0x14a4660e0] Client handshake state: TLS 1.3 client read_server_hello
default	09:45:29.554379+0800	hootowl	boringssl_context_info_handler(2823) [C9.1.2.1:2][0x14a4660e0] Client handshake state: TLS 1.3 client read_encrypted_extensions
default	09:45:29.557804+0800	hootowl	boringssl_context_info_handler(2823) [C9.1.2.1:2][0x14a4660e0] Client handshake state: TLS 1.3 client read_certificate_request
default	09:45:29.557851+0800	hootowl	boringssl_context_info_handler(2823) [C9.1.2.1:2][0x14a4660e0] Client handshake state: TLS 1.3 client read_server_certificate
default	09:45:29.557862+0800	hootowl	boringssl_context_info_handler(2823) [C9.1.2.1:2][0x14a4660e0] Client handshake state: TLS 1.3 client read_server_certificate_verify
default	09:45:29.559063+0800	hootowl	boringssl_context_evaluate_trust_async(2249) [C9.1.2.1:2][0x14a4660e0] Performing external trust evaluation
default	09:45:29.559149+0800	hootowl	boringssl_context_evaluate_trust_async_external(2234) [C9.1.2.1:2][0x14a4660e0] Asyncing for external verify block
default	09:45:29.565462+0800	hootowl	quic_pmtud_restart [C9.1.1.1:2] [-ea8483eeb705f272] PMTUD enabled, max PMTU: 1500, header size: 28, current PMTU 1228
default	09:45:29.565495+0800	hootowl	quic_crypto_tls_ready_inner [C9.1.1.1:2] [-ea8483eeb705f272] QUIC connection established in 1013.48 ms, RTT 89.347 ms
default	09:45:29.565515+0800	hootowl	nw_flow_connected [C9.1.1.1 216.239.36.54:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Transport protocol connected (quic-connection)
default	09:45:29.623094+0800	hootowl	[C9.1.1.1 216.239.36.54:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_transport @1.434s
default	09:45:29.624275+0800	hootowl	nw_flow_connected [C9.1.1.1 216.239.36.54:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (CFNetworkConnection-4283075305)
default	09:45:29.628735+0800	hootowl	[C9.1.1.1 216.239.36.54:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @1.438s
default	09:45:29.629618+0800	hootowl	[C9.1.1 us-central1-tataro2.cloudfunctions.net:443 ready resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @1.439s
default	09:45:29.629682+0800	hootowl	[C9.1 us-central1-tataro2.cloudfunctions.net:443 ready transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @1.439s
default	09:45:29.630276+0800	hootowl	nw_protocol_tcp_log_summary [C9.1.2.1:3] 
	[0D040898-0310-4D26-9677-CE18058A5421 192.168.50.191:50796<->216.239.36.54:443]
	Init: 1, Conn_Time: 105.650ms, SYNs: 1, WR_T: 0/0, RD_T: 0/0, TFO: 0/0/0, ECN: 0/1/1, Accurate ECN (client/server): Disabled/Disabled, TS: 1, TSO: 0
	rtt_cache: none, rtt_upd: 3, rtt: 125.000ms, rtt_var: 62.750ms rtt_nc: 125.000ms, rtt_var_nc: 62.750ms base rtt: 106ms
	ACKs-compressed: 1, ACKs delayed: 0 delayed ACKs sent: 0
default	09:45:29.697215+0800	hootowl	[C9.1.1.1 216.239.36.54:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @1.505s
default	09:45:29.697333+0800	hootowl	[C9.1.1 us-central1-tataro2.cloudfunctions.net:443 ready resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @1.505s
default	09:45:29.697361+0800	hootowl	[C9.1 us-central1-tataro2.cloudfunctions.net:443 ready transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @1.505s
default	09:45:29.697556+0800	hootowl	nw_flow_connected [C9 216.239.36.54:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (endpoint_flow)
default	09:45:29.697596+0800	hootowl	[C9 216.239.36.54:443 ready parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_connect @1.505s
default	09:45:29.697690+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C9] reporting state ready
default	09:45:29.697700+0800	hootowl	[C9 216.239.36.54:443 ready parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @1.506s
default	09:45:29.697716+0800	hootowl	nw_connection_send_viability_changed_on_nw_queue [C9] viability_changed_handler(true)
error	09:45:29.698062+0800	hootowl	nw_protocol_instance_set_output_handler Not calling remove_input_handler on 0x14a611680:udp
default	09:45:29.698081+0800	hootowl	quic_migration_path_event_block_invoke [C9.1.1.1:2] [-ea8483eeb705f272] path 28cd40009b7cfd38 over en0 received event established
default	09:45:29.698126+0800	hootowl	quic_migration_evaluate_primary [C9.1.1.1:2] [-ea8483eeb705f272] promoted path 0x149879180 over en0 to primary
default	09:45:29.698142+0800	hootowl	quic_migration_path_event_block_invoke [C9.1.1.1:2] [-ea8483eeb705f272] path af4c88651163d58a over pdp_ip0 received event available
error	09:45:29.698189+0800	hootowl	quic_conn_setup_pmtud [C9.1.1.1:2] [-ea8483eeb705f272] unable to query remote endpoint, assuming IPv6
default	09:45:29.698242+0800	hootowl	quic_pmtud_restart [C9.1.1.1:2] [-ea8483eeb705f272] PMTUD enabled, max PMTU: 1450, header size: 48, current PMTU 1248
default	09:45:29.698283+0800	hootowl	quic_migration_evaluate [C9.1.1.1:2] [-ea8483eeb705f272] evaluating path migration
default	09:45:29.698293+0800	hootowl	quic_migration_evaluate_block_invoke [C9.1.1.1:2] [-ea8483eeb705f272] path af4c88651163d58a state available (0), ifname pdp_ip0, primary? 0, initial? 0, fallback? 0, preferred? 0 lossy? 0
default	09:45:29.698302+0800	hootowl	quic_migration_evaluate_block_invoke [C9.1.1.1:2] [-ea8483eeb705f272] path 28cd40009b7cfd38 state validated (0), ifname en0, primary? 1, initial? 1, fallback? 0, preferred? 0 lossy? 0
default	09:45:29.698316+0800	hootowl	quic_migration_evaluate [C9.1.1.1:2] [-ea8483eeb705f272] current path is usable, no strong fallback or we are probing
default	09:45:29.698323+0800	hootowl	nw_protocol_instance_report_ready [C9.1.1.1:2] Calling notify with interface en0 for flow_registration 2ACCD937-C206-4B25-AF35-DAE5AEE6C638
default	09:45:29.699933+0800	hootowl	[C9.1.1.1 216.239.36.54:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:migrated @1.510s, uuid: B015E773-199E-4856-B998-78344E85AAA6
default	09:45:29.699981+0800	hootowl	[C9.1.1 us-central1-tataro2.cloudfunctions.net:443 ready resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:migrated @1.510s, uuid: 96FDE15E-41A3-4F39-8B32-45B97223B44C
default	09:45:29.700017+0800	hootowl	[C9.1 us-central1-tataro2.cloudfunctions.net:443 ready transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:migrated @1.510s, uuid: 8947A3B0-E196-4106-B66C-E7013CF1305C
default	09:45:29.700032+0800	hootowl	[C9 216.239.36.54:443 ready parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:migrated @1.510s, uuid: 8947A3B0-E196-4106-B66C-E7013CF1305C
default	09:45:29.700066+0800	hootowl	quic_stream_create_inbound [C9.1.1.1:2] [-ea8483eeb705f272] creating inbound stream 3
default	09:45:29.700556+0800	hootowl	boringssl_context_new_session_handler(1771) [C10:1][0x14a464060] Asyncing for session update block
default	09:45:29.701240+0800	hootowl	boringssl_context_new_session_handler(1771) [C10:1][0x14a464060] Asyncing for session update block
default	09:45:29.701284+0800	hootowl	nw_protocol_boringssl_signal_connected(895) [C10:1][0x14a464060] TLS connected [server(0) version(0x0304) ciphersuite(TLS_AES_256_GCM_SHA384) group(0x11ec) signature_alg(0x0403) alpn(h3) resumed(0) offered_ticket(0) in_early_data(0) early_data_accepted(0) false_started(0) ocsp_received(0) sct_received(0) connect_time(805ms) flight_time(72ms) rtt(71ms) write_stalls(0) read_stalls(14) pake(0x0000)]
default	09:45:29.701309+0800	hootowl	nw_flow_connected [C10 216.239.36.54:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (tls)
default	09:45:29.701879+0800	hootowl	quic_migration_evaluate [C9.1.1.1:2] [-ea8483eeb705f272] evaluating path migration
default	09:45:29.701903+0800	hootowl	quic_migration_evaluate_block_invoke [C9.1.1.1:2] [-ea8483eeb705f272] path af4c88651163d58a state available (0), ifname pdp_ip0, primary? 0, initial? 0, fallback? 0, preferred? 0 lossy? 0
default	09:45:29.706314+0800	hootowl	quic_migration_evaluate_block_invoke [C9.1.1.1:2] [-ea8483eeb705f272] path 28cd40009b7cfd38 state validated (0), ifname en0, primary? 1, initial? 1, fallback? 0, preferred? 0 lossy? 0
default	09:45:29.706406+0800	hootowl	quic_migration_evaluate [C9.1.1.1:2] [-ea8483eeb705f272] current path is usable, no strong fallback or we are probing
default	09:45:29.706422+0800	hootowl	Connection 9: connected successfully
default	09:45:29.706444+0800	hootowl	Connection 9: TLS handshake complete
default	09:45:29.706465+0800	hootowl	Connection 9: ready C(N) E(N)
default	09:45:29.706676+0800	hootowl	[C9] event: client:connection_reused @1.514s
default	09:45:29.706717+0800	hootowl	Task <93538818-97EE-404C-8274-265196A34402>.<5> now using Connection 9
default	09:45:29.707206+0800	hootowl	Connection 9: received viability advisory(Y)
default	09:45:29.710273+0800	hootowl	tcp_output [C9.1.2.1:3] flags=[F.] seq=3879886280, ack=2148281733, win=2048 state=FIN_WAIT_1 rcv_nxt=2148281733, snd_una=3879886280
default	09:45:29.710546+0800	hootowl	boringssl_context_new_session_handler_block_invoke(1774) [C10:1][0x14a464060] Returning from session update block
default	09:45:29.711230+0800	hootowl	boringssl_context_new_session_handler_block_invoke(1774) [C10:1][0x14a464060] Returning from session update block
default	09:45:29.712099+0800	hootowl	0x14c0ab9d8 ID=0 Task <93538818-97EE-404C-8274-265196A34402>.<5> sent request, body S 2395
default	09:45:29.731833+0800	hootowl	Received configuration update from daemon (initial)
default	09:45:29.734333+0800	hootowl	tcp_input [C9.1.2.1:3] flags=[F.] seq=2148281733, ack=3879886281, win=1045 state=FIN_WAIT_1 rcv_nxt=2148281733, snd_una=3879886280
default	09:45:29.791237+0800	hootowl	[(FBSceneManager):sceneID:com.sharkda.hootowl-83FF55F6-7B28-4BFD-8825-33CB43E5D162] Sending action(s): BLSInvalidateFrameSpecifiersAction
default	09:45:29.796314+0800	hootowl	0x148d71000 -[WKWebView _updateVisibleContentRects:] finally ran 2.08s after being scheduled
default	09:45:29.856627+0800	hootowl	[(FBSceneManager):sceneID:com.sharkda.hootowl-83FF55F6-7B28-4BFD-8825-33CB43E5D162] Sending action(s): BLSInvalidateFrameSpecifiersAction
default	09:45:29.857410+0800	hootowl	[(FBSceneManager):sceneID:com.sharkda.hootowl-83FF55F6-7B28-4BFD-8825-33CB43E5D162] Sending action(s): BLSInvalidateFrameSpecifiersAction
default	09:45:29.861716+0800	hootowl	[ATTrackingManager] trackingAuthorizationStatus API call invoked.
default	09:45:29.861854+0800	hootowl	[ATTrackingManager] Performing TCC Access Preflight Request.
default	09:45:29.862107+0800	hootowl	[ATTrackingManager] Returning from trackingAuthorizationStatus - 0
default	09:45:29.865895+0800	hootowl	Mu1Base+Ext 152
newTaipeiCity 📦 minutely Received 19990 bytes
default	09:45:29.865955+0800	hootowl	Mu1Base+Ext 175
previousHash updated
default	09:45:29.873300+0800	hootowl	    AVAudioSession_iOS.mm:996   Activated session 0x77c67d3
default	09:45:29.936724+0800	hootowl	Received state update for 46045 (app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>, unknown-NotVisible
fault	09:45:29.945595+0800	hootowl	__delegate_identifier__:Performance Diagnostics__:::____message__:{"message":"Interprocess communication on the main thread can cause non-deterministic delays.","antipattern trigger":"-[CLLocationManager authorizationStatus]","message type":"suppressable","issue type":1,"category type":17,"subcategory type":0,"show in console":"0"}'26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 08 82 16 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 F4 8A 16 00 DC 4F 50 56 DB E7 36 8A 99 ED A6 79 F2 C1 4F B0 CC 4E 00 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 CC DA 02 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 98 D7 02 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 90 F1 02 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 4C E5 02 00 41 11 65 E2 EE 8E 38 0E B2 54 99 77 27 39 71 E3 98 14 00 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 70 16 12 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 58 C1 08 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 70 05 03 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D F4 D0 02 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 48 CC 02 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 14 8C 36 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 C0 8C 36 00 0F 8D 35 B6 55 6F 3E 34 8E AA 80 AB 54 04 7D C5 1C 4C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
fault	09:45:29.956211+0800	hootowl	__delegate_identifier__:Performance Diagnostics__:::____message__:{"message":"Interprocess communication on the main thread can cause non-deterministic delays.","antipattern trigger":"-[CLLocationManager authorizationStatus]","message type":"suppressable","issue type":4,"category type":17,"subcategory type":0,"show in console":"0"}'26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 08 82 16 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 F4 8A 16 00 DC 4F 50 56 DB E7 36 8A 99 ED A6 79 F2 C1 4F B0 CC 4E 00 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 CC DA 02 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 98 D7 02 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 90 F1 02 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 4C E5 02 00 41 11 65 E2 EE 8E 38 0E B2 54 99 77 27 39 71 E3 98 14 00 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 70 16 12 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 58 C1 08 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 70 05 03 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D F4 D0 02 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 48 CC 02 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 14 8C 36 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 C0 8C 36 00 0F 8D 35 B6 55 6F 3E 34 8E AA 80 AB 54 04 7D C5 1C 4C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
error	09:45:29.978339+0800	hootowl	73	oParseMinute(data:)	🔴 060105 NOT in feed (source missing)
default	09:45:29.978857+0800	hootowl	MncplCyclopsScreen 166
🦵 uiKick received — syncing items
default	09:45:29.978893+0800	hootowl	Municipal+Cyclops 93
🎨 model refreshed — obs:4s car:0 thread:main 🆔 8064324136773232350
default	09:45:29.982032+0800	hootowl	Municipal 130
🐎 minutelyAvailable ["newTaipeiCity ⏳05 09:45 ∑1428", "taipei ⏳05 09:45 ∑1172"]
default	09:45:29.991970+0800	hootowl	MncplCyclopsScreen 166
🦵 uiKick received — syncing items
default	09:45:29.991993+0800	hootowl	Municipal+Cyclops 93
🎨 model refreshed — obs:4s car:0 thread:main 🆔 8064324136773232350
default	09:45:29.997519+0800	hootowl	MncplCyclopsScreen 78
🏠 body eval — items:6 firstObs:4s firstCar:0
default	09:45:30.007437+0800	hootowl	Task <77E2D366-C6BB-4243-8B20-397A36B5FC01>.<6> resuming, timeouts(60.0, 604800.0) qos(0x19) voucher((null)) activity(00000000-0000-0000-0000-000000000000)
default	09:45:30.008292+0800	hootowl	Connection 0: creating secure tcp or quic connection
default	09:45:30.008435+0800	hootowl	Connection 11: enabling TLS
default	09:45:30.008467+0800	hootowl	Connection 11: starting, TC(0x0)
default	09:45:30.008619+0800	hootowl	[C11 097EEFC4-A32D-46CC-AEE4-D09EF76938A7 gist.githubusercontent.com:443 quic-connection, url: https://gist.githubusercontent.com/sharkda/1abaa9806dae0f34205725b51f21ad87/raw, definite, attribution: developer, context: com.apple.CFNetwork.NSURLSession.{D8375FAB-BCC3-47F6-9F42-2CD36CF9484B}{(null)}{Y}{2}{0x0} (private), proc: 1B526020-2DE0-3C65-9122-F1177549D69A, delegated upid: 0] start
default	09:45:30.008641+0800	hootowl	[C11 gist.githubusercontent.com:443 initial parent-flow ((null))] event: path:start @0.000s
default	09:45:30.009182+0800	hootowl	[C11 gist.githubusercontent.com:443 waiting parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.000s, uuid: 353FB8CE-E581-40AB-AA02-810E826BAA50
default	09:45:30.009206+0800	hootowl	Loading PDFKit
default	09:45:30.009412+0800	hootowl	[C11 gist.githubusercontent.com:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_connect @0.000s
default	09:45:30.009418+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C11] reporting state preparing
default	09:45:30.009525+0800	hootowl	[C11 gist.githubusercontent.com:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_child @0.000s
default	09:45:30.009594+0800	hootowl	[C11.1 gist.githubusercontent.com:443 initial path ((null))] event: path:start @0.000s
default	09:45:30.009743+0800	hootowl	[C11.1 gist.githubusercontent.com:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.001s, uuid: 353FB8CE-E581-40AB-AA02-810E826BAA50
default	09:45:30.009776+0800	hootowl	[C11.1 gist.githubusercontent.com:443 in_progress transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: transform:start @0.001s
default	09:45:30.010154+0800	hootowl	[C11.1.1 gist.githubusercontent.com:443 initial path ((null))] event: path:start @0.001s
default	09:45:30.010912+0800	hootowl	[C11.1.1 gist.githubusercontent.com:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.002s, uuid: 69EE4C71-FAA7-4057-9B34-41FF800FCC4A
default	09:45:30.011413+0800	hootowl	[C11.1.1 gist.githubusercontent.com:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:start_dns @0.002s
default	09:45:30.011477+0800	hootowl	Task <77E2D366-C6BB-4243-8B20-397A36B5FC01>.<6> setting up Connection 11
default	09:45:30.018038+0800	hootowl	App is being debugged, do not track this hang
default	09:45:30.018076+0800	hootowl	Hang detected: 2.30s (debugger attached, not reporting)
default	09:45:30.018292+0800	hootowl	beginSafeBrowsingCheck: no threat, completing navigationID=13
default	09:45:30.018647+0800	hootowl	0x148ec1518 - [pageProxyID=7, webPageID=8, PID=46063] WebPageProxy::didStartProvisionalLoadForFrame: frameID=4294967297, isMainFrame=1
default	09:45:30.018713+0800	hootowl	0x1310740c0 - [PID=46063] WebProcessProxy::didStartProvisionalLoadForMainFrame:
default	09:45:30.021250+0800	hootowl	[ATTrackingManager] trackingAuthorizationStatus API call invoked.
default	09:45:30.021279+0800	hootowl	[ATTrackingManager] Call to trackingAuthorizationStatus eligible for rate limiting. Returning 0
default	09:45:30.021486+0800	hootowl	WebContent[46063]: [webPageID=8, frameID=4294967297, resourceID=18] WebResourceLoader::didReceiveResource
default	09:45:30.022360+0800	hootowl	WebContent[46063]: [pageID=8 frameID=4294967297 isMainFrame=1] FrameLoader::setDocumentLoader: Setting document loader to 4614852608 (was 4614832128)
default	09:45:30.022373+0800	hootowl	WebContent[46063]: [pageID=8, frameID=4294967297, isMainFrame=1] DocumentLoader::detachFromFrame
default	09:45:30.022403+0800	hootowl	WebContent[46063]: [pageID=8, frameID=4294967297, isMainFrame=1] DocumentLoader::stopLoading
default	09:45:30.022423+0800	hootowl	WebContent[46063]: [pageID=8 frameID=4294967297 isMainFrame=1] FrameLoader::transitionToCommitted: Clearing provisional document loader (m_provisionalDocumentLoader=4614852608)
default	09:45:30.022474+0800	hootowl	WebContent[46063]: [pageID=8 frameID=4294967297 isMainFrame=1] FrameLoader::setProvisionalDocumentLoader: Setting provisional document loader to 0 (was 4614852608)
error	09:45:30.086232+0800	hootowl	WebContent[46063] Unable to hide query parameters from script (missing data)
default	09:45:30.086659+0800	hootowl	WebContent[46063]: [webPageID=8] WebPage::unfreezeLayerTree: Removing a reason to freeze layer tree (reason=128, new=1, old=1)
default	09:45:30.086776+0800	hootowl	WebContent[46063]: [webPageID=8] WebPage::unfreezeLayerTree: Removing a reason to freeze layer tree (reason=128, new=1, old=1)
default	09:45:30.086940+0800	hootowl	WebContent[46063]: [webPageID=8] WebPage::unfreezeLayerTree: Removing a reason to freeze layer tree (reason=32, new=1, old=1)
default	09:45:30.087065+0800	hootowl	0x148ec1518 - [pageProxyID=7, webPageID=8, PID=46063] WebPageProxy::didNavigateWithNavigationDataShared:
default	09:45:30.087407+0800	hootowl	0x148ec1518 - [pageProxyID=7, webPageID=8, PID=46063] WebPageProxy::didCommitLoadForFrame: frameID=4294967297, isMainFrame=1
default	09:45:30.087454+0800	hootowl	0x148ec1518 - [pageProxyID=7, webPageID=8, PID=46063] WebPageProxy::setMediaCapability: creating (envID=46045-1-com.sharkda.hootowl) for URL 'https://googleads.g.doubleclick.net/mads/static/sdk/native/sdk-core-v40.html?sdk=afma-sdk-i-v13.3.0&stfv=prod'
default	09:45:30.087480+0800	hootowl	WebContent[46063]: [pageID=8, frameID=4294967297, resourceID=18 SubResourceLoader::didFinishLoading
default	09:45:30.087568+0800	hootowl	WebContent[46063]: [webPageID=8] WebPage::unfreezeLayerTree: Removing a reason to freeze layer tree (reason=1, new=0, old=1)
default	09:45:30.092947+0800	hootowl	WebContent[46063]: [pageID=8, frameID=4294967297, isMainFrame=1] LocalFrameView::fireLayoutRelatedMilestonesIfNeeded: Firing first visually non-empty layout milestone on the main frame
default	09:45:30.094083+0800	hootowl	WebContent[46063]: [webFrameID=4294967297, webPageID=8] WebLocalFrameLoaderClient::dispatchDidReachLayoutMilestone: dispatching DidReachLayoutMilestone (milestones=DidFirstVisuallyNonEmptyLayout)
default	09:45:30.094436+0800	hootowl	WebContent[46063]: [webFrameID=4294967297, webPageID=8] WebLocalFrameLoaderClient::dispatchDidReachLayoutMilestone: dispatching DidFirstVisuallyNonEmptyLayoutForFrame
default	09:45:30.095138+0800	hootowl	WebContent[46063]: [webFrameID=4294967297, webPageID=8] WebLocalFrameLoaderClient::completePageTransitionIfNeeded: dispatching didCompletePageTransition
default	09:45:30.096093+0800	hootowl	WebContent[46063]: [webFrameID=4294967297, webPageID=8] WebLocalFrameLoaderClient::dispatchDidReachLayoutMilestone: dispatching DidFirstLayoutForFrame
default	09:45:30.096152+0800	hootowl	WebContent[46063]: [webFrameID=4294967297, webPageID=8] WebLocalFrameLoaderClient::dispatchDidReachLayoutMilestone: dispatching DidReachLayoutMilestone (milestones=DidFirstLayout)
default	09:45:30.096179+0800	hootowl	WebContent[46063]: [pageID=8 frameID=4294967297 isMainFrame=1] FrameLoader::setState: main frame load completed
default	09:45:30.096218+0800	hootowl	WebContent[46063]: Memory usage info dump at MainFrameLoadCompleted:
default	09:45:30.096241+0800	hootowl	WebContent[46063]:   page_count: 1
default	09:45:30.096256+0800	hootowl	WebContent[46063]:   backforward_cache_page_count: 0
default	09:45:30.096288+0800	hootowl	WebContent[46063]:   document_count: 1
default	09:45:30.096296+0800	hootowl	WebContent[46063]:   javascript_gc_heap_capacity_mb: 2
default	09:45:30.096334+0800	hootowl	WebContent[46063]:   javascript_gc_heap_extra_memory_size_mb: 0
default	09:45:30.096477+0800	hootowl	WebContent[46063]:   internal_mb: 24
default	09:45:30.096497+0800	hootowl	WebContent[46063]:   compressed_mb: 0
default	09:45:30.096594+0800	hootowl	WebContent[46063]:   phys_footprint_mb: 34
default	09:45:30.097002+0800	hootowl	WebContent[46063]:   resident_size_mb: 78
default	09:45:30.097018+0800	hootowl	WebContent[46063]:   virtual_size_mb: 420584
default	09:45:30.097667+0800	hootowl	WebContent[46063]: ProgressTracker::progressCompleted: frameID 4294967297, value 0.300000, tracked frames 1, originating frameID 4294967297, isMainLoad 1
default	09:45:30.097688+0800	hootowl	WebContent[46063]: ProgressTracker::finalProgressComplete: value 0.300000, tracked frames 0, originating frameID 4294967297, isMainLoad 1, isMainLoadProgressing 0
default	09:45:30.097997+0800	hootowl	WebContent[46063]: [pageID=8 frameID=4294967297 isMainFrame=1] FrameLoader::checkLoadCompleteForThisFrame: Finished frame load
default	09:45:30.098136+0800	hootowl	WebContent[46063]: [webFrameID=4294967297, webPageID=8] WebLocalFrameLoaderClient::dispatchDidReachLayoutMilestone: dispatching DidReachLayoutMilestone (milestones=DidFirstMeaningfulPaint)
default	09:45:30.098581+0800	hootowl	0x148ec1518 - [pageProxyID=7, webPageID=8, PID=46063] WebPageProxy::didFinishDocumentLoadForFrame: frameID=4294967297, isMainFrame=1
default	09:45:30.098591+0800	hootowl	0x148ec1518 - [pageProxyID=7, webPageID=8, PID=46063] WebPageProxy::didFinishLoadForFrame: frameID=4294967297, isMainFrame=1
default	09:45:30.098598+0800	hootowl	0x1310501c0 - NavigationState will release its process network assertion soon because the page load completed
default	09:45:30.102229+0800	hootowl	Task <6EC8DD19-C575-4F9B-9BCB-1DA167EBFD27>.<3> resuming, timeouts(60.0, 180.0) qos(0x19) voucher((null)) activity(00000000-0000-0000-0000-000000000000)
default	09:45:30.116064+0800	hootowl	0x131050230 - [PID=0] WebProcessCache::updateCapacity: Cache is disabled because process swap on navigation is disabled
default	09:45:30.116489+0800	hootowl	Task <9ABDA649-77F1-4B70-9828-D27E5CA9CB20>.<8> resuming, timeouts(60.0, 604800.0) qos(0x15) voucher((null)) activity(00000000-0000-0000-0000-000000000000)
default	09:45:30.116501+0800	hootowl	Task <4AEBF80A-C0C0-4A75-A035-DF07743AA658>.<7> resuming, timeouts(60.0, 604800.0) qos(0x15) voucher((null)) activity(00000000-0000-0000-0000-000000000000)
default	09:45:30.117438+0800	hootowl	[C3] event: client:connection_reused @5.477s
default	09:45:30.117499+0800	hootowl	Task <6EC8DD19-C575-4F9B-9BCB-1DA167EBFD27>.<3> now using Connection 3
default	09:45:30.118022+0800	hootowl	0x14a499908 - PageConfiguration::delaysWebProcessLaunchUntilFirstLoad() -> false because of associated processPool value
default	09:45:30.118030+0800	hootowl	0x14a3cc508 - WebProcessPool::createWebPage: Not delaying WebProcess launch
default	09:45:30.118035+0800	hootowl	0x131074680 - [PID=0] WebProcessProxy::constructor:
default	09:45:30.118391+0800	hootowl	Successfully created a sandbox extension for '/private/var/containers/Bundle/Application/2290ADA6-FC62-4EB4-863B-0C67EBF31518/hootowl.app'
default	09:45:30.119450+0800	hootowl	Successfully created a sandbox extension for '/private/var/mobile/Containers/Data/Application/9C61D988-8BEB-42B6-A397-1E3A058F7BB4/Library/WebKit/WebsiteData/MediaKeys/v1'
default	09:45:30.119462+0800	hootowl	0x1310301b0 - [PID=0, throttler=0x131074710] ProcessThrottler::Activity::Activity: Starting foreground activity / 'Process initialization'
default	09:45:30.119502+0800	hootowl	0x148ec3118 - [pageProxyID=20, webPageID=21, PID=0] WebPageProxy::constructor, site isolation enabled 0
default	09:45:30.119512+0800	hootowl	PlaybackSessionManagerProxy::PlaybackSessionManagerProxy(867535770)
default	09:45:30.119518+0800	hootowl	PlaybackSessionManagerProxy::VideoPresentationManagerProxy(867535770)
default	09:45:30.119735+0800	hootowl	0x131074680 - [PID=0] WebProcessProxy::addExistingWebPage: webPage=0x148ec3118, pageProxyID=20, webPageID=21
default	09:45:30.120148+0800	hootowl	WebsiteDataStore::propagateSettingUpdates (0x149bbc008) sessionID=1, OptInCookiePartitioning enabled, setting ThirdPartyCookieBlockingMode::AllExceptPartitioned
default	09:45:30.120889+0800	hootowl	0x131050230 - [PID=0] WebProcessCache::updateCapacity: Cache is disabled by client
default	09:45:30.121531+0800	hootowl	Created visibility propagation interaction <_UIVisibilityPropagationInteraction: 0x148062fa0> for process with PID=46064
default	09:45:30.199907+0800	hootowl	nw_endpoint_resolver_update [C11.1.1 gist.githubusercontent.com:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Adding endpoint handler for 185.199.110.133:443
default	09:45:30.199929+0800	hootowl	nw_endpoint_resolver_update [C11.1.1 gist.githubusercontent.com:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Adding endpoint handler for 185.199.109.133:443
default	09:45:30.199963+0800	hootowl	nw_endpoint_resolver_update [C11.1.1 gist.githubusercontent.com:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Adding endpoint handler for 185.199.108.133:443
default	09:45:30.199973+0800	hootowl	nw_endpoint_resolver_update [C11.1.1 gist.githubusercontent.com:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Adding endpoint handler for 185.199.111.133:443
default	09:45:30.200023+0800	hootowl	[C11.1.1 gist.githubusercontent.com:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:receive_dns @0.191s
default	09:45:30.200047+0800	hootowl	0x14c06c558 ID=4 Task <6EC8DD19-C575-4F9B-9BCB-1DA167EBFD27>.<3> sent request, body N 0
default	09:45:30.200123+0800	hootowl	[C7] event: client:connection_idle @4.607s
default	09:45:30.200144+0800	hootowl	nw_protocol_tcp_notify [C7.1.1.1:3] nw_protocol_notification_type_connection_idle is true
default	09:45:30.200162+0800	hootowl	nw_protocol_tcp_set_connection_idle [C7.1.1.1:3] os_nexus_flow_set_connection_idle returned 0
default	09:45:30.200169+0800	hootowl	Task <9ABDA649-77F1-4B70-9828-D27E5CA9CB20>.<8> now using Connection 7
default	09:45:30.200186+0800	hootowl	[C7] event: client:connection_reused @4.607s
default	09:45:30.200340+0800	hootowl	nw_protocol_tcp_notify [C7.1.1.1:3] nw_protocol_notification_type_connection_idle is false
default	09:45:30.200350+0800	hootowl	nw_protocol_tcp_set_connection_idle [C7.1.1.1:3] os_nexus_flow_set_connection_idle returned 0
default	09:45:30.200359+0800	hootowl	Launching process with config: bundleID: com.apple.WebKit.WebContent instance ID: Optional([_EXExtensionInstanceIdentifier: E0F3CF3A-AEE4-4ED0-A985-1735BF137E05])
default	09:45:30.201567+0800	hootowl	[C11.1.1.1 185.199.110.133:443 initial path ((null))] event: path:start @0.191s
default	09:45:30.202095+0800	hootowl	[C11.1.1.1 185.199.110.133:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.192s, uuid: 13D30904-289B-4566-A81E-7A72AC6C4F6B
default	09:45:30.202184+0800	hootowl	[C11.1.1.1 185.199.110.133:443 in_progress channel-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_nexus @0.192s
default	09:45:30.202197+0800	hootowl	0x131068190 - ApplicationStateTracker::setIsInBackground: 0
default	09:45:30.202208+0800	hootowl	0x148c18c00 - WKApplicationStateTrackingView: View with page [0x148ec3118, pageProxyID=20] was added to a window, _lastObservedStateWasBackground=0, isNowBackground=0
default	09:45:30.258388+0800	hootowl	[C11.1.1.1 185.199.110.133:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:receive_nexus @0.249s
default	09:45:30.259201+0800	hootowl	[C11.1.1.1 185.199.110.133:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_connect @0.250s
default	09:45:30.259927+0800	hootowl	tcp_output [C11.1.1.1:3] flags=[SEC] seq=4283226014, ack=0, win=65535 state=SYN_SENT rcv_nxt=0, snd_una=4283226014
default	09:45:30.259942+0800	hootowl	0x148ec3118 - [pageProxyID=20, webPageID=21, PID=0] WebPageProxy::updateActivityState: view visibility state changed 0 -> 1
default	09:45:30.259951+0800	hootowl	0x148ec3118 - [pageProxyID=20, webPageID=21, PID=0] WebPageProxy::viewIsBecomingVisible:
default	09:45:30.259958+0800	hootowl	Screen Time has updated to use the system shield for any blocked URL.
default	09:45:30.259982+0800	hootowl	0x148ec3118 - [pageProxyID=20, webPageID=21, PID=0] WebPageProxy::updateThrottleState: UIProcess is taking a foreground assertion because the view is visible
default	09:45:30.260235+0800	hootowl	0x1310303f0 - [PID=0, throttler=0x131074710] ProcessThrottler::Activity::Activity: Starting foreground activity / 'View is visible'
default	09:45:30.260248+0800	hootowl	RemoteLayerTreeDrawingAreaProxy(23)::hideContentUntilPendingUpdate
default	09:45:30.260255+0800	hootowl	0x148d73000 (pageProxyID=20) -[WKWebView _endLiveResize]
default	09:45:30.260313+0800	hootowl	[C1] event: client:connection_idle @7.274s
default	09:45:30.260319+0800	hootowl	0x148ec3118 - [pageProxyID=20, webPageID=21, PID=0] WebPageProxy::loadRequest:
default	09:45:30.260389+0800	hootowl	0x148ec3118 - [pageProxyID=20, webPageID=21, PID=0] WebPageProxy::loadRequestWithNavigationShared:
default	09:45:30.260457+0800	hootowl	nw_protocol_tcp_notify [C1.1.1.1:3] nw_protocol_notification_type_connection_idle is true
default	09:45:30.260631+0800	hootowl	nw_protocol_tcp_set_connection_idle [C1.1.1.1:3] os_nexus_flow_set_connection_idle returned 0
default	09:45:30.260644+0800	hootowl	Task <4AEBF80A-C0C0-4A75-A035-DF07743AA658>.<7> now using Connection 1
default	09:45:30.260668+0800	hootowl	[C1] event: client:connection_reused @7.274s
default	09:45:30.260710+0800	hootowl	0x131050310 - NavigationState is taking a process network assertion because a page load started
default	09:45:30.260715+0800	hootowl	Taking network activity on WebProcess with PID 0
default	09:45:30.260731+0800	hootowl	0x131030420 - [PID=0, throttler=0x131074710] ProcessThrottler::Activity::Activity: Starting background activity / 'Page Load'
default	09:45:30.262113+0800	hootowl	0x131030450 - [PID=46063, throttler=0x131074150] ProcessThrottler::Activity::Activity: Starting foreground activity / 'WebPageProxy::runJavaScriptInFrameInScriptWorld'
default	09:45:30.263494+0800	hootowl	[ATTrackingManager] trackingAuthorizationStatus API call invoked.
default	09:45:30.263510+0800	hootowl	[ATTrackingManager] Call to trackingAuthorizationStatus eligible for rate limiting. Returning 0
default	09:45:30.263561+0800	hootowl	nw_protocol_tcp_notify [C1.1.1.1:3] nw_protocol_notification_type_connection_idle is false
default	09:45:30.263674+0800	hootowl	nw_protocol_tcp_set_connection_idle [C1.1.1.1:3] os_nexus_flow_set_connection_idle returned 0
default	09:45:30.328496+0800	hootowl	[0x149569e00] activating connection: mach=true listener=false peer=false name=com.apple.ScreenTimeAgent
default	09:45:30.328515+0800	hootowl	WebContent[46063] 0x11e3c4008 - [webPageID=8] WebPage::runJavaScriptInFrameInScriptWorld: frameID=0
default	09:45:30.328528+0800	hootowl	WebContent[46063] 0x11e3c4008 - [webPageID=8] WebPage::runJavaScriptInFrameInScriptWorld: Request to run JavaScript succeeded
default	09:45:30.331646+0800	hootowl	Task <9ABDA649-77F1-4B70-9828-D27E5CA9CB20>.<8> sent request, body N 0
default	09:45:30.331722+0800	hootowl	Task <4AEBF80A-C0C0-4A75-A035-DF07743AA658>.<7> sent request, body N 0
default	09:45:30.336481+0800	hootowl	0x1310304b0 - [PID=46063, throttler=0x131074150] ProcessThrottler::Activity::Activity: Starting foreground activity / 'WebPageProxy::runJavaScriptInFrameInScriptWorld'
default	09:45:30.336622+0800	hootowl	0x131030120 - [PID=46063, throttler=0x131074150] ProcessThrottler::Activity::Activity: Starting foreground activity / 'WebPageProxy::runJavaScriptInFrameInScriptWorld'
default	09:45:30.336652+0800	hootowl	WebContent[46063] 0x11e3c4008 - [webPageID=8] WebPage::runJavaScriptInFrameInScriptWorld: frameID=0
default	09:45:30.336694+0800	hootowl	WebContent[46063] 0x11e3c4008 - [webPageID=8] WebPage::runJavaScriptInFrameInScriptWorld: Request to run JavaScript succeeded
default	09:45:30.336713+0800	hootowl	WebContent[46063] 0x11e3c4008 - [webPageID=8] WebPage::runJavaScriptInFrameInScriptWorld: frameID=0
default	09:45:30.413933+0800	hootowl	WebContent[46063]: [pageID=8, frameID=4294967297, resourceID=33] ResourceLoader::willSendRequestInternal: calling completion handler
default	09:45:30.413942+0800	hootowl	WebContent[46063]: [pageID=8, frameID=4294967297, resourceID=33 SubResourceLoader::willSendRequestInternal: resource load finished; calling completion handler
default	09:45:30.413952+0800	hootowl	WebContent[46063]: [webPageID=8, frameID=4294967297, resourceID=33] WebLoaderStrategy::scheduleLoad: URL will be scheduled with the NetworkProcess
default	09:45:30.413960+0800	hootowl	WebContent[46063]: [webPageID=8, frameID=4294967297, resourceID=33] WebLoaderStrategy::scheduleLoad: Resource is being scheduled with the NetworkProcess (priority=2, existingNetworkResourceLoadIdentifierToResume=0)
default	09:45:30.413969+0800	hootowl	WebContent[46063]: [webPageID=8, frameID=4294967297, resourceID=33] WebResourceLoader::WebResourceLoader
default	09:45:30.413978+0800	hootowl	WebContent[46063]: [pageID=8, frameID=4294967297, resourceID=34] ResourceLoader::willSendRequestInternal: calling completion handler
default	09:45:30.414942+0800	hootowl	WebContent[46063]: [pageID=8, frameID=4294967297, resourceID=34 SubResourceLoader::willSendRequestInternal: resource load finished; calling completion handler
default	09:45:30.414978+0800	hootowl	WebContent[46063]: [webPageID=8, frameID=4294967297, resourceID=34] WebLoaderStrategy::scheduleLoad: URL will be scheduled with the NetworkProcess
default	09:45:30.415050+0800	hootowl	WebContent[46063]: [webPageID=8, frameID=4294967297, resourceID=34] WebLoaderStrategy::scheduleLoad: Resource is being scheduled with the NetworkProcess (priority=2, existingNetworkResourceLoadIdentifierToResume=0)
default	09:45:30.415097+0800	hootowl	WebContent[46063]: [webPageID=8, frameID=4294967297, resourceID=34] WebResourceLoader::WebResourceLoader
default	09:45:30.415713+0800	hootowl	quic_stream_create_inbound [C9.1.1.1:2] [-ea8483eeb705f272] creating inbound stream 7 (out of order)
default	09:45:30.415909+0800	hootowl	Starting death monitoring for handle [xpcservice<com.apple.WebKit.WebContent([app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>:46045])>{vt hash: 71395982}[uuid:E0F3CF3A-AEE4-4ED0-A985-1735BF137E05]{definition:com.apple.WebKit.WebContent[extension][client]}:46067]
default	09:45:30.416452+0800	hootowl	quic_stream_create_inbound [C9.1.1.1:2] [-ea8483eeb705f272] creating inbound stream 11
default	09:45:30.418577+0800	hootowl	Created new process ExtensionProcess: bundleID: com.apple.WebKit.WebContent instance ID: Optional([_EXExtensionInstanceIdentifier: E0F3CF3A-AEE4-4ED0-A985-1735BF137E05]) pid: 46067.
default	09:45:30.419593+0800	hootowl	AssertionCapability::AssertionCapability: taking assertion Foreground
default	09:45:30.424810+0800	hootowl	tcp_input [C11.1.1.1:3] flags=[S.] seq=501783951, ack=4283226015, win=65535 state=SYN_SENT rcv_nxt=0, snd_una=4283226014
default	09:45:30.426837+0800	hootowl	nw_flow_connected [C11.1.1.1 185.199.110.133:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Transport protocol connected (tcp)
default	09:45:30.430418+0800	hootowl	WebContent[46063]: [webPageID=8, frameID=4294967297, resourceID=34] WebResourceLoader::didReceiveResponse: (httpStatusCode=200)
default	09:45:30.430535+0800	hootowl	[C11.1.1.1 185.199.110.133:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_transport @0.416s
default	09:45:30.430558+0800	hootowl	WebContent[46063]: [webPageID=8, frameID=4294967297, resourceID=34] WebResourceLoader::didReceiveData: Started receiving data
default	09:45:30.431447+0800	hootowl	WebContent[46063]: [webPageID=8, frameID=4294967297, resourceID=34] WebResourceLoader::didFinishResourceLoad: (length=407)
default	09:45:30.431493+0800	hootowl	WebContent[46063]: [pageID=8, frameID=4294967297, resourceID=34 SubResourceLoader::didFinishLoading
default	09:45:30.432420+0800	hootowl	boringssl_session_apply_protocol_options_for_transport_block_invoke_2(2367) [C11.1.1.1:2][0x149a282e0] TLS configured [server(0) min_version(0x0303) max_version(0x0304) name(gist.githubusercontent.com) tickets(false) false_start(false) enforce_ev(false) enforce_ats(false) ats_non_pfs_ciphersuite_allowed(false) cc_mode_enforced(false) ech(false) pqtls(true), pake(false) skip_ats_trust(false)]
default	09:45:30.432461+0800	hootowl	boringssl_context_info_handler(2806) [C11.1.1.1:2][0x149a282e0] Client handshake started
default	09:45:30.432708+0800	hootowl	boringssl_context_info_handler(2823) [C11.1.1.1:2][0x149a282e0] Client handshake state: TLS client enter_early_data
default	09:45:30.433156+0800	hootowl	boringssl_context_info_handler(2823) [C11.1.1.1:2][0x149a282e0] Client handshake state: TLS client read_server_hello
default	09:45:30.434840+0800	hootowl	0x131050380 - [PID=0] WebProcessCache::updateCapacity: Cache is disabled because process swap on navigation is disabled
default	09:45:30.435403+0800	hootowl	0x14c0ab9d8 ID=0 Task <93538818-97EE-404C-8274-265196A34402>.<5> received response, status 500 content K
default	09:45:30.435441+0800	hootowl	[0x14956b980] activating connection: mach=true listener=false peer=false name=com.apple.trustd
default	09:45:30.436285+0800	hootowl	0x14a49a308 - PageConfiguration::delaysWebProcessLaunchUntilFirstLoad() -> false because of associated processPool value
default	09:45:30.436290+0800	hootowl	0x14a3cca08 - WebProcessPool::createWebPage: Not delaying WebProcess launch
default	09:45:30.436297+0800	hootowl	0x131074c40 - [PID=0] WebProcessProxy::constructor:
default	09:45:30.436364+0800	hootowl	Successfully created a sandbox extension for '/private/var/containers/Bundle/Application/2290ADA6-FC62-4EB4-863B-0C67EBF31518/hootowl.app'
default	09:45:30.437391+0800	hootowl	Successfully created a sandbox extension for '/private/var/mobile/Containers/Data/Application/9C61D988-8BEB-42B6-A397-1E3A058F7BB4/Library/WebKit/WebsiteData/MediaKeys/v1'
default	09:45:30.437413+0800	hootowl	0x131030510 - [PID=0, throttler=0x131074cd0] ProcessThrottler::Activity::Activity: Starting foreground activity / 'Process initialization'
default	09:45:30.437422+0800	hootowl	0x148ec2318 - [pageProxyID=375, webPageID=376, PID=0] WebPageProxy::constructor, site isolation enabled 0
default	09:45:30.437477+0800	hootowl	PlaybackSessionManagerProxy::PlaybackSessionManagerProxy(1292624887)
default	09:45:30.437489+0800	hootowl	PlaybackSessionManagerProxy::VideoPresentationManagerProxy(1292624887)
default	09:45:30.437504+0800	hootowl	0x131074c40 - [PID=0] WebProcessProxy::addExistingWebPage: webPage=0x148ec2318, pageProxyID=375, webPageID=376
default	09:45:30.437513+0800	hootowl	0x131050380 - [PID=0] WebProcessCache::updateCapacity: Cache is disabled by client
default	09:45:30.437822+0800	hootowl	Created visibility propagation interaction <_UIVisibilityPropagationInteraction: 0x1480633c0> for process with PID=46064
default	09:45:30.437838+0800	hootowl	Launching process with config: bundleID: com.apple.WebKit.WebContent instance ID: Optional([_EXExtensionInstanceIdentifier: 2263C525-304F-4342-BED8-324592BF25D1])
default	09:45:30.438419+0800	hootowl	0x131068220 - ApplicationStateTracker::setIsInBackground: 0
default	09:45:30.438458+0800	hootowl	0x148c1c800 - WKApplicationStateTrackingView: View with page [0x148ec2318, pageProxyID=375] was added to a window, _lastObservedStateWasBackground=0, isNowBackground=0
default	09:45:30.439263+0800	hootowl	0x148ec2318 - [pageProxyID=375, webPageID=376, PID=0] WebPageProxy::updateActivityState: view visibility state changed 0 -> 1
default	09:45:30.439271+0800	hootowl	0x148ec2318 - [pageProxyID=375, webPageID=376, PID=0] WebPageProxy::viewIsBecomingVisible:
default	09:45:30.439279+0800	hootowl	Screen Time has updated to use the system shield for any blocked URL.
default	09:45:30.439285+0800	hootowl	0x148ec2318 - [pageProxyID=375, webPageID=376, PID=0] WebPageProxy::updateThrottleState: UIProcess is taking a foreground assertion because the view is visible
default	09:45:30.439292+0800	hootowl	0x131030600 - [PID=0, throttler=0x131074cd0] ProcessThrottler::Activity::Activity: Starting foreground activity / 'View is visible'
default	09:45:30.439347+0800	hootowl	RemoteLayerTreeDrawingAreaProxy(378)::hideContentUntilPendingUpdate
default	09:45:30.439354+0800	hootowl	0x148d72800 (pageProxyID=375) -[WKWebView _endLiveResize]
default	09:45:30.440457+0800	hootowl	[0x14956b980] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	09:45:30.442087+0800	hootowl	Task <93538818-97EE-404C-8274-265196A34402>.<5> response ended
default	09:45:30.442874+0800	hootowl	0x131030450 - [PID=46063, throttler=0x131074150] ProcessThrottler::Activity::invalidate: Ending foreground activity / 'WebPageProxy::runJavaScriptInFrameInScriptWorld'
default	09:45:30.442951+0800	hootowl	0x1310304b0 - [PID=46063, throttler=0x131074150] ProcessThrottler::Activity::invalidate: Ending foreground activity / 'WebPageProxy::runJavaScriptInFrameInScriptWorld'
default	09:45:30.442960+0800	hootowl	Screen Time has updated to use the system shield for any blocked URL.
default	09:45:30.442989+0800	hootowl	[0x148ebb700] activating connection: mach=false listener=false peer=false name=(anonymous)
default	09:45:30.443667+0800	hootowl	[C9] event: client:connection_idle @2.255s
default	09:45:30.443711+0800	hootowl	Task <93538818-97EE-404C-8274-265196A34402>.<5> done using Connection 9
default	09:45:30.444415+0800	hootowl	Task <93538818-97EE-404C-8274-265196A34402>.<5> summary for task success {transaction_duration_ms=2652, response_status=500, connection=9, protocol="h3", domain_lookup_duration_ms=174, connect_duration_ms=1143, secure_connection_duration_ms=1013, private_relay=false, request_start_ms=1911, request_duration_ms=9, response_start_ms=2639, response_duration_ms=12, request_bytes=155, request_throughput_kbps=128, response_bytes=486, response_throughput_kbps=299, cache_hit=false}
default	09:45:30.444487+0800	hootowl	Task <93538818-97EE-404C-8274-265196A34402>.<5> finished successfully
default	09:45:30.444494+0800	hootowl	TX focusApplication (peekAppEvent) stealKB:Y scene:com.sharkda.hootowl-83FF55F6-7B28-4BFD-8825-33CB43E5D162
default	09:45:30.444531+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:30.444545+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	09:45:30.444562+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1481fc400>; contextId: 0xF4D9041F
default	09:45:30.445272+0800	hootowl	Task <9ABDA649-77F1-4B70-9828-D27E5CA9CB20>.<8> received response, status 200 content C
default	09:45:30.445453+0800	hootowl	Task <4AEBF80A-C0C0-4A75-A035-DF07743AA658>.<7> received response, status 200 content K
default	09:45:30.445636+0800	hootowl	0x14c06c558 ID=4 Task <6EC8DD19-C575-4F9B-9BCB-1DA167EBFD27>.<3> received response, status 200 content K
default	09:45:30.456559+0800	hootowl	Starting death monitoring for handle [xpcservice<com.apple.WebKit.WebContent([app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>:46045])>{vt hash: 71395982}[uuid:2263C525-304F-4342-BED8-324592BF25D1]{definition:com.apple.WebKit.WebContent[extension][client]}:46068]
default	09:45:30.456702+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:30.458184+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:30.458220+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	09:45:30.458230+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1481fc400>; contextId: 0xF4D9041F
default	09:45:30.459424+0800	hootowl	Created new process ExtensionProcess: bundleID: com.apple.WebKit.WebContent instance ID: Optional([_EXExtensionInstanceIdentifier: 2263C525-304F-4342-BED8-324592BF25D1]) pid: 46068.
default	09:45:30.459450+0800	hootowl	AssertionCapability::AssertionCapability: taking assertion Foreground
default	09:45:30.459867+0800	hootowl	<UIWindowScene: 0x148378200> (83FF55F6-7B28-4BFD-8825-33CB43E5D162) Scene updated orientation preferences: ( Pu ) -> ( Pu Ll Lr )
default	09:45:30.460295+0800	hootowl	<UIWindowScene: 0x148378200> (83FF55F6-7B28-4BFD-8825-33CB43E5D162) Scene updated orientation preferences: ( Pu Ll Lr ) -> ( Pu )
default	09:45:30.469399+0800	hootowl	MncplCyclopsScreen 78
🏠 body eval — items:6 firstObs:5s firstCar:0
default	09:45:30.490509+0800	hootowl	MncplCyclopsScreen 78
🏠 body eval — items:6 firstObs:5s firstCar:0
fault	09:45:30.496296+0800	hootowl	__delegate_identifier__:Performance Diagnostics__:::____message__:{"message":"Interprocess communication on the main thread can cause non-deterministic delays.","antipattern trigger":"-[AVAudioSession setActive:withOptions:error:]","message type":"suppressable","issue type":1,"category type":17,"subcategory type":0,"show in console":"0"}'5C 1D 99 DD E0 FB 36 D2 81 44 D1 3E C7 94 D6 09 FC 97 03 00 5C 1D 99 DD E0 FB 36 D2 81 44 D1 3E C7 94 D6 09 A8 BA 0C 00 5C 1D 99 DD E0 FB 36 D2 81 44 D1 3E C7 94 D6 09 34 E3 1F 00 9C 46 02 57 4A 68 37 D5 82 C4 55 C3 3C 0A 25 9E BC A8 0B 00 9C 46 02 57 4A 68 37 D5 82 C4 55 C3 3C 0A 25 9E D8 A4 0B 00 9C 46 02 57 4A 68 37 D5 82 C4 55 C3 3C 0A 25 9E 98 9F 0B 00 9C 46 02 57 4A 68 37 D5 82 C4 55 C3 3C 0A 25 9E C0 2B 06 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 4C 4E 1C 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 84 63 1C 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 10 4E 1B 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 24 74 07 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 2C 7F 01 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 44 7C 32 00 E1 18 0F C2 AA 2B 3F E3 B2 6E D4 52 27 36 44 57 18 6E 00 00 E1 18 0F C2 AA 2B 3F E3 B2 6E D4 52 27 36 44 57 AC 6D 00 00 E1 18 0F C2 AA 2B 3F E3 B2 6E D4 52 27 36 44 57 04 02 01 00 66 91 CD 79 AE 1D 32 2A 96 63 28 2E 38 36 C4 C8 94 31 00 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 44 45 00 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 48 F7 03 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 04 42 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 44 41 01 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 68 20 0A 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 04 F6 02 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 4C E5 02 00 41 11 65 E2 EE 8E 38 0E B2 54 99 77 27 39 71 E3 98 14 00 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 70 16 12 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 58 C1 08 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 70 05 03 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D F4 D0 02 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 48 CC 02 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 14 8C 36 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 C0 8C 36 00 0F 8D 35 B6 55 6F 3E 34 8E AA 80 AB 54 04 7D C5 1C 4C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
default	09:45:30.500582+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 1
default	09:45:30.500652+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:30.502068+0800	hootowl	TX focusApplication (peekAppEvent) stealKB:Y scene:com.sharkda.hootowl-83FF55F6-7B28-4BFD-8825-33CB43E5D162
default	09:45:30.502116+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:30.502199+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	09:45:30.502249+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1481fc400>; contextId: 0xF4D9041F
default	09:45:30.503750+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:30.503774+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:30.503791+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	09:45:30.503813+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1481fc400>; contextId: 0xF4D9041F
default	09:45:30.510277+0800	hootowl	<UIWindowScene: 0x148378200> (83FF55F6-7B28-4BFD-8825-33CB43E5D162) Scene updated orientation preferences: ( Pu ) -> ( Pu Ll Lr )
default	09:45:30.525316+0800	hootowl	MncplCyclopsScreen 78
🏠 body eval — items:6 firstObs:5s firstCar:0
default	09:45:30.534688+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:30.534765+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 1
default	09:45:30.535068+0800	hootowl	TX focusApplication (peekAppEvent) stealKB:Y scene:com.sharkda.hootowl-83FF55F6-7B28-4BFD-8825-33CB43E5D162
default	09:45:30.535116+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:30.535130+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	09:45:30.535151+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1481fc400>; contextId: 0xF4D9041F
default	09:45:30.536281+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:30.536303+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:30.536314+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	09:45:30.536325+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1481fc400>; contextId: 0xF4D9041F
default	09:45:30.537420+0800	hootowl	<UIWindowScene: 0x148378200> (83FF55F6-7B28-4BFD-8825-33CB43E5D162) Scene updated orientation preferences: ( Pu Ll Lr ) -> ( Pu )
default	09:45:30.539727+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 1
default	09:45:30.539860+0800	hootowl	TX focusApplication (peekAppEvent) stealKB:Y scene:com.sharkda.hootowl-83FF55F6-7B28-4BFD-8825-33CB43E5D162
default	09:45:30.539887+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:30.539935+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	09:45:30.540002+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1481fc400>; contextId: 0xF4D9041F
default	09:45:30.542045+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:30.542089+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:30.542113+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	09:45:30.542268+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1481fc400>; contextId: 0xF4D9041F
default	09:45:30.543819+0800	hootowl	<UIWindowScene: 0x148378200> (83FF55F6-7B28-4BFD-8825-33CB43E5D162) Scene updated orientation preferences: ( Pu ) -> ( Pu Ll Lr )
fault	09:45:30.549858+0800	hootowl	__delegate_identifier__:Performance Diagnostics__:::____message__:{"message":"Performing I/O on the main thread can cause hangs.","antipattern trigger":"-[NSBundle bundleIdentifier]","message type":"suppressable","issue type":1,"category type":17,"subcategory type":3,"show in console":"0"}'F7 90 60 28 1C 6D 3B 4C BD 93 78 C1 96 C8 3A 83 00 B9 0A 00 C3 9B D2 2C 34 75 38 AF 91 BD 0B 75 74 08 10 11 7C 4A 55 00 C3 9B D2 2C 34 75 38 AF 91 BD 0B 75 74 08 10 11 F0 3F 8B 00 C3 9B D2 2C 34 75 38 AF 91 BD 0B 75 74 08 10 11 64 9F C6 00 C3 9B D2 2C 34 75 38 AF 91 BD 0B 75 74 08 10 11 8C CA 5D 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 14 19 52 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 7C C6 42 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 88 A6 4D 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 E0 A0 4D 00 73 84 1A A3 BF DD 32 2D 8D C2 E5 18 5A 14 DE E1 C4 4B 02 00 73 84 1A A3 BF DD 32 2D 8D C2 E5 18 5A 14 DE E1 D0 47 02 00 73 84 1A A3 BF DD 32 2D 8D C2 E5 18 5A 14 DE E1 F8 48 02 00 73 84 1A A3 BF DD 32 2D 8D C2 E5 18 5A 14 DE E1 94 44 02 00 73 84 1A A3 BF DD 32 2D 8D C2 E5 18 5A 14 DE E1 70 47 02 00 73 84 1A A3 BF DD 32 2D 8D C2 E5 18 5A 14 DE E1 28 39 02 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 24 47 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 48 F7 03 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 04 42 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 44 41 01 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 68 20 0A 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 04 F6 02 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 4C E5 02 00 41 11 65 E2 EE 8E 38 0E B2 54 99 77 27 39 71 E3 98 14 00 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 70 16 12 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 58 C1 08 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 70 05 03 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D F4 D0 02 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 48 CC 02 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 14 8C 36 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 C0 8C 36 00 0F 8D 35 B6 55 6F 3E 34 8E AA 80 AB 54 04 7D C5 1C 4C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
default	09:45:30.550678+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 1
default	09:45:30.554403+0800	hootowl	MncplCyclopsScreen 78
🏠 body eval — items:6 firstObs:5s firstCar:0
fault	09:45:30.573805+0800	hootowl	__delegate_identifier__:Performance Diagnostics__:::____message__:{"message":"Performing I/O on the main thread can cause hangs.","antipattern trigger":"-[NSBundle bundleIdentifier]","message type":"suppressable","issue type":1,"category type":17,"subcategory type":3,"show in console":"0"}'17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 7C E5 62 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D EC C3 B3 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 94 C4 B3 00 82 A2 1C E4 4E 43 38 FB 98 62 F0 BE 7B 90 9D F1 14 16 03 00 82 A2 1C E4 4E 43 38 FB 98 62 F0 BE 7B 90 9D F1 B0 11 03 00 82 A2 1C E4 4E 43 38 FB 98 62 F0 BE 7B 90 9D F1 48 0F 03 00 82 A2 1C E4 4E 43 38 FB 98 62 F0 BE 7B 90 9D F1 A4 4A 02 00 82 A2 1C E4 4E 43 38 FB 98 62 F0 BE 7B 90 9D F1 24 42 02 00 82 A2 1C E4 4E 43 38 FB 98 62 F0 BE 7B 90 9D F1 D0 FF 4F 00 A9 73 AD 42 3C FF 3C 90 BC 78 E4 E0 BF FA 15 5B 14 C9 00 00 A9 73 AD 42 3C FF 3C 90 BC 78 E4 E0 BF FA 15 5B 4C E7 00 00 82 A2 1C E4 4E 43 38 FB 98 62 F0 BE 7B 90 9D F1 40 50 08 00 82 A2 1C E4 4E 43 38 FB 98 62 F0 BE 7B 90 9D F1 9C D7 01 00 82 A2 1C E4 4E 43 38 FB 98 62 F0 BE 7B 90 9D F1 88 B4 12 00 82 A2 1C E4 4E 43 38 FB 98 62 F0 BE 7B 90 9D F1 FC AF 12 00 82 A2 1C E4 4E 43 38 FB 98 62 F0 BE 7B 90 9D F1 60 AE 12 00 CA BC CF 8B 28 93 39 39 8C 05 38 CF 2E 43 EB 55 3C 43 00 00 CA BC CF 8B 28 93 39 39 8C 05 38 CF 2E 43 EB 55 78 43 00 00 CA BC CF 8B 28 93 39 39 8C 05 38 CF 2E 43 EB 55 18 69 00 00 CA BC CF 8B 28 93 39 39 8C 05 38 CF 2E 43 EB 55 40 12 00 00 CA BC CF 8B 28 93 39 39 8C 05 38 CF 2E 43 EB 55 9C 11 00 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 14 0A 0D 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 70 07 0D 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 44 17 0D 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 8C E2 1D 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 38 40 1E 00 82 A2 1C E4 4E 43 38 FB 98 62 F0 BE 7B 90 9D F1 70 70 04 00 82 A2 1C E4 4E 43 38 FB 98 62 F0 BE 7B 90 9D F1 20 71 04 00 82 A2 1C E4 4E 43 38 FB 98 62 F0 BE 7B 90 9D F1 BC DD 00 00 82 A2 1C E4 4E 43 38 FB 98 62 F0 BE 7B 90 9D F1 24 6F 04 00 82 A2 1C E4 4E 43 38 FB 98 62 F0 BE 7B 90 9D F1 80 6E 04 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 B0 E1 1D 00 82 A2 1C E4 4E 43 38 FB 98 62 F0 BE 7B 90 9D F1 0C 7F 21 00 82 A2 1C E4 4E 43 38 FB 98 62 F0 BE 7B 90 9D F1 90 8D 21 00 82 A2 1C E4 4E 43 38 FB 98 62 F0 BE 7B 90 9D F1 54 00 01 00 82 A2 1C E4 4E 43 38 FB 98 62 F0 BE 7B 90 9D F1 54 F6 00 00 82 A2 1C E4 4E 43 38 FB 98 62 F0 BE 7B 90 9D F1 20 C7 07 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D B4 74 4A 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D A0 76 4A 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 20 29 35 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 98 2C EA 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 88 A8 D5 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 68 0A 90 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 30 AD 35 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC F8 54 55 01 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 84 17 62 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 60 C4 8F 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 30 07 90 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC A8 E0 5A 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC B8 D9 5A 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 64 D7 5A 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC D4 1D 0F 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC FC 63 0B 00 F3 95 52 EF B5 2C 38 D1 92 90 6B 3A 75 65 B0 5B 54 97 00 00 F3 95 52 EF B5 2C 38 D1 92 90 6B 3A 75 65 B0 5B 1C 7C 04 00 F3 95 52 EF B5 2C 38 D1 92 90 6B 3A 75 65 B0 5B 24 D3 00 00 F3 95 52 EF B5 2C 38 D1 92 90 6B 3A 75 65 B0 5B F4 89 01 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 14 65 0F 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 90 E9 0D 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 68 2A 0F 00 54 14 D8 03 4E 97 34 AB 94 F7 35 CE B7 A7 53 71 20 0A 06 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 80 F4 0D 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC B8 85 0F 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 88 21 0E 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC D4 B6 0F 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 60 8C 0F 00 26 FA B8 14 4C 8F 3A 06 B4 5E CB A2 71 02 0D C4 6C 15 00 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 90 03 0A 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 04 03 0A 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 3C 56 06 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 A0 F1 02 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 4C E5 02 00 41 11 65 E2 EE 8E 38 0E B2 54 99 77 27 39 71 E3 98 14 00 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 70 16 12 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 58 C1 08 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 70 05 03 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D F4 D0 02 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 48 CC 02 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 14 8C 36 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 C0 8C 36 00 0F 8D 35 B6 55 6F 3E 34 8E AA 80 AB 54 04 7D C5 1C 4C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
default	09:45:30.602631+0800	hootowl	[0x148f18280] activating connection: mach=true listener=false peer=false name=com.apple.geod
default	09:45:30.625917+0800	hootowl	Metal API Validation Enabled
default	09:45:30.740539+0800	hootowl	Did not find downloaded resource "default.csv" at "(null)", trying fallback
error	09:45:30.741499+0800	hootowl	Failed to locate resource named "default.csv"
default	09:45:30.745412+0800	hootowl	Did not find downloaded resource "groundSettings.json" at "(null)", trying fallback
default	09:45:30.753712+0800	hootowl	[0x14978e6c0] activating connection: mach=true listener=false peer=false name=com.apple.geod
default	09:45:30.754300+0800	hootowl	[0x14978e080] activating connection: mach=true listener=true peer=false name=com.apple.notifyd.matching
default	09:45:30.762065+0800	hootowl	Task <6EC8DD19-C575-4F9B-9BCB-1DA167EBFD27>.<3> response ended
default	09:45:30.762464+0800	hootowl	[C3] event: client:connection_idle @6.122s
default	09:45:30.762628+0800	hootowl	Did not find downloaded resource "CurrencyStyleAttributes.plist" at "(null)", trying fallback
default	09:45:30.762960+0800	hootowl	Task <6EC8DD19-C575-4F9B-9BCB-1DA167EBFD27>.<3> done using Connection 3
default	09:45:30.762979+0800	hootowl	Task <6EC8DD19-C575-4F9B-9BCB-1DA167EBFD27>.<3> summary for task success {transaction_duration_ms=647, response_status=200, connection=3, reused=1, reused_after_ms=2817, request_start_ms=1, request_duration_ms=83, response_start_ms=330, response_duration_ms=317, request_bytes=8732, request_throughput_kbps=839, response_bytes=25152, response_throughput_kbps=634, cache_hit=false}
default	09:45:30.763101+0800	hootowl	Task <6EC8DD19-C575-4F9B-9BCB-1DA167EBFD27>.<3> finished successfully
default	09:45:30.768032+0800	hootowl	boringssl_context_info_handler(2823) [C11.1.1.1:2][0x149a282e0] Client handshake state: TLS 1.3 client read_hello_retry_request
default	09:45:30.768086+0800	hootowl	boringssl_context_info_handler(2823) [C11.1.1.1:2][0x149a282e0] Client handshake state: TLS 1.3 client read_server_hello
default	09:45:30.768212+0800	hootowl	boringssl_context_info_handler(2823) [C11.1.1.1:2][0x149a282e0] Client handshake state: TLS 1.3 client read_encrypted_extensions
default	09:45:30.768440+0800	hootowl	boringssl_context_info_handler(2823) [C11.1.1.1:2][0x149a282e0] Client handshake state: TLS 1.3 client read_certificate_request
default	09:45:30.768559+0800	hootowl	boringssl_context_info_handler(2823) [C11.1.1.1:2][0x149a282e0] Client handshake state: TLS 1.3 client read_server_certificate
default	09:45:30.768587+0800	hootowl	boringssl_context_info_handler(2823) [C11.1.1.1:2][0x149a282e0] Client handshake state: TLS 1.3 client read_server_certificate_verify
default	09:45:30.768943+0800	hootowl	boringssl_context_evaluate_trust_async(2249) [C11.1.1.1:2][0x149a282e0] Performing external trust evaluation
default	09:45:30.768990+0800	hootowl	boringssl_context_evaluate_trust_async_external(2234) [C11.1.1.1:2][0x149a282e0] Asyncing for external verify block
default	09:45:30.769273+0800	hootowl	Connection 11: asked to evaluate TLS Trust
default	09:45:30.769289+0800	hootowl	Task <77E2D366-C6BB-4243-8B20-397A36B5FC01>.<6> auth completion disp=1 cred=0x0
default	09:45:30.769373+0800	hootowl	(Trust 0x14b58d200) No pending evals, starting
default	09:45:30.769506+0800	hootowl	[0x14978fc00] activating connection: mach=true listener=false peer=false name=com.apple.trustd
default	09:45:30.769514+0800	hootowl	(Trust 0x14b58d200) Completed async eval kickoff
default	09:45:30.781754+0800	hootowl	Did not find downloaded resource "NonTiledAssets.pb" at "(null)", trying fallback
default	09:45:30.785629+0800	hootowl	(Trust 0x14b58d200) trustd returned 4
default	09:45:30.786040+0800	hootowl	System Trust Evaluation yielded status(0)
default	09:45:30.786564+0800	hootowl	(Trust 0x14b58d140) No pending evals, starting
default	09:45:30.786840+0800	hootowl	[0x14978ebc0] activating connection: mach=true listener=false peer=false name=com.apple.trustd
default	09:45:30.786848+0800	hootowl	(Trust 0x14b58d140) Completed async eval kickoff
default	09:45:30.788235+0800	hootowl	[0x14978fc00] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	09:45:30.797580+0800	hootowl	(Trust 0x14b58d140) trustd returned 4
default	09:45:30.798881+0800	hootowl	Connection 11: TLS Trust result 0
default	09:45:30.799031+0800	hootowl	boringssl_context_evaluate_trust_async_external_block_invoke_3(2148) [C11.1.1.1:2][0x149a282e0] Returning from external verify block with result: true
default	09:45:30.799118+0800	hootowl	boringssl_context_certificate_verify_callback(2430) [C11.1.1.1:2][0x149a282e0] Certificate verification result: OK
default	09:45:30.799184+0800	hootowl	[0x14b669e00] activating connection: mach=false listener=false peer=false name=com.apple.PerfPowerTelemetryClientRegistrationService
default	09:45:30.799196+0800	hootowl	boringssl_context_info_handler(2823) [C11.1.1.1:2][0x149a282e0] Client handshake state: TLS 1.3 client read_server_finished
default	09:45:30.799453+0800	hootowl	boringssl_context_info_handler(2823) [C11.1.1.1:2][0x149a282e0] Client handshake state: TLS 1.3 client send_end_of_early_data
error	09:45:30.799463+0800	hootowl	CAMetalLayer ignoring invalid setDrawableSize width=0.000000 height=0.000000
default	09:45:30.799531+0800	hootowl	boringssl_context_info_handler(2823) [C11.1.1.1:2][0x149a282e0] Client handshake state: TLS 1.3 client send_client_encrypted_extensions
default	09:45:30.799550+0800	hootowl	boringssl_context_info_handler(2823) [C11.1.1.1:2][0x149a282e0] Client handshake state: TLS 1.3 client send_client_certificate
default	09:45:30.799616+0800	hootowl	boringssl_context_info_handler(2823) [C11.1.1.1:2][0x149a282e0] Client handshake state: TLS 1.3 client complete_second_flight
default	09:45:30.799676+0800	hootowl	boringssl_context_info_handler(2823) [C11.1.1.1:2][0x149a282e0] Client handshake state: TLS 1.3 client done
default	09:45:30.799776+0800	hootowl	boringssl_context_info_handler(2823) [C11.1.1.1:2][0x149a282e0] Client handshake state: TLS client finish_client_handshake
default	09:45:30.799813+0800	hootowl	boringssl_context_info_handler(2823) [C11.1.1.1:2][0x149a282e0] Client handshake state: TLS client done
default	09:45:30.799822+0800	hootowl	boringssl_context_info_handler(2812) [C11.1.1.1:2][0x149a282e0] Client handshake done
default	09:45:30.799853+0800	hootowl	[0x14b669e00] failed to do a bootstrap look-up: xpc_error=[159: Unknown error: 159]
default	09:45:30.799938+0800	hootowl	[0x14b669e00] invalidated after a failed init
default	09:45:30.800481+0800	hootowl	nw_protocol_boringssl_signal_connected(895) [C11.1.1.1:2][0x149a282e0] TLS connected [server(0) version(0x0304) ciphersuite(TLS_AES_128_GCM_SHA256) group(0x11ec) signature_alg(0x0804) alpn(h2) resumed(0) offered_ticket(0) in_early_data(0) early_data_accepted(0) false_started(0) ocsp_received(0) sct_received(0) connect_time(372ms) flight_time(340ms) rtt(339ms) write_stalls(0) read_stalls(4) pake(0x0000)]
default	09:45:30.800817+0800	hootowl	nw_flow_connected [C11.1.1.1 185.199.110.133:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (CFNetworkConnection-4283075305)
default	09:45:30.802232+0800	hootowl	[C11.1.1.1 185.199.110.133:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.792s
error	09:45:30.802314+0800	hootowl	Connection error: Error Domain=NSCocoaErrorDomain Code=4099 "The connection to service named com.apple.PerfPowerTelemetryClientRegistrationService was invalidated: Connection init failed at lookup with error 159 - Sandbox restriction." UserInfo={NSDebugDescription=The connection to service named com.apple.PerfPowerTelemetryClientRegistrationService was invalidated: Connection init failed at lookup with error 159 - Sandbox restriction.}
error	09:45:30.806431+0800	hootowl	(+[PPSClientDonation isRegisteredSubsystem:category:]) Permission denied: Maps / SpringfieldUsage
default	09:45:30.809854+0800	hootowl	[C11.1.1 gist.githubusercontent.com:443 ready resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.800s
default	09:45:30.810601+0800	hootowl	[C11.1 gist.githubusercontent.com:443 ready transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.801s
error	09:45:30.810864+0800	hootowl	(+[PPSClientDonation sendEventWithIdentifier:payload:]) Invalid inputs: payload={
    isSPR = 0;
}
default	09:45:30.811002+0800	hootowl	[C11.1.1.1 185.199.110.133:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.802s
default	09:45:30.811145+0800	hootowl	[C11.1.1 gist.githubusercontent.com:443 ready resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.802s
default	09:45:30.811178+0800	hootowl	[C11.1 gist.githubusercontent.com:443 ready transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.802s
default	09:45:30.811217+0800	hootowl	nw_flow_connected [C11 185.199.110.133:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (endpoint_flow)
default	09:45:30.811384+0800	hootowl	[C11 185.199.110.133:443 ready parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_connect @0.802s
default	09:45:30.811790+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C11] reporting state ready
default	09:45:30.811803+0800	hootowl	[C11 185.199.110.133:443 ready parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.802s
default	09:45:30.813601+0800	hootowl	nw_connection_send_viability_changed_on_nw_queue [C11] viability_changed_handler(true)
default	09:45:30.815144+0800	hootowl	[0x14978ebc0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	09:45:30.815155+0800	hootowl	Connection 11: connected successfully
default	09:45:30.815161+0800	hootowl	Connection 11: TLS handshake complete
default	09:45:30.815171+0800	hootowl	Connection 11: ready C(N) E(N)
default	09:45:30.815308+0800	hootowl	[C11] event: client:connection_reused @0.805s
default	09:45:30.815449+0800	hootowl	nw_protocol_tcp_notify [C11.1.1.1:3] nw_protocol_notification_type_connection_idle is false
default	09:45:30.815474+0800	hootowl	nw_protocol_tcp_set_connection_idle [C11.1.1.1:3] os_nexus_flow_set_connection_idle returned 0
default	09:45:30.815491+0800	hootowl	Task <77E2D366-C6BB-4243-8B20-397A36B5FC01>.<6> now using Connection 11
default	09:45:30.815531+0800	hootowl	Connection 11: received viability advisory(Y)
default	09:45:30.815643+0800	hootowl	Task <77E2D366-C6BB-4243-8B20-397A36B5FC01>.<6> sent request, body N 0
default	09:45:30.824126+0800	hootowl	[0x1495630c0] activating connection: mach=true listener=false peer=false name=com.apple.geoanalyticsd
default	09:45:30.838676+0800	hootowl	{"msg":"CLLocationManager", "event":"activity", "_cmd":"startUpdatingLocation", "self":"0x1483580a0"}
default	09:45:30.856081+0800	hootowl	[(FBSceneManager):sceneID:com.sharkda.hootowl-83FF55F6-7B28-4BFD-8825-33CB43E5D162] Sending action(s): BLSInvalidateFrameSpecifiersAction
default	09:45:30.856838+0800	hootowl	[ATTrackingManager] trackingAuthorizationStatus API call invoked.
default	09:45:30.856857+0800	hootowl	[ATTrackingManager] Call to trackingAuthorizationStatus eligible for rate limiting. Returning 0
default	09:45:30.877424+0800	hootowl	0x131030450 - [PID=46063, throttler=0x131074150] ProcessThrottler::Activity::Activity: Starting foreground activity / 'WebPageProxy::runJavaScriptInFrameInScriptWorld'
default	09:45:30.877799+0800	hootowl	Requesting container lookup; class = 12, identifier = com.apple.geod, group_identifier = (null), create = 1, temp = 0, euid = 501, uid = 501
default	09:45:30.877870+0800	hootowl	WebContent[46063] 0x11e3c4008 - [webPageID=8] WebPage::runJavaScriptInFrameInScriptWorld: frameID=0
default	09:45:30.878510+0800	hootowl	WebContent[46063] 0x11e3c4008 - [webPageID=8] WebPage::runJavaScriptInFrameInScriptWorld: Request to run JavaScript succeeded
default	09:45:30.879035+0800	hootowl	_container_query_get_result_at_index: success
default	09:45:30.879115+0800	hootowl	container_system_path_for_identifier: success
default	09:45:30.879151+0800	hootowl	Requesting container lookup; class = 12, identifier = com.apple.geod, group_identifier = (null), create = 1, temp = 0, euid = 501, uid = 501
default	09:45:30.880981+0800	hootowl	_container_query_get_result_at_index: success
default	09:45:30.881237+0800	hootowl	container_system_path_for_identifier: success
default	09:45:30.881299+0800	hootowl	Requesting container lookup; class = 12, identifier = com.apple.geod, group_identifier = (null), create = 1, temp = 0, euid = 501, uid = 501
default	09:45:30.881656+0800	hootowl	_container_query_get_result_at_index: success
default	09:45:30.882049+0800	hootowl	container_system_path_for_identifier: success
default	09:45:30.914603+0800	hootowl	    AVAudioSession_iOS.mm:996   Activated session 0x77c67d3
default	09:45:30.950613+0800	hootowl	Received state update for 46045 (app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>, unknown-NotVisible
error	09:45:30.961647+0800	hootowl	110	postCloudFunc(receiptText:_:isSpecific:)	noResult!
default	09:45:30.961668+0800	hootowl	0x131074680 - [PID=46067] WebProcessProxy::didFinishLaunching:
default	09:45:30.962246+0800	hootowl	0x131074710 - [PID=46067] ProcessThrottler::didConnectToProcess
default	09:45:30.962318+0800	hootowl	0x131074710 - [PID=46067] ProcessThrottler::setThrottleState: Updating process assertion type to 3 (foregroundActivities=2, backgroundActivities=5)
default	09:45:30.962331+0800	hootowl	AssertionCapability::AssertionCapability: taking assertion Foreground
default	09:45:30.962384+0800	hootowl	0x131074680 - [PID=46067] WebProcessProxy::didChangeThrottleState: type=2
default	09:45:30.962424+0800	hootowl	0x131074680 - [PID=46067] WebProcessProxy::didChangeThrottleState(Foreground) Taking foreground assertion for network process
default	09:45:30.962435+0800	hootowl	0x13113c300 - ProcessAssertion::acquireSync Trying to take RBS assertion 'WebProcess Foreground Assertion' for process with PID=46067
default	09:45:30.962452+0800	hootowl	0x131114190 - NetworkProcessProxy::sendXPCEndpointToProcess(0x131074680) state = 1 has connection = 1 XPC endpoint message = 0x14a32cc00
default	09:45:30.964682+0800	hootowl	0x13113c300 - ProcessAssertion() Successfully granted capability
default	09:45:30.966625+0800	hootowl	0x1310304b0 - [PID=46063, throttler=0x131074150] ProcessThrottler::Activity::Activity: Starting foreground activity / 'WebPageProxy::runJavaScriptInFrameInScriptWorld'
default	09:45:30.966636+0800	hootowl	WebContent[46063] 0x11e3c4008 - [webPageID=8] WebPage::runJavaScriptInFrameInScriptWorld: frameID=0
default	09:45:30.976886+0800	hootowl	{"msg":"CLLocationManager", "event":"activity", "_cmd":"startUpdatingLocation", "self":"0x1483580a0"}
default	09:45:30.977344+0800	hootowl	App is being debugged, do not track this hang
default	09:45:30.977449+0800	hootowl	Hang detected: 0.53s (debugger attached, not reporting)
default	09:45:30.978918+0800	hootowl	WebContent[46067] Installed launch log hook
default	09:45:30.978979+0800	hootowl	WebContent[46067] [0x1011370c0] invalidated after the last release of the connection object
default	09:45:30.978995+0800	hootowl	WebContent[46067] [0x1011373d0] invalidated because the client process (pid 46067) either cancelled the connection or exited
default	09:45:30.979078+0800	hootowl	[0x149595e00] activating connection: mach=false listener=false peer=false name=(anonymous)
default	09:45:30.979104+0800	hootowl	WebContent[46063] 0x11e3c4008 - [webPageID=8] WebPage::runJavaScriptInFrameInScriptWorld: Request to run JavaScript succeeded
default	09:45:30.980195+0800	hootowl	0x131030450 - [PID=46063, throttler=0x131074150] ProcessThrottler::Activity::invalidate: Ending foreground activity / 'WebPageProxy::runJavaScriptInFrameInScriptWorld'
default	09:45:30.980209+0800	hootowl	WebContent[46067] [0x101137ea0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	09:45:30.980220+0800	hootowl	0x1310301b0 - [PID=46067, throttler=0x131074710] ProcessThrottler::Activity::invalidate: Ending foreground activity / 'Process initialization'
default	09:45:30.980230+0800	hootowl	0x131114190 - NetworkProcessProxy::getNetworkProcessConnection: Taking a background assertion because web process pid 46067 (core identifier 5) is requesting a connection
default	09:45:30.980787+0800	hootowl	WebContent[46067] getNetworkProcessConnection: Request connection for core identifier 5
default	09:45:30.980806+0800	hootowl	WebContent[46067] Received Launch Services database
default	09:45:30.980834+0800	hootowl	WebContent[46068] Installed launch log hook
default	09:45:30.980885+0800	hootowl	WebContent[46068] [0x1012df0c0] invalidated after the last release of the connection object
default	09:45:30.980952+0800	hootowl	Task <184316FC-8AA6-4448-B994-329DB5E27CFF>.<4> resuming, timeouts(60.0, 180.0) qos(0x19) voucher((null)) activity(00000000-0000-0000-0000-000000000000)
default	09:45:30.980979+0800	hootowl	0x131074c40 - [PID=46068] WebProcessProxy::didFinishLaunching:
default	09:45:30.981045+0800	hootowl	0x131074cd0 - [PID=46068] ProcessThrottler::didConnectToProcess
default	09:45:30.981077+0800	hootowl	0x131074cd0 - [PID=46068] ProcessThrottler::setThrottleState: Updating process assertion type to 3 (foregroundActivities=2, backgroundActivities=3)
default	09:45:30.981127+0800	hootowl	AssertionCapability::AssertionCapability: taking assertion Foreground
default	09:45:30.981149+0800	hootowl	0x131074c40 - [PID=46068] WebProcessProxy::didChangeThrottleState: type=2
default	09:45:30.981156+0800	hootowl	0x131074c40 - [PID=46068] WebProcessProxy::didChangeThrottleState(Foreground) Taking foreground assertion for network process
default	09:45:30.981302+0800	hootowl	0x131114190 - NetworkProcessProxy::sendXPCEndpointToProcess(0x131074c40) state = 1 has connection = 1 XPC endpoint message = 0x14a32cc00
default	09:45:30.981368+0800	hootowl	0x13113c3c0 - ProcessAssertion::acquireSync Trying to take RBS assertion 'WebProcess Foreground Assertion' for process with PID=46068
default	09:45:30.981396+0800	hootowl	[ATTrackingManager] trackingAuthorizationStatus API call invoked.
default	09:45:30.981513+0800	hootowl	[ATTrackingManager] Performing TCC Access Preflight Request.
default	09:45:30.981545+0800	hootowl	[ATTrackingManager] Returning from trackingAuthorizationStatus - 0
default	09:45:30.981690+0800	hootowl	0x1310304b0 - [PID=46063, throttler=0x131074150] ProcessThrottler::Activity::invalidate: Ending foreground activity / 'WebPageProxy::runJavaScriptInFrameInScriptWorld'
default	09:45:30.981901+0800	hootowl	0x13113c3c0 - ProcessAssertion() Successfully granted capability
default	09:45:30.981925+0800	hootowl	[C3] event: client:connection_reused @6.338s
default	09:45:30.982033+0800	hootowl	Task <184316FC-8AA6-4448-B994-329DB5E27CFF>.<4> now using Connection 3
default	09:45:30.983114+0800	hootowl	0x14cb2e318 ID=8 Task <184316FC-8AA6-4448-B994-329DB5E27CFF>.<4> sent request, body N 0
default	09:45:30.985663+0800	hootowl	WebContent[46068] [0x1012df3d0] invalidated because the client process (pid 46068) either cancelled the connection or exited
default	09:45:30.985671+0800	hootowl	WebContent[46068] [0x1012e0da0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	09:45:30.985707+0800	hootowl	WebContent[46068] getNetworkProcessConnection: Request connection for core identifier 6
default	09:45:30.985719+0800	hootowl	0x131030510 - [PID=46068, throttler=0x131074cd0] ProcessThrottler::Activity::invalidate: Ending foreground activity / 'Process initialization'
default	09:45:30.985745+0800	hootowl	0x131114190 - NetworkProcessProxy::getNetworkProcessConnection: Taking a background assertion because web process pid 46068 (core identifier 6) is requesting a connection
default	09:45:30.985755+0800	hootowl	WebContent[46068] Received Launch Services database
default	09:45:30.986473+0800	hootowl	<Google> <Google:HTML> 8 required SKAdNetwork identifier(s) missing from Info.plist. Missing network(s): BidMachine, ironsource Ads, Persona.ly Ltd., Pubmatic, StackAdapt, Verve, Viant, Zemanta. See [Enable SKAdNetwork to track conversions] (https://goo.gle/enable-skadnetwork).
default	09:45:30.992662+0800	hootowl	0x1310301e0 - [PID=46063, throttler=0x131074150] ProcessThrottler::Activity::Activity: Starting foreground activity / 'WebPageProxy::runJavaScriptInFrameInScriptWorld'
default	09:45:30.992681+0800	hootowl	WebContent[46063] 0x11e3c4008 - [webPageID=8] WebPage::runJavaScriptInFrameInScriptWorld: frameID=0
default	09:45:30.992707+0800	hootowl	WebContent[46067] 0x10e06c100 - [sessionID=1] WebProcess::initializeLogForwarding: Debug logging enabled: 1
default	09:45:30.992722+0800	hootowl	WebContent[46067] WebProcess::platformInitializeWebProcess
default	09:45:30.992835+0800	hootowl	WebContent[46067] [0x101136ee0] Connection returned listener port: 0x1103
default	09:45:30.992851+0800	hootowl	WebContent[46067] [0x101139830] activating connection: mach=false listener=false peer=false name=(anonymous)
default	09:45:30.992866+0800	hootowl	WebContent[46067] [0x1055b8000] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0x101136ee0.peer[46067].0x1055b8000
default	09:45:30.993196+0800	hootowl	WebContent[46067] Application accessibility enabled: 1, (
	0   libAccessibility.dylib              0x00000001943ea920 _AXSApplicationAccessibilitySetEnabled + 84
	1   WebKit                              0x00000001ace77730 C39BD22C-3475-38AF-91BD-0B7574081011 + 12146480
	2   WebKit                              0x00000001ad0d054c C39BD22C-3475-38AF-91BD-0B7574081011 + 14607692
	3   WebKit                              0x00000001ac8f43f4 C39BD22C-3475-38AF-91BD-0B7574081011 + 6366196
	4   WebKit                              0x00000001ad58b714 C39BD22C-3475-38AF-91BD-0B7574081011 + 19568404
	5   WebKit                              0x00000001ad5b23a8 C39BD22C-3475-38AF-91BD-0B7574081011 + 19727272
	6   JavaScriptCore                      0x00000001a68da140 F7906028-1C6D-3B4C-BD93-78C196C83A83 + 692544
	7   JavaScriptCore                      0x00000001a68db6f8 F7906028-1C6D-3B4C-BD93-78C196C83A83 + 698104
	8   CoreFoundation                      0x0000000191073390 101EB2F1-1915-34A0-8BC9-631D03753B84 + 656272
	9   CoreFoundation                      0x000
default	09:45:30.993212+0800	hootowl	WebContent[46067] Stored App AX setting: 1
default	09:45:30.993220+0800	hootowl	WebContent[46067] AXS AccessibilityEnabled: (app ax: 1), ax settings: 1, cached: 1
default	09:45:30.993253+0800	hootowl	WebContent[46063] 0x11e3c4008 - [webPageID=8] WebPage::runJavaScriptInFrameInScriptWorld: Request to run JavaScript succeeded
default	09:45:30.995425+0800	hootowl	[0x148ebb700] Re-initialization successful; calling out to event handler with XPC_ERROR_CONNECTION_INTERRUPTED
default	09:45:31.010186+0800	hootowl	WebContent[46068] 0x10e06c100 - [sessionID=1] WebProcess::initializeLogForwarding: Debug logging enabled: 1
default	09:45:31.010195+0800	hootowl	WebContent[46068] WebProcess::platformInitializeWebProcess
default	09:45:31.013534+0800	hootowl	WebContent[46068] [0x1012deee0] Connection returned listener port: 0x1c03
default	09:45:31.013612+0800	hootowl	WebContent[46068] [0x1012e1b90] activating connection: mach=false listener=false peer=false name=(anonymous)
default	09:45:31.015227+0800	hootowl	WebContent[46068] [0x1051f8000] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0x1012deee0.peer[46068].0x1051f8000
default	09:45:31.015309+0800	hootowl	WebContent[46068] Application accessibility enabled: 1, (
	0   libAccessibility.dylib              0x00000001943ea920 _AXSApplicationAccessibilitySetEnabled + 84
	1   WebKit                              0x00000001ace77730 C39BD22C-3475-38AF-91BD-0B7574081011 + 12146480
	2   WebKit                              0x00000001ad0d054c C39BD22C-3475-38AF-91BD-0B7574081011 + 14607692
	3   WebKit                              0x00000001ac8f43f4 C39BD22C-3475-38AF-91BD-0B7574081011 + 6366196
	4   WebKit                              0x00000001ad58b714 C39BD22C-3475-38AF-91BD-0B7574081011 + 19568404
	5   WebKit                              0x00000001ad5b23a8 C39BD22C-3475-38AF-91BD-0B7574081011 + 19727272
	6   JavaScriptCore                      0x00000001a68da140 F7906028-1C6D-3B4C-BD93-78C196C83A83 + 692544
	7   JavaScriptCore                      0x00000001a68db6f8 F7906028-1C6D-3B4C-BD93-78C196C83A83 + 698104
	8   CoreFoundation                      0x0000000191073390 101EB2F1-1915-34A0-8BC9-631D03753B84 + 656272
	9   CoreFoundation                      0x000
default	09:45:31.015583+0800	hootowl	WebContent[46068] Stored App AX setting: 1
default	09:45:31.015825+0800	hootowl	WebContent[46068] AXS AccessibilityEnabled: (app ax: 1), ax settings: 1, cached: 1
default	09:45:31.018697+0800	hootowl	0x1310301e0 - [PID=46063, throttler=0x131074150] ProcessThrottler::Activity::invalidate: Ending foreground activity / 'WebPageProxy::runJavaScriptInFrameInScriptWorld'
default	09:45:31.019201+0800	hootowl	0x148ec3118 - [pageProxyID=20, webPageID=21, PID=46067] WebPageProxy::decidePolicyForNavigationAction: frameID=4294967298, isMainFrame=1, navigationID=25
default	09:45:31.019237+0800	hootowl	[0x149595e00] Re-initialization successful; calling out to event handler with XPC_ERROR_CONNECTION_INTERRUPTED
default	09:45:31.019252+0800	hootowl	0x1310b40c0 - SOAuthorizationCoordinator::tryAuthorize
default	09:45:31.019273+0800	hootowl	Fetching native takeover URLs
default	09:45:31.019486+0800	hootowl	URL shouldn't be processed
default	09:45:31.019515+0800	hootowl	SOAuthorizationCoordinator::tryAuthorize: The requested URL is not registered for AppSSO handling. No further action needed.
default	09:45:31.021303+0800	hootowl	0x148ec3118 - [pageProxyID=20, webPageID=21, PID=46067] WebPageProxy::decidePolicyForNavigationAction: listener called: frameID=4294967298, isMainFrame=1, navigationID=25, policyAction=Use, isAppBoundDomain=0, wasNavigationIntercepted=0
default	09:45:31.021327+0800	hootowl	0x148ec3118 - [pageProxyID=20, webPageID=21, PID=46067] WebPageProxy::receivedNavigationActionPolicyDecision: frameID=4294967298, isMainFrame=1, navigationID=25, policyAction=Use
default	09:45:31.021420+0800	hootowl	WebContent[46067]: [renderingBackend=11] Created rendering backend for pageProxyID=20, webPageID=21
default	09:45:31.021497+0800	hootowl	WebContent[46067] GPUProcessConnection::create - 0x10e1125a0
default	09:45:31.021605+0800	hootowl	0x1310e41e0 - GPUProcessProxy is taking a background assertion because a web process is requesting a connection
default	09:45:31.025844+0800	hootowl	beginSafeBrowsingCheck: no threat, completing navigationID=25
default	09:45:31.025907+0800	hootowl	0x148ec3118 - [pageProxyID=20, webPageID=21, PID=46067] WebPageProxy::decidePolicyForNavigationAction: keep using process 46067 for navigation, reason=Process has not yet committed any provisional loads
default	09:45:31.025935+0800	hootowl	0x131074680 - [PID=46067] WebProcessProxy::canTerminateAuxiliaryProcess: returns false (pageCount=1, remotePageCount=0, provisionalPageCount=0, suspendedPageCount=0, m_isInProcessCache=0, m_shutdownPreventingScopeCounter=0)
default	09:45:31.025959+0800	hootowl	0x1310e41e0 - GPUProcessProxy::didCreateContextForVisibilityPropagation: webPageProxyID: 20, pagePID: 21, contextID: 6
default	09:45:31.033818+0800	hootowl	WebContent[46067] 0x10e1125a0 - GPUProcessConnection::didInitialize
default	09:45:31.033965+0800	hootowl	WebContent[46067]: [webFrameID=4294967298, webPageID=21] WebFrameLoaderClient::dispatchDecidePolicyForNavigationAction: Got policyAction Use from async IPC
default	09:45:31.033998+0800	hootowl	WebContent[46067] 0x10e1d8180 - [pageID=21, frameID=4294967298] PolicyChecker::checkNavigationPolicy: continuing because this policyAction from dispatchDecidePolicyForNavigationAction is Use
default	09:45:31.034013+0800	hootowl	WebContent[46067]: [pageID=21 frameID=4294967298 isMainFrame=1] FrameLoader::stopAllLoaders: m_provisionalDocumentLoader=0, m_documentLoader=4598185984
default	09:45:31.034024+0800	hootowl	WebContent[46067]: [pageID=21, frameID=4294967298, isMainFrame=1] DocumentLoader::stopLoading
default	09:45:31.034034+0800	hootowl	WebContent[46067]: [pageID=21 frameID=4294967298 isMainFrame=1] FrameLoader::setProvisionalDocumentLoader: Setting provisional document loader to 4598206464 (was 0)
default	09:45:31.034044+0800	hootowl	WebContent[46067]: [pageID=21 frameID=4294967298 isMainFrame=1] FrameLoader::continueLoadAfterNavigationPolicy: Setting provisional document loader (m_provisionalDocumentLoader=4598206464)
default	09:45:31.034054+0800	hootowl	WebContent[46067]: [webPageID=21] WebPage::freezeLayerTree: Adding a reason to freeze layer tree (reason=1, new=1, old=0)
default	09:45:31.034064+0800	hootowl	WebContent[46067]: [pageID=21 frameID=4294967298 isMainFrame=1] FrameLoader::setPolicyDocumentLoader: Setting policy document loader to 0 (was 4598206464)
default	09:45:31.034071+0800	hootowl	WebContent[46067]: [pageID=21 frameID=4294967298 isMainFrame=1] FrameLoader::prepareForLoadStart: Starting frame load
default	09:45:31.034081+0800	hootowl	WebContent[46067]: ProgressTracker::progressStarted: frameID 4294967298, value 0.100000, tracked frames 1, originating frameID 4294967298, isMainLoad 1
default	09:45:31.034091+0800	hootowl	WebContent[46067]: [pageID=21, frameID=4294967298, isMainFrame=1] DocumentLoader::startLoadingMainResource: Starting load
default	09:45:31.034101+0800	hootowl	WebContent[46067]: [pageID=21, frameID=4294967298, resourceID=18] ResourceLoader::willSendRequestInternal: calling completion handler
default	09:45:31.034110+0800	hootowl	WebContent[46067]: [pageID=21, frameID=4294967298, resourceID=18 SubResourceLoader::willSendRequestInternal: resource load finished; calling completion handler
default	09:45:31.034132+0800	hootowl	WebContent[46067]: [webPageID=21, frameID=4294967298, resourceID=18] WebLoaderStrategy::scheduleLoad: URL will be scheduled with the NetworkProcess
default	09:45:31.034188+0800	hootowl	WebContent[46067]: [webPageID=21, frameID=4294967298, resourceID=18] WebLoaderStrategy::scheduleLoad: Resource is being scheduled with the NetworkProcess (priority=4, existingNetworkResourceLoadIdentifierToResume=0)
default	09:45:31.034234+0800	hootowl	WebContent[46067]: [webPageID=21, frameID=4294967298, resourceID=18] WebResourceLoader::WebResourceLoader
default	09:45:31.034398+0800	hootowl	0x148ec3118 - [pageProxyID=20, webPageID=21, PID=46067] WebPageProxy::didStartProvisionalLoadForFrame: frameID=4294967298, isMainFrame=1
default	09:45:31.034404+0800	hootowl	0x131074680 - [PID=46067] WebProcessProxy::didStartProvisionalLoadForMainFrame:
default	09:45:31.034521+0800	hootowl	RemoteLayerTreeDrawingAreaProxy(23)::hideContentUntilPendingUpdate completed
default	09:45:31.034528+0800	hootowl	RemoteLayerTreeDrawingAreaProxy(23) Unhiding layer tree
default	09:45:31.034553+0800	hootowl	WebContent[46068]: [renderingBackend=10] Created rendering backend for pageProxyID=375, webPageID=376
default	09:45:31.034563+0800	hootowl	WebContent[46068] GPUProcessConnection::create - 0x10e08e920
default	09:45:31.034569+0800	hootowl	0x1310e41e0 - GPUProcessProxy is taking a background assertion because a web process is requesting a connection
default	09:45:31.041543+0800	hootowl	0x1310e41e0 - GPUProcessProxy::didCreateContextForVisibilityPropagation: webPageProxyID: 375, pagePID: 376, contextID: 9
default	09:45:31.066927+0800	hootowl	WebContent[46068] 0x10e08e920 - GPUProcessConnection::didInitialize
default	09:45:31.087207+0800	hootowl	RemoteLayerTreeDrawingAreaProxy(378)::hideContentUntilPendingUpdate completed
default	09:45:31.087286+0800	hootowl	RemoteLayerTreeDrawingAreaProxy(378) Unhiding layer tree
error	09:45:31.090110+0800	hootowl	WebContent[46067] Could not register system wide server: -25204
error	09:45:31.090122+0800	hootowl	WebContent[46067] _AXAddToElementCache was called even though the element was in the cache: <WKAccessibilityWebPageObject: 0x101139b70>
error	09:45:31.094352+0800	hootowl	WebContent[46068] Could not register system wide server: -25204
error	09:45:31.094800+0800	hootowl	WebContent[46068] _AXAddToElementCache was called even though the element was in the cache: <WKAccessibilityWebPageObject: 0x1012e10e0>
default	09:45:31.117283+0800	hootowl	Received state update for 46045 (app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>, unknown-NotVisible
default	09:45:31.144498+0800	hootowl	TX focusApplication (peekAppEvent) stealKB:Y scene:com.sharkda.hootowl-83FF55F6-7B28-4BFD-8825-33CB43E5D162
default	09:45:31.144551+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:31.144562+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	09:45:31.144591+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1481fc400>; contextId: 0xF4D9041F
default	09:45:31.147324+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:31.148405+0800	hootowl	WebContent[46067]: [webPageID=21, frameID=4294967298, resourceID=18] WebResourceLoader::didReceiveResponse: (httpStatusCode=200)
default	09:45:31.150226+0800	hootowl	WebContent[46067]: [webPageID=21, frameID=4294967298, resourceID=18] WebResourceLoader::didReceiveData: Started receiving data
default	09:45:31.150285+0800	hootowl	WebContent[46067]: [pageID=21 frameID=4294967298 isMainFrame=1] FrameLoader::setDocumentLoader: Setting document loader to 4598206464 (was 4598185984)
default	09:45:31.150290+0800	hootowl	WebContent[46067]: [pageID=21, frameID=4294967298, isMainFrame=1] DocumentLoader::detachFromFrame
default	09:45:31.150293+0800	hootowl	WebContent[46067]: [pageID=21, frameID=4294967298, isMainFrame=1] DocumentLoader::stopLoading
default	09:45:31.150296+0800	hootowl	WebContent[46067]: [pageID=21 frameID=4294967298 isMainFrame=1] FrameLoader::transitionToCommitted: Clearing provisional document loader (m_provisionalDocumentLoader=4598206464)
default	09:45:31.150301+0800	hootowl	WebContent[46067]: [pageID=21 frameID=4294967298 isMainFrame=1] FrameLoader::setProvisionalDocumentLoader: Setting provisional document loader to 0 (was 4598206464)
default	09:45:31.150763+0800	hootowl	0x148ec3118 - [pageProxyID=20, webPageID=21, PID=46067] WebPageProxy::didNavigateWithNavigationDataShared:
default	09:45:31.150908+0800	hootowl	WebContent[46067]: [webPageID=21] WebPage::unfreezeLayerTree: Removing a reason to freeze layer tree (reason=128, new=1, old=1)
default	09:45:31.150942+0800	hootowl	WebContent[46067]: [webPageID=21] WebPage::unfreezeLayerTree: Removing a reason to freeze layer tree (reason=128, new=1, old=1)
default	09:45:31.151006+0800	hootowl	WebContent[46067]: [webPageID=21] WebPage::unfreezeLayerTree: Removing a reason to freeze layer tree (reason=32, new=1, old=1)
default	09:45:31.151242+0800	hootowl	0x148ec3118 - [pageProxyID=20, webPageID=21, PID=46067] WebPageProxy::didCommitLoadForFrame: frameID=4294967298, isMainFrame=1
default	09:45:31.151554+0800	hootowl	0x148ec3118 - [pageProxyID=20, webPageID=21, PID=46067] WebPageProxy::setMediaCapability: creating (envID=46045-2-com.sharkda.hootowl) for URL 'https://googleads.g.doubleclick.net/mads/static/sdk/native/sdk-core-v40.html?sdk=afma-sdk-i-v13.3.0&stfv=prod'
default	09:45:31.156784+0800	hootowl	WebContent[46063]: [webPageID=8, frameID=4294967297, resourceID=33] WebResourceLoader::didReceiveResponse: (httpStatusCode=200)
default	09:45:31.156809+0800	hootowl	WebContent[46063]: [webPageID=8, frameID=4294967297, resourceID=33] WebResourceLoader::didReceiveData: Started receiving data
default	09:45:31.156826+0800	hootowl	WebContent[46063]: [webPageID=8, frameID=4294967297, resourceID=33] WebResourceLoader::didFinishResourceLoad: (length=251)
default	09:45:31.157241+0800	hootowl	WebContent[46063]: [pageID=8, frameID=4294967297, resourceID=33 SubResourceLoader::didFinishLoading
default	09:45:31.161330+0800	hootowl	WebContent[46063]: [pageID=8, frameID=4294967297, resourceID=97] ResourceLoader::willSendRequestInternal: calling completion handler
default	09:45:31.161382+0800	hootowl	WebContent[46063]: [pageID=8, frameID=4294967297, resourceID=97 SubResourceLoader::willSendRequestInternal: resource load finished; calling completion handler
default	09:45:31.161391+0800	hootowl	WebContent[46063]: [webPageID=8, frameID=4294967297, resourceID=97] WebLoaderStrategy::scheduleLoad: URL will be scheduled with the NetworkProcess
default	09:45:31.161426+0800	hootowl	WebContent[46063]: [webPageID=8, frameID=4294967297, resourceID=97] WebLoaderStrategy::scheduleLoad: Resource is being scheduled with the NetworkProcess (priority=2, existingNetworkResourceLoadIdentifierToResume=0)
default	09:45:31.161461+0800	hootowl	WebContent[46063]: [webPageID=8, frameID=4294967297, resourceID=97] WebResourceLoader::WebResourceLoader
default	09:45:31.260735+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:31.260761+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	09:45:31.260777+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1481fc400>; contextId: 0xF4D9041F
default	09:45:31.261218+0800	hootowl	<UIWindowScene: 0x148378200> (83FF55F6-7B28-4BFD-8825-33CB43E5D162) Scene updated orientation preferences: ( Pu Ll Lr ) -> ( Pu )
default	09:45:31.267993+0800	hootowl	MncplCyclopsScreen 78
🏠 body eval — items:6 firstObs:6s firstCar:0
default	09:45:31.282474+0800	hootowl	MncplCyclopsScreen 78
🏠 body eval — items:6 firstObs:6s firstCar:0
default	09:45:31.350723+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:31.350934+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 1
default	09:45:31.353140+0800	hootowl	0x14cb2e318 ID=8 Task <184316FC-8AA6-4448-B994-329DB5E27CFF>.<4> received response, status 200 content K
default	09:45:31.356343+0800	hootowl	WebContent[46067]: [webPageID=21, frameID=4294967298, resourceID=18] WebResourceLoader::didFinishResourceLoad: (length=733011)
default	09:45:31.356811+0800	hootowl	WebContent[46067]: [pageID=21, frameID=4294967298, resourceID=18 SubResourceLoader::didFinishLoading
default	09:45:31.362272+0800	hootowl	WebContent[46067]: [webPageID=21] WebPage::unfreezeLayerTree: Removing a reason to freeze layer tree (reason=1, new=0, old=1)
default	09:45:31.362297+0800	hootowl	WebContent[46067]: [pageID=21, frameID=4294967298, isMainFrame=1] LocalFrameView::fireLayoutRelatedMilestonesIfNeeded: Firing first visually non-empty layout milestone on the main frame
default	09:45:31.362356+0800	hootowl	WebContent[46067]: [webFrameID=4294967298, webPageID=21] WebLocalFrameLoaderClient::dispatchDidReachLayoutMilestone: dispatching DidReachLayoutMilestone (milestones=DidFirstVisuallyNonEmptyLayout)
default	09:45:31.362375+0800	hootowl	WebContent[46067]: [webFrameID=4294967298, webPageID=21] WebLocalFrameLoaderClient::dispatchDidReachLayoutMilestone: dispatching DidFirstVisuallyNonEmptyLayoutForFrame
default	09:45:31.362391+0800	hootowl	WebContent[46067]: [webFrameID=4294967298, webPageID=21] WebLocalFrameLoaderClient::completePageTransitionIfNeeded: dispatching didCompletePageTransition
default	09:45:31.362649+0800	hootowl	WebContent[46067]: [webFrameID=4294967298, webPageID=21] WebLocalFrameLoaderClient::dispatchDidReachLayoutMilestone: dispatching DidFirstLayoutForFrame
default	09:45:31.362675+0800	hootowl	WebContent[46067]: [webFrameID=4294967298, webPageID=21] WebLocalFrameLoaderClient::dispatchDidReachLayoutMilestone: dispatching DidReachLayoutMilestone (milestones=DidFirstLayout)
default	09:45:31.362693+0800	hootowl	WebContent[46067]: [pageID=21 frameID=4294967298 isMainFrame=1] FrameLoader::setState: main frame load completed
default	09:45:31.364129+0800	hootowl	WebContent[46067]: Memory usage info dump at MainFrameLoadCompleted:
default	09:45:31.364393+0800	hootowl	WebContent[46067]:   page_count: 1
default	09:45:31.364409+0800	hootowl	WebContent[46067]:   backforward_cache_page_count: 0
default	09:45:31.364430+0800	hootowl	WebContent[46067]:   document_count: 1
default	09:45:31.364454+0800	hootowl	WebContent[46067]:   javascript_gc_heap_capacity_mb: 2
default	09:45:31.364483+0800	hootowl	WebContent[46067]:   javascript_gc_heap_extra_memory_size_mb: 0
default	09:45:31.364504+0800	hootowl	WebContent[46067]:   internal_mb: 21
default	09:45:31.364523+0800	hootowl	WebContent[46067]:   compressed_mb: 0
default	09:45:31.364552+0800	hootowl	WebContent[46067]:   phys_footprint_mb: 29
default	09:45:31.364571+0800	hootowl	WebContent[46067]:   resident_size_mb: 49
default	09:45:31.364639+0800	hootowl	WebContent[46067]:   virtual_size_mb: 420410
default	09:45:31.364826+0800	hootowl	0x148ec3118 - [pageProxyID=20, webPageID=21, PID=46067] WebPageProxy::didFinishDocumentLoadForFrame: frameID=4294967298, isMainFrame=1
default	09:45:31.364840+0800	hootowl	WebContent[46067]: ProgressTracker::progressCompleted: frameID 4294967298, value 0.483202, tracked frames 1, originating frameID 4294967298, isMainLoad 1
default	09:45:31.364850+0800	hootowl	WebContent[46067]: ProgressTracker::finalProgressComplete: value 0.483202, tracked frames 0, originating frameID 4294967298, isMainLoad 1, isMainLoadProgressing 0
default	09:45:31.364886+0800	hootowl	WebContent[46067]: [pageID=21 frameID=4294967298 isMainFrame=1] FrameLoader::checkLoadCompleteForThisFrame: Finished frame load
default	09:45:31.364909+0800	hootowl	WebContent[46067]: [webFrameID=4294967298, webPageID=21] WebLocalFrameLoaderClient::dispatchDidReachLayoutMilestone: dispatching DidReachLayoutMilestone (milestones=DidFirstMeaningfulPaint)
default	09:45:31.364918+0800	hootowl	0x148ec3118 - [pageProxyID=20, webPageID=21, PID=46067] WebPageProxy::didFinishLoadForFrame: frameID=4294967298, isMainFrame=1
default	09:45:31.364926+0800	hootowl	0x131050310 - NavigationState will release its process network assertion soon because the page load completed
default	09:45:31.364939+0800	hootowl	0x1310301e0 - [PID=46067, throttler=0x131074710] ProcessThrottler::Activity::Activity: Starting foreground activity / 'WebPageProxy::runJavaScriptInFrameInScriptWorld'
default	09:45:31.364953+0800	hootowl	[ATTrackingManager] trackingAuthorizationStatus API call invoked.
default	09:45:31.365430+0800	hootowl	[ATTrackingManager] Call to trackingAuthorizationStatus eligible for rate limiting. Returning 0
default	09:45:31.366008+0800	hootowl	0x1310303c0 - [PID=46067, throttler=0x131074710] ProcessThrottler::Activity::Activity: Starting foreground activity / 'WebPageProxy::runJavaScriptInFrameInScriptWorld'
default	09:45:31.366345+0800	hootowl	WebContent[46067] 0x101bb8008 - [webPageID=21] WebPage::runJavaScriptInFrameInScriptWorld: frameID=0
default	09:45:31.366353+0800	hootowl	WebContent[46067] 0x101bb8008 - [webPageID=21] WebPage::runJavaScriptInFrameInScriptWorld: Request to run JavaScript succeeded
default	09:45:31.366393+0800	hootowl	0x1310301e0 - [PID=46067, throttler=0x131074710] ProcessThrottler::Activity::invalidate: Ending foreground activity / 'WebPageProxy::runJavaScriptInFrameInScriptWorld'
default	09:45:31.366647+0800	hootowl	WebContent[46067] 0x101bb8008 - [webPageID=21] WebPage::runJavaScriptInFrameInScriptWorld: frameID=0
default	09:45:31.366662+0800	hootowl	WebContent[46067] 0x101bb8008 - [webPageID=21] WebPage::runJavaScriptInFrameInScriptWorld: Request to run JavaScript succeeded
default	09:45:31.366677+0800	hootowl	[0x14957d2c0] activating connection: mach=true listener=false peer=false name=com.apple.ScreenTimeAgent
default	09:45:31.366693+0800	hootowl	0x1310303c0 - [PID=46067, throttler=0x131074710] ProcessThrottler::Activity::invalidate: Ending foreground activity / 'WebPageProxy::runJavaScriptInFrameInScriptWorld'
default	09:45:31.366761+0800	hootowl	Screen Time has updated to use the system shield for any blocked URL.
error	09:45:31.367436+0800	hootowl	UIColor created with component values far outside the expected range. Set a breakpoint on UIColorBreakForOutOfRangeColorComponents to debug. This message will only be logged once.
default	09:45:31.367989+0800	hootowl	<Google> <Google:HTML> 8 required SKAdNetwork identifier(s) missing from Info.plist. Missing network(s): BidMachine, ironsource Ads, Persona.ly Ltd., Pubmatic, StackAdapt, Verve, Viant, Zemanta. See [Enable SKAdNetwork to track conversions] (https://goo.gle/enable-skadnetwork).
default	09:45:31.368577+0800	hootowl	Task <184316FC-8AA6-4448-B994-329DB5E27CFF>.<4> response ended
default	09:45:31.369635+0800	hootowl	[C3] event: client:connection_idle @6.729s
default	09:45:31.369709+0800	hootowl	Task <184316FC-8AA6-4448-B994-329DB5E27CFF>.<4> done using Connection 3
default	09:45:31.372927+0800	hootowl	Task <184316FC-8AA6-4448-B994-329DB5E27CFF>.<4> summary for task success {transaction_duration_ms=395, response_status=200, connection=3, reused=1, reused_after_ms=216, request_start_ms=1, request_duration_ms=1, response_start_ms=375, response_duration_ms=15, request_bytes=8738, request_throughput_kbps=53159, response_bytes=24746, response_throughput_kbps=12425, cache_hit=false}
default	09:45:31.373132+0800	hootowl	Task <184316FC-8AA6-4448-B994-329DB5E27CFF>.<4> finished successfully
default	09:45:31.373920+0800	hootowl	0x1310301b0 - [PID=46067, throttler=0x131074710] ProcessThrottler::Activity::Activity: Starting foreground activity / 'WebPageProxy::runJavaScriptInFrameInScriptWorld'
default	09:45:31.385715+0800	hootowl	Task <9ABDA649-77F1-4B70-9828-D27E5CA9CB20>.<8> response ended
default	09:45:31.385730+0800	hootowl	Task <9ABDA649-77F1-4B70-9828-D27E5CA9CB20>.<8> done using Connection 7
default	09:45:31.392599+0800	hootowl	[C7] event: client:connection_idle @5.793s
default	09:45:31.392633+0800	hootowl	nw_protocol_tcp_notify [C7.1.1.1:3] nw_protocol_notification_type_connection_idle is true
default	09:45:31.392642+0800	hootowl	nw_protocol_tcp_set_connection_idle [C7.1.1.1:3] os_nexus_flow_set_connection_idle returned 0
default	09:45:31.392823+0800	hootowl	Task <9ABDA649-77F1-4B70-9828-D27E5CA9CB20>.<8> summary for task success {transaction_duration_ms=1182, response_status=200, connection=7, reused=1, reused_after_ms=128, request_start_ms=128, request_duration_ms=2, response_start_ms=245, response_duration_ms=932, request_bytes=391, request_throughput_kbps=1445, response_bytes=381916, response_throughput_kbps=3276, cache_hit=false}
default	09:45:31.392919+0800	hootowl	[C7] event: client:connection_idle @5.796s
default	09:45:31.392955+0800	hootowl	nw_protocol_tcp_notify [C7.1.1.1:3] nw_protocol_notification_type_connection_idle is true
default	09:45:31.397501+0800	hootowl	nw_protocol_tcp_set_connection_idle [C7.1.1.1:3] os_nexus_flow_set_connection_idle returned 0
default	09:45:31.397682+0800	hootowl	Task <9ABDA649-77F1-4B70-9828-D27E5CA9CB20>.<8> finished successfully
default	09:45:31.418250+0800	hootowl	WebContent[46063]: [webPageID=8, frameID=4294967297, resourceID=97] WebResourceLoader::didReceiveResponse: (httpStatusCode=500)
default	09:45:31.418683+0800	hootowl	WebContent[46063]: [webPageID=8, frameID=4294967297, resourceID=97] WebResourceLoader::didFinishResourceLoad: (length=0)
default	09:45:31.418812+0800	hootowl	WebContent[46063]: [pageID=8, frameID=4294967297, resourceID=97 SubResourceLoader::didFinishLoading
default	09:45:31.418828+0800	hootowl	WebContent[46063] 0x11e3c4008 - [webPageID=8] WebPage::runJavaScriptInFrameInScriptWorld: Request to run JavaScript succeeded
default	09:45:31.426057+0800	hootowl	WebContent[46067] 0x101bb8008 - [webPageID=21] WebPage::runJavaScriptInFrameInScriptWorld: frameID=0
default	09:45:31.426469+0800	hootowl	0x148c16400 - WKApplicationStateTrackingView: View with page [0x148ec1518, pageProxyID=7] was removed from a window, _lastObservedStateWasBackground=0
default	09:45:31.426485+0800	hootowl	0x148d71000 (pageProxyID=7) -[WKWebView _endLiveResize]
default	09:45:31.426510+0800	hootowl	0x131030120 - [PID=46063, throttler=0x131074150] ProcessThrottler::Activity::invalidate: Ending foreground activity / 'WebPageProxy::runJavaScriptInFrameInScriptWorld'
default	09:45:31.426605+0800	hootowl	[0x149569e00] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	09:45:31.426616+0800	hootowl	0x148ec1518 - [pageProxyID=7, webPageID=8, PID=46063] WebPageProxy::close:
default	09:45:31.426624+0800	hootowl	PlaybackSessionManagerProxy::invalidate(2906663760)
default	09:45:31.426630+0800	hootowl	PlaybackSessionManagerProxy::invalidate(2906663760)
default	09:45:31.426701+0800	hootowl	PlaybackSessionManagerProxy::~VideoPresentationManagerProxy(2906663760)
default	09:45:31.426712+0800	hootowl	PlaybackSessionManagerProxy::invalidate(2906663760)
default	09:45:31.426719+0800	hootowl	PlaybackSessionManagerProxy::~PlaybackSessionManagerProxy(2906663760)
default	09:45:31.426734+0800	hootowl	0x148ec1518 - [pageProxyID=7, webPageID=8, PID=46063] WebPageProxy::deactivateMediaCapability: deactivating (envID=46045-1-com.sharkda.hootowl) for URL 'https://googleads.g.doubleclick.net/mads/static/sdk/native/sdk-core-v40.html?sdk=afma-sdk-i-v13.3.0&stfv=prod'
default	09:45:31.426744+0800	hootowl	0x148ec1518 - [pageProxyID=7, webPageID=8, PID=46063] WebPageProxy::setMediaCapability: clearing media capability
default	09:45:31.426769+0800	hootowl	0x1310740c0 - [PID=46063] WebProcessProxy::removeWebPage: webPage=0x148ec1518, pageProxyID=7, webPageID=8
default	09:45:31.426779+0800	hootowl	0x1310740c0 - [PID=46063] WebProcessProxy::canTerminateAuxiliaryProcess: returns false (pageCount=0, remotePageCount=0, provisionalPageCount=0, suspendedPageCount=0, m_isInProcessCache=0, m_shutdownPreventingScopeCounter=1)
default	09:45:31.426819+0800	hootowl	0x131030240 - [PID=46063, throttler=0x131074150] ProcessThrottler::Activity::invalidate: Ending foreground activity / 'View is visible'
default	09:45:31.426881+0800	hootowl	0x131074150 - [PID=46063] ProcessThrottler::setThrottleState: Updating process assertion type to 1 (foregroundActivities=0, backgroundActivities=1)
default	09:45:31.428788+0800	hootowl	AssertionCapability::AssertionCapability: taking assertion Background
default	09:45:31.428814+0800	hootowl	0x1310740c0 - [PID=46063] WebProcessProxy::didChangeThrottleState: type=1
default	09:45:31.428823+0800	hootowl	0x1310740c0 - [PID=46063] WebProcessProxy::didChangeThrottleState(Background) Taking background assertion for network process
default	09:45:31.428833+0800	hootowl	0x148ec1518 - [pageProxyID=7, webPageID=8, PID=46063] WebPageProxy::destructor:
default	09:45:31.428885+0800	hootowl	0x1310302d0 - [PID=46063, throttler=0x131074150] ProcessThrottler::Activity::invalidate: Ending background activity / 'Page Load'
default	09:45:31.428978+0800	hootowl	0x131074150 - [PID=46063] ProcessThrottler::sendPrepareToSuspendIPC: Sending PrepareToSuspend(1, isSuspensionImminent=0) IPC, remainingRunTime=0.000000s
default	09:45:31.428993+0800	hootowl	0x1310740c0 - [PID=46063] WebProcessProxy::sendPrepareToSuspend: isSuspensionImminent=0
default	09:45:31.428999+0800	hootowl	0x131068100 - ~ApplicationStateTracker
default	09:45:31.429006+0800	hootowl	0x131068100 - ApplicationStateTracker::setIsInBackground: 1
default	09:45:31.429018+0800	hootowl	0x13113c480 - ProcessAssertion::acquireSync Trying to take RBS assertion 'WebProcess Background Assertion' for process with PID=46063
default	09:45:31.429025+0800	hootowl	0x131074150 - [PID=46063] ProcessThrottler::updateThrottleStateIfNeeded: sending ProcessDidResume IPC because the WebProcess is still processing request to suspend=1 (probable wakeup reason: WebPage_Close)
default	09:45:31.429032+0800	hootowl	0x1310740c0 - [PID=46063] WebProcessProxy::sendProcessDidResume:
default	09:45:31.429044+0800	hootowl	0x1310740c0 - [PID=46063] WebProcessProxy::canTerminateAuxiliaryProcess: returns false (pageCount=0, remotePageCount=0, provisionalPageCount=0, suspendedPageCount=0, m_isInProcessCache=0, m_shutdownPreventingScopeCounter=1)
default	09:45:31.429547+0800	hootowl	WebContent[46067] 0x101bb8008 - [webPageID=21] WebPage::runJavaScriptInFrameInScriptWorld: Request to run JavaScript succeeded
default	09:45:31.430742+0800	hootowl	0x1310301b0 - [PID=46067, throttler=0x131074710] ProcessThrottler::Activity::invalidate: Ending foreground activity / 'WebPageProxy::runJavaScriptInFrameInScriptWorld'
default	09:45:31.436893+0800	hootowl	0x13113c480 - ProcessAssertion() Successfully granted capability
default	09:45:31.437578+0800	hootowl	WebContent[46063]: [sessionID=1] WebProcess::prepareToSuspend: isSuspensionImminent=0, remainingRunTime=0.011293s
default	09:45:31.437591+0800	hootowl	WebContent[46063] 0x11206c100 - [sessionID=1] WebProcess::releaseMemory: BEGIN
default	09:45:31.437603+0800	hootowl	0x148ec2318 - [pageProxyID=375, webPageID=376, PID=46068] WebPageProxy::loadData:
default	09:45:31.437623+0800	hootowl	0x148ec2318 - [pageProxyID=375, webPageID=376, PID=46068] WebPageProxy::loadDataWithNavigation
default	09:45:31.437815+0800	hootowl	0x131050460 - NavigationState is taking a process network assertion because a page load started
default	09:45:31.437895+0800	hootowl	Taking network activity on WebProcess with PID 46068
default	09:45:31.437997+0800	hootowl	0x131030210 - [PID=46068, throttler=0x131074cd0] ProcessThrottler::Activity::Activity: Starting background activity / 'Page Load'
default	09:45:31.441729+0800	hootowl	Task <77E2D366-C6BB-4243-8B20-397A36B5FC01>.<6> received response, status 304 content U
default	09:45:31.441756+0800	hootowl	Task <77E2D366-C6BB-4243-8B20-397A36B5FC01>.<6> done using Connection 11
default	09:45:31.441817+0800	hootowl	[C11] event: client:connection_idle @1.432s
default	09:45:31.441843+0800	hootowl	WebContent[46068] 0x101bb0008 - [webPageID=376] WebPage::loadData: navigationID=1697, shouldTreatAsContinuingLoad=0
default	09:45:31.441853+0800	hootowl	WebContent[46068]: [pageID=376 frameID=4294967299 isMainFrame=1] FrameLoader::load (FrameLoadRequest): frame load started
default	09:45:31.441859+0800	hootowl	WebContent[46068]: [pageID=376 frameID=4294967299 isMainFrame=1] FrameLoader::load (DocumentLoader): frame load started
default	09:45:31.441901+0800	hootowl	WebContent[46068]: [pageID=376 frameID=4294967299 isMainFrame=1] FrameLoader::loadWithDocumentLoader: frame load started
default	09:45:31.442023+0800	hootowl	WebContent[46068]: [pageID=376 frameID=4294967299 isMainFrame=1] FrameLoader::loadWithDocumentLoader: main frame load started
default	09:45:31.442034+0800	hootowl	WebContent[46068]: Memory usage info dump at MainFrameLoadStarted:
default	09:45:31.442042+0800	hootowl	WebContent[46068]:   page_count: 1
default	09:45:31.442049+0800	hootowl	WebContent[46068]:   backforward_cache_page_count: 0
default	09:45:31.442054+0800	hootowl	WebContent[46068]:   document_count: 1
default	09:45:31.442183+0800	hootowl	WebContent[46068]:   javascript_gc_heap_capacity_mb: 0
default	09:45:31.442193+0800	hootowl	WebContent[46068]:   javascript_gc_heap_extra_memory_size_mb: 0
default	09:45:31.442199+0800	hootowl	WebContent[46068]:   internal_mb: 10
default	09:45:31.442207+0800	hootowl	WebContent[46068]:   compressed_mb: 0
default	09:45:31.442213+0800	hootowl	WebContent[46068]:   phys_footprint_mb: 24
default	09:45:31.442223+0800	hootowl	WebContent[46068]:   resident_size_mb: 47
default	09:45:31.442229+0800	hootowl	WebContent[46068]:   virtual_size_mb: 420409
default	09:45:31.442235+0800	hootowl	WebContent[46068]: [pageID=376 frameID=4294967299 isMainFrame=1] FrameLoader::setPolicyDocumentLoader: Setting policy document loader to 4598304768 (was 0)
default	09:45:31.442243+0800	hootowl	WebContent[46068]: [pageID=376, frameID=4294967299, isMainFrame=1] DocumentLoader::attachToFrame
default	09:45:31.442260+0800	hootowl	WebContent[46068] networkd_settings_read_from_file_locked initialized networkd settings by reading plist directly
default	09:45:31.442265+0800	hootowl	WebContent[46068] networkd_settings_read_from_file_locked initialized networkd settings by reading plist directly
default	09:45:31.443166+0800	hootowl	nw_protocol_tcp_notify [C11.1.1.1:3] nw_protocol_notification_type_connection_idle is true
default	09:45:31.443793+0800	hootowl	nw_protocol_tcp_set_connection_idle [C11.1.1.1:3] os_nexus_flow_set_connection_idle returned 0
default	09:45:31.443823+0800	hootowl	0x148ec2318 - [pageProxyID=375, webPageID=376, PID=46068] WebPageProxy::decidePolicyForNavigationAction: frameID=4294967299, isMainFrame=1, navigationID=1697
default	09:45:31.443850+0800	hootowl	0x1310b40c0 - SOAuthorizationCoordinator::tryAuthorize
default	09:45:31.443867+0800	hootowl	Fetching native takeover URLs
default	09:45:31.443882+0800	hootowl	Task <77E2D366-C6BB-4243-8B20-397A36B5FC01>.<6> summary for task success {transaction_duration_ms=1435, response_status=304, connection=11, protocol="h2", domain_lookup_duration_ms=189, connect_duration_ms=552, secure_connection_duration_ms=372, private_relay=false, request_start_ms=806, request_duration_ms=0, response_start_ms=1433, response_duration_ms=2, request_bytes=196, request_throughput_kbps=41233, response_bytes=318, response_throughput_kbps=1242, cache_hit=true}
default	09:45:31.444231+0800	hootowl	Task <77E2D366-C6BB-4243-8B20-397A36B5FC01>.<6> finished successfully
default	09:45:31.446362+0800	hootowl	URL shouldn't be processed
default	09:45:31.446727+0800	hootowl	SOAuthorizationCoordinator::tryAuthorize: The requested URL is not registered for AppSSO handling. No further action needed.
default	09:45:31.446739+0800	hootowl	0x148ec2318 - [pageProxyID=375, webPageID=376, PID=46068] WebPageProxy::decidePolicyForNavigationAction: listener called: frameID=4294967299, isMainFrame=1, navigationID=1697, policyAction=Use, isAppBoundDomain=0, wasNavigationIntercepted=0
default	09:45:31.446753+0800	hootowl	0x148ec2318 - [pageProxyID=375, webPageID=376, PID=46068] WebPageProxy::receivedNavigationActionPolicyDecision: frameID=4294967299, isMainFrame=1, navigationID=1697, policyAction=Use
default	09:45:31.450411+0800	hootowl	beginSafeBrowsingCheck: no threat, completing navigationID=1697
default	09:45:31.450809+0800	hootowl	WebContent[46063] Memory pressure relief: Total: res = 56983552/24788992/-32194560, res+swap = 69420096/37225536/-32194560
default	09:45:31.450822+0800	hootowl	WebContent[46063] 0x11206c100 - [sessionID=1] WebProcess::releaseMemory: END
default	09:45:31.450984+0800	hootowl	WebContent[46063]: [sessionID=1] WebProcess::freezeAllLayerTrees: WebProcess is freezing all layer trees
default	09:45:31.450998+0800	hootowl	WebContent[46063]: [webPageID=8] WebPage::freezeLayerTree: Adding a reason to freeze layer tree (reason=4, new=4, old=0)
default	09:45:31.451008+0800	hootowl	WebContent[46063]: [sessionID=1] WebProcess::destroyRenderingResources: took 0.00ms
default	09:45:31.451014+0800	hootowl	WebContent[46063] 0x11206c100 - [sessionID=1] WebProcess::updateFreezerStatus: isFreezable=1, success
default	09:45:31.451021+0800	hootowl	WebContent[46063]: [sessionID=1] WebProcess::markAllLayersVolatile:
default	09:45:31.451205+0800	hootowl	WebContent[46063]: [webPageID=8] WebPage::markLayersVolatile
default	09:45:31.451261+0800	hootowl	0x148ec2318 - [pageProxyID=375, webPageID=376, PID=46068] WebPageProxy::decidePolicyForNavigationAction: keep using process 46068 for navigation, reason=Process has not yet committed any provisional loads
default	09:45:31.451272+0800	hootowl	0x131074c40 - [PID=46068] WebProcessProxy::canTerminateAuxiliaryProcess: returns false (pageCount=1, remotePageCount=0, provisionalPageCount=0, suspendedPageCount=0, m_isInProcessCache=0, m_shutdownPreventingScopeCounter=0)
default	09:45:31.451281+0800	hootowl	WebContent[46063] 0x11206c100 - [sessionID=1] WebProcess::processDidResume:
default	09:45:31.451288+0800	hootowl	WebContent[46063] 0x11206c100 - [sessionID=1] WebProcess::cancelMarkAllLayersVolatile:
default	09:45:31.451294+0800	hootowl	WebContent[46063] 0x11e3c4008 - [webPageID=8] WebPage::cancelMarkLayersVolatile:
error	09:45:31.451302+0800	hootowl	WebContent[46063] 0x11206c100 - [sessionID=1] WebProcess::markAllLayersVolatile: Failed to mark layers as volatile for webPageID=8
default	09:45:31.451308+0800	hootowl	WebContent[46063]: [sessionID=1] WebProcess::prepareToSuspend: Process is ready to suspend
default	09:45:31.451316+0800	hootowl	WebContent[46063] 0x11206c100 - [sessionID=1] WebProcess::unfreezeAllLayerTrees: WebProcess is unfreezing all layer trees
default	09:45:31.451323+0800	hootowl	WebContent[46063]: [webPageID=8] WebPage::unfreezeLayerTree: Removing a reason to freeze layer tree (reason=4, new=0, old=4)
default	09:45:31.451385+0800	hootowl	WebContent[46063]: [webPageID=8] WebPage::close
default	09:45:31.451461+0800	hootowl	WebContent[46063]: [pageID=8 frameID=4294967297 isMainFrame=1] FrameLoader::stopAllLoaders: m_provisionalDocumentLoader=0, m_documentLoader=4614852608
default	09:45:31.451471+0800	hootowl	WebContent[46063]: [pageID=8, frameID=4294967297, isMainFrame=1] DocumentLoader::stopLoading
default	09:45:31.451478+0800	hootowl	WebContent[46063]: [pageID=8 frameID=4294967297 isMainFrame=1] FrameLoader::setDocumentLoader: Setting document loader to 0 (was 4614852608)
default	09:45:31.451502+0800	hootowl	WebContent[46063]: [pageID=8, frameID=4294967297, isMainFrame=1] DocumentLoader::detachFromFrame
default	09:45:31.451514+0800	hootowl	WebContent[46063]: [pageID=8, frameID=4294967297, isMainFrame=1] DocumentLoader::stopLoading
default	09:45:31.451522+0800	hootowl	WebContent[46068]: [webFrameID=4294967299, webPageID=376] WebFrameLoaderClient::dispatchDecidePolicyForNavigationAction: Got policyAction Use from async IPC
default	09:45:31.451579+0800	hootowl	WebContent[46068] 0x10e05c240 - [pageID=376, frameID=4294967299] PolicyChecker::checkNavigationPolicy: continuing because this policyAction from dispatchDecidePolicyForNavigationAction is Use
default	09:45:31.451606+0800	hootowl	WebContent[46068]: [pageID=376 frameID=4294967299 isMainFrame=1] FrameLoader::stopAllLoaders: m_provisionalDocumentLoader=0, m_documentLoader=4598317056
default	09:45:31.451617+0800	hootowl	WebContent[46068]: [pageID=376, frameID=4294967299, isMainFrame=1] DocumentLoader::stopLoading
default	09:45:31.451630+0800	hootowl	WebContent[46068]: [pageID=376 frameID=4294967299 isMainFrame=1] FrameLoader::setProvisionalDocumentLoader: Setting provisional document loader to 4598304768 (was 0)
default	09:45:31.451637+0800	hootowl	WebContent[46068]: [pageID=376 frameID=4294967299 isMainFrame=1] FrameLoader::continueLoadAfterNavigationPolicy: Setting provisional document loader (m_provisionalDocumentLoader=4598304768)
default	09:45:31.451644+0800	hootowl	WebContent[46068]: [webPageID=376] WebPage::freezeLayerTree: Adding a reason to freeze layer tree (reason=1, new=1, old=0)
default	09:45:31.451652+0800	hootowl	WebContent[46068]: [pageID=376 frameID=4294967299 isMainFrame=1] FrameLoader::setPolicyDocumentLoader: Setting policy document loader to 0 (was 4598304768)
default	09:45:31.451674+0800	hootowl	WebContent[46068]: [pageID=376 frameID=4294967299 isMainFrame=1] FrameLoader::prepareForLoadStart: Starting frame load
default	09:45:31.451687+0800	hootowl	WebContent[46068]: ProgressTracker::progressStarted: frameID 4294967299, value 0.100000, tracked frames 1, originating frameID 4294967299, isMainLoad 1
default	09:45:31.451826+0800	hootowl	WebContent[46068]: [pageID=376, frameID=4294967299, isMainFrame=1] DocumentLoader::startLoadingMainResource: Starting load
default	09:45:31.451850+0800	hootowl	WebContent[46068] 0x112149000 - [pageID=376, frameID=4294967299, isMainFrame=1] DocumentLoader::startLoadingMainResource: Returning substitute data
default	09:45:31.451858+0800	hootowl	WebContent[46068] 0x112149000 - [pageID=376, frameID=4294967299, isMainFrame=1] DocumentLoader::startLoadingMainResource callback: Load canceled because of substitute data
default	09:45:31.451867+0800	hootowl	WebContent[46068]: [pageID=376 frameID=4294967299 isMainFrame=1] FrameLoader::setDocumentLoader: Setting document loader to 4598304768 (was 4598317056)
default	09:45:31.451873+0800	hootowl	WebContent[46068]: [pageID=376, frameID=4294967299, isMainFrame=1] DocumentLoader::detachFromFrame
default	09:45:31.451879+0800	hootowl	WebContent[46068]: [pageID=376, frameID=4294967299, isMainFrame=1] DocumentLoader::stopLoading
default	09:45:31.451885+0800	hootowl	WebContent[46068]: [pageID=376 frameID=4294967299 isMainFrame=1] FrameLoader::transitionToCommitted: Clearing provisional document loader (m_provisionalDocumentLoader=4598304768)
default	09:45:31.451893+0800	hootowl	WebContent[46068]: [pageID=376 frameID=4294967299 isMainFrame=1] FrameLoader::setProvisionalDocumentLoader: Setting provisional document loader to 0 (was 4598304768)
default	09:45:31.451900+0800	hootowl	WebContent[46068]: [webPageID=376] WebPage::unfreezeLayerTree: Removing a reason to freeze layer tree (reason=128, new=1, old=1)
default	09:45:31.451906+0800	hootowl	WebContent[46068]: [webPageID=376] WebPage::unfreezeLayerTree: Removing a reason to freeze layer tree (reason=128, new=1, old=1)
default	09:45:31.451958+0800	hootowl	WebContent[46068]: [webPageID=376] WebPage::unfreezeLayerTree: Removing a reason to freeze layer tree (reason=32, new=1, old=1)
default	09:45:31.452517+0800	hootowl	0x148ec2318 - [pageProxyID=375, webPageID=376, PID=46068] WebPageProxy::didStartProvisionalLoadForFrame: frameID=4294967299, isMainFrame=1
default	09:45:31.452533+0800	hootowl	0x131074c40 - [PID=46068] WebProcessProxy::didStartProvisionalLoadForMainFrame:
default	09:45:31.452893+0800	hootowl	0x148ec2318 - [pageProxyID=375, webPageID=376, PID=46068] WebPageProxy::didCommitLoadForFrame: frameID=4294967299, isMainFrame=1
default	09:45:31.454025+0800	hootowl	0x148ec2318 - [pageProxyID=375, webPageID=376, PID=46068] WebPageProxy::setMediaCapability: creating (envID=46045-3-com.sharkda.hootowl) for URL 'https://googleads.g.doubleclick.net/mads/gma?caps=interactiveVideo_inlineVideo_transparentBackground_sdkVideo_sfv_ct_aboi_gcache_nav_navc_aso_th_mraid1_mraid2_mraid3_sdkAdmobApiForAds_di_autoplay_dinm_dim_dinmo_gls_xSeconds_omidEnabled_mediation_av&eid=318502621%2C318500618%2C318526966%2C44766145&format=713x100_mb&js=afma-sdk-i-v13.3.0&preqs=7&seq_num=8#caps=interactiveVideo_inlineVideo_transparentBackground_sdkVideo_sfv_ct_aboi_gcache_nav_navc_aso_th_mraid1_mraid2_mraid3_sdkAdmobApiForAds_di_autoplay_dinm_dim_dinmo_gls_xSeconds_omidEnabled_mediation_av&eid=318502621%252C318500618%252C318526966%252C44766145&format=713x100_mb&js=afma-sdk-i-v13.3.0&preqs=7&seq_num=8'
default	09:45:31.455327+0800	hootowl	0x1310740c0 - [PID=46063] WebProcessProxy::canTerminateAuxiliaryProcess: returns false (pageCount=0, remotePageCount=0, provisionalPageCount=0, suspendedPageCount=0, m_isInProcessCache=0, m_shutdownPreventingScopeCounter=1)
default	09:45:31.455704+0800	hootowl	WebContent[46063] 0x11e3c4008 - [webPageID=8] WebPage::destructor:
default	09:45:31.456425+0800	hootowl	0x1310740c0 - [PID=46063] WebProcessProxy::canTerminateAuxiliaryProcess: returns true
default	09:45:31.456442+0800	hootowl	0x1310500e0 - [PID=46063] WebProcessCache::canCacheProcess: Not caching process because the cache has no capacity
default	09:45:31.456449+0800	hootowl	0x1310740c0 - [PID=46063] WebProcessProxy::shutDown:
default	09:45:31.456455+0800	hootowl	AssertionCapability::AssertionCapability: taking assertion Background
default	09:45:31.456461+0800	hootowl	0x1310740c0 - [PID=46063] WebProcessProxy::processWillShutDown:
default	09:45:31.456468+0800	hootowl	0x131074150 - [PID=46063] ProcessThrottler::didDisconnectFromProcess:
default	09:45:31.457325+0800	hootowl	0x13113c480 - ~ProcessAssertion: Releasing process assertion 'WebProcess Background Assertion' for process with PID=46063
default	09:45:31.457389+0800	hootowl	0x13113c540 - ProcessAssertion::acquireSync Trying to take RBS assertion 'XPCConnectionTerminationWatchdog' for process with PID=46063
default	09:45:31.458278+0800	hootowl	0x1310740c0 - [PID=46063] WebProcessProxy::destructor:
default	09:45:31.458300+0800	hootowl	WebBackForwardCache::clear
default	09:45:31.458321+0800	hootowl	0x131074150 - [PID=46063] ProcessThrottler::didDisconnectFromProcess:
default	09:45:31.458338+0800	hootowl	Assertion for extension process 'ExtensionProcess: bundleID: com.apple.WebKit.WebContent instance ID: Optional([_EXExtensionInstanceIdentifier: A86A11E2-3333-4DD5-9507-34F43D5DAD05]) pid: 46063' invalidated
default	09:45:31.464365+0800	hootowl	WebContent[46068]: [pageID=376, frameID=4294967299, resourceID=24] ResourceLoader::willSendRequestInternal: calling completion handler
default	09:45:31.464380+0800	hootowl	WebContent[46068]: [pageID=376, frameID=4294967299, resourceID=24 SubResourceLoader::willSendRequestInternal: resource load finished; calling completion handler
default	09:45:31.464714+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=24] WebLoaderStrategy::scheduleLoad: URL will be scheduled with the NetworkProcess
default	09:45:31.465975+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=24] WebLoaderStrategy::scheduleLoad: Resource is being scheduled with the NetworkProcess (priority=3, existingNetworkResourceLoadIdentifierToResume=0)
default	09:45:31.466717+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=24] WebResourceLoader::WebResourceLoader
default	09:45:31.466732+0800	hootowl	WebContent[46068]: [webPageID=376] WebPage::freezeLayerTree: Adding a reason to freeze layer tree (reason=128, new=129, old=1)
default	09:45:31.466768+0800	hootowl	WebContent[46068]: [pageID=376, frameID=4294967299, resourceID=25] ResourceLoader::willSendRequestInternal: calling completion handler
default	09:45:31.466855+0800	hootowl	WebContent[46068]: [pageID=376, frameID=4294967299, resourceID=25 SubResourceLoader::willSendRequestInternal: resource load finished; calling completion handler
default	09:45:31.466907+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=25] WebLoaderStrategy::scheduleLoad: URL will be scheduled with the NetworkProcess
default	09:45:31.466937+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=25] WebLoaderStrategy::scheduleLoad: Resource is being scheduled with the NetworkProcess (priority=1, existingNetworkResourceLoadIdentifierToResume=0)
default	09:45:31.466958+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=25] WebResourceLoader::WebResourceLoader
default	09:45:31.467000+0800	hootowl	WebContent[46068]: [pageID=376, frameID=4294967299, resourceID=26] ResourceLoader::willSendRequestInternal: calling completion handler
default	09:45:31.467024+0800	hootowl	WebContent[46068]: [pageID=376, frameID=4294967299, resourceID=26 SubResourceLoader::willSendRequestInternal: resource load finished; calling completion handler
default	09:45:31.467045+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=26] WebLoaderStrategy::scheduleLoad: URL will be scheduled with the NetworkProcess
default	09:45:31.467063+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=26] WebLoaderStrategy::scheduleLoad: Resource is being scheduled with the NetworkProcess (priority=3, existingNetworkResourceLoadIdentifierToResume=0)
default	09:45:31.467088+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=26] WebResourceLoader::WebResourceLoader
default	09:45:31.467097+0800	hootowl	WebContent[46068]: [pageID=376, frameID=4294967299, resourceID=27] ResourceLoader::willSendRequestInternal: calling completion handler
default	09:45:31.467113+0800	hootowl	WebContent[46068]: [pageID=376, frameID=4294967299, resourceID=27 SubResourceLoader::willSendRequestInternal: resource load finished; calling completion handler
default	09:45:31.467125+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=27] WebLoaderStrategy::scheduleLoad: URL will be scheduled with the NetworkProcess
default	09:45:31.467133+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=27] WebLoaderStrategy::scheduleLoad: Resource is being scheduled with the NetworkProcess (priority=2, existingNetworkResourceLoadIdentifierToResume=0)
default	09:45:31.467148+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=27] WebResourceLoader::WebResourceLoader
default	09:45:31.467164+0800	hootowl	WebContent[46068]: [pageID=376, frameID=4294967299, resourceID=28] ResourceLoader::willSendRequestInternal: calling completion handler
default	09:45:31.467171+0800	hootowl	WebContent[46068]: [pageID=376, frameID=4294967299, resourceID=28 SubResourceLoader::willSendRequestInternal: resource load finished; calling completion handler
default	09:45:31.467185+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=28] WebLoaderStrategy::scheduleLoad: URL will be scheduled with the NetworkProcess
default	09:45:31.467197+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=28] WebLoaderStrategy::scheduleLoad: Resource is being scheduled with the NetworkProcess (priority=3, existingNetworkResourceLoadIdentifierToResume=0)
default	09:45:31.467204+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=28] WebResourceLoader::WebResourceLoader
default	09:45:31.467271+0800	hootowl	WebContent[46068]: [pageID=376, frameID=4294967299, resourceID=29] ResourceLoader::willSendRequestInternal: calling completion handler
default	09:45:31.467283+0800	hootowl	WebContent[46068]: [pageID=376, frameID=4294967299, resourceID=29 SubResourceLoader::willSendRequestInternal: resource load finished; calling completion handler
default	09:45:31.467307+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=29] WebLoaderStrategy::scheduleLoad: URL will be scheduled with the NetworkProcess
default	09:45:31.467324+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=29] WebLoaderStrategy::scheduleLoad: Resource is being scheduled with the NetworkProcess (priority=3, existingNetworkResourceLoadIdentifierToResume=0)
default	09:45:31.467339+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=29] WebResourceLoader::WebResourceLoader
default	09:45:31.467351+0800	hootowl	WebContent[46068]: [pageID=376, frameID=4294967299, resourceID=30] ResourceLoader::willSendRequestInternal: calling completion handler
default	09:45:31.467359+0800	hootowl	WebContent[46068]: [pageID=376, frameID=4294967299, resourceID=30 SubResourceLoader::willSendRequestInternal: resource load finished; calling completion handler
default	09:45:31.467372+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=30] WebLoaderStrategy::scheduleLoad: URL will be scheduled with the NetworkProcess
default	09:45:31.467385+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=30] WebLoaderStrategy::scheduleLoad: Resource is being scheduled with the NetworkProcess (priority=2, existingNetworkResourceLoadIdentifierToResume=0)
default	09:45:31.471460+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=30] WebResourceLoader::WebResourceLoader
default	09:45:31.471472+0800	hootowl	WebContent[46068]: [pageID=376, frameID=4294967299, resourceID=31] ResourceLoader::willSendRequestInternal: calling completion handler
default	09:45:31.471481+0800	hootowl	WebContent[46068]: [pageID=376, frameID=4294967299, resourceID=31 SubResourceLoader::willSendRequestInternal: resource load finished; calling completion handler
default	09:45:31.471959+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=31] WebLoaderStrategy::scheduleLoad: URL will be scheduled with the NetworkProcess
default	09:45:31.472012+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=31] WebLoaderStrategy::scheduleLoad: Resource is being scheduled with the NetworkProcess (priority=3, existingNetworkResourceLoadIdentifierToResume=0)
default	09:45:31.472019+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=31] WebResourceLoader::WebResourceLoader
error	09:45:31.472086+0800	hootowl	Error acquiring assertion: <Error Domain=RBSServiceErrorDomain Code=1 "((target is not running or doesn't have entitlement com.apple.developer.web-browser-engine.rendering AND target is not running or doesn't have entitlement com.apple.developer.web-browser-engine.networking AND target is not running or doesn't have entitlement com.apple.developer.web-browser-engine.webcontent))" UserInfo={NSLocalizedFailureReason=((target is not running or doesn't have entitlement com.apple.developer.web-browser-engine.rendering AND target is not running or doesn't have entitlement com.apple.developer.web-browser-engine.networking AND target is not running or doesn't have entitlement com.apple.developer.web-browser-engine.webcontent))}>
default	09:45:31.472103+0800	hootowl	0x13113c540 - ProcessAssertion() Failed to grant capability Background
error	09:45:31.472111+0800	hootowl	0x13113c540 - ProcessAssertion::acquireSync Failed to acquire RBS assertion 'XPCConnectionTerminationWatchdog' for process with PID=46063, error: (null)
default	09:45:31.472250+0800	hootowl	0x131074150 - [PID=0] ProcessThrottler::invalidateAllActivities: BEGIN (foregroundActivityCount: 0, backgroundActivityCount: 0)
default	09:45:31.472322+0800	hootowl	0x131074150 - [PID=0] ProcessThrottler::invalidateAllActivities: END
default	09:45:31.472512+0800	hootowl	0x13113c0c0 - ~ProcessAssertion: Releasing process assertion 'WebProcess Foreground Assertion' for process with PID=46063
default	09:45:31.472528+0800	hootowl	[0x149614a00] invalidated after the last release of the connection object
default	09:45:31.474713+0800	hootowl	0x0 - ProcessAssertion: RBS Background assertion for process with PID=0 was invalidated
default	09:45:31.474735+0800	hootowl	0x13113c540 - ProcessAssertion::processAssertionWasInvalidated() PID=46063
default	09:45:31.475388+0800	hootowl	0x0 - ProcessAssertion: RBS Foreground assertion for process with PID=0 was invalidated
default	09:45:31.475461+0800	hootowl	0x148ec3118 - [pageProxyID=20, webPageID=21, PID=46067] WebPageProxy::didGeneratePageLoadTiming: url=https://googleads.g.doubleclick.net/mads/static/sdk/native/sdk-core-v40.html?sdk=afma-sdk-i-v13.3.0&stfv=prod firstVisualLayout=0.330 firstMeaningfulPaint=0.334 domContentLoaded=0.330 loadEvent=0.330 subresourcesFinished=0.330
default	09:45:31.477174+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=25] WebResourceLoader::didReceiveResponse: (httpStatusCode=200)
default	09:45:31.477190+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=25] WebResourceLoader::didReceiveResource
error	09:45:31.478902+0800	hootowl	WebContent[46068] xpc_user_sessions_get_foreground_uid() failed with error 1 - Operation not permitted
default	09:45:31.479228+0800	hootowl	WebContent[46068] [0x105320a00] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	09:45:31.479244+0800	hootowl	WebContent[46068] [0x105320a00] failed to do a bootstrap look-up: xpc_error=[1: Operation not permitted]
default	09:45:31.479348+0800	hootowl	WebContent[46068] [0x105320a00] invalidated after a failed init
default	09:45:31.480386+0800	hootowl	WebContent[46068]: [pageID=376, frameID=4294967299, resourceID=25 SubResourceLoader::didFinishLoading
default	09:45:31.480479+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=27] WebResourceLoader::didReceiveResponse: (httpStatusCode=200)
default	09:45:31.480494+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=27] WebResourceLoader::didReceiveData: Started receiving data
default	09:45:31.480503+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=27] WebResourceLoader::didFinishResourceLoad: (length=3047)
default	09:45:31.480510+0800	hootowl	WebContent[46068]: [pageID=376, frameID=4294967299, resourceID=27 SubResourceLoader::didFinishLoading
default	09:45:31.480518+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=28] WebResourceLoader::didReceiveResponse: (httpStatusCode=200)
default	09:45:31.480525+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=28] WebResourceLoader::didReceiveResource
default	09:45:31.480532+0800	hootowl	WebContent[46068]: [pageID=376, frameID=4294967299, resourceID=28 SubResourceLoader::didFinishLoading
default	09:45:31.480540+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=26] WebResourceLoader::didReceiveResponse: (httpStatusCode=200)
default	09:45:31.481101+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=26] WebResourceLoader::didReceiveResource
default	09:45:31.481110+0800	hootowl	WebContent[46068]: [pageID=376, frameID=4294967299, resourceID=26 SubResourceLoader::didFinishLoading
default	09:45:31.481113+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=30] WebResourceLoader::didReceiveResponse: (httpStatusCode=200)
default	09:45:31.481436+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=30] WebResourceLoader::didReceiveResource
default	09:45:31.481456+0800	hootowl	WebContent[46068]: [pageID=376, frameID=4294967299, resourceID=30 SubResourceLoader::didFinishLoading
default	09:45:31.488986+0800	hootowl	Firing exit handlers for 46063 with context <RBSProcessExitContext| voluntary>
default	09:45:31.489037+0800	hootowl	Calling process death completion block for handle [xpcservice<com.apple.WebKit.WebContent([app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>:46045])>{vt hash: 71395982}[uuid:A86A11E2-3333-4DD5-9507-34F43D5DAD05]{definition:com.apple.WebKit.WebContent[extension][client]}:46063]
error	09:45:31.492347+0800	hootowl	WebContent[46068] Service "com.apple.CARenderServer" failed bootstrap look up (1) - (os/kern) invalid address
default	09:45:31.493340+0800	hootowl	WebContent[46068] Evaluated capturing state as 0 on <UIScreen: 0x105320b40> for initial
error	09:45:31.493382+0800	hootowl	WebContent[46068] Failed to initialize application enviroment context
error	09:45:31.493417+0800	hootowl	WebContent[46068] Failed to load a device context.
error	09:45:31.493552+0800	hootowl	WebContent[46068] Failed to initialize application enviroment context
error	09:45:31.493562+0800	hootowl	WebContent[46068] Failed to load a device context.
default	09:45:31.493907+0800	hootowl	WebContent[46068] Read CategoryName: per-app = 1, category name = (null)
default	09:45:31.494190+0800	hootowl	WebContent[46068] Read CategoryName: per-app = 0, category name = UICTContentSizeCategoryXXXL
default	09:45:31.494292+0800	hootowl	WebContent[46067] Read Per-App on Init: Smart invert = (null)
default	09:45:31.500183+0800	hootowl	Mu1Base+Ext 690
WgsNoPre(dyanmic)mapped is 1417
error	09:45:31.502034+0800	hootowl	WebContent[46067] Service "com.apple.CARenderServer" failed bootstrap look up (1) - (os/kern) invalid address
default	09:45:31.502407+0800	hootowl	WebContent[46067] Evaluated capturing state as 0 on <UIScreen: 0x1056e03c0> for initial
error	09:45:31.502428+0800	hootowl	WebContent[46067] Failed to initialize application enviroment context
error	09:45:31.502440+0800	hootowl	WebContent[46067] Failed to load a device context.
error	09:45:31.502619+0800	hootowl	WebContent[46067] Failed to initialize application enviroment context
error	09:45:31.502634+0800	hootowl	WebContent[46067] Failed to load a device context.
default	09:45:31.502772+0800	hootowl	WebContent[46067] Read CategoryName: per-app = 1, category name = (null)
default	09:45:31.502823+0800	hootowl	WebContent[46067] Read CategoryName: per-app = 0, category name = UICTContentSizeCategoryXXXL
default	09:45:31.507131+0800	hootowl	WebContent[46068] Read Per-App on Init: Smart invert = (null)
default	09:45:31.508430+0800	hootowl	WebContent[46068] XPC connection invalidated (daemon unloaded/disabled)
default	09:45:31.524568+0800	hootowl	    AVAudioSession_iOS.mm:996   Activated session 0x77c67d3
default	09:45:31.568401+0800	hootowl	Received state update for 46045 (app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>, unknown-NotVisible
fault	09:45:31.607933+0800	hootowl	Publishing changes from background threads is not allowed; make sure to publish values from the main thread (via operators like receive(on:)) on model updates.
default	09:45:31.607944+0800	hootowl	Municipal+Cyclops 93
🎨 model refreshed — obs:6s car:0 thread:BG 🆔 8064324136773232350
default	09:45:31.633245+0800	hootowl	    AVAudioSession_iOS.mm:996   Activated session 0x77c67d3
error	09:45:31.689258+0800	hootowl	181	search(mapMode:loc0:max:radius:)	⚠️ quadTree findNearest returned 0 results for center:lat:25.001,lng:121.565 — location may be outside tree bounds or tree is sparse
default	09:45:31.704298+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=31] WebResourceLoader::didReceiveResponse: (httpStatusCode=200)
default	09:45:31.704431+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=31] WebResourceLoader::didReceiveData: Started receiving data
default	09:45:31.704463+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=31] WebResourceLoader::didFinishResourceLoad: (length=43381)
default	09:45:31.705039+0800	hootowl	WebContent[46068]: [pageID=376, frameID=4294967299, resourceID=31 SubResourceLoader::didFinishLoading
default	09:45:31.705132+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=24] WebResourceLoader::didReceiveResponse: (httpStatusCode=200)
default	09:45:31.705342+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=24] WebResourceLoader::didReceiveData: Started receiving data
default	09:45:31.705416+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=24] WebResourceLoader::didFinishResourceLoad: (length=49735)
default	09:45:31.705485+0800	hootowl	WebContent[46068]: [pageID=376, frameID=4294967299, resourceID=24 SubResourceLoader::didFinishLoading
default	09:45:31.705552+0800	hootowl	WebContent[46068]: [webPageID=376] WebPage::unfreezeLayerTree: Removing a reason to freeze layer tree (reason=128, new=1, old=129)
default	09:45:31.713470+0800	hootowl	WebContent[46068]: [pageID=376 frameID=25769803777 isMainFrame=0] FrameLoader::setPolicyDocumentLoader: Setting policy document loader to 4598366208 (was 0)
default	09:45:31.713541+0800	hootowl	WebContent[46068]: [pageID=376, frameID=25769803777, isMainFrame=0] DocumentLoader::attachToFrame
default	09:45:31.713553+0800	hootowl	WebContent[46068]: [pageID=376 frameID=25769803777 isMainFrame=0] FrameLoader::setProvisionalDocumentLoader: Setting provisional document loader to 4598366208 (was 0)
default	09:45:31.713567+0800	hootowl	WebContent[46068]: [pageID=376 frameID=25769803777 isMainFrame=0] FrameLoader::setDocumentLoader: Setting document loader to 4598366208 (was 0)
default	09:45:31.713577+0800	hootowl	WebContent[46068]: [pageID=376 frameID=25769803777 isMainFrame=0] FrameLoader::transitionToCommitted: Clearing provisional document loader (m_provisionalDocumentLoader=4598366208)
default	09:45:31.713584+0800	hootowl	WebContent[46068]: [pageID=376 frameID=25769803777 isMainFrame=0] FrameLoader::setProvisionalDocumentLoader: Setting provisional document loader to 0 (was 4598366208)
default	09:45:31.713634+0800	hootowl	WebContent[46068]: [pageID=376, frameID=25769803777, isMainFrame=0] DocumentLoader::startLoadingMainResource: Returning empty document
default	09:45:31.713669+0800	hootowl	WebContent[46068]: [pageID=376 frameID=25769803777 isMainFrame=0] FrameLoader::setPolicyDocumentLoader: Setting policy document loader to 0 (was 4598366208)
default	09:45:31.713705+0800	hootowl	WebContent[46068]: [pageID=376 frameID=4294967299 isMainFrame=1] FrameLoader::loadURLIntoChildFrame: frame load started
default	09:45:31.713857+0800	hootowl	WebContent[46068]: [pageID=376 frameID=25769803777 isMainFrame=0] FrameLoader::loadURL: frame load started
default	09:45:31.713902+0800	hootowl	WebContent[46068]: [pageID=376 frameID=25769803777 isMainFrame=0] FrameLoader::loadWithNavigationAction: frame load started
default	09:45:31.713926+0800	hootowl	WebContent[46068]: [pageID=376 frameID=25769803777 isMainFrame=0] FrameLoader::loadWithDocumentLoader: frame load started
default	09:45:31.713936+0800	hootowl	WebContent[46068]: [pageID=376 frameID=25769803777 isMainFrame=0] FrameLoader::setPolicyDocumentLoader: Setting policy document loader to 4598374400 (was 0)
default	09:45:31.713962+0800	hootowl	WebContent[46068]: [pageID=376, frameID=25769803777, isMainFrame=0] DocumentLoader::attachToFrame
default	09:45:31.714083+0800	hootowl	WebContent[46068]: [pageID=376, frameID=25769803777] PolicyChecker::checkNavigationPolicy: continuing because this is an initial empty document
default	09:45:31.714118+0800	hootowl	WebContent[46068]: [pageID=376 frameID=25769803777 isMainFrame=0] FrameLoader::stopAllLoaders: m_provisionalDocumentLoader=0, m_documentLoader=4598366208
default	09:45:31.714159+0800	hootowl	WebContent[46068]: [pageID=376, frameID=25769803777, isMainFrame=0] DocumentLoader::stopLoading
default	09:45:31.714329+0800	hootowl	WebContent[46068]: [pageID=376 frameID=25769803777 isMainFrame=0] FrameLoader::setProvisionalDocumentLoader: Setting provisional document loader to 4598374400 (was 0)
default	09:45:31.714344+0800	hootowl	WebContent[46068]: [pageID=376 frameID=25769803777 isMainFrame=0] FrameLoader::continueLoadAfterNavigationPolicy: Setting provisional document loader (m_provisionalDocumentLoader=4598374400)
default	09:45:31.714384+0800	hootowl	WebContent[46068]: [pageID=376 frameID=25769803777 isMainFrame=0] FrameLoader::setPolicyDocumentLoader: Setting policy document loader to 0 (was 4598374400)
default	09:45:31.714392+0800	hootowl	WebContent[46068]: [pageID=376 frameID=25769803777 isMainFrame=0] FrameLoader::prepareForLoadStart: Starting frame load
default	09:45:31.714401+0800	hootowl	WebContent[46068]: ProgressTracker::progressStarted: frameID 25769803777, value 0.453968, tracked frames 2, originating frameID 4294967299, isMainLoad 1
default	09:45:31.714409+0800	hootowl	WebContent[46068]: [pageID=376 frameID=25769803777 isMainFrame=0] FrameLoader::setDocumentLoader: Setting document loader to 4598374400 (was 4598366208)
default	09:45:31.714415+0800	hootowl	WebContent[46068]: [pageID=376, frameID=25769803777, isMainFrame=0] DocumentLoader::detachFromFrame
default	09:45:31.714421+0800	hootowl	WebContent[46068]: [pageID=376, frameID=25769803777, isMainFrame=0] DocumentLoader::stopLoading
default	09:45:31.714624+0800	hootowl	WebContent[46068]: [pageID=376 frameID=25769803777 isMainFrame=0] FrameLoader::transitionToCommitted: Clearing provisional document loader (m_provisionalDocumentLoader=4598374400)
default	09:45:31.714682+0800	hootowl	WebContent[46068]: [pageID=376 frameID=25769803777 isMainFrame=0] FrameLoader::setProvisionalDocumentLoader: Setting provisional document loader to 0 (was 4598374400)
default	09:45:31.717227+0800	hootowl	Received state update for 46045 (app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>, unknown-NotVisible
default	09:45:31.719785+0800	hootowl	WebContent[46068]: [webPageID=376] WebPage::unfreezeLayerTree: Removing a reason to freeze layer tree (reason=1, new=0, old=1)
default	09:45:31.719923+0800	hootowl	WebContent[46068]: [pageID=376, frameID=4294967299, isMainFrame=1] LocalFrameView::fireLayoutRelatedMilestonesIfNeeded: Firing first visually non-empty layout milestone on the main frame
default	09:45:31.720036+0800	hootowl	WebContent[46068]: [webFrameID=4294967299, webPageID=376] WebLocalFrameLoaderClient::dispatchDidReachLayoutMilestone: dispatching DidReachLayoutMilestone (milestones=DidFirstVisuallyNonEmptyLayout)
default	09:45:31.720415+0800	hootowl	WebContent[46068]: [webFrameID=4294967299, webPageID=376] WebLocalFrameLoaderClient::dispatchDidReachLayoutMilestone: dispatching DidFirstVisuallyNonEmptyLayoutForFrame
default	09:45:31.720427+0800	hootowl	WebContent[46068]: [webFrameID=4294967299, webPageID=376] WebLocalFrameLoaderClient::completePageTransitionIfNeeded: dispatching didCompletePageTransition
default	09:45:31.720436+0800	hootowl	WebContent[46068]: ProgressTracker::progressCompleted: frameID 25769803777, value 0.453968, tracked frames 2, originating frameID 4294967299, isMainLoad 1
default	09:45:31.720453+0800	hootowl	WebContent[46068]: [pageID=376 frameID=25769803777 isMainFrame=0] FrameLoader::checkLoadCompleteForThisFrame: Finished frame load
default	09:45:31.720459+0800	hootowl	WebContent[46068]: [pageID=376, frameID=25769803777, isMainFrame=0] DocumentLoader::startLoadingMainResource: Returning empty document
default	09:45:31.720566+0800	hootowl	WebContent[46068]: [pageID=376 frameID=25769803778 isMainFrame=0] FrameLoader::setPolicyDocumentLoader: Setting policy document loader to 4598386688 (was 0)
default	09:45:31.720577+0800	hootowl	WebContent[46068]: [pageID=376, frameID=25769803778, isMainFrame=0] DocumentLoader::attachToFrame
default	09:45:31.720585+0800	hootowl	WebContent[46068]: [pageID=376 frameID=25769803778 isMainFrame=0] FrameLoader::setProvisionalDocumentLoader: Setting provisional document loader to 4598386688 (was 0)
default	09:45:31.720592+0800	hootowl	WebContent[46068]: [pageID=376 frameID=25769803778 isMainFrame=0] FrameLoader::setDocumentLoader: Setting document loader to 4598386688 (was 0)
default	09:45:31.720607+0800	hootowl	WebContent[46068]: [pageID=376 frameID=25769803778 isMainFrame=0] FrameLoader::transitionToCommitted: Clearing provisional document loader (m_provisionalDocumentLoader=4598386688)
default	09:45:31.720693+0800	hootowl	WebContent[46068]: [pageID=376 frameID=25769803778 isMainFrame=0] FrameLoader::setProvisionalDocumentLoader: Setting provisional document loader to 0 (was 4598386688)
default	09:45:31.720824+0800	hootowl	WebContent[46068]: [pageID=376, frameID=25769803778, isMainFrame=0] DocumentLoader::startLoadingMainResource: Returning empty document
default	09:45:31.720885+0800	hootowl	WebContent[46068]: [pageID=376 frameID=25769803778 isMainFrame=0] FrameLoader::setPolicyDocumentLoader: Setting policy document loader to 0 (was 4598386688)
default	09:45:31.721155+0800	hootowl	WebContent[46068]: [pageID=376 frameID=4294967299 isMainFrame=1] FrameLoader::loadURLIntoChildFrame: frame load started
default	09:45:31.721170+0800	hootowl	WebContent[46068]: [pageID=376 frameID=25769803778 isMainFrame=0] FrameLoader::loadURL: frame load started
default	09:45:31.721178+0800	hootowl	WebContent[46068]: [pageID=376 frameID=25769803778 isMainFrame=0] FrameLoader::loadWithNavigationAction: frame load started
default	09:45:31.721249+0800	hootowl	WebContent[46068]: [pageID=376 frameID=25769803778 isMainFrame=0] FrameLoader::loadWithDocumentLoader: frame load started
default	09:45:31.721261+0800	hootowl	WebContent[46068]: [pageID=376 frameID=25769803778 isMainFrame=0] FrameLoader::setPolicyDocumentLoader: Setting policy document loader to 4598394880 (was 0)
default	09:45:31.721268+0800	hootowl	WebContent[46068]: [pageID=376, frameID=25769803778, isMainFrame=0] DocumentLoader::attachToFrame
default	09:45:31.721275+0800	hootowl	WebContent[46068]: [pageID=376, frameID=25769803778] PolicyChecker::checkNavigationPolicy: continuing because this is an initial empty document
default	09:45:31.721282+0800	hootowl	WebContent[46068]: [pageID=376 frameID=25769803778 isMainFrame=0] FrameLoader::stopAllLoaders: m_provisionalDocumentLoader=0, m_documentLoader=4598386688
default	09:45:31.721288+0800	hootowl	WebContent[46068]: [pageID=376, frameID=25769803778, isMainFrame=0] DocumentLoader::stopLoading
default	09:45:31.721296+0800	hootowl	WebContent[46068]: [pageID=376 frameID=25769803778 isMainFrame=0] FrameLoader::setProvisionalDocumentLoader: Setting provisional document loader to 4598394880 (was 0)
default	09:45:31.721302+0800	hootowl	WebContent[46068]: [pageID=376 frameID=25769803778 isMainFrame=0] FrameLoader::continueLoadAfterNavigationPolicy: Setting provisional document loader (m_provisionalDocumentLoader=4598394880)
default	09:45:31.721309+0800	hootowl	WebContent[46068]: [pageID=376 frameID=25769803778 isMainFrame=0] FrameLoader::setPolicyDocumentLoader: Setting policy document loader to 0 (was 4598394880)
default	09:45:31.721316+0800	hootowl	WebContent[46068]: [pageID=376 frameID=25769803778 isMainFrame=0] FrameLoader::prepareForLoadStart: Starting frame load
default	09:45:31.721323+0800	hootowl	WebContent[46068]: ProgressTracker::progressStarted: frameID 25769803778, value 0.453968, tracked frames 2, originating frameID 4294967299, isMainLoad 1
default	09:45:31.721330+0800	hootowl	WebContent[46068]: [pageID=376 frameID=25769803778 isMainFrame=0] FrameLoader::setDocumentLoader: Setting document loader to 4598394880 (was 4598386688)
default	09:45:31.721340+0800	hootowl	WebContent[46068]: [pageID=376, frameID=25769803778, isMainFrame=0] DocumentLoader::detachFromFrame
default	09:45:31.721348+0800	hootowl	WebContent[46068]: [pageID=376, frameID=25769803778, isMainFrame=0] DocumentLoader::stopLoading
default	09:45:31.721354+0800	hootowl	WebContent[46068]: [pageID=376 frameID=25769803778 isMainFrame=0] FrameLoader::transitionToCommitted: Clearing provisional document loader (m_provisionalDocumentLoader=4598394880)
default	09:45:31.721359+0800	hootowl	WebContent[46068]: [pageID=376 frameID=25769803778 isMainFrame=0] FrameLoader::setProvisionalDocumentLoader: Setting provisional document loader to 0 (was 4598394880)
default	09:45:31.722059+0800	hootowl	WebContent[46068]: ProgressTracker::progressCompleted: frameID 25769803778, value 0.453968, tracked frames 2, originating frameID 4294967299, isMainLoad 1
default	09:45:31.722084+0800	hootowl	WebContent[46068]: [pageID=376 frameID=25769803778 isMainFrame=0] FrameLoader::checkLoadCompleteForThisFrame: Finished frame load
default	09:45:31.722322+0800	hootowl	WebContent[46068]: [pageID=376, frameID=25769803778, isMainFrame=0] DocumentLoader::startLoadingMainResource: Returning empty document
default	09:45:31.728755+0800	hootowl	WebContent[46068]: [webFrameID=4294967299, webPageID=376] WebLocalFrameLoaderClient::dispatchDidReachLayoutMilestone: dispatching DidFirstLayoutForFrame
default	09:45:31.728774+0800	hootowl	WebContent[46068]: [webFrameID=4294967299, webPageID=376] WebLocalFrameLoaderClient::dispatchDidReachLayoutMilestone: dispatching DidReachLayoutMilestone (milestones=DidFirstLayout)
default	09:45:31.730854+0800	hootowl	WebContent[46068]: [webFrameID=4294967299, webPageID=376] WebLocalFrameLoaderClient::dispatchDidReachLayoutMilestone: dispatching DidReachLayoutMilestone (milestones=DidFirstMeaningfulPaint)
default	09:45:31.734153+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=29] WebResourceLoader::didReceiveResponse: (httpStatusCode=200)
default	09:45:31.734217+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=29] WebResourceLoader::didReceiveData: Started receiving data
default	09:45:31.734232+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=29] WebResourceLoader::didFinishResourceLoad: (length=272410)
default	09:45:31.734244+0800	hootowl	WebContent[46068]: [pageID=376, frameID=4294967299, resourceID=29 SubResourceLoader::didFinishLoading
default	09:45:31.750124+0800	hootowl	WebContent[46068]: [pageID=376, frameID=4294967299, resourceID=55] ResourceLoader::willSendRequestInternal: calling completion handler
default	09:45:31.750137+0800	hootowl	WebContent[46068]: [pageID=376, frameID=4294967299, resourceID=55 SubResourceLoader::willSendRequestInternal: resource load finished; calling completion handler
default	09:45:31.750479+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=55] WebLoaderStrategy::scheduleLoad: URL will be scheduled with the NetworkProcess
default	09:45:31.750500+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=55] WebLoaderStrategy::scheduleLoad: Resource is being scheduled with the NetworkProcess (priority=2, existingNetworkResourceLoadIdentifierToResume=0)
default	09:45:31.750509+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=55] WebResourceLoader::WebResourceLoader
default	09:45:31.751482+0800	hootowl	WebContent[46068] XPC message reply connection invalidated (client likely exiting): Connection invalid
default	09:45:31.751498+0800	hootowl	WebContent[46068] XPC message reply connection invalidated (client likely exiting): Connection invalid
default	09:45:31.755985+0800	hootowl	MncplCyclopsScreen 166
🦵 uiKick received — syncing items
default	09:45:31.758390+0800	hootowl	0x148ec2318 - [pageProxyID=375, webPageID=376, PID=46068] WebPageProxy::decidePolicyForNavigationAction: frameID=25769803777, isMainFrame=0, navigationID=0
default	09:45:31.758567+0800	hootowl	0x1310b40c0 - SOAuthorizationCoordinator::tryAuthorize
default	09:45:31.758972+0800	hootowl	Fetching native takeover URLs
default	09:45:31.759041+0800	hootowl	0x148ec2318 - [pageProxyID=375, webPageID=376, PID=46068] WebPageProxy::didStartProvisionalLoadForFrame: frameID=25769803777, isMainFrame=0
default	09:45:31.759054+0800	hootowl	0x148ec2318 - [pageProxyID=375, webPageID=376, PID=46068] WebPageProxy::didCommitLoadForFrame: frameID=25769803777, isMainFrame=0
default	09:45:31.759078+0800	hootowl	0x148ec2318 - [pageProxyID=375, webPageID=376, PID=46068] WebPageProxy::didFinishDocumentLoadForFrame: frameID=25769803777, isMainFrame=0
default	09:45:31.759098+0800	hootowl	0x148ec2318 - [pageProxyID=375, webPageID=376, PID=46068] WebPageProxy::didFinishLoadForFrame: frameID=25769803777, isMainFrame=0
default	09:45:31.759121+0800	hootowl	0x148ec2318 - [pageProxyID=375, webPageID=376, PID=46068] WebPageProxy::decidePolicyForNavigationAction: frameID=25769803778, isMainFrame=0, navigationID=0
default	09:45:31.759601+0800	hootowl	0x1310b40c0 - SOAuthorizationCoordinator::tryAuthorize
default	09:45:31.759634+0800	hootowl	Fetching native takeover URLs
default	09:45:31.759654+0800	hootowl	0x148ec2318 - [pageProxyID=375, webPageID=376, PID=46068] WebPageProxy::didStartProvisionalLoadForFrame: frameID=25769803778, isMainFrame=0
default	09:45:31.759663+0800	hootowl	0x148ec2318 - [pageProxyID=375, webPageID=376, PID=46068] WebPageProxy::didCommitLoadForFrame: frameID=25769803778, isMainFrame=0
default	09:45:31.759670+0800	hootowl	0x148ec2318 - [pageProxyID=375, webPageID=376, PID=46068] WebPageProxy::didFinishDocumentLoadForFrame: frameID=25769803778, isMainFrame=0
default	09:45:31.760569+0800	hootowl	0x148ec2318 - [pageProxyID=375, webPageID=376, PID=46068] WebPageProxy::didFinishLoadForFrame: frameID=25769803778, isMainFrame=0
default	09:45:31.760591+0800	hootowl	[0x1496c6440] activating connection: mach=true listener=false peer=false name=com.apple.ScreenTimeAgent
default	09:45:31.760627+0800	hootowl	URL shouldn't be processed
default	09:45:31.760643+0800	hootowl	beginSafeBrowsingCheck: no threat, completing navigationID=1699
default	09:45:31.760664+0800	hootowl	beginSafeBrowsingCheck: no threat, completing navigationID=1701
default	09:45:31.761010+0800	hootowl	URL shouldn't be processed
default	09:45:31.765388+0800	hootowl	MncplCyclopsScreen 78
🏠 body eval — items:6 firstObs:6s firstCar:0
default	09:45:31.773745+0800	hootowl	WebContent[46068]: [pageID=376, frameID=4294967299, resourceID=61] ResourceLoader::willSendRequestInternal: calling completion handler
default	09:45:31.773819+0800	hootowl	WebContent[46068]: [pageID=376, frameID=4294967299, resourceID=61 SubResourceLoader::willSendRequestInternal: resource load finished; calling completion handler
default	09:45:31.773838+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=61] WebLoaderStrategy::scheduleLoad: URL will be loaded as data
default	09:45:31.773847+0800	hootowl	WebContent[46068]: [webPageID=0, frameID=0, resourceID=0] WebResourceLoader::WebResourceLoader
default	09:45:31.778526+0800	hootowl	WebContent[46068]: [pageID=376, frameID=4294967299, resourceID=62] ResourceLoader::willSendRequestInternal: calling completion handler
default	09:45:31.778691+0800	hootowl	WebContent[46068]: [pageID=376, frameID=4294967299, resourceID=62 SubResourceLoader::willSendRequestInternal: resource load finished; calling completion handler
default	09:45:31.778701+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=62] WebLoaderStrategy::scheduleLoad: URL will be scheduled with the NetworkProcess
default	09:45:31.778714+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=62] WebLoaderStrategy::scheduleLoad: Resource is being scheduled with the NetworkProcess (priority=2, existingNetworkResourceLoadIdentifierToResume=0)
default	09:45:31.778728+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=62] WebResourceLoader::WebResourceLoader
default	09:45:31.780195+0800	hootowl	SOAuthorizationCoordinator::tryAuthorize: The requested URL is not registered for AppSSO handling. No further action needed.
default	09:45:31.780216+0800	hootowl	0x148ec2318 - [pageProxyID=375, webPageID=376, PID=46068] WebPageProxy::decidePolicyForNavigationAction: listener called: frameID=25769803777, isMainFrame=0, navigationID=1699, policyAction=Use, isAppBoundDomain=0, wasNavigationIntercepted=0
default	09:45:31.780395+0800	hootowl	0x148ec2318 - [pageProxyID=375, webPageID=376, PID=46068] WebPageProxy::receivedNavigationActionPolicyDecision: frameID=25769803777, isMainFrame=0, navigationID=1699, policyAction=Use
default	09:45:31.780425+0800	hootowl	Screen Time has updated to use the system shield for any blocked URL.
default	09:45:31.780523+0800	hootowl	SOAuthorizationCoordinator::tryAuthorize: The requested URL is not registered for AppSSO handling. No further action needed.
default	09:45:31.780553+0800	hootowl	0x148ec2318 - [pageProxyID=375, webPageID=376, PID=46068] WebPageProxy::decidePolicyForNavigationAction: listener called: frameID=25769803778, isMainFrame=0, navigationID=1701, policyAction=Use, isAppBoundDomain=0, wasNavigationIntercepted=0
default	09:45:31.780599+0800	hootowl	0x148ec2318 - [pageProxyID=375, webPageID=376, PID=46068] WebPageProxy::receivedNavigationActionPolicyDecision: frameID=25769803778, isMainFrame=0, navigationID=1701, policyAction=Use
default	09:45:31.782577+0800	hootowl	WebContent[46068]: [webFrameID=25769803777, webPageID=376] WebFrameLoaderClient::dispatchDecidePolicyForNavigationAction: Got policyAction Use from async IPC
default	09:45:31.782586+0800	hootowl	WebContent[46068]: [webFrameID=25769803778, webPageID=376] WebFrameLoaderClient::dispatchDecidePolicyForNavigationAction: Got policyAction Use from async IPC
default	09:45:31.787292+0800	hootowl	WebContent[46068]: [pageID=376, frameID=4294967299, resourceID=61 SubResourceLoader::didFinishLoading
default	09:45:31.788281+0800	hootowl	0x148ec2318 - [pageProxyID=375, webPageID=376, PID=46068] WebPageProxy::didFinishDocumentLoadForFrame: frameID=4294967299, isMainFrame=1
default	09:45:31.790617+0800	hootowl	WebContent[46068]: [pageID=376 frameID=4294967299 isMainFrame=1] FrameLoader::setState: main frame load completed
default	09:45:31.790955+0800	hootowl	WebContent[46068]: Memory usage info dump at MainFrameLoadCompleted:
default	09:45:31.790976+0800	hootowl	WebContent[46068]:   page_count: 1
default	09:45:31.790992+0800	hootowl	WebContent[46068]:   backforward_cache_page_count: 0
default	09:45:31.791018+0800	hootowl	WebContent[46068]:   document_count: 3
default	09:45:31.791292+0800	hootowl	WebContent[46068]:   javascript_gc_heap_capacity_mb: 10
default	09:45:31.791326+0800	hootowl	WebContent[46068]:   javascript_gc_heap_extra_memory_size_mb: 2
default	09:45:31.791336+0800	hootowl	WebContent[46068]:   internal_mb: 41
default	09:45:31.791344+0800	hootowl	WebContent[46068]:   compressed_mb: 0
default	09:45:31.791464+0800	hootowl	WebContent[46068]:   phys_footprint_mb: 61
default	09:45:31.791484+0800	hootowl	WebContent[46068]:   resident_size_mb: 91
default	09:45:31.791493+0800	hootowl	WebContent[46068]:   virtual_size_mb: 420606
default	09:45:31.791559+0800	hootowl	WebContent[46068]: ProgressTracker::progressCompleted: frameID 4294967299, value 0.667370, tracked frames 1, originating frameID 4294967299, isMainLoad 1
default	09:45:31.791589+0800	hootowl	WebContent[46068]: ProgressTracker::finalProgressComplete: value 0.667370, tracked frames 0, originating frameID 4294967299, isMainLoad 1, isMainLoadProgressing 0
default	09:45:31.791646+0800	hootowl	WebContent[46068]: [pageID=376 frameID=4294967299 isMainFrame=1] FrameLoader::checkLoadCompleteForThisFrame: Finished frame load
default	09:45:31.791680+0800	hootowl	0x148ec2318 - [pageProxyID=375, webPageID=376, PID=46068] WebPageProxy::didFinishLoadForFrame: frameID=4294967299, isMainFrame=1
default	09:45:31.791687+0800	hootowl	0x131050460 - NavigationState will release its process network assertion soon because the page load completed
default	09:45:31.791693+0800	hootowl	0x131030120 - [PID=46068, throttler=0x131074cd0] ProcessThrottler::Activity::Activity: Starting foreground activity / 'WebPageProxy::runJavaScriptInFrameInScriptWorld'
default	09:45:31.791701+0800	hootowl	0x1310301e0 - [PID=46068, throttler=0x131074cd0] ProcessThrottler::Activity::Activity: Starting foreground activity / 'WebPageProxy::runJavaScriptInFrameInScriptWorld'
default	09:45:31.791707+0800	hootowl	0x1310302a0 - [PID=46068, throttler=0x131074cd0] ProcessThrottler::Activity::Activity: Starting foreground activity / 'WebPageProxy::runJavaScriptInFrameInScriptWorld'
default	09:45:31.791718+0800	hootowl	WebContent[46068] 0x101bb0008 - [webPageID=376] WebPage::runJavaScriptInFrameInScriptWorld: frameID=0
default	09:45:31.791723+0800	hootowl	Will add backgroundTask with taskName: com.google.backgroundPing, expirationHandler: <__NSMallocBlock__: 0x14a3e0d50>
default	09:45:31.791729+0800	hootowl	Creating new assertion because there is no existing background assertion.
default	09:45:31.791776+0800	hootowl	Creating new background assertion
default	09:45:31.791785+0800	hootowl	Created new background assertion <BKSProcessAssertion: 0x14d2205f0>
default	09:45:31.792643+0800	hootowl	Incrementing reference count for background assertion <BKSProcessAssertion: 0x14d2205f0>
default	09:45:31.793313+0800	hootowl	Created background task <_UIBackgroundTaskInfo: 0x148e25680>: taskID = 2, taskName = com.google.backgroundPing, creationTime = 771922 (elapsed = 0).
default	09:45:31.793325+0800	hootowl	Task <6CFF7C9A-048E-4F63-BCCC-5D1446230E4B>.<1> resuming, timeouts(60.0, 604800.0) qos(0x19) voucher((null)) activity(00000000-0000-0000-0000-000000000000)
default	09:45:31.793451+0800	hootowl	WebContent[46068] 0x101bb0008 - [webPageID=376] WebPage::runJavaScriptInFrameInScriptWorld: Request to run JavaScript succeeded
default	09:45:31.793457+0800	hootowl	WebContent[46068] 0x101bb0008 - [webPageID=376] WebPage::runJavaScriptInFrameInScriptWorld: frameID=0
default	09:45:31.793622+0800	hootowl	WebContent[46068] 0x101bb0008 - [webPageID=376] WebPage::runJavaScriptInFrameInScriptWorld: Request to run JavaScript succeeded
default	09:45:31.794241+0800	hootowl	WebContent[46068] 0x101bb0008 - [webPageID=376] WebPage::runJavaScriptInFrameInScriptWorld: frameID=0
default	09:45:31.794285+0800	hootowl	WebContent[46068] 0x101bb0008 - [webPageID=376] WebPage::runJavaScriptInFrameInScriptWorld: Request to run JavaScript succeeded
default	09:45:31.794687+0800	hootowl	0x131030120 - [PID=46068, throttler=0x131074cd0] ProcessThrottler::Activity::invalidate: Ending foreground activity / 'WebPageProxy::runJavaScriptInFrameInScriptWorld'
default	09:45:31.794714+0800	hootowl	0x1310301e0 - [PID=46068, throttler=0x131074cd0] ProcessThrottler::Activity::invalidate: Ending foreground activity / 'WebPageProxy::runJavaScriptInFrameInScriptWorld'
default	09:45:31.794804+0800	hootowl	0x1310302a0 - [PID=46068, throttler=0x131074cd0] ProcessThrottler::Activity::invalidate: Ending foreground activity / 'WebPageProxy::runJavaScriptInFrameInScriptWorld'
default	09:45:31.795219+0800	hootowl	Connection 0: creating secure tcp or quic connection
default	09:45:31.795825+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=55] WebResourceLoader::didReceiveResponse: (httpStatusCode=204)
default	09:45:31.796797+0800	hootowl	Connection 12: enabling TLS
default	09:45:31.796828+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=55] WebResourceLoader::didFinishResourceLoad: (length=0)
default	09:45:31.797009+0800	hootowl	WebContent[46068]: [pageID=376, frameID=4294967299, resourceID=55 SubResourceLoader::didFinishLoading
default	09:45:31.797329+0800	hootowl	Connection 12: starting, TC(0x0)
default	09:45:31.797394+0800	hootowl	[C12 DBCE5FB2-7175-4C2A-8E62-463ED0A11670 googleads.g.doubleclick.net:443 quic-connection, url: https://googleads.g.doubleclick.net/pagead/interaction/, definite, attribution: developer, context: com.apple.CFNetwork.NSURLSession.{EEABEA8B-723F-4B76-8EEA-091F44FC194B}{(null)}{Y}{2}{0x0} (private), proc: 1B526020-2DE0-3C65-9122-F1177549D69A, delegated upid: 0] start
default	09:45:31.797523+0800	hootowl	[C12 googleads.g.doubleclick.net:443 initial parent-flow ((null))] event: path:start @0.000s
default	09:45:31.797924+0800	hootowl	[C12 googleads.g.doubleclick.net:443 waiting parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.001s, uuid: 4F7DF4B0-1D6A-4298-83A6-080DCC81EB1C
default	09:45:31.797993+0800	hootowl	[C12 googleads.g.doubleclick.net:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_connect @0.001s
default	09:45:31.798008+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C12] reporting state preparing
default	09:45:31.798383+0800	hootowl	[C12 googleads.g.doubleclick.net:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_child @0.001s
default	09:45:31.798863+0800	hootowl	[C12.1 googleads.g.doubleclick.net:443 initial path ((null))] event: path:start @0.001s
default	09:45:31.799021+0800	hootowl	[C12.1 googleads.g.doubleclick.net:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.002s, uuid: 4F7DF4B0-1D6A-4298-83A6-080DCC81EB1C
error	09:45:31.799141+0800	hootowl	{"msg":"#Warning Error reading file", "file":"\/\/private\/var\/Managed Preferences\/mobile\/com.apple.CoreMotion.plist", "error":"Error Domain=NSCocoaErrorDomain Code=257 \"The file “com.apple.CoreMotion.plist” couldn’t be opened because you don’t have permission to view it.\" UserInfo={NSFilePath=\/\/private\/var\/Managed Preferences\/mobile\/com.apple.CoreMotion.plist, NSURL=file:\/\/\/\/private\/var\/Managed%20Preferences\/mobile\/com.apple.CoreMotion.plist, NSUnderlyingError=0x14ca70660 {Error Domain=NSPOSIXErrorDomain Code=1 \"Operation not permitted\"}}"}
default	09:45:31.799700+0800	hootowl	[C12.1 googleads.g.doubleclick.net:443 in_progress transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: transform:start @0.002s
default	09:45:31.799751+0800	hootowl	[C12.1.1 googleads.g.doubleclick.net:443 initial path ((null))] event: path:start @0.002s
default	09:45:31.800172+0800	hootowl	[C12.1.1 googleads.g.doubleclick.net:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.003s, uuid: 75CBD141-81A8-4F52-AAB4-C248E7AF0D33
default	09:45:31.800204+0800	hootowl	[C12.1.1 googleads.g.doubleclick.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:start_dns @0.003s
default	09:45:31.800863+0800	hootowl	Task <6CFF7C9A-048E-4F63-BCCC-5D1446230E4B>.<1> setting up Connection 12
default	09:45:31.805490+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=62] WebResourceLoader::didReceiveResponse: (httpStatusCode=204)
default	09:45:31.805569+0800	hootowl	WebContent[46068]: [webPageID=376, frameID=4294967299, resourceID=62] WebResourceLoader::didFinishResourceLoad: (length=0)
default	09:45:31.805617+0800	hootowl	WebContent[46068]: [pageID=376, frameID=4294967299, resourceID=62 SubResourceLoader::didFinishLoading
default	09:45:31.815052+0800	hootowl	nw_endpoint_resolver_update [C12.1.1 googleads.g.doubleclick.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Adding endpoint handler for 142.250.204.34:443, tracker
default	09:45:31.815746+0800	hootowl	[C12.1.1 googleads.g.doubleclick.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:receive_dns @0.018s
default	09:45:31.818049+0800	hootowl	0x1310500e0 - [PID=0] WebProcessCache::updateCapacity: Cache is disabled because process swap on navigation is disabled
default	09:45:31.818233+0800	hootowl	[C12.1.1.1 142.250.204.34:443 initial path ((null))] event: path:start @0.021s
default	09:45:31.818677+0800	hootowl	[C12.1.1.1 142.250.204.34:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.021s, uuid: 4225A72C-8C9D-4228-8798-760778B4703B
default	09:45:31.818802+0800	hootowl	[C12.1.1.1 142.250.204.34:443 in_progress channel-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_nexus @0.022s
default	09:45:31.819103+0800	hootowl	[C12.1.1.1 142.250.204.34:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:receive_nexus @0.022s
default	09:45:31.819561+0800	hootowl	quic_conn_initialize_inner [C12.1.1.1:2] [-c810b29be49a92b4] created QUIC connection (spin bit disabled)
default	09:45:31.819891+0800	hootowl	[C12.1.1.1 142.250.204.34:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_connect @0.023s
default	09:45:31.820727+0800	hootowl	quic_crypto_new_flow [C12.1.1.1:2] [-c810b29be49a92b4] TLS stream is: [C13]
default	09:45:31.820734+0800	hootowl	[C13 E6F4F2C1-455B-4552-A56D-81CFD8DC986D 142.250.204.34:443 quic-connection, url: https://googleads.g.doubleclick.net/pagead/interaction/, tls, definite, attribution: developer, context: com.apple.CFNetwork.NSURLSession.{EEABEA8B-723F-4B76-8EEA-091F44FC194B}{(null)}{Y}{2}{0x0} (private), proc: 1B526020-2DE0-3C65-9122-F1177549D69A, delegated upid: 0, known tracker] start
default	09:45:31.820808+0800	hootowl	[C13 142.250.204.34:443 initial socket-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:start @0.000s
default	09:45:31.820900+0800	hootowl	[C13 142.250.204.34:443 waiting socket-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.000s, uuid: 4225A72C-8C9D-4228-8798-760778B4703B
default	09:45:31.821007+0800	hootowl	[C13 142.250.204.34:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_connect @0.000s
default	09:45:31.821027+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C13] reporting state preparing
default	09:45:31.821134+0800	hootowl	nw_flow_connected [C13 142.250.204.34:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Transport protocol connected (quic-connection)
default	09:45:31.821182+0800	hootowl	[C13 142.250.204.34:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_transport @0.000s
default	09:45:31.822218+0800	hootowl	0x14b653488 - PageConfiguration::delaysWebProcessLaunchUntilFirstLoad() -> false because of associated processPool value
default	09:45:31.822247+0800	hootowl	0x14d204f08 - WebProcessPool::createWebPage: Not delaying WebProcess launch
default	09:45:31.822293+0800	hootowl	0x1310740c0 - [PID=0] WebProcessProxy::constructor:
default	09:45:31.822721+0800	hootowl	Successfully created a sandbox extension for '/private/var/containers/Bundle/Application/2290ADA6-FC62-4EB4-863B-0C67EBF31518/hootowl.app'
default	09:45:31.823602+0800	hootowl	Successfully created a sandbox extension for '/private/var/mobile/Containers/Data/Application/9C61D988-8BEB-42B6-A397-1E3A058F7BB4/Library/WebKit/WebsiteData/MediaKeys/v1'
default	09:45:31.823616+0800	hootowl	boringssl_session_apply_protocol_options_for_transport_block_invoke_2(2367) [C13:1][0x14d148560] TLS configured [server(0) min_version(0x0304) max_version(0x0304) name(googleads.g.doubleclick.net) tickets(false) false_start(false) enforce_ev(false) enforce_ats(false) ats_non_pfs_ciphersuite_allowed(false) cc_mode_enforced(false) ech(false) pqtls(true), pake(false) skip_ats_trust(false)]
default	09:45:31.823623+0800	hootowl	0x131030120 - [PID=0, throttler=0x131074150] ProcessThrottler::Activity::Activity: Starting foreground activity / 'Process initialization'
default	09:45:31.823659+0800	hootowl	boringssl_context_info_handler(2806) [C13:1][0x14d148560] Client handshake started
default	09:45:31.823673+0800	hootowl	0x14b50ce18 - [pageProxyID=1708, webPageID=1709, PID=0] WebPageProxy::constructor, site isolation enabled 0
default	09:45:31.823776+0800	hootowl	PlaybackSessionManagerProxy::PlaybackSessionManagerProxy(266764145)
default	09:45:31.823786+0800	hootowl	PlaybackSessionManagerProxy::VideoPresentationManagerProxy(266764145)
default	09:45:31.823795+0800	hootowl	0x1310740c0 - [PID=0] WebProcessProxy::addExistingWebPage: webPage=0x14b50ce18, pageProxyID=1708, webPageID=1709
default	09:45:31.823801+0800	hootowl	0x1310500e0 - [PID=0] WebProcessCache::updateCapacity: Cache is disabled by client
default	09:45:31.823883+0800	hootowl	Created visibility propagation interaction <_UIVisibilityPropagationInteraction: 0x1480629a0> for process with PID=46064
default	09:45:31.824057+0800	hootowl	boringssl_context_info_handler(2823) [C13:1][0x14d148560] Client handshake state: TLS client enter_early_data
default	09:45:31.824083+0800	hootowl	boringssl_context_info_handler(2823) [C13:1][0x14d148560] Client handshake state: TLS client read_server_hello
default	09:45:31.824163+0800	hootowl	Launching process with config: bundleID: com.apple.WebKit.WebContent instance ID: Optional([_EXExtensionInstanceIdentifier: 664DE272-5DCA-4C17-806E-27DDD3A03950])
default	09:45:31.895801+0800	hootowl	WebContent[46067] Loading PDFKit
default	09:45:31.903254+0800	hootowl	Starting death monitoring for handle [xpcservice<com.apple.WebKit.WebContent([app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>:46045])>{vt hash: 71395982}[uuid:664DE272-5DCA-4C17-806E-27DDD3A03950]{definition:com.apple.WebKit.WebContent[extension][client]}:46069]
default	09:45:31.906270+0800	hootowl	0x148ec2318 - [pageProxyID=375, webPageID=376, PID=46068] WebPageProxy::didGeneratePageLoadTiming: url=https://googleads.g.doubleclick.net/mads/gma?caps=interactiveVideo_inlineVideo_transparentBackground_sdkVideo_sfv_ct_aboi_gcache_nav_navc_aso_th_mraid1_mraid2_mraid3_sdkAdmobApiForAds_di_autoplay_dinm_dim_dinmo_gls_xSeconds_omidEnabled_mediation_av&eid=318502621%2C318500618%2C318526966%2C44766145&format=713x100_mb&js=afma-sdk-i-v13.3.0&preqs=7&seq_num=8#caps=interactiveVideo_inlineVideo_transparentBackground_sdkVideo_sfv_ct_aboi_gcache_nav_navc_aso_th_mraid1_mraid2_mraid3_sdkAdmobApiForAds_di_autoplay_dinm_dim_dinmo_gls_xSeconds_omidEnabled_mediation_av&eid=318502621%252C318500618%252C318526966%252C44766145&format=713x100_mb&js=afma-sdk-i-v13.3.0&preqs=7&seq_num=8 firstVisualLayout=0.269 firstMeaningfulPaint=0.308 domContentLoaded=0.330 loadEvent=0.339 subresourcesFinished=0.354
default	09:45:31.906919+0800	hootowl	Created new process ExtensionProcess: bundleID: com.apple.WebKit.WebContent instance ID: Optional([_EXExtensionInstanceIdentifier: 664DE272-5DCA-4C17-806E-27DDD3A03950]) pid: 46069.
default	09:45:31.907021+0800	hootowl	AssertionCapability::AssertionCapability: taking assertion Foreground
default	09:45:31.907540+0800	hootowl	[0x1495b4dc0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	09:45:31.914107+0800	hootowl	WebContent[46069] Installed launch log hook
default	09:45:31.914428+0800	hootowl	0x1310740c0 - [PID=46069] WebProcessProxy::didFinishLaunching:
default	09:45:31.914577+0800	hootowl	0x131074150 - [PID=46069] ProcessThrottler::didConnectToProcess
default	09:45:31.914640+0800	hootowl	0x131074150 - [PID=46069] ProcessThrottler::setThrottleState: Updating process assertion type to 3 (foregroundActivities=1, backgroundActivities=2)
default	09:45:31.914702+0800	hootowl	AssertionCapability::AssertionCapability: taking assertion Foreground
default	09:45:31.914746+0800	hootowl	0x1310740c0 - [PID=46069] WebProcessProxy::didChangeThrottleState: type=2
default	09:45:31.914781+0800	hootowl	0x1310740c0 - [PID=46069] WebProcessProxy::didChangeThrottleState(Foreground) Taking foreground assertion for network process
default	09:45:31.914813+0800	hootowl	0x13113c0c0 - ProcessAssertion::acquireSync Trying to take RBS assertion 'WebProcess Foreground Assertion' for process with PID=46069
default	09:45:31.914851+0800	hootowl	0x131114190 - NetworkProcessProxy::sendXPCEndpointToProcess(0x1310740c0) state = 1 has connection = 1 XPC endpoint message = 0x14a32cc00
default	09:45:31.915038+0800	hootowl	WebContent[46069] [0x1036070c0] invalidated after the last release of the connection object
default	09:45:31.915054+0800	hootowl	WebContent[46069] [0x1036073d0] invalidated because the client process (pid 46069) either cancelled the connection or exited
default	09:45:31.915409+0800	hootowl	0x13113c0c0 - ProcessAssertion() Successfully granted capability
default	09:45:31.919873+0800	hootowl	WebContent[46069] [0x10360ad20] activating connection: mach=false listener=false peer=false name=(anonymous)
default	09:45:31.919986+0800	hootowl	0x131030120 - [PID=46069, throttler=0x131074150] ProcessThrottler::Activity::invalidate: Ending foreground activity / 'Process initialization'
default	09:45:31.920005+0800	hootowl	0x131074150 - [PID=46069] ProcessThrottler::setThrottleState: Updating process assertion type to 1 (foregroundActivities=0, backgroundActivities=2)
default	09:45:31.920012+0800	hootowl	AssertionCapability::AssertionCapability: taking assertion Background
default	09:45:31.920567+0800	hootowl	0x1310740c0 - [PID=46069] WebProcessProxy::didChangeThrottleState: type=1
default	09:45:31.921154+0800	hootowl	0x1310740c0 - [PID=46069] WebProcessProxy::didChangeThrottleState(Background) Taking background assertion for network process
default	09:45:31.921225+0800	hootowl	0x13113c480 - ProcessAssertion::acquireSync Trying to take RBS assertion 'WebProcess Background Assertion' for process with PID=46069
default	09:45:31.921232+0800	hootowl	WebContent[46069] getNetworkProcessConnection: Request connection for core identifier 7
default	09:45:31.921241+0800	hootowl	0x131114190 - NetworkProcessProxy::getNetworkProcessConnection: Taking a background assertion because web process pid 46069 (core identifier 7) is requesting a connection
default	09:45:31.921272+0800	hootowl	0x13113c480 - ProcessAssertion() Successfully granted capability
default	09:45:31.921463+0800	hootowl	WebContent[46069] Received Launch Services database
default	09:45:31.921648+0800	hootowl	WebContent[46069] 0x10806c100 - [sessionID=1] WebProcess::initializeLogForwarding: Debug logging enabled: 1
default	09:45:31.921858+0800	hootowl	WebContent[46069] WebProcess::platformInitializeWebProcess
default	09:45:31.921892+0800	hootowl	WebContent[46069] [0x103606ee0] Connection returned listener port: 0x1b03
default	09:45:31.921964+0800	hootowl	WebContent[46069] [0x103607fe0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	09:45:31.921972+0800	hootowl	WebContent[46069] [0x106e48000] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0x103606ee0.peer[46069].0x106e48000
default	09:45:31.924412+0800	hootowl	[0x1495b4dc0] Re-initialization successful; calling out to event handler with XPC_ERROR_CONNECTION_INTERRUPTED
default	09:45:31.924520+0800	hootowl	WebContent[46069] Application accessibility enabled: 1, (
	0   libAccessibility.dylib              0x00000001943ea920 _AXSApplicationAccessibilitySetEnabled + 84
	1   WebKit                              0x00000001ace77730 C39BD22C-3475-38AF-91BD-0B7574081011 + 12146480
	2   WebKit                              0x00000001ad0d054c C39BD22C-3475-38AF-91BD-0B7574081011 + 14607692
	3   WebKit                              0x00000001ac8f43f4 C39BD22C-3475-38AF-91BD-0B7574081011 + 6366196
	4   WebKit                              0x00000001ad58b714 C39BD22C-3475-38AF-91BD-0B7574081011 + 19568404
	5   WebKit                              0x00000001ad5b23a8 C39BD22C-3475-38AF-91BD-0B7574081011 + 19727272
	6   JavaScriptCore                      0x00000001a68da140 F7906028-1C6D-3B4C-BD93-78C196C83A83 + 692544
	7   JavaScriptCore                      0x00000001a68db6f8 F7906028-1C6D-3B4C-BD93-78C196C83A83 + 698104
	8   CoreFoundation                      0x0000000191073390 101EB2F1-1915-34A0-8BC9-631D03753B84 + 656272
	9   CoreFoundation                      0x000
default	09:45:31.924591+0800	hootowl	WebContent[0] Stored App AX setting: 1
default	09:45:31.924676+0800	hootowl	WebContent[0] AXS AccessibilityEnabled: (app ax: 1), ax settings: 1, cached: 1
default	09:45:31.931874+0800	hootowl	0x131074150 - [PID=46069] ProcessThrottler::sendPrepareToSuspendIPC: Sending PrepareToSuspend(2, isSuspensionImminent=0) IPC, remainingRunTime=0.000000s
default	09:45:31.932086+0800	hootowl	0x1310740c0 - [PID=46069] WebProcessProxy::sendPrepareToSuspend: isSuspensionImminent=0
default	09:45:31.932351+0800	hootowl	RemoteLayerTreeDrawingAreaProxy(1711)::hideContentUntilPendingUpdate
default	09:45:31.940818+0800	hootowl	boringssl_context_info_handler(2823) [C13:1][0x14d148560] Client handshake state: TLS 1.3 client read_hello_retry_request
default	09:45:31.940887+0800	hootowl	boringssl_context_info_handler(2823) [C13:1][0x14d148560] Client handshake state: TLS 1.3 client read_server_hello
default	09:45:31.941200+0800	hootowl	boringssl_context_info_handler(2823) [C13:1][0x14d148560] Client handshake state: TLS 1.3 client read_encrypted_extensions
default	09:45:31.941368+0800	hootowl	boringssl_context_info_handler(2823) [C13:1][0x14d148560] Client handshake state: TLS 1.3 client read_certificate_request
default	09:45:31.950016+0800	hootowl	boringssl_context_info_handler(2823) [C13:1][0x14d148560] Client handshake state: TLS 1.3 client read_server_certificate
default	09:45:31.950036+0800	hootowl	boringssl_context_info_handler(2823) [C13:1][0x14d148560] Client handshake state: TLS 1.3 client read_server_certificate_verify
default	09:45:31.951205+0800	hootowl	boringssl_context_evaluate_trust_async(2249) [C13:1][0x14d148560] Performing external trust evaluation
default	09:45:31.951386+0800	hootowl	boringssl_context_evaluate_trust_async_external(2234) [C13:1][0x14d148560] Asyncing for external verify block
default	09:45:31.951486+0800	hootowl	Connection 12: asked to evaluate TLS Trust
default	09:45:31.951929+0800	hootowl	WebContent[46069]: [sessionID=1] WebProcess::prepareToSuspend: isSuspensionImminent=0, remainingRunTime=0.020245s
default	09:45:31.951950+0800	hootowl	Task <6CFF7C9A-048E-4F63-BCCC-5D1446230E4B>.<1> auth completion disp=1 cred=0x0
default	09:45:31.951957+0800	hootowl	WebContent[46069]: [sessionID=1] WebProcess::freezeAllLayerTrees: WebProcess is freezing all layer trees
default	09:45:31.951966+0800	hootowl	WebContent[46069]: [webPageID=1709] WebPage::freezeLayerTree: Adding a reason to freeze layer tree (reason=4, new=4, old=0)
default	09:45:31.951976+0800	hootowl	WebContent[46069]: [sessionID=1] WebProcess::destroyRenderingResources: took 0.01ms
default	09:45:31.952002+0800	hootowl	WebContent[46069] 0x10806c100 - [sessionID=1] WebProcess::updateFreezerStatus: isFreezable=1, success
default	09:45:31.952089+0800	hootowl	WebContent[46069]: [sessionID=1] WebProcess::markAllLayersVolatile:
default	09:45:31.952097+0800	hootowl	WebContent[46069]: [webPageID=1709] WebPage::markLayersVolatile
default	09:45:31.952105+0800	hootowl	WebContent[46069] 0x10e3a0008 - [webPageID=1709] WebPage::markLayersVolatile: Succeeded in marking layers as volatile
default	09:45:31.952111+0800	hootowl	WebContent[46069] 0x10806c100 - [sessionID=1] WebProcess::markAllLayersVolatile: Successfuly marked layers as volatile for webPageID=1709
default	09:45:31.952119+0800	hootowl	WebContent[46069]: [sessionID=1] WebProcess::prepareToSuspend: Process is ready to suspend
default	09:45:31.952543+0800	hootowl	(Trust 0x14d239c80) No pending evals, starting
default	09:45:31.952553+0800	hootowl	0x131074150 - [PID=46069] ProcessThrottler::processReadyToSuspend: Updating process assertion to allow suspension
default	09:45:31.952575+0800	hootowl	0x131074150 - [PID=46069] ProcessThrottler::setThrottleState: Updating process assertion type to 0 (foregroundActivities=0, backgroundActivities=0)
default	09:45:31.952591+0800	hootowl	AssertionCapability::AssertionCapability: taking assertion Suspended
default	09:45:31.952600+0800	hootowl	0x131074150 - [PID=46069] ProcessThrottler::clearAssertion:
default	09:45:31.952609+0800	hootowl	0x1310740c0 - [PID=46069] WebProcessProxy::canTerminateAuxiliaryProcess: returns false (pageCount=1, remotePageCount=0, provisionalPageCount=0, suspendedPageCount=0, m_isInProcessCache=0, m_shutdownPreventingScopeCounter=0)
default	09:45:31.952615+0800	hootowl	0x1310740c0 - [PID=46069] WebProcessProxy::didChangeThrottleState: type=0
default	09:45:31.952621+0800	hootowl	0x1310740c0 - [PID=46069] WebProcessProxy::didChangeThrottleState(Suspended) Release all assertions for network process
default	09:45:31.952629+0800	hootowl	0x13113c600 - ProcessAssertion::acquireSync Trying to take RBS assertion 'WebProcess NearSuspended Assertion' for process with PID=46069
default	09:45:31.952650+0800	hootowl	[0x1495b7ac0] activating connection: mach=true listener=false peer=false name=com.apple.trustd
default	09:45:31.953022+0800	hootowl	WebContent[46069] 0x10806c100 - [sessionID=1] WebProcess::releaseMemory: BEGIN
default	09:45:31.953062+0800	hootowl	(Trust 0x14d239c80) Completed async eval kickoff
default	09:45:31.954935+0800	hootowl	0x13113c600 - ProcessAssertion() Successfully granted capability
default	09:45:31.958775+0800	hootowl	WebContent[46069] Memory pressure relief: Total: res = 9535488/8437760/-1097728, res+swap = 9978656/8880928/-1097728
default	09:45:31.960740+0800	hootowl	WebContent[46069] 0x10806c100 - [sessionID=1] WebProcess::releaseMemory: END
default	09:45:31.961922+0800	hootowl	0x131074150 - [PID=46069] ProcessThrottler::clearAssertion: Releasing near-suspended assertion
default	09:45:31.962189+0800	hootowl	0x13113c600 - ~ProcessAssertion: Releasing process assertion 'WebProcess NearSuspended Assertion' for process with PID=46069
default	09:45:31.962610+0800	hootowl	0x0 - ProcessAssertion: RBS Suspended assertion for process with PID=0 was invalidated
default	09:45:31.965236+0800	hootowl	(Trust 0x14d239c80) trustd returned 4
default	09:45:31.965316+0800	hootowl	System Trust Evaluation yielded status(0)
default	09:45:31.965368+0800	hootowl	(Trust 0x14d239bc0) No pending evals, starting
default	09:45:31.965998+0800	hootowl	[0x1495b43c0] activating connection: mach=true listener=false peer=false name=com.apple.trustd
default	09:45:31.966016+0800	hootowl	(Trust 0x14d239bc0) Completed async eval kickoff
default	09:45:31.966027+0800	hootowl	[0x1495b7ac0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	09:45:31.968628+0800	hootowl	(Trust 0x14d239bc0) trustd returned 4
default	09:45:31.968715+0800	hootowl	Connection 12: TLS Trust result 0
default	09:45:31.968741+0800	hootowl	boringssl_context_evaluate_trust_async_external_block_invoke_3(2148) [C13:1][0x14d148560] Returning from external verify block with result: true
default	09:45:31.968836+0800	hootowl	boringssl_context_certificate_verify_callback(2430) [C13:1][0x14d148560] Certificate verification result: OK
default	09:45:31.968862+0800	hootowl	boringssl_context_info_handler(2823) [C13:1][0x14d148560] Client handshake state: TLS 1.3 client read_server_finished
default	09:45:31.968918+0800	hootowl	boringssl_context_info_handler(2823) [C13:1][0x14d148560] Client handshake state: TLS 1.3 client send_end_of_early_data
default	09:45:31.969218+0800	hootowl	boringssl_context_info_handler(2823) [C13:1][0x14d148560] Client handshake state: TLS 1.3 client send_client_encrypted_extensions
default	09:45:31.969237+0800	hootowl	boringssl_context_info_handler(2823) [C13:1][0x14d148560] Client handshake state: TLS 1.3 client send_client_certificate
default	09:45:31.969386+0800	hootowl	boringssl_context_info_handler(2823) [C13:1][0x14d148560] Client handshake state: TLS 1.3 client complete_second_flight
default	09:45:31.969475+0800	hootowl	boringssl_context_info_handler(2823) [C13:1][0x14d148560] Client handshake state: TLS 1.3 client done
default	09:45:31.969481+0800	hootowl	boringssl_context_info_handler(2823) [C13:1][0x14d148560] Client handshake state: TLS client finish_client_handshake
default	09:45:31.969489+0800	hootowl	boringssl_context_info_handler(2823) [C13:1][0x14d148560] Client handshake state: TLS client done
default	09:45:31.969497+0800	hootowl	boringssl_context_info_handler(2812) [C13:1][0x14d148560] Client handshake done
default	09:45:31.970694+0800	hootowl	TX focusApplication (peekAppEvent) stealKB:Y scene:com.sharkda.hootowl-83FF55F6-7B28-4BFD-8825-33CB43E5D162
default	09:45:31.970741+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:31.970758+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	09:45:31.970769+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1481fc400>; contextId: 0xF4D9041F
default	09:45:31.972176+0800	hootowl	nw_protocol_boringssl_signal_connected(895) [C13:1][0x14d148560] TLS connected [server(0) version(0x0304) ciphersuite(TLS_AES_256_GCM_SHA384) group(0x11ec) signature_alg(0x0403) alpn(h3) resumed(0) offered_ticket(0) in_early_data(0) early_data_accepted(0) false_started(0) ocsp_received(0) sct_received(0) connect_time(146ms) flight_time(118ms) rtt(117ms) write_stalls(0) read_stalls(7) pake(0x0000)]
default	09:45:31.972206+0800	hootowl	nw_flow_connected [C13 142.250.204.34:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (tls)
default	09:45:31.972341+0800	hootowl	[C13 142.250.204.34:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_connect @0.150s
default	09:45:31.972393+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C13] reporting state ready
default	09:45:31.972465+0800	hootowl	[C13 142.250.204.34:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.151s
default	09:45:31.972803+0800	hootowl	[0x1495b43c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	09:45:31.973624+0800	hootowl	quic_pmtud_restart [C12.1.1.1:2] [-e810b29be49a92b4] PMTUD enabled, max PMTU: 1500, header size: 28, current PMTU 1228
default	09:45:31.973642+0800	hootowl	quic_crypto_tls_ready_inner [C12.1.1.1:2] [-e810b29be49a92b4] QUIC connection established in 153.616 ms, RTT 89.053 ms
default	09:45:31.973668+0800	hootowl	nw_flow_connected [C12.1.1.1 142.250.204.34:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Transport protocol connected (quic-connection)
default	09:45:31.974046+0800	hootowl	[C12.1.1.1 142.250.204.34:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_transport @0.176s
default	09:45:31.974220+0800	hootowl	nw_flow_connected [C12.1.1.1 142.250.204.34:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (CFNetworkConnection-4283075305)
default	09:45:31.974358+0800	hootowl	[C12.1.1.1 142.250.204.34:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.177s
default	09:45:31.974678+0800	hootowl	[C12.1.1 googleads.g.doubleclick.net:443 ready resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.177s
default	09:45:31.975193+0800	hootowl	[C12.1 googleads.g.doubleclick.net:443 ready transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.177s
default	09:45:31.975244+0800	hootowl	[C12.1.1.1 142.250.204.34:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.178s
default	09:45:31.975269+0800	hootowl	[C12.1.1 googleads.g.doubleclick.net:443 ready resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.178s
default	09:45:31.975315+0800	hootowl	[C12.1 googleads.g.doubleclick.net:443 ready transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.178s
default	09:45:31.975323+0800	hootowl	nw_flow_connected [C12 142.250.204.34:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (endpoint_flow)
default	09:45:31.975452+0800	hootowl	[C12 142.250.204.34:443 ready parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_connect @0.178s
default	09:45:31.975642+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C12] reporting state ready
default	09:45:31.975651+0800	hootowl	[C12 142.250.204.34:443 ready parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.178s
default	09:45:31.975658+0800	hootowl	nw_connection_send_viability_changed_on_nw_queue [C12] viability_changed_handler(true)
error	09:45:31.975800+0800	hootowl	nw_protocol_instance_set_output_handler Not calling remove_input_handler on 0x14c2943c0:udp
default	09:45:31.975876+0800	hootowl	quic_migration_path_event_block_invoke [C12.1.1.1:2] [-e810b29be49a92b4] path acc2fbe472287a9c over en0 received event established
default	09:45:31.975972+0800	hootowl	quic_migration_evaluate_primary [C12.1.1.1:2] [-e810b29be49a92b4] promoted path 0x14ca86680 over en0 to primary
default	09:45:31.976008+0800	hootowl	quic_migration_path_event_block_invoke [C12.1.1.1:2] [-e810b29be49a92b4] path bf1e24ca3f13ab06 over pdp_ip0 received event available
error	09:45:31.976255+0800	hootowl	quic_conn_setup_pmtud [C12.1.1.1:2] [-e810b29be49a92b4] unable to query remote endpoint, assuming IPv6
default	09:45:31.976341+0800	hootowl	quic_pmtud_restart [C12.1.1.1:2] [-e810b29be49a92b4] PMTUD enabled, max PMTU: 1450, header size: 48, current PMTU 1248
default	09:45:31.976670+0800	hootowl	quic_migration_evaluate [C12.1.1.1:2] [-e810b29be49a92b4] evaluating path migration
default	09:45:31.976705+0800	hootowl	quic_migration_evaluate_block_invoke [C12.1.1.1:2] [-e810b29be49a92b4] path bf1e24ca3f13ab06 state available (0), ifname pdp_ip0, primary? 0, initial? 0, fallback? 0, preferred? 0 lossy? 0
default	09:45:31.976766+0800	hootowl	quic_migration_evaluate_block_invoke [C12.1.1.1:2] [-e810b29be49a92b4] path acc2fbe472287a9c state validated (0), ifname en0, primary? 1, initial? 1, fallback? 0, preferred? 0 lossy? 0
default	09:45:31.976835+0800	hootowl	quic_migration_evaluate [C12.1.1.1:2] [-e810b29be49a92b4] current path is usable, no strong fallback or we are probing
default	09:45:31.976845+0800	hootowl	nw_protocol_instance_report_ready [C12.1.1.1:2] Calling notify with interface en0 for flow_registration C9261B5B-E31B-4DCF-ABEF-01BFD6380F6D
default	09:45:31.976943+0800	hootowl	[C12.1.1.1 142.250.204.34:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:migrated @0.180s, uuid: 4225A72C-8C9D-4228-8798-760778B4703B
default	09:45:31.977193+0800	hootowl	[C12.1.1 googleads.g.doubleclick.net:443 ready resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:migrated @0.180s, uuid: 75CBD141-81A8-4F52-AAB4-C248E7AF0D33
default	09:45:31.977242+0800	hootowl	[C12.1 googleads.g.doubleclick.net:443 ready transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:migrated @0.180s, uuid: 4F7DF4B0-1D6A-4298-83A6-080DCC81EB1C
default	09:45:31.977250+0800	hootowl	[C12 142.250.204.34:443 ready parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:migrated @0.180s, uuid: 4F7DF4B0-1D6A-4298-83A6-080DCC81EB1C
default	09:45:31.977332+0800	hootowl	quic_stream_create_inbound [C12.1.1.1:2] [-e810b29be49a92b4] creating inbound stream 3
default	09:45:31.977526+0800	hootowl	quic_migration_evaluate [C12.1.1.1:2] [-e810b29be49a92b4] evaluating path migration
default	09:45:31.977533+0800	hootowl	quic_migration_evaluate_block_invoke [C12.1.1.1:2] [-e810b29be49a92b4] path bf1e24ca3f13ab06 state available (0), ifname pdp_ip0, primary? 0, initial? 0, fallback? 0, preferred? 0 lossy? 0
default	09:45:31.977576+0800	hootowl	quic_migration_evaluate_block_invoke [C12.1.1.1:2] [-e810b29be49a92b4] path acc2fbe472287a9c state validated (0), ifname en0, primary? 1, initial? 1, fallback? 0, preferred? 0 lossy? 0
default	09:45:31.977587+0800	hootowl	quic_migration_evaluate [C12.1.1.1:2] [-e810b29be49a92b4] current path is usable, no strong fallback or we are probing
default	09:45:31.977722+0800	hootowl	Connection 12: connected successfully
default	09:45:31.977734+0800	hootowl	Connection 12: TLS handshake complete
default	09:45:31.978086+0800	hootowl	Connection 12: ready C(N) E(N)
default	09:45:31.978337+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:31.978785+0800	hootowl	[C12] event: client:connection_reused @0.181s
default	09:45:31.978816+0800	hootowl	Task <6CFF7C9A-048E-4F63-BCCC-5D1446230E4B>.<1> now using Connection 12
default	09:45:31.979316+0800	hootowl	Connection 12: received viability advisory(Y)
default	09:45:31.979541+0800	hootowl	0x14cb10718 ID=0 Task <6CFF7C9A-048E-4F63-BCCC-5D1446230E4B>.<1> sent request, body N 0
default	09:45:31.981520+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:31.994158+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
error	09:45:32.999811+0800	hootowl	WebContent[46069] Could not register system wide server: -25204
error	09:45:32.999866+0800	hootowl	WebContent[46069] _AXAddToElementCache was called even though the element was in the cache: <WKAccessibilityWebPageObject: 0x103600e10>
default	09:45:32.013097+0800	hootowl	<UIWindowScene: 0x148378200> (83FF55F6-7B28-4BFD-8825-33CB43E5D162) Scene updated orientation preferences: ( Pu ) -> ( Pu Ll Lr )
default	09:45:32.019048+0800	hootowl	boringssl_context_new_session_handler(1771) [C13:1][0x14d148560] Asyncing for session update block
default	09:45:32.019215+0800	hootowl	boringssl_context_new_session_handler(1771) [C13:1][0x14d148560] Asyncing for session update block
default	09:45:32.019299+0800	hootowl	nw_protocol_boringssl_signal_connected(895) [C13:1][0x14d148560] TLS connected [server(0) version(0x0304) ciphersuite(TLS_AES_256_GCM_SHA384) group(0x11ec) signature_alg(0x0403) alpn(h3) resumed(0) offered_ticket(0) in_early_data(0) early_data_accepted(0) false_started(0) ocsp_received(0) sct_received(0) connect_time(146ms) flight_time(118ms) rtt(117ms) write_stalls(0) read_stalls(7) pake(0x0000)]
default	09:45:32.019365+0800	hootowl	nw_flow_connected [C13 142.250.204.34:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (tls)
default	09:45:32.020195+0800	hootowl	boringssl_context_new_session_handler_block_invoke(1774) [C13:1][0x14d148560] Returning from session update block
default	09:45:32.020545+0800	hootowl	boringssl_context_new_session_handler_block_invoke(1774) [C13:1][0x14d148560] Returning from session update block
default	09:45:32.028548+0800	hootowl	quic_stream_create_inbound [C12.1.1.1:2] [-e810b29be49a92b4] creating inbound stream 7 (out of order)
default	09:45:32.028676+0800	hootowl	quic_stream_create_inbound [C12.1.1.1:2] [-e810b29be49a92b4] creating inbound stream 11
default	09:45:32.028932+0800	hootowl	0x14cb10718 ID=0 Task <6CFF7C9A-048E-4F63-BCCC-5D1446230E4B>.<1> received response, status 200 content K
default	09:45:32.029000+0800	hootowl	[0x14957f840] activating connection: mach=true listener=false peer=false name=com.apple.trustd
default	09:45:32.031141+0800	hootowl	[0x14957f840] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	09:45:32.031440+0800	hootowl	Task <6CFF7C9A-048E-4F63-BCCC-5D1446230E4B>.<1> response ended
default	09:45:32.031801+0800	hootowl	[C12] event: client:connection_idle @0.234s
default	09:45:32.031934+0800	hootowl	Task <6CFF7C9A-048E-4F63-BCCC-5D1446230E4B>.<1> done using Connection 12
default	09:45:32.032007+0800	hootowl	Task <6CFF7C9A-048E-4F63-BCCC-5D1446230E4B>.<1> summary for task success {transaction_duration_ms=238, response_status=200, connection=12, protocol="h3", domain_lookup_duration_ms=15, connect_duration_ms=155, secure_connection_duration_ms=153, private_relay=false, request_start_ms=185, request_duration_ms=0, response_start_ms=235, response_duration_ms=2, request_bytes=1393, request_throughput_kbps=14287, response_bytes=367, response_throughput_kbps=1009, cache_hit=false}
default	09:45:32.032104+0800	hootowl	Task <6CFF7C9A-048E-4F63-BCCC-5D1446230E4B>.<1> finished successfully
default	09:45:32.032411+0800	hootowl	Ending background task with UIBackgroundTaskIdentifier: 2
default	09:45:32.032418+0800	hootowl	Ending task with identifier 2 and description: <_UIBackgroundTaskInfo: 0x148e25680>: taskID = 2, taskName = com.google.backgroundPing, creationTime = 771922 (elapsed = 1), _expireHandler: <__NSMallocBlock__: 0x14a3e0d50>
default	09:45:32.032437+0800	hootowl	Decrementing reference count for assertion <BKSProcessAssertion: 0x14d2205f0> (used by background task with identifier 2: <_UIBackgroundTaskInfo: 0x148e25680>: taskID = 2, taskName = com.google.backgroundPing, creationTime = 771922 (elapsed = 1))
default	09:45:32.032444+0800	hootowl	Will invalidate assertion: <BKSProcessAssertion: 0x14d2205f0> for task identifier: 2
default	09:45:32.068711+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:32.068831+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	09:45:32.069025+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1481fc400>; contextId: 0xF4D9041F
default	09:45:32.069346+0800	hootowl	<UIWindowScene: 0x148378200> (83FF55F6-7B28-4BFD-8825-33CB43E5D162) Scene updated orientation preferences: ( Pu Ll Lr ) -> ( Pu )
default	09:45:32.082417+0800	hootowl	MncplCyclopsScreen 78
🏠 body eval — items:6 firstObs:6s firstCar:0
default	09:45:32.087136+0800	hootowl	MncplCyclopsScreen 78
🏠 body eval — items:6 firstObs:6s firstCar:0
default	09:45:32.109764+0800	hootowl	WebContent[46068] Loading PDFKit
default	09:45:32.122566+0800	hootowl	MncplCyclopsScreen 149
🪟 MncplCyclopsScreen onAppear — municipal 🆔 8064324136773232350
default	09:45:32.141063+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 1
fault	09:45:32.233357+0800	hootowl	__delegate_identifier__:Performance Diagnostics__:::____message__:{"message":"Interprocess communication on the main thread can cause non-deterministic delays.","antipattern trigger":"-[AVAudioSession setActive:withOptions:error:]","message type":"suppressable","issue type":1,"category type":17,"subcategory type":0,"show in console":"0"}'5C 1D 99 DD E0 FB 36 D2 81 44 D1 3E C7 94 D6 09 FC 97 03 00 5C 1D 99 DD E0 FB 36 D2 81 44 D1 3E C7 94 D6 09 A8 BA 0C 00 5C 1D 99 DD E0 FB 36 D2 81 44 D1 3E C7 94 D6 09 34 E3 1F 00 9C 46 02 57 4A 68 37 D5 82 C4 55 C3 3C 0A 25 9E BC A8 0B 00 9C 46 02 57 4A 68 37 D5 82 C4 55 C3 3C 0A 25 9E D8 A4 0B 00 9C 46 02 57 4A 68 37 D5 82 C4 55 C3 3C 0A 25 9E 98 9F 0B 00 9C 46 02 57 4A 68 37 D5 82 C4 55 C3 3C 0A 25 9E C0 2B 06 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 4C 4E 1C 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 84 63 1C 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 10 4E 1B 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 24 74 07 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 48 D0 29 00 FF 77 AB D1 15 84 38 80 88 51 C0 F3 AD 15 F7 7D 60 4F 00 00 FF 77 AB D1 15 84 38 80 88 51 C0 F3 AD 15 F7 7D FC 3B 00 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 18 F6 03 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 04 42 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 44 41 01 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 68 20 0A 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 04 F6 02 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 4C E5 02 00 41 11 65 E2 EE 8E 38 0E B2 54 99 77 27 39 71 E3 98 14 00 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 70 16 12 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 58 C1 08 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 70 05 03 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D F4 D0 02 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 48 CC 02 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 14 8C 36 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 C0 8C 36 00 0F 8D 35 B6 55 6F 3E 34 8E AA 80 AB 54 04 7D C5 1C 4C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
error	09:45:32.296201+0800	hootowl	WebContent[46069] Service "com.apple.CARenderServer" failed bootstrap look up (1) - (os/kern) invalid address
default	09:45:32.296799+0800	hootowl	WebContent[46069] Evaluated capturing state as 0 on <UIScreen: 0x106fa0a00> for initial
error	09:45:32.296967+0800	hootowl	WebContent[46069] Failed to initialize application enviroment context
error	09:45:32.297075+0800	hootowl	WebContent[46069] Failed to load a device context.
error	09:45:32.297180+0800	hootowl	WebContent[46069] Failed to initialize application enviroment context
error	09:45:32.297327+0800	hootowl	WebContent[46069] Failed to load a device context.
default	09:45:32.297354+0800	hootowl	WebContent[46069] Read CategoryName: per-app = 1, category name = (null)
default	09:45:32.297374+0800	hootowl	WebContent[46069] Read CategoryName: per-app = 0, category name = UICTContentSizeCategoryXXXL
default	09:45:32.447746+0800	hootowl	WebContent[46069] Read Per-App on Init: Smart invert = (null)
default	09:45:32.623152+0800	hootowl	WebContent[46069] Loading PDFKit
default	09:45:32.640317+0800	hootowl	TX focusApplication (peekAppEvent) stealKB:Y scene:com.sharkda.hootowl-83FF55F6-7B28-4BFD-8825-33CB43E5D162
default	09:45:32.640328+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:32.640337+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	09:45:32.640351+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1481fc400>; contextId: 0xF4D9041F
default	09:45:32.641089+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:32.736001+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:32.736025+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	09:45:32.736035+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1481fc400>; contextId: 0xF4D9041F
default	09:45:32.739413+0800	hootowl	<UIWindowScene: 0x148378200> (83FF55F6-7B28-4BFD-8825-33CB43E5D162) Scene updated orientation preferences: ( Pu ) -> ( Pu Ll Lr )
default	09:45:32.739440+0800	hootowl	<UIWindowScene: 0x148378200> (83FF55F6-7B28-4BFD-8825-33CB43E5D162) Scene updated orientation preferences: ( Pu Ll Lr ) -> ( Pu )
default	09:45:32.754837+0800	hootowl	MncplCyclopsScreen 78
🏠 body eval — items:6 firstObs:7s firstCar:0
default	09:45:32.768733+0800	hootowl	MncplCyclopsScreen 78
🏠 body eval — items:6 firstObs:7s firstCar:0
default	09:45:32.804975+0800	hootowl	Received state update for 46045 (app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>, unknown-NotVisible
default	09:45:32.822834+0800	hootowl	{"msg":"CLLocationManager", "event":"activity", "_cmd":"initWithEffectiveBundleIdentifier:bundlePath:websiteIdentifier:delegate:silo:", "self":"0x14ca9c180", "identifier":"", "bundlePath":""}
default	09:45:32.822945+0800	hootowl	{"msg":"client allocated", "client":"0x14a02ed80"}
default	09:45:32.823000+0800	hootowl	{"msg":"_CLClientCreateConnection", "event":"activity", "client":"0x14a02ed80"}
default	09:45:32.823034+0800	hootowl	{"msg":"Sending cached messages to daemon", "event":"activity"}
default	09:45:32.823044+0800	hootowl	[0x1496517c0] activating connection: mach=true listener=false peer=false name=com.apple.locationd.registration
default	09:45:32.823354+0800	hootowl	{"msg":"CLLocationManager", "event":"activity", "_cmd":"setDelegate:", "self":"0x14ca9c180", "delegate":"0x14b4d0840"}
default	09:45:32.823440+0800	hootowl	{"msg":"CLLocationManager", "event":"activity", "_cmd":"setDistanceFilter:", "self":"0x14ca9c180", "distance":"-1.000000"}
default	09:45:32.823498+0800	hootowl	{"msg":"CLLocationManager", "event":"activity", "_cmd":"setDesiredAccuracy:", "self":"0x14ca9c180", "accuracy":"-1.000000"}
default	09:45:32.823559+0800	hootowl	{"msg":"CLLocationManager", "event":"activity", "_cmd":"setActivityType:", "self":"0x14ca9c180", "activityType":{"type":"decode failure","raw value":0,"expected type":"Generic"}}
default	09:45:32.823735+0800	hootowl	{"msg":"CLLocationManager", "event":"activity", "_cmd":"setAllowsAlteredAccessoryLocations:", "self":"0x14ca9c180", "enabled":1}
default	09:45:32.824718+0800	hootowl	{"msg":"CLLocationManager", "event":"activity", "_cmd":"onClientEventRegistration:", "self":"0x14ca9c180", "clientKey":"icom.sharkda.hootowl:"}
default	09:45:32.825905+0800	hootowl	{"msg":"#CLLocationManager invoking #delegate", "self":"0x14ca9c180", "delegate":"0x14b4d0840", "selector":"locationManagerDidChangeAuthorization:", "authorizationStatus":"AuthorizedWhenInUse", "limitsPrecision":0, "isAuthorizedForWidgetUpdates":0}
default	09:45:32.825951+0800	hootowl	{"msg":"CLLocationManager", "event":"activity", "_cmd":"desiredAccuracy", "self":"0x14ca9c180"}
default	09:45:32.826000+0800	hootowl	{"msg":"CLLocationManager", "event":"activity", "_cmd":"desiredAccuracy", "self":"0x14ca9c180"}
default	09:45:32.826414+0800	hootowl	{"msg":"CLLocationManager", "event":"activity", "_cmd":"desiredAccuracy", "self":"0x14ca9c180"}
default	09:45:32.826488+0800	hootowl	{"msg":"CLLocationManager", "event":"activity", "_cmd":"desiredAccuracy", "self":"0x14ca9c180"}
default	09:45:32.826606+0800	hootowl	{"msg":"CLLocationManager", "event":"activity", "_cmd":"desiredAccuracy", "self":"0x14ca9c180"}
default	09:45:32.826630+0800	hootowl	{"msg":"CLLocationManager", "event":"activity", "_cmd":"desiredAccuracy", "self":"0x14ca9c180"}
default	09:45:32.826807+0800	hootowl	{"msg":"CLLocationManager", "event":"activity", "_cmd":"desiredAccuracy", "self":"0x14ca9c180"}
default	09:45:32.826905+0800	hootowl	{"msg":"CLLocationManager", "event":"activity", "_cmd":"desiredAccuracy", "self":"0x14ca9c180"}
default	09:45:32.827621+0800	hootowl	{"msg":"CLLocationManager", "event":"activity", "_cmd":"desiredAccuracy", "self":"0x14ca9c180"}
default	09:45:32.827651+0800	hootowl	{"msg":"CLLocationManager", "event":"activity", "_cmd":"desiredAccuracy", "self":"0x14ca9c180"}
default	09:45:32.828099+0800	hootowl	[0x1495b4280] activating connection: mach=true listener=false peer=false name=com.apple.geod
default	09:45:32.854809+0800	hootowl	[0x149580780] activating connection: mach=true listener=false peer=false name=com.apple.geod
default	09:45:32.880940+0800	hootowl	{"msg":"CLLocationManager", "event":"activity", "_cmd":"desiredAccuracy", "self":"0x14ca9c180"}
default	09:45:32.882489+0800	hootowl	{"msg":"CLLocationManager", "event":"activity", "_cmd":"desiredAccuracy", "self":"0x14ca9c180"}
default	09:45:32.891071+0800	hootowl	{"msg":"CLLocationManager", "event":"activity", "_cmd":"desiredAccuracy", "self":"0x14ca9c180"}
default	09:45:32.891139+0800	hootowl	{"msg":"CLLocationManager", "event":"activity", "_cmd":"desiredAccuracy", "self":"0x14ca9c180"}
default	09:45:32.891222+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 1
default	09:45:32.916877+0800	hootowl	[0x14d232700] activating connection: mach=false listener=false peer=false name=com.apple.PerfPowerTelemetryClientRegistrationService
default	09:45:32.918978+0800	hootowl	[0x14d232700] failed to do a bootstrap look-up: xpc_error=[159: Unknown error: 159]
default	09:45:32.918999+0800	hootowl	[0x14d232700] invalidated after a failed init
error	09:45:32.919584+0800	hootowl	Connection error: Error Domain=NSCocoaErrorDomain Code=4099 "The connection to service named com.apple.PerfPowerTelemetryClientRegistrationService was invalidated: Connection init failed at lookup with error 159 - Sandbox restriction." UserInfo={NSDebugDescription=The connection to service named com.apple.PerfPowerTelemetryClientRegistrationService was invalidated: Connection init failed at lookup with error 159 - Sandbox restriction.}
error	09:45:32.919976+0800	hootowl	(+[PPSClientDonation isRegisteredSubsystem:category:]) Permission denied: Maps / SpringfieldUsage
error	09:45:32.920116+0800	hootowl	(+[PPSClientDonation sendEventWithIdentifier:payload:]) Invalid inputs: payload={
    isSPR = 1;
}
default	09:45:32.934681+0800	hootowl	nw_path_evaluator_start [D9FCE28C-D9A7-4BCD-B13E-9705B4B35876 configuration.ls.apple.com:443 generic, url: https://configuration.ls.apple.com/config/defaults, attribution: developer]
	path: satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good
default	09:45:32.968631+0800	hootowl	0x148c1c800 - WKApplicationStateTrackingView: View with page [0x148ec2318, pageProxyID=375] was removed from a window, _lastObservedStateWasBackground=0
default	09:45:32.968652+0800	hootowl	0x148d72800 (pageProxyID=375) -[WKWebView _endLiveResize]
default	09:45:32.970211+0800	hootowl	[0x1496c6440] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	09:45:32.970222+0800	hootowl	0x148ec2318 - [pageProxyID=375, webPageID=376, PID=46068] WebPageProxy::close:
default	09:45:32.970326+0800	hootowl	PlaybackSessionManagerProxy::invalidate(1292624887)
default	09:45:32.970345+0800	hootowl	PlaybackSessionManagerProxy::invalidate(1292624887)
default	09:45:32.970428+0800	hootowl	PlaybackSessionManagerProxy::~VideoPresentationManagerProxy(1292624887)
default	09:45:32.970459+0800	hootowl	PlaybackSessionManagerProxy::invalidate(1292624887)
default	09:45:32.970511+0800	hootowl	PlaybackSessionManagerProxy::~PlaybackSessionManagerProxy(1292624887)
default	09:45:32.970685+0800	hootowl	0x148ec2318 - [pageProxyID=375, webPageID=376, PID=46068] WebPageProxy::deactivateMediaCapability: deactivating (envID=46045-3-com.sharkda.hootowl) for URL 'https://googleads.g.doubleclick.net/mads/gma?caps=interactiveVideo_inlineVideo_transparentBackground_sdkVideo_sfv_ct_aboi_gcache_nav_navc_aso_th_mraid1_mraid2_mraid3_sdkAdmobApiForAds_di_autoplay_dinm_dim_dinmo_gls_xSeconds_omidEnabled_mediation_av&eid=318502621%2C318500618%2C318526966%2C44766145&format=713x100_mb&js=afma-sdk-i-v13.3.0&preqs=7&seq_num=8#caps=interactiveVideo_inlineVideo_transparentBackground_sdkVideo_sfv_ct_aboi_gcache_nav_navc_aso_th_mraid1_mraid2_mraid3_sdkAdmobApiForAds_di_autoplay_dinm_dim_dinmo_gls_xSeconds_omidEnabled_mediation_av&eid=318502621%252C318500618%252C318526966%252C44766145&format=713x100_mb&js=afma-sdk-i-v13.3.0&preqs=7&seq_num=8'
default	09:45:32.970834+0800	hootowl	0x148ec2318 - [pageProxyID=375, webPageID=376, PID=46068] WebPageProxy::setMediaCapability: clearing media capability
default	09:45:32.970921+0800	hootowl	0x131074c40 - [PID=46068] WebProcessProxy::removeWebPage: webPage=0x148ec2318, pageProxyID=375, webPageID=376
default	09:45:32.970943+0800	hootowl	0x131074c40 - [PID=46068] WebProcessProxy::canTerminateAuxiliaryProcess: returns false (pageCount=0, remotePageCount=0, provisionalPageCount=0, suspendedPageCount=0, m_isInProcessCache=0, m_shutdownPreventingScopeCounter=1)
default	09:45:32.971003+0800	hootowl	0x131030600 - [PID=46068, throttler=0x131074cd0] ProcessThrottler::Activity::invalidate: Ending foreground activity / 'View is visible'
default	09:45:32.971024+0800	hootowl	0x131074cd0 - [PID=46068] ProcessThrottler::setThrottleState: Updating process assertion type to 1 (foregroundActivities=0, backgroundActivities=1)
default	09:45:32.971359+0800	hootowl	AssertionCapability::AssertionCapability: taking assertion Background
default	09:45:32.971391+0800	hootowl	0x131074c40 - [PID=46068] WebProcessProxy::didChangeThrottleState: type=1
default	09:45:32.971556+0800	hootowl	0x131074c40 - [PID=46068] WebProcessProxy::didChangeThrottleState(Background) Taking background assertion for network process
default	09:45:32.971591+0800	hootowl	0x13113c600 - ProcessAssertion::acquireSync Trying to take RBS assertion 'WebProcess Background Assertion' for process with PID=46068
default	09:45:32.971648+0800	hootowl	0x148ec2318 - [pageProxyID=375, webPageID=376, PID=46068] WebPageProxy::destructor:
default	09:45:32.971669+0800	hootowl	0x131030210 - [PID=46068, throttler=0x131074cd0] ProcessThrottler::Activity::invalidate: Ending background activity / 'Page Load'
default	09:45:32.972285+0800	hootowl	0x13113c600 - ProcessAssertion() Successfully granted capability
default	09:45:32.972306+0800	hootowl	0x131074cd0 - [PID=46068] ProcessThrottler::sendPrepareToSuspendIPC: Sending PrepareToSuspend(3, isSuspensionImminent=0) IPC, remainingRunTime=0.000000s
default	09:45:32.972315+0800	hootowl	0x131074c40 - [PID=46068] WebProcessProxy::sendPrepareToSuspend: isSuspensionImminent=0
default	09:45:32.972322+0800	hootowl	0x131068220 - ~ApplicationStateTracker
default	09:45:32.972347+0800	hootowl	0x131068220 - ApplicationStateTracker::setIsInBackground: 1
default	09:45:32.972361+0800	hootowl	0x131074cd0 - [PID=46068] ProcessThrottler::updateThrottleStateIfNeeded: sending ProcessDidResume IPC because the WebProcess is still processing request to suspend=3 (probable wakeup reason: WebPage_Close)
default	09:45:32.972368+0800	hootowl	0x131074c40 - [PID=46068] WebProcessProxy::sendProcessDidResume:
default	09:45:32.972430+0800	hootowl	0x131074c40 - [PID=46068] WebProcessProxy::canTerminateAuxiliaryProcess: returns false (pageCount=0, remotePageCount=0, provisionalPageCount=0, suspendedPageCount=0, m_isInProcessCache=0, m_shutdownPreventingScopeCounter=1)
default	09:45:32.972466+0800	hootowl	0x13113c0c0 - ~ProcessAssertion: Releasing process assertion 'WebProcess Foreground Assertion' for process with PID=46069
default	09:45:32.972482+0800	hootowl	0x13113c480 - ~ProcessAssertion: Releasing process assertion 'WebProcess Background Assertion' for process with PID=46069
default	09:45:32.972489+0800	hootowl	0x0 - ProcessAssertion: RBS Foreground assertion for process with PID=0 was invalidated
default	09:45:32.972764+0800	hootowl	0x0 - ProcessAssertion: RBS Background assertion for process with PID=0 was invalidated
default	09:45:32.973545+0800	hootowl	WebContent[46068]: [sessionID=1] WebProcess::prepareToSuspend: isSuspensionImminent=0, remainingRunTime=0.002356s
default	09:45:32.973563+0800	hootowl	WebContent[46068] 0x10e06c100 - [sessionID=1] WebProcess::releaseMemory: BEGIN
default	09:45:32.977369+0800	hootowl	WebContent[46068] Memory pressure relief: Total: res = 38289408/27639808/-10649600, res+swap = 56345616/46760976/-9584640
default	09:45:32.977384+0800	hootowl	WebContent[46068] 0x10e06c100 - [sessionID=1] WebProcess::releaseMemory: END
default	09:45:32.977396+0800	hootowl	WebContent[46068]: [sessionID=1] WebProcess::freezeAllLayerTrees: WebProcess is freezing all layer trees
default	09:45:32.977442+0800	hootowl	WebContent[46068]: [webPageID=376] WebPage::freezeLayerTree: Adding a reason to freeze layer tree (reason=4, new=4, old=0)
default	09:45:32.977478+0800	hootowl	WebContent[46068]: [sessionID=1] WebProcess::destroyRenderingResources: took 0.00ms
default	09:45:32.977493+0800	hootowl	WebContent[46068] 0x10e06c100 - [sessionID=1] WebProcess::updateFreezerStatus: isFreezable=1, success
default	09:45:32.977509+0800	hootowl	WebContent[46068]: [sessionID=1] WebProcess::markAllLayersVolatile:
default	09:45:32.977602+0800	hootowl	WebContent[46068]: [webPageID=376] WebPage::markLayersVolatile
default	09:45:32.977757+0800	hootowl	WebContent[46068] 0x10e06c100 - [sessionID=1] WebProcess::processDidResume:
default	09:45:32.977845+0800	hootowl	WebContent[46068] 0x10e06c100 - [sessionID=1] WebProcess::cancelMarkAllLayersVolatile:
default	09:45:32.977891+0800	hootowl	WebContent[46068] 0x101bb0008 - [webPageID=376] WebPage::cancelMarkLayersVolatile:
error	09:45:32.977968+0800	hootowl	WebContent[46068] 0x10e06c100 - [sessionID=1] WebProcess::markAllLayersVolatile: Failed to mark layers as volatile for webPageID=376
default	09:45:32.977993+0800	hootowl	WebContent[46068]: [sessionID=1] WebProcess::prepareToSuspend: Process is ready to suspend
default	09:45:32.978075+0800	hootowl	WebContent[46068] 0x10e06c100 - [sessionID=1] WebProcess::unfreezeAllLayerTrees: WebProcess is unfreezing all layer trees
default	09:45:32.978091+0800	hootowl	WebContent[46068]: [webPageID=376] WebPage::unfreezeLayerTree: Removing a reason to freeze layer tree (reason=4, new=0, old=4)
default	09:45:32.978100+0800	hootowl	WebContent[46068]: [webPageID=376] WebPage::close
default	09:45:32.979118+0800	hootowl	WebContent[46068]: [pageID=376 frameID=25769803778 isMainFrame=0] FrameLoader::stopAllLoaders: m_provisionalDocumentLoader=0, m_documentLoader=4598394880
default	09:45:32.979126+0800	hootowl	WebContent[46068]: [pageID=376, frameID=25769803778, isMainFrame=0] DocumentLoader::stopLoading
default	09:45:32.979135+0800	hootowl	WebContent[46068]: [pageID=376 frameID=25769803778 isMainFrame=0] FrameLoader::setDocumentLoader: Setting document loader to 0 (was 4598394880)
default	09:45:32.979182+0800	hootowl	WebContent[46068]: [pageID=376, frameID=25769803778, isMainFrame=0] DocumentLoader::detachFromFrame
default	09:45:32.979268+0800	hootowl	WebContent[46068]: [pageID=376, frameID=25769803778, isMainFrame=0] DocumentLoader::stopLoading
default	09:45:32.979285+0800	hootowl	WebContent[46068]: [pageID=376 frameID=25769803777 isMainFrame=0] FrameLoader::stopAllLoaders: m_provisionalDocumentLoader=0, m_documentLoader=4598374400
default	09:45:32.979583+0800	hootowl	WebContent[46068]: [pageID=376, frameID=25769803777, isMainFrame=0] DocumentLoader::stopLoading
default	09:45:32.979628+0800	hootowl	WebContent[46068]: [pageID=376 frameID=25769803777 isMainFrame=0] FrameLoader::setDocumentLoader: Setting document loader to 0 (was 4598374400)
default	09:45:32.979728+0800	hootowl	WebContent[46068]: [pageID=376, frameID=25769803777, isMainFrame=0] DocumentLoader::detachFromFrame
default	09:45:32.979863+0800	hootowl	WebContent[46068]: [pageID=376, frameID=25769803777, isMainFrame=0] DocumentLoader::stopLoading
default	09:45:32.979885+0800	hootowl	WebContent[46068]: [pageID=376 frameID=4294967299 isMainFrame=1] FrameLoader::stopAllLoaders: m_provisionalDocumentLoader=0, m_documentLoader=4598304768
default	09:45:32.979901+0800	hootowl	WebContent[46068]: [pageID=376, frameID=4294967299, isMainFrame=1] DocumentLoader::stopLoading
default	09:45:32.979913+0800	hootowl	WebContent[46068]: [pageID=376 frameID=4294967299 isMainFrame=1] FrameLoader::setDocumentLoader: Setting document loader to 0 (was 4598304768)
default	09:45:32.979928+0800	hootowl	WebContent[46068]: [pageID=376, frameID=4294967299, isMainFrame=1] DocumentLoader::detachFromFrame
default	09:45:32.980000+0800	hootowl	WebContent[46068]: [pageID=376, frameID=4294967299, isMainFrame=1] DocumentLoader::stopLoading
default	09:45:32.981709+0800	hootowl	[0x14a69e100] activating connection: mach=false listener=false peer=false name=com.apple.PerfPowerTelemetryClientRegistrationService
default	09:45:32.988944+0800	hootowl	0x131074c40 - [PID=46068] WebProcessProxy::canTerminateAuxiliaryProcess: returns false (pageCount=0, remotePageCount=0, provisionalPageCount=0, suspendedPageCount=0, m_isInProcessCache=0, m_shutdownPreventingScopeCounter=1)
default	09:45:32.988951+0800	hootowl	WebContent[46068] 0x101bb0008 - [webPageID=376] WebPage::destructor:
default	09:45:32.989001+0800	hootowl	0x131074c40 - [PID=46068] WebProcessProxy::canTerminateAuxiliaryProcess: returns true
default	09:45:32.989008+0800	hootowl	0x131050380 - [PID=46068] WebProcessCache::canCacheProcess: Not caching process because the cache has no capacity
default	09:45:32.989016+0800	hootowl	0x131074c40 - [PID=46068] WebProcessProxy::shutDown:
default	09:45:32.989029+0800	hootowl	AssertionCapability::AssertionCapability: taking assertion Background
default	09:45:32.989044+0800	hootowl	0x131074c40 - [PID=46068] WebProcessProxy::processWillShutDown:
default	09:45:32.989253+0800	hootowl	0x131074cd0 - [PID=46068] ProcessThrottler::didDisconnectFromProcess:
default	09:45:32.989406+0800	hootowl	0x13113c600 - ~ProcessAssertion: Releasing process assertion 'WebProcess Background Assertion' for process with PID=46068
default	09:45:32.989670+0800	hootowl	0x131074c40 - [PID=46068] WebProcessProxy::destructor:
default	09:45:32.990309+0800	hootowl	0x13113c6c0 - ProcessAssertion::acquireSync Trying to take RBS assertion 'XPCConnectionTerminationWatchdog' for process with PID=46068
default	09:45:32.990335+0800	hootowl	WebBackForwardCache::clear
default	09:45:32.990345+0800	hootowl	0x131074cd0 - [PID=46068] ProcessThrottler::didDisconnectFromProcess:
default	09:45:32.990360+0800	hootowl	Assertion for extension process 'ExtensionProcess: bundleID: com.apple.WebKit.WebContent instance ID: Optional([_EXExtensionInstanceIdentifier: 2263C525-304F-4342-BED8-324592BF25D1]) pid: 46068' invalidated
default	09:45:32.991846+0800	hootowl	0x131074cd0 - [PID=0] ProcessThrottler::invalidateAllActivities: BEGIN (foregroundActivityCount: 0, backgroundActivityCount: 0)
default	09:45:32.991924+0800	hootowl	0x131074cd0 - [PID=0] ProcessThrottler::invalidateAllActivities: END
default	09:45:32.992012+0800	hootowl	0x13113c3c0 - ~ProcessAssertion: Releasing process assertion 'WebProcess Foreground Assertion' for process with PID=46068
error	09:45:33.003002+0800	hootowl	Error acquiring assertion: <Error Domain=RBSAssertionErrorDomain Code=2 "Specified target process 46068 does not exist" UserInfo={NSLocalizedFailureReason=Specified target process 46068 does not exist}>
default	09:45:33.003016+0800	hootowl	0x13113c6c0 - ProcessAssertion() Failed to grant capability Background
default	09:45:33.003096+0800	hootowl	[0x149595e00] invalidated after the last release of the connection object
default	09:45:33.003123+0800	hootowl	0x0 - ProcessAssertion: RBS Background assertion for process with PID=0 was invalidated
default	09:45:33.003194+0800	hootowl	0x0 - ProcessAssertion: RBS Foreground assertion for process with PID=0 was invalidated
error	09:45:33.003364+0800	hootowl	0x13113c6c0 - ProcessAssertion::acquireSync Failed to acquire RBS assertion 'XPCConnectionTerminationWatchdog' for process with PID=46068, error: (null)
default	09:45:33.004163+0800	hootowl	0x13113c6c0 - ProcessAssertion::processAssertionWasInvalidated() PID=46068
default	09:45:33.006550+0800	hootowl	Firing exit handlers for 46068 with context <RBSProcessExitContext| voluntary>
default	09:45:33.007031+0800	hootowl	Calling process death completion block for handle [xpcservice<com.apple.WebKit.WebContent([app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>:46045])>{vt hash: 71395982}[uuid:2263C525-304F-4342-BED8-324592BF25D1]{definition:com.apple.WebKit.WebContent[extension][client]}:46068]
error	09:45:33.018409+0800	hootowl	No packs of type config available for key: [Asia Southeast Icons, 3.000000]
error	09:45:33.018434+0800	hootowl	Failed to resolve packName for packKey:Asia Southeast Icons.3.000000 packType:config with resourceNames:[Guides_Icons_Default@3x.iconconfigpack, Guides_Icons_Default@3x.icondatapack, Expert_Partners_Icons@3x.iconconfigpack, Railroad_Crossing@3x.iconconfigpack, Default_Icons@3x.iconconfigpack, Expert_Partners_Icons@3x.icondatapack, Default_Icons@3x.icondatapack, Default_Shields@3x.iconconfigpack, Default@3x.iconmappack, Railroad_Crossing@3x.icondatapack, Default_Shields@3x.icondatapack]
error	09:45:33.018474+0800	hootowl	No config pack found for key Asia Southeast Icons
default	09:45:33.101999+0800	hootowl	[0x14a69e100] failed to do a bootstrap look-up: xpc_error=[159: Unknown error: 159]
default	09:45:33.164504+0800	hootowl	[0x14a69e100] invalidated after a failed init
error	09:45:33.189503+0800	hootowl	Connection error: Error Domain=NSCocoaErrorDomain Code=4099 "The connection to service named com.apple.PerfPowerTelemetryClientRegistrationService was invalidated: Connection init failed at lookup with error 159 - Sandbox restriction." UserInfo={NSDebugDescription=The connection to service named com.apple.PerfPowerTelemetryClientRegistrationService was invalidated: Connection init failed at lookup with error 159 - Sandbox restriction.}
error	09:45:33.189795+0800	hootowl	(+[PPSClientDonation isRegisteredSubsystem:category:]) Permission denied: Maps / SpringfieldUsage
error	09:45:33.189915+0800	hootowl	(+[PPSClientDonation sendEventWithIdentifier:payload:]) Invalid inputs: payload={
    isSPR = 0;
}
default	09:45:33.190706+0800	hootowl	[0x1509b5680] activating connection: mach=false listener=false peer=false name=com.apple.PerfPowerTelemetryClientRegistrationService
default	09:45:33.201423+0800	hootowl	[0x1509b5680] failed to do a bootstrap look-up: xpc_error=[159: Unknown error: 159]
default	09:45:33.201445+0800	hootowl	[0x1509b5680] invalidated after a failed init
error	09:45:33.207467+0800	hootowl	Connection error: Error Domain=NSCocoaErrorDomain Code=4099 "The connection to service named com.apple.PerfPowerTelemetryClientRegistrationService was invalidated: Connection init failed at lookup with error 159 - Sandbox restriction." UserInfo={NSDebugDescription=The connection to service named com.apple.PerfPowerTelemetryClientRegistrationService was invalidated: Connection init failed at lookup with error 159 - Sandbox restriction.}
error	09:45:33.207541+0800	hootowl	(+[PPSClientDonation isRegisteredSubsystem:category:]) Permission denied: Maps / SpringfieldUsage
default	09:45:33.239900+0800	hootowl	Task <4AEBF80A-C0C0-4A75-A035-DF07743AA658>.<7> response ended
default	09:45:33.239998+0800	hootowl	Task <4AEBF80A-C0C0-4A75-A035-DF07743AA658>.<7> done using Connection 1
default	09:45:33.240209+0800	hootowl	Task <4AEBF80A-C0C0-4A75-A035-DF07743AA658>.<7> summary for task success {transaction_duration_ms=3039, response_status=200, connection=1, reused=1, reused_after_ms=70, request_start_ms=130, request_duration_ms=0, response_start_ms=244, response_duration_ms=2794, request_bytes=248, request_throughput_kbps=24474, response_bytes=2857501, response_throughput_kbps=8179, cache_hit=false}
default	09:45:33.240230+0800	hootowl	[C1] event: client:connection_idle @10.253s
default	09:45:33.240427+0800	hootowl	nw_protocol_tcp_notify [C1.1.1.1:3] nw_protocol_notification_type_connection_idle is true
default	09:45:33.240443+0800	hootowl	nw_protocol_tcp_set_connection_idle [C1.1.1.1:3] os_nexus_flow_set_connection_idle returned 0
default	09:45:33.240966+0800	hootowl	[C1] event: client:connection_idle @10.254s
default	09:45:33.241017+0800	hootowl	Task <4AEBF80A-C0C0-4A75-A035-DF07743AA658>.<7> finished successfully
default	09:45:33.241039+0800	hootowl	nw_protocol_tcp_notify [C1.1.1.1:3] nw_protocol_notification_type_connection_idle is true
default	09:45:33.241079+0800	hootowl	nw_protocol_tcp_set_connection_idle [C1.1.1.1:3] os_nexus_flow_set_connection_idle returned 0
default	09:45:33.272448+0800	hootowl	81	doTransfer(source:)	1756
default	09:45:33.292515+0800	hootowl	Mu1Base+Ext 690
WgsNoPre(dyanmic)mapped is 1756
fault	09:45:33.326204+0800	hootowl	Publishing changes from background threads is not allowed; make sure to publish values from the main thread (via operators like receive(on:)) on model updates.
default	09:45:33.326210+0800	hootowl	MncplCyclopsScreen 166
🦵 uiKick received — syncing items
default	09:45:33.326214+0800	hootowl	Municipal+Cyclops 93
🎨 model refreshed — obs:8s car:0 thread:BG 🆔 8064324136773232350
default	09:45:33.326216+0800	hootowl	MncplCyclopsScreen 78
🏠 body eval — items:6 firstObs:8s firstCar:0
default	09:45:33.397084+0800	hootowl	TX focusApplication (peekAppEvent) stealKB:Y scene:com.sharkda.hootowl-83FF55F6-7B28-4BFD-8825-33CB43E5D162
default	09:45:33.397129+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:33.397165+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	09:45:33.397254+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1481fc400>; contextId: 0xF4D9041F
default	09:45:33.399437+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:33.511811+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:33.511828+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	09:45:33.511884+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1481fc400>; contextId: 0xF4D9041F
default	09:45:33.514178+0800	hootowl	<UIWindowScene: 0x148378200> (83FF55F6-7B28-4BFD-8825-33CB43E5D162) Scene updated orientation preferences: ( Pu ) -> ( Pu Ll Lr )
default	09:45:33.514409+0800	hootowl	<UIWindowScene: 0x148378200> (83FF55F6-7B28-4BFD-8825-33CB43E5D162) Scene updated orientation preferences: ( Pu Ll Lr ) -> ( Pu )
default	09:45:33.515635+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 1
default	09:45:33.528675+0800	hootowl	MncplCyclopsScreen 78
🏠 body eval — items:6 firstObs:8s firstCar:0
default	09:45:33.563226+0800	hootowl	MncplCyclopsScreen 78
🏠 body eval — items:6 firstObs:8s firstCar:0
default	09:45:33.592926+0800	hootowl	MncplCyclopsScreen 149
🪟 MncplCyclopsScreen onAppear — municipal 🆔 8064324136773232350
default	09:45:34.086713+0800	hootowl	TX focusApplication (peekAppEvent) stealKB:Y scene:com.sharkda.hootowl-83FF55F6-7B28-4BFD-8825-33CB43E5D162
default	09:45:34.086802+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:34.086906+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	09:45:34.087570+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1481fc400>; contextId: 0xF4D9041F
default	09:45:34.090058+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:34.202995+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:34.203020+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	09:45:34.203036+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1481fc400>; contextId: 0xF4D9041F
default	09:45:34.206043+0800	hootowl	<UIWindowScene: 0x148378200> (83FF55F6-7B28-4BFD-8825-33CB43E5D162) Scene updated orientation preferences: ( Pu ) -> ( Pu Ll Lr )
default	09:45:34.206237+0800	hootowl	<UIWindowScene: 0x148378200> (83FF55F6-7B28-4BFD-8825-33CB43E5D162) Scene updated orientation preferences: ( Pu Ll Lr ) -> ( Pu )
default	09:45:34.220132+0800	hootowl	MncplCyclopsScreen 78
🏠 body eval — items:6 firstObs:9s firstCar:0
default	09:45:34.237931+0800	hootowl	MncplCyclopsScreen 78
🏠 body eval — items:6 firstObs:9s firstCar:0
default	09:45:34.310473+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 1
default	09:45:34.357507+0800	hootowl	0x131050310 NavigationState is releasing background process assertion because a page load completed
default	09:45:34.357568+0800	hootowl	Dropping network activity on WebProcess with PID 46067
default	09:45:34.357585+0800	hootowl	0x131030420 - [PID=46067, throttler=0x131074710] ProcessThrottler::Activity::invalidate: Ending background activity / 'Page Load'
default	09:45:34.813950+0800	hootowl	TX focusApplication (peekAppEvent) stealKB:Y scene:com.sharkda.hootowl-83FF55F6-7B28-4BFD-8825-33CB43E5D162
default	09:45:34.814203+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:34.814327+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	09:45:34.814496+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1481fc400>; contextId: 0xF4D9041F
default	09:45:34.815743+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:34.944855+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:34.944885+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	09:45:34.944897+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1481fc400>; contextId: 0xF4D9041F
default	09:45:34.949270+0800	hootowl	<UIWindowScene: 0x148378200> (83FF55F6-7B28-4BFD-8825-33CB43E5D162) Scene updated orientation preferences: ( Pu ) -> ( Pu Ll Lr )
default	09:45:34.949534+0800	hootowl	<UIWindowScene: 0x148378200> (83FF55F6-7B28-4BFD-8825-33CB43E5D162) Scene updated orientation preferences: ( Pu Ll Lr ) -> ( Pu )
default	09:45:34.950911+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 1
default	09:45:34.964304+0800	hootowl	MncplCyclopsScreen 78
🏠 body eval — items:6 firstObs:9s firstCar:0
default	09:45:34.984735+0800	hootowl	MncplCyclopsScreen 78
🏠 body eval — items:6 firstObs:9s firstCar:0
default	09:45:35.016540+0800	hootowl	MncplCyclopsScreen 149
🪟 MncplCyclopsScreen onAppear — municipal 🆔 8064324136773232350
default	09:45:35.429614+0800	hootowl	tcp_input [C7.1.1.1:3] flags=[F.] seq=2245256006, ack=820731644, win=16884 state=ESTABLISHED rcv_nxt=2245256006, snd_una=820731644
default	09:45:35.429651+0800	hootowl	nw_protocol_tcp_log_summary [C7.1.1.1:3] 
	[8C2F83C9-27B2-4158-8AA7-37AB81B5FE26 192.168.50.191:50794<->61.60.98.243:443]
	Init: 1, Conn_Time: 502.789ms, SYNs: 1, WR_T: 0/0, RD_T: 0/0, TFO: 0/0/0, ECN: 0/0/1, Accurate ECN (client/server): Disabled/Disabled, TS: 1, TSO: 0
	rtt_cache: none, rtt_upd: 6, rtt: 345.843ms, rtt_var: 239.187ms rtt_nc: 345.843ms, rtt_var_nc: 239.187ms base rtt: 13ms
	ACKs-compressed: 64, ACKs delayed: 0 delayed ACKs sent: 0
default	09:45:35.429733+0800	hootowl	Connection 7: read-side closed
default	09:45:35.429764+0800	hootowl	Connection 7: cleaning up
default	09:45:35.429797+0800	hootowl	[C7 B9B949F5-0712-4ED6-BFEC-38E741D950D0 data.ntpc.gov.tw:443 quic-connection, url: https://data.ntpc.gov.tw/api/datasets/e09b35a5-a738-48cc-b0f5-570b67ad9c78/csv/file, definite, attribution: developer] cancel
default	09:45:35.429934+0800	hootowl	[C7 B9B949F5-0712-4ED6-BFEC-38E741D950D0 data.ntpc.gov.tw:443 quic-connection, url: https://data.ntpc.gov.tw/api/datasets/e09b35a5-a738-48cc-b0f5-570b67ad9c78/csv/file, definite, attribution: developer] cancelled
	[C7.1.1.1 35A9D9F9-1DE0-4B86-B8FA-EA827DD9D855 192.168.50.191:50794<->61.60.98.243:443]
	Connected Path: satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good
	Privacy Stance: Not Eligible
	Duration: 9.837s, DNS @0.068s took 0.315s, TCP @0.561s took 0.503s,  took 1.583s
	bytes in/out: 412192/3889, packets in/out: 144/108, rtt: 0.345s, retransmitted bytes: 1525, out-of-order bytes: 38164
	ecn packets sent/acked/marked/lost: 5/5/0/2
default	09:45:35.430495+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C7] reporting state cancelled
default	09:45:35.430501+0800	hootowl	Connection 7: done
default	09:45:35.430639+0800	hootowl	tcp_output [C7.1.1.1:3] flags=[F.] seq=820731675, ack=2245256007, win=2318 state=LAST_ACK rcv_nxt=2245256007, snd_una=820731644
default	09:45:35.441603+0800	hootowl	tcp_close [C7.1.1.1:3] TCP Packets:
	 snd    0.000s seq  820731644:820731644  ack 2245201178 win 2318  len 0    [.]
	 rcv    0.004s seq 2245201178:2245216712 ack 820731644  win 16884 len 15534 [P.] ECT0
	 snd    0.000s seq  820731644:820731644  ack 2245216712 win 2076  len 0    [.]
	 rcv    0.000s seq 2245216712:2245221053 ack 820731644  win 16884 len 4341 [P.] ECT0
	 snd    0.000s seq  820731644:820731644  ack 2245221053 win 2009  len 0    [.]
	 snd    0.000s seq  820731644:820731644  ack 2245221053 win 2318  len 0    [.]
	 rcv    0.006s seq 2245221053:2245222823 ack 820731644  win 16884 len 1770 [P.] ECT0
	 snd    0.000s seq  820731644:820731644  ack 2245222823 win 2291  len 0    [.]
	 rcv    0.000s seq 2245222823:2245223933 ack 820731644  win 16884 len 1110 [.] ECT0
	 snd    0.000s seq  820731644:820731644  ack 2245223933 win 2301  len 0    [.]
	 rcv    0.010s seq 2245223933:2245231096 ack 820731644  win 16884 len 7163 [P.] ECT0
	 snd    0.000s seq  820731644:820731644  ack 2245231096 win 2207  len 0    [.]
	 snd    0.000s seq  820731644:820731644  ack 2245231096 win 2318  len 0    [.]
	 rcv    0.022s seq 2245232536:2245233976 ack 820731644  win 16884 len 1440 [.] ECT0
	 snd    0.000s seq  820731644:820731644  ack 2245231096 win 2318  len 0    [.]
	 rcv    0.000s seq 2245231096:2245232536 ack 820731644  win 16884 len 1440 [.] ECT0
	 snd    0.000s seq  820731644:820731644  ack 2245233976 win 2273  len 0    [.]
	 rcv    0.000s seq 2245234491:2245235445 ack 820731644  win 16884 len 954  [.] ECT0
	 snd    0.000s seq  820731644:820731644  ack 2245233976 win 2273  len 0    [.]
	 rcv    0.000s seq 2245233976:2245234491 ack 820731644  win 16884 len 515  [.] ECT0
	 snd    0.000s seq  820731644:820731644  ack 2245235445 win 2251  len 0    [.]
	 rcv    0.000s seq 2245235445:2245239757 ack 820731644  win 16884 len 4312 [.] ECT0
	 snd    0.000s seq  820731644:820731644  ack 2245239757 win 2184  len 0    [.]
	 rcv    0.000s seq 2245239757:2245248360 ack 820731644  win 16884 len 8603 [.] ECT0
	 snd    0.000s seq  820731644:820731644  ack 2245248360 win 2050  len 0    [.]
	 snd    0.002s seq  820731644:820731644  ack 2245248360 win 2318  len 0    [.]
	 rcv    0.000s seq 2245248360:2245250904 ack 820731644  win 16884 len 2544 [.] ECT0
	 snd    0.000s seq  820731644:820731644  ack 2245250904 win 2279  len 0    [.]
	 rcv    0.007s seq 2245250904:2245255582 ack 820731644  win 16884 len 4678 [.] ECT0
	 snd    0.000s seq  820731644:820731644  ack 2245255582 win 2245  len 0    [.]
	 snd    0.000s seq  820731644:820731644  ack 2245255582 win 2318  len 0    [.]
	 rcv    0.003s seq 2245255582:2245256006 ack 820731644  win 16884 len 424  [P.] ECT0
	 snd    0.000s seq  820731644:820731644  ack 2245256006 win 2312  len 0    [.]
	 rcv    2.982s seq 2245256006:2245256006 ack 820731644  win 16884 len 0    [.]
	 rcv    1.069s seq 2245256006:2245256007 ack 820731644  win 16884 len 0    [F.]
	 snd    0.000s seq  820731644:820731644  ack 2245256007 win 2318  len 0    [.]
	 snd    0.000s seq  820731644:820731675  ack 2245256007 win 2318  len 31   [P.] ECT0
	 snd    0.001s seq  820731675:820731676  ack 2245256007 win 2318  len 0    [F.]
	 rcv    0.010s seq 2245256007:2245256007 ack 820731644  win 16884 len 0    [.]
	 rcv    0.000s seq 2245256007:2245256007 ack 820731676  win 16915 len 0    [.]
	Last packet 0ms ago.
default	09:45:35.545425+0800	hootowl	TX focusApplication (peekAppEvent) stealKB:Y scene:com.sharkda.hootowl-83FF55F6-7B28-4BFD-8825-33CB43E5D162
default	09:45:35.545473+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:35.545492+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	09:45:35.545514+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1481fc400>; contextId: 0xF4D9041F
default	09:45:35.548619+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:35.645055+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:35.645083+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	09:45:35.645101+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1481fc400>; contextId: 0xF4D9041F
default	09:45:35.650352+0800	hootowl	<UIWindowScene: 0x148378200> (83FF55F6-7B28-4BFD-8825-33CB43E5D162) Scene updated orientation preferences: ( Pu ) -> ( Pu Ll Lr )
default	09:45:35.650419+0800	hootowl	<UIWindowScene: 0x148378200> (83FF55F6-7B28-4BFD-8825-33CB43E5D162) Scene updated orientation preferences: ( Pu Ll Lr ) -> ( Pu )
default	09:45:35.651640+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 1
default	09:45:35.669420+0800	hootowl	MncplCyclopsScreen 78
🏠 body eval — items:6 firstObs:10s firstCar:0
default	09:45:35.689342+0800	hootowl	MncplCyclopsScreen 78
🏠 body eval — items:6 firstObs:10s firstCar:0
default	09:45:35.729625+0800	hootowl	{"msg":"CLLocationManager", "event":"activity", "_cmd":"startUpdatingLocation", "self":"0x1483580a0"}
default	09:45:35.757059+0800	hootowl	{"msg":"CLLocationManager", "event":"activity", "_cmd":"startUpdatingLocation", "self":"0x1483580a0"}
default	09:45:36.195271+0800	hootowl	{"msg":"CLLocationManager", "event":"activity", "_cmd":"desiredAccuracy", "self":"0x14ca9c180"}
default	09:45:36.195353+0800	hootowl	{"msg":"CLLocationManager", "event":"activity", "_cmd":"desiredAccuracy", "self":"0x14ca9c180"}
fault	09:45:36.199940+0800	hootowl	__delegate_identifier__:Performance Diagnostics__:::____message__:{"message":"Interprocess communication on the main thread can cause non-deterministic delays.","antipattern trigger":"-[CLLocationManager authorizationStatus]","message type":"suppressable","issue type":1,"category type":17,"subcategory type":0,"show in console":"0"}'97 44 92 D8 2B 5D 39 C1 AE CF 67 84 40 DE 87 48 E4 8B 01 00 97 44 92 D8 2B 5D 39 C1 AE CF 67 84 40 DE 87 48 14 58 01 00 97 44 92 D8 2B 5D 39 C1 AE CF 67 84 40 DE 87 48 40 58 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 DC 4D 01 00 97 44 92 D8 2B 5D 39 C1 AE CF 67 84 40 DE 87 48 D4 57 01 00 97 44 92 D8 2B 5D 39 C1 AE CF 67 84 40 DE 87 48 30 57 01 00 97 44 92 D8 2B 5D 39 C1 AE CF 67 84 40 DE 87 48 9C 4D 01 00 97 44 92 D8 2B 5D 39 C1 AE CF 67 84 40 DE 87 48 A8 4C 01 00 97 44 92 D8 2B 5D 39 C1 AE CF 67 84 40 DE 87 48 20 4C 01 00 97 44 92 D8 2B 5D 39 C1 AE CF 67 84 40 DE 87 48 B4 4B 01 00 97 44 92 D8 2B 5D 39 C1 AE CF 67 84 40 DE 87 48 84 43 01 00 97 44 92 D8 2B 5D 39 C1 AE CF 67 84 40 DE 87 48 E0 49 01 00 07 74 32 85 BF 1C 31 67 98 20 93 BF 76 B6 77 55 30 80 A9 00 07 74 32 85 BF 1C 31 67 98 20 93 BF 76 B6 77 55 D0 5A 15 00 07 74 32 85 BF 1C 31 67 98 20 93 BF 76 B6 77 55 E4 56 15 00 07 74 32 85 BF 1C 31 67 98 20 93 BF 76 B6 77 55 70 7F A9 00 07 74 32 85 BF 1C 31 67 98 20 93 BF 76 B6 77 55 A8 9C 13 00 07 74 32 85 BF 1C 31 67 98 20 93 BF 76 B6 77 55 10 85 15 00 07 74 32 85 BF 1C 31 67 98 20 93 BF 76 B6 77 55 10 52 4A 00 07 74 32 85 BF 1C 31 67 98 20 93 BF 76 B6 77 55 BC AC 18 00 07 74 32 85 BF 1C 31 67 98 20 93 BF 76 B6 77 55 C8 AB 18 00 07 74 32 85 BF 1C 31 67 98 20 93 BF 76 B6 77 55 2C 9F 18 00 07 74 32 85 BF 1C 31 67 98 20 93 BF 76 B6 77 55 88 E2 15 00 07 74 32 85 BF 1C 31 67 98 20 93 BF 76 B6 77 55 B4 BB 15 00 07 74 32 85 BF 1C 31 67 98 20 93 BF 76 B6 77 55 24 AF 15 00 07 74 32 85 BF 1C 31 67 98 20 93 BF 76 B6 77 55 C8 AB 15 00 07 74 32 85 BF 1C 31 67 98 20 93 BF 76 B6 77 55 C0 A6 15 00 07 74 32 85 BF 1C 31 67 98 20 93 BF 76 B6 77 55 20 13 87 00 07 74 32 85 BF 1C 31 67 98 20 93 BF 76 B6 77 55 A4 9C 15 00 07 74 32 85 BF 1C 31 67 98 20 93 BF 76 B6 77 55 80 99 15 00 8F 1E 0B 3F AD D6 37 10 A7 90 00 93 33 59 7A B4 84 31 0C 00 8F 1E 0B 3F AD D6 37 10 A7 90 00 93 33 59 7A B4 6C B0 09 00 8F 1E 0B 3F AD D6 37 10 A7 90 00 93 33 59 7A B4 C0 1C 0B 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC D4 B6 0F 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 60 8C 0F 00 26 FA B8 14 4C 8F 3A 06 B4 5E CB A2 71 02 0D C4 6C 15 00 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 D8 21 02 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 54 48 06 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 7C 47 06 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 E4 F6 02 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 4C E5 02 00 41 11 65 E2 EE 8E 38 0E B2 54 99 77 27 39 71 E3 98 14 00 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 70 16 12 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 58 C1 08 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 70 05 03 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D F4 D0 02 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 48 CC 02 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 14 8C 36 00 26 AC 71 E6 76 15 3C 47 81 FE 51 DA CA 72 43 B5 C0 8C 36 00 0F 8D 35 B6 55 6F 3E 34 8E AA 80 AB 54 04 7D C5 1C 4C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
default	09:45:36.417684+0800	hootowl	<UIWindowScene: 0x148378200> (83FF55F6-7B28-4BFD-8825-33CB43E5D162) Scene updated orientation preferences: ( Pu ) -> ( Pu Ll Lr )
default	09:45:36.503777+0800	hootowl	TX focusApplication (peekAppEvent) stealKB:Y scene:com.sharkda.hootowl-83FF55F6-7B28-4BFD-8825-33CB43E5D162
default	09:45:36.506428+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:36.506643+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	09:45:36.506690+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1481fc400>; contextId: 0xF4D9041F
default	09:45:36.507358+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:36.507375+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:36.511801+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:36.528469+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:36.628520+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:36.628547+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	09:45:36.628566+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1481fc400>; contextId: 0xF4D9041F
default	09:45:36.629098+0800	hootowl	<UIWindowScene: 0x148378200> (83FF55F6-7B28-4BFD-8825-33CB43E5D162) Scene updated orientation preferences: ( Pu Ll Lr ) -> ( Pu )
default	09:45:36.630832+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 1
default	09:45:36.654184+0800	hootowl	MncplCyclopsScreen 149
🪟 MncplCyclopsScreen onAppear — municipal 🆔 8064324136773232350
default	09:45:37.322968+0800	hootowl	<UIWindowScene: 0x148378200> (83FF55F6-7B28-4BFD-8825-33CB43E5D162) Scene updated orientation preferences: ( Pu ) -> ( Pu Ll Lr )
default	09:45:38.445971+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:38.459906+0800	hootowl	TX focusApplication (peekAppEvent) stealKB:Y scene:com.sharkda.hootowl-83FF55F6-7B28-4BFD-8825-33CB43E5D162
default	09:45:38.460084+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:38.460108+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	09:45:38.460122+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1481fc400>; contextId: 0xF4D9041F
default	09:45:38.493036+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:38.529184+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:38.529319+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	09:45:38.529505+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1481fc400>; contextId: 0xF4D9041F
default	09:45:38.543246+0800	hootowl	<UIWindowScene: 0x148378200> (83FF55F6-7B28-4BFD-8825-33CB43E5D162) Scene updated orientation preferences: ( Pu Ll Lr ) -> ( Pu )
default	09:45:38.643119+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 1, systemGestureStateChange: 0
default	09:45:39.155913+0800	hootowl	<UIWindowScene: 0x148378200> (83FF55F6-7B28-4BFD-8825-33CB43E5D162) Scene updated orientation preferences: ( Pu ) -> ( Pu Ll Lr )
default	09:45:39.865681+0800	hootowl	TX focusApplication (peekAppEvent) stealKB:Y scene:com.sharkda.hootowl-83FF55F6-7B28-4BFD-8825-33CB43E5D162
default	09:45:39.865701+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:39.865819+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	09:45:39.866570+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1481fc400>; contextId: 0xF4D9041F
default	09:45:39.870668+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:39.950427+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:39.950473+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	09:45:39.950587+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1481fc400>; contextId: 0xF4D9041F
default	09:45:39.953567+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 1
default	09:45:39.954128+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:39.965028+0800	hootowl	<UIWindowScene: 0x148378200> (83FF55F6-7B28-4BFD-8825-33CB43E5D162) Scene updated orientation preferences: ( Pu Ll Lr ) -> ( Pu )
default	09:45:40.544306+0800	hootowl	<UIWindowScene: 0x148378200> (83FF55F6-7B28-4BFD-8825-33CB43E5D162) Scene updated orientation preferences: ( Pu ) -> ( Pu Ll Lr )
default	09:45:41.178791+0800	hootowl	TX focusApplication (peekAppEvent) stealKB:Y scene:com.sharkda.hootowl-83FF55F6-7B28-4BFD-8825-33CB43E5D162
default	09:45:41.178814+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:41.178838+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	09:45:41.179671+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1481fc400>; contextId: 0xF4D9041F
default	09:45:41.192986+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:41.313127+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:41.313261+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	09:45:41.313427+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1481fc400>; contextId: 0xF4D9041F
default	09:45:41.314791+0800	hootowl	<UIWindowScene: 0x148378200> (83FF55F6-7B28-4BFD-8825-33CB43E5D162) Scene updated orientation preferences: ( Pu Ll Lr ) -> ( Pu )
default	09:45:41.357086+0800	hootowl	WebContent[46067]: PerformanceMonitor::measurePostLoadMemoryUsage: Process was using 41829344 bytes of memory after the page load.
default	09:45:41.402290+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 1
default	09:45:42.083560+0800	hootowl	<UIWindowScene: 0x148378200> (83FF55F6-7B28-4BFD-8825-33CB43E5D162) Scene updated orientation preferences: ( Pu ) -> ( Pu Ll Lr )
default	09:45:43.301333+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:43.301539+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:43.327528+0800	hootowl	TX focusApplication (peekAppEvent) stealKB:N scene:com.sharkda.hootowl-83FF55F6-7B28-4BFD-8825-33CB43E5D162
default	09:45:43.327559+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:43.327584+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	09:45:43.327621+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1481fc400>; contextId: 0xF4D9041F
default	09:45:43.388528+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:43.389499+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:43.390036+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	09:45:43.390105+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1481fc400>; contextId: 0xF4D9041F
default	09:45:43.522917+0800	hootowl	[0x149602800] activating connection: mach=true listener=false peer=false name=com.apple.TextInput
default	09:45:43.606242+0800	hootowl	<_UIKBFeedbackGenerator: 0x153264600>: Updating mode. Haptics: supported. Haptics: enabled. Ringer: on. Sound: disabled. Mode: haptics only
default	09:45:43.649096+0800	hootowl	Reloading input views for key-window scene responder: <UITextField: 0x149781400; frame = (0 0; 205.667 34); opaque = NO; > force:N
default	09:45:43.649296+0800	hootowl	Activating connection to server: (null)
default	09:45:43.649456+0800	hootowl	server remote target <BSXPCServiceConnectionProxy<BKSKeyboardServiceClientToServerIPC>: 0x14cab5500>
default	09:45:43.649496+0800	hootowl	currently observing: YES
default	09:45:43.649830+0800	hootowl	currently observing: NO
default	09:45:43.651376+0800	hootowl	_reloadInputViewsForKeyWindowSceneResponder: 1 force: 0, fromBecomeFirstResponder: 1 (automaticKeyboard: 1, reloadIdentifier: 271CF99D-BE99-4374-9A9E-89E450B71B14)
default	09:45:43.651388+0800	hootowl	_inputViewsForResponder: <UITextField: 0x149781400; frame = (0 0; 205.667 34); opaque = NO; >, automaticKeyboard: 1, force: 0
default	09:45:43.651403+0800	hootowl	_inputViewsForResponder, found custom inputView: <(null): 0x0>, customInputViewController: <(null): 0x0>
default	09:45:43.651496+0800	hootowl	_inputViewsForResponder, found inputAccessoryView: <_TtCC7SwiftUI23InputAccessoryGeneratorP33_5C36F4A49E2E2562B910FE6399D2C51E10RootUIView: 0x149676f40; frame = {{0, 0}, {0, 0}}; alpha = 1.000000; isHidden = 0; tAMIC = 0>
default	09:45:43.651520+0800	hootowl	_inputViewsForResponder, responderRequiresKeyboard 1 (automaticKeyboardEnabled: 1, activeInstance: <(null): 0x0>, self.isOnScreen: 0, requiresKBWhenFirstResponder: 1)
default	09:45:43.651534+0800	hootowl	_inputViewsForResponder, useKeyboard 1 (allowsSystemInputView: 1, !inputView <(null): 0x0>, responderRequiresKeyboard 1)
default	09:45:43.653915+0800	hootowl	[Interface Orientation] was:Interface Unknown now:UIInterfaceOrientationPortrait reason:Using key window scene
default	09:45:43.672971+0800	hootowl	_inputViewsForResponder, found assistantVC: <UISystemInputAssistantViewController: 0x152b38000; frame = {{0, 0}, {0, 0}}> (should suppress: 0, _dontNeed: 0)
default	09:45:43.672991+0800	hootowl	_inputViewsForResponder, configuring _responderWithoutAutomaticAppearanceEnabled: <(null): 0x0> (_automaticAppearEnabled: 1)
default	09:45:43.673011+0800	hootowl	_inputViewsForResponder, useKeyboard ivs: <UIInputViewSet: 0x153265200>
default	09:45:43.673897+0800	hootowl	_inputViewsForResponder returning: <<UIInputViewSet: 0x153265200>; view = <_UIKBCompatInputView: 0x14d357480; frame = (0 0; 0 0); >; assistant = <TUISystemInputAssistantView: 0x150572d00; frame = (0 0; 0 0); hidden = YES; >; accessory = <_TtCC7SwiftUI23InputAccessoryGeneratorP33_5C36F4A49E2E2562B910FE6399D2C51E10RootUIView: 0x149676f40; frame = (0 0; 0 0); >; usesKeyClicks = NO;  >
default	09:45:43.679181+0800	hootowl	Change from input view set: (null)
default	09:45:43.679209+0800	hootowl	Change to input view set: (null)
default	09:45:43.679819+0800	hootowl	_moveGuideOffscreenAtEdge: 4
default	09:45:43.679855+0800	hootowl	changeOffsetConstants: offset is changing to {0, 0} [previous offset: {-1, -1}]
default	09:45:43.679995+0800	hootowl	changeSizingConstants: size is changing [not transitioning] to {393, 0} [previous size: {1, 0}]
default	09:45:43.680645+0800	hootowl	currently observing: YES
default	09:45:43.680763+0800	hootowl	currently observing: NO
default	09:45:43.680824+0800	hootowl	-_teardownExistingDelegate:(nil) forSetDelegate:<UITextField: 0x149781400> force:NO delayEndInputSession:YES
default	09:45:43.684422+0800	hootowl	endInputSession completion is disabled
default	09:45:43.685055+0800	hootowl	Handling responseContextDidChange - existing: (null), new: (null)
error	09:45:43.707007+0800	hootowl	UIKeyboardLayoutStar implements focusItemsInRect: - caching for linear focus movement is limited as long as this view is on screen.
default	09:45:43.720973+0800	hootowl	<TUIKeyplaneView: 0x153372800> changed keyplane size to {393, 216}; docked
default	09:45:43.721117+0800	hootowl	Setting dynamic keyplane: Dynamic-Cangjie-QWERTY-Small_Small-Letters-Small-Display
default	09:45:43.723865+0800	hootowl	Requesting calls from host
default	09:45:43.723927+0800	hootowl	[0x1532921c0] activating connection: mach=true listener=false peer=false name=com.apple.callkit.callcontrollerhost
default	09:45:43.725215+0800	hootowl	Received requested calls from host: (
)
default	09:45:43.736356+0800	hootowl	channel:CandidateBar signal:Reset uniqueStringId:(null) creationTimestamp:810265543.736188 timestamp:810265543.736261 payload:(null)
default	09:45:43.736551+0800	hootowl	[0x149560140] activating connection: mach=true listener=false peer=false name=com.apple.inputanalyticsd
default	09:45:43.737018+0800	hootowl	[0x1495617c0] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.pasted
default	09:45:43.739619+0800	hootowl	-[TUIKeyboardCandidateMultiplexer installGeneratorForSource:]_block_invoke: Multiplexer is installing generator for source: 1
default	09:45:43.739634+0800	hootowl	-[TUIKeyboardCandidateMultiplexer installGeneratorForSource:]_block_invoke: Multiplexer is installing generator for source: 2
default	09:45:43.739748+0800	hootowl	Creating a new RTI client
default	09:45:43.739814+0800	hootowl	[C:3] Alloc com.apple.inputservice.input-ui-host
default	09:45:43.739847+0800	hootowl	[0x149562940] activating connection: mach=false listener=false peer=false name=(anonymous)
default	09:45:43.740045+0800	hootowl	creating new AutofillUI connection
default	09:45:43.740087+0800	hootowl	[0x149561cc0] activating connection: mach=true listener=false peer=false name=com.apple.rti-screencontinuity
default	09:45:43.740286+0800	hootowl	-[RTIInputSystemClient beginAllowingRemoteTextInput:]  Begin allowing remote text input: 311756FE-E472-4053-B1A1-580865B63F96
default	09:45:43.740304+0800	hootowl	-[RTIInputSystemClient _modifyTextEditingAllowedForReason:notify:animated:modifyAllowancesBlock:completion:]  Text editing allowed did change (editingAllowedAfter = YES)
default	09:45:43.741030+0800	hootowl	-[RTIInputSystemClient _beginSessionWithID:forServices:force:]  Begin text input session. sessionID = 311756FE-E472-4053-B1A1-580865B63F96, options = <RTISessionOptions: 0x1521e32c0; shouldResign = NO; animated = YES; offscreenDirection = 0; enhancedWindowingModeEnabled = NO
default	09:45:43.750296+0800	hootowl	-[TUIKeyboardCandidateMultiplexer installGeneratorForSource:]_block_invoke: Multiplexer is installing generator for source: 4
default	09:45:43.750566+0800	hootowl	-[TUIKeyboardCandidateMultiplexer installGeneratorForSource:]_block_invoke: Multiplexer is installing generator for source: 3
default	09:45:43.750802+0800	hootowl	-[TUIKeyboardCandidateMultiplexer installGeneratorForSource:]_block_invoke: Multiplexer is installing generator for source: 5
default	09:45:43.756964+0800	hootowl	Document state contextBeforeInput length is zero.
default	09:45:43.756972+0800	hootowl	Cancelled smart reply generation due to nil ICH
default	09:45:43.756974+0800	hootowl	Cancelled Smart Reply generateCandidates
default	09:45:43.757086+0800	hootowl	All generators are not complete.
default	09:45:43.757111+0800	hootowl	All generators are not complete.
default	09:45:43.759351+0800	hootowl	Document state contextBeforeInput length is zero.
default	09:45:43.759361+0800	hootowl	Cancelled smart reply generation due to nil ICH
default	09:45:43.759370+0800	hootowl	Cancelled Smart Reply generateCandidates
default	09:45:43.759735+0800	hootowl	All generators are not complete.
default	09:45:43.759804+0800	hootowl	All generators are not complete.
error	09:45:43.762761+0800	hootowl	Received external candidate resultset. Total number of candidates: 0
default	09:45:43.762790+0800	hootowl	All generators are not complete.
default	09:45:43.766841+0800	hootowl	KeyboardTrackingCoordinator: Creating tracking coordinator for <UIWindowScene: 0x148378200; role: UIWindowSceneSessionRoleApplication; persistentIdentifier: 83FF55F6-7B28-4BFD-8825-33CB43E5D162; activationState: UISceneActivationStateForegroundActive>
default	09:45:43.768796+0800	hootowl	App is being debugged, do not track this hang
default	09:45:43.768834+0800	hootowl	Hang detected: 0.38s (debugger attached, not reporting)
default	09:45:43.769841+0800	hootowl	Document state contextBeforeInput length is zero.
default	09:45:43.770493+0800	hootowl	Cancelled smart reply generation due to nil ICH
default	09:45:43.770500+0800	hootowl	Cancelled Smart Reply generateCandidates
default	09:45:43.770528+0800	hootowl	All generators are not complete.
default	09:45:43.770631+0800	hootowl	All generators are not complete.
error	09:45:43.770648+0800	hootowl	Received external candidate resultset. Total number of candidates: 0
default	09:45:43.770730+0800	hootowl	All generators are not complete.
default	09:45:43.774153+0800	hootowl	TX setWindowContextID:0 windowState:Disabled level:5.0
    focusContext:<contextID:4107863071 sceneID:com.sharkda.hootowl-83FF55F6-7B28-4BFD-8825-33CB43E5D162>
default	09:45:43.774533+0800	hootowl	endPlacementForInputViewSet: <<UIInputViewSet: 0x153265200>; keyboard = <UIKeyboardAutomatic: 0x15306f480; frame = (0 0; 0 0); opaque = NO; layer = <CALayer: 0x14ca73630>>%; assistant = <TUISystemInputAssistantView: 0x150572d00; frame = (0 0; 0 0); hidden = YES; >; accessory = <_TtCC7SwiftUI23InputAccessoryGeneratorP33_5C36F4A49E2E2562B910FE6399D2C51E10RootUIView: 0x149676f40; frame = (0 0; 0 0); >; usesKeyClicks = NO;  > windowScene: <UIWindowScene: 0x148378200; role: UIWindowSceneSessionRoleApplication; persistentIdentifier: 83FF55F6-7B28-4BFD-8825-33CB43E5D162; activationState: UISceneActivationStateForegroundActive>
default	09:45:43.774641+0800	hootowl	endPlacementForInputViewSet, returning -> <UIInputViewSetPlacementOnScreenWithAccessory>
fault	09:45:43.776334+0800	hootowl	Invalid frame dimension (negative or non-finite).
default	09:45:43.776971+0800	hootowl	-[_UIRemoteKeyboards prepareToMoveKeyboard:withIAV:isIAVRelevant:showing:notifyRemote:forScene:] position: {{0, 0}, {393, 325}} visible: 1; notifyRemote: 1; isMinimized: NO
default	09:45:43.777123+0800	hootowl	Should send trait collection or coordinate space update, interface style 1 -> 1, <_UIKeyboardWindowScene: 0x1533f8000> (23B762E6-7AF8-43A0-B7F3-84DA7955C122)
default	09:45:43.777148+0800	hootowl	Should send trait collection or coordinate space update, interface style 1 -> 1, <_UIKeyboardWindowScene: 0x1533f8000> (23B762E6-7AF8-43A0-B7F3-84DA7955C122)
default	09:45:43.777380+0800	hootowl	Initializing: <_UIHomeAffordanceSceneNotifierProxy: 0x1521f4de0>; with scene: <_UIKeyboardWindowScene: 0x1533f8000>
default	09:45:43.778237+0800	hootowl	Change from input view set: (null)
default	09:45:43.778265+0800	hootowl	Change to input view set: (null)
default	09:45:43.778352+0800	hootowl	Realizing settings extension <_UIApplicationSceneDisplaySettings> on FBSSceneSettings
default	09:45:43.778812+0800	hootowl	Change from input view set: (null)
default	09:45:43.778836+0800	hootowl	Change to input view set: <<UIInputViewSet: 0x153267e40>; (empty)>
default	09:45:43.787126+0800	hootowl	nw_path_evaluator_start [91F6FEA6-24E6-45E8-803A-039328F3703E <NULL> generic, multipath service: handover, attribution: developer]
	path: satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good
default	09:45:43.787336+0800	hootowl	[0x152b64140] activating connection: mach=true listener=false peer=false name=com.apple.SystemConfiguration.NetworkInformation
default	09:45:43.791352+0800	hootowl	updatePlacementWithPlacement: <UITrackingElementPlacementInitialPosition>
default	09:45:43.792845+0800	hootowl	prepareToMoveKeyboard: set currentKeyboard:Y
default	09:45:43.814161+0800	hootowl	TX signalKeyboardChanged
default	09:45:43.814184+0800	hootowl	-[_UIRemoteKeyboards signalToProxyKeyboardChanged:onCompletion:]  Signaling keyboard changed <<<_UIKeyboardChangedInformation: 0x152b1d500>; appId (null) bundleId (null) animation fence <BKSAnimationFenceHandle:0x149988df0 -> <CAFenceHandle:0x15334ac30 name=2c fence=4b00003c8e usable=YES>>; position {{0, 527}, {393, 325}}; animated YES; on screen YES; tracking NO; resizing NO; local NO, dock state: Unknown, hasValidNotif: NO>; source canvas com.apple.frontboard.systemappservices/FBSceneManager:sceneID%3Acom.sharkda.hootowl-83FF55F6-7B28-4BFD-8825-33CB43E5D162; source display Main; source bundle com.sharkda.hootowl; host bundle (null); animation fence <BKSAnimationFenceHandle:0x149988df0 -> <CAFenceHandle:0x15334ac30 name=2c fence=4b00003c8e usable=YES>>; position {{0, 527}, {393, 325}} (with IAV {{0, 479}, {393, 373}}); floating 0; on screen YES;  intersectable YES; snapshot YES>
default	09:45:43.814220+0800	hootowl	TX setWindowContextID:201872809 windowState:Enabled level:5.0
    focusContext:<contextID:4107863071 sceneID:com.sharkda.hootowl-83FF55F6-7B28-4BFD-8825-33CB43E5D162>
default	09:45:43.814274+0800	hootowl	Show keyboard with visual mode windowed (0)
default	09:45:43.814810+0800	hootowl	Setting input views: <<UIInputViewSet: 0x14a3c4f00>; keyboard = [uninitialized]; assistant = <TUISystemInputAssistantView: 0x150572d00; frame = (0 0; 0 0); hidden = YES; >; accessory = <_UIRemoteKeyboardPlaceholderView: 0x1530f9a00; frame = (0 0; 0 0); >; usesKeyClicks = NO;  >
default	09:45:43.819175+0800	hootowl	endPlacementForInputViewSet: <<UIInputViewSet: 0x14a3c4f00>; keyboard = <UIKeyboardAutomatic: 0x15306f480; frame = (0 0; 0 0); opaque = NO; layer = <CALayer: 0x14ca73630>>%; assistant = <TUISystemInputAssistantView: 0x150572d00; frame = (0 0; 0 0); >; accessory = <_UIRemoteKeyboardPlaceholderView: 0x1530f9a00; frame = (0 0; 0 0); >; usesKeyClicks = NO;  > windowScene: <_UIKeyboardWindowScene: 0x1533f8000; role: _UIScreenBasedSceneSession; persistentIdentifier: 23B762E6-7AF8-43A0-B7F3-84DA7955C122; activationState: UISceneActivationStateForegroundActive>
default	09:45:43.819601+0800	hootowl	endPlacementForInputViewSet, returning -> <UIInputViewSetPlacementOnScreenWithAccessory>
default	09:45:43.819621+0800	hootowl	Moving from placement: <UITrackingElementPlacementInitialPosition> to placement: <UIInputViewSetPlacementOnScreenWithAccessory> (currentPlacement: <UITrackingElementPlacementInitialPosition>)
default	09:45:43.820039+0800	hootowl	Change from input view set: <<UIInputViewSet: 0x153267e40>; (empty)>
default	09:45:43.820200+0800	hootowl	Change to input view set: <<UIInputViewSet: 0x14a3c4f00>; keyboard = <UIKeyboardAutomatic: 0x15306f480; frame = (0 0; 0 0); opaque = NO; layer = <CALayer: 0x14ca73630>>%; assistant = <TUISystemInputAssistantView: 0x150572d00; frame = (0 0; 0 0); >; accessory = <_UIRemoteKeyboardPlaceholderView: 0x1530f9a00; frame = (0 0; 0 0); >; usesKeyClicks = NO;  >
default	09:45:43.820235+0800	hootowl	<_UIKBFeedbackGenerator: 0x153264600>: -[_UIKBFeedbackGenerator activateWithCompletionBlock:]
default	09:45:43.820276+0800	hootowl	<_UIKBFeedbackGenerator: 0x153264600>: Releasing engine and players.
default	09:45:43.820283+0800	hootowl	<_UIKBFeedbackGenerator: 0x153264600>: Recreating engine with reason -[_UIKBFeedbackGenerator activateWithCompletionBlock:]_block_invoke_4.
default	09:45:43.821712+0800	hootowl	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	09:45:43.821729+0800	hootowl	[0x15329ea80] activating connection: mach=false listener=false peer=false name=com.apple.audio.AudioConverterService.HighCapacity
default	09:45:43.821753+0800	hootowl	        CHHapticEngine.mm:1532  -[CHHapticEngine initWithAudioSession:sessionIsShared:options:error:]: Creating engine 0x151024a80 with unshared audio session 0x0
default	09:45:43.823012+0800	hootowl	[0x1496008c0] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	09:45:43.823765+0800	hootowl	endPlacementForInputViewSet: <<UIInputViewSet: 0x14a3c4f00>; keyboard = <UIKeyboardAutomatic: 0x15306f480; frame = (0 0; 0 0); opaque = NO; layer = <CALayer: 0x14ca73630>>%; assistant = <TUISystemInputAssistantView: 0x150572d00; frame = (0 0; 0 0); >; accessory = <_UIRemoteKeyboardPlaceholderView: 0x1530f9a00; frame = (0 0; 0 0); >; usesKeyClicks = NO;  > windowScene: <_UIKeyboardWindowScene: 0x1533f8000; role: _UIScreenBasedSceneSession; persistentIdentifier: 23B762E6-7AF8-43A0-B7F3-84DA7955C122; activationState: UISceneActivationStateForegroundActive>
default	09:45:43.823893+0800	hootowl	endPlacementForInputViewSet, returning -> <UIInputViewSetPlacementOnScreenWithAccessory>
default	09:45:43.823936+0800	hootowl	    SessionCore_Create.mm:99    Created session 0x14998b7e0 with ID: 0x77c67d6
default	09:45:43.824246+0800	hootowl	endPlacementForInputViewSet: <<UIInputViewSet: 0x14a3c4f00>; keyboard = <UIKeyboardAutomatic: 0x15306f480; frame = (0 0; 0 0); opaque = NO; layer = <CALayer: 0x14ca73630>>%; assistant = <TUISystemInputAssistantView: 0x150572d00; frame = (0 0; 0 0); >; accessory = <_UIRemoteKeyboardPlaceholderView: 0x1530f9a00; frame = (0 0; 0 0); >; usesKeyClicks = NO;  > windowScene: <_UIKeyboardWindowScene: 0x1533f8000; role: _UIScreenBasedSceneSession; persistentIdentifier: 23B762E6-7AF8-43A0-B7F3-84DA7955C122; activationState: UISceneActivationStateForegroundActive>
default	09:45:43.824330+0800	hootowl	endPlacementForInputViewSet, returning -> <UIInputViewSetPlacementOnScreenWithAccessory>
error	09:45:43.824419+0800	hootowl	Received external candidate resultset. Total number of candidates: 17
default	09:45:43.824517+0800	hootowl	All generators are not complete.
default	09:45:43.824623+0800	hootowl	<<<< AVInputDeviceDiscoverySession >>>> -[AVInputDeviceDiscoverySession setFastDiscoveryEnabled:]: called (session=0x150436000, setFastDiscoveryEnabled=NO)
default	09:45:43.824646+0800	hootowl	endPlacementForInputViewSet: <<UIInputViewSet: 0x14a3c4f00>; keyboard = <UIKeyboardAutomatic: 0x15306f480; frame = (0 0; 0 0); opaque = NO; layer = <CALayer: 0x14ca73630>>%; assistant = <TUISystemInputAssistantView: 0x150572d00; frame = (0 0; 0 0); >; accessory = <_UIRemoteKeyboardPlaceholderView: 0x1530f9a00; frame = (0 0; 0 0); >; usesKeyClicks = NO;  > windowScene: <_UIKeyboardWindowScene: 0x1533f8000; role: _UIScreenBasedSceneSession; persistentIdentifier: 23B762E6-7AF8-43A0-B7F3-84DA7955C122; activationState: UISceneActivationStateForegroundActive>
default	09:45:43.824670+0800	hootowl	<<<< AVInputDeviceDiscoverySession (FigRouteDiscoverer) >>>> -[AVFigRouteDiscovererInputDeviceDiscoverySessionImpl inputDeviceDiscoverySessionFastDiscoveryDidChange:]: Setting fastDiscoveryEnabled to NO (client: hootowl) for session=0x153190150
default	09:45:43.824907+0800	hootowl	endPlacementForInputViewSet, returning -> <UIInputViewSetPlacementOnScreenWithAccessory>
default	09:45:43.824919+0800	hootowl	<<<< AVOutputDeviceDiscoverySession >>>> -[AVOutputDeviceDiscoverySession setFastDiscoveryEnabled:]: called (session=0x14c3845c0, setFastDiscoveryEnabled=NO)
default	09:45:43.824989+0800	hootowl	<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> -[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl outputDeviceDiscoverySessionFastDiscoveryDidChange:]: Setting fastDiscoveryEnabled to NO (client: hootowl) for session=0x14c3845c0
default	09:45:43.825282+0800	hootowl	endPlacementForInputViewSet: <<UIInputViewSet: 0x14a3c4f00>; keyboard = <UIKeyboardAutomatic: 0x15306f480; frame = (0 0; 0 0); opaque = NO; layer = <CALayer: 0x14ca73630>>%; assistant = <TUISystemInputAssistantView: 0x150572d00; frame = (0 0; 0 0); >; accessory = <_UIRemoteKeyboardPlaceholderView: 0x1530f9a00; frame = (0 0; 0 0); >; usesKeyClicks = NO;  > windowScene: <_UIKeyboardWindowScene: 0x1533f8000; role: _UIScreenBasedSceneSession; persistentIdentifier: 23B762E6-7AF8-43A0-B7F3-84DA7955C122; activationState: UISceneActivationStateForegroundActive>
default	09:45:43.825953+0800	hootowl	endPlacementForInputViewSet, returning -> <UIInputViewSetPlacementOnScreenWithAccessory>
default	09:45:43.827517+0800	hootowl	    AVAudioSession_iOS.mm:3459  enableNotifications: inValue = 0
default	09:45:43.828608+0800	hootowl	[0x153292580] activating connection: mach=true listener=false peer=false name=com.apple.audio.hapticd
default	09:45:43.828623+0800	hootowl	[0x153290dc0] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
default	09:45:43.829684+0800	hootowl	endPlacementForInputViewSet: <<UIInputViewSet: 0x14a3c4f00>; keyboard = <UIKeyboardAutomatic: 0x15306f480; frame = (0 0; 0 0); opaque = NO; layer = <CALayer: 0x14ca73630>>%; assistant = <TUISystemInputAssistantView: 0x150572d00; frame = (0 0; 0 0); >; accessory = <_UIRemoteKeyboardPlaceholderView: 0x1530f9a00; frame = (0 0; 0 0); >; usesKeyClicks = NO;  > windowScene: <_UIKeyboardWindowScene: 0x1533f8000; role: _UIScreenBasedSceneSession; persistentIdentifier: 23B762E6-7AF8-43A0-B7F3-84DA7955C122; activationState: UISceneActivationStateForegroundActive>
default	09:45:43.829746+0800	hootowl	    HapticServerConfig.mm:40    -[HapticServerConfig initWithHapticPlayer:withOptions:error:]: Querying server for capabilities with 'FullGamut' Locality
default	09:45:43.829984+0800	hootowl	    HapticServerConfig.mm:64    -[HapticServerConfig initWithHapticPlayer:withOptions:error:]: Querying server for capabilities with Priority 'LowPriority'
default	09:45:43.830061+0800	hootowl	    HapticServerConfig.mm:88    -[HapticServerConfig initWithHapticPlayer:withOptions:error:]: Querying server for capabilities with HapticPowerUsage 'LowPower'
default	09:45:43.830089+0800	hootowl	endPlacementForInputViewSet, returning -> <UIInputViewSetPlacementOnScreenWithAccessory>
default	09:45:43.830101+0800	hootowl	    HapticServerConfig.mm:106   -[HapticServerConfig initWithHapticPlayer:withOptions:error:]: Querying server for UsageCategory of 'iOSKeyboard'
default	09:45:43.830391+0800	hootowl	        AVHapticPlayer.mm:313   -[AVHapticPlayer queryServerCapabilities:reply:]: clientID: 0x100b3dd
default	09:45:43.830904+0800	hootowl	endPlacementForInputViewSet: <<UIInputViewSet: 0x14a3c4f00>; keyboard = <UIKeyboardAutomatic: 0x15306f480; frame = (0 0; 0 0); opaque = NO; layer = <CALayer: 0x14ca73630>>%; assistant = <TUISystemInputAssistantView: 0x150572d00; frame = (0 0; 0 0); >; accessory = <_UIRemoteKeyboardPlaceholderView: 0x1530f9a00; frame = (0 0; 0 0); >; usesKeyClicks = NO;  > windowScene: <_UIKeyboardWindowScene: 0x1533f8000; role: _UIScreenBasedSceneSession; persistentIdentifier: 23B762E6-7AF8-43A0-B7F3-84DA7955C122; activationState: UISceneActivationStateForegroundActive>
default	09:45:43.831226+0800	hootowl	endPlacementForInputViewSet, returning -> <UIInputViewSetPlacementOnScreenWithAccessory>
default	09:45:43.832739+0800	hootowl	endPlacementForInputViewSet: <<UIInputViewSet: 0x14a3c4f00>; keyboard = <UIKeyboardAutomatic: 0x15306f480; frame = (0 0; 0 0); opaque = NO; layer = <CALayer: 0x14ca73630>>%; assistant = <TUISystemInputAssistantView: 0x150572d00; frame = (0 0; 0 0); >; accessory = <_UIRemoteKeyboardPlaceholderView: 0x1530f9a00; frame = (0 0; 0 0); >; usesKeyClicks = NO;  > windowScene: <_UIKeyboardWindowScene: 0x1533f8000; role: _UIScreenBasedSceneSession; persistentIdentifier: 23B762E6-7AF8-43A0-B7F3-84DA7955C122; activationState: UISceneActivationStateForegroundActive>
default	09:45:43.833360+0800	hootowl	endPlacementForInputViewSet, returning -> <UIInputViewSetPlacementOnScreenWithAccessory>
default	09:45:43.833611+0800	hootowl	endPlacementForInputViewSet: <<UIInputViewSet: 0x14a3c4f00>; keyboard = <UIKeyboardAutomatic: 0x15306f480; frame = (0 0; 0 0); opaque = NO; layer = <CALayer: 0x14ca73630>>%; assistant = <TUISystemInputAssistantView: 0x150572d00; frame = (0 0; 0 0); >; accessory = <_UIRemoteKeyboardPlaceholderView: 0x1530f9a00; frame = (0 0; 0 0); >; usesKeyClicks = NO;  > windowScene: <_UIKeyboardWindowScene: 0x1533f8000; role: _UIScreenBasedSceneSession; persistentIdentifier: 23B762E6-7AF8-43A0-B7F3-84DA7955C122; activationState: UISceneActivationStateForegroundActive>
default	09:45:43.833770+0800	hootowl	endPlacementForInputViewSet, returning -> <UIInputViewSetPlacementOnScreenWithAccessory>
default	09:45:43.838373+0800	hootowl	        CHHapticEngine.mm:879   -[CHHapticEngine updateEngineBehavior]: Setting player's behavior to 0x0
default	09:45:43.838396+0800	hootowl	        AVHapticPlayer.mm:323   -[AVHapticPlayer setBehavior:error:]: clientID: 0x100b3dd behavior: 0
default	09:45:43.838476+0800	hootowl	        CHHapticEngine.mm:879   -[CHHapticEngine updateEngineBehavior]: Setting player's behavior to 0x4
default	09:45:43.838496+0800	hootowl	        AVHapticPlayer.mm:323   -[AVHapticPlayer setBehavior:error:]: clientID: 0x100b3dd behavior: 4
default	09:45:43.839723+0800	hootowl	moveFromPlacement, updated placements from: <UITrackingElementPlacementInitialPosition>, to: <UIInputViewSetPlacementOnScreenWithAccessory>
default	09:45:43.840094+0800	hootowl	updatePlacementWithPlacement: <UIInputViewSetPlacementOnScreenWithAccessory>
default	09:45:43.840267+0800	hootowl	endPlacementForInputViewSet: <<UIInputViewSet: 0x14a3c4f00>; keyboard = <UIKeyboardAutomatic: 0x15306f480; frame = (0 0; 393 233); opaque = NO; layer = <CALayer: 0x14ca73630>>%; assistant = <TUISystemInputAssistantView: 0x150572d00; frame = (0 0; 393 45); >; accessory = <_UIRemoteKeyboardPlaceholderView: 0x1530f9a00; frame = (0 0; 393 0); >; usesKeyClicks = NO;  > windowScene: <_UIKeyboardWindowScene: 0x1533f8000; role: _UIScreenBasedSceneSession; persistentIdentifier: 23B762E6-7AF8-43A0-B7F3-84DA7955C122; activationState: UISceneActivationStateForegroundActive>
default	09:45:43.841248+0800	hootowl	endPlacementForInputViewSet, returning -> <UIInputViewSetPlacementOnScreenWithAccessory>
default	09:45:43.841330+0800	hootowl	<_UIKBFeedbackGenerator: 0x153264600>: Creating engine with mode: haptics only.
default	09:45:43.841376+0800	hootowl	endPlacementForInputViewSet: <<UIInputViewSet: 0x14a3c4f00>; keyboard = <UIKeyboardAutomatic: 0x15306f480; frame = (0 0; 393 233); opaque = NO; layer = <CALayer: 0x14ca73630>>%; assistant = <TUISystemInputAssistantView: 0x150572d00; frame = (0 0; 393 45); >; accessory = <_UIRemoteKeyboardPlaceholderView: 0x1530f9a00; frame = (0 0; 393 0); >; usesKeyClicks = NO;  > windowScene: <_UIKeyboardWindowScene: 0x1533f8000; role: _UIScreenBasedSceneSession; persistentIdentifier: 23B762E6-7AF8-43A0-B7F3-84DA7955C122; activationState: UISceneActivationStateForegroundActive>
default	09:45:43.841732+0800	hootowl	endPlacementForInputViewSet, returning -> <UIInputViewSetPlacementOnScreenWithAccessory>
default	09:45:43.842134+0800	hootowl	       ACv2Workarounds.mm:51    com.sharkda.hootowl: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	09:45:43.842387+0800	hootowl	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	09:45:43.842536+0800	hootowl	endPlacementForInputViewSet: <<UIInputViewSet: 0x14a3c4f00>; keyboard = <UIKeyboardAutomatic: 0x15306f480; frame = (0 0; 393 233); opaque = NO; layer = <CALayer: 0x14ca73630>>%; assistant = <TUISystemInputAssistantView: 0x150572d00; frame = (0 0; 393 45); >; accessory = <_UIRemoteKeyboardPlaceholderView: 0x1530f9a00; frame = (0 0; 393 0); >; usesKeyClicks = NO;  > windowScene: <_UIKeyboardWindowScene: 0x1533f8000; role: _UIScreenBasedSceneSession; persistentIdentifier: 23B762E6-7AF8-43A0-B7F3-84DA7955C122; activationState: UISceneActivationStateForegroundActive>
default	09:45:43.842561+0800	hootowl	       AudioConverter.cpp:1077  Created a new in process converter -> 0x152bdc0c0, from  1 ch,  44100 Hz, Int16 to  1 ch,  44100 Hz, Float32
default	09:45:43.842813+0800	hootowl	        AVHapticPlayer.mm:563   -[AVHapticPlayer createCustomAudioEvent:format:frames:options:reply:]: creating custom audio event: clientID: 0x100b3dd, frameCount: 197
default	09:45:43.842864+0800	hootowl	endPlacementForInputViewSet, returning -> <UIInputViewSetPlacementOnScreenWithAccessory>
default	09:45:43.843095+0800	hootowl	endPlacementForInputViewSet: <<UIInputViewSet: 0x14a3c4f00>; keyboard = <UIKeyboardAutomatic: 0x15306f480; frame = (0 0; 393 233); opaque = NO; layer = <CALayer: 0x14ca73630>>%; assistant = <TUISystemInputAssistantView: 0x150572d00; frame = (0 0; 393 45); >; accessory = <_UIRemoteKeyboardPlaceholderView: 0x1530f9a00; frame = (0 0; 393 0); >; usesKeyClicks = NO;  > windowScene: <_UIKeyboardWindowScene: 0x1533f8000; role: _UIScreenBasedSceneSession; persistentIdentifier: 23B762E6-7AF8-43A0-B7F3-84DA7955C122; activationState: UISceneActivationStateForegroundActive>
default	09:45:43.843386+0800	hootowl	endPlacementForInputViewSet, returning -> <UIInputViewSetPlacementOnScreenWithAccessory>
default	09:45:43.843611+0800	hootowl	AudioConverter -> 0x152bdc0c0: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	09:45:43.843717+0800	hootowl	AudioConverter -> 0x152bdc0c0: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	09:45:43.844835+0800	hootowl	-[_UIRemoteKeyboards prepareToMoveKeyboard:withIAV:isIAVRelevant:showing:notifyRemote:forScene:] position: {{0, 0}, {393, 336}} visible: 1; notifyRemote: 1; isMinimized: NO
default	09:45:43.844928+0800	hootowl	prepareToMoveKeyboard: set currentKeyboard:Y
error	09:45:43.845228+0800	hootowl	Reporter disconnected. { function=sendMessage, reporterID=197761769144322 }
default	09:45:43.845705+0800	hootowl	TX signalKeyboardChanged
default	09:45:43.845942+0800	hootowl	-[_UIRemoteKeyboards signalToProxyKeyboardChanged:onCompletion:]  Signaling keyboard changed <<<_UIKeyboardChangedInformation: 0x152b1c300>; appId (null) bundleId (null) animation fence <BKSAnimationFenceHandle:0x14c384cd0 -> <CAFenceHandle:0x15334a840 name=2e fence=4b00003c8e usable=YES>>; position {{0, 516}, {393, 336}}; animated YES; on screen YES; tracking NO; resizing NO; local NO, dock state: Unknown, hasValidNotif: NO>; source canvas com.apple.frontboard.systemappservices/FBSceneManager:sceneID%3Acom.sharkda.hootowl-83FF55F6-7B28-4BFD-8825-33CB43E5D162; source display Main; source bundle com.sharkda.hootowl; host bundle (null); animation fence <BKSAnimationFenceHandle:0x14c384cd0 -> <CAFenceHandle:0x15334a840 name=2e fence=4b00003c8e usable=YES>>; position {{0, 516}, {393, 336}} (with IAV {{0, 468}, {393, 384}}); floating 0; on screen YES;  intersectable YES; snapshot YES>
default	09:45:43.846726+0800	hootowl	Tracking provider: moveFromPlacement: <UITrackingElementPlacementInitialPosition> toPlacement: <UIInputViewSetPlacementOnScreenWithAccessory> update to: {{0, 516}, {393, 336}}
default	09:45:43.846750+0800	hootowl	KeyboardTrackingCoordinator: Creating tracking provider for <_UIKeyboardWindowScene: 0x1533f8000; role: _UIScreenBasedSceneSession; persistentIdentifier: 23B762E6-7AF8-43A0-B7F3-84DA7955C122; activationState: UISceneActivationStateForegroundActive>
default	09:45:43.847173+0800	hootowl	Updating tracking clients for start <TUIKeyboardTrackingCoordinator:0x149ad6080 state=<TUIKeyboardState: 0x1521e1f00 State: onscreen with input view; has IAV; is docked>; frame={{0, 516}, {393, 336}}; animation=<TUIKeyboardAnimationInfo: 0x151077440, duration: 0.38, from local keyboard, is not rotating, should animate, type: 0, notificationInfo: {
    UIKeyboardAnimationCurveUserInfoKey = 7;
    UIKeyboardAnimationDurationUserInfoKey = "0.3833";
    UIKeyboardBoundsUserInfoKey = "NSRect: {{0, 0}, {393, 336}}";
    UIKeyboardCenterBeginUserInfoKey = "NSPoint: {196.5, 852}";
    UIKeyboardCenterEndUserInfoKey = "NSPoint: {196.5, 684}";
    UIKeyboardFrameBeginUserInfoKey = "NSRect: {{0, 852}, {393, 0}}";
    UIKeyboardFrameEndUserInfoKey = "NSRect: {{0, 516}, {393, 336}}";
    UIKeyboardIsLocalUserInfoKey = 1;
}notificationsDebug: >>
default	09:45:43.847196+0800	hootowl	changeSizingConstants: size is changing [not transitioning] to {393, 336} [previous size: {1, 0}]
default	09:45:43.847214+0800	hootowl	changeOffsetConstants: offset is changing to {0, 0} [previous offset: {-1, -1}]
default	09:45:43.847383+0800	hootowl	changeSizingConstants: size is changing [not transitioning] to {393, 336} [previous size: {393, 0}]
default	09:45:43.848378+0800	hootowl	       AudioConverter.cpp:1077  Created a new in process converter -> 0x152bdf060, from  1 ch,  44100 Hz, Int16 to  1 ch,  44100 Hz, Float32
default	09:45:43.848598+0800	hootowl	        AVHapticPlayer.mm:563   -[AVHapticPlayer createCustomAudioEvent:format:frames:options:reply:]: creating custom audio event: clientID: 0x100b3dd, frameCount: 662
default	09:45:43.848793+0800	hootowl	AudioConverter -> 0x152bdf060: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	09:45:43.849152+0800	hootowl	Setting tracking element input views: <<UIInputViewSet: 0x14a3c6a00>; keyboard = [uninitialized]; accessory = <_TtCC7SwiftUI23InputAccessoryGeneratorP33_5C36F4A49E2E2562B910FE6399D2C51E10RootUIView: 0x149676f40; frame = (0 0; 0 0); >; usesKeyClicks = NO;  >
default	09:45:43.849184+0800	hootowl	endPlacementForInputViewSet: <<UIInputViewSet: 0x14a3c6a00>; keyboard = [uninitialized]; accessory = <_TtCC7SwiftUI23InputAccessoryGeneratorP33_5C36F4A49E2E2562B910FE6399D2C51E10RootUIView: 0x149676f40; frame = (0 0; 0 0); >; usesKeyClicks = NO;  > windowScene: <UIWindowScene: 0x148378200; role: UIWindowSceneSessionRoleApplication; persistentIdentifier: 83FF55F6-7B28-4BFD-8825-33CB43E5D162; activationState: UISceneActivationStateForegroundActive>
default	09:45:43.849311+0800	hootowl	endPlacementForInputViewSet, returning -> <UIInputViewSetPlacementOnScreenWithAccessory>
default	09:45:43.849376+0800	hootowl	Moving from placement: <UITrackingElementPlacementInitialPosition> to placement: <UIInputViewSetPlacementOnScreenWithAccessory> (currentPlacement: <UITrackingElementPlacementInitialPosition>)
default	09:45:43.849428+0800	hootowl	Change from input view set: (null)
default	09:45:43.849452+0800	hootowl	Change to input view set: <<UIInputViewSet: 0x14a3c6a00>; keyboard = <UIKeyboardAutomatic: 0x15306f480; frame = (0 0; 393 233); opaque = NO; layer = <CALayer: 0x14ca73630>>%; accessory = <_TtCC7SwiftUI23InputAccessoryGeneratorP33_5C36F4A49E2E2562B910FE6399D2C51E10RootUIView: 0x149676f40; frame = (0 0; 0 0); >; usesKeyClicks = NO;  >
default	09:45:43.849549+0800	hootowl	-[_UIRemoteKeyboardPlaceholderView refreshPlaceholder]  refreshPlaceholder: size={393, 336} [previous size={393, 0}]
error	09:45:43.849896+0800	hootowl	Reporter disconnected. { function=sendMessage, reporterID=197761769144322 }
default	09:45:43.850141+0800	hootowl	endPlacementForInputViewSet: <<UIInputViewSet: 0x14a3c6a00>; keyboard = <UIKeyboardAutomatic: 0x15306f480; frame = (0 0; 393 233); opaque = NO; layer = <CALayer: 0x14ca73630>>%; accessory = <_TtCC7SwiftUI23InputAccessoryGeneratorP33_5C36F4A49E2E2562B910FE6399D2C51E10RootUIView: 0x149676f40; frame = (0 0; 0 0); >; usesKeyClicks = NO;  > windowScene: <UIWindowScene: 0x148378200; role: UIWindowSceneSessionRoleApplication; persistentIdentifier: 83FF55F6-7B28-4BFD-8825-33CB43E5D162; activationState: UISceneActivationStateForegroundActive>
default	09:45:43.850500+0800	hootowl	endPlacementForInputViewSet, returning -> <UIInputViewSetPlacementOnScreenWithAccessory>
default	09:45:43.851448+0800	hootowl	AudioConverter -> 0x152bdf060: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
default	09:45:43.851788+0800	hootowl	        AVHapticPlayer.mm:575   -[AVHapticPlayer referenceCustomAudioEvent:reply:]: referencing custom audio event: clientID: 0x100b3dd
default	09:45:43.851797+0800	hootowl	[0x1532a0140] activating connection: mach=true listener=false peer=false name=com.apple.powerlog.plxpclogger.xpc
error	09:45:43.852160+0800	hootowl	Reporter disconnected. { function=sendMessage, reporterID=197761769144322 }
default	09:45:43.853806+0800	hootowl	[0x15329ea80] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	09:45:43.854629+0800	hootowl	        AVHapticPlayer.mm:575   -[AVHapticPlayer referenceCustomAudioEvent:reply:]: referencing custom audio event: clientID: 0x100b3dd
error	09:45:43.855190+0800	hootowl	Reporter disconnected. { function=sendMessage, reporterID=197761769144322 }
default	09:45:43.857717+0800	hootowl	       AudioConverter.cpp:1077  Created a new in process converter -> 0x152bddf80, from  1 ch,  44100 Hz, Int16 to  1 ch,  44100 Hz, Float32
default	09:45:43.857841+0800	hootowl	        AVHapticPlayer.mm:563   -[AVHapticPlayer createCustomAudioEvent:format:frames:options:reply:]: creating custom audio event: clientID: 0x100b3dd, frameCount: 856
default	09:45:43.858119+0800	hootowl	AudioConverter -> 0x152bddf80: The in-process SetProperty call returned 1886547824 for property 1886546285 with size 8.
default	09:45:43.858231+0800	hootowl	AudioConverter -> 0x152bddf80: The in-process SetProperty call returned 1886547824 for property 610889331 with size 4.
error	09:45:43.859496+0800	hootowl	Reporter disconnected. { function=sendMessage, reporterID=197761769144322 }
default	09:45:43.861917+0800	hootowl	        AVHapticPlayer.mm:575   -[AVHapticPlayer referenceCustomAudioEvent:reply:]: referencing custom audio event: clientID: 0x100b3dd
error	09:45:43.862478+0800	hootowl	Reporter disconnected. { function=sendMessage, reporterID=197761769144322 }
default	09:45:43.864069+0800	hootowl	        AVHapticPlayer.mm:575   -[AVHapticPlayer referenceCustomAudioEvent:reply:]: referencing custom audio event: clientID: 0x100b3dd
error	09:45:43.864501+0800	hootowl	Reporter disconnected. { function=sendMessage, reporterID=197761769144322 }
default	09:45:43.866360+0800	hootowl	        AVHapticPlayer.mm:575   -[AVHapticPlayer referenceCustomAudioEvent:reply:]: referencing custom audio event: clientID: 0x100b3dd
error	09:45:43.866997+0800	hootowl	Reporter disconnected. { function=sendMessage, reporterID=197761769144322 }
default	09:45:43.879276+0800	hootowl	        AVHapticPlayer.mm:575   -[AVHapticPlayer referenceCustomAudioEvent:reply:]: referencing custom audio event: clientID: 0x100b3dd
error	09:45:43.880688+0800	hootowl	Reporter disconnected. { function=sendMessage, reporterID=197761769144322 }
default	09:45:43.881093+0800	hootowl	<_UIKBFeedbackGenerator: 0x153264600>: Requesting engine start for reason: -[_UIKBFeedbackGenerator activateWithCompletionBlock:]_block_invoke_4
default	09:45:43.882051+0800	hootowl	        CHHapticEngine.mm:1362  -[CHHapticEngine startAndReturnError:]: Called on engine 0x151024a80
default	09:45:43.882163+0800	hootowl	        CHHapticEngine.mm:1251  -[CHHapticEngine doStartWithCompletionHandler:]: Starting underlying Haptic Player
default	09:45:43.882277+0800	hootowl	        CHHapticEngine.mm:885   -[CHHapticEngine updateEngineBehaviorWithError:]: Setting player's behavior to 0x7
default	09:45:43.882297+0800	hootowl	        AVHapticPlayer.mm:323   -[AVHapticPlayer setBehavior:error:]: clientID: 0x100b3dd behavior: 7
default	09:45:43.882446+0800	hootowl	        AVHapticPlayer.mm:675   -[AVHapticPlayer startRunningWithCompletionHandler:]: start running: clientID: 0x100b3dd
default	09:45:43.882472+0800	hootowl	        AVHapticClient.mm:363   -[AVHapticClient startRunning:]: Client 0x100b3dd starting
default	09:45:43.885586+0800	hootowl	updatePlacementWithPlacement: <UIInputViewSetPlacementOnScreenWithAccessory>
default	09:45:43.885929+0800	hootowl	changeSizingConstants: size is changing [not transitioning] to {393, 418} [previous size: {393, 336}]
default	09:45:43.886487+0800	hootowl	changeSizingConstants: size is changing [not transitioning] to {393, 350} [previous size: {393, 418}]
default	09:45:43.887129+0800	hootowl	Init Service connection: <BSServiceConnectionEndpoint: 0x1532dad20; target: NL:com.apple.AccessibilityUIServer; service: com.apple.AccessibilityUIServer>
default	09:45:43.887403+0800	hootowl	[C:4] Alloc com.apple.AccessibilityUIServer
default	09:45:43.887423+0800	hootowl	[0x149b35900] activating connection: mach=false listener=false peer=false name=(anonymous)
default	09:45:43.890074+0800	hootowl	Connection activated to <BSXPC(com.apple.AccessibilityUIServer[C:4-1])-as(com.apple.AccessibilityUIServer):0x15106e440>
default	09:45:43.890475+0800	hootowl	Posted notification willShow with {
    UIKeyboardAnimationCurveUserInfoKey = 7;
    UIKeyboardAnimationDurationUserInfoKey = "0.3833";
    UIKeyboardBoundsUserInfoKey = "NSRect: {{0, 0}, {393, 336}}";
    UIKeyboardCenterBeginUserInfoKey = "NSPoint: {196.5, 852}";
    UIKeyboardCenterEndUserInfoKey = "NSPoint: {196.5, 684}";
    UIKeyboardFrameBeginUserInfoKey = "NSRect: {{0, 852}, {393, 0}}";
    UIKeyboardFrameEndUserInfoKey = "NSRect: {{0, 468}, {393, 384}}";
    UIKeyboardIsLocalUserInfoKey = 1;
} (null); Update from coordinator for IAV bounds change to {{0, 0}, {393, 82}}; Update from coordinator for IAV bounds change to {{0, 0}, {393, 48}}
default	09:45:43.890563+0800	hootowl	All generators are not complete.
default	09:45:43.890675+0800	hootowl	All generators are not complete.
default	09:45:43.890701+0800	hootowl	All generators are complete, dispatching to `completionBlockJustOnce`
default	09:45:43.890790+0800	hootowl	Preparing to push (null) to candidate receiver, for request token: 89AD0AA0
error	09:45:43.890898+0800	hootowl	containerToPush is nil, will not push anything to candidate receiver for request token: 89AD0AA0
default	09:45:43.891022+0800	hootowl	Performing delayed generation for token=89AD0AA0
default	09:45:43.893155+0800	hootowl	ClientConnection registered client SpeakThisClientIdentifier-46045
default	09:45:44.010313+0800	hootowl	<_UIKBFeedbackGenerator: 0x153264600>: Engine started (or it was already running).
default	09:45:44.012672+0800	hootowl	Received state update for 46045 (app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>, unknown-NotVisible
default	09:45:44.013014+0800	hootowl	Received state update for 46045 (app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>, unknown-NotVisible
default	09:45:44.013267+0800	hootowl	channel:CandidateBar signal:Reset uniqueStringId:(null) creationTimestamp:810265543.761853 timestamp:810265543.784359 payload:(null)
default	09:45:44.020273+0800	hootowl	channel:LegacyTextInputActions signal:DidSessionBegin sessionID:311756FE-E472-4053-B1A1-580865B63F96 timestamp:810265543.898464 payload:{
    Class = IATextInputActionsSessionBeganAction;
    appBundleId = "com.sharkda.hootowl";
    clientSideSessionErrors = "";
    flagOptions = 0;
    inputActionCountFromMergedActions = 0;
    inputMode =     {
        inputModeIdentifier = "zh_Hant-Pinyin@sw=Pinyin-Traditional;hw=Automatic";
        keyboardLayout = "Pinyin-Traditional";
        keyboardVariant = Pinyin;
        language = zh;
        region = Hant;
    };
    insertedEmojiCount = 0;
    insertedPunctuationCount = 0;
    insertedTextLength = 0;
    largestSingleDeletionLength = 0;
    largestSingleInsertionLength = 0;
    processBundleId = "com.sharkda.hootowl";
    "relativeRangeBefore_length" = 0;
    "relativeRangeBefore_location" = 0;
    removedEmojiCount = 0;
    removedPunctuationCount = 0;
    removedTextLength = 0;
    source = 4;
    textInputActionsType = 0;
    timestamp = "810265543.743216";
}
default	09:45:44.066943+0800	hootowl	RX keyboardArbiterClientHandle:Y
default	09:45:44.111701+0800	hootowl	RX keyboardArbiterClientHandle:Y
default	09:45:44.180833+0800	hootowl	Received state update for 46045 (app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>, unknown-NotVisible
default	09:45:44.459647+0800	hootowl	TX setWindowContextID:201872809 windowState:Enabled level:5.0
    focusContext:<contextID:4107863071 sceneID:com.sharkda.hootowl-83FF55F6-7B28-4BFD-8825-33CB43E5D162>
default	09:45:44.460798+0800	hootowl	Remote touch surface type has been initialized to: Unknown
default	09:45:44.460846+0800	hootowl	Remote microphone capability has been initialized to: NO
default	09:45:44.461836+0800	hootowl	Posted notification didShow with {
    UIKeyboardAnimationCurveUserInfoKey = 7;
    UIKeyboardAnimationDurationUserInfoKey = "0.3833";
    UIKeyboardBoundsUserInfoKey = "NSRect: {{0, 0}, {393, 336}}";
    UIKeyboardCenterBeginUserInfoKey = "NSPoint: {196.5, 852}";
    UIKeyboardCenterEndUserInfoKey = "NSPoint: {196.5, 684}";
    UIKeyboardFrameBeginUserInfoKey = "NSRect: {{0, 852}, {393, 0}}";
    UIKeyboardFrameEndUserInfoKey = "NSRect: {{0, 468}, {393, 384}}";
    UIKeyboardIsLocalUserInfoKey = 1;
} (null); Update from coordinator for IAV bounds change to {{0, 0}, {393, 82}}; Update from coordinator for IAV bounds change to {{0, 0}, {393, 48}}
default	09:45:44.512671+0800	hootowl	0x148d71000 (pageProxyID=1708) -[WKWebView _updateVisibleContentRects:] - have not received a commit 12.67s after visible content rect update; lastTransactionID 0
default	09:45:45.617079+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:45.617115+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	09:45:45.617161+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIRemoteKeyboardWindow: 0x152b39900>; contextId: 0xC0855A9
default	09:45:45.707578+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:45.744374+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:45.744460+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	09:45:45.744594+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIRemoteKeyboardWindow: 0x152b39900>; contextId: 0xC0855A9
default	09:45:45.802985+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 1
default	09:45:46.359025+0800	hootowl	WebContent[46067]: PerformanceMonitor::measurePostLoadCPUUsage: Process was using 0.0% CPU after the page load.
error	09:45:46.903887+0800	hootowl	Result accumulator timeout: 3.000000, exceeded.
error	09:45:46.904155+0800	hootowl	Result accumulator timeout: 3.000000, exceeded.
default	09:45:46.904436+0800	hootowl	Could not match any valid candidates of any source. `containerToPush` will be nil. 53F7E9A5
default	09:45:46.904459+0800	hootowl	Preparing to push (null) to candidate receiver, for request token: 53F7E9A5
error	09:45:46.904551+0800	hootowl	containerToPush is nil, will not push anything to candidate receiver for request token: 53F7E9A5
default	09:45:46.904591+0800	hootowl	Could not match any valid candidates of any source. `containerToPush` will be nil. 3AEBE9BE
default	09:45:46.904680+0800	hootowl	Preparing to push (null) to candidate receiver, for request token: 3AEBE9BE
error	09:45:46.904836+0800	hootowl	containerToPush is nil, will not push anything to candidate receiver for request token: 3AEBE9BE
default	09:45:47.764297+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:47.770291+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:47.770492+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	09:45:47.770631+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1481fc400>; contextId: 0xF4D9041F
default	09:45:47.779709+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:47.810888+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:47.811435+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	09:45:47.811450+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1481fc400>; contextId: 0xF4D9041F
default	09:45:47.841377+0800	hootowl	endPlacementForInputViewSet: <<UIInputViewSet: 0x14a3c4f00>; keyboard = <UIKeyboardAutomatic: 0x15306f480; frame = (0 0; 393 233); opaque = NO; layer = <CALayer: 0x14ca73630>>%; assistant = <TUISystemInputAssistantView: 0x150572d00; frame = (0 0; 393 45); >; accessory = <_UIRemoteKeyboardPlaceholderView: 0x1530f9a00; frame = (0 0; 393 0); >; usesKeyClicks = NO;  > windowScene: <_UIKeyboardWindowScene: 0x1533f8000; role: _UIScreenBasedSceneSession; persistentIdentifier: 23B762E6-7AF8-43A0-B7F3-84DA7955C122; activationState: UISceneActivationStateForegroundActive>
default	09:45:47.841449+0800	hootowl	endPlacementForInputViewSet, returning -> <UIInputViewSetPlacementOnScreenWithAccessory>
default	09:45:47.841610+0800	hootowl	endPlacementForInputViewSet: <<UIInputViewSet: 0x14a3c4f00>; keyboard = <UIKeyboardAutomatic: 0x15306f480; frame = (0 0; 393 233); opaque = NO; layer = <CALayer: 0x14ca73630>>%; assistant = <TUISystemInputAssistantView: 0x150572d00; frame = (0 0; 393 45); >; accessory = <_UIRemoteKeyboardPlaceholderView: 0x1530f9a00; frame = (0 0; 393 0); >; usesKeyClicks = NO;  > windowScene: <_UIKeyboardWindowScene: 0x1533f8000; role: _UIScreenBasedSceneSession; persistentIdentifier: 23B762E6-7AF8-43A0-B7F3-84DA7955C122; activationState: UISceneActivationStateForegroundActive>
default	09:45:47.841733+0800	hootowl	endPlacementForInputViewSet, returning -> <UIInputViewSetPlacementOnScreenWithAccessory>
default	09:45:47.841993+0800	hootowl	endPlacementForInputViewSet: <<UIInputViewSet: 0x14a3c4f00>; keyboard = <UIKeyboardAutomatic: 0x15306f480; frame = (0 0; 393 233); opaque = NO; layer = <CALayer: 0x14ca73630>>%; assistant = <TUISystemInputAssistantView: 0x150572d00; frame = (0 0; 393 45); >; accessory = <_UIRemoteKeyboardPlaceholderView: 0x1530f9a00; frame = (0 0; 393 0); >; usesKeyClicks = NO;  > windowScene: <_UIKeyboardWindowScene: 0x1533f8000; role: _UIScreenBasedSceneSession; persistentIdentifier: 23B762E6-7AF8-43A0-B7F3-84DA7955C122; activationState: UISceneActivationStateForegroundActive>
default	09:45:47.842057+0800	hootowl	endPlacementForInputViewSet, returning -> <UIInputViewSetPlacementOnScreenWithAccessory>
default	09:45:47.842149+0800	hootowl	endPlacementForInputViewSet: <<UIInputViewSet: 0x14a3c4f00>; keyboard = <UIKeyboardAutomatic: 0x15306f480; frame = (0 0; 393 233); opaque = NO; layer = <CALayer: 0x14ca73630>>%; assistant = <TUISystemInputAssistantView: 0x150572d00; frame = (0 0; 393 45); >; accessory = <_UIRemoteKeyboardPlaceholderView: 0x1530f9a00; frame = (0 0; 393 0); >; usesKeyClicks = NO;  > windowScene: <_UIKeyboardWindowScene: 0x1533f8000; role: _UIScreenBasedSceneSession; persistentIdentifier: 23B762E6-7AF8-43A0-B7F3-84DA7955C122; activationState: UISceneActivationStateForegroundActive>
default	09:45:47.842237+0800	hootowl	endPlacementForInputViewSet, returning -> <UIInputViewSetPlacementOnScreenWithAccessory>
default	09:45:47.842457+0800	hootowl	endPlacementForInputViewSet: <<UIInputViewSet: 0x14a3c4f00>; keyboard = <UIKeyboardAutomatic: 0x15306f480; frame = (0 0; 393 233); opaque = NO; layer = <CALayer: 0x14ca73630>>%; assistant = <TUISystemInputAssistantView: 0x150572d00; frame = (0 0; 393 45); >; accessory = <_UIRemoteKeyboardPlaceholderView: 0x1530f9a00; frame = (0 0; 393 0); >; usesKeyClicks = NO;  > windowScene: <_UIKeyboardWindowScene: 0x1533f8000; role: _UIScreenBasedSceneSession; persistentIdentifier: 23B762E6-7AF8-43A0-B7F3-84DA7955C122; activationState: UISceneActivationStateForegroundActive>
default	09:45:47.842557+0800	hootowl	endPlacementForInputViewSet, returning -> <UIInputViewSetPlacementOnScreenWithAccessory>
default	09:45:47.842631+0800	hootowl	endPlacementForInputViewSet: <<UIInputViewSet: 0x14a3c4f00>; keyboard = <UIKeyboardAutomatic: 0x15306f480; frame = (0 0; 393 233); opaque = NO; layer = <CALayer: 0x14ca73630>>%; assistant = <TUISystemInputAssistantView: 0x150572d00; frame = (0 0; 393 45); >; accessory = <_UIRemoteKeyboardPlaceholderView: 0x1530f9a00; frame = (0 0; 393 0); >; usesKeyClicks = NO;  > windowScene: <_UIKeyboardWindowScene: 0x1533f8000; role: _UIScreenBasedSceneSession; persistentIdentifier: 23B762E6-7AF8-43A0-B7F3-84DA7955C122; activationState: UISceneActivationStateForegroundActive>
default	09:45:47.842698+0800	hootowl	endPlacementForInputViewSet, returning -> <UIInputViewSetPlacementOnScreenWithAccessory>
default	09:45:47.842864+0800	hootowl	endPlacementForInputViewSet: <<UIInputViewSet: 0x14a3c4f00>; keyboard = <UIKeyboardAutomatic: 0x15306f480; frame = (0 0; 393 233); opaque = NO; layer = <CALayer: 0x14ca73630>>%; assistant = <TUISystemInputAssistantView: 0x150572d00; frame = (0 0; 393 45); >; accessory = <_UIRemoteKeyboardPlaceholderView: 0x1530f9a00; frame = (0 0; 393 0); >; usesKeyClicks = NO;  > windowScene: <_UIKeyboardWindowScene: 0x1533f8000; role: _UIScreenBasedSceneSession; persistentIdentifier: 23B762E6-7AF8-43A0-B7F3-84DA7955C122; activationState: UISceneActivationStateForegroundActive>
default	09:45:47.842977+0800	hootowl	endPlacementForInputViewSet, returning -> <UIInputViewSetPlacementOnScreenWithAccessory>
default	09:45:47.843122+0800	hootowl	endPlacementForInputViewSet: <<UIInputViewSet: 0x14a3c4f00>; keyboard = <UIKeyboardAutomatic: 0x15306f480; frame = (0 0; 393 233); opaque = NO; layer = <CALayer: 0x14ca73630>>%; assistant = <TUISystemInputAssistantView: 0x150572d00; frame = (0 0; 393 45); >; accessory = <_UIRemoteKeyboardPlaceholderView: 0x1530f9a00; frame = (0 0; 393 0); >; usesKeyClicks = NO;  > windowScene: <_UIKeyboardWindowScene: 0x1533f8000; role: _UIScreenBasedSceneSession; persistentIdentifier: 23B762E6-7AF8-43A0-B7F3-84DA7955C122; activationState: UISceneActivationStateForegroundActive>
default	09:45:47.843245+0800	hootowl	endPlacementForInputViewSet, returning -> <UIInputViewSetPlacementOnScreenWithAccessory>
default	09:45:47.843408+0800	hootowl	channel:CandidateBar signal:Reset uniqueStringId:(null) creationTimestamp:810265547.843232 timestamp:810265547.843314 payload:(null)
default	09:45:47.845150+0800	hootowl	-[_UIRemoteKeyboardPlaceholderView refreshPlaceholder]  refreshPlaceholder: size={393, 336} [previous size={393, 336}]
default	09:45:47.849823+0800	hootowl	Document state contextBeforeInput length is zero.
default	09:45:47.849952+0800	hootowl	Cancelled smart reply generation due to nil ICH
default	09:45:47.849997+0800	hootowl	Cancelled Smart Reply generateCandidates
default	09:45:47.850013+0800	hootowl	All generators are not complete.
default	09:45:47.850027+0800	hootowl	All generators are not complete.
default	09:45:47.851350+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
error	09:45:47.860735+0800	hootowl	Received external candidate resultset. Total number of candidates: 17
default	09:45:47.860774+0800	hootowl	All generators are not complete.
default	09:45:47.861066+0800	hootowl	All generators are complete, dispatching to `completionBlockJustOnce`
default	09:45:47.861243+0800	hootowl	Preparing to push (null) to candidate receiver, for request token: 6321FC06
error	09:45:47.861569+0800	hootowl	containerToPush is nil, will not push anything to candidate receiver for request token: 6321FC06
default	09:45:47.861607+0800	hootowl	Performing delayed generation for token=6321FC06
default	09:45:48.112060+0800	hootowl	Retrieving pasteboard named com.apple.UIKit.pboard.general, create if needed: NO
default	09:45:48.113663+0800	hootowl	...retrieving pasteboard named com.apple.UIKit.pboard.general completed successfully.
default	09:45:48.216849+0800	hootowl	registering darwin observer for name: com.apple.gms.availability.notification
default	09:45:48.216873+0800	hootowl	registering darwin observer for name: com.apple.os-eligibility-domain.change.greymatter
default	09:45:48.216917+0800	hootowl	registering darwin observer for name: com.apple.language.changed
default	09:45:48.217001+0800	hootowl	isAvailable value changed: isMDMAllowed = true, gmAvailable (current) = true
default	09:45:48.264245+0800	hootowl	App is being debugged, do not track this hang
default	09:45:48.264261+0800	hootowl	Hang detected: 0.26s (debugger attached, not reporting)
default	09:45:48.731682+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:48.731766+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	09:45:48.731900+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIRemoteKeyboardWindow: 0x152b39900>; contextId: 0xC0855A9
default	09:45:48.731926+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:48.810940+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 1
default	09:45:48.824696+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:48.825207+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	09:45:48.825694+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIRemoteKeyboardWindow: 0x152b39900>; contextId: 0xC0855A9
default	09:45:48.831552+0800	hootowl	channel:LegacyTextInputActions signal:DidAction sessionID:311756FE-E472-4053-B1A1-580865B63F96 timestamp:810265548.831187 payload:{
    Class = IATextInputActionsSessionBeganAction;
    appBundleId = "com.sharkda.hootowl";
    clientSideSessionErrors = "";
    flagOptions = 0;
    inputActionCountFromMergedActions = 0;
    inputMode =     {
        inputModeIdentifier = "zh_Hant-Pinyin@sw=Pinyin-Traditional;hw=Automatic";
        keyboardLayout = "Pinyin-Traditional";
        keyboardVariant = Pinyin;
        language = zh;
        region = Hant;
    };
    insertedEmojiCount = 0;
    insertedPunctuationCount = 0;
    insertedTextLength = 0;
    largestSingleDeletionLength = 0;
    largestSingleInsertionLength = 0;
    processBundleId = "com.sharkda.hootowl";
    "relativeRangeBefore_length" = 0;
    "relativeRangeBefore_location" = 0;
    removedEmojiCount = 0;
    removedPunctuationCount = 0;
    removedTextLength = 0;
    source = 4;
    textInputActionsType = 0;
    timestamp = "810265543.743216";
}
default	09:45:48.839699+0800	hootowl	endPlacementForInputViewSet: <<UIInputViewSet: 0x14a3c4f00>; keyboard = <UIKeyboardAutomatic: 0x15306f480; frame = (0 0; 393 233); opaque = NO; layer = <CALayer: 0x14ca73630>>%; assistant = <TUISystemInputAssistantView: 0x150572d00; frame = (0 0; 393 45); >; accessory = <_UIRemoteKeyboardPlaceholderView: 0x1530f9a00; frame = (0 0; 393 0); >; usesKeyClicks = NO;  > windowScene: <_UIKeyboardWindowScene: 0x1533f8000; role: _UIScreenBasedSceneSession; persistentIdentifier: 23B762E6-7AF8-43A0-B7F3-84DA7955C122; activationState: UISceneActivationStateForegroundActive>
default	09:45:48.839900+0800	hootowl	endPlacementForInputViewSet, returning -> <UIInputViewSetPlacementOnScreenWithAccessory>
default	09:45:48.840226+0800	hootowl	endPlacementForInputViewSet: <<UIInputViewSet: 0x14a3c4f00>; keyboard = <UIKeyboardAutomatic: 0x15306f480; frame = (0 0; 393 233); opaque = NO; layer = <CALayer: 0x14ca73630>>%; assistant = <TUISystemInputAssistantView: 0x150572d00; frame = (0 0; 393 45); >; accessory = <_UIRemoteKeyboardPlaceholderView: 0x1530f9a00; frame = (0 0; 393 0); >; usesKeyClicks = NO;  > windowScene: <_UIKeyboardWindowScene: 0x1533f8000; role: _UIScreenBasedSceneSession; persistentIdentifier: 23B762E6-7AF8-43A0-B7F3-84DA7955C122; activationState: UISceneActivationStateForegroundActive>
default	09:45:48.840367+0800	hootowl	endPlacementForInputViewSet, returning -> <UIInputViewSetPlacementOnScreenWithAccessory>
default	09:45:48.840972+0800	hootowl	endPlacementForInputViewSet: <<UIInputViewSet: 0x14a3c4f00>; keyboard = <UIKeyboardAutomatic: 0x15306f480; frame = (0 0; 393 233); opaque = NO; layer = <CALayer: 0x14ca73630>>%; assistant = <TUISystemInputAssistantView: 0x150572d00; frame = (0 0; 393 45); >; accessory = <_UIRemoteKeyboardPlaceholderView: 0x1530f9a00; frame = (0 0; 393 0); >; usesKeyClicks = NO;  > windowScene: <_UIKeyboardWindowScene: 0x1533f8000; role: _UIScreenBasedSceneSession; persistentIdentifier: 23B762E6-7AF8-43A0-B7F3-84DA7955C122; activationState: UISceneActivationStateForegroundActive>
default	09:45:48.842068+0800	hootowl	endPlacementForInputViewSet, returning -> <UIInputViewSetPlacementOnScreenWithAccessory>
default	09:45:48.842232+0800	hootowl	endPlacementForInputViewSet: <<UIInputViewSet: 0x14a3c4f00>; keyboard = <UIKeyboardAutomatic: 0x15306f480; frame = (0 0; 393 233); opaque = NO; layer = <CALayer: 0x14ca73630>>%; assistant = <TUISystemInputAssistantView: 0x150572d00; frame = (0 0; 393 45); >; accessory = <_UIRemoteKeyboardPlaceholderView: 0x1530f9a00; frame = (0 0; 393 0); >; usesKeyClicks = NO;  > windowScene: <_UIKeyboardWindowScene: 0x1533f8000; role: _UIScreenBasedSceneSession; persistentIdentifier: 23B762E6-7AF8-43A0-B7F3-84DA7955C122; activationState: UISceneActivationStateForegroundActive>
default	09:45:48.843869+0800	hootowl	endPlacementForInputViewSet, returning -> <UIInputViewSetPlacementOnScreenWithAccessory>
default	09:45:48.844244+0800	hootowl	endPlacementForInputViewSet: <<UIInputViewSet: 0x14a3c4f00>; keyboard = <UIKeyboardAutomatic: 0x15306f480; frame = (0 0; 393 233); opaque = NO; layer = <CALayer: 0x14ca73630>>%; assistant = <TUISystemInputAssistantView: 0x150572d00; frame = (0 0; 393 45); >; accessory = <_UIRemoteKeyboardPlaceholderView: 0x1530f9a00; frame = (0 0; 393 0); >; usesKeyClicks = NO;  > windowScene: <_UIKeyboardWindowScene: 0x1533f8000; role: _UIScreenBasedSceneSession; persistentIdentifier: 23B762E6-7AF8-43A0-B7F3-84DA7955C122; activationState: UISceneActivationStateForegroundActive>
default	09:45:48.844398+0800	hootowl	endPlacementForInputViewSet, returning -> <UIInputViewSetPlacementOnScreenWithAccessory>
default	09:45:48.844497+0800	hootowl	endPlacementForInputViewSet: <<UIInputViewSet: 0x14a3c4f00>; keyboard = <UIKeyboardAutomatic: 0x15306f480; frame = (0 0; 393 233); opaque = NO; layer = <CALayer: 0x14ca73630>>%; assistant = <TUISystemInputAssistantView: 0x150572d00; frame = (0 0; 393 45); >; accessory = <_UIRemoteKeyboardPlaceholderView: 0x1530f9a00; frame = (0 0; 393 0); >; usesKeyClicks = NO;  > windowScene: <_UIKeyboardWindowScene: 0x1533f8000; role: _UIScreenBasedSceneSession; persistentIdentifier: 23B762E6-7AF8-43A0-B7F3-84DA7955C122; activationState: UISceneActivationStateForegroundActive>
default	09:45:48.844841+0800	hootowl	endPlacementForInputViewSet, returning -> <UIInputViewSetPlacementOnScreenWithAccessory>
default	09:45:48.844945+0800	hootowl	endPlacementForInputViewSet: <<UIInputViewSet: 0x14a3c4f00>; keyboard = <UIKeyboardAutomatic: 0x15306f480; frame = (0 0; 393 233); opaque = NO; layer = <CALayer: 0x14ca73630>>%; assistant = <TUISystemInputAssistantView: 0x150572d00; frame = (0 0; 393 45); >; accessory = <_UIRemoteKeyboardPlaceholderView: 0x1530f9a00; frame = (0 0; 393 0); >; usesKeyClicks = NO;  > windowScene: <_UIKeyboardWindowScene: 0x1533f8000; role: _UIScreenBasedSceneSession; persistentIdentifier: 23B762E6-7AF8-43A0-B7F3-84DA7955C122; activationState: UISceneActivationStateForegroundActive>
default	09:45:48.845166+0800	hootowl	endPlacementForInputViewSet, returning -> <UIInputViewSetPlacementOnScreenWithAccessory>
default	09:45:48.845366+0800	hootowl	endPlacementForInputViewSet: <<UIInputViewSet: 0x14a3c4f00>; keyboard = <UIKeyboardAutomatic: 0x15306f480; frame = (0 0; 393 233); opaque = NO; layer = <CALayer: 0x14ca73630>>%; assistant = <TUISystemInputAssistantView: 0x150572d00; frame = (0 0; 393 45); >; accessory = <_UIRemoteKeyboardPlaceholderView: 0x1530f9a00; frame = (0 0; 393 0); >; usesKeyClicks = NO;  > windowScene: <_UIKeyboardWindowScene: 0x1533f8000; role: _UIScreenBasedSceneSession; persistentIdentifier: 23B762E6-7AF8-43A0-B7F3-84DA7955C122; activationState: UISceneActivationStateForegroundActive>
default	09:45:48.845590+0800	hootowl	endPlacementForInputViewSet, returning -> <UIInputViewSetPlacementOnScreenWithAccessory>
default	09:45:48.852204+0800	hootowl	channel:CandidateBar signal:Reset uniqueStringId:(null) creationTimestamp:810265548.845543 timestamp:810265548.852136 payload:(null)
default	09:45:48.855928+0800	hootowl	channel:LegacyTextInputActions signal:DidAction sessionID:311756FE-E472-4053-B1A1-580865B63F96 timestamp:810265548.855704 payload:{
    Class = IATextInputActionsSessionReplaceTextAction;
    appBundleId = "com.sharkda.hootowl";
    clientSideSessionErrors = "";
    flagOptions = 0;
    inputActionCountFromMergedActions = 0;
    inputMode =     {
        inputModeIdentifier = "zh_Hant-Pinyin@sw=Pinyin-Traditional;hw=Automatic";
        keyboardLayout = "Pinyin-Traditional";
        keyboardVariant = Pinyin;
        language = zh;
        region = Hant;
    };
    insertedEmojiCount = 0;
    insertedPunctuationCount = 0;
    insertedTextLength = 0;
    largestSingleDeletionLength = 0;
    largestSingleInsertionLength = 0;
    options = 0;
    processBundleId = "com.sharkda.hootowl";
    "relativeRangeBefore_length" = 0;
    "relativeRangeBefore_location" = 0;
    removedEmojiCount = 0;
    removedPunctuationCount = 0;
    removedTextLength = 0;
    source = 7;
    textInputActionsType = 1;
    timestamp = "810265548.826079";
}
default	09:45:48.867752+0800	hootowl	Cancelled Smart Reply generateCandidates
default	09:45:48.868206+0800	hootowl	All generators are not complete.
default	09:45:48.868231+0800	hootowl	All generators are not complete.
default	09:45:48.869786+0800	hootowl	        AVHapticPlayer.mm:150   -[AVHapticPlayerChannel resetAtTime:error:]: sending reset event: clientID: 0x100b3dd time: 0.000
default	09:45:48.869841+0800	hootowl	        AVHapticPlayer.mm:103   -[AVHapticPlayerChannel sendEvents:withImmediateParameters:atTime:error:]: sending event array: clientID: 0x100b3dd atTime: 0.000
default	09:45:48.870268+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:48.870285+0800	hootowl	        AVHapticPlayer.mm:762   -[AVHapticPlayer finishWithCompletionHandler:]: finish with comp handler: clientID: 0x100b3dd
default	09:45:48.870296+0800	hootowl	        AVHapticClient.mm:421   -[AVHapticClient finish:]: Client 0x100b3dd finishing
default	09:45:48.870305+0800	hootowl	        AVHapticClient.mm:426   -[AVHapticClient finish:]_block_invoke: completionCallback set to 0x1529d42a0
default	09:45:48.870312+0800	hootowl	        AVHapticClient.mm:453   -[AVHapticClient finish:]: Client 0x100b3dd done with finish
default	09:45:48.898165+0800	hootowl	        AVHapticClient.mm:1472  -[AVHapticClient clientCompletedWithError:]: Client-side (async) finish completion callback for client 0x100b3dd called from server
default	09:45:48.898180+0800	hootowl	        AVHapticClient.mm:1477  -[AVHapticClient clientCompletedWithError:]_block_invoke: Async dispatch: preparing to call completionCallback for client 0x100b3dd
default	09:45:48.898190+0800	hootowl	        AVHapticClient.mm:1479  -[AVHapticClient clientCompletedWithError:]_block_invoke: Calling completionCallback 0x1529d42a0 and then setting to nil
error	09:45:48.907603+0800	hootowl	Received external candidate resultset. Total number of candidates: 17
default	09:45:48.907627+0800	hootowl	All generators are not complete.
default	09:45:48.910830+0800	hootowl	-[_UIRemoteKeyboardPlaceholderView refreshPlaceholder]  refreshPlaceholder: size={393, 336} [previous size={393, 336}]
default	09:45:48.940140+0800	hootowl	All generators are complete, dispatching to `completionBlockJustOnce`
default	09:45:48.940174+0800	hootowl	Preparing to push (null) to candidate receiver, for request token: 6DD3538E
error	09:45:48.940192+0800	hootowl	containerToPush is nil, will not push anything to candidate receiver for request token: 6DD3538E
default	09:45:50.501919+0800	hootowl	Performing delayed generation for token=6DD3538E
default	09:45:52.407322+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:52.407691+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	09:45:52.407891+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIRemoteKeyboardWindow: 0x152b39900>; contextId: 0xC0855A9
default	09:45:52.408823+0800	hootowl	touch down
default	09:45:52.413022+0800	hootowl	-[_UIRemoteKeyboardPlaceholderView refreshPlaceholder]  refreshPlaceholder: size={393, 336} [previous size={393, 336}]
default	09:45:52.414448+0800	hootowl	        AVHapticPlayer.mm:150   -[AVHapticPlayerChannel resetAtTime:error:]: sending reset event: clientID: 0x100b3dd time: 0.000
default	09:45:52.414479+0800	hootowl	        AVHapticPlayer.mm:103   -[AVHapticPlayerChannel sendEvents:withImmediateParameters:atTime:error:]: sending event array: clientID: 0x100b3dd atTime: 0.000
default	09:45:52.415071+0800	hootowl	        AVHapticPlayer.mm:762   -[AVHapticPlayer finishWithCompletionHandler:]: finish with comp handler: clientID: 0x100b3dd
default	09:45:52.415218+0800	hootowl	        AVHapticClient.mm:421   -[AVHapticClient finish:]: Client 0x100b3dd finishing
default	09:45:52.415235+0800	hootowl	        AVHapticClient.mm:426   -[AVHapticClient finish:]_block_invoke: completionCallback set to 0x1529d4ed0
default	09:45:52.415484+0800	hootowl	        AVHapticClient.mm:453   -[AVHapticClient finish:]: Client 0x100b3dd done with finish
default	09:45:52.418559+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:52.433942+0800	hootowl	        AVHapticClient.mm:1472  -[AVHapticClient clientCompletedWithError:]: Client-side (async) finish completion callback for client 0x100b3dd called from server
default	09:45:52.434151+0800	hootowl	        AVHapticClient.mm:1477  -[AVHapticClient clientCompletedWithError:]_block_invoke: Async dispatch: preparing to call completionCallback for client 0x100b3dd
default	09:45:52.434170+0800	hootowl	        AVHapticClient.mm:1479  -[AVHapticClient clientCompletedWithError:]_block_invoke: Calling completionCallback 0x1529d4ed0 and then setting to nil
default	09:45:52.526580+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:52.526597+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	09:45:52.527728+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIRemoteKeyboardWindow: 0x152b39900>; contextId: 0xC0855A9
default	09:45:52.530581+0800	hootowl	touch up
default	09:45:52.558927+0800	hootowl	Keyboard receives keyEvent type: 4; subtype: 0
default	09:45:52.561655+0800	hootowl	Keyboard adds a string
default	09:45:52.561877+0800	hootowl	[0x1531fa300] activating connection: mach=true listener=false peer=false name=com.apple.TextInput.preferences
default	09:45:52.575560+0800	hootowl	Keyboard sends inputEvent to kbd
default	09:45:52.576864+0800	hootowl	Keyboard receives output from kbd
default	09:45:52.579272+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 1
default	09:45:52.592892+0800	hootowl	Reloading input views for key-window scene responder: <(null): 0x0; > force:N
default	09:45:52.592953+0800	hootowl	_reloadInputViewsForKeyWindowSceneResponder: 0 force: 0, fromBecomeFirstResponder: 0 (automaticKeyboard: 0, reloadIdentifier: 93CD7371-89F0-48A9-96DA-9152393F9FCD)
default	09:45:52.593064+0800	hootowl	_inputViewsForResponder: <(null): 0x0; >, automaticKeyboard: 0, force: 0
default	09:45:52.593075+0800	hootowl	_inputViewsForResponder, found custom inputView: <(null): 0x0>, customInputViewController: <(null): 0x0>
default	09:45:52.593086+0800	hootowl	_inputViewsForResponder, found inputAccessoryView: <(null): 0x0>
default	09:45:52.593097+0800	hootowl	_inputViewsForResponder, responderRequiresKeyboard 0 (automaticKeyboardEnabled: 0, activeInstance: <UIKeyboardAutomatic: 0x15306f480; frame = {{0, 0}, {393, 233}}; alpha = 1.000000; isHidden = 0; tAMIC = 0>, self.isOnScreen: 1, requiresKBWhenFirstResponder: 0)
default	09:45:52.593130+0800	hootowl	_inputViewsForResponder, useKeyboard 0 (allowsSystemInputView: 1, !inputView <(null): 0x0>, responderRequiresKeyboard 0)
default	09:45:52.593168+0800	hootowl	_inputViewsForResponder, configuring _responderWithoutAutomaticAppearanceEnabled: <(null): 0x0> (_automaticAppearEnabled: 1)
default	09:45:52.593182+0800	hootowl	_inputViewsForResponder returning: <<UIInputViewSet: 0x15308d800>; (empty)>
default	09:45:52.593245+0800	hootowl	currently observing: YES
default	09:45:52.593256+0800	hootowl	currently observing: NO
default	09:45:52.593321+0800	hootowl	-_teardownExistingDelegate:<UITextField: 0x149781400> forSetDelegate:(nil) force:NO delayEndInputSession:NO
default	09:45:52.593472+0800	hootowl	nw_path_evaluator_cancel [91F6FEA6-24E6-45E8-803A-039328F3703E] cancel
default	09:45:52.597884+0800	hootowl	-[RTIInputSystemClient endRemoteTextInputSessionWithID:options:completion:]  Ending text input session. sessionID = 311756FE-E472-4053-B1A1-580865B63F96, options = <RTISessionOptions: 0x15118fa60; shouldResign = YES; animated = YES; offscreenDirection = 0; enhancedWindowingModeEnabled = NO
default	09:45:52.598112+0800	hootowl	-[RTIInputSystemClient _endSessionWithID:forServices:options:completion:]  End input session: 311756FE-E472-4053-B1A1-580865B63F96
default	09:45:52.598225+0800	hootowl	-[RTIInputSystemClient endAllowingRemoteTextInput:completion:]  End allowing remote text input: 311756FE-E472-4053-B1A1-580865B63F96
default	09:45:52.598294+0800	hootowl	-[RTIInputSystemClient _modifyTextEditingAllowedForReason:notify:animated:modifyAllowancesBlock:completion:]  Text editing allowed did change (editingAllowedAfter = NO)
default	09:45:52.600830+0800	hootowl	Handling responseContextDidChange - existing: (null), new: (null)
default	09:45:52.601792+0800	hootowl	Requesting scene for autofill UI
default	09:45:52.602499+0800	hootowl	endPlacementForInputViewSet: <<UIInputViewSet: 0x15308d800>; (empty)> windowScene: <UIWindowScene: 0x148378200; role: UIWindowSceneSessionRoleApplication; persistentIdentifier: 83FF55F6-7B28-4BFD-8825-33CB43E5D162; activationState: UISceneActivationStateForegroundActive>
default	09:45:52.603121+0800	hootowl	-[_UIRemoteKeyboards prepareToMoveKeyboard:withIAV:isIAVRelevant:showing:notifyRemote:forScene:] position: {{0, 0}, {0, 0}} visible: 0; notifyRemote: 1; isMinimized: NO
default	09:45:52.603420+0800	hootowl	prepareToMoveKeyboard: set currentKeyboard:N
default	09:45:52.603703+0800	hootowl	TX signalKeyboardChanged
default	09:45:52.605758+0800	hootowl	-[_UIRemoteKeyboards signalToProxyKeyboardChanged:onCompletion:]  Signaling keyboard changed <<<_UIKeyboardChangedInformation: 0x15221c300>; appId (null) bundleId (null) animation fence <BKSAnimationFenceHandle:0x14b92b1d0 -> <CAFenceHandle:0x151274230 name=30 fence=4b00003c8f usable=YES>>; position {{0, 0}, {0, 0}}; animated YES; on screen NO; tracking NO; resizing NO; local NO, dock state: Unknown, hasValidNotif: NO>; source canvas com.apple.frontboard.systemappservices/FBSceneManager:sceneID%3Acom.sharkda.hootowl-83FF55F6-7B28-4BFD-8825-33CB43E5D162; source display Main; source bundle com.sharkda.hootowl; host bundle (null); animation fence <BKSAnimationFenceHandle:0x14b92b1d0 -> <CAFenceHandle:0x151274230 name=30 fence=4b00003c8f usable=YES>>; position {{0, 0}, {0, 0}} (with IAV same); floating 0; on screen NO;  intersectable YES; snapshot YES>
default	09:45:52.606600+0800	hootowl	Show keyboard with visual mode windowed (0)
default	09:45:52.608584+0800	hootowl	Setting input views: <<UIInputViewSet: 0x153264840>; (empty)>
default	09:45:52.608712+0800	hootowl	endPlacementForInputViewSet: <<UIInputViewSet: 0x14a3c4f00>; keyboard = <UIKeyboardAutomatic: 0x15306f480; frame = (0 0; 393 233); opaque = NO; layer = <CALayer: 0x14ca73630>>%; assistant = <TUISystemInputAssistantView: 0x150572d00; frame = (0 0; 393 45); >; accessory = <_UIRemoteKeyboardPlaceholderView: 0x1530f9a00; frame = (0 0; 393 0); >; usesKeyClicks = NO;  > windowScene: <_UIKeyboardWindowScene: 0x1533f8000; role: _UIScreenBasedSceneSession; persistentIdentifier: 23B762E6-7AF8-43A0-B7F3-84DA7955C122; activationState: UISceneActivationStateForegroundActive>
default	09:45:52.608764+0800	hootowl	endPlacementForInputViewSet, returning -> <UIInputViewSetPlacementOnScreenWithAccessory>
default	09:45:52.608815+0800	hootowl	endPlacementForInputViewSet: <<UIInputViewSet: 0x14a3c4f00>; keyboard = <UIKeyboardAutomatic: 0x15306f480; frame = (0 0; 393 233); opaque = NO; layer = <CALayer: 0x14ca73630>>%; assistant = <TUISystemInputAssistantView: 0x150572d00; frame = (0 0; 393 45); >; accessory = <_UIRemoteKeyboardPlaceholderView: 0x1530f9a00; frame = (0 0; 393 0); >; usesKeyClicks = NO;  > windowScene: <_UIKeyboardWindowScene: 0x1533f8000; role: _UIScreenBasedSceneSession; persistentIdentifier: 23B762E6-7AF8-43A0-B7F3-84DA7955C122; activationState: UISceneActivationStateForegroundActive>
default	09:45:52.609184+0800	hootowl	endPlacementForInputViewSet, returning -> <UIInputViewSetPlacementOnScreenWithAccessory>
default	09:45:52.609256+0800	hootowl	endPlacementForInputViewSet: <<UIInputViewSet: 0x14a3c4f00>; keyboard = <UIKeyboardAutomatic: 0x15306f480; frame = (0 0; 393 233); opaque = NO; layer = <CALayer: 0x14ca73630>>%; assistant = <TUISystemInputAssistantView: 0x150572d00; frame = (0 0; 393 45); >; accessory = <_UIRemoteKeyboardPlaceholderView: 0x1530f9a00; frame = (0 0; 393 0); >; usesKeyClicks = NO;  > windowScene: <_UIKeyboardWindowScene: 0x1533f8000; role: _UIScreenBasedSceneSession; persistentIdentifier: 23B762E6-7AF8-43A0-B7F3-84DA7955C122; activationState: UISceneActivationStateForegroundActive>
default	09:45:52.609370+0800	hootowl	endPlacementForInputViewSet, returning -> <UIInputViewSetPlacementOnScreenWithAccessory>
default	09:45:52.609436+0800	hootowl	endPlacementForInputViewSet: <<UIInputViewSet: 0x14a3c4f00>; keyboard = <UIKeyboardAutomatic: 0x15306f480; frame = (0 0; 393 233); opaque = NO; layer = <CALayer: 0x14ca73630>>%; assistant = <TUISystemInputAssistantView: 0x150572d00; frame = (0 0; 393 45); >; accessory = <_UIRemoteKeyboardPlaceholderView: 0x1530f9a00; frame = (0 0; 393 0); >; usesKeyClicks = NO;  > windowScene: <_UIKeyboardWindowScene: 0x1533f8000; role: _UIScreenBasedSceneSession; persistentIdentifier: 23B762E6-7AF8-43A0-B7F3-84DA7955C122; activationState: UISceneActivationStateForegroundActive>
default	09:45:52.609503+0800	hootowl	endPlacementForInputViewSet, returning -> <UIInputViewSetPlacementOnScreenWithAccessory>
default	09:45:52.609873+0800	hootowl	endPlacementForInputViewSet: <<UIInputViewSet: 0x153264840>; (empty)> windowScene: <_UIKeyboardWindowScene: 0x1533f8000; role: _UIScreenBasedSceneSession; persistentIdentifier: 23B762E6-7AF8-43A0-B7F3-84DA7955C122; activationState: UISceneActivationStateForegroundActive>
default	09:45:52.610040+0800	hootowl	Moving from placement: <UIInputViewSetPlacementOnScreenWithAccessory> to placement: <UIInputViewSetPlacementOffScreenDown> (currentPlacement: <UIInputViewSetPlacementOnScreenWithAccessory>)
default	09:45:52.610219+0800	hootowl	updatePlacementWithPlacement: <UIInputViewSetPlacementOffScreenDown>
default	09:45:52.610238+0800	hootowl	endPlacementForInputViewSet: <<UIInputViewSet: 0x14a3c4f00>; keyboard = <UIKeyboardAutomatic: 0x15306f480; frame = (0 0; 393 233); opaque = NO; layer = <CALayer: 0x14ca73630>>%; assistant = <TUISystemInputAssistantView: 0x150572d00; frame = (0 0; 393 45); >; accessory = <_UIRemoteKeyboardPlaceholderView: 0x1530f9a00; frame = (0 0; 393 0); >; usesKeyClicks = NO;  > windowScene: <_UIKeyboardWindowScene: 0x1533f8000; role: _UIScreenBasedSceneSession; persistentIdentifier: 23B762E6-7AF8-43A0-B7F3-84DA7955C122; activationState: UISceneActivationStateForegroundActive>
default	09:45:52.610271+0800	hootowl	endPlacementForInputViewSet, returning -> <UIInputViewSetPlacementOnScreenWithAccessory>
default	09:45:52.610409+0800	hootowl	endPlacementForInputViewSet: <<UIInputViewSet: 0x14a3c4f00>; keyboard = <UIKeyboardAutomatic: 0x15306f480; frame = (0 0; 393 233); opaque = NO; layer = <CALayer: 0x14ca73630>>%; assistant = <TUISystemInputAssistantView: 0x150572d00; frame = (0 0; 393 45); >; accessory = <_UIRemoteKeyboardPlaceholderView: 0x1530f9a00; frame = (0 0; 393 0); >; usesKeyClicks = NO;  > windowScene: <_UIKeyboardWindowScene: 0x1533f8000; role: _UIScreenBasedSceneSession; persistentIdentifier: 23B762E6-7AF8-43A0-B7F3-84DA7955C122; activationState: UISceneActivationStateForegroundActive>
default	09:45:52.610482+0800	hootowl	endPlacementForInputViewSet, returning -> <UIInputViewSetPlacementOnScreenWithAccessory>
default	09:45:52.610835+0800	hootowl	endPlacementForInputViewSet: <<UIInputViewSet: 0x14a3c4f00>; keyboard = <UIKeyboardAutomatic: 0x15306f480; frame = (0 0; 393 233); opaque = NO; layer = <CALayer: 0x14ca73630>>%; assistant = <TUISystemInputAssistantView: 0x150572d00; frame = (0 0; 393 45); >; accessory = <_UIRemoteKeyboardPlaceholderView: 0x1530f9a00; frame = (0 0; 393 0); >; usesKeyClicks = NO;  > windowScene: <_UIKeyboardWindowScene: 0x1533f8000; role: _UIScreenBasedSceneSession; persistentIdentifier: 23B762E6-7AF8-43A0-B7F3-84DA7955C122; activationState: UISceneActivationStateForegroundActive>
default	09:45:52.610891+0800	hootowl	endPlacementForInputViewSet, returning -> <UIInputViewSetPlacementOnScreenWithAccessory>
default	09:45:52.611011+0800	hootowl	endPlacementForInputViewSet: <<UIInputViewSet: 0x14a3c4f00>; keyboard = <UIKeyboardAutomatic: 0x15306f480; frame = (0 0; 393 233); opaque = NO; layer = <CALayer: 0x14ca73630>>%; assistant = <TUISystemInputAssistantView: 0x150572d00; frame = (0 0; 393 45); >; accessory = <_UIRemoteKeyboardPlaceholderView: 0x1530f9a00; frame = (0 0; 393 0); >; usesKeyClicks = NO;  > windowScene: <_UIKeyboardWindowScene: 0x1533f8000; role: _UIScreenBasedSceneSession; persistentIdentifier: 23B762E6-7AF8-43A0-B7F3-84DA7955C122; activationState: UISceneActivationStateForegroundActive>
default	09:45:52.611411+0800	hootowl	endPlacementForInputViewSet, returning -> <UIInputViewSetPlacementOnScreenWithAccessory>
default	09:45:52.611618+0800	hootowl	Tracking provider: moveFromPlacement: <UIInputViewSetPlacementOnScreenWithAccessory> toPlacement: <UIInputViewSetPlacementOffScreenDown> update to: {{0, 852}, {393, 336}}
default	09:45:52.611722+0800	hootowl	Updating tracking clients for start <TUIKeyboardTrackingCoordinator:0x149ad6080 state=<TUIKeyboardState: 0x14ca62960 State: offscreen; is docked>; frame={{0, 852}, {393, 336}}; animation=<TUIKeyboardAnimationInfo: 0x151247240, duration: 0.38, from local keyboard, is not rotating, should animate, type: 0, notificationInfo: {
    UIKeyboardAnimationCurveUserInfoKey = 7;
    UIKeyboardAnimationDurationUserInfoKey = "0.3833";
    UIKeyboardBoundsUserInfoKey = "NSRect: {{0, 0}, {393, 336}}";
    UIKeyboardCenterBeginUserInfoKey = "NSPoint: {196.5, 684}";
    UIKeyboardCenterEndUserInfoKey = "NSPoint: {196.5, 1020}";
    UIKeyboardFrameBeginUserInfoKey = "NSRect: {{0, 516}, {393, 336}}";
    UIKeyboardFrameEndUserInfoKey = "NSRect: {{0, 852}, {393, 336}}";
    UIKeyboardIsLocalUserInfoKey = 1;
}notificationsDebug: >>
default	09:45:52.611768+0800	hootowl	changeSizingConstants: size is changing [not transitioning] to {393, 0} [previous size: {393, 350}]
default	09:45:52.611799+0800	hootowl	changeSizingConstants: size is changing [not transitioning] to {393, 0} [previous size: {393, 336}]
default	09:45:52.612025+0800	hootowl	changeSizingConstants: size is changing [not transitioning] to {393, 48} [previous size: {393, 0}]
default	09:45:52.612241+0800	hootowl	changeSizingConstants: size is changing [not transitioning] to {393, 34} [previous size: {393, 48}]
default	09:45:52.613543+0800	hootowl	Setting tracking element input views: <<UIInputViewSet: 0x1532679c0>; (empty)>
default	09:45:52.613553+0800	hootowl	-[_UIRemoteKeyboardPlaceholderView refreshPlaceholder]  refreshPlaceholder: size={393, 0} [previous size={393, 0}]
default	09:45:52.613560+0800	hootowl	Placeholder height changed from 336.0 to 0.0
default	09:45:52.613580+0800	hootowl	endPlacementForInputViewSet: <<UIInputViewSet: 0x1532679c0>; (empty)> windowScene: <UIWindowScene: 0x148378200; role: UIWindowSceneSessionRoleApplication; persistentIdentifier: 83FF55F6-7B28-4BFD-8825-33CB43E5D162; activationState: UISceneActivationStateForegroundActive>
default	09:45:52.613603+0800	hootowl	Moving from placement: <UIInputViewSetPlacementOnScreenWithAccessory> to placement: <UIInputViewSetPlacementOffScreenDown> (currentPlacement: <UIInputViewSetPlacementOnScreenWithAccessory>)
default	09:45:52.613681+0800	hootowl	updatePlacementWithPlacement: <UIInputViewSetPlacementOffScreenDown>
default	09:45:52.614315+0800	hootowl	Posted notification willHide with {
    UIKeyboardAnimationCurveUserInfoKey = 7;
    UIKeyboardAnimationDurationUserInfoKey = 0;
    UIKeyboardBoundsUserInfoKey = "NSRect: {{0, 0}, {393, 82}}";
    UIKeyboardCenterBeginUserInfoKey = "NSPoint: {196.5, 828}";
    UIKeyboardCenterEndUserInfoKey = "NSPoint: {196.5, 811}";
    UIKeyboardFrameBeginUserInfoKey = "NSRect: {{0, 804}, {393, 48}}";
    UIKeyboardFrameEndUserInfoKey = "NSRect: {{0, 770}, {393, 82}}";
    UIKeyboardIsLocalUserInfoKey = 1;
} (null)
default	09:45:52.614427+0800	hootowl	-[RTIInputSystemClient remoteTextInputSessionWithID:textSuggestionsChanged:]  Text input session suggestions changed. sessionID = (null)
default	09:45:52.626173+0800	hootowl	Keyboard inserts text
default	09:45:52.626368+0800	hootowl	Document state contextBeforeInput length is zero.
default	09:45:52.626395+0800	hootowl	Cancelled smart reply generation due to nil ICH
default	09:45:52.626419+0800	hootowl	Cancelled Smart Reply generateCandidates
default	09:45:52.626703+0800	hootowl	All generators are not complete.
default	09:45:52.628990+0800	hootowl	All generators are not complete.
error	09:45:52.631872+0800	hootowl	Received external candidate resultset. Total number of candidates: 17
default	09:45:52.632338+0800	hootowl	All generators are not complete.
default	09:45:52.645266+0800	hootowl	0x148d71000 (pageProxyID=1708) -[WKWebView _updateVisibleContentRects:] - have not received a commit 20.82s after visible content rect update; lastTransactionID 0
default	09:45:52.645344+0800	hootowl	0x148d73000 (pageProxyID=20) -[WKWebView _updateVisibleContentRects:] - have not received a commit 8.15s after visible content rect update; lastTransactionID 4
default	09:45:52.662038+0800	hootowl	All generators are complete, dispatching to `completionBlockJustOnce`
default	09:45:52.662323+0800	hootowl	Preparing to push (null) to candidate receiver, for request token: CE92FE9C
error	09:45:52.662353+0800	hootowl	containerToPush is nil, will not push anything to candidate receiver for request token: CE92FE9C
default	09:45:52.662435+0800	hootowl	Performing delayed generation for token=CE92FE9C
default	09:45:52.662460+0800	hootowl	<_UIKBFeedbackGenerator: 0x153264600>: Request engine to stop for: -[_UIKBFeedbackGenerator _deactivateWithCompletionBlock:]
default	09:45:52.662497+0800	hootowl	[0x149602800] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	09:45:52.664063+0800	hootowl	        CHHapticEngine.mm:1439  -[CHHapticEngine stopWithCompletionHandler:]: Called on engine 0x151024a80
default	09:45:52.666809+0800	hootowl	        CHHapticEngine.mm:1403  -[CHHapticEngine doStopWithCompletionHandler:]: Stopping underlying Haptic Player
default	09:45:52.667037+0800	hootowl	        AVHapticPlayer.mm:739   -[AVHapticPlayer stopRunningWithCompletionHandler:]: stop running: clientID: 0x100b3dd
default	09:45:52.667191+0800	hootowl	        AVHapticClient.mm:398   -[AVHapticClient stopRunning:]: Client 0x100b3dd stopping
default	09:45:52.673460+0800	hootowl	        AVHapticClient.mm:1472  -[AVHapticClient clientCompletedWithError:]: Client-side (async) finish completion callback for client 0x100b3dd called from server
default	09:45:52.673466+0800	hootowl	        AVHapticClient.mm:1477  -[AVHapticClient clientCompletedWithError:]_block_invoke: Async dispatch: preparing to call completionCallback for client 0x100b3dd
default	09:45:52.673485+0800	hootowl	        AVHapticClient.mm:1484  -[AVHapticClient clientCompletedWithError:]_block_invoke: strongSelf.completionCallback is nil
default	09:45:52.673661+0800	hootowl	<_UIKBFeedbackGenerator: 0x153264600>: Engine stopped.
default	09:45:52.673671+0800	hootowl	<_UIKBFeedbackGenerator: 0x153264600>: Releasing engine and players.
default	09:45:52.674164+0800	hootowl	        AVHapticPlayer.mm:581   -[AVHapticPlayer releaseCustomAudioEvent:reply:]: releasing custom audio event: clientID: 0x100b3dd
default	09:45:52.674216+0800	hootowl	        AVHapticPlayer.mm:581   -[AVHapticPlayer releaseCustomAudioEvent:reply:]: releasing custom audio event: clientID: 0x100b3dd
default	09:45:52.674401+0800	hootowl	        AVHapticPlayer.mm:581   -[AVHapticPlayer releaseCustomAudioEvent:reply:]: releasing custom audio event: clientID: 0x100b3dd
default	09:45:52.674510+0800	hootowl	        AVHapticClient.mm:387   -[AVHapticClient stopRunning]: Client 0x100b3dd stopping
default	09:45:52.676582+0800	hootowl	[0x153292580] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	09:45:52.676632+0800	hootowl	[0x1496008c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
error	09:45:52.676774+0800	hootowl	Reporter disconnected or already stopped. { func=stop, reporterID=197761769144322 }
default	09:45:52.719923+0800	hootowl	Received state update for 46045 (app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>, unknown-NotVisible
default	09:45:52.753438+0800	hootowl	Received state update for 46045 (app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>, unknown-NotVisible
default	09:45:52.774931+0800	hootowl	channel:LegacyTextInputActions signal:DidAction sessionID:311756FE-E472-4053-B1A1-580865B63F96 timestamp:810265552.774703 payload:{
    Class = IATextInputActionsSessionCommitTextAction;
    appBundleId = "com.sharkda.hootowl";
    clientSideSessionErrors = "";
    flagOptions = 0;
    inputActionCountFromMergedActions = 0;
    inputMode =     {
        inputModeIdentifier = "zh_Hant-Pinyin@sw=Pinyin-Traditional;hw=Automatic";
        keyboardLayout = "Pinyin-Traditional";
        keyboardVariant = Pinyin;
        language = zh;
        region = Hant;
    };
    insertedEmojiCount = 0;
    insertedPunctuationCount = 0;
    insertedTextLength = 1;
    largestSingleDeletionLength = 0;
    largestSingleInsertionLength = 1;
    processBundleId = "com.sharkda.hootowl";
    "relativeRangeBefore_length" = 0;
    "relativeRangeBefore_location" = 0;
    removedEmojiCount = 0;
    removedPunctuationCount = 0;
    removedTextLength = 0;
    source = 7;
    textInputActionsType = 0;
    timestamp = "810265548.8507611";
}
default	09:45:52.776864+0800	hootowl	channel:LegacyTextInputActions signal:DidAction sessionID:(null) timestamp:810265552.776626 payload:{
    Class = IATextInputActionsSessionEndAction;
    appBundleId = "com.sharkda.hootowl";
    clientSideSessionErrors = "";
    flagOptions = 0;
    inputActionCountFromMergedActions = 0;
    inputMode =     {
        inputModeIdentifier = "zh_Hant-Pinyin@sw=Pinyin-Traditional;hw=Automatic";
        keyboardLayout = "Pinyin-Traditional";
        keyboardVariant = Pinyin;
        language = zh;
        region = Hant;
    };
    insertedEmojiCount = 0;
    insertedPunctuationCount = 0;
    insertedTextLength = 0;
    largestSingleDeletionLength = 0;
    largestSingleInsertionLength = 0;
    processBundleId = "com.sharkda.hootowl";
    "relativeRangeBefore_length" = 0;
    "relativeRangeBefore_location" = 0;
    removedEmojiCount = 0;
    removedPunctuationCount = 0;
    removedTextLength = 0;
    source = 4;
    textInputActionsType = 0;
    timestamp = "810265552.601297";
}
default	09:45:52.777534+0800	hootowl	channel:LegacyTextInputActions signal:DidSessionEnd sessionID:311756FE-E472-4053-B1A1-580865B63F96 timestamp:810265552.777186 payload:{
    Class = IATextInputActionsSessionEndAction;
    appBundleId = "com.sharkda.hootowl";
    clientSideSessionErrors = "";
    flagOptions = 0;
    inputActionCountFromMergedActions = 0;
    inputMode =     {
        inputModeIdentifier = "zh_Hant-Pinyin@sw=Pinyin-Traditional;hw=Automatic";
        keyboardLayout = "Pinyin-Traditional";
        keyboardVariant = Pinyin;
        language = zh;
        region = Hant;
    };
    insertedEmojiCount = 0;
    insertedPunctuationCount = 0;
    insertedTextLength = 0;
    largestSingleDeletionLength = 0;
    largestSingleInsertionLength = 0;
    processBundleId = "com.sharkda.hootowl";
    "relativeRangeBefore_length" = 0;
    "relativeRangeBefore_location" = 0;
    removedEmojiCount = 0;
    removedPunctuationCount = 0;
    removedTextLength = 0;
    source = 4;
    textInputActionsType = 0;
    timestamp = "810265552.601297";
}
default	09:45:53.055419+0800	hootowl	TX setWindowContextID:201872809 windowState:Disabled level:5.0
    focusContext:<contextID:4107863071 sceneID:com.sharkda.hootowl-83FF55F6-7B28-4BFD-8825-33CB43E5D162>
default	09:45:53.057848+0800	hootowl	Change from input view set: <<UIInputViewSet: 0x14a3c6a00>; keyboard = <UIKeyboardAutomatic: 0x15306f480; frame = (0 0; 393 233); opaque = NO; layer = <CALayer: 0x14ca73630>>%; accessory = <_TtCC7SwiftUI23InputAccessoryGeneratorP33_5C36F4A49E2E2562B910FE6399D2C51E10RootUIView: 0x149676f40; frame = (0 0; 393 82); >; usesKeyClicks = NO;  >
default	09:45:53.058218+0800	hootowl	Change to input view set: <<UIInputViewSet: 0x1532679c0>; (empty)>
default	09:45:53.058248+0800	hootowl	endPlacementForInputViewSet: <<UIInputViewSet: 0x1532679c0>; (empty)> windowScene: <UIWindowScene: 0x148378200; role: UIWindowSceneSessionRoleApplication; persistentIdentifier: 83FF55F6-7B28-4BFD-8825-33CB43E5D162; activationState: UISceneActivationStateForegroundActive>
default	09:45:53.058422+0800	hootowl	nw_path_evaluator_start [AA5674D5-F069-4A69-9D44-257B92AF4F0D <NULL> generic, multipath service: handover, attribution: developer]
	path: satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good
default	09:45:53.069678+0800	hootowl	-[UIDictationController setIgnoreFinalizePhrases:] Setting ignoreFinalizePhrases flag 1
default	09:45:53.070020+0800	hootowl	Posted notification didHide with {
    UIKeyboardAnimationCurveUserInfoKey = 7;
    UIKeyboardAnimationDurationUserInfoKey = 0;
    UIKeyboardBoundsUserInfoKey = "NSRect: {{0, 0}, {393, 82}}";
    UIKeyboardCenterBeginUserInfoKey = "NSPoint: {196.5, 828}";
    UIKeyboardCenterEndUserInfoKey = "NSPoint: {196.5, 811}";
    UIKeyboardFrameBeginUserInfoKey = "NSRect: {{0, 804}, {393, 48}}";
    UIKeyboardFrameEndUserInfoKey = "NSRect: {{0, 770}, {393, 82}}";
    UIKeyboardIsLocalUserInfoKey = 1;
} (null)
default	09:45:53.073363+0800	hootowl	Change from input view set: <<UIInputViewSet: 0x14a3c4f00>; keyboard = <UIKeyboardAutomatic: 0x15306f480; frame = (0 0; 393 233); opaque = NO; layer = <CALayer: 0x14ca73630>>%; assistant = <TUISystemInputAssistantView: 0x150572d00; frame = (0 0; 393 45); >; accessory = <_UIRemoteKeyboardPlaceholderView: 0x1530f9a00; frame = (0 0; 393 0); >; usesKeyClicks = NO;  >
default	09:45:53.073379+0800	hootowl	Change to input view set: <<UIInputViewSet: 0x153264840>; (empty)>
default	09:45:53.077425+0800	hootowl	-[UIDictationController setIgnoreFinalizePhrases:] Setting ignoreFinalizePhrases flag 1
default	09:45:53.077786+0800	hootowl	Posted notification didHide with {
    UIKeyboardAnimationCurveUserInfoKey = 7;
    UIKeyboardAnimationDurationUserInfoKey = 0;
    UIKeyboardBoundsUserInfoKey = "NSRect: {{0, 0}, {393, 82}}";
    UIKeyboardCenterBeginUserInfoKey = "NSPoint: {196.5, 828}";
    UIKeyboardCenterEndUserInfoKey = "NSPoint: {196.5, 811}";
    UIKeyboardFrameBeginUserInfoKey = "NSRect: {{0, 804}, {393, 48}}";
    UIKeyboardFrameEndUserInfoKey = "NSRect: {{0, 770}, {393, 82}}";
    UIKeyboardIsLocalUserInfoKey = 1;
} (null)
default	09:45:53.082864+0800	hootowl	SecTaskLoadEntitlements: failed to get cs_flags, error=1, pid=46067
default	09:45:53.082870+0800	hootowl	SecTaskLoadEntitlements: failed to get cs_flags, error=1, pid=46069
default	09:45:53.082889+0800	hootowl	0x148d71000 (pageProxyID=1708) -[WKWebView _updateVisibleContentRects:] - have not received a commit 21.25s after visible content rect update; lastTransactionID 0
default	09:45:53.082895+0800	hootowl	0x148d73000 (pageProxyID=20) -[WKWebView _updateVisibleContentRects:] - have not received a commit 8.58s after visible content rect update; lastTransactionID 4
default	09:45:53.166485+0800	hootowl	Received state update for 46045 (app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>, unknown-NotVisible
default	09:45:57.619118+0800	hootowl	tcp_close [C3.1.2.1:3] TCP Packets:
	 snd    0.000s seq 3362154437:3362154438 ack 0          win 65535 len 0    [SEC]
	 rcv    0.121s seq 3214497661:3214497662 ack 3362154438 win 65535 len 0    [S.]
	 snd    0.000s seq 3362154438:3362154438 ack 3214497662 win 2057  len 0    [.]
	 snd    0.004s seq 3362154438:3362155838 ack 3214497662 win 2057  len 1400 [.]
	 snd    0.000s seq 3362155838:3362155974 ack 3214497662 win 2057  len 136  [P.]
	 rcv    0.121s seq 3214497662:3214497662 ack 3362155974 win 1044  len 0    [.]
	 rcv    0.001s seq 3214497662:3214503114 ack 3362155974 win 1044  len 5452 [P.]
	 snd    0.000s seq 3362155974:3362155974 ack 3214503114 win 1972  len 0    [.]
	 snd    0.000s seq 3362155974:3362155974 ack 3214503114 win 2048  len 0    [.]
	 snd    0.677s seq 3362155974:3362155975 ack 3214503114 win 2048  len 0    [F.]
	 rcv    0.179s seq 3214503114:3214503114 ack 3362155974 win 1044  len 0    [.]
	 rcv    0.054s seq 3214503114:3214503115 ack 3362155975 win 1044  len 0    [F.]
	 snd    0.000s seq 3362155975:3362155975 ack 3214503115 win 2048  len 0    [.]
	Last packet 30552ms ago.
default	09:45:57.620306+0800	hootowl	tcp_close [C4.1.2.1:3] TCP Packets:
	 snd    0.000s seq 3488196868:3488196869 ack 0          win 65535 len 0    [SEC]
	 rcv    0.180s seq  950012595:950012596  ack 3488196869 win 65535 len 0    [S.]
	 snd    0.000s seq 3488196869:3488196869 ack 950012596  win 2057  len 0    [.]
	 snd    0.001s seq 3488196869:3488198269 ack 950012596  win 2057  len 1400 [.]
	 snd    0.000s seq 3488198269:3488198402 ack 950012596  win 2057  len 133  [P.]
	 snd    0.385s seq 3488197002:3488198402 ack 950012596  win 2057  len 1400 [P.]
	 rcv    0.188s seq  950012596:950012596  ack 3488198402 win 1045  len 0    [.]
	 rcv    0.000s seq  950012596:950018048  ack 3488198402 win 1045  len 5452 [P.]
	 snd    0.000s seq 3488198402:3488198402 ack 950018048  win 1972  len 0    [.]
	 snd    0.001s seq 3488198402:3488198402 ack 950018048  win 2048  len 0    [.]
	 rcv    0.051s seq  950016796:950018048  ack 3488198402 win 1045  len 1252 [P.]
	 snd    0.000s seq 3488198402:3488198402 ack 950018048  win 2048  len 0    [.]
	 rcv    0.000s seq  950018048:950018048  ack 3488198402 win 1045  len 0    [.]
	 snd    0.327s seq 3488198402:3488198403 ack 950018048  win 2048  len 0    [F.]
	 rcv    0.081s seq  950018048:950018049  ack 3488198403 win 1045  len 0    [F.]
	 snd    0.000s seq 3488198403:3488198403 ack 950018049  win 2048  len 0    [.]
	Last packet 30430ms ago.
default	09:45:58.264178+0800	hootowl	Connection 2: cleaning up
default	09:45:58.264372+0800	hootowl	[C2 7162D2BB-8A88-4463-93E0-DE8625890B51 tcgbusfs.blob.core.windows.net:443 tcp, url: https://tcgbusfs.blob.core.windows.net/blobtcmsv/TCMSV_alldesc.json, tls, definite, attribution: developer] cancel
default	09:45:58.265511+0800	hootowl	[C2 7162D2BB-8A88-4463-93E0-DE8625890B51 tcgbusfs.blob.core.windows.net:443 tcp, url: https://tcgbusfs.blob.core.windows.net/blobtcmsv/TCMSV_alldesc.json, tls, definite, attribution: developer] cancelled
	[C2.1.1 B8A11390-9624-446D-B4E0-95DD59AACEAC 192.168.50.191:50790<->20.150.22.100:443]
	Connected Path: satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good
	Privacy Stance: Not Eligible
	Duration: 34.592s, DNS @0.000s took 0.018s, TCP @0.019s took 0.078s,  took 0.353s
	bytes in/out: 2873226/3690, packets in/out: 464/92, rtt: 0.101s, retransmitted bytes: 1428, out-of-order bytes: 0
	ecn packets sent/acked/marked/lost: 5/4/0/1
default	09:45:58.267429+0800	hootowl	nw_protocol_tcp_log_summary [C2.1.1:3] 
	[1712C2DE-F57A-4D54-8C0B-88047351B4F0 192.168.50.191:50790<->20.150.22.100:443]
	Init: 1, Conn_Time: 77.448ms, SYNs: 1, WR_T: 0/0, RD_T: 0/0, TFO: 0/0/0, ECN: 0/1/1, Accurate ECN (client/server): Disabled/Disabled, TS: 1, TSO: 0
	rtt_cache: none, rtt_upd: 5, rtt: 101.250ms, rtt_var: 46.687ms rtt_nc: 101.250ms, rtt_var_nc: 46.687ms base rtt: 65ms
	ACKs-compressed: 36, ACKs delayed: 381 delayed ACKs sent: 1
default	09:45:58.270435+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C2] reporting state cancelled
default	09:45:58.270467+0800	hootowl	Connection 2: done
default	09:45:58.270704+0800	hootowl	tcp_output [C2.1.1:3] flags=[F.] seq=3020162680, ack=2415292092, win=12401 state=FIN_WAIT_1 rcv_nxt=2415292092, snd_una=3020162656
default	09:45:58.341727+0800	hootowl	tcp_input [C2.1.1:3] flags=[F.] seq=2415292092, ack=3020162681, win=16382 state=FIN_WAIT_2 rcv_nxt=2415292092, snd_una=3020162681
default	09:45:58.607613+0800	hootowl	TX focusApplication (peekAppEvent) stealKB:Y scene:com.sharkda.hootowl-83FF55F6-7B28-4BFD-8825-33CB43E5D162
default	09:45:58.607641+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:58.607664+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	09:45:58.607678+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1481fc400>; contextId: 0xF4D9041F
default	09:45:58.686321+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:58.686685+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:58.687555+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	09:45:58.687640+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1481fc400>; contextId: 0xF4D9041F
default	09:45:58.717998+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 1
default	09:45:59.353461+0800	hootowl	TX focusApplication (peekAppEvent) stealKB:Y scene:com.sharkda.hootowl-83FF55F6-7B28-4BFD-8825-33CB43E5D162
default	09:45:59.353918+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:59.354300+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	09:45:59.354345+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1481fc400>; contextId: 0xF4D9041F
default	09:45:59.373682+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:59.450341+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:45:59.450515+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	09:45:59.450658+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1481fc400>; contextId: 0xF4D9041F
default	09:45:59.452430+0800	hootowl	<UIWindowScene: 0x148378200> (83FF55F6-7B28-4BFD-8825-33CB43E5D162) Scene updated orientation preferences: ( Pu Ll Lr ) -> ( Pu )
default	09:45:59.457720+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 1
default	09:45:59.519165+0800	hootowl	MncplCyclopsScreen 149
🪟 MncplCyclopsScreen onAppear — municipal 🆔 8064324136773232350
default	09:46:00.189003+0800	hootowl	<UIWindowScene: 0x148378200> (83FF55F6-7B28-4BFD-8825-33CB43E5D162) Scene updated orientation preferences: ( Pu ) -> ( Pu Ll Lr )
default	09:46:00.629182+0800	hootowl	tcp_close [C9.1.2.1:3] TCP Packets:
	 snd    0.000s seq 3879884732:3879884733 ack 0          win 65535 len 0    [SEC]
	 rcv    0.106s seq 2148268902:2148268903 ack 3879884733 win 65535 len 0    [S.]
	 snd    0.000s seq 3879884733:3879884733 ack 2148268903 win 2057  len 0    [.]
	 snd    0.002s seq 3879884733:3879886133 ack 2148268903 win 2057  len 1400 [.]
	 snd    0.000s seq 3879886133:3879886280 ack 2148268903 win 2057  len 147  [P.]
	 rcv    0.187s seq 2148268903:2148268903 ack 3879886133 win 1045  len 0    [.]
	 rcv    0.000s seq 2148268903:2148268903 ack 3879886280 win 1045  len 0    [.]
	 rcv    0.000s seq 2148268903:2148270303 ack 3879886280 win 1045  len 1400 [.]
	 snd    0.000s seq 3879886280:3879886280 ack 2148270303 win 2036  len 0    [.]
	 rcv    0.000s seq 2148270303:2148281733 ack 3879886280 win 1045  len 11430 [P.]
	 snd    0.000s seq 3879886280:3879886280 ack 2148281733 win 1858  len 0    [.]
	 snd    0.010s seq 3879886280:3879886280 ack 2148281733 win 2048  len 0    [.]
	 rcv    0.061s seq 2148281503:2148281733 ack 3879886280 win 1045  len 230  [P.]
	 snd    0.000s seq 3879886280:3879886280 ack 2148281733 win 2048  len 0    [.]
	 snd    0.151s seq 3879886280:3879886281 ack 2148281733 win 2048  len 0    [F.]
	 rcv    0.026s seq 2148281733:2148281734 ack 3879886281 win 1045  len 0    [F.]
	 snd    0.000s seq 3879886281:3879886281 ack 2148281734 win 2048  len 0    [.]
	Last packet 30894ms ago.
error	09:46:01.460593+0800	hootowl	Failed to terminate process: Error Domain=com.apple.extensionKit.errorDomain Code=18 "(null)" UserInfo={NSUnderlyingError=0x151237060 {Error Domain=RBSRequestErrorDomain Code=3 "No such process found" UserInfo={NSLocalizedFailureReason=No such process found}}}
default	09:46:01.460630+0800	hootowl	0x13113c540 - ~ProcessAssertion: Releasing process assertion 'XPCConnectionTerminationWatchdog' for process with PID=46063
error	09:46:02.988168+0800	hootowl	Failed to terminate process: Error Domain=com.apple.extensionKit.errorDomain Code=18 "(null)" UserInfo={NSUnderlyingError=0x151234990 {Error Domain=RBSRequestErrorDomain Code=3 "No such process found" UserInfo={NSLocalizedFailureReason=No such process found}}}
default	09:46:02.988478+0800	hootowl	0x13113c6c0 - ~ProcessAssertion: Releasing process assertion 'XPCConnectionTerminationWatchdog' for process with PID=46068
default	09:46:03.664144+0800	hootowl	Connection 1: cleaning up
default	09:46:03.664350+0800	hootowl	[C1 C821D611-DBE6-4952-B979-8DDAD1E7ACFE tcgbusfs.blob.core.windows.net:443 quic-connection, url: https://tcgbusfs.blob.core.windows.net/blobtcmsv/TCMSV_allavailable.json, definite, attribution: developer] cancel
default	09:46:03.664521+0800	hootowl	[C1 C821D611-DBE6-4952-B979-8DDAD1E7ACFE tcgbusfs.blob.core.windows.net:443 quic-connection, url: https://tcgbusfs.blob.core.windows.net/blobtcmsv/TCMSV_allavailable.json, definite, attribution: developer] cancelled
	[C1.1.1.1 B8A11390-9624-446D-B4E0-95DD59AACEAC 192.168.50.191:50789<->20.150.22.100:443]
	Connected Path: satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good
	Privacy Stance: Not Eligible
	Duration: 40.678s, DNS @0.002s took 0.026s, TCP @0.031s took 0.098s,  took 0.440s
	bytes in/out: 3345484/2627, packets in/out: 461/289, rtt: 0.103s, retransmitted bytes: 0, out-of-order bytes: 169920
	ecn packets sent/acked/marked/lost: 6/5/0/0
default	09:46:03.665715+0800	hootowl	nw_protocol_tcp_log_summary [C1.1.1.1:3] 
	[8E8E4A87-F644-46AB-ADC9-CDFCDC76D914 192.168.50.191:50789<->20.150.22.100:443]
	Init: 1, Conn_Time: 97.655ms, SYNs: 1, WR_T: 0/0, RD_T: 0/0, TFO: 0/0/0, ECN: 0/0/1, Accurate ECN (client/server): Disabled/Disabled, TS: 1, TSO: 0
	rtt_cache: none, rtt_upd: 6, rtt: 103.718ms, rtt_var: 31.500ms rtt_nc: 103.718ms, rtt_var_nc: 31.500ms base rtt: 65ms
	ACKs-compressed: 56, ACKs delayed: 332 delayed ACKs sent: 0
default	09:46:03.666448+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C1] reporting state cancelled
default	09:46:03.666459+0800	hootowl	Connection 1: done
default	09:46:03.666593+0800	hootowl	tcp_output [C1.1.1.1:3] flags=[F.] seq=3673468005, ack=4180612776, win=9791 state=FIN_WAIT_1 rcv_nxt=4180612776, snd_una=3673467981
default	09:46:03.757419+0800	hootowl	tcp_input [C1.1.1.1:3] flags=[F.] seq=4180612776, ack=3673468006, win=16381 state=FIN_WAIT_2 rcv_nxt=4180612776, snd_una=3673468006
default	09:46:04.169650+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c67d3 posting AVAudioSessionAvailableOutputsChangeNotification
default	09:46:04.177386+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c67d3 posting AVAudioSessionAvailableInputsChangeNotification
default	09:46:04.177558+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c67d3 posting AVAudioSessionAvailableOutputsChangeNotification
default	09:46:04.225706+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c67d3 posting AVAudioSessionAvailableOutputsChangeNotification
default	09:46:04.234461+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c67d3 posting AVAudioSessionAvailableInputsChangeNotification
default	09:46:04.234512+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c67d3 posting AVAudioSessionAvailableOutputsChangeNotification
default	09:46:04.268335+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c67d3 posting AVAudioSessionAvailableOutputsChangeNotification
default	09:46:04.288341+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c67d3 posting AVAudioSessionAvailableInputsChangeNotification
default	09:46:04.288518+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c67d3 posting AVAudioSessionAvailableOutputsChangeNotification
default	09:46:04.325838+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c67d3 posting AVAudioSessionAvailableOutputsChangeNotification
default	09:46:04.337095+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c67d3 posting AVAudioSessionAvailableInputsChangeNotification
default	09:46:04.337106+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c67d3 posting AVAudioSessionAvailableOutputsChangeNotification
default	09:46:04.429136+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c67d3 posting AVAudioSessionAvailableOutputsChangeNotification
default	09:46:04.429739+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c67d3 posting AVAudioSessionAvailableInputsChangeNotification
default	09:46:04.432885+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c67d3 posting AVAudioSessionAvailableOutputsChangeNotification
default	09:46:04.553760+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c67d3 posting AVAudioSessionAvailableOutputsChangeNotification
default	09:46:04.572405+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c67d3 posting AVAudioSessionAvailableInputsChangeNotification
default	09:46:04.572695+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c67d3 posting AVAudioSessionAvailableOutputsChangeNotification
default	09:46:04.622011+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c67d3 posting AVAudioSessionAvailableOutputsChangeNotification
default	09:46:04.648307+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c67d3 posting AVAudioSessionAvailableInputsChangeNotification
default	09:46:04.648386+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c67d3 posting AVAudioSessionAvailableOutputsChangeNotification
default	09:46:05.131737+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c67d3 posting AVAudioSessionAvailableOutputsChangeNotification
default	09:46:05.134232+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c67d3 posting AVAudioSessionAvailableInputsChangeNotification
default	09:46:05.139978+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c67d3 posting AVAudioSessionAvailableOutputsChangeNotification
default	09:46:05.234426+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c67d3 posting AVAudioSessionAvailableOutputsChangeNotification
default	09:46:05.254260+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c67d3 posting AVAudioSessionAvailableInputsChangeNotification
default	09:46:05.257710+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c67d3 posting AVAudioSessionAvailableOutputsChangeNotification
default	09:46:05.282854+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c67d3 posting AVAudioSessionAvailableOutputsChangeNotification
default	09:46:05.299396+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c67d3 posting AVAudioSessionAvailableInputsChangeNotification
default	09:46:05.299742+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c67d3 posting AVAudioSessionAvailableOutputsChangeNotification
default	09:46:06.737478+0800	hootowl	TX focusApplication (peekAppEvent) stealKB:Y scene:com.sharkda.hootowl-83FF55F6-7B28-4BFD-8825-33CB43E5D162
default	09:46:06.737823+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:46:06.738401+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	09:46:06.738590+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1481fc400>; contextId: 0xF4D9041F
default	09:46:06.739165+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:46:06.778723+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:46:06.778749+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	09:46:06.778779+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1481fc400>; contextId: 0xF4D9041F
default	09:46:06.818900+0800	hootowl	<UIWindowScene: 0x148378200> (83FF55F6-7B28-4BFD-8825-33CB43E5D162) Scene updated orientation preferences: ( Pu Ll Lr ) -> ( Pu )
default	09:46:06.824398+0800	hootowl	Override focusSystemState: (ENABLED) for reason(s): {(
    "<_UIAlertControllerPhoneTVMacView 0x15108ca00>"
)}
default	09:46:06.824498+0800	hootowl	Not push traits update to screen for new style 1, <UIWindowScene: 0x148378200> (83FF55F6-7B28-4BFD-8825-33CB43E5D162)
default	09:46:06.865066+0800	hootowl	RBDevice: initialized bg state: false
default	09:46:06.870538+0800	hootowl	[0x149b37700] activating connection: mach=false listener=false peer=false name=com.apple.MTLCompilerService
default	09:46:06.870748+0800	hootowl	[0x149942940] activating connection: mach=false listener=false peer=false name=com.apple.MTLCompilerService
default	09:46:06.870894+0800	hootowl	[0x1499421c0] activating connection: mach=false listener=false peer=false name=com.apple.MTLCompilerService
default	09:46:06.871056+0800	hootowl	[0x149940000] activating connection: mach=false listener=false peer=false name=com.apple.MTLCompilerService
default	09:46:06.911470+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 1
default	09:46:07.417296+0800	hootowl	<UIWindowScene: 0x148378200> (83FF55F6-7B28-4BFD-8825-33CB43E5D162) Scene updated orientation preferences: ( Pu ) -> ( Pu Ll Lr )
default	09:46:07.702476+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:46:07.702711+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	09:46:07.702761+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1481fc400>; contextId: 0xF4D9041F
default	09:46:07.704130+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:46:07.816463+0800	hootowl	TX focusApplication (peekAppEvent) stealKB:Y scene:com.sharkda.hootowl-83FF55F6-7B28-4BFD-8825-33CB43E5D162
default	09:46:07.816507+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	09:46:07.816646+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	09:46:07.816719+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1481fc400>; contextId: 0xF4D9041F
default	09:46:07.830954+0800	hootowl	Evaluating dispatch of UIEvent: 0x1494e7c00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 1
default	09:46:07.831831+0800	hootowl	<UIWindowScene: 0x148378200> (83FF55F6-7B28-4BFD-8825-33CB43E5D162) Scene updated orientation preferences: ( Pu Ll Lr ) -> ( Pu )
default	09:46:08.438925+0800	hootowl	<UIWindowScene: 0x148378200> (83FF55F6-7B28-4BFD-8825-33CB43E5D162) Scene updated orientation preferences: ( Pu ) -> ( Pu Ll Lr )
default	09:46:08.441910+0800	hootowl	Override focusSystemState: (DISABLED) for reason(s): <_UIAlertControllerPhoneTVMacView: 0x15108ca00; frame = (0 0; 240 87); layer = <CALayer: 0x1512367c0>>
default	09:46:08.442240+0800	hootowl	Not push traits update to screen for new style 1, <UIWindowScene: 0x148378200> (83FF55F6-7B28-4BFD-8825-33CB43E5D162)
default	09:46:09.751658+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c67d3 posting AVAudioSessionAvailableOutputsChangeNotification
default	09:46:09.763012+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c67d3 posting AVAudioSessionAvailableInputsChangeNotification
default	09:46:09.763859+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c67d3 posting AVAudioSessionAvailableOutputsChangeNotification
default	09:46:09.788413+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c67d3 posting AVAudioSessionAvailableOutputsChangeNotification
default	09:46:09.804923+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c67d3 posting AVAudioSessionAvailableInputsChangeNotification
default	09:46:09.804961+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c67d3 posting AVAudioSessionAvailableOutputsChangeNotification
default	09:46:09.827924+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c67d3 posting AVAudioSessionAvailableOutputsChangeNotification
default	09:46:09.846034+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c67d3 posting AVAudioSessionAvailableInputsChangeNotification
default	09:46:09.846826+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c67d3 posting AVAudioSessionAvailableOutputsChangeNotification
default	09:46:28.715461+0800	hootowl	tcp_close [C2.1.1:3] TCP Packets:
	 rcv    0.000s seq 2415041461:2415057301 ack 3020162656 win 16382 len 15840 [.] ECT0
	 rcv    0.000s seq 2415057301:2415060181 ack 3020162656 win 16382 len 2880 [.] ECT0
	 rcv    0.000s seq 2415060181:2415061621 ack 3020162656 win 16382 len 1440 [.] ECT0
	 rcv    0.000s seq 2415061621:2415063061 ack 3020162656 win 16382 len 1440 [.] ECT0
	 rcv    0.000s seq 2415063061:2415064501 ack 3020162656 win 16382 len 1440 [.] ECT0
	 rcv    0.000s seq 2415064501:2415068821 ack 3020162656 win 16382 len 4320 [.] ECT0
	 rcv    0.000s seq 2415068821:2415084661 ack 3020162656 win 16382 len 15840 [.] ECT0
	 rcv    0.000s seq 2415084661:2415100501 ack 3020162656 win 16382 len 15840 [.] ECT0
	 rcv    0.000s seq 2415100501:2415103381 ack 3020162656 win 16382 len 2880 [.] ECT0
	 rcv    0.000s seq 2415103381:2415119221 ack 3020162656 win 16382 len 15840 [.] ECT0
	 rcv    0.000s seq 2415119221:2415135061 ack 3020162656 win 16382 len 15840 [.] ECT0
	 rcv    0.000s seq 2415135061:2415136501 ack 3020162656 win 16382 len 1440 [.] ECT0
	 rcv    0.000s seq 2415136501:2415137941 ack 3020162656 win 16382 len 1440 [.] ECT0
	 rcv    0.000s seq 2415137941:2415142261 ack 3020162656 win 16382 len 4320 [.] ECT0
	 rcv    0.000s seq 2415142261:2415146581 ack 3020162656 win 16382 len 4320 [.] ECT0
	 rcv    0.000s seq 2415146581:2415149461 ack 3020162656 win 16382 len 2880 [.] ECT0
	 snd    0.000s seq 3020162656:3020162656 ack 2415149461 win 12044 len 0    [.]
	 rcv    0.000s seq 2415149461:2415160981 ack 3020162656 win 16382 len 11520 [.] ECT0
	 rcv    0.000s seq 2415160981:2415162421 ack 3020162656 win 16382 len 1440 [.] ECT0
	 rcv    0.000s seq 2415162421:2415163861 ack 3020162656 win 16382 len 1440 [.] ECT0
	 rcv    0.000s seq 2415163861:2415179701 ack 3020162656 win 16382 len 15840 [.] ECT0
	 rcv    0.000s seq 2415179701:2415181141 ack 3020162656 win 16382 len 1440 [.] ECT0
	 rcv    0.000s seq 2415181141:2415196981 ack 3020162656 win 16382 len 15840 [.] ECT0
	 rcv    0.000s seq 2415196981:2415198421 ack 3020162656 win 16382 len 1440 [.] ECT0
	 rcv    0.000s seq 2415198421:2415207061 ack 3020162656 win 16382 len 8640 [.] ECT0
	 rcv    0.000s seq 2415207061:2415222901 ack 3020162656 win 16382 len 15840 [.] ECT0
	 rcv    0.000s seq 2415222901:2415238741 ack 3020162656 win 16382 len 15840 [.] ECT0
	 rcv    0.000s seq 2415238741:2415243061 ack 3020162656 win 16382 len 4320 [.] ECT0
	 rcv    0.000s seq 2415243061:2415258901 ack 3020162656 win 16382 len 15840 [.] ECT0
	 rcv    0.000s seq 2415258901:2415271861 ack 3020162656 win 16382 len 12960 [.] ECT0
	 rcv    0.000s seq 2415271861:2415273301 ack 3020162656 win 16382 len 1440 [.] ECT0
	 rcv    0.000s seq 2415273301:2415289141 ack 3020162656 win 16382 len 15840 [.] ECT0
	 rcv    0.000s seq 2415289141:2415292092 ack 3020162656 win 16382 len 2951 [P.] ECT0
	 snd    0.000s seq 3020162656:3020162656 ack 2415292092 win 12401 len 0    [.]
	 rcv    1.068s seq 2415292092:2415292092 ack 3020162656 win 16382 len 0    [.]
	 snd   29.888s seq 3020162656:3020162680 ack 2415292092 win 12401 len 24   [P.] ECT0
	 snd    0.005s seq 3020162680:3020162681 ack 2415292092 win 12401 len 0    [F.]
	 rcv    0.066s seq 2415292092:2415292092 ack 3020162681 win 16382 len 0    [.]
	 rcv    0.006s seq 2415292092:2415292093 ack 3020162681 win 16382 len 0    [F.]
	 snd    0.000s seq 3020162681:3020162681 ack 2415292093 win 12401 len 0    [.]
	Last packet 30373ms ago.
default	09:46:34.739604+0800	hootowl	tcp_close [C1.1.1.1:3] TCP Packets:
	 snd    0.000s seq 3673467981:3673467981 ack 4180445665 win 9791  len 0    [.]
	 rcv    0.005s seq 4180445665:4180461505 ack 3673467981 win 16381 len 15840 [.] ECT0
	 rcv    0.000s seq 4180461505:4180467265 ack 3673467981 win 16381 len 5760 [.] ECT0
	 snd    0.000s seq 3673467981:3673467981 ack 4180467265 win 9791  len 0    [.]
	 rcv    0.004s seq 4180467265:4180481665 ack 3673467981 win 16381 len 14400 [.] ECT0
	 snd    0.000s seq 3673467981:3673467981 ack 4180481665 win 9791  len 0    [.]
	 rcv    0.002s seq 4180481665:4180483105 ack 3673467981 win 16381 len 1440 [.] ECT0
	 rcv    0.009s seq 4180483105:4180490305 ack 3673467981 win 16381 len 7200 [.] ECT0
	 rcv    0.000s seq 4180490305:4180493185 ack 3673467981 win 16381 len 2880 [.] ECT0
	 rcv    0.000s seq 4180493185:4180494625 ack 3673467981 win 16381 len 1440 [.] ECT0
	 rcv    0.000s seq 4180494625:4180496065 ack 3673467981 win 16381 len 1440 [.] ECT0
	 rcv    0.000s seq 4180496065:4180498945 ack 3673467981 win 16381 len 2880 [.] ECT0
	 snd    0.000s seq 3673467981:3673467981 ack 4180498945 win 9791  len 0    [.]
	 rcv    0.000s seq 4180498945:4180500385 ack 3673467981 win 16381 len 1440 [.] ECT0
	 rcv    0.000s seq 4180500385:4180509025 ack 3673467981 win 16381 len 8640 [.] ECT0
	 snd    0.000s seq 3673467981:3673467981 ack 4180509025 win 9791  len 0    [.]
	 rcv    0.001s seq 4180509025:4180513345 ack 3673467981 win 16381 len 4320 [.] ECT0
	 snd    0.000s seq 3673467981:3673467981 ack 4180513345 win 9791  len 0    [.]
	 rcv    0.026s seq 4180513345:4180524865 ack 3673467981 win 16381 len 11520 [.] ECT0
	 snd    0.000s seq 3673467981:3673467981 ack 4180524865 win 9791  len 0    [.]
	 rcv    0.041s seq 4180524865:4180527745 ack 3673467981 win 16381 len 2880 [.] ECT0
	 snd    0.001s seq 3673467981:3673467981 ack 4180527745 win 9791  len 0    [.]
	 rcv    0.007s seq 4180527745:4180543585 ack 3673467981 win 16381 len 15840 [.] ECT0
	 rcv    0.000s seq 4180543585:4180559425 ack 3673467981 win 16381 len 15840 [.] ECT0
	 rcv    0.000s seq 4180559425:4180566625 ack 3673467981 win 16381 len 7200 [.] ECT0
	 snd    0.000s seq 3673467981:3673467981 ack 4180566625 win 9791  len 0    [.]
	 rcv    0.004s seq 4180566625:4180581025 ack 3673467981 win 16381 len 14400 [.] ECT0
	 snd    0.000s seq 3673467981:3673467981 ack 4180581025 win 9791  len 0    [.]
	 rcv    0.001s seq 4180581025:4180582465 ack 3673467981 win 16381 len 1440 [.] ECT0
	 rcv    0.002s seq 4180582465:4180583905 ack 3673467981 win 16381 len 1440 [.] ECT0
	 snd    0.000s seq 3673467981:3673467981 ack 4180583905 win 9791  len 0    [.]
	 rcv    0.005s seq 4180583905:4180599745 ack 3673467981 win 16381 len 15840 [.] ECT0
	 rcv    0.000s seq 4180599745:4180612776 ack 3673467981 win 16381 len 13031 [P.] ECT0
	 snd    0.000s seq 3673467981:3673467981 ack 4180612776 win 9791  len 0    [.]
	 rcv    0.663s seq 4180612776:4180612776 ack 3673467981 win 16381 len 0    [.]
	 snd   29.760s seq 3673467981:3673468005 ack 4180612776 win 9791  len 24   [P.] ECT0
	 snd    0.001s seq 3673468005:3673468006 ack 4180612776 win 9791  len 0    [F.]
	 rcv    0.088s seq 4180612776:4180612776 ack 3673468006 win 16381 len 0    [.]
	 rcv    0.004s seq 4180612776:4180612777 ack 3673468006 win 16381 len 0    [F.]
	 snd    0.000s seq 3673468006:3673468006 ack 4180612777 win 9791  len 0    [.]
	Last packet 30981ms ago.

```