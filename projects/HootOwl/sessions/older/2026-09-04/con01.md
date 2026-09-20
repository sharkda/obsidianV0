```
default	11:00:00.320226+0800	hootowl	tcp_timers [C7.1.1.3:3] retransmit seq=3466882418 7
default	11:00:10.536169+0800	hootowl	Task <AA267BFF-52B7-464B-8EFA-242EE2D4068B>.<13> resuming, timeouts(60.0, 604800.0) qos(0x15) voucher((null)) activity(00000000-0000-0000-0000-000000000000)
default	11:00:10.540086+0800	hootowl	Connection 0: creating secure tcp or quic connection
default	11:00:10.541412+0800	hootowl	Connection 18: enabling TLS
default	11:00:10.541485+0800	hootowl	Connection 18: starting, TC(0x0)
default	11:00:10.543349+0800	hootowl	[C18 B9812D2D-024E-40E0-A08E-FD10BA727710 tcgbusfs.blob.core.windows.net:443 quic-connection, url: https://tcgbusfs.blob.core.windows.net/blobtcmsv/TCMSV_allavailable.json, definite, attribution: developer, context: com.apple.CFNetwork.NSURLSession.{D885363E-9839-4032-B958-F32329B8DC25}{(null)}{Y}{2}{0x0} (private), proc: 1B526020-2DE0-3C65-9122-F1177549D69A, delegated upid: 0] start
default	11:00:10.543520+0800	hootowl	[C18 tcgbusfs.blob.core.windows.net:443 initial parent-flow ((null))] event: path:start @0.000s
default	11:00:10.545187+0800	hootowl	[C18 tcgbusfs.blob.core.windows.net:443 waiting parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.003s, uuid: 13597A47-3BF4-4F4F-AFC0-B27C0153A507
default	11:00:10.546443+0800	hootowl	[C18 tcgbusfs.blob.core.windows.net:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_connect @0.003s
default	11:00:10.546569+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C18] reporting state preparing
default	11:00:10.546757+0800	hootowl	[C18 tcgbusfs.blob.core.windows.net:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_child @0.004s
default	11:00:10.547115+0800	hootowl	[C18.1 tcgbusfs.blob.core.windows.net:443 initial path ((null))] event: path:start @0.005s
default	11:00:10.547950+0800	hootowl	[C18.1 tcgbusfs.blob.core.windows.net:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.006s, uuid: 13597A47-3BF4-4F4F-AFC0-B27C0153A507
default	11:00:10.548207+0800	hootowl	[C18.1 tcgbusfs.blob.core.windows.net:443 in_progress transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: transform:start @0.006s
default	11:00:10.548377+0800	hootowl	[C18.1.1 tcgbusfs.blob.core.windows.net:443 initial path ((null))] event: path:start @0.007s
default	11:00:10.548974+0800	hootowl	[C18.1.1 tcgbusfs.blob.core.windows.net:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.008s, uuid: E237C58B-956E-45E8-AD64-107C093E4A86
default	11:00:10.549467+0800	hootowl	[C18.1.1 tcgbusfs.blob.core.windows.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:start_dns @0.008s
default	11:00:10.549577+0800	hootowl	Task <AA267BFF-52B7-464B-8EFA-242EE2D4068B>.<13> setting up Connection 18
default	11:00:10.603991+0800	hootowl	nw_endpoint_resolver_update [C18.1.1 tcgbusfs.blob.core.windows.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Adding endpoint handler for 20.150.22.100:443
default	11:00:10.604309+0800	hootowl	[C18.1.1 tcgbusfs.blob.core.windows.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:receive_dns @0.063s
default	11:00:10.604728+0800	hootowl	[C18.1.1.1 20.150.22.100:443 initial path ((null))] event: path:start @0.063s
default	11:00:10.605642+0800	hootowl	[C18.1.1.1 20.150.22.100:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.064s, uuid: 4276D7A6-52B9-4E21-821E-DB35F075EF3E
default	11:00:10.606076+0800	hootowl	[C18.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_nexus @0.064s
default	11:00:10.607311+0800	hootowl	[C18.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:receive_nexus @0.066s
default	11:00:10.608108+0800	hootowl	[C18.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_connect @0.067s
default	11:00:10.608655+0800	hootowl	tcp_output [C18.1.1.1:3] flags=[SEC] seq=2331441403, ack=0, win=65535 state=SYN_SENT rcv_nxt=0, snd_una=2331441403
default	11:00:10.691401+0800	hootowl	[C18.1.1 tcgbusfs.blob.core.windows.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:receive_dns @0.147s
default	11:00:10.783454+0800	hootowl	tcp_input [C18.1.1.1:3] flags=[S.E] seq=1067264017, ack=2331441404, win=65535 state=SYN_SENT rcv_nxt=0, snd_una=2331441403
default	11:00:10.783518+0800	hootowl	nw_flow_connected [C18.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Transport protocol connected (tcp)
default	11:00:10.783710+0800	hootowl	[C18.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_transport @0.242s
default	11:00:10.784861+0800	hootowl	boringssl_session_apply_protocol_options_for_transport_block_invoke_2(2367) [C18.1.1.1:2][0x14f4e11e0] TLS configured [server(0) min_version(0x0303) max_version(0x0304) name(tcgbusfs.blob.core.windows.net) tickets(false) false_start(false) enforce_ev(false) enforce_ats(false) ats_non_pfs_ciphersuite_allowed(false) cc_mode_enforced(false) ech(false) pqtls(true), pake(false) skip_ats_trust(false)]
default	11:00:10.785217+0800	hootowl	boringssl_context_info_handler(2806) [C18.1.1.1:2][0x14f4e11e0] Client handshake started
default	11:00:10.785737+0800	hootowl	boringssl_context_info_handler(2823) [C18.1.1.1:2][0x14f4e11e0] Client handshake state: TLS client enter_early_data
default	11:00:10.786088+0800	hootowl	boringssl_context_info_handler(2823) [C18.1.1.1:2][0x14f4e11e0] Client handshake state: TLS client read_server_hello
default	11:00:10.864655+0800	hootowl	boringssl_context_info_handler(2823) [C18.1.1.1:2][0x14f4e11e0] Client handshake state: TLS 1.3 client read_hello_retry_request
default	11:00:10.867620+0800	hootowl	boringssl_context_info_handler(2823) [C18.1.1.1:2][0x14f4e11e0] Client handshake state: TLS 1.3 client send_second_client_hello
default	11:00:10.867775+0800	hootowl	boringssl_context_info_handler(2823) [C18.1.1.1:2][0x14f4e11e0] Client handshake state: TLS 1.3 client read_server_hello
default	11:00:10.949661+0800	hootowl	boringssl_context_info_handler(2823) [C18.1.1.1:2][0x14f4e11e0] Client handshake state: TLS 1.3 client read_encrypted_extensions
default	11:00:10.951045+0800	hootowl	boringssl_context_info_handler(2823) [C18.1.1.1:2][0x14f4e11e0] Client handshake state: TLS 1.3 client read_certificate_request
default	11:00:10.951195+0800	hootowl	boringssl_context_info_handler(2823) [C18.1.1.1:2][0x14f4e11e0] Client handshake state: TLS 1.3 client read_server_certificate
default	11:00:10.951234+0800	hootowl	boringssl_context_info_handler(2823) [C18.1.1.1:2][0x14f4e11e0] Client handshake state: TLS 1.3 client read_server_certificate_verify
default	11:00:10.952334+0800	hootowl	boringssl_context_evaluate_trust_async(2249) [C18.1.1.1:2][0x14f4e11e0] Performing external trust evaluation
default	11:00:10.952785+0800	hootowl	boringssl_context_evaluate_trust_async_external(2234) [C18.1.1.1:2][0x14f4e11e0] Asyncing for external verify block
default	11:00:10.953082+0800	hootowl	Connection 18: asked to evaluate TLS Trust
default	11:00:10.953238+0800	hootowl	Task <AA267BFF-52B7-464B-8EFA-242EE2D4068B>.<13> auth completion disp=1 cred=0x0
default	11:00:10.953445+0800	hootowl	(Trust 0x152220780) No pending evals, starting
default	11:00:10.953960+0800	hootowl	[0x15230fac0] activating connection: mach=true listener=false peer=false name=com.apple.trustd
default	11:00:10.954303+0800	hootowl	(Trust 0x152220780) Completed async eval kickoff
default	11:00:10.964776+0800	hootowl	(Trust 0x152220780) trustd returned 4
default	11:00:10.964947+0800	hootowl	System Trust Evaluation yielded status(0)
default	11:00:10.964966+0800	hootowl	(Trust 0x150cf0a80) No pending evals, starting
default	11:00:10.965259+0800	hootowl	[0x15230df40] activating connection: mach=true listener=false peer=false name=com.apple.trustd
default	11:00:10.965468+0800	hootowl	(Trust 0x150cf0a80) Completed async eval kickoff
default	11:00:10.965797+0800	hootowl	[0x15230fac0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	11:00:10.972614+0800	hootowl	(Trust 0x150cf0a80) trustd returned 4
default	11:00:10.972742+0800	hootowl	Connection 18: TLS Trust result 0
default	11:00:10.972891+0800	hootowl	boringssl_context_evaluate_trust_async_external_block_invoke_3(2148) [C18.1.1.1:2][0x14f4e11e0] Returning from external verify block with result: true
default	11:00:10.973038+0800	hootowl	boringssl_context_certificate_verify_callback(2430) [C18.1.1.1:2][0x14f4e11e0] Certificate verification result: OK
default	11:00:10.973062+0800	hootowl	boringssl_context_info_handler(2823) [C18.1.1.1:2][0x14f4e11e0] Client handshake state: TLS 1.3 client read_server_finished
default	11:00:10.973166+0800	hootowl	boringssl_context_info_handler(2823) [C18.1.1.1:2][0x14f4e11e0] Client handshake state: TLS 1.3 client send_end_of_early_data
default	11:00:10.973181+0800	hootowl	boringssl_context_info_handler(2823) [C18.1.1.1:2][0x14f4e11e0] Client handshake state: TLS 1.3 client send_client_encrypted_extensions
default	11:00:10.973189+0800	hootowl	boringssl_context_info_handler(2823) [C18.1.1.1:2][0x14f4e11e0] Client handshake state: TLS 1.3 client send_client_certificate
default	11:00:10.973197+0800	hootowl	boringssl_context_info_handler(2823) [C18.1.1.1:2][0x14f4e11e0] Client handshake state: TLS 1.3 client complete_second_flight
default	11:00:10.973215+0800	hootowl	boringssl_context_info_handler(2823) [C18.1.1.1:2][0x14f4e11e0] Client handshake state: TLS 1.3 client done
default	11:00:10.973397+0800	hootowl	boringssl_context_info_handler(2823) [C18.1.1.1:2][0x14f4e11e0] Client handshake state: TLS client finish_client_handshake
default	11:00:10.973432+0800	hootowl	boringssl_context_info_handler(2823) [C18.1.1.1:2][0x14f4e11e0] Client handshake state: TLS client done
default	11:00:10.973464+0800	hootowl	boringssl_context_info_handler(2812) [C18.1.1.1:2][0x14f4e11e0] Client handshake done
default	11:00:10.973743+0800	hootowl	nw_protocol_boringssl_signal_connected(895) [C18.1.1.1:2][0x14f4e11e0] TLS connected [server(0) version(0x0304) ciphersuite(TLS_AES_256_GCM_SHA384) group(0x0018) signature_alg(0x0804) alpn(nil) resumed(0) offered_ticket(0) in_early_data(0) early_data_accepted(0) false_started(0) ocsp_received(1) sct_received(0) connect_time(189ms) flight_time(158ms) rtt(79ms) write_stalls(0) read_stalls(10) pake(0x0000)]
default	11:00:10.973875+0800	hootowl	nw_flow_connected [C18.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (CFNetworkConnection-3170269070)
default	11:00:10.974133+0800	hootowl	[C18.1.1.1 20.150.22.100:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.433s
default	11:00:10.974280+0800	hootowl	[C18.1.1 tcgbusfs.blob.core.windows.net:443 ready resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.433s
default	11:00:10.974334+0800	hootowl	[C18.1 tcgbusfs.blob.core.windows.net:443 ready transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.433s
default	11:00:10.974430+0800	hootowl	[C18.1.1.1 20.150.22.100:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.433s
default	11:00:10.974505+0800	hootowl	[C18.1.1 tcgbusfs.blob.core.windows.net:443 ready resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.433s
default	11:00:10.974545+0800	hootowl	[C18.1 tcgbusfs.blob.core.windows.net:443 ready transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.433s
default	11:00:10.974611+0800	hootowl	nw_flow_connected [C18 20.150.22.100:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (endpoint_flow)
default	11:00:10.974662+0800	hootowl	[C18 20.150.22.100:443 ready parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_connect @0.433s
default	11:00:10.974997+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C18] reporting state ready
default	11:00:10.975052+0800	hootowl	[C18 20.150.22.100:443 ready parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.434s
default	11:00:10.975061+0800	hootowl	nw_connection_send_viability_changed_on_nw_queue [C18] viability_changed_handler(true)
default	11:00:10.975090+0800	hootowl	[0x15230df40] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	11:00:10.975120+0800	hootowl	Connection 18: connected successfully
default	11:00:10.975126+0800	hootowl	Connection 18: TLS handshake complete
default	11:00:10.975133+0800	hootowl	Connection 18: ready C(N) E(N)
default	11:00:10.975203+0800	hootowl	Task <AA267BFF-52B7-464B-8EFA-242EE2D4068B>.<13> now using Connection 18
default	11:00:10.975256+0800	hootowl	Connection 18: received viability advisory(Y)
default	11:00:10.975379+0800	hootowl	Task <AA267BFF-52B7-464B-8EFA-242EE2D4068B>.<13> sent request, body N 0
default	11:00:11.099603+0800	hootowl	Task <AA267BFF-52B7-464B-8EFA-242EE2D4068B>.<13> received response, status 304 content K
default	11:00:11.100322+0800	hootowl	Task <AA267BFF-52B7-464B-8EFA-242EE2D4068B>.<13> done using Connection 18
default	11:00:11.100442+0800	hootowl	[C18] event: client:connection_idle @0.559s
default	11:00:11.100579+0800	hootowl	nw_protocol_tcp_notify [C18.1.1.1:3] nw_protocol_notification_type_connection_idle is true
default	11:00:11.100624+0800	hootowl	Task <AA267BFF-52B7-464B-8EFA-242EE2D4068B>.<13> summary for task success {transaction_duration_ms=563, response_status=304, connection=18, protocol="http/1.1", domain_lookup_duration_ms=55, connect_duration_ms=366, secure_connection_duration_ms=189, private_relay=false, request_start_ms=438, request_duration_ms=0, response_start_ms=562, response_duration_ms=0, request_bytes=337, request_throughput_kbps=32919, response_bytes=308, response_throughput_kbps=4563, cache_hit=true}
default	11:00:11.100683+0800	hootowl	nw_protocol_tcp_set_connection_idle [C18.1.1.1:3] os_nexus_flow_set_connection_idle returned 0
default	11:00:11.100748+0800	hootowl	[C18] event: client:connection_idle @0.559s
default	11:00:11.101079+0800	hootowl	nw_protocol_tcp_notify [C18.1.1.1:3] nw_protocol_notification_type_connection_idle is true
default	11:00:11.101306+0800	hootowl	nw_protocol_tcp_set_connection_idle [C18.1.1.1:3] os_nexus_flow_set_connection_idle returned 0
default	11:00:11.101475+0800	hootowl	Task <AA267BFF-52B7-464B-8EFA-242EE2D4068B>.<13> finished successfully
default	11:00:11.101666+0800	hootowl	Mu1Base+Ext 152
taipei 📦 minutely Received 472943 bytes
default	11:00:11.102565+0800	hootowl	Mu1Base+Ext 177
previousHash not changed
default	11:00:11.112838+0800	hootowl	MncplCyclopsScreen 166
🦵 uiKick received — syncing items
default	11:00:11.113296+0800	hootowl	Municipal+Cyclops 93
🎨 model refreshed — obs:0s car:7 thread:main 🆔 12708723194660554214
default	11:00:11.115277+0800	hootowl	MncplCyclopsScreen 78
🏠 body eval — items:6 firstObs:0s firstCar:7
default	11:00:33.383934+0800	hootowl	tcp_timers [C1.1.1.1:3] retransmit seq=2721530959 9
default	11:00:33.384361+0800	hootowl	tcp_output [C1.1.1.1:3] flags=[FP.] seq=2721530959, ack=1177347048, win=7359 state=FIN_WAIT_1 rcv_nxt=1177347048, snd_una=2721530959
default	11:00:42.184442+0800	hootowl	Connection 18: cleaning up
default	11:00:42.184465+0800	hootowl	[C18 B9812D2D-024E-40E0-A08E-FD10BA727710 tcgbusfs.blob.core.windows.net:443 quic-connection, url: https://tcgbusfs.blob.core.windows.net/blobtcmsv/TCMSV_allavailable.json, definite, attribution: developer] cancel
default	11:00:42.186712+0800	hootowl	[C18 B9812D2D-024E-40E0-A08E-FD10BA727710 tcgbusfs.blob.core.windows.net:443 quic-connection, url: https://tcgbusfs.blob.core.windows.net/blobtcmsv/TCMSV_allavailable.json, definite, attribution: developer] cancelled
	[C18.1.1.1 4276D7A6-52B9-4E21-821E-DB35F075EF3E 192.168.50.191:56387<->20.150.22.100:443]
	Connected Path: satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good
	Privacy Stance: Not Eligible
	Duration: 31.638s, DNS @0.008s took 0.055s, TCP @0.067s took 0.175s,  took 0.189s
	bytes in/out: 10765/2357, packets in/out: 8/14, rtt: 0.144s, retransmitted bytes: 0, out-of-order bytes: 0
	ecn packets sent/acked/marked/lost: 5/4/0/0
default	11:00:42.186986+0800	hootowl	nw_protocol_tcp_log_summary [C18.1.1.1:3] 
	[5AC75DA4-CCB9-458F-87D7-C0A939FF5B7A 192.168.50.191:56387<->20.150.22.100:443]
	Init: 1, Conn_Time: 174.957ms, SYNs: 1, WR_T: 0/0, RD_T: 0/0, TFO: 0/0/0, ECN: 0/1/1, Accurate ECN (client/server): Disabled/Disabled, TS: 1, TSO: 0
	rtt_cache: process, rtt_upd: 5, rtt: 144.312ms, rtt_var: 63.125ms rtt_nc: 144.312ms, rtt_var_nc: 63.125ms base rtt: 65ms
	ACKs-compressed: 0, ACKs delayed: 0 delayed ACKs sent: 0
default	11:00:42.187732+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C18] reporting state cancelled
default	11:00:42.187745+0800	hootowl	Connection 18: done
default	11:00:42.187814+0800	hootowl	tcp_output [C18.1.1.1:3] flags=[F.] seq=2331443785, ack=1067274783, win=2048 state=FIN_WAIT_1 rcv_nxt=1067274783, snd_una=2331443761
default	11:00:42.266911+0800	hootowl	tcp_input [C18.1.1.1:3] flags=[F.] seq=1067274783, ack=2331443786, win=16382 state=FIN_WAIT_2 rcv_nxt=1067274783, snd_una=2331443786
default	11:01:04.325484+0800	hootowl	tcp_timers [C7.1.1.3:3] retransmit seq=3466882418 8
default	11:01:12.383620+0800	hootowl	tcp_close [C18.1.1.1:3] TCP Packets:
	 snd    0.000s seq 2331441403:2331441404 ack 0          win 65535 len 0    [SEC]
	 rcv    0.175s seq 1067264017:1067264018 ack 2331441404 win 65535 len 0    [S.E] ECT0
	 snd    0.000s seq 2331441404:2331441404 ack 1067264018 win 2053  len 0    [.]
	 snd    0.003s seq 2331441404:2331442832 ack 1067264018 win 2053  len 1428 [.] ECT0
	 snd    0.000s seq 2331442832:2331442943 ack 1067264018 win 2053  len 111  [P.] ECT0
	 rcv    0.076s seq 1067264018:1067264018 ack 2331442943 win 16385 len 0    [.]
	 rcv    0.002s seq 1067264018:1067264117 ack 2331442943 win 16385 len 99   [P.] ECT0
	 snd    0.000s seq 2331442943:2331442943 ack 1067264117 win 2052  len 0    [.]
	 snd    0.004s seq 2331442943:2331443328 ack 1067264117 win 2052  len 385  [P.] ECT0
	 rcv    0.078s seq 1067264117:1067265557 ack 2331443328 win 16384 len 1440 [.] ECT0
	 snd    0.000s seq 2331443328:2331443328 ack 1067265557 win 2030  len 0    [.]
	 rcv    0.005s seq 1067265557:1067274350 ack 2331443328 win 16384 len 8793 [P.] ECT0
	 snd    0.000s seq 2331443328:2331443328 ack 1067274350 win 1911  len 0    [.]
	 snd    0.000s seq 2331443328:2331443328 ack 1067274350 win 2048  len 0    [.]
	 snd    0.022s seq 2331443328:2331443402 ack 1067274350 win 2048  len 74   [P.] ECT0
	 snd    0.002s seq 2331443402:2331443761 ack 1067274350 win 2048  len 359  [P.] ECT0
	 rcv    0.111s seq 1067274350:1067274453 ack 2331443402 win 16383 len 103  [P.] ECT0
	 snd    0.000s seq 2331443761:2331443761 ack 1067274453 win 2047  len 0    [.]
	 rcv    0.013s seq 1067274453:1067274783 ack 2331443761 win 16382 len 330  [P.] ECT0
	 snd    0.000s seq 2331443761:2331443761 ack 1067274783 win 2043  len 0    [.]
	 rcv    0.888s seq 1067274783:1067274783 ack 2331443761 win 16382 len 0    [.]
	 snd   30.192s seq 2331443761:2331443785 ack 1067274783 win 2048  len 24   [P.] ECT0
	 snd    0.003s seq 2331443785:2331443786 ack 1067274783 win 2048  len 0    [F.]
	 rcv    0.081s seq 1067274783:1067274783 ack 2331443786 win 16382 len 0    [.]
	 rcv    0.000s seq 1067274783:1067274784 ack 2331443786 win 16382 len 0    [F.]
	 snd    0.000s seq 2331443786:2331443786 ack 1067274784 win 2048  len 0    [.]
	Last packet 30115ms ago.
default	11:01:37.389292+0800	hootowl	tcp_timers [C1.1.1.1:3] retransmit seq=2721530959 10
default	11:01:37.389374+0800	hootowl	tcp_output [C1.1.1.1:3] flags=[FP.] seq=2721530959, ack=1177347048, win=7359 state=FIN_WAIT_1 rcv_nxt=1177347048, snd_una=2721530959
default	11:02:08.331943+0800	hootowl	tcp_timers [C7.1.1.3:3] retransmit seq=3466882418 9
default	11:02:11.117147+0800	hootowl	Task <4478B31E-21B9-4C79-8F7C-186BA02BF88A>.<14> resuming, timeouts(60.0, 604800.0) qos(0x15) voucher((null)) activity(00000000-0000-0000-0000-000000000000)
default	11:02:11.123229+0800	hootowl	Connection 0: creating secure tcp or quic connection
default	11:02:11.123708+0800	hootowl	Connection 19: enabling TLS
default	11:02:11.123739+0800	hootowl	Connection 19: starting, TC(0x0)
default	11:02:11.123820+0800	hootowl	[C19 69A7A193-1261-4953-A53B-6423F73A6376 tcgbusfs.blob.core.windows.net:443 quic-connection, url: https://tcgbusfs.blob.core.windows.net/blobtcmsv/TCMSV_allavailable.json, definite, attribution: developer, context: com.apple.CFNetwork.NSURLSession.{D885363E-9839-4032-B958-F32329B8DC25}{(null)}{Y}{2}{0x0} (private), proc: 1B526020-2DE0-3C65-9122-F1177549D69A, delegated upid: 0] start
default	11:02:11.123964+0800	hootowl	[C19 tcgbusfs.blob.core.windows.net:443 initial parent-flow ((null))] event: path:start @0.000s
default	11:02:11.125473+0800	hootowl	[C19 tcgbusfs.blob.core.windows.net:443 waiting parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.001s, uuid: A9751AD5-7A34-40DE-9A72-BCC94D0AABCD
default	11:02:11.126427+0800	hootowl	[C19 tcgbusfs.blob.core.windows.net:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_connect @0.001s
default	11:02:11.126446+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C19] reporting state preparing
default	11:02:11.126502+0800	hootowl	[C19 tcgbusfs.blob.core.windows.net:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_child @0.002s
default	11:02:11.126566+0800	hootowl	[C19.1 tcgbusfs.blob.core.windows.net:443 initial path ((null))] event: path:start @0.002s
default	11:02:11.126753+0800	hootowl	[C19.1 tcgbusfs.blob.core.windows.net:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.002s, uuid: A9751AD5-7A34-40DE-9A72-BCC94D0AABCD
default	11:02:11.126876+0800	hootowl	[C19.1 tcgbusfs.blob.core.windows.net:443 in_progress transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: transform:start @0.002s
default	11:02:11.127048+0800	hootowl	[C19.1.1 tcgbusfs.blob.core.windows.net:443 initial path ((null))] event: path:start @0.003s
default	11:02:11.128637+0800	hootowl	[C19.1.1 tcgbusfs.blob.core.windows.net:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.004s, uuid: A708B3AB-2E0E-4E5A-B1F6-D45BDD6FB30B
default	11:02:11.128710+0800	hootowl	[C19.1.1 tcgbusfs.blob.core.windows.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:start_dns @0.004s
default	11:02:11.128742+0800	hootowl	Task <4478B31E-21B9-4C79-8F7C-186BA02BF88A>.<14> setting up Connection 19
default	11:02:11.153368+0800	hootowl	nw_endpoint_resolver_update [C19.1.1 tcgbusfs.blob.core.windows.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Adding endpoint handler for 20.150.22.100:443
default	11:02:11.153887+0800	hootowl	[C19.1.1 tcgbusfs.blob.core.windows.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:receive_dns @0.029s
default	11:02:11.155431+0800	hootowl	[C19.1.1.1 20.150.22.100:443 initial path ((null))] event: path:start @0.030s
default	11:02:11.157210+0800	hootowl	[C19.1.1.1 20.150.22.100:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.031s, uuid: C3021194-CD7F-4A88-BEC8-7B5C1E92AF39
default	11:02:11.157361+0800	hootowl	[C19.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_nexus @0.032s
default	11:02:11.158854+0800	hootowl	[C19.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:receive_nexus @0.033s
default	11:02:11.160058+0800	hootowl	[C19.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_connect @0.035s
default	11:02:11.160284+0800	hootowl	tcp_output [C19.1.1.1:3] flags=[SEC] seq=722854327, ack=0, win=65535 state=SYN_SENT rcv_nxt=0, snd_una=722854327
default	11:02:11.275401+0800	hootowl	tcp_input [C19.1.1.1:3] flags=[S.E] seq=2822589646, ack=722854328, win=65535 state=SYN_SENT rcv_nxt=0, snd_una=722854327
default	11:02:11.275449+0800	hootowl	nw_flow_connected [C19.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Transport protocol connected (tcp)
default	11:02:11.275907+0800	hootowl	[C19.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_transport @0.151s
default	11:02:11.277082+0800	hootowl	boringssl_session_apply_protocol_options_for_transport_block_invoke_2(2367) [C19.1.1.1:2][0x14ef765e0] TLS configured [server(0) min_version(0x0303) max_version(0x0304) name(tcgbusfs.blob.core.windows.net) tickets(false) false_start(false) enforce_ev(false) enforce_ats(false) ats_non_pfs_ciphersuite_allowed(false) cc_mode_enforced(false) ech(false) pqtls(true), pake(false) skip_ats_trust(false)]
default	11:02:11.277296+0800	hootowl	boringssl_context_info_handler(2806) [C19.1.1.1:2][0x14ef765e0] Client handshake started
default	11:02:11.277802+0800	hootowl	boringssl_context_info_handler(2823) [C19.1.1.1:2][0x14ef765e0] Client handshake state: TLS client enter_early_data
default	11:02:11.278142+0800	hootowl	boringssl_context_info_handler(2823) [C19.1.1.1:2][0x14ef765e0] Client handshake state: TLS client read_server_hello
default	11:02:11.406353+0800	hootowl	boringssl_context_info_handler(2823) [C19.1.1.1:2][0x14ef765e0] Client handshake state: TLS 1.3 client read_hello_retry_request
default	11:02:11.407546+0800	hootowl	boringssl_context_info_handler(2823) [C19.1.1.1:2][0x14ef765e0] Client handshake state: TLS 1.3 client send_second_client_hello
default	11:02:11.407624+0800	hootowl	boringssl_context_info_handler(2823) [C19.1.1.1:2][0x14ef765e0] Client handshake state: TLS 1.3 client read_server_hello
default	11:02:11.514411+0800	hootowl	boringssl_context_info_handler(2823) [C19.1.1.1:2][0x14ef765e0] Client handshake state: TLS 1.3 client read_encrypted_extensions
default	11:02:11.517393+0800	hootowl	boringssl_context_info_handler(2823) [C19.1.1.1:2][0x14ef765e0] Client handshake state: TLS 1.3 client read_certificate_request
default	11:02:11.517575+0800	hootowl	boringssl_context_info_handler(2823) [C19.1.1.1:2][0x14ef765e0] Client handshake state: TLS 1.3 client read_server_certificate
default	11:02:11.517657+0800	hootowl	boringssl_context_info_handler(2823) [C19.1.1.1:2][0x14ef765e0] Client handshake state: TLS 1.3 client read_server_certificate_verify
default	11:02:11.518126+0800	hootowl	boringssl_context_evaluate_trust_async(2249) [C19.1.1.1:2][0x14ef765e0] Performing external trust evaluation
default	11:02:11.518173+0800	hootowl	boringssl_context_evaluate_trust_async_external(2234) [C19.1.1.1:2][0x14ef765e0] Asyncing for external verify block
default	11:02:11.518294+0800	hootowl	Connection 19: asked to evaluate TLS Trust
default	11:02:11.518815+0800	hootowl	Task <4478B31E-21B9-4C79-8F7C-186BA02BF88A>.<14> auth completion disp=1 cred=0x0
default	11:02:11.519316+0800	hootowl	(Trust 0x152220000) No pending evals, starting
default	11:02:11.519922+0800	hootowl	[0x15230df40] activating connection: mach=true listener=false peer=false name=com.apple.trustd
default	11:02:11.520260+0800	hootowl	(Trust 0x152220000) Completed async eval kickoff
default	11:02:11.531239+0800	hootowl	(Trust 0x152220000) trustd returned 4
default	11:02:11.531335+0800	hootowl	System Trust Evaluation yielded status(0)
default	11:02:11.531399+0800	hootowl	(Trust 0x1522212c0) No pending evals, starting
default	11:02:11.531724+0800	hootowl	[0x15230fac0] activating connection: mach=true listener=false peer=false name=com.apple.trustd
default	11:02:11.531932+0800	hootowl	(Trust 0x1522212c0) Completed async eval kickoff
default	11:02:11.532154+0800	hootowl	[0x15230df40] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	11:02:11.538624+0800	hootowl	(Trust 0x1522212c0) trustd returned 4
default	11:02:11.538770+0800	hootowl	Connection 19: TLS Trust result 0
default	11:02:11.538799+0800	hootowl	boringssl_context_evaluate_trust_async_external_block_invoke_3(2148) [C19.1.1.1:2][0x14ef765e0] Returning from external verify block with result: true
default	11:02:11.538908+0800	hootowl	boringssl_context_certificate_verify_callback(2430) [C19.1.1.1:2][0x14ef765e0] Certificate verification result: OK
default	11:02:11.538933+0800	hootowl	boringssl_context_info_handler(2823) [C19.1.1.1:2][0x14ef765e0] Client handshake state: TLS 1.3 client read_server_finished
default	11:02:11.538980+0800	hootowl	boringssl_context_info_handler(2823) [C19.1.1.1:2][0x14ef765e0] Client handshake state: TLS 1.3 client send_end_of_early_data
default	11:02:11.539005+0800	hootowl	boringssl_context_info_handler(2823) [C19.1.1.1:2][0x14ef765e0] Client handshake state: TLS 1.3 client send_client_encrypted_extensions
default	11:02:11.539027+0800	hootowl	boringssl_context_info_handler(2823) [C19.1.1.1:2][0x14ef765e0] Client handshake state: TLS 1.3 client send_client_certificate
default	11:02:11.539051+0800	hootowl	boringssl_context_info_handler(2823) [C19.1.1.1:2][0x14ef765e0] Client handshake state: TLS 1.3 client complete_second_flight
default	11:02:11.539094+0800	hootowl	boringssl_context_info_handler(2823) [C19.1.1.1:2][0x14ef765e0] Client handshake state: TLS 1.3 client done
default	11:02:11.539237+0800	hootowl	boringssl_context_info_handler(2823) [C19.1.1.1:2][0x14ef765e0] Client handshake state: TLS client finish_client_handshake
default	11:02:11.539288+0800	hootowl	boringssl_context_info_handler(2823) [C19.1.1.1:2][0x14ef765e0] Client handshake state: TLS client done
default	11:02:11.539314+0800	hootowl	boringssl_context_info_handler(2812) [C19.1.1.1:2][0x14ef765e0] Client handshake done
default	11:02:11.539578+0800	hootowl	nw_protocol_boringssl_signal_connected(895) [C19.1.1.1:2][0x14ef765e0] TLS connected [server(0) version(0x0304) ciphersuite(TLS_AES_256_GCM_SHA384) group(0x0018) signature_alg(0x0804) alpn(nil) resumed(0) offered_ticket(0) in_early_data(0) early_data_accepted(0) false_started(0) ocsp_received(1) sct_received(0) connect_time(263ms) flight_time(233ms) rtt(129ms) write_stalls(0) read_stalls(10) pake(0x0000)]
default	11:02:11.539724+0800	hootowl	nw_flow_connected [C19.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (CFNetworkConnection-3170269070)
default	11:02:11.539858+0800	hootowl	[C19.1.1.1 20.150.22.100:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.415s
default	11:02:11.540040+0800	hootowl	[C19.1.1 tcgbusfs.blob.core.windows.net:443 ready resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.416s
default	11:02:11.540091+0800	hootowl	[C19.1 tcgbusfs.blob.core.windows.net:443 ready transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.416s
default	11:02:11.540199+0800	hootowl	[C19.1.1.1 20.150.22.100:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.416s
default	11:02:11.540314+0800	hootowl	[C19.1.1 tcgbusfs.blob.core.windows.net:443 ready resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.416s
default	11:02:11.540409+0800	hootowl	[C19.1 tcgbusfs.blob.core.windows.net:443 ready transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.416s
default	11:02:11.540433+0800	hootowl	nw_flow_connected [C19 20.150.22.100:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (endpoint_flow)
default	11:02:11.540533+0800	hootowl	[C19 20.150.22.100:443 ready parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_connect @0.416s
default	11:02:11.540721+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C19] reporting state ready
default	11:02:11.540781+0800	hootowl	[C19 20.150.22.100:443 ready parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.416s
default	11:02:11.540800+0800	hootowl	nw_connection_send_viability_changed_on_nw_queue [C19] viability_changed_handler(true)
default	11:02:11.540833+0800	hootowl	[0x15230fac0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	11:02:11.540864+0800	hootowl	Connection 19: connected successfully
default	11:02:11.540889+0800	hootowl	Connection 19: TLS handshake complete
default	11:02:11.540909+0800	hootowl	Connection 19: ready C(N) E(N)
default	11:02:11.541064+0800	hootowl	Task <4478B31E-21B9-4C79-8F7C-186BA02BF88A>.<14> now using Connection 19
default	11:02:11.541095+0800	hootowl	Connection 19: received viability advisory(Y)
default	11:02:11.541203+0800	hootowl	Task <4478B31E-21B9-4C79-8F7C-186BA02BF88A>.<14> sent request, body N 0
default	11:02:11.632741+0800	hootowl	Task <4478B31E-21B9-4C79-8F7C-186BA02BF88A>.<14> received response, status 200 content K
default	11:02:12.019193+0800	hootowl	Task <4478B31E-21B9-4C79-8F7C-186BA02BF88A>.<14> response ended
default	11:02:12.019767+0800	hootowl	Task <4478B31E-21B9-4C79-8F7C-186BA02BF88A>.<14> done using Connection 19
default	11:02:12.019898+0800	hootowl	[C19] event: client:connection_idle @0.895s
default	11:02:12.020240+0800	hootowl	Task <4478B31E-21B9-4C79-8F7C-186BA02BF88A>.<14> summary for task success {transaction_duration_ms=901, response_status=200, connection=19, protocol="http/1.1", domain_lookup_duration_ms=25, connect_duration_ms=381, secure_connection_duration_ms=263, private_relay=false, request_start_ms=422, request_duration_ms=0, response_start_ms=514, response_duration_ms=386, request_bytes=337, request_throughput_kbps=36418, response_bytes=473388, response_throughput_kbps=9788, cache_hit=true}
default	11:02:12.020293+0800	hootowl	nw_protocol_tcp_notify [C19.1.1.1:3] nw_protocol_notification_type_connection_idle is true
default	11:02:12.020394+0800	hootowl	nw_protocol_tcp_set_connection_idle [C19.1.1.1:3] os_nexus_flow_set_connection_idle returned 0
default	11:02:12.020562+0800	hootowl	[C19] event: client:connection_idle @0.896s
default	11:02:12.021564+0800	hootowl	nw_protocol_tcp_notify [C19.1.1.1:3] nw_protocol_notification_type_connection_idle is true
default	11:02:12.021616+0800	hootowl	nw_protocol_tcp_set_connection_idle [C19.1.1.1:3] os_nexus_flow_set_connection_idle returned 0
default	11:02:12.021637+0800	hootowl	Task <4478B31E-21B9-4C79-8F7C-186BA02BF88A>.<14> finished successfully
default	11:02:12.021677+0800	hootowl	Mu1Base+Ext 152
taipei 📦 minutely Received 472935 bytes
default	11:02:12.022816+0800	hootowl	Mu1Base+Ext 175
previousHash updated
default	11:02:12.051692+0800	hootowl	MncplCyclopsScreen 166
🦵 uiKick received — syncing items
default	11:02:12.051776+0800	hootowl	Municipal+Cyclops 93
🎨 model refreshed — obs:0s car:7 thread:main 🆔 12708723194660554214
error	11:02:12.056802+0800	hootowl	333	wireAvailableUpdateFromMunicipal()	⚠️ duplicate parkIds in avail feed (11): 040014(綠寶石區, ?), 040037(綠光河岸區, ?), 040068(玉清宮, ?), 060021(陽光運動公園, ?), 060047(親情河濱公園1區, ?), 060068(萊茵區, ?), 060079(城市車旅新店安德二, ?), 060085(親情河濱公園2區, ?), 060085(親情河濱公園2區, ?), 170120(MITSUI OUTLET PARK 林口二館收費, ?), 170120(MITSUI OUTLET PARK 林口二館收費, ?)
default	11:02:12.057338+0800	hootowl	Municipal 130
🐎 minutelyAvailable ["newTaipeiCity ⏳04 10:54 ∑1428", "taipei ⏳04 11:02 ∑1175"]
default	11:02:12.067224+0800	hootowl	MncplCyclopsScreen 166
🦵 uiKick received — syncing items
default	11:02:12.067276+0800	hootowl	Municipal+Cyclops 93
🎨 model refreshed — obs:0s car:7 thread:main 🆔 12708723194660554214
default	11:02:12.077657+0800	hootowl	MncplCyclopsScreen 78
🏠 body eval — items:6 firstObs:0s firstCar:7
default	11:02:41.395210+0800	hootowl	tcp_timers [C1.1.1.1:3] retransmit seq=2721530959 11
default	11:02:41.395426+0800	hootowl	tcp_output [C1.1.1.1:3] flags=[FP.] seq=2721530959, ack=1177347048, win=7359 state=FIN_WAIT_1 rcv_nxt=1177347048, snd_una=2721530959
default	11:02:42.811347+0800	hootowl	Connection 19: cleaning up
default	11:02:42.811472+0800	hootowl	[C19 69A7A193-1261-4953-A53B-6423F73A6376 tcgbusfs.blob.core.windows.net:443 quic-connection, url: https://tcgbusfs.blob.core.windows.net/blobtcmsv/TCMSV_allavailable.json, definite, attribution: developer] cancel
default	11:02:42.812264+0800	hootowl	[C19 69A7A193-1261-4953-A53B-6423F73A6376 tcgbusfs.blob.core.windows.net:443 quic-connection, url: https://tcgbusfs.blob.core.windows.net/blobtcmsv/TCMSV_allavailable.json, definite, attribution: developer] cancelled
	[C19.1.1.1 C3021194-CD7F-4A88-BEC8-7B5C1E92AF39 192.168.50.191:56389<->20.150.22.100:443]
	Connected Path: satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good
	Privacy Stance: Not Eligible
	Duration: 31.687s, DNS @0.004s took 0.025s, TCP @0.035s took 0.116s,  took 0.263s
	bytes in/out: 484461/2357, packets in/out: 91/87, rtt: 0.105s, retransmitted bytes: 0, out-of-order bytes: 0
	ecn packets sent/acked/marked/lost: 5/4/0/0
default	11:02:42.813385+0800	hootowl	nw_protocol_tcp_log_summary [C19.1.1.1:3] 
	[184BA066-945A-49BE-BBA5-1D9B06D753A1 192.168.50.191:56389<->20.150.22.100:443]
	Init: 1, Conn_Time: 115.155ms, SYNs: 1, WR_T: 0/0, RD_T: 0/0, TFO: 0/0/0, ECN: 0/1/1, Accurate ECN (client/server): Disabled/Disabled, TS: 1, TSO: 0
	rtt_cache: process, rtt_upd: 5, rtt: 105.093ms, rtt_var: 38.375ms rtt_nc: 105.093ms, rtt_var_nc: 38.375ms base rtt: 65ms
	ACKs-compressed: 5, ACKs delayed: 57 delayed ACKs sent: 0
default	11:02:42.814564+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C19] reporting state cancelled
default	11:02:42.814583+0800	hootowl	Connection 19: done
default	11:02:42.814753+0800	hootowl	tcp_output [C19.1.1.1:3] flags=[F.] seq=722856709, ack=2823074108, win=8452 state=FIN_WAIT_1 rcv_nxt=2823074108, snd_una=722856685
default	11:02:42.884548+0800	hootowl	tcp_input [C19.1.1.1:3] flags=[F.] seq=2823074108, ack=722856710, win=16382 state=FIN_WAIT_2 rcv_nxt=2823074108, snd_una=722856710
default	11:03:06.045737+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:03:06.066745+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c6554 posting AVAudioSessionAvailableInputsChangeNotification
default	11:03:06.070555+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:03:06.110759+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:03:06.127036+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c6554 posting AVAudioSessionAvailableInputsChangeNotification
default	11:03:06.127131+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:03:06.156774+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:03:06.167139+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c6554 posting AVAudioSessionAvailableInputsChangeNotification
default	11:03:06.167150+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:03:06.178597+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:03:06.185168+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c6554 posting AVAudioSessionAvailableInputsChangeNotification
default	11:03:06.185180+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:03:06.772288+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:03:06.782929+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c6554 posting AVAudioSessionAvailableInputsChangeNotification
default	11:03:06.783045+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:03:06.801327+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:03:06.809020+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c6554 posting AVAudioSessionAvailableInputsChangeNotification
default	11:03:06.809168+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:03:06.823931+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:03:06.832143+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c6554 posting AVAudioSessionAvailableInputsChangeNotification
default	11:03:06.832216+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:03:12.334533+0800	hootowl	tcp_timers [C7.1.1.3:3] retransmit seq=3466882418 10
default	11:03:13.006020+0800	hootowl	tcp_close [C19.1.1.1:3] TCP Packets:
	 snd    0.000s seq  722856685:722856685  ack 2822876562 win 4949  len 0    [.]
	 rcv    0.000s seq 2822876562:2822878002 ack 722856685  win 16382 len 1440 [.] ECT0
	 rcv    0.000s seq 2822878002:2822880882 ack 722856685  win 16382 len 2880 [.] ECT0
	 snd    0.000s seq  722856685:722856685  ack 2822880882 win 4949  len 0    [.]
	 rcv    0.000s seq 2822880882:2822882322 ack 722856685  win 16382 len 1440 [.] ECT0
	 rcv    0.001s seq 2822882322:2822883762 ack 722856685  win 16382 len 1440 [.] ECT0
	 snd    0.000s seq  722856685:722856685  ack 2822883762 win 4949  len 0    [.]
	 rcv    0.001s seq 2822883762:2822893842 ack 722856685  win 16382 len 10080 [.] ECT0
	 snd    0.000s seq  722856685:722856685  ack 2822893842 win 4949  len 0    [.]
	 rcv    0.035s seq 2822893842:2822895282 ack 722856685  win 16382 len 1440 [.] ECT0
	 snd    0.000s seq  722856685:722856685  ack 2822895282 win 8430  len 0    [.]
	 rcv    0.004s seq 2822895282:2822911122 ack 722856685  win 16382 len 15840 [.] ECT0
	 rcv    0.000s seq 2822911122:2822921202 ack 722856685  win 16382 len 10080 [.] ECT0
	 snd    0.001s seq  722856685:722856685  ack 2822921202 win 8452  len 0    [.]
	 rcv    0.052s seq 2822921202:2822937042 ack 722856685  win 16382 len 15840 [.] ECT0
	 snd    0.000s seq  722856685:722856685  ack 2822937042 win 8452  len 0    [.]
	 rcv    0.003s seq 2822937042:2822952882 ack 722856685  win 16382 len 15840 [.] ECT0
	 rcv    0.000s seq 2822952882:2822965842 ack 722856685  win 16382 len 12960 [.] ECT0
	 snd    0.000s seq  722856685:722856685  ack 2822965842 win 8452  len 0    [.]
	 rcv    0.002s seq 2822965842:2822968722 ack 722856685  win 16382 len 2880 [.] ECT0
	 snd    0.000s seq  722856685:722856685  ack 2822968722 win 8452  len 0    [.]
	 rcv    0.003s seq 2822968722:2822984562 ack 722856685  win 16382 len 15840 [.] ECT0
	 rcv    0.000s seq 2822984562:2822998962 ack 722856685  win 16382 len 14400 [.] ECT0
	 snd    0.000s seq  722856685:722856685  ack 2822998962 win 8452  len 0    [.]
	 rcv    0.006s seq 2822998962:2823014802 ack 722856685  win 16382 len 15840 [.] ECT0
	 rcv    0.000s seq 2823014802:2823030642 ack 722856685  win 16382 len 15840 [.] ECT0
	 rcv    0.000s seq 2823030642:2823033522 ack 722856685  win 16382 len 2880 [.] ECT0
	 snd    0.000s seq  722856685:722856685  ack 2823033522 win 8452  len 0    [.]
	 rcv    0.005s seq 2823033522:2823040722 ack 722856685  win 16382 len 7200 [.] ECT0
	 snd    0.000s seq  722856685:722856685  ack 2823040722 win 8452  len 0    [.]
	 rcv    0.005s seq 2823040722:2823056562 ack 722856685  win 16382 len 15840 [.] ECT0
	 rcv    0.000s seq 2823056562:2823072402 ack 722856685  win 16382 len 15840 [.] ECT0
	 rcv    0.000s seq 2823072402:2823074108 ack 722856685  win 16382 len 1706 [P.] ECT0
	 snd    0.000s seq  722856685:722856685  ack 2823074108 win 8452  len 0    [.]
	 rcv    0.607s seq 2823074108:2823074108 ack 722856685  win 16382 len 0    [.]
	 snd   30.176s seq  722856685:722856709  ack 2823074108 win 8452  len 24   [P.] ECT0
	 snd    0.002s seq  722856709:722856710  ack 2823074108 win 8452  len 0    [F.]
	 rcv    0.070s seq 2823074108:2823074108 ack 722856710  win 16382 len 0    [.]
	 rcv    0.000s seq 2823074108:2823074109 ack 722856710  win 16382 len 0    [F.]
	 snd    0.000s seq  722856710:722856710  ack 2823074109 win 8452  len 0    [.]
	Last packet 30120ms ago.
default	11:03:13.507661+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:03:13.528845+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c6554 posting AVAudioSessionAvailableInputsChangeNotification
default	11:03:13.528945+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:03:13.556406+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:03:13.572674+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c6554 posting AVAudioSessionAvailableInputsChangeNotification
default	11:03:13.572695+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:03:13.600318+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:03:13.616177+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c6554 posting AVAudioSessionAvailableInputsChangeNotification
default	11:03:13.616296+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:03:45.401179+0800	hootowl	tcp_timers [C1.1.1.1:3] retransmit seq=2721530959 12
default	11:03:45.401422+0800	hootowl	tcp_output [C1.1.1.1:3] flags=[FP.] seq=2721530959, ack=1177347048, win=7359 state=FIN_WAIT_1 rcv_nxt=1177347048, snd_una=2721530959
default	11:04:12.070837+0800	hootowl	Task <74973C91-E77D-41E2-9D3F-37942096EDDC>.<15> resuming, timeouts(60.0, 604800.0) qos(0x15) voucher((null)) activity(00000000-0000-0000-0000-000000000000)
default	11:04:12.075303+0800	hootowl	Connection 0: creating secure tcp or quic connection
default	11:04:12.075947+0800	hootowl	Connection 20: enabling TLS
default	11:04:12.075982+0800	hootowl	Connection 20: starting, TC(0x0)
default	11:04:12.076052+0800	hootowl	[C20 AA0BEDB5-35A9-4FE4-BAC4-BCF202BFB2B6 tcgbusfs.blob.core.windows.net:443 quic-connection, url: https://tcgbusfs.blob.core.windows.net/blobtcmsv/TCMSV_allavailable.json, definite, attribution: developer, context: com.apple.CFNetwork.NSURLSession.{D885363E-9839-4032-B958-F32329B8DC25}{(null)}{Y}{2}{0x0} (private), proc: 1B526020-2DE0-3C65-9122-F1177549D69A, delegated upid: 0] start
default	11:04:12.076183+0800	hootowl	[C20 tcgbusfs.blob.core.windows.net:443 initial parent-flow ((null))] event: path:start @0.000s
default	11:04:12.078624+0800	hootowl	[C20 tcgbusfs.blob.core.windows.net:443 waiting parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.001s, uuid: CA56E186-F30E-42D6-B6BE-E5169BE549AC
default	11:04:12.078885+0800	hootowl	[C20 tcgbusfs.blob.core.windows.net:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_connect @0.002s
default	11:04:12.078903+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C20] reporting state preparing
default	11:04:12.079049+0800	hootowl	[C20 tcgbusfs.blob.core.windows.net:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_child @0.002s
default	11:04:12.079214+0800	hootowl	[C20.1 tcgbusfs.blob.core.windows.net:443 initial path ((null))] event: path:start @0.002s
default	11:04:12.079569+0800	hootowl	[C20.1 tcgbusfs.blob.core.windows.net:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.003s, uuid: CA56E186-F30E-42D6-B6BE-E5169BE549AC
default	11:04:12.079680+0800	hootowl	[C20.1 tcgbusfs.blob.core.windows.net:443 in_progress transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: transform:start @0.003s
default	11:04:12.080029+0800	hootowl	[C20.1.1 tcgbusfs.blob.core.windows.net:443 initial path ((null))] event: path:start @0.003s
default	11:04:12.081533+0800	hootowl	[C20.1.1 tcgbusfs.blob.core.windows.net:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.005s, uuid: 1CA4FB8D-1B6A-4013-8FC4-7A9A01C7FC06
default	11:04:12.081692+0800	hootowl	[C20.1.1 tcgbusfs.blob.core.windows.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:start_dns @0.005s
default	11:04:12.081732+0800	hootowl	Task <74973C91-E77D-41E2-9D3F-37942096EDDC>.<15> setting up Connection 20
default	11:04:12.114419+0800	hootowl	nw_endpoint_resolver_update [C20.1.1 tcgbusfs.blob.core.windows.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Adding endpoint handler for 20.150.22.100:443
default	11:04:12.114729+0800	hootowl	[C20.1.1 tcgbusfs.blob.core.windows.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:receive_dns @0.036s
default	11:04:12.116997+0800	hootowl	[C20.1.1.1 20.150.22.100:443 initial path ((null))] event: path:start @0.038s
default	11:04:12.142621+0800	hootowl	[C20.1.1.1 20.150.22.100:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.041s, uuid: B30D4595-949A-4F0E-9304-30ECB0B78247
default	11:04:12.143783+0800	hootowl	[C20.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_nexus @0.064s
default	11:04:12.150047+0800	hootowl	[C20.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:receive_nexus @0.069s
default	11:04:12.154642+0800	hootowl	[C20.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_connect @0.075s
default	11:04:12.156116+0800	hootowl	tcp_output [C20.1.1.1:3] flags=[SEC] seq=629147915, ack=0, win=65535 state=SYN_SENT rcv_nxt=0, snd_una=629147915
default	11:04:12.267643+0800	hootowl	tcp_input [C20.1.1.1:3] flags=[S.E] seq=383714594, ack=629147916, win=65535 state=SYN_SENT rcv_nxt=0, snd_una=629147915
default	11:04:12.267708+0800	hootowl	nw_flow_connected [C20.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Transport protocol connected (tcp)
default	11:04:12.267841+0800	hootowl	[C20.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_transport @0.191s
default	11:04:12.268187+0800	hootowl	boringssl_session_apply_protocol_options_for_transport_block_invoke_2(2367) [C20.1.1.1:2][0x151b3c2e0] TLS configured [server(0) min_version(0x0303) max_version(0x0304) name(tcgbusfs.blob.core.windows.net) tickets(false) false_start(false) enforce_ev(false) enforce_ats(false) ats_non_pfs_ciphersuite_allowed(false) cc_mode_enforced(false) ech(false) pqtls(true), pake(false) skip_ats_trust(false)]
default	11:04:12.268398+0800	hootowl	boringssl_context_info_handler(2806) [C20.1.1.1:2][0x151b3c2e0] Client handshake started
default	11:04:12.268781+0800	hootowl	boringssl_context_info_handler(2823) [C20.1.1.1:2][0x151b3c2e0] Client handshake state: TLS client enter_early_data
default	11:04:12.269172+0800	hootowl	boringssl_context_info_handler(2823) [C20.1.1.1:2][0x151b3c2e0] Client handshake state: TLS client read_server_hello
default	11:04:12.365852+0800	hootowl	boringssl_context_info_handler(2823) [C20.1.1.1:2][0x151b3c2e0] Client handshake state: TLS 1.3 client read_hello_retry_request
default	11:04:12.366930+0800	hootowl	boringssl_context_info_handler(2823) [C20.1.1.1:2][0x151b3c2e0] Client handshake state: TLS 1.3 client send_second_client_hello
default	11:04:12.367042+0800	hootowl	boringssl_context_info_handler(2823) [C20.1.1.1:2][0x151b3c2e0] Client handshake state: TLS 1.3 client read_server_hello
default	11:04:12.439883+0800	hootowl	boringssl_context_info_handler(2823) [C20.1.1.1:2][0x151b3c2e0] Client handshake state: TLS 1.3 client read_encrypted_extensions
default	11:04:12.440865+0800	hootowl	boringssl_context_info_handler(2823) [C20.1.1.1:2][0x151b3c2e0] Client handshake state: TLS 1.3 client read_certificate_request
default	11:04:12.440967+0800	hootowl	boringssl_context_info_handler(2823) [C20.1.1.1:2][0x151b3c2e0] Client handshake state: TLS 1.3 client read_server_certificate
default	11:04:12.441025+0800	hootowl	boringssl_context_info_handler(2823) [C20.1.1.1:2][0x151b3c2e0] Client handshake state: TLS 1.3 client read_server_certificate_verify
default	11:04:12.441878+0800	hootowl	boringssl_context_evaluate_trust_async(2249) [C20.1.1.1:2][0x151b3c2e0] Performing external trust evaluation
default	11:04:12.442037+0800	hootowl	boringssl_context_evaluate_trust_async_external(2234) [C20.1.1.1:2][0x151b3c2e0] Asyncing for external verify block
default	11:04:12.442387+0800	hootowl	Connection 20: asked to evaluate TLS Trust
default	11:04:12.443206+0800	hootowl	Task <74973C91-E77D-41E2-9D3F-37942096EDDC>.<15> auth completion disp=1 cred=0x0
default	11:04:12.443917+0800	hootowl	(Trust 0x152220000) No pending evals, starting
default	11:04:12.444823+0800	hootowl	[0x15230fac0] activating connection: mach=true listener=false peer=false name=com.apple.trustd
default	11:04:12.445013+0800	hootowl	(Trust 0x152220000) Completed async eval kickoff
default	11:04:12.456129+0800	hootowl	(Trust 0x152220000) trustd returned 4
default	11:04:12.456227+0800	hootowl	System Trust Evaluation yielded status(0)
default	11:04:12.456285+0800	hootowl	(Trust 0x1522212c0) No pending evals, starting
default	11:04:12.456583+0800	hootowl	[0x15230cb40] activating connection: mach=true listener=false peer=false name=com.apple.trustd
default	11:04:12.456793+0800	hootowl	(Trust 0x1522212c0) Completed async eval kickoff
default	11:04:12.457015+0800	hootowl	[0x15230fac0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	11:04:12.463628+0800	hootowl	(Trust 0x1522212c0) trustd returned 4
default	11:04:12.463707+0800	hootowl	Connection 20: TLS Trust result 0
default	11:04:12.463752+0800	hootowl	boringssl_context_evaluate_trust_async_external_block_invoke_3(2148) [C20.1.1.1:2][0x151b3c2e0] Returning from external verify block with result: true
default	11:04:12.463849+0800	hootowl	boringssl_context_certificate_verify_callback(2430) [C20.1.1.1:2][0x151b3c2e0] Certificate verification result: OK
default	11:04:12.463881+0800	hootowl	boringssl_context_info_handler(2823) [C20.1.1.1:2][0x151b3c2e0] Client handshake state: TLS 1.3 client read_server_finished
default	11:04:12.463948+0800	hootowl	boringssl_context_info_handler(2823) [C20.1.1.1:2][0x151b3c2e0] Client handshake state: TLS 1.3 client send_end_of_early_data
default	11:04:12.463958+0800	hootowl	boringssl_context_info_handler(2823) [C20.1.1.1:2][0x151b3c2e0] Client handshake state: TLS 1.3 client send_client_encrypted_extensions
default	11:04:12.463987+0800	hootowl	boringssl_context_info_handler(2823) [C20.1.1.1:2][0x151b3c2e0] Client handshake state: TLS 1.3 client send_client_certificate
default	11:04:12.464004+0800	hootowl	boringssl_context_info_handler(2823) [C20.1.1.1:2][0x151b3c2e0] Client handshake state: TLS 1.3 client complete_second_flight
default	11:04:12.464102+0800	hootowl	boringssl_context_info_handler(2823) [C20.1.1.1:2][0x151b3c2e0] Client handshake state: TLS 1.3 client done
default	11:04:12.464236+0800	hootowl	boringssl_context_info_handler(2823) [C20.1.1.1:2][0x151b3c2e0] Client handshake state: TLS client finish_client_handshake
default	11:04:12.464246+0800	hootowl	boringssl_context_info_handler(2823) [C20.1.1.1:2][0x151b3c2e0] Client handshake state: TLS client done
default	11:04:12.464252+0800	hootowl	boringssl_context_info_handler(2812) [C20.1.1.1:2][0x151b3c2e0] Client handshake done
default	11:04:12.464716+0800	hootowl	nw_protocol_boringssl_signal_connected(895) [C20.1.1.1:2][0x151b3c2e0] TLS connected [server(0) version(0x0304) ciphersuite(TLS_AES_256_GCM_SHA384) group(0x0018) signature_alg(0x0804) alpn(nil) resumed(0) offered_ticket(0) in_early_data(0) early_data_accepted(0) false_started(0) ocsp_received(1) sct_received(0) connect_time(196ms) flight_time(167ms) rtt(97ms) write_stalls(0) read_stalls(8) pake(0x0000)]
default	11:04:12.464791+0800	hootowl	nw_flow_connected [C20.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (CFNetworkConnection-3170269070)
default	11:04:12.465015+0800	hootowl	[C20.1.1.1 20.150.22.100:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.388s
default	11:04:12.465223+0800	hootowl	[C20.1.1 tcgbusfs.blob.core.windows.net:443 ready resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.389s
default	11:04:12.465296+0800	hootowl	[C20.1 tcgbusfs.blob.core.windows.net:443 ready transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.389s
default	11:04:12.465358+0800	hootowl	[C20.1.1.1 20.150.22.100:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.389s
default	11:04:12.465436+0800	hootowl	[C20.1.1 tcgbusfs.blob.core.windows.net:443 ready resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.389s
default	11:04:12.465483+0800	hootowl	[C20.1 tcgbusfs.blob.core.windows.net:443 ready transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.389s
default	11:04:12.465563+0800	hootowl	nw_flow_connected [C20 20.150.22.100:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (endpoint_flow)
default	11:04:12.465647+0800	hootowl	[C20 20.150.22.100:443 ready parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_connect @0.389s
default	11:04:12.465841+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C20] reporting state ready
default	11:04:12.465857+0800	hootowl	[C20 20.150.22.100:443 ready parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.389s
default	11:04:12.465872+0800	hootowl	nw_connection_send_viability_changed_on_nw_queue [C20] viability_changed_handler(true)
default	11:04:12.465907+0800	hootowl	[0x15230cb40] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	11:04:12.465956+0800	hootowl	Connection 20: connected successfully
default	11:04:12.465972+0800	hootowl	Connection 20: TLS handshake complete
default	11:04:12.466118+0800	hootowl	Connection 20: ready C(N) E(N)
default	11:04:12.466304+0800	hootowl	Task <74973C91-E77D-41E2-9D3F-37942096EDDC>.<15> now using Connection 20
default	11:04:12.466361+0800	hootowl	Connection 20: received viability advisory(Y)
default	11:04:12.466485+0800	hootowl	Task <74973C91-E77D-41E2-9D3F-37942096EDDC>.<15> sent request, body N 0
default	11:04:12.563365+0800	hootowl	Task <74973C91-E77D-41E2-9D3F-37942096EDDC>.<15> received response, status 304 content K
default	11:04:12.564877+0800	hootowl	Task <74973C91-E77D-41E2-9D3F-37942096EDDC>.<15> done using Connection 20
default	11:04:12.565567+0800	hootowl	[C20] event: client:connection_idle @0.488s
default	11:04:12.565893+0800	hootowl	nw_protocol_tcp_notify [C20.1.1.1:3] nw_protocol_notification_type_connection_idle is true
default	11:04:12.566710+0800	hootowl	Task <74973C91-E77D-41E2-9D3F-37942096EDDC>.<15> summary for task success {transaction_duration_ms=492, response_status=304, connection=20, protocol="http/1.1", domain_lookup_duration_ms=31, connect_duration_ms=314, secure_connection_duration_ms=196, private_relay=false, request_start_ms=394, request_duration_ms=0, response_start_ms=490, response_duration_ms=0, request_bytes=337, request_throughput_kbps=33654, response_bytes=308, response_throughput_kbps=2604, cache_hit=true}
default	11:04:12.566813+0800	hootowl	nw_protocol_tcp_set_connection_idle [C20.1.1.1:3] os_nexus_flow_set_connection_idle returned 0
default	11:04:12.568028+0800	hootowl	[C20] event: client:connection_idle @0.489s
default	11:04:12.571661+0800	hootowl	Task <74973C91-E77D-41E2-9D3F-37942096EDDC>.<15> finished successfully
default	11:04:12.572046+0800	hootowl	Mu1Base+Ext 152
taipei 📦 minutely Received 472935 bytes
default	11:04:12.572243+0800	hootowl	nw_protocol_tcp_notify [C20.1.1.1:3] nw_protocol_notification_type_connection_idle is true
default	11:04:12.572374+0800	hootowl	nw_protocol_tcp_set_connection_idle [C20.1.1.1:3] os_nexus_flow_set_connection_idle returned 0
default	11:04:12.572393+0800	hootowl	Mu1Base+Ext 177
previousHash not changed
default	11:04:12.578635+0800	hootowl	MncplCyclopsScreen 166
🦵 uiKick received — syncing items
default	11:04:12.578748+0800	hootowl	Municipal+Cyclops 93
🎨 model refreshed — obs:0s car:7 thread:main 🆔 12708723194660554214
default	11:04:12.580954+0800	hootowl	MncplCyclopsScreen 78
🏠 body eval — items:6 firstObs:0s firstCar:7
default	11:04:16.339489+0800	hootowl	tcp_timers [C7.1.1.3:3] retransmit seq=3466882418 11
default	11:04:42.935681+0800	hootowl	Connection 20: cleaning up
default	11:04:42.935792+0800	hootowl	[C20 AA0BEDB5-35A9-4FE4-BAC4-BCF202BFB2B6 tcgbusfs.blob.core.windows.net:443 quic-connection, url: https://tcgbusfs.blob.core.windows.net/blobtcmsv/TCMSV_allavailable.json, definite, attribution: developer] cancel
default	11:04:42.936429+0800	hootowl	[C20 AA0BEDB5-35A9-4FE4-BAC4-BCF202BFB2B6 tcgbusfs.blob.core.windows.net:443 quic-connection, url: https://tcgbusfs.blob.core.windows.net/blobtcmsv/TCMSV_allavailable.json, definite, attribution: developer] cancelled
	[C20.1.1.1 B30D4595-949A-4F0E-9304-30ECB0B78247 192.168.50.191:56390<->20.150.22.100:443]
	Connected Path: satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good
	Privacy Stance: Not Eligible
	Duration: 30.859s, DNS @0.005s took 0.031s, TCP @0.075s took 0.116s,  took 0.196s
	bytes in/out: 10765/2357, packets in/out: 9/14, rtt: 0.101s, retransmitted bytes: 0, out-of-order bytes: 0
	ecn packets sent/acked/marked/lost: 5/4/0/0
default	11:04:42.938288+0800	hootowl	nw_protocol_tcp_log_summary [C20.1.1.1:3] 
	[12C6C4B8-F6C6-4B45-891F-FE7E7759C2F2 192.168.50.191:56390<->20.150.22.100:443]
	Init: 1, Conn_Time: 114.222ms, SYNs: 1, WR_T: 0/0, RD_T: 0/0, TFO: 0/0/0, ECN: 0/1/1, Accurate ECN (client/server): Disabled/Disabled, TS: 1, TSO: 0
	rtt_cache: process, rtt_upd: 5, rtt: 101.718ms, rtt_var: 33.375ms rtt_nc: 101.718ms, rtt_var_nc: 33.375ms base rtt: 65ms
	ACKs-compressed: 1, ACKs delayed: 0 delayed ACKs sent: 0
default	11:04:42.938751+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C20] reporting state cancelled
default	11:04:42.938770+0800	hootowl	Connection 20: done
default	11:04:42.938906+0800	hootowl	tcp_output [C20.1.1.1:3] flags=[F.] seq=629150297, ack=383725360, win=2048 state=FIN_WAIT_1 rcv_nxt=383725360, snd_una=629150273
default	11:04:43.007742+0800	hootowl	tcp_input [C20.1.1.1:3] flags=[F.] seq=383725360, ack=629150298, win=16382 state=FIN_WAIT_2 rcv_nxt=383725360, snd_una=629150298
error	11:04:49.406980+0800	hootowl	tcp_output [C1.1.1.1:3] flags=[R.] seq=2721531343, ack=1177347048, win=7359 state=CLOSED rcv_nxt=1177347048, snd_una=2721530959
default	11:04:49.408620+0800	hootowl	tcp_close [C1.1.1.1:3] TCP Packets:
	 rcv    3.740s seq 1177223135:1177238975 ack 2721530959 win 16382 len 15840 [.] ECT0
	 rcv    0.001s seq 1177238975:1177254815 ack 2721530959 win 16382 len 15840 [.] ECT0
	 rcv    0.000s seq 1177254815:1177257695 ack 2721530959 win 16382 len 2880 [.] ECT0
	 rcv    0.000s seq 1177257695:1177260575 ack 2721530959 win 16382 len 2880 [.] ECT0
	 snd    0.000s seq 2721530959:2721530959 ack 1177260575 win 7359  len 0    [.]
	 rcv    0.002s seq 1177260575:1177276415 ack 2721530959 win 16382 len 15840 [.] ECT0
	 rcv    0.000s seq 1177276415:1177292255 ack 2721530959 win 16382 len 15840 [.] ECT0
	 rcv    0.000s seq 1177292255:1177300895 ack 2721530959 win 16382 len 8640 [.] ECT0
	 rcv    0.000s seq 1177300895:1177302335 ack 2721530959 win 16382 len 1440 [.] ECT0
	 rcv    0.000s seq 1177302335:1177306655 ack 2721530959 win 16382 len 4320 [.] ECT0
	 rcv    0.000s seq 1177306655:1177322495 ack 2721530959 win 16382 len 15840 [.] ECT0
	 rcv    0.000s seq 1177322495:1177338335 ack 2721530959 win 16382 len 15840 [.] ECT0
	 rcv    0.000s seq 1177338335:1177346975 ack 2721530959 win 16382 len 8640 [.] ECT0
	 rcv    0.000s seq 1177346975:1177347048 ack 2721530959 win 16382 len 73   [P.] ECT0
	 rcv    0.000s seq 1177345608:1177347048 ack 2721530959 win 16382 len 1440 [P.]
	 snd    0.000s seq 2721530959:2721530959 ack 1177347048 win 6008  len 0    [.]
	 rcv    0.000s seq 1177223135:1177224575 ack 2721530959 win 16382 len 1440 [.]
	 snd    0.000s seq 2721530959:2721530959 ack 1177347048 win 6008  len 0    [.]
	 rcv    0.000s seq 1177223135:1177224575 ack 2721530959 win 16382 len 1440 [.]
	 snd    0.000s seq 2721530959:2721530959 ack 1177347048 win 6008  len 0    [.]
	 rcv    0.000s seq 1177223135:1177224575 ack 2721530959 win 16382 len 1440 [.]
	 snd    0.000s seq 2721530959:2721530959 ack 1177347048 win 6008  len 0    [.]
	 snd    0.000s seq 2721530959:2721530959 ack 1177347048 win 7359  len 0    [.]
	 snd   22.432s seq 2721530959:2721531318 ack 1177347048 win 7359  len 359  [P.]
	 snd    2.758s seq 2721530959:2721531318 ack 1177347048 win 7359  len 359  [P.]
	 snd    5.832s seq 2721530959:2721531318 ack 1177347048 win 7359  len 359  [P.]
	 snd   10.136s seq 2721530959:2721531318 ack 1177347048 win 7359  len 359  [P.]
	 snd   19.792s seq 2721530959:2721531318 ack 1177347048 win 7359  len 359  [P.]
	 snd   23.184s seq 2721531318:2721531342 ack 1177347048 win 7359  len 24   [P.C]
	 snd    0.003s seq 2721531342:2721531343 ack 1177347048 win 7359  len 0    [F.]
	 snd   16.512s seq 2721530959:2721531343 ack 1177347048 win 7359  len 383  [FP.]
	 snd   64.000s seq 2721530959:2721531343 ack 1177347048 win 7359  len 383  [FP.]
	 snd   64.000s seq 2721530959:2721531343 ack 1177347048 win 7359  len 383  [FP.]
	 snd   64.000s seq 2721530959:2721531343 ack 1177347048 win 7359  len 383  [FP.]
	 snd   64.000s seq 2721530959:2721531343 ack 1177347048 win 7359  len 383  [FP.]
	 snd   64.000s seq 2721530959:2721531343 ack 1177347048 win 7359  len 383  [FP.]
	 snd   64.000s seq 2721530959:2721531343 ack 1177347048 win 7359  len 383  [FP.]
	 snd   64.000s seq 2721530959:2721531343 ack 1177347048 win 7359  len 383  [FP.]
	 snd   64.000s seq 2721530959:2721531343 ack 1177347048 win 7359  len 383  [FP.]
	 snd   64.000s seq 2721531343:2721531343 ack 1177347048 win 7359  len 0    [R.]
	Last packet 0ms ago.
default	11:05:13.499912+0800	hootowl	tcp_close [C20.1.1.1:3] TCP Packets:
	 snd    0.000s seq  629147915:629147916  ack 0          win 65535 len 0    [SEC]
	 rcv    0.114s seq  383714594:383714595  ack 629147916  win 65535 len 0    [S.E] ECT0
	 snd    0.000s seq  629147916:629147916  ack 383714595  win 2053  len 0    [.]
	 snd    0.002s seq  629147916:629149344  ack 383714595  win 2053  len 1428 [.] ECT0
	 snd    0.000s seq  629149344:629149455  ack 383714595  win 2053  len 111  [P.] ECT0
	 rcv    0.096s seq  383714595:383714595  ack 629149455  win 16385 len 0    [.]
	 rcv    0.000s seq  383714595:383714694  ack 629149455  win 16385 len 99   [P.] ECT0
	 snd    0.000s seq  629149455:629149455  ack 383714694  win 2052  len 0    [.]
	 snd    0.002s seq  629149455:629149840  ack 383714694  win 2052  len 385  [P.] ECT0
	 rcv    0.069s seq  383714694:383716134  ack 629149840  win 16384 len 1440 [.] ECT0
	 snd    0.000s seq  629149840:629149840  ack 383716134  win 2030  len 0    [.]
	 rcv    0.004s seq  383716134:383720454  ack 629149840  win 16384 len 4320 [.] ECT0
	 snd    0.000s seq  629149840:629149840  ack 383720454  win 1981  len 0    [.]
	 rcv    0.000s seq  383720454:383724927  ack 629149840  win 16384 len 4473 [P.] ECT0
	 snd    0.000s seq  629149840:629149840  ack 383724927  win 1912  len 0    [.]
	 snd    0.000s seq  629149840:629149840  ack 383724927  win 2048  len 0    [.]
	 snd    0.024s seq  629149840:629149914  ack 383724927  win 2048  len 74   [P.] ECT0
	 snd    0.002s seq  629149914:629150273  ack 383724927  win 2048  len 359  [P.] ECT0
	 rcv    0.072s seq  383724927:383725030  ack 629149914  win 16383 len 103  [P.] ECT0
	 snd    0.000s seq  629150273:629150273  ack 383725030  win 2047  len 0    [.]
	 rcv    0.025s seq  383725030:383725360  ack 629150273  win 16382 len 330  [P.] ECT0
	 snd    0.000s seq  629150273:629150273  ack 383725360  win 2043  len 0    [.]
	 rcv    0.546s seq  383725360:383725360  ack 629150273  win 16382 len 0    [.]
	 snd   29.824s seq  629150273:629150297  ack 383725360  win 2048  len 24   [P.] ECT0
	 snd    0.002s seq  629150297:629150298  ack 383725360  win 2048  len 0    [F.]
	 rcv    0.069s seq  383725360:383725360  ack 629150298  win 16382 len 0    [.]
	 rcv    0.000s seq  383725360:383725361  ack 629150298  win 16382 len 0    [F.]
	 snd    0.000s seq  629150298:629150298  ack 383725361  win 2048  len 0    [.]
	Last packet 30491ms ago.
default	11:05:20.345535+0800	hootowl	tcp_timers [C7.1.1.3:3] retransmit seq=3466882418 12
default	11:06:12.582686+0800	hootowl	Task <143BDEBC-588C-465F-A181-2FE83A5FA655>.<16> resuming, timeouts(60.0, 604800.0) qos(0x15) voucher((null)) activity(00000000-0000-0000-0000-000000000000)
default	11:06:12.585800+0800	hootowl	Connection 0: creating secure tcp or quic connection
default	11:06:12.586338+0800	hootowl	Connection 21: enabling TLS
default	11:06:12.586368+0800	hootowl	Connection 21: starting, TC(0x0)
default	11:06:12.586451+0800	hootowl	[C21 AA270A28-87AD-41CC-971F-06C9FF16F07D tcgbusfs.blob.core.windows.net:443 quic-connection, url: https://tcgbusfs.blob.core.windows.net/blobtcmsv/TCMSV_allavailable.json, definite, attribution: developer, context: com.apple.CFNetwork.NSURLSession.{D885363E-9839-4032-B958-F32329B8DC25}{(null)}{Y}{2}{0x0} (private), proc: 1B526020-2DE0-3C65-9122-F1177549D69A, delegated upid: 0] start
default	11:06:12.586637+0800	hootowl	[C21 tcgbusfs.blob.core.windows.net:443 initial parent-flow ((null))] event: path:start @0.000s
default	11:06:12.588041+0800	hootowl	[C21 tcgbusfs.blob.core.windows.net:443 waiting parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.001s, uuid: E1AA5923-C37B-4337-AC26-73309224C057
default	11:06:12.588323+0800	hootowl	[C21 tcgbusfs.blob.core.windows.net:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_connect @0.001s
default	11:06:12.588345+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C21] reporting state preparing
default	11:06:12.588473+0800	hootowl	[C21 tcgbusfs.blob.core.windows.net:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_child @0.002s
default	11:06:12.588604+0800	hootowl	[C21.1 tcgbusfs.blob.core.windows.net:443 initial path ((null))] event: path:start @0.002s
default	11:06:12.589085+0800	hootowl	[C21.1 tcgbusfs.blob.core.windows.net:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.002s, uuid: E1AA5923-C37B-4337-AC26-73309224C057
default	11:06:12.589265+0800	hootowl	[C21.1 tcgbusfs.blob.core.windows.net:443 in_progress transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: transform:start @0.002s
default	11:06:12.589495+0800	hootowl	[C21.1.1 tcgbusfs.blob.core.windows.net:443 initial path ((null))] event: path:start @0.002s
default	11:06:12.591562+0800	hootowl	[C21.1.1 tcgbusfs.blob.core.windows.net:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.004s, uuid: 2120C72C-71B7-435B-917C-11FA7ACE61EA
default	11:06:12.591922+0800	hootowl	[C21.1.1 tcgbusfs.blob.core.windows.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:start_dns @0.004s
default	11:06:12.592442+0800	hootowl	Task <143BDEBC-588C-465F-A181-2FE83A5FA655>.<16> setting up Connection 21
default	11:06:12.621675+0800	hootowl	nw_endpoint_resolver_update [C21.1.1 tcgbusfs.blob.core.windows.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Adding endpoint handler for 20.150.22.100:443
default	11:06:12.622129+0800	hootowl	[C21.1.1 tcgbusfs.blob.core.windows.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:receive_dns @0.034s
default	11:06:12.622550+0800	hootowl	[C21.1.1.1 20.150.22.100:443 initial path ((null))] event: path:start @0.035s
default	11:06:12.623244+0800	hootowl	[C21.1.1.1 20.150.22.100:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.036s, uuid: D04C4F5C-EE80-4F40-9298-4EE4A4319271
default	11:06:12.623298+0800	hootowl	[C21.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_nexus @0.036s
default	11:06:12.624562+0800	hootowl	[C21.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:receive_nexus @0.037s
default	11:06:12.625267+0800	hootowl	[C21.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_connect @0.037s
default	11:06:12.625628+0800	hootowl	tcp_output [C21.1.1.1:3] flags=[SEC] seq=2379520225, ack=0, win=65535 state=SYN_SENT rcv_nxt=0, snd_una=2379520225
default	11:06:12.705301+0800	hootowl	tcp_input [C21.1.1.1:3] flags=[S.E] seq=1650380940, ack=2379520226, win=65535 state=SYN_SENT rcv_nxt=0, snd_una=2379520225
default	11:06:12.705362+0800	hootowl	nw_flow_connected [C21.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Transport protocol connected (tcp)
default	11:06:12.705652+0800	hootowl	[C21.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_transport @0.118s
default	11:06:12.706619+0800	hootowl	boringssl_session_apply_protocol_options_for_transport_block_invoke_2(2367) [C21.1.1.1:2][0x151b3f4e0] TLS configured [server(0) min_version(0x0303) max_version(0x0304) name(tcgbusfs.blob.core.windows.net) tickets(false) false_start(false) enforce_ev(false) enforce_ats(false) ats_non_pfs_ciphersuite_allowed(false) cc_mode_enforced(false) ech(false) pqtls(true), pake(false) skip_ats_trust(false)]
default	11:06:12.707145+0800	hootowl	boringssl_context_info_handler(2806) [C21.1.1.1:2][0x151b3f4e0] Client handshake started
default	11:06:12.707750+0800	hootowl	boringssl_context_info_handler(2823) [C21.1.1.1:2][0x151b3f4e0] Client handshake state: TLS client enter_early_data
default	11:06:12.708167+0800	hootowl	boringssl_context_info_handler(2823) [C21.1.1.1:2][0x151b3f4e0] Client handshake state: TLS client read_server_hello
default	11:06:12.780180+0800	hootowl	boringssl_context_info_handler(2823) [C21.1.1.1:2][0x151b3f4e0] Client handshake state: TLS 1.3 client read_hello_retry_request
default	11:06:12.783494+0800	hootowl	boringssl_context_info_handler(2823) [C21.1.1.1:2][0x151b3f4e0] Client handshake state: TLS 1.3 client send_second_client_hello
default	11:06:12.783674+0800	hootowl	boringssl_context_info_handler(2823) [C21.1.1.1:2][0x151b3f4e0] Client handshake state: TLS 1.3 client read_server_hello
default	11:06:12.887115+0800	hootowl	boringssl_context_info_handler(2823) [C21.1.1.1:2][0x151b3f4e0] Client handshake state: TLS 1.3 client read_encrypted_extensions
default	11:06:12.887626+0800	hootowl	boringssl_context_info_handler(2823) [C21.1.1.1:2][0x151b3f4e0] Client handshake state: TLS 1.3 client read_certificate_request
default	11:06:12.887684+0800	hootowl	boringssl_context_info_handler(2823) [C21.1.1.1:2][0x151b3f4e0] Client handshake state: TLS 1.3 client read_server_certificate
default	11:06:12.887713+0800	hootowl	boringssl_context_info_handler(2823) [C21.1.1.1:2][0x151b3f4e0] Client handshake state: TLS 1.3 client read_server_certificate_verify
default	11:06:12.888953+0800	hootowl	boringssl_context_evaluate_trust_async(2249) [C21.1.1.1:2][0x151b3f4e0] Performing external trust evaluation
default	11:06:12.889010+0800	hootowl	boringssl_context_evaluate_trust_async_external(2234) [C21.1.1.1:2][0x151b3f4e0] Asyncing for external verify block
default	11:06:12.889332+0800	hootowl	Connection 21: asked to evaluate TLS Trust
default	11:06:12.889739+0800	hootowl	Task <143BDEBC-588C-465F-A181-2FE83A5FA655>.<16> auth completion disp=1 cred=0x0
default	11:06:12.890475+0800	hootowl	(Trust 0x150cf0a80) No pending evals, starting
default	11:06:12.891310+0800	hootowl	[0x15230cb40] activating connection: mach=true listener=false peer=false name=com.apple.trustd
default	11:06:12.891470+0800	hootowl	(Trust 0x150cf0a80) Completed async eval kickoff
default	11:06:12.901778+0800	hootowl	(Trust 0x150cf0a80) trustd returned 4
default	11:06:12.901875+0800	hootowl	System Trust Evaluation yielded status(0)
default	11:06:12.901937+0800	hootowl	(Trust 0x150cf3e40) No pending evals, starting
default	11:06:12.902280+0800	hootowl	[0x15230fac0] activating connection: mach=true listener=false peer=false name=com.apple.trustd
default	11:06:12.902482+0800	hootowl	(Trust 0x150cf3e40) Completed async eval kickoff
default	11:06:12.902827+0800	hootowl	[0x15230cb40] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	11:06:12.909127+0800	hootowl	(Trust 0x150cf3e40) trustd returned 4
default	11:06:12.909221+0800	hootowl	Connection 21: TLS Trust result 0
default	11:06:12.909266+0800	hootowl	boringssl_context_evaluate_trust_async_external_block_invoke_3(2148) [C21.1.1.1:2][0x151b3f4e0] Returning from external verify block with result: true
default	11:06:12.909400+0800	hootowl	boringssl_context_certificate_verify_callback(2430) [C21.1.1.1:2][0x151b3f4e0] Certificate verification result: OK
default	11:06:12.909425+0800	hootowl	boringssl_context_info_handler(2823) [C21.1.1.1:2][0x151b3f4e0] Client handshake state: TLS 1.3 client read_server_finished
default	11:06:12.909451+0800	hootowl	boringssl_context_info_handler(2823) [C21.1.1.1:2][0x151b3f4e0] Client handshake state: TLS 1.3 client send_end_of_early_data
default	11:06:12.909490+0800	hootowl	boringssl_context_info_handler(2823) [C21.1.1.1:2][0x151b3f4e0] Client handshake state: TLS 1.3 client send_client_encrypted_extensions
default	11:06:12.909513+0800	hootowl	boringssl_context_info_handler(2823) [C21.1.1.1:2][0x151b3f4e0] Client handshake state: TLS 1.3 client send_client_certificate
default	11:06:12.909543+0800	hootowl	boringssl_context_info_handler(2823) [C21.1.1.1:2][0x151b3f4e0] Client handshake state: TLS 1.3 client complete_second_flight
default	11:06:12.909631+0800	hootowl	boringssl_context_info_handler(2823) [C21.1.1.1:2][0x151b3f4e0] Client handshake state: TLS 1.3 client done
default	11:06:12.909785+0800	hootowl	boringssl_context_info_handler(2823) [C21.1.1.1:2][0x151b3f4e0] Client handshake state: TLS client finish_client_handshake
default	11:06:12.909817+0800	hootowl	boringssl_context_info_handler(2823) [C21.1.1.1:2][0x151b3f4e0] Client handshake state: TLS client done
default	11:06:12.909830+0800	hootowl	boringssl_context_info_handler(2812) [C21.1.1.1:2][0x151b3f4e0] Client handshake done
default	11:06:12.910145+0800	hootowl	nw_protocol_boringssl_signal_connected(895) [C21.1.1.1:2][0x151b3f4e0] TLS connected [server(0) version(0x0304) ciphersuite(TLS_AES_256_GCM_SHA384) group(0x0018) signature_alg(0x0804) alpn(nil) resumed(0) offered_ticket(0) in_early_data(0) early_data_accepted(0) false_started(0) ocsp_received(1) sct_received(0) connect_time(203ms) flight_time(172ms) rtt(72ms) write_stalls(0) read_stalls(7) pake(0x0000)]
default	11:06:12.910223+0800	hootowl	nw_flow_connected [C21.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (CFNetworkConnection-3170269070)
default	11:06:12.910454+0800	hootowl	[C21.1.1.1 20.150.22.100:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.323s
default	11:06:12.910701+0800	hootowl	[C21.1.1 tcgbusfs.blob.core.windows.net:443 ready resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.324s
default	11:06:12.910734+0800	hootowl	[C21.1 tcgbusfs.blob.core.windows.net:443 ready transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.324s
default	11:06:12.910835+0800	hootowl	[C21.1.1.1 20.150.22.100:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.324s
default	11:06:12.910911+0800	hootowl	[C21.1.1 tcgbusfs.blob.core.windows.net:443 ready resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.324s
default	11:06:12.910928+0800	hootowl	[C21.1 tcgbusfs.blob.core.windows.net:443 ready transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.324s
default	11:06:12.910974+0800	hootowl	nw_flow_connected [C21 20.150.22.100:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (endpoint_flow)
default	11:06:12.911103+0800	hootowl	[C21 20.150.22.100:443 ready parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_connect @0.324s
default	11:06:12.911395+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C21] reporting state ready
default	11:06:12.911418+0800	hootowl	[C21 20.150.22.100:443 ready parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.324s
default	11:06:12.911432+0800	hootowl	nw_connection_send_viability_changed_on_nw_queue [C21] viability_changed_handler(true)
default	11:06:12.911463+0800	hootowl	[0x15230fac0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	11:06:12.911472+0800	hootowl	Connection 21: connected successfully
default	11:06:12.911484+0800	hootowl	Connection 21: TLS handshake complete
default	11:06:12.911513+0800	hootowl	Connection 21: ready C(N) E(N)
default	11:06:12.911648+0800	hootowl	Task <143BDEBC-588C-465F-A181-2FE83A5FA655>.<16> now using Connection 21
default	11:06:12.911678+0800	hootowl	Connection 21: received viability advisory(Y)
default	11:06:12.911786+0800	hootowl	Task <143BDEBC-588C-465F-A181-2FE83A5FA655>.<16> sent request, body N 0
default	11:06:13.034612+0800	hootowl	Task <143BDEBC-588C-465F-A181-2FE83A5FA655>.<16> received response, status 200 content K
default	11:06:13.568941+0800	hootowl	Task <143BDEBC-588C-465F-A181-2FE83A5FA655>.<16> response ended
default	11:06:13.569607+0800	hootowl	Task <143BDEBC-588C-465F-A181-2FE83A5FA655>.<16> done using Connection 21
default	11:06:13.569715+0800	hootowl	[C21] event: client:connection_idle @0.982s
default	11:06:13.569828+0800	hootowl	Task <143BDEBC-588C-465F-A181-2FE83A5FA655>.<16> summary for task success {transaction_duration_ms=985, response_status=200, connection=21, protocol="http/1.1", domain_lookup_duration_ms=30, connect_duration_ms=287, secure_connection_duration_ms=203, private_relay=false, request_start_ms=328, request_duration_ms=0, response_start_ms=450, response_duration_ms=534, request_bytes=337, request_throughput_kbps=45780, response_bytes=472906, response_throughput_kbps=7073, cache_hit=true}
default	11:06:13.569885+0800	hootowl	nw_protocol_tcp_notify [C21.1.1.1:3] nw_protocol_notification_type_connection_idle is true
default	11:06:13.569909+0800	hootowl	nw_protocol_tcp_set_connection_idle [C21.1.1.1:3] os_nexus_flow_set_connection_idle returned 0
default	11:06:13.570065+0800	hootowl	[C21] event: client:connection_idle @0.983s
default	11:06:13.570626+0800	hootowl	nw_protocol_tcp_notify [C21.1.1.1:3] nw_protocol_notification_type_connection_idle is true
default	11:06:13.570647+0800	hootowl	Task <143BDEBC-588C-465F-A181-2FE83A5FA655>.<16> finished successfully
default	11:06:13.570667+0800	hootowl	nw_protocol_tcp_set_connection_idle [C21.1.1.1:3] os_nexus_flow_set_connection_idle returned 0
default	11:06:13.570692+0800	hootowl	Mu1Base+Ext 152
taipei 📦 minutely Received 472453 bytes
default	11:06:13.571904+0800	hootowl	Mu1Base+Ext 175
previousHash updated
default	11:06:13.600955+0800	hootowl	MncplCyclopsScreen 166
🦵 uiKick received — syncing items
default	11:06:13.601013+0800	hootowl	Municipal+Cyclops 93
🎨 model refreshed — obs:0s car:7 thread:main 🆔 12708723194660554214
error	11:06:13.606079+0800	hootowl	333	wireAvailableUpdateFromMunicipal()	⚠️ duplicate parkIds in avail feed (11): 040014(綠寶石區, ?), 040037(綠光河岸區, ?), 040068(玉清宮, ?), 060021(陽光運動公園, ?), 060047(親情河濱公園1區, ?), 060068(萊茵區, ?), 060079(城市車旅新店安德二, ?), 060085(親情河濱公園2區, ?), 060085(親情河濱公園2區, ?), 170120(MITSUI OUTLET PARK 林口二館收費, ?), 170120(MITSUI OUTLET PARK 林口二館收費, ?)
default	11:06:13.606689+0800	hootowl	Municipal 130
🐎 minutelyAvailable ["newTaipeiCity ⏳04 10:54 ∑1428", "taipei ⏳04 11:06 ∑1174"]
default	11:06:13.616492+0800	hootowl	MncplCyclopsScreen 166
🦵 uiKick received — syncing items
default	11:06:13.616547+0800	hootowl	Municipal+Cyclops 93
🎨 model refreshed — obs:0s car:7 thread:main 🆔 12708723194660554214
default	11:06:13.626889+0800	hootowl	MncplCyclopsScreen 78
🏠 body eval — items:6 firstObs:0s firstCar:7
default	11:06:18.010219+0800	hootowl	TX focusApplication (peekAppEvent) stealKB:Y scene:com.sharkda.hootowl-1B8F959F-618F-4A0D-AD89-E09DEC0EAB34
default	11:06:18.011419+0800	hootowl	Evaluating dispatch of UIEvent: 0x151469e00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	11:06:18.011540+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	11:06:18.011671+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x14e20c800>; contextId: 0xD3314357
default	11:06:18.011697+0800	hootowl	Evaluating dispatch of UIEvent: 0x151469e00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	11:06:18.138771+0800	hootowl	Evaluating dispatch of UIEvent: 0x151469e00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	11:06:18.139048+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	11:06:18.139087+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x14e20c800>; contextId: 0xD3314357
default	11:06:18.159960+0800	hootowl	Evaluating dispatch of UIEvent: 0x151469e00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	11:06:18.159986+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	11:06:18.163423+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x14e20c800>; contextId: 0xD3314357
default	11:06:18.173866+0800	hootowl	Evaluating dispatch of UIEvent: 0x151469e00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	11:06:18.173883+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	11:06:18.173903+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x14e20c800>; contextId: 0xD3314357
default	11:06:18.191310+0800	hootowl	Evaluating dispatch of UIEvent: 0x151469e00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	11:06:18.192178+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	11:06:18.192261+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x14e20c800>; contextId: 0xD3314357
default	11:06:18.200715+0800	hootowl	Not push traits update to screen for new style 1, <UIWindowScene: 0x14ec14200> (1B8F959F-618F-4A0D-AD89-E09DEC0EAB34)
default	11:06:18.205818+0800	hootowl	sceneOfRecord: sceneID: sceneID:com.sharkda.hootowl-1B8F959F-618F-4A0D-AD89-E09DEC0EAB34  persistentID: 1B8F959F-618F-4A0D-AD89-E09DEC0EAB34
default	11:06:18.205841+0800	hootowl	Deactivation reason added: 0; deactivation reasons: 0 -> 1; animating application lifecycle event: 1
default	11:06:18.205902+0800	hootowl	App transitioned to background, suspending HangTracing.
default	11:06:18.206043+0800	hootowl	App with bundleID:com.sharkda.hootowl is no longer foreground at time=16742539740355, attempting to emit telemetry with emission type: HTFGUpdateAppBackgrounded
default	11:06:18.206245+0800	hootowl	Deactivation reason added: 12; deactivation reasons: 1 -> 4097; animating application lifecycle event: 1
default	11:06:18.214997+0800	hootowl	Evaluating dispatch of UIEvent: 0x151469e00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	11:06:18.215020+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	11:06:18.215038+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x14e20c800>; contextId: 0xD3314357
default	11:06:18.215087+0800	hootowl	Evaluating dispatch of UIEvent: 0x151469e00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	11:06:18.215204+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	11:06:18.218820+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x14e20c800>; contextId: 0xD3314357
default	11:06:18.268781+0800	hootowl	policyStatus:<BKSHIDEventDeliveryPolicyObserver: 0x14e05cba0; token: com.apple.frontboard.systemappservices/FBSceneManager:sceneID%3Acom.sharkda.hootowl-1B8F959F-618F-4A0D-AD89-E09DEC0EAB34; status: none> was:ancestor
default	11:06:18.269046+0800	hootowl	policyStatus:<BKSHIDEventDeliveryPolicyObserver: 0x14ed16ac0; environment: keyboardFocus; status: none> was:target
default	11:06:18.269160+0800	hootowl	policyStatus:<BKSHIDEventDeliveryPolicyObserver: 0x14edcb7e0; environment: keyboardFocus; status: none> was:target
default	11:06:18.271644+0800	hootowl	Scene target of keyboard event deferring environment did change: 0; scene: UIWindowScene: 0x14ec14200; scene identity: com.apple.frontboard.systemappservices/FBSceneManager:sceneID%3Acom.sharkda.hootowl-1B8F959F-618F-4A0D-AD89-E09DEC0EAB34
default	11:06:18.273389+0800	hootowl	sceneOfRecord: sceneID: sceneID:com.sharkda.hootowl-1B8F959F-618F-4A0D-AD89-E09DEC0EAB34  persistentID: 1B8F959F-618F-4A0D-AD89-E09DEC0EAB34
default	11:06:18.282916+0800	hootowl	sceneOfRecord: sceneID: sceneID:com.sharkda.hootowl-1B8F959F-618F-4A0D-AD89-E09DEC0EAB34  persistentID: 1B8F959F-618F-4A0D-AD89-E09DEC0EAB34
default	11:06:18.282952+0800	hootowl	Deactivation reason added: 5; deactivation reasons: 4097 -> 4129; animating application lifecycle event: 1
default	11:06:18.791387+0800	hootowl	sceneOfRecord: sceneID: sceneID:com.sharkda.hootowl-1B8F959F-618F-4A0D-AD89-E09DEC0EAB34  persistentID: 1B8F959F-618F-4A0D-AD89-E09DEC0EAB34
default	11:06:18.791543+0800	hootowl	Deactivation reason removed: 5; deactivation reasons: 4129 -> 4097; animating application lifecycle event: 1
default	11:06:18.818424+0800	hootowl	[(FBSceneManager):sceneID:com.sharkda.hootowl-1B8F959F-618F-4A0D-AD89-E09DEC0EAB34] Received action(s) in scene-update: <FBSceneSnapshotAction: 0x6c285308>
default	11:06:18.822263+0800	hootowl	sceneOfRecord: sceneID: sceneID:com.sharkda.hootowl-1B8F959F-618F-4A0D-AD89-E09DEC0EAB34  persistentID: 1B8F959F-618F-4A0D-AD89-E09DEC0EAB34
default	11:06:18.822573+0800	hootowl	[0x151e40780] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	11:06:18.822599+0800	hootowl	[0x151e2c050] Session canceled.
default	11:06:18.822627+0800	hootowl	Deactivation reason added: 11; deactivation reasons: 4097 -> 6145; animating application lifecycle event: 0
default	11:06:18.822652+0800	hootowl	agent connection cancelled (details: Session manually canceled)
default	11:06:18.822675+0800	hootowl	[0x151e2c050] Disposing of session
default	11:06:18.824548+0800	hootowl	{"msg":"CLLocationManager", "event":"activity", "_cmd":"onDidEnterBackground:", "self":"0x105a46e70", "notification":"NSConcreteNotification 0x1522bfd00 {name = UIApplicationDidEnterBackgroundNotification; object = <_TtC7SwiftUIP33_ACC2C5639A7D76F611E170E831FCA49118SwiftUIApplication: 0x14ec14000>}"}
default	11:06:18.824595+0800	hootowl	Will add backgroundTask with taskName: com.apple.asset_manager.cache_resource_cleanup, expirationHandler: <__NSMallocBlock__: 0x1529fac40>
default	11:06:18.824620+0800	hootowl	Creating new assertion because there is no existing background assertion.
default	11:06:18.824636+0800	hootowl	Creating new background assertion
default	11:06:18.825345+0800	hootowl	Created new background assertion <BKSProcessAssertion: 0x151e2c050>
default	11:06:18.825495+0800	hootowl	Incrementing reference count for background assertion <BKSProcessAssertion: 0x151e2c050>
default	11:06:18.825510+0800	hootowl	Created background task <_UIBackgroundTaskInfo: 0x151beb340>: taskID = 19, taskName = com.apple.asset_manager.cache_resource_cleanup, creationTime = 697606 (elapsed = 0).
default	11:06:18.825588+0800	hootowl	Ending background task with UIBackgroundTaskIdentifier: 19
default	11:06:18.825874+0800	hootowl	Ending task with identifier 19 and description: <_UIBackgroundTaskInfo: 0x151beb340>: taskID = 19, taskName = com.apple.asset_manager.cache_resource_cleanup, creationTime = 697606 (elapsed = 0), _expireHandler: <__NSMallocBlock__: 0x1529f93e0>
default	11:06:18.828936+0800	hootowl	Decrementing reference count for assertion <BKSProcessAssertion: 0x151e2c050> (used by background task with identifier 19: <_UIBackgroundTaskInfo: 0x151beb340>: taskID = 19, taskName = com.apple.asset_manager.cache_resource_cleanup, creationTime = 697606 (elapsed = 0))
default	11:06:18.830363+0800	hootowl	Will invalidate assertion: <BKSProcessAssertion: 0x151e2c050> for task identifier: 19
default	11:06:18.830396+0800	hootowl	Will add backgroundTask with taskName: _UIRemoteKeyboard XPC disconnection, expirationHandler: (null)
default	11:06:18.830451+0800	hootowl	Creating new assertion because there is no existing background assertion.
default	11:06:18.830521+0800	hootowl	Creating new background assertion
default	11:06:18.831116+0800	hootowl	Created new background assertion <BKSProcessAssertion: 0x151e2c0f0>
default	11:06:18.831919+0800	hootowl	Incrementing reference count for background assertion <BKSProcessAssertion: 0x151e2c0f0>
default	11:06:18.832247+0800	hootowl	Created background task <_UIBackgroundTaskInfo: 0x151beb040>: taskID = 20, taskName = _UIRemoteKeyboard XPC disconnection, creationTime = 697606 (elapsed = 0).
default	11:06:18.832556+0800	hootowl	com.sharkda.hootowl(40785) invalidateConnection (appDidSuspend)
default	11:06:18.832580+0800	hootowl	[0x14f9bfc00] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	11:06:18.832876+0800	hootowl	Will add backgroundTask with taskName: com.apple.asset_manager.cache_resource_cleanup, expirationHandler: <__NSMallocBlock__: 0x1529f9e90>
default	11:06:18.832899+0800	hootowl	Reusing background assertion <BKSProcessAssertion: 0x151e2c0f0>
default	11:06:18.833076+0800	hootowl	Incrementing reference count for background assertion <BKSProcessAssertion: 0x151e2c0f0>
default	11:06:18.833105+0800	hootowl	Created background task <_UIBackgroundTaskInfo: 0x151beb480>: taskID = 21, taskName = com.apple.asset_manager.cache_resource_cleanup, creationTime = 697606 (elapsed = 0).
default	11:06:18.833132+0800	hootowl	Ending background task with UIBackgroundTaskIdentifier: 21
default	11:06:18.833318+0800	hootowl	Ending task with identifier 21 and description: <_UIBackgroundTaskInfo: 0x151beb480>: taskID = 21, taskName = com.apple.asset_manager.cache_resource_cleanup, creationTime = 697606 (elapsed = 0), _expireHandler: <__NSMallocBlock__: 0x1529f9e90>
default	11:06:18.836035+0800	hootowl	Decrementing reference count for assertion <BKSProcessAssertion: 0x151e2c0f0> (used by background task with identifier 21: <_UIBackgroundTaskInfo: 0x151beb480>: taskID = 21, taskName = com.apple.asset_manager.cache_resource_cleanup, creationTime = 697606 (elapsed = 0))
default	11:06:18.836126+0800	hootowl	Will add backgroundTask with taskName: com.apple.asset_manager.cache_resource_cleanup, expirationHandler: <__NSMallocBlock__: 0x1529f94a0>
default	11:06:18.836240+0800	hootowl	Reusing background assertion <BKSProcessAssertion: 0x151e2c0f0>
default	11:06:18.836808+0800	hootowl	Incrementing reference count for background assertion <BKSProcessAssertion: 0x151e2c0f0>
default	11:06:18.836827+0800	hootowl	Created background task <_UIBackgroundTaskInfo: 0x151beb480>: taskID = 22, taskName = com.apple.asset_manager.cache_resource_cleanup, creationTime = 697606 (elapsed = 0).
default	11:06:18.836873+0800	hootowl	Ending background task with UIBackgroundTaskIdentifier: 22
default	11:06:18.836894+0800	hootowl	Ending task with identifier 22 and description: <_UIBackgroundTaskInfo: 0x151beb480>: taskID = 22, taskName = com.apple.asset_manager.cache_resource_cleanup, creationTime = 697606 (elapsed = 0), _expireHandler: <__NSMallocBlock__: 0x1529f94a0>
default	11:06:18.836918+0800	hootowl	Decrementing reference count for assertion <BKSProcessAssertion: 0x151e2c0f0> (used by background task with identifier 22: <_UIBackgroundTaskInfo: 0x151beb480>: taskID = 22, taskName = com.apple.asset_manager.cache_resource_cleanup, creationTime = 697606 (elapsed = 0))
default	11:06:18.836971+0800	hootowl	Will add backgroundTask with taskName: com.apple.asset_manager.cache_resource_cleanup, expirationHandler: <__NSMallocBlock__: 0x1529f94a0>
default	11:06:18.836987+0800	hootowl	Reusing background assertion <BKSProcessAssertion: 0x151e2c0f0>
default	11:06:18.837054+0800	hootowl	Incrementing reference count for background assertion <BKSProcessAssertion: 0x151e2c0f0>
default	11:06:18.837078+0800	hootowl	Created background task <_UIBackgroundTaskInfo: 0x151beb280>: taskID = 23, taskName = com.apple.asset_manager.cache_resource_cleanup, creationTime = 697606 (elapsed = 0).
default	11:06:18.837199+0800	hootowl	Ending background task with UIBackgroundTaskIdentifier: 23
default	11:06:18.837570+0800	hootowl	Ending task with identifier 23 and description: <_UIBackgroundTaskInfo: 0x151beb280>: taskID = 23, taskName = com.apple.asset_manager.cache_resource_cleanup, creationTime = 697606 (elapsed = 0), _expireHandler: <__NSMallocBlock__: 0x1529f94a0>
default	11:06:18.837634+0800	hootowl	Decrementing reference count for assertion <BKSProcessAssertion: 0x151e2c0f0> (used by background task with identifier 23: <_UIBackgroundTaskInfo: 0x151beb280>: taskID = 23, taskName = com.apple.asset_manager.cache_resource_cleanup, creationTime = 697606 (elapsed = 0))
default	11:06:18.837716+0800	hootowl	RBDevice.didEnterBackground: in bg false, allows bg: false
default	11:06:18.837830+0800	hootowl	RBDevice.didEnterBackground: done
default	11:06:18.837850+0800	hootowl	Will add backgroundTask with taskName: com.apple.asset_manager.cache_resource_cleanup, expirationHandler: <__NSMallocBlock__: 0x1529f94a0>
default	11:06:18.837888+0800	hootowl	Reusing background assertion <BKSProcessAssertion: 0x151e2c0f0>
default	11:06:18.837905+0800	hootowl	Incrementing reference count for background assertion <BKSProcessAssertion: 0x151e2c0f0>
default	11:06:18.837924+0800	hootowl	Created background task <_UIBackgroundTaskInfo: 0x151beb280>: taskID = 24, taskName = com.apple.asset_manager.cache_resource_cleanup, creationTime = 697606 (elapsed = 0).
default	11:06:18.837944+0800	hootowl	Ending background task with UIBackgroundTaskIdentifier: 24
default	11:06:18.838598+0800	hootowl	Ending task with identifier 24 and description: <_UIBackgroundTaskInfo: 0x151beb280>: taskID = 24, taskName = com.apple.asset_manager.cache_resource_cleanup, creationTime = 697606 (elapsed = 0), _expireHandler: <__NSMallocBlock__: 0x1529f94a0>
default	11:06:18.838654+0800	hootowl	Decrementing reference count for assertion <BKSProcessAssertion: 0x151e2c0f0> (used by background task with identifier 24: <_UIBackgroundTaskInfo: 0x151beb280>: taskID = 24, taskName = com.apple.asset_manager.cache_resource_cleanup, creationTime = 697606 (elapsed = 0))
default	11:06:18.838809+0800	hootowl	0x152b8c018 - [pageProxyID=1596, webPageID=1597, PID=40803] WebPageProxy::applicationWillEnterForegroundForMedia: isSuspendedUnderLock? 0
default	11:06:18.839303+0800	hootowl	Deactivation reason removed: 0; deactivation reasons: 6145 -> 6144; animating application lifecycle event: 0
default	11:06:18.852571+0800	hootowl	Municipal+Lifecycle 25
⏸️ app → background: pausing GPS + 2 active proto timer(s)
default	11:06:18.852636+0800	hootowl	{"msg":"CLLocationManager", "event":"activity", "_cmd":"stopUpdatingLocation", "self":"0x105a46e70"}
default	11:06:18.866756+0800	hootowl	Will add backgroundTask with taskName: com.apple.uikit.applicationSnapshot, expirationHandler: <__NSMallocBlock__: 0x15154cd20>
default	11:06:18.866779+0800	hootowl	Reusing background assertion <BKSProcessAssertion: 0x151e2c0f0>
default	11:06:18.866853+0800	hootowl	Incrementing reference count for background assertion <BKSProcessAssertion: 0x151e2c0f0>
default	11:06:18.866936+0800	hootowl	Created background task <_UIBackgroundTaskInfo: 0x152b3cec0>: taskID = 25, taskName = com.apple.uikit.applicationSnapshot, creationTime = 697606 (elapsed = 0).
default	11:06:18.867001+0800	hootowl	forceReloadInputViews
default	11:06:18.867108+0800	hootowl	Reloading input views for key-window scene responder: <(null): 0x0; > force:Y
default	11:06:18.867449+0800	hootowl	Push traits update to screen for new style 1, <UIWindowScene: 0x14ec14200> (1B8F959F-618F-4A0D-AD89-E09DEC0EAB34)
default	11:06:18.867840+0800	hootowl	forceReloadInputViews
default	11:06:18.867974+0800	hootowl	Reloading input views for key-window scene responder: <(null): 0x0; > force:Y
default	11:06:18.868244+0800	hootowl	Should not send trait collection or coordinate space update, interface style 1 -> 1, <UIWindowScene: 0x14ec14200> (1B8F959F-618F-4A0D-AD89-E09DEC0EAB34)
default	11:06:18.870551+0800	hootowl	Received state update for 40785 (app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>, unknown-NotVisible
default	11:06:18.872164+0800	hootowl	Received state update for 40785 (app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>, unknown-NotVisible
default	11:06:18.892292+0800	hootowl	Performing snapshot request 0x151555a40 (type 1)
default	11:06:18.892402+0800	hootowl	[(FBSceneManager):sceneID:com.sharkda.hootowl-1B8F959F-618F-4A0D-AD89-E09DEC0EAB34] Sending action(s): <FBSSceneSnapshotRequestAction: 0x9f510002>
default	11:06:18.921252+0800	hootowl	Received state update for 40785 (app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>, unknown-NotVisible
default	11:06:18.936372+0800	hootowl	Snapshot request 0x151555a40 complete
default	11:06:18.936480+0800	hootowl	Push traits update to screen for new style 1, <UIWindowScene: 0x14ec14200> (1B8F959F-618F-4A0D-AD89-E09DEC0EAB34)
default	11:06:18.937684+0800	hootowl	forceReloadInputViews
default	11:06:18.937870+0800	hootowl	Reloading input views for key-window scene responder: <(null): 0x0; > force:Y
default	11:06:18.938148+0800	hootowl	Should not send trait collection or coordinate space update, interface style 2 -> 2, <UIWindowScene: 0x14ec14200> (1B8F959F-618F-4A0D-AD89-E09DEC0EAB34)
default	11:06:18.954384+0800	hootowl	MncplCyclopsScreen 78
🏠 body eval — items:6 firstObs:5s firstCar:7
default	11:06:18.974340+0800	hootowl	Performing snapshot request 0x1522c9c20 (type 1)
default	11:06:18.974406+0800	hootowl	[(FBSceneManager):sceneID:com.sharkda.hootowl-1B8F959F-618F-4A0D-AD89-E09DEC0EAB34] Sending action(s): <FBSSceneSnapshotRequestAction: 0x9f510003>
default	11:06:19.009593+0800	hootowl	Snapshot request 0x1522c9c20 complete
default	11:06:19.009721+0800	hootowl	forceReloadInputViews
default	11:06:19.009763+0800	hootowl	Reloading input views for key-window scene responder: <(null): 0x0; > force:Y
default	11:06:19.009906+0800	hootowl	Ending background task with UIBackgroundTaskIdentifier: 25
default	11:06:19.009918+0800	hootowl	Ending task with identifier 25 and description: <_UIBackgroundTaskInfo: 0x152b3cec0>: taskID = 25, taskName = com.apple.uikit.applicationSnapshot, creationTime = 697606 (elapsed = 0), _expireHandler: <__NSMallocBlock__: 0x15154cd20>
default	11:06:19.009949+0800	hootowl	Decrementing reference count for assertion <BKSProcessAssertion: 0x151e2c0f0> (used by background task with identifier 25: <_UIBackgroundTaskInfo: 0x152b3cec0>: taskID = 25, taskName = com.apple.uikit.applicationSnapshot, creationTime = 697606 (elapsed = 0))
default	11:06:19.011898+0800	hootowl	Push traits update to screen for new style 1, <UIWindowScene: 0x14ec14200> (1B8F959F-618F-4A0D-AD89-E09DEC0EAB34)
default	11:06:19.012772+0800	hootowl	Should not send trait collection or coordinate space update, interface style 1 -> 1, <UIWindowScene: 0x14ec14200> (1B8F959F-618F-4A0D-AD89-E09DEC0EAB34)
default	11:06:19.023188+0800	hootowl	MncplCyclopsScreen 78
🏠 body eval — items:6 firstObs:5s firstCar:7
default	11:06:19.044039+0800	hootowl	[0x14ee7caf0] [keyboardFocus] Disabling event deferring records requested: adding recreation reason: detachedContext; for reason: _UIEventDeferringManager: 0x14ee7caf0: disabling keyboardFocus: context detached for window: 0x14e20c800; contextID: 0xD3314357
default	11:06:19.044491+0800	hootowl	Will add backgroundTask with taskName: com.apple.UIKit.CABackingStoreCollect, expirationHandler: (null)
default	11:06:19.044769+0800	hootowl	Reusing background assertion <BKSProcessAssertion: 0x151e2c0f0>
default	11:06:19.044823+0800	hootowl	Incrementing reference count for background assertion <BKSProcessAssertion: 0x151e2c0f0>
default	11:06:19.044837+0800	hootowl	Created background task <_UIBackgroundTaskInfo: 0x151a0c9c0>: taskID = 26, taskName = com.apple.UIKit.CABackingStoreCollect, creationTime = 697606 (elapsed = 0).
default	11:06:19.047529+0800	hootowl	Target list changed:
default	11:06:19.048408+0800	hootowl	Ending background task with UIBackgroundTaskIdentifier: 20
default	11:06:19.048506+0800	hootowl	Ending task with identifier 20 and description: <_UIBackgroundTaskInfo: 0x151beb040>: taskID = 20, taskName = _UIRemoteKeyboard XPC disconnection, creationTime = 697606 (elapsed = 0), _expireHandler: (null)
default	11:06:19.048521+0800	hootowl	Decrementing reference count for assertion <BKSProcessAssertion: 0x151e2c0f0> (used by background task with identifier 20: <_UIBackgroundTaskInfo: 0x151beb040>: taskID = 20, taskName = _UIRemoteKeyboard XPC disconnection, creationTime = 697606 (elapsed = 0))
default	11:06:19.048856+0800	hootowl	sceneOfRecord: sceneID: sceneID:com.sharkda.hootowl-1B8F959F-618F-4A0D-AD89-E09DEC0EAB34  persistentID: 1B8F959F-618F-4A0D-AD89-E09DEC0EAB34
default	11:06:19.048978+0800	hootowl	Not push traits update to screen for new style 1, <UIWindowScene: 0x14ec14200> (1B8F959F-618F-4A0D-AD89-E09DEC0EAB34)
default	11:06:19.061644+0800	hootowl	Ending background task with UIBackgroundTaskIdentifier: 26
default	11:06:19.061660+0800	hootowl	Ending task with identifier 26 and description: <_UIBackgroundTaskInfo: 0x151a0c9c0>: taskID = 26, taskName = com.apple.UIKit.CABackingStoreCollect, creationTime = 697606 (elapsed = 0), _expireHandler: (null)
default	11:06:19.061674+0800	hootowl	Decrementing reference count for assertion <BKSProcessAssertion: 0x151e2c0f0> (used by background task with identifier 26: <_UIBackgroundTaskInfo: 0x151a0c9c0>: taskID = 26, taskName = com.apple.UIKit.CABackingStoreCollect, creationTime = 697606 (elapsed = 0))
default	11:06:19.061686+0800	hootowl	Will invalidate assertion: <BKSProcessAssertion: 0x151e2c0f0> for task identifier: 26
default	11:06:19.117748+0800	hootowl	Received state update for 40785 (app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>, unknown-NotVisible
default	11:06:19.269118+0800	hootowl	Received state update for 40785 (app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>, unknown-NotVisible
error	11:06:24.525037+0800	hootowl	tcp_output [C7.1.1.3:3] flags=[R.] seq=3466883954, ack=3963203469, win=2059 state=CLOSED rcv_nxt=3963203469, snd_una=3466882418
default	11:06:24.525877+0800	hootowl	tcp_close [C7.1.1.3:3] TCP Packets:
	 snd    0.000s seq 3466882417:3466882418 ack 0          win 65535 len 0    [SEC]
	 snd    2.084s seq 3466882417:3466882418 ack 0          win 65535 len 0    [S]
	 snd    1.082s seq 3466882417:3466882418 ack 0          win 65535 len 0    [S]
	 snd    1.375s seq 3466882417:3466882418 ack 0          win 65535 len 0    [S]
	 rcv    0.000s seq 3963203468:3963203469 ack 3466882418 win 65535 len 0    [S.]
	 snd    0.000s seq 3466882418:3466882418 ack 3963203469 win 2059  len 0    [.]
	 snd    0.007s seq 3466882418:3466883866 ack 3963203469 win 2059  len 1448 [.]
	 snd    0.000s seq 3466883866:3466883953 ack 3963203469 win 2059  len 87   [P.]
	 rcv    0.001s seq 3963203468:3963203469 ack 3466882418 win 65535 len 0    [S.]
	 snd    0.000s seq 3466883953:3466883953 ack 3963203469 win 2059  len 0    [.]
	 rcv    2.110s seq 3963203469:3963203469 ack 3466882418 win 285   len 0    [.]
	 snd    0.000s seq 3466882418:3466883866 ack 3963203469 win 2059  len 1448 [.]
	 snd    7.412s seq 3466883953:3466883954 ack 3963203469 win 2059  len 0    [F.]
	 rcv    0.697s seq 3963203469:3963203469 ack 3466882418 win 291   len 0    [.]
	 snd    5.920s seq 3466882418:3466883866 ack 3963203469 win 2059  len 1448 [.]
	 snd   36.928s seq 3466882418:3466883866 ack 3963203469 win 2059  len 1448 [.]
	 snd   54.688s seq 3466882418:3466883866 ack 3963203469 win 2059  len 1448 [.]
	 snd   64.000s seq 3466882418:3466883866 ack 3963203469 win 2059  len 1448 [.]
	 snd   64.000s seq 3466882418:3466883866 ack 3963203469 win 2059  len 1448 [.]
	 snd   64.000s seq 3466882418:3466883866 ack 3963203469 win 2059  len 1448 [.]
	 snd   64.000s seq 3466882418:3466883866 ack 3963203469 win 2059  len 1448 [.]
	 snd   64.000s seq 3466882418:3466883866 ack 3963203469 win 2059  len 1448 [.]
	 snd   64.000s seq 3466882418:3466883866 ack 3963203469 win 2059  len 1448 [.]
	 snd   64.000s seq 3466882418:3466883866 ack 3963203469 win 2059  len 1448 [.]
	 snd   64.000s seq 3466882418:3466883866 ack 3963203469 win 2059  len 1448 [.]
	 snd   64.000s seq 3466882418:3466883866 ack 3963203469 win 2059  len 1448 [.]
	 snd   64.000s seq 3466883954:3466883954 ack 3963203469 win 2059  len 0    [R.]
	Last packet 0ms ago.
default	11:06:31.826942+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:06:31.828931+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c6554 posting AVAudioSessionAvailableInputsChangeNotification
default	11:06:31.828944+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:06:33.024250+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:06:33.028505+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c6554 posting AVAudioSessionAvailableInputsChangeNotification
default	11:06:33.028537+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:06:33.032881+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:06:33.035276+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c6554 posting AVAudioSessionAvailableInputsChangeNotification
default	11:06:33.035310+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:06:42.541716+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:06:43.687416+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c6554 posting AVAudioSessionAvailableInputsChangeNotification
default	11:06:43.689116+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:06:43.689171+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:06:43.692276+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c6554 posting AVAudioSessionAvailableInputsChangeNotification
default	11:06:43.692780+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:06:43.706312+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c6554 posting AVAudioSessionAvailableInputsChangeNotification
default	11:06:43.706321+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:06:44.511509+0800	hootowl	Connection 21: cleaning up
default	11:06:44.511645+0800	hootowl	[C21 AA270A28-87AD-41CC-971F-06C9FF16F07D tcgbusfs.blob.core.windows.net:443 quic-connection, url: https://tcgbusfs.blob.core.windows.net/blobtcmsv/TCMSV_allavailable.json, definite, attribution: developer] cancel
default	11:06:44.512003+0800	hootowl	[C21 AA270A28-87AD-41CC-971F-06C9FF16F07D tcgbusfs.blob.core.windows.net:443 quic-connection, url: https://tcgbusfs.blob.core.windows.net/blobtcmsv/TCMSV_allavailable.json, definite, attribution: developer] cancelled
	[C21.1.1.1 D04C4F5C-EE80-4F40-9298-4EE4A4319271 192.168.50.191:56391<->20.150.22.100:443]
	Connected Path: satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good
	Privacy Stance: Not Eligible
	Duration: 31.924s, DNS @0.004s took 0.030s, TCP @0.037s took 0.081s,  took 0.203s
	bytes in/out: 483979/2357, packets in/out: 63/63, rtt: 0.084s, retransmitted bytes: 0, out-of-order bytes: 0
	ecn packets sent/acked/marked/lost: 5/4/0/0
default	11:06:44.581644+0800	hootowl	nw_protocol_tcp_log_summary [C21.1.1.1:3] 
	[AB673CF0-F6E5-4195-AF11-9C2691AFCFA0 192.168.50.191:56391<->20.150.22.100:443]
	Init: 1, Conn_Time: 80.826ms, SYNs: 1, WR_T: 0/0, RD_T: 0/0, TFO: 0/0/0, ECN: 0/1/1, Accurate ECN (client/server): Disabled/Disabled, TS: 1, TSO: 0
	rtt_cache: process, rtt_upd: 5, rtt: 84.656ms, rtt_var: 26.500ms rtt_nc: 84.656ms, rtt_var_nc: 26.500ms base rtt: 65ms
	ACKs-compressed: 4, ACKs delayed: 28 delayed ACKs sent: 0
default	11:06:44.582328+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C21] reporting state cancelled
default	11:06:44.582354+0800	hootowl	Connection 21: done
default	11:06:44.582482+0800	hootowl	tcp_output [C21.1.1.1:3] flags=[F.] seq=2379522607, ack=1650864920, win=5261 state=FIN_WAIT_1 rcv_nxt=1650864920, snd_una=2379522583
default	11:06:44.585752+0800	hootowl	tcp_input [C21.1.1.1:3] flags=[F.] seq=1650864920, ack=2379522608, win=16382 state=FIN_WAIT_2 rcv_nxt=1650864920, snd_una=2379522608
default	11:06:45.263009+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.263168+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.263191+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.263437+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.263565+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.264705+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.264816+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.264847+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.264981+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.265021+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.266732+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.266892+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.267014+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.267191+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.267231+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.268343+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.268431+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.268452+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.268610+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.268661+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.269793+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.269880+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.269908+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.270044+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.270093+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.271219+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.271333+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.271378+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.271491+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.271522+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.272643+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.272743+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.272754+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.272906+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.272958+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.274014+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.274105+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.274131+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.274277+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.274334+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.275567+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.275654+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.275710+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.275837+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.275875+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.276912+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.276992+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.277003+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.277187+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.277251+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.278378+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.278460+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.278512+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.278624+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.278655+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.279779+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.279870+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.279886+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.280020+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.280066+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.281198+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.281286+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.281303+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.281451+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.281493+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.282591+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.282701+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.282773+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.282847+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.282893+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.284123+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.284205+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.284215+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.284392+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.284430+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.285734+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.285820+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.285830+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.285964+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.286000+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.287256+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.287379+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.287422+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.287511+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.287564+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.288836+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.288925+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.288943+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.289102+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.289139+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.290271+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.290353+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.290380+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.290538+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.290579+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.291677+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.291764+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.291784+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.291922+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.291951+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.293083+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.293168+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.293221+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.293351+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.293391+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.294496+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.294584+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.294636+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.294763+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.294795+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.296135+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.296220+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.296250+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.296397+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.296458+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.297574+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.297663+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.297692+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.297842+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.297888+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.298898+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.298994+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.299036+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.299170+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.299210+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.300338+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.300437+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.300462+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.300602+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.300640+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.301763+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.301851+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.301878+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.302021+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.302057+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.335874+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.335901+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.335908+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.335988+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.336004+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.336366+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.336416+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.336436+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.336507+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.336513+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.336755+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.336772+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.336780+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.336826+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.336848+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.338399+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.338422+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.338428+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.338471+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.338483+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.338740+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.338762+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.338774+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.338823+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.338834+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.339323+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.339344+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.339349+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.339400+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.339425+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.339657+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.339677+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.339684+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.339730+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.339736+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.340126+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.340143+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.340151+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.340197+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.340203+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.340512+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.340531+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.340538+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.340606+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.340612+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.340856+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.340873+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.340878+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.340919+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.340929+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.341161+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.341178+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.341185+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.341226+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.341236+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.341517+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.341592+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.341603+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.341672+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.341689+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.341970+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.341989+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.341996+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.342047+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.342056+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.342328+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.342344+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.342350+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.342395+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.342408+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.342643+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.342659+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.342665+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.342771+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.342782+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.343182+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.343211+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.343219+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.343270+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.343280+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.343550+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.343573+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.343580+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.343621+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.343636+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.343867+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.343883+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.343889+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.343935+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.343945+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.344244+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.344284+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.344300+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.344363+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.344374+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.344688+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.344712+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.344717+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.344758+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.344772+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.345019+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.345036+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.345041+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.345088+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.345098+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.345338+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.345357+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.345364+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.345417+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.345423+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.346079+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.346118+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.346126+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.346184+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.346215+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.346775+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.346806+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.346812+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.346873+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.346889+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.347120+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.347142+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.347153+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.347208+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.347214+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.347548+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.347570+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.347577+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.347652+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.347666+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.347922+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.347939+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.347953+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.347995+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.348002+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.348259+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.348287+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.348297+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.348351+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.348357+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.348648+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.348689+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.348699+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.348746+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.348761+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.349195+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.349221+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.349229+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.349296+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.349309+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.349878+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.349982+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.350013+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.350157+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.350198+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.351301+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.351402+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.351459+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.351612+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.351682+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.353995+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.354183+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.354245+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.354490+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.354583+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.356904+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.357007+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.357036+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.357198+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.357239+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.358418+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.358521+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.358534+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.358704+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.358769+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.359900+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.359992+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.360049+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.360181+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.360224+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.361351+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.361452+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.361463+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.361643+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.361682+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.362905+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.362998+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.363054+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.363183+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.363244+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.364331+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.364428+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.364454+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.364594+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.364655+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.365900+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.366049+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.366153+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.660329+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.660353+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.660367+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.660406+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.660417+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.660748+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.660773+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.660787+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.678364+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.678390+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.678765+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.678786+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.678798+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.678868+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.678893+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.679214+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.679234+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.679240+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.679289+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.679310+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.734169+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.734483+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.734508+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.734522+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.734579+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.734596+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.734868+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.734898+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.734905+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.734971+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.734982+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.735270+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.735300+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.735307+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.735361+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.735373+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.735699+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.735718+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.735734+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.735797+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.735805+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.735980+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.735997+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.736013+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.736068+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.736084+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.746308+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.746346+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.746373+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.746417+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.746463+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.746999+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.747040+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.747052+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.747102+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.747114+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.747443+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.890552+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.890635+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.890651+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.890820+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.890835+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.891179+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:45.891196+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:45.891210+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:45.891263+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:45.891279+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:45.891577+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:46.738800+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:46.738828+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:46.738837+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:46.742371+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:46.742424+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:46.742492+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:46.742602+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:46.742657+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:46.744353+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:46.744385+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:46.744416+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:46.744503+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:46.744539+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:46.750715+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:46.750763+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:46.750781+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:46.750842+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:46.750852+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:46.751135+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:46.751157+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:46.751169+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:46.751220+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:46.751235+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:46.751247+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:46.751444+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:46.751465+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:46.751471+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:46.751516+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:46.751522+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:46.751787+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:46.751811+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:46.751816+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:46.751872+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:46.751882+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:46.752262+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:46.752288+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:46.752296+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:46.752347+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:46.752378+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:46.753097+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:46.753161+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:46.753196+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:46.753237+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:46.753257+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:46.754153+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:06:46.754201+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:06:46.754220+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:06:46.754250+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:06:46.754291+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:06:50.609739+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:06:50.611912+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c6554 posting AVAudioSessionAvailableInputsChangeNotification
default	11:06:50.611920+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:07:12.280728+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:07:12.281403+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:07:12.281493+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:07:12.282176+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:07:12.282248+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:07:14.673096+0800	hootowl	tcp_close [C21.1.1.1:3] TCP Packets:
	 rcv    0.000s seq 1650646256:1650656336 ack 2379522583 win 16382 len 10080 [P.] ECT0
	 snd    0.000s seq 2379522583:2379522583 ack 1650656336 win 5217  len 0    [.]
	 rcv    0.004s seq 1650656336:1650672176 ack 2379522583 win 16382 len 15840 [.] ECT0
	 rcv    0.000s seq 1650672176:1650673616 ack 2379522583 win 16382 len 1440 [.] ECT0
	 snd    0.000s seq 2379522583:2379522583 ack 1650673616 win 5217  len 0    [.]
	 rcv    0.058s seq 1650673616:1650689456 ack 2379522583 win 16382 len 15840 [.] ECT0
	 rcv    0.000s seq 1650689456:1650705296 ack 2379522583 win 16382 len 15840 [.] ECT0
	 rcv    0.000s seq 1650705296:1650719696 ack 2379522583 win 16382 len 14400 [.] ECT0
	 snd    0.000s seq 2379522583:2379522583 ack 1650719696 win 5217  len 0    [.]
	 rcv    0.003s seq 1650719696:1650735536 ack 2379522583 win 16382 len 15840 [.] ECT0
	 rcv    0.000s seq 1650735536:1650751376 ack 2379522583 win 16382 len 15840 [.] ECT0
	 rcv    0.000s seq 1650751376:1650755696 ack 2379522583 win 16382 len 4320 [.] ECT0
	 snd    0.000s seq 2379522583:2379522583 ack 1650755696 win 5217  len 0    [.]
	 rcv    0.000s seq 1650755696:1650758576 ack 2379522583 win 16382 len 2880 [.] ECT0
	 rcv    0.000s seq 1650758576:1650762896 ack 2379522583 win 16382 len 4320 [.] ECT0
	 snd    0.000s seq 2379522583:2379522583 ack 1650762896 win 5217  len 0    [.]
	 rcv    0.000s seq 1650762896:1650765776 ack 2379522583 win 16382 len 2880 [.] ECT0
	 snd    0.000s seq 2379522583:2379522583 ack 1650765776 win 5217  len 0    [.]
	 rcv    0.119s seq 1650765776:1650781616 ack 2379522583 win 16382 len 15840 [.] ECT0
	 rcv    0.000s seq 1650781616:1650797456 ack 2379522583 win 16382 len 15840 [.] ECT0
	 rcv    0.000s seq 1650797456:1650811856 ack 2379522583 win 16382 len 14400 [.] ECT0
	 snd    0.000s seq 2379522583:2379522583 ack 1650811856 win 5217  len 0    [.]
	 rcv    0.003s seq 1650811856:1650827696 ack 2379522583 win 16382 len 15840 [.] ECT0
	 rcv    0.000s seq 1650827696:1650843536 ack 2379522583 win 16382 len 15840 [.] ECT0
	 rcv    0.000s seq 1650843536:1650853616 ack 2379522583 win 16382 len 10080 [.] ECT0
	 snd    0.000s seq 2379522583:2379522583 ack 1650853616 win 5217  len 0    [.]
	 rcv    0.004s seq 1650853616:1650856496 ack 2379522583 win 16382 len 2880 [.] ECT0
	 snd    0.000s seq 2379522583:2379522583 ack 1650856496 win 5217  len 0    [.]
	 rcv    0.050s seq 1650856496:1650857936 ack 2379522583 win 16382 len 1440 [.] ECT0
	 snd    0.000s seq 2379522583:2379522583 ack 1650857936 win 5239  len 0    [.]
	 rcv    0.001s seq 1650857936:1650862256 ack 2379522583 win 16382 len 4320 [.] ECT0
	 snd    0.000s seq 2379522583:2379522583 ack 1650862256 win 5261  len 0    [.]
	 rcv    0.000s seq 1650862256:1650864920 ack 2379522583 win 16382 len 2664 [P.] ECT0
	 snd    0.000s seq 2379522583:2379522583 ack 1650864920 win 5261  len 0    [.]
	 rcv    0.452s seq 1650864920:1650864920 ack 2379522583 win 16382 len 0    [.]
	 snd   30.480s seq 2379522583:2379522607 ack 1650864920 win 5261  len 24   [P.] ECT0
	 snd    0.002s seq 2379522607:2379522608 ack 1650864920 win 5261  len 0    [F.]
	 rcv    0.068s seq 1650864920:1650864920 ack 2379522608 win 16382 len 0    [.]
	 rcv    0.001s seq 1650864920:1650864921 ack 2379522608 win 16382 len 0    [F.]
	 snd    0.000s seq 2379522608:2379522608 ack 1650864921 win 5261  len 0    [.]
	Last packet 30088ms ago.
default	11:07:26.639520+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:07:26.658394+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c6554 posting AVAudioSessionAvailableInputsChangeNotification
default	11:07:26.659219+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:07:26.707844+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:07:26.718101+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c6554 posting AVAudioSessionAvailableInputsChangeNotification
default	11:07:26.718116+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:07:26.737441+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:07:26.749722+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c6554 posting AVAudioSessionAvailableInputsChangeNotification
default	11:07:26.749775+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:07:26.769284+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:07:26.780082+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c6554 posting AVAudioSessionAvailableInputsChangeNotification
default	11:07:26.780203+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:07:34.105323+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:07:34.125442+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c6554 posting AVAudioSessionAvailableInputsChangeNotification
default	11:07:34.125474+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:07:34.153274+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:07:34.170367+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c6554 posting AVAudioSessionAvailableInputsChangeNotification
default	11:07:34.170706+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:07:34.198236+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:07:34.213577+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c6554 posting AVAudioSessionAvailableInputsChangeNotification
default	11:07:34.213620+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:07:38.277302+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:07:38.277622+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:07:38.277662+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:07:38.278156+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:07:38.278194+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:07:38.280148+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:07:38.280390+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:07:38.280402+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:07:38.280864+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:07:38.280894+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:07:38.282640+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:07:38.282851+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:07:38.282882+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:07:38.283327+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:07:38.283339+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:07:38.284859+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:07:38.285058+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:07:38.285099+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:07:38.285510+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:07:38.285537+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:07:38.287015+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:07:38.287216+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:07:38.287245+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:07:38.287693+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:07:38.287713+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:07:38.289674+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:07:38.289853+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:07:38.289865+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:07:38.290257+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:07:38.290299+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:07:38.292331+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:07:38.292649+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:07:38.292660+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:07:38.293162+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:07:38.293193+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:07:38.294711+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:07:38.294913+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:07:38.294940+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:07:38.295372+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:07:38.295402+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:07:38.296941+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:07:38.297142+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:07:38.297174+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:07:38.297612+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:07:38.297713+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:07:38.299355+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:07:38.299556+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:07:38.299586+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:07:38.300012+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:07:38.300040+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:07:38.301455+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:07:38.301646+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:07:38.301676+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:07:38.302110+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:07:38.302139+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:07:38.303843+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:07:38.304044+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:07:38.304073+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:07:38.304507+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:07:38.304534+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:07:38.306289+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:07:38.306524+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:07:38.306565+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:07:38.307079+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:07:38.307266+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:07:38.308825+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:07:38.309045+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:07:38.309124+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:07:38.309514+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:07:38.309555+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:07:38.310986+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:07:38.311197+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:07:38.311223+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:07:38.311656+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:07:38.311685+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:07:38.313082+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:07:38.313277+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:07:38.313308+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:07:38.313730+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:07:38.313829+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:07:38.315228+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:07:38.315443+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:07:38.315452+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:07:38.315903+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:07:38.315929+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:07:38.317378+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:07:38.317583+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:07:38.317631+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:07:38.318063+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:07:38.318119+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:07:38.319725+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:07:38.319933+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:07:38.319964+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:07:38.320410+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:07:38.320419+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:07:38.322370+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:07:38.322580+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:07:38.322611+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:07:38.323096+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:07:38.323162+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:07:38.324487+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:07:38.324739+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:07:38.324769+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:07:38.325227+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:07:38.325258+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:07:38.326759+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:07:38.326945+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:07:38.326977+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:07:38.327414+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:07:38.327444+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:07:38.329322+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:07:38.329598+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:07:38.329634+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:07:38.330049+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:07:38.330077+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:07:38.331444+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:07:38.331651+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:07:38.331684+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:07:38.332149+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:07:38.332170+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:07:38.333600+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:07:38.333817+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:07:38.333846+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:07:38.334281+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:07:38.334311+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:07:38.335778+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:07:38.335978+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:07:38.336009+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:07:38.336446+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:07:38.336472+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:07:38.337913+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:07:38.338123+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:07:38.338157+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:07:38.338608+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:07:38.338670+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:07:38.340063+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:07:38.340280+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:07:38.340311+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:07:38.340744+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:07:38.340851+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:07:38.342099+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:07:38.342299+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:07:38.342328+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:07:38.342823+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:07:38.342852+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:07:38.344171+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:07:38.344364+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:07:38.344393+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:07:38.344850+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:07:38.344877+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:07:38.346508+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:07:38.346729+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:07:38.346775+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:07:38.347199+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:07:38.347229+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:07:38.348575+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:07:38.348871+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:07:38.348947+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:07:38.349299+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:07:38.349327+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:07:38.350759+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:07:38.350956+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:07:38.350996+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:07:38.351531+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:07:38.351545+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:07:38.353001+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:07:38.353207+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:07:38.353235+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:07:38.353708+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:07:38.353732+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:07:38.355134+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:07:38.355334+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:07:38.355364+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:07:38.355823+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:07:38.355851+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:07:38.357314+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:07:38.357518+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:07:38.357542+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:07:38.357991+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:07:38.358020+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:07:38.359671+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:07:38.359903+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:07:38.359931+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:07:38.360372+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:07:38.360403+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:07:38.361742+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:07:38.361953+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:07:38.361982+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:07:38.362435+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:07:38.362448+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:07:38.363864+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:07:38.364064+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:07:38.364088+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:07:38.364706+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:07:38.364739+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:07:38.366067+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:07:38.366275+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:07:38.366303+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:07:38.366741+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:07:38.366775+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:07:38.368134+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:07:38.368346+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:07:38.368366+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:07:38.368911+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:07:38.369004+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:07:38.370256+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:07:38.370457+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:07:38.370490+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:07:38.370924+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:07:38.370951+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:07:38.372411+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:07:38.372632+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:07:38.372663+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:07:38.373089+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:07:38.373116+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:07:38.374906+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:07:38.375113+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:07:38.375147+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:07:38.375601+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:07:38.375628+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:07:38.377022+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:07:38.377238+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:07:38.377266+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:07:38.377732+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:07:38.377777+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:07:38.379386+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:07:38.379595+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:07:38.379628+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:07:38.380090+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:07:38.380099+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:07:38.381480+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:07:38.381686+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:07:38.381714+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:07:38.382200+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:07:38.382226+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:07:38.383632+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:07:38.383846+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:07:38.383860+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:07:38.384340+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:07:38.384366+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:07:38.459870+0800	hootowl	Received state update for 40785 (app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>, unknown-NotVisible
default	11:08:04.456084+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:04.456921+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:04.457148+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:04.458391+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:04.458446+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:30.459175+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:30.460026+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:30.460089+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:30.461383+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:30.461436+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:30.466255+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:30.466809+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:30.467466+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:30.467926+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:30.467955+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:30.471379+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:30.471824+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:30.472021+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:30.472897+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:30.472959+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:30.476247+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:30.476526+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:30.476783+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:30.477300+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:30.477356+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:30.480552+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:30.480850+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:30.480989+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:30.481533+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:30.481625+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:30.483618+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:30.483875+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:30.483983+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:30.484450+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:30.484493+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:30.486535+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:30.486805+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:30.486825+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:30.487318+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:30.487392+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:30.489166+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:30.489384+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:30.489402+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:30.489979+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:30.489990+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:30.491599+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:30.492082+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:30.492230+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:30.492423+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:30.492507+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:30.494229+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:30.494441+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:30.494471+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:30.494968+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:30.495038+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:30.497462+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:30.497531+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:30.497778+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:30.497994+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:30.498065+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:30.499727+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:30.499954+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:30.500013+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:30.500525+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:30.500551+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:30.502295+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:30.502542+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:30.502562+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:30.503027+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:30.503065+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:30.504836+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:30.505047+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:30.505080+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:30.505551+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:30.505569+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:30.507730+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:30.507952+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:30.507971+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:30.508445+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:30.508522+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:30.510180+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:30.510395+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:30.510464+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:30.510927+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:30.510957+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:30.512630+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:30.512864+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:30.512882+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:30.513386+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:30.513477+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:30.515209+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:30.515439+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:30.515458+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:30.515914+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:30.515940+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:30.518065+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:30.518301+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:30.518322+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:30.518831+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:30.518850+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:30.520355+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:30.520590+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:30.520637+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:30.521090+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:30.521104+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:30.522686+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:30.522918+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:30.522933+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:30.523395+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:30.523416+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:30.524879+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:30.525089+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:30.525108+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:30.525599+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:30.525629+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:30.527688+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:30.527925+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:30.527944+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:30.528438+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:30.528467+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:30.530016+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:30.530232+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:30.530256+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:30.530715+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:30.530735+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:30.532166+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:30.532376+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:30.532408+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:30.532887+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:30.532916+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:30.534523+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:30.534776+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:30.534795+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:30.535331+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:30.535362+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:30.537292+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:30.537516+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:30.537535+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:30.538032+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:30.538068+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:30.539681+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:30.539891+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:30.539921+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:30.540379+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:30.540410+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:30.542443+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:30.542670+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:30.542690+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:30.543199+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:30.543318+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:30.544852+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:30.545068+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:30.545093+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:30.545588+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:30.545607+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:30.547538+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:30.547758+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:30.547775+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:30.548271+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:30.548300+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:30.549845+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:30.550051+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:30.550080+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:30.550585+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:30.550611+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:30.552251+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:30.552480+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:30.552498+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:30.552978+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:30.553003+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:30.554447+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:30.554656+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:30.554672+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:30.555146+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:30.555226+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:30.556858+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:30.557023+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:30.557284+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:30.557585+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:30.557635+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:30.559201+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:30.559413+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:30.559431+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:30.559915+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:30.559931+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:30.561465+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:30.561682+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:30.561697+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:30.607986+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:30.608082+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:30.613614+0800	hootowl	Received state update for 40785 (app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>, unknown-NotVisible
default	11:08:30.715557+0800	hootowl	Received state update for 40785 (app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>, unknown-NotVisible
default	11:08:56.609184+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.610054+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.610158+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.611476+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.611565+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.615731+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.616131+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.616249+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.617342+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.617372+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.620645+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.621237+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.621273+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.622181+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.622246+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.625062+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.625447+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.625497+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.626236+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.626247+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.628312+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.628573+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.628657+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.629254+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.629282+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.631545+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.631797+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.631839+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.632352+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.632401+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.634449+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.634669+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.634685+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.635158+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.635189+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.637069+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.637286+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.637315+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.637774+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.637871+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.639467+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.639698+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.639818+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.640233+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.640264+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.642323+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.642565+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.642584+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.643064+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.643100+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.644798+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.645020+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.645036+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.645479+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.645493+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.647492+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.647732+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.647797+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.648222+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.648238+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.650083+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.650312+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.650330+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.650897+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.650978+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.652746+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.652956+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.652997+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.653489+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.653562+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.655308+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.655529+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.655548+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.655996+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.656009+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.657756+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.657975+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.658085+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.658458+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.658653+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.660365+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.660578+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.660655+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.661262+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.661312+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.663402+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.663731+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.664041+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.664283+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.664356+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.666135+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.666354+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.666382+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.666901+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.666918+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.668673+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.668926+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.668946+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.669394+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.669425+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.671351+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.671576+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.671612+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.672117+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.672151+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.674046+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.674254+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.674283+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.674747+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.674774+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.676413+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.676649+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.676675+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.677134+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.677431+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.678915+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.679141+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.679157+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.679655+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.679675+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.681514+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.681823+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.681883+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.682296+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.682327+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.684233+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.684453+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.684480+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.684958+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.684986+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.687197+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.687433+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.687474+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.687947+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.687974+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.689574+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.689789+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.689810+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.690519+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.690557+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.692121+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.692466+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.692483+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.693011+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.693028+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.694715+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.694941+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.694960+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.695483+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.695650+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.698358+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.698749+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.698770+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.699285+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.699346+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.701287+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.701527+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.701545+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.702033+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.702092+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.704072+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.704303+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.704318+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.704832+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.704854+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.706804+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.707062+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.707082+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.707580+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.707643+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.710099+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.710347+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.710366+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.711218+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.711265+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.713046+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.713438+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.713572+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.713896+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.713903+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.715747+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.715971+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.715997+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.716471+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.716506+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.763375+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.763665+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.763730+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.764014+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.764051+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.765477+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.765625+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.765640+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.765820+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.765866+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.767256+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.767409+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.767422+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.767643+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.767652+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.768924+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.769074+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.769083+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.769268+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.769310+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.770642+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.770772+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.770798+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.771003+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.771045+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.772468+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.772594+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.772603+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.772809+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.772852+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.774285+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.774413+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.774478+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.774719+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.774729+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.775924+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.776107+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.776114+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.776268+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.776309+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.777793+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.777909+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.777960+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.778125+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.778249+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.779839+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.779968+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.780004+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.780183+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.780225+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.781651+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.781776+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.781944+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.782001+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.782057+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.783587+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.783713+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.783749+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.783942+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.783998+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.785830+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.785960+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.786098+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.786220+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.786284+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.788573+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.788731+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.788809+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.789074+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.789161+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.791160+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.791333+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.791344+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.791531+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.791610+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.792973+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.793095+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.793131+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.793323+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.793364+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.794811+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.794941+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.794955+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.795176+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.795218+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.796545+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.796670+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.796709+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.796899+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.796911+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.798338+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.798465+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.798500+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.798691+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.798705+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.799983+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.800111+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.800182+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.800329+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.800369+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.801757+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.801879+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.801915+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.802103+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.802153+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.803342+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.803462+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.803498+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.803703+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.803755+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.804965+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.805083+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.805118+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.805299+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.805344+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.806658+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.806823+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.806838+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.807035+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.807080+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.808402+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.808541+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.808604+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.808764+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.808795+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.810008+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.810141+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.810159+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.810348+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.810417+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.811768+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.811891+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.811925+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.812136+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.812180+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.813433+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.813560+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.813599+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.813796+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.813807+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.814997+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.815182+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.815191+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.815366+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.815402+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.816622+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.816745+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.816850+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.816986+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.817100+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.818662+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.818797+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.818849+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.820591+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.820620+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.821803+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.821929+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.821993+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.822154+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.822201+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.823474+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.823600+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.823636+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.823838+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.823873+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.825125+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.825249+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.825287+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.825572+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.825582+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.826750+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.826877+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.826910+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.827109+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.827124+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.828438+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.828556+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.828579+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.828773+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.828824+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.830075+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.830193+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.830229+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.830435+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.830482+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.834629+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.834773+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.834800+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.835005+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.835058+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.836321+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.836457+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.836493+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.836693+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.836736+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.837898+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.838036+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.838068+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.838282+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.838325+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.839643+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.839771+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.839823+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.839986+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.840040+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.841371+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.841528+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.841708+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.841758+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.841799+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.843055+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.843178+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.843218+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.843393+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.843436+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.844611+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.844742+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.844757+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.844970+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.845012+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.846242+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.846366+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.846501+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.846616+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.846659+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.848009+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.848139+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.848170+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.848366+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.848422+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.849699+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.849833+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.849869+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.850172+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.850181+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.851413+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.851600+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.851774+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.851813+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.851829+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.853207+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.853349+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.853382+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.853579+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.853616+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.854887+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.855048+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.855062+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.855262+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.855302+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.856661+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.856841+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.856857+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.857054+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.857109+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.858550+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.858691+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.858728+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.858947+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.859020+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.860735+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.860886+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.860901+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.861114+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.861160+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.862665+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.862802+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.862831+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.863064+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.863099+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.864414+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.864546+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.864581+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.864794+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.864844+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.866084+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.866220+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.866236+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.866458+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.866491+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.977551+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.977907+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.978116+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.978235+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.978251+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.980498+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.980621+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.980699+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.980812+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.981003+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.984018+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.984147+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.984213+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.984369+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.984438+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.986596+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.986694+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.986731+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.986898+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.986959+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.988217+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.988317+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.988331+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.988503+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.988559+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.989948+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.990048+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.990268+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.990310+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.990324+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.991683+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.991801+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.991837+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.992037+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.992084+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.993475+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.993575+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.993608+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.993766+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.993815+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.995215+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.995316+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.995374+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.995517+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.995577+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.996872+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.996973+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.997013+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.997411+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.997426+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:56.998470+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:56.998579+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:56.998640+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:56.998771+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:56.998832+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:57.000015+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:57.000117+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:57.000174+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:57.000317+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:57.000363+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:57.001883+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:57.002027+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:57.002104+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:57.002307+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:57.002346+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:57.003679+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:57.003962+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:57.003973+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:57.004029+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:57.004038+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:57.005192+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:57.005311+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:57.005343+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:57.005527+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:57.005559+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:57.007021+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:57.007136+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:57.007164+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:57.007330+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:57.007431+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:57.008693+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:57.008805+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:57.008826+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:57.009126+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:57.009144+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:57.010314+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:57.010365+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:57.010379+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:57.010535+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:57.010580+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:57.011893+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:57.011991+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:57.012003+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:57.012221+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:57.012253+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:57.013573+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:57.013681+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:57.013711+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:57.013889+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:57.013920+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:57.015152+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:57.015278+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:57.015328+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:57.015471+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:57.015552+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:57.016655+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:57.016925+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:57.016936+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:57.017016+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:57.017030+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:57.018354+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:57.018466+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:57.018496+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:57.018646+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:57.018712+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:57.020051+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:57.020164+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:57.020196+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:57.020348+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:57.020395+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:57.021604+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:57.021716+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:57.021744+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:57.021924+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:57.022097+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:57.023401+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:57.023514+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:57.023550+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:57.023684+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:57.023729+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:57.024996+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:57.025104+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:57.025139+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:57.025393+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:57.025402+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:57.026524+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:57.026572+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:57.026609+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:57.026771+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:57.026830+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:57.028157+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:57.028271+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:57.028305+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:57.028464+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:57.028518+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:57.029661+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:57.029756+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:57.029799+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:57.029973+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:57.030025+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:57.031280+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:57.031399+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:57.031433+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:57.031591+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:57.031651+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:57.033049+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:57.033165+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:57.033196+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:57.033519+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:57.033528+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:57.034569+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:57.034697+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:57.034706+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:57.034885+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:57.034929+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:57.036149+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:57.036263+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:57.036302+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:57.036468+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:57.036518+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:57.037868+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:57.037987+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:57.038064+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:57.038235+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:57.038326+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:57.041824+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:57.041992+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:57.042015+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:57.042541+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:57.043356+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:57.045809+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:57.045931+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:57.045962+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:57.046117+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:57.046169+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:57.047544+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:57.047658+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:57.047693+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:57.047856+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:57.048077+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:57.049109+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:57.049226+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:57.049457+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:57.049499+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:57.049510+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:57.050699+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:57.050820+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:57.050848+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:57.051012+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:57.051069+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:57.052505+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:57.052619+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:57.052648+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:57.052831+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:57.052913+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:57.054017+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:57.054133+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:57.054162+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:57.054325+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:57.054374+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:57.055671+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:57.055793+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:57.055850+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:57.055993+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:57.056041+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:57.057575+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:57.057696+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:57.057729+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:57.660146+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:57.660209+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:57.660906+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:57.660948+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:57.660963+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:57.661052+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:57.661070+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:57.661571+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:57.661607+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:57.661619+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:57.661698+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:57.661714+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:57.662260+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:57.662293+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:57.662311+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:57.662405+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:57.662432+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:57.662856+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:57.662883+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:57.662900+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:57.662964+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:57.662992+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:57.663444+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:57.663474+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:57.663482+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:57.663573+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:57.663584+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:57.664203+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:57.664288+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:57.664320+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:57.664444+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:57.664469+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:57.664930+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:57.664973+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:57.664994+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:57.665091+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:57.665108+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:57.665554+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:57.665587+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:57.665599+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:57.665673+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:57.665697+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:57.666110+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:57.666145+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:57.666162+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:57.666258+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:57.666279+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:57.666815+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:57.666851+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:57.666863+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:57.666955+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:57.666975+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:57.667428+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:57.667457+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:57.667465+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:57.667541+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:57.667581+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:57.668138+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:57.668158+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:57.668190+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:57.668282+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:57.668292+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:57.668751+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:57.668793+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:57.668804+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:57.668884+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:57.668901+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:08:57.669572+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Background task expired while holding WebKit ProcessAssertion (isMainThread=0, remainingTime=-1).
default	11:08:57.669631+0800	hootowl	WKProcessAssertionBackgroundTaskManager: _handleBackgroundTaskExpirationOnMainThread (remainingTime=-1).
default	11:08:57.669662+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: endBackgroundTask
default	11:08:57.669802+0800	hootowl	0x1522cd540 - WKProcessAssertionBackgroundTaskManager: beginBackgroundTaskWithName
default	11:08:57.669837+0800	hootowl	WKProcessAssertionBackgroundTaskManager: Took a FinishTaskInterruptable assertion for own process
default	11:09:24.529205+0800	hootowl	tcp_input [C22.1.1.1:3] flags=[S.E] seq=478320313, ack=3080042469, win=65535 state=SYN_SENT rcv_nxt=0, snd_una=3080042468
default	11:09:24.529252+0800	hootowl	nw_flow_connected [C22.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Transport protocol connected (tcp)
default	11:09:24.529378+0800	hootowl	[C22.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_transport @0.219s
default	11:09:24.529659+0800	hootowl	boringssl_session_apply_protocol_options_for_transport_block_invoke_2(2367) [C22.1.1.1:2][0x14ef774e0] TLS configured [server(0) min_version(0x0303) max_version(0x0304) name(tcgbusfs.blob.core.windows.net) tickets(false) false_start(false) enforce_ev(false) enforce_ats(false) ats_non_pfs_ciphersuite_allowed(false) cc_mode_enforced(false) ech(false) pqtls(true), pake(false) skip_ats_trust(false)]
default	11:09:24.529776+0800	hootowl	boringssl_context_info_handler(2806) [C22.1.1.1:2][0x14ef774e0] Client handshake started
default	11:09:24.529844+0800	hootowl	boringssl_context_info_handler(2823) [C22.1.1.1:2][0x14ef774e0] Client handshake state: TLS client enter_early_data
default	11:09:24.529966+0800	hootowl	boringssl_context_info_handler(2823) [C22.1.1.1:2][0x14ef774e0] Client handshake state: TLS client read_server_hello
default	11:09:24.531920+0800	hootowl	boringssl_context_info_handler(2823) [C23.1.1.1:2][0x14ef77260] Client handshake state: TLS client read_session_ticket
default	11:09:24.531954+0800	hootowl	boringssl_context_info_handler(2823) [C23.1.1.1:2][0x14ef77260] Client handshake state: TLS client process_change_cipher_spec
default	11:09:24.532155+0800	hootowl	boringssl_context_info_handler(2823) [C23.1.1.1:2][0x14ef77260] Client handshake state: TLS client read_server_finished
default	11:09:24.532318+0800	hootowl	boringssl_context_info_handler(2823) [C23.1.1.1:2][0x14ef77260] Client handshake state: TLS client send_client_finished
default	11:09:24.532387+0800	hootowl	boringssl_context_info_handler(2823) [C23.1.1.1:2][0x14ef77260] Client handshake state: TLS client finish_flight
default	11:09:24.532527+0800	hootowl	boringssl_context_info_handler(2823) [C23.1.1.1:2][0x14ef77260] Client handshake state: TLS client finish_client_handshake
default	11:09:24.532552+0800	hootowl	boringssl_context_info_handler(2823) [C23.1.1.1:2][0x14ef77260] Client handshake state: TLS client done
default	11:09:24.532574+0800	hootowl	boringssl_context_info_handler(2812) [C23.1.1.1:2][0x14ef77260] Client handshake done
default	11:09:24.532978+0800	hootowl	nw_protocol_boringssl_signal_connected(895) [C23.1.1.1:2][0x14ef77260] TLS connected [server(0) version(0x0303) ciphersuite(TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256) group(0x0017) signature_alg(0x0401) alpn(nil) resumed(1) offered_ticket(0) in_early_data(0) early_data_accepted(0) false_started(0) ocsp_received(0) sct_received(0) connect_time(127ms) flight_time(125ms) rtt(125ms) write_stalls(0) read_stalls(4) pake(0x0000)]
default	11:09:24.533114+0800	hootowl	nw_flow_connected [C23.1.1.1 61.60.98.243:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (CFNetworkConnection-3170269070)
default	11:09:24.533353+0800	hootowl	[C23.1.1.1 61.60.98.243:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.220s
default	11:09:24.533571+0800	hootowl	[C23.1.1 data.ntpc.gov.tw:443 ready resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.220s
default	11:09:24.533639+0800	hootowl	[C23.1 data.ntpc.gov.tw:443 ready transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.220s
default	11:09:24.533763+0800	hootowl	[C23.1.1.1 61.60.98.243:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.220s
default	11:09:24.533844+0800	hootowl	[C23.1.1 data.ntpc.gov.tw:443 ready resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.220s
default	11:09:24.533906+0800	hootowl	[C23.1 data.ntpc.gov.tw:443 ready transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.220s
default	11:09:24.533967+0800	hootowl	nw_flow_connected [C23 61.60.98.243:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (endpoint_flow)
default	11:09:24.534028+0800	hootowl	[C23 61.60.98.243:443 ready parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_connect @0.220s
default	11:09:24.534162+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C23] reporting state ready
default	11:09:24.534184+0800	hootowl	[C23 61.60.98.243:443 ready parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.220s
default	11:09:24.534204+0800	hootowl	nw_connection_send_viability_changed_on_nw_queue [C23] viability_changed_handler(true)
default	11:09:24.534219+0800	hootowl	Connection 23: connected successfully
default	11:09:24.534231+0800	hootowl	Connection 23: TLS handshake complete
default	11:09:24.534245+0800	hootowl	Connection 23: ready C(N) E(N)
default	11:09:24.534307+0800	hootowl	Task <F679417D-4C7B-4E46-9173-27740DAB937D>.<18> now using Connection 23
default	11:09:24.534364+0800	hootowl	Connection 23: received viability advisory(Y)
default	11:09:24.534379+0800	hootowl	Task <F679417D-4C7B-4E46-9173-27740DAB937D>.<18> sent request, body N 0
default	11:09:25.245964+0800	hootowl	boringssl_context_info_handler(2823) [C22.1.1.1:2][0x14ef774e0] Client handshake state: TLS 1.3 client read_encrypted_extensions
default	11:09:25.246095+0800	hootowl	boringssl_context_info_handler(2823) [C22.1.1.1:2][0x14ef774e0] Client handshake state: TLS 1.3 client read_certificate_request
default	11:09:25.246131+0800	hootowl	boringssl_context_info_handler(2823) [C22.1.1.1:2][0x14ef774e0] Client handshake state: TLS 1.3 client read_server_certificate
default	11:09:25.246153+0800	hootowl	boringssl_context_info_handler(2823) [C22.1.1.1:2][0x14ef774e0] Client handshake state: TLS 1.3 client read_server_certificate_verify
default	11:09:25.246412+0800	hootowl	boringssl_context_evaluate_trust_async(2249) [C22.1.1.1:2][0x14ef774e0] Performing external trust evaluation
default	11:09:25.246475+0800	hootowl	boringssl_context_evaluate_trust_async_external(2234) [C22.1.1.1:2][0x14ef774e0] Asyncing for external verify block
default	11:09:25.246511+0800	hootowl	Task <F679417D-4C7B-4E46-9173-27740DAB937D>.<18> received response, status 200 content C
default	11:09:25.246547+0800	hootowl	Task <F679417D-4C7B-4E46-9173-27740DAB937D>.<18> response ended
default	11:09:25.246557+0800	hootowl	Task <F679417D-4C7B-4E46-9173-27740DAB937D>.<18> done using Connection 23
default	11:09:25.246598+0800	hootowl	Task <F679417D-4C7B-4E46-9173-27740DAB937D>.<18> summary for task success {transaction_duration_ms=413, response_status=200, connection=23, protocol="http/1.1", domain_lookup_duration_ms=55, connect_duration_ms=152, secure_connection_duration_ms=127, private_relay=false, request_start_ms=231, request_duration_ms=0, response_start_ms=412, response_duration_ms=0, request_bytes=391, request_throughput_kbps=32922, response_bytes=21982, response_throughput_kbps=175868, cache_hit=true}
default	11:09:25.246721+0800	hootowl	Connection 22: asked to evaluate TLS Trust
default	11:09:25.246752+0800	hootowl	Task <F679417D-4C7B-4E46-9173-27740DAB937D>.<18> finished successfully
default	11:09:25.246766+0800	hootowl	Mu1Base+Ext 152
newTaipeiCity 📦 minutely Received 20002 bytes
default	11:09:25.246793+0800	hootowl	[C23] event: client:connection_idle @0.404s
default	11:09:25.246840+0800	hootowl	Mu1Base+Ext 175
previousHash updated
default	11:09:25.246905+0800	hootowl	nw_protocol_tcp_notify [C23.1.1.1:3] nw_protocol_notification_type_connection_idle is true
default	11:09:25.246913+0800	hootowl	nw_protocol_tcp_set_connection_idle [C23.1.1.1:3] os_nexus_flow_set_connection_idle returned 0
default	11:09:25.246939+0800	hootowl	[C23] event: client:connection_idle @0.404s
default	11:09:25.246968+0800	hootowl	nw_protocol_tcp_notify [C23.1.1.1:3] nw_protocol_notification_type_connection_idle is true
default	11:09:25.246989+0800	hootowl	nw_protocol_tcp_set_connection_idle [C23.1.1.1:3] os_nexus_flow_set_connection_idle returned 0
default	11:09:25.246998+0800	hootowl	Task <FE784BC1-7BEE-4FD2-8203-443FA6992379>.<17> auth completion disp=1 cred=0x0
default	11:09:25.247028+0800	hootowl	(Trust 0x152221680) No pending evals, starting
default	11:09:25.247082+0800	hootowl	[0x14f9bc640] activating connection: mach=true listener=false peer=false name=com.apple.trustd
default	11:09:25.247106+0800	hootowl	(Trust 0x152221680) Completed async eval kickoff
error	11:09:25.247394+0800	hootowl	73	oParseMinute(data:)	🔴 060105 NOT in feed (source missing)
default	11:09:25.248239+0800	hootowl	MncplCyclopsScreen 166
🦵 uiKick received — syncing items
default	11:09:25.248270+0800	hootowl	Municipal+Cyclops 93
🎨 model refreshed — obs:190s car:7 thread:main 🆔 12708723194660554214
default	11:09:25.248785+0800	hootowl	[C22.1.1 tcgbusfs.blob.core.windows.net:443 ready resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.438s
default	11:09:25.248857+0800	hootowl	[C22.1 tcgbusfs.blob.core.windows.net:443 ready transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.438s
default	11:09:25.249104+0800	hootowl	[C22.1.1.1 20.150.22.100:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.438s
default	11:09:25.249202+0800	hootowl	[C22.1.1 tcgbusfs.blob.core.windows.net:443 ready resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.439s
default	11:09:25.249260+0800	hootowl	[C22.1 tcgbusfs.blob.core.windows.net:443 ready transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.439s
default	11:09:25.249335+0800	hootowl	nw_flow_connected [C22 20.150.22.100:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (endpoint_flow)
default	11:09:25.249356+0800	hootowl	MncplCyclopsScreen 166
🦵 uiKick received — syncing items
default	11:09:25.249366+0800	hootowl	Municipal+Cyclops 93
🎨 model refreshed — obs:190s car:7 thread:main 🆔 12708723194660554214
default	11:09:25.249404+0800	hootowl	[C22 20.150.22.100:443 ready parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_connect @0.440s
default	11:09:25.249634+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C22] reporting state ready
default	11:09:25.249656+0800	hootowl	[C22 20.150.22.100:443 ready parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.440s
default	11:09:25.249677+0800	hootowl	nw_connection_send_viability_changed_on_nw_queue [C22] viability_changed_handler(true)
default	11:09:25.249733+0800	hootowl	[0x14f9bf480] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	11:09:25.249952+0800	hootowl	Connection 22: connected successfully
default	11:09:25.249969+0800	hootowl	Connection 22: TLS handshake complete
default	11:09:25.250010+0800	hootowl	Connection 22: ready C(N) E(N)
default	11:09:25.250104+0800	hootowl	MncplCyclopsScreen 78
🏠 body eval — items:6 firstObs:190s firstCar:7
default	11:09:25.250147+0800	hootowl	Task <FE784BC1-7BEE-4FD2-8203-443FA6992379>.<17> now using Connection 22
default	11:09:25.250247+0800	hootowl	MncplCyclopsScreen 166
🦵 uiKick received — syncing items
default	11:09:25.250262+0800	hootowl	Municipal+Cyclops 93
🎨 model refreshed — obs:0s car:7 thread:main 🆔 12708723194660554214
default	11:09:25.250272+0800	hootowl	MncplCyclopsScreen 78
🏠 body eval — items:6 firstObs:0s firstCar:7
default	11:09:29.294461+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C23] reporting state cancelled
default	11:09:29.294569+0800	hootowl	tcp_output [C23.1.1.1:3] flags=[F.] seq=4027249732, ack=2238630537, win=2048 state=LAST_ACK rcv_nxt=2238630537, snd_una=4027249701
default	11:09:29.323261+0800	hootowl	tcp_close [C23.1.1.1:3] TCP Packets:
	 snd    0.000s seq 4027247705:4027247705 ack 2238608314 win 2070  len 0    [.]
	 snd    0.000s seq 4027247705:4027249145 ack 2238608314 win 2070  len 1440 [.] ECT0
	 snd    0.000s seq 4027249145:4027249230 ack 2238608314 win 2070  len 85   [P.] ECT0
	 snd    0.054s seq 4027247790:4027249230 ack 2238608314 win 2070  len 1440 [P.]
	 rcv    0.072s seq 2238608314:2238608314 ack 4027249230 win 65535 len 0    [.]
	 rcv    0.000s seq 2238608314:2238608465 ack 4027249230 win 16045 len 151  [P.] ECT0
	 snd    0.000s seq 4027249230:4027249230 ack 2238608465 win 2068  len 0    [.]
	 snd    0.001s seq 4027249230:4027249281 ack 2238608465 win 2068  len 51   [P.] ECT0
	 snd    0.002s seq 4027249281:4027249701 ack 2238608465 win 2068  len 420  [P.] ECT0
	 rcv    0.063s seq 2238608465:2238608465 ack 4027249701 win 16516 len 0    [.]
	 rcv    0.001s seq 2238608465:2238608465 ack 4027249701 win 16516 len 0    [.]
	 rcv    0.043s seq 2238609889:2238614374 ack 4027249701 win 16516 len 4485 [.] ECT0
	 snd    0.000s seq 4027249701:4027249701 ack 2238608465 win 2068  len 0    [.]
	 rcv    0.000s seq 2238608465:2238609889 ack 4027249701 win 16516 len 1424 [.] ECT0
	 snd    0.000s seq 4027249701:4027249701 ack 2238614374 win 1976  len 0    [.]
	 rcv    0.000s seq 2238614374:2238615814 ack 4027249701 win 16516 len 1440 [.] ECT0
	 snd    0.000s seq 4027249701:4027249701 ack 2238615814 win 1954  len 0    [.]
	 rcv    0.000s seq 2238616819:2238617793 ack 4027249701 win 16516 len 974  [.] ECT0
	 snd    0.000s seq 4027249701:4027249701 ack 2238615814 win 1954  len 0    [.]
	 rcv    0.000s seq 2238618645:2238621506 ack 4027249701 win 16516 len 2861 [.] ECT0
	 snd    0.000s seq 4027249701:4027249701 ack 2238615814 win 1954  len 0    [.]
	 rcv    0.000s seq 2238615814:2238616819 ack 4027249701 win 16516 len 1005 [.] ECT0
	 snd    0.000s seq 4027249701:4027249701 ack 2238617793 win 1924  len 0    [.]
	 rcv    0.000s seq 2238617793:2238618645 ack 4027249701 win 16516 len 852  [.] ECT0
	 snd    0.000s seq 4027249701:4027249701 ack 2238621506 win 1866  len 0    [.]
	 rcv    0.000s seq 2238621506:2238622946 ack 4027249701 win 16516 len 1440 [P.] ECT0
	 snd    0.000s seq 4027249701:4027249701 ack 2238622946 win 1844  len 0    [.]
	 snd    0.000s seq 4027249701:4027249701 ack 2238622946 win 2048  len 0    [.]
	 rcv    0.068s seq 2238622946:2238624386 ack 4027249701 win 16516 len 1440 [.] ECT0
	 snd    0.000s seq 4027249701:4027249701 ack 2238624386 win 2026  len 0    [.]
	 rcv    0.003s seq 2238624386:2238630536 ack 4027249701 win 16516 len 6150 [P.] ECT0
	 snd    0.000s seq 4027249701:4027249701 ack 2238630536 win 1952  len 0    [.]
	 snd    0.000s seq 4027249701:4027249701 ack 2238630536 win 2048  len 0    [.]
	 rcv    0.792s seq 2238630536:2238630536 ack 4027249701 win 16516 len 0    [.]
	 rcv    4.152s seq 2238630536:2238630537 ack 4027249701 win 16516 len 0    [F.]
	 snd    0.000s seq 4027249701:4027249701 ack 2238630537 win 2048  len 0    [.]
	 snd    0.001s seq 4027249701:4027249732 ack 2238630537 win 2048  len 31   [P.] ECT0
	 snd    0.001s seq 4027249732:4027249733 ack 2238630537 win 2048  len 0    [F.]
	 rcv    0.094s seq 2238630537:2238630537 ack 4027249732 win 16547 len 0    [.]
	 rcv    0.000s seq 2238630537:2238630537 ack 4027249733 win 16547 len 0    [.]
	Last packet 0ms ago.
default	11:09:30.127775+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:09:30.161866+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c6554 posting AVAudioSessionAvailableInputsChangeNotification
default	11:09:30.161885+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:09:30.212614+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:09:30.214911+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c6554 posting AVAudioSessionAvailableInputsChangeNotification
default	11:09:30.214932+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:09:30.230619+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:09:30.305228+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c6554 posting AVAudioSessionAvailableInputsChangeNotification
default	11:09:30.305248+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c6554 posting AVAudioSessionAvailableOutputsChangeNotification
default	11:09:54.400659+0800	hootowl	Connection 22: cleaning up
default	11:09:54.400782+0800	hootowl	[C22 C52153E6-1649-4B00-A76D-B3AE9F65F853 tcgbusfs.blob.core.windows.net:443 quic-connection, url: https://tcgbusfs.blob.core.windows.net/blobtcmsv/TCMSV_allavailable.json, definite, attribution: developer] cancel
default	11:09:54.401218+0800	hootowl	[C22 C52153E6-1649-4B00-A76D-B3AE9F65F853 tcgbusfs.blob.core.windows.net:443 quic-connection, url: https://tcgbusfs.blob.core.windows.net/blobtcmsv/TCMSV_allavailable.json, definite, attribution: developer] cancelled
	[C22.1.1.1 8F29CF17-7D97-438B-A6F2-AB7364BE6DE9 192.168.50.191:56425<->20.150.22.100:443]
	Connected Path: satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good
	Privacy Stance: Not Eligible
	Duration: 30.725s, DNS @0.002s took 0.064s, TCP @0.072s took 0.147s,  took 0.217s
	bytes in/out: 10765/2357, packets in/out: 7/13, rtt: 0.123s, retransmitted bytes: 0, out-of-order bytes: 0
	ecn packets sent/acked/marked/lost: 5/4/0/0
default	11:09:54.402195+0800	hootowl	nw_protocol_tcp_log_summary [C22.1.1.1:3] 
	[49EFAF08-579C-4825-A4A1-D163EB64916D 192.168.50.191:56425<->20.150.22.100:443]
	Init: 1, Conn_Time: 145.880ms, SYNs: 1, WR_T: 0/0, RD_T: 0/0, TFO: 0/0/0, ECN: 0/1/1, Accurate ECN (client/server): Disabled/Disabled, TS: 1, TSO: 0
	rtt_cache: process, rtt_upd: 5, rtt: 123.781ms, rtt_var: 50.312ms rtt_nc: 123.781ms, rtt_var_nc: 50.312ms base rtt: 66ms
	ACKs-compressed: 0, ACKs delayed: 0 delayed ACKs sent: 0
default	11:09:54.403655+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C22] reporting state cancelled
default	11:09:54.403673+0800	hootowl	Connection 22: done
default	11:09:54.403888+0800	hootowl	tcp_output [C22.1.1.1:3] flags=[F.] seq=3080044850, ack=478331079, win=2048 state=FIN_WAIT_1 rcv_nxt=478331079, snd_una=3080044826
default	11:09:54.484882+0800	hootowl	tcp_input [C22.1.1.1:3] flags=[F.] seq=478331079, ack=3080044851, win=16382 state=FIN_WAIT_2 rcv_nxt=478331079, snd_una=3080044851

```