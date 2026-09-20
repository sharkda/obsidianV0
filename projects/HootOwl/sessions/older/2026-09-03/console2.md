```
default	19:29:06.831620+0800	hootowl	tcp_close [C33.1.1.1:3] TCP Packets:
	 snd    0.000s seq 3258446131:3258446132 ack 0          win 65535 len 0    [SEC]
	 rcv    0.071s seq 3991101678:3991101679 ack 3258446132 win 65535 len 0    [S.E] ECT0
	 snd    0.000s seq 3258446132:3258446132 ack 3991101679 win 2053  len 0    [.]
	 snd    0.005s seq 3258446132:3258447560 ack 3991101679 win 2053  len 1428 [.] ECT0
	 snd    0.000s seq 3258447560:3258447671 ack 3991101679 win 2053  len 111  [P.] ECT0
	 rcv    0.099s seq 3991101679:3991101679 ack 3258447671 win 16385 len 0    [.]
	 rcv    0.000s seq 3991101679:3991101778 ack 3258447671 win 16385 len 99   [P.] ECT0
	 snd    0.000s seq 3258447671:3258447671 ack 3991101778 win 2052  len 0    [.]
	 snd    0.004s seq 3258447671:3258448056 ack 3991101778 win 2052  len 385  [P.] ECT0
	 rcv    0.114s seq 3991101778:3991103218 ack 3258448056 win 16384 len 1440 [.] ECT0
	 snd    0.000s seq 3258448056:3258448056 ack 3991103218 win 2030  len 0    [.]
	 rcv    0.004s seq 3991103218:3991112011 ack 3258448056 win 16384 len 8793 [P.] ECT0
	 snd    0.000s seq 3258448056:3258448056 ack 3991112011 win 1911  len 0    [.]
	 snd    0.001s seq 3258448056:3258448056 ack 3991112011 win 2048  len 0    [.]
	 snd    0.033s seq 3258448056:3258448130 ack 3991112011 win 2048  len 74   [P.] ECT0
	 snd    0.003s seq 3258448130:3258448489 ack 3991112011 win 2048  len 359  [P.] ECT0
	 rcv    0.104s seq 3991112011:3991112011 ack 3258448489 win 16382 len 0    [.]
	 rcv    0.003s seq 3991112011:3991112444 ack 3258448489 win 16382 len 433  [P.] ECT0
	 snd    0.000s seq 3258448489:3258448489 ack 3991112444 win 2042  len 0    [.]
	 rcv    0.756s seq 3991112444:3991112444 ack 3258448489 win 16382 len 0    [.]
	 snd   29.632s seq 3258448489:3258448513 ack 3991112444 win 2048  len 24   [P.] ECT0
	 snd    0.001s seq 3258448513:3258448514 ack 3991112444 win 2048  len 0    [F.]
	 rcv    0.139s seq 3991112444:3991112444 ack 3258448514 win 16382 len 0    [.]
	 rcv    0.000s seq 3991112444:3991112445 ack 3258448514 win 16382 len 0    [F.]
	 snd    0.000s seq 3258448514:3258448514 ack 3991112445 win 2048  len 0    [.]
	Last packet 30103ms ago.
default	19:30:06.204617+0800	hootowl	Task <3CD7844B-2A88-4F67-8431-03E55B54D5E7>.<27> resuming, timeouts(60.0, 604800.0) qos(0x15) voucher((null)) activity(00000000-0000-0000-0000-000000000000)
default	19:30:06.210661+0800	hootowl	Connection 0: creating secure tcp or quic connection
default	19:30:06.211117+0800	hootowl	Connection 34: enabling TLS
default	19:30:06.211133+0800	hootowl	Connection 34: starting, TC(0x0)
default	19:30:06.211179+0800	hootowl	[C34 23A0DD6D-C3F0-488D-A769-041AC5328668 tcgbusfs.blob.core.windows.net:443 quic-connection, url: https://tcgbusfs.blob.core.windows.net/blobtcmsv/TCMSV_allavailable.json, definite, attribution: developer, context: com.apple.CFNetwork.NSURLSession.{4EE848AE-A5DC-4E55-A08E-E23FD8E7E021}{(null)}{Y}{2}{0x0} (private), proc: 1B526020-2DE0-3C65-9122-F1177549D69A, delegated upid: 0] start
default	19:30:06.211319+0800	hootowl	[C34 tcgbusfs.blob.core.windows.net:443 initial parent-flow ((null))] event: path:start @0.000s
default	19:30:06.212610+0800	hootowl	[C34 tcgbusfs.blob.core.windows.net:443 waiting parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.001s, uuid: 46644448-81D8-46E0-8442-876FFD28B5E5
default	19:30:06.212738+0800	hootowl	[C34 tcgbusfs.blob.core.windows.net:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_connect @0.001s
default	19:30:06.212752+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C34] reporting state preparing
default	19:30:06.212832+0800	hootowl	[C34 tcgbusfs.blob.core.windows.net:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_child @0.001s
default	19:30:06.213407+0800	hootowl	[C34.1 tcgbusfs.blob.core.windows.net:443 initial path ((null))] event: path:start @0.001s
default	19:30:06.213576+0800	hootowl	[C34.1 tcgbusfs.blob.core.windows.net:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.002s, uuid: 46644448-81D8-46E0-8442-876FFD28B5E5
default	19:30:06.213648+0800	hootowl	[C34.1 tcgbusfs.blob.core.windows.net:443 in_progress transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: transform:start @0.002s
default	19:30:06.213804+0800	hootowl	[C34.1.1 tcgbusfs.blob.core.windows.net:443 initial path ((null))] event: path:start @0.002s
default	19:30:06.214739+0800	hootowl	[C34.1.1 tcgbusfs.blob.core.windows.net:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.003s, uuid: 14207466-1ADB-40E2-9934-AECDB0D27E3F
default	19:30:06.215392+0800	hootowl	[C34.1.1 tcgbusfs.blob.core.windows.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:start_dns @0.003s
default	19:30:06.215691+0800	hootowl	Task <3CD7844B-2A88-4F67-8431-03E55B54D5E7>.<27> setting up Connection 34
default	19:30:06.272886+0800	hootowl	nw_endpoint_resolver_update [C34.1.1 tcgbusfs.blob.core.windows.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Adding endpoint handler for 20.150.22.100:443
default	19:30:06.273530+0800	hootowl	[C34.1.1 tcgbusfs.blob.core.windows.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:receive_dns @0.061s
default	19:30:06.273910+0800	hootowl	[C34.1.1.1 20.150.22.100:443 initial path ((null))] event: path:start @0.062s
default	19:30:06.276808+0800	hootowl	[C34.1.1.1 20.150.22.100:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.064s, uuid: 3BA7B0DD-3DCA-4C0A-819E-A7A671C2DD5D
default	19:30:06.277689+0800	hootowl	[C34.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_nexus @0.065s
default	19:30:06.280425+0800	hootowl	[C34.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:receive_nexus @0.067s
default	19:30:06.282568+0800	hootowl	[C34.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_connect @0.070s
default	19:30:06.283854+0800	hootowl	tcp_output [C34.1.1.1:3] flags=[SEC] seq=3877927640, ack=0, win=65535 state=SYN_SENT rcv_nxt=0, snd_una=3877927640
default	19:30:06.284292+0800	hootowl	[C34.1.1 tcgbusfs.blob.core.windows.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:receive_dns @0.072s
default	19:30:06.356415+0800	hootowl	tcp_input [C34.1.1.1:3] flags=[S.E] seq=1583532237, ack=3877927641, win=65535 state=SYN_SENT rcv_nxt=0, snd_una=3877927640
default	19:30:06.357125+0800	hootowl	nw_flow_connected [C34.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Transport protocol connected (tcp)
default	19:30:06.358056+0800	hootowl	[C34.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_transport @0.145s
default	19:30:06.360764+0800	hootowl	boringssl_session_apply_protocol_options_for_transport_block_invoke_2(2367) [C34.1.1.1:2][0x12c80c7e0] TLS configured [server(0) min_version(0x0303) max_version(0x0304) name(tcgbusfs.blob.core.windows.net) tickets(false) false_start(false) enforce_ev(false) enforce_ats(false) ats_non_pfs_ciphersuite_allowed(false) cc_mode_enforced(false) ech(false) pqtls(true), pake(false) skip_ats_trust(false)]
default	19:30:06.361479+0800	hootowl	boringssl_context_info_handler(2806) [C34.1.1.1:2][0x12c80c7e0] Client handshake started
default	19:30:06.361902+0800	hootowl	boringssl_context_info_handler(2823) [C34.1.1.1:2][0x12c80c7e0] Client handshake state: TLS client enter_early_data
default	19:30:06.362628+0800	hootowl	boringssl_context_info_handler(2823) [C34.1.1.1:2][0x12c80c7e0] Client handshake state: TLS client read_server_hello
default	19:30:06.457928+0800	hootowl	boringssl_context_info_handler(2823) [C34.1.1.1:2][0x12c80c7e0] Client handshake state: TLS 1.3 client read_hello_retry_request
default	19:30:06.460968+0800	hootowl	boringssl_context_info_handler(2823) [C34.1.1.1:2][0x12c80c7e0] Client handshake state: TLS 1.3 client send_second_client_hello
default	19:30:06.461204+0800	hootowl	boringssl_context_info_handler(2823) [C34.1.1.1:2][0x12c80c7e0] Client handshake state: TLS 1.3 client read_server_hello
default	19:30:06.648072+0800	hootowl	boringssl_context_info_handler(2823) [C34.1.1.1:2][0x12c80c7e0] Client handshake state: TLS 1.3 client read_encrypted_extensions
default	19:30:06.648801+0800	hootowl	boringssl_context_info_handler(2823) [C34.1.1.1:2][0x12c80c7e0] Client handshake state: TLS 1.3 client read_certificate_request
default	19:30:06.648865+0800	hootowl	boringssl_context_info_handler(2823) [C34.1.1.1:2][0x12c80c7e0] Client handshake state: TLS 1.3 client read_server_certificate
default	19:30:06.648927+0800	hootowl	boringssl_context_info_handler(2823) [C34.1.1.1:2][0x12c80c7e0] Client handshake state: TLS 1.3 client read_server_certificate_verify
default	19:30:06.649288+0800	hootowl	boringssl_context_evaluate_trust_async(2249) [C34.1.1.1:2][0x12c80c7e0] Performing external trust evaluation
default	19:30:06.649327+0800	hootowl	boringssl_context_evaluate_trust_async_external(2234) [C34.1.1.1:2][0x12c80c7e0] Asyncing for external verify block
default	19:30:06.649648+0800	hootowl	Connection 34: asked to evaluate TLS Trust
default	19:30:06.649919+0800	hootowl	Task <3CD7844B-2A88-4F67-8431-03E55B54D5E7>.<27> auth completion disp=1 cred=0x0
default	19:30:06.650274+0800	hootowl	(Trust 0x13a3406c0) No pending evals, starting
default	19:30:06.651051+0800	hootowl	[0x11ad7fc00] activating connection: mach=true listener=false peer=false name=com.apple.trustd
default	19:30:06.651165+0800	hootowl	(Trust 0x13a3406c0) Completed async eval kickoff
default	19:30:06.661370+0800	hootowl	(Trust 0x13a3406c0) trustd returned 4
default	19:30:06.661484+0800	hootowl	System Trust Evaluation yielded status(0)
default	19:30:06.661555+0800	hootowl	(Trust 0x13a340840) No pending evals, starting
default	19:30:06.661889+0800	hootowl	[0x11ad7dcc0] activating connection: mach=true listener=false peer=false name=com.apple.trustd
default	19:30:06.662139+0800	hootowl	(Trust 0x13a340840) Completed async eval kickoff
default	19:30:06.662525+0800	hootowl	[0x11ad7fc00] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	19:30:06.668845+0800	hootowl	(Trust 0x13a340840) trustd returned 4
default	19:30:06.668939+0800	hootowl	Connection 34: TLS Trust result 0
default	19:30:06.668958+0800	hootowl	boringssl_context_evaluate_trust_async_external_block_invoke_3(2148) [C34.1.1.1:2][0x12c80c7e0] Returning from external verify block with result: true
default	19:30:06.669064+0800	hootowl	boringssl_context_certificate_verify_callback(2430) [C34.1.1.1:2][0x12c80c7e0] Certificate verification result: OK
default	19:30:06.669104+0800	hootowl	boringssl_context_info_handler(2823) [C34.1.1.1:2][0x12c80c7e0] Client handshake state: TLS 1.3 client read_server_finished
default	19:30:06.669188+0800	hootowl	boringssl_context_info_handler(2823) [C34.1.1.1:2][0x12c80c7e0] Client handshake state: TLS 1.3 client send_end_of_early_data
default	19:30:06.669204+0800	hootowl	boringssl_context_info_handler(2823) [C34.1.1.1:2][0x12c80c7e0] Client handshake state: TLS 1.3 client send_client_encrypted_extensions
default	19:30:06.669218+0800	hootowl	boringssl_context_info_handler(2823) [C34.1.1.1:2][0x12c80c7e0] Client handshake state: TLS 1.3 client send_client_certificate
default	19:30:06.669225+0800	hootowl	boringssl_context_info_handler(2823) [C34.1.1.1:2][0x12c80c7e0] Client handshake state: TLS 1.3 client complete_second_flight
default	19:30:06.669379+0800	hootowl	boringssl_context_info_handler(2823) [C34.1.1.1:2][0x12c80c7e0] Client handshake state: TLS 1.3 client done
default	19:30:06.669431+0800	hootowl	boringssl_context_info_handler(2823) [C34.1.1.1:2][0x12c80c7e0] Client handshake state: TLS client finish_client_handshake
default	19:30:06.669440+0800	hootowl	boringssl_context_info_handler(2823) [C34.1.1.1:2][0x12c80c7e0] Client handshake state: TLS client done
default	19:30:06.669449+0800	hootowl	boringssl_context_info_handler(2812) [C34.1.1.1:2][0x12c80c7e0] Client handshake done
default	19:30:06.670059+0800	hootowl	nw_protocol_boringssl_signal_connected(895) [C34.1.1.1:2][0x12c80c7e0] TLS connected [server(0) version(0x0304) ciphersuite(TLS_AES_256_GCM_SHA384) group(0x0018) signature_alg(0x0804) alpn(nil) resumed(0) offered_ticket(0) in_early_data(0) early_data_accepted(0) false_started(0) ocsp_received(1) sct_received(0) connect_time(309ms) flight_time(281ms) rtt(96ms) write_stalls(0) read_stalls(7) pake(0x0000)]
default	19:30:06.670118+0800	hootowl	nw_flow_connected [C34.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (CFNetworkConnection-4160941018)
default	19:30:06.670300+0800	hootowl	[C34.1.1.1 20.150.22.100:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.459s
default	19:30:06.670506+0800	hootowl	[C34.1.1 tcgbusfs.blob.core.windows.net:443 ready resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.459s
default	19:30:06.670598+0800	hootowl	[C34.1 tcgbusfs.blob.core.windows.net:443 ready transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.459s
default	19:30:06.670933+0800	hootowl	[C34.1.1.1 20.150.22.100:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.459s
default	19:30:06.670975+0800	hootowl	[C34.1.1 tcgbusfs.blob.core.windows.net:443 ready resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.459s
default	19:30:06.671004+0800	hootowl	[C34.1 tcgbusfs.blob.core.windows.net:443 ready transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.459s
default	19:30:06.671031+0800	hootowl	nw_flow_connected [C34 20.150.22.100:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (endpoint_flow)
default	19:30:06.671073+0800	hootowl	[C34 20.150.22.100:443 ready parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_connect @0.459s
default	19:30:06.671240+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C34] reporting state ready
default	19:30:06.671260+0800	hootowl	[C34 20.150.22.100:443 ready parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.460s
default	19:30:06.671273+0800	hootowl	nw_connection_send_viability_changed_on_nw_queue [C34] viability_changed_handler(true)
default	19:30:06.671319+0800	hootowl	[0x11ad7dcc0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	19:30:06.671344+0800	hootowl	Connection 34: connected successfully
default	19:30:06.671384+0800	hootowl	Connection 34: TLS handshake complete
default	19:30:06.671478+0800	hootowl	Connection 34: ready C(N) E(N)
default	19:30:06.671597+0800	hootowl	Task <3CD7844B-2A88-4F67-8431-03E55B54D5E7>.<27> now using Connection 34
default	19:30:06.671700+0800	hootowl	Connection 34: received viability advisory(Y)
default	19:30:06.671849+0800	hootowl	Task <3CD7844B-2A88-4F67-8431-03E55B54D5E7>.<27> sent request, body N 0
default	19:30:06.778764+0800	hootowl	Task <3CD7844B-2A88-4F67-8431-03E55B54D5E7>.<27> received response, status 304 content K
default	19:30:06.779535+0800	hootowl	Task <3CD7844B-2A88-4F67-8431-03E55B54D5E7>.<27> done using Connection 34
default	19:30:06.779963+0800	hootowl	[C34] event: client:connection_idle @0.567s
default	19:30:06.780128+0800	hootowl	nw_protocol_tcp_notify [C34.1.1.1:3] nw_protocol_notification_type_connection_idle is true
default	19:30:06.780246+0800	hootowl	nw_protocol_tcp_set_connection_idle [C34.1.1.1:3] os_nexus_flow_set_connection_idle returned 0
default	19:30:06.780330+0800	hootowl	Task <3CD7844B-2A88-4F67-8431-03E55B54D5E7>.<27> summary for task success {transaction_duration_ms=574, response_status=304, connection=34, protocol="http/1.1", domain_lookup_duration_ms=58, connect_duration_ms=389, secure_connection_duration_ms=309, private_relay=false, request_start_ms=466, request_duration_ms=0, response_start_ms=573, response_duration_ms=0, request_bytes=337, request_throughput_kbps=28376, response_bytes=308, response_throughput_kbps=5415, cache_hit=true}
default	19:30:06.781920+0800	hootowl	[C34] event: client:connection_idle @0.568s
default	19:30:06.783107+0800	hootowl	nw_protocol_tcp_notify [C34.1.1.1:3] nw_protocol_notification_type_connection_idle is true
default	19:30:06.783155+0800	hootowl	Task <3CD7844B-2A88-4F67-8431-03E55B54D5E7>.<27> finished successfully
default	19:30:06.784089+0800	hootowl	nw_protocol_tcp_set_connection_idle [C34.1.1.1:3] os_nexus_flow_set_connection_idle returned 0
default	19:30:06.785110+0800	hootowl	Mu1Base+Ext 152
taipei 📦 minutely Received 460036 bytes
default	19:30:06.785164+0800	hootowl	Mu1Base+Ext 177
previousHash not changed
default	19:30:06.792093+0800	hootowl	Municipal+Cyclops 93
🎨 model refreshed — obs:0s car:19 thread:main
default	19:30:37.165513+0800	hootowl	Connection 34: cleaning up
default	19:30:37.165862+0800	hootowl	[C34 23A0DD6D-C3F0-488D-A769-041AC5328668 tcgbusfs.blob.core.windows.net:443 quic-connection, url: https://tcgbusfs.blob.core.windows.net/blobtcmsv/TCMSV_allavailable.json, definite, attribution: developer] cancel
default	19:30:37.166040+0800	hootowl	[C34 23A0DD6D-C3F0-488D-A769-041AC5328668 tcgbusfs.blob.core.windows.net:443 quic-connection, url: https://tcgbusfs.blob.core.windows.net/blobtcmsv/TCMSV_allavailable.json, definite, attribution: developer] cancelled
	[C34.1.1.1 3BA7B0DD-3DCA-4C0A-819E-A7A671C2DD5D 192.168.50.191:56019<->20.150.22.100:443]
	Connected Path: satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good
	Privacy Stance: Not Eligible
	Duration: 30.954s, DNS @0.003s took 0.058s, TCP @0.070s took 0.075s,  took 0.309s
	bytes in/out: 12205/2357, packets in/out: 8/13, rtt: 0.091s, retransmitted bytes: 0, out-of-order bytes: 0
	ecn packets sent/acked/marked/lost: 5/3/0/0
default	19:30:37.166265+0800	hootowl	nw_protocol_tcp_log_summary [C34.1.1.1:3] 
	[EC0F2441-74C4-4868-90ED-B93438226065 192.168.50.191:56019<->20.150.22.100:443]
	Init: 1, Conn_Time: 73.217ms, SYNs: 1, WR_T: 0/0, RD_T: 0/0, TFO: 0/0/0, ECN: 0/1/1, Accurate ECN (client/server): Disabled/Disabled, TS: 1, TSO: 0
	rtt_cache: process, rtt_upd: 4, rtt: 91.500ms, rtt_var: 43.562ms rtt_nc: 91.500ms, rtt_var_nc: 43.562ms base rtt: 63ms
	ACKs-compressed: 0, ACKs delayed: 0 delayed ACKs sent: 0
default	19:30:37.166620+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C34] reporting state cancelled
default	19:30:37.166630+0800	hootowl	Connection 34: done
default	19:30:37.166850+0800	hootowl	tcp_output [C34.1.1.1:3] flags=[F.] seq=3877930022, ack=1583543003, win=2048 state=FIN_WAIT_1 rcv_nxt=1583543003, snd_una=3877929998
default	19:30:37.286216+0800	hootowl	tcp_input [C34.1.1.1:3] flags=[F.] seq=1583543003, ack=3877930023, win=16382 state=FIN_WAIT_2 rcv_nxt=1583543003, snd_una=3877930023
default	19:31:07.384063+0800	hootowl	tcp_close [C34.1.1.1:3] TCP Packets:
	 snd    0.000s seq 3877927640:3877927641 ack 0          win 65535 len 0    [SEC]
	 rcv    0.073s seq 1583532237:1583532238 ack 3877927641 win 65535 len 0    [S.E] ECT0
	 snd    0.000s seq 3877927641:3877927641 ack 1583532238 win 2053  len 0    [.]
	 snd    0.006s seq 3877927641:3877929069 ack 1583532238 win 2053  len 1428 [.] ECT0
	 snd    0.000s seq 3877929069:3877929180 ack 1583532238 win 2053  len 111  [P.] ECT0
	 rcv    0.092s seq 1583532238:1583532238 ack 3877929180 win 16385 len 0    [.]
	 rcv    0.004s seq 1583532238:1583532337 ack 3877929180 win 16385 len 99   [P.] ECT0
	 snd    0.000s seq 3877929180:3877929180 ack 1583532337 win 2052  len 0    [.]
	 snd    0.003s seq 3877929180:3877929565 ack 1583532337 win 2052  len 385  [P.] ECT0
	 rcv    0.184s seq 1583532337:1583542570 ack 3877929565 win 16384 len 10233 [P.] ECT0
	 snd    0.000s seq 3877929565:3877929565 ack 1583542570 win 1893  len 0    [.]
	 snd    0.000s seq 3877929565:3877929565 ack 1583542570 win 2048  len 0    [.]
	 snd    0.024s seq 3877929565:3877929639 ack 1583542570 win 2048  len 74   [P.] ECT0
	 snd    0.003s seq 3877929639:3877929998 ack 1583542570 win 2048  len 359  [P.] ECT0
	 rcv    0.106s seq 1583541130:1583542570 ack 3877929565 win 16384 len 1440 [P.]
	 snd    0.000s seq 3877929998:3877929998 ack 1583542570 win 2048  len 0    [.]
	 rcv    0.000s seq 1583542570:1583542570 ack 3877929998 win 16382 len 0    [.]
	 rcv    0.000s seq 1583542570:1583543003 ack 3877929998 win 16382 len 433  [P.] ECT0
	 snd    0.000s seq 3877929998:3877929998 ack 1583543003 win 2042  len 0    [.]
	 rcv    1.065s seq 1583543003:1583543003 ack 3877929998 win 16382 len 0    [.]
	 snd   29.312s seq 3877929998:3877930022 ack 1583543003 win 2048  len 24   [P.] ECT0
	 snd    0.001s seq 3877930022:3877930023 ack 1583543003 win 2048  len 0    [F.]
	 rcv    0.119s seq 1583543003:1583543003 ack 3877930023 win 16382 len 0    [.]
	 rcv    0.000s seq 1583543003:1583543004 ack 3877930023 win 16382 len 0    [F.]
	 snd    0.000s seq 3877930023:3877930023 ack 1583543004 win 2048  len 0    [.]
	Last packet 30097ms ago.
default	19:32:06.879575+0800	hootowl	Task <E93AA86D-BF3F-4F68-B469-0C601F66C8CD>.<28> resuming, timeouts(60.0, 604800.0) qos(0x15) voucher((null)) activity(00000000-0000-0000-0000-000000000000)
default	19:32:06.880296+0800	hootowl	Connection 0: creating secure tcp or quic connection
default	19:32:06.880534+0800	hootowl	Connection 35: enabling TLS
default	19:32:06.880562+0800	hootowl	Connection 35: starting, TC(0x0)
default	19:32:06.880579+0800	hootowl	[C35 3A8630AC-074B-46BF-A48C-F0B8299835B2 tcgbusfs.blob.core.windows.net:443 quic-connection, url: https://tcgbusfs.blob.core.windows.net/blobtcmsv/TCMSV_allavailable.json, definite, attribution: developer, context: com.apple.CFNetwork.NSURLSession.{4EE848AE-A5DC-4E55-A08E-E23FD8E7E021}{(null)}{Y}{2}{0x0} (private), proc: 1B526020-2DE0-3C65-9122-F1177549D69A, delegated upid: 0] start
default	19:32:06.880609+0800	hootowl	[C35 tcgbusfs.blob.core.windows.net:443 initial parent-flow ((null))] event: path:start @0.000s
default	19:32:06.880747+0800	hootowl	[C35 tcgbusfs.blob.core.windows.net:443 waiting parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.001s, uuid: 7EBB463A-3A65-4544-946E-62434802242A
default	19:32:06.880814+0800	hootowl	[C35 tcgbusfs.blob.core.windows.net:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_connect @0.001s
default	19:32:06.880821+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C35] reporting state preparing
default	19:32:06.880856+0800	hootowl	[C35 tcgbusfs.blob.core.windows.net:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_child @0.001s
default	19:32:06.880894+0800	hootowl	[C35.1 tcgbusfs.blob.core.windows.net:443 initial path ((null))] event: path:start @0.001s
default	19:32:06.880976+0800	hootowl	[C35.1 tcgbusfs.blob.core.windows.net:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.001s, uuid: 7EBB463A-3A65-4544-946E-62434802242A
default	19:32:06.881007+0800	hootowl	[C35.1 tcgbusfs.blob.core.windows.net:443 in_progress transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: transform:start @0.001s
default	19:32:06.881055+0800	hootowl	[C35.1.1 tcgbusfs.blob.core.windows.net:443 initial path ((null))] event: path:start @0.001s
default	19:32:06.881165+0800	hootowl	[C35.1.1 tcgbusfs.blob.core.windows.net:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.002s, uuid: 3F83EAAA-3B4B-4195-850A-F0322D302861
default	19:32:06.881222+0800	hootowl	[C35.1.1 tcgbusfs.blob.core.windows.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:start_dns @0.002s
default	19:32:06.881493+0800	hootowl	Task <E93AA86D-BF3F-4F68-B469-0C601F66C8CD>.<28> setting up Connection 35
default	19:32:06.943788+0800	hootowl	nw_endpoint_resolver_update [C35.1.1 tcgbusfs.blob.core.windows.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Adding endpoint handler for 20.150.22.100:443
default	19:32:06.943888+0800	hootowl	[C35.1.1 tcgbusfs.blob.core.windows.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:receive_dns @0.054s
default	19:32:06.944144+0800	hootowl	[C35.1.1.1 20.150.22.100:443 initial path ((null))] event: path:start @0.054s
default	19:32:06.944428+0800	hootowl	[C35.1.1.1 20.150.22.100:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.056s, uuid: BC7C1F26-67B2-4068-8E38-4C3B9F80EDBB
default	19:32:06.944565+0800	hootowl	[C35.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_nexus @0.057s
default	19:32:06.944824+0800	hootowl	[C35.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:receive_nexus @0.058s
default	19:32:06.945095+0800	hootowl	[C35.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_connect @0.059s
default	19:32:06.945280+0800	hootowl	tcp_output [C35.1.1.1:3] flags=[SEC] seq=3711245382, ack=0, win=65535 state=SYN_SENT rcv_nxt=0, snd_una=3711245382
default	19:32:07.037851+0800	hootowl	tcp_input [C35.1.1.1:3] flags=[S.E] seq=1925793438, ack=3711245383, win=65535 state=SYN_SENT rcv_nxt=0, snd_una=3711245382
default	19:32:07.037879+0800	hootowl	nw_flow_connected [C35.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Transport protocol connected (tcp)
default	19:32:07.037952+0800	hootowl	[C35.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_transport @0.159s
default	19:32:07.038121+0800	hootowl	boringssl_session_apply_protocol_options_for_transport_block_invoke_2(2367) [C35.1.1.1:2][0x12c80c7e0] TLS configured [server(0) min_version(0x0303) max_version(0x0304) name(tcgbusfs.blob.core.windows.net) tickets(false) false_start(false) enforce_ev(false) enforce_ats(false) ats_non_pfs_ciphersuite_allowed(false) cc_mode_enforced(false) ech(false) pqtls(true), pake(false) skip_ats_trust(false)]
default	19:32:07.038247+0800	hootowl	boringssl_context_info_handler(2806) [C35.1.1.1:2][0x12c80c7e0] Client handshake started
default	19:32:07.038305+0800	hootowl	boringssl_context_info_handler(2823) [C35.1.1.1:2][0x12c80c7e0] Client handshake state: TLS client enter_early_data
default	19:32:07.038357+0800	hootowl	boringssl_context_info_handler(2823) [C35.1.1.1:2][0x12c80c7e0] Client handshake state: TLS client read_server_hello
default	19:32:07.389636+0800	hootowl	boringssl_context_info_handler(2823) [C35.1.1.1:2][0x12c80c7e0] Client handshake state: TLS 1.3 client read_encrypted_extensions
default	19:32:07.389847+0800	hootowl	boringssl_context_info_handler(2823) [C35.1.1.1:2][0x12c80c7e0] Client handshake state: TLS 1.3 client read_certificate_request
default	19:32:07.389868+0800	hootowl	boringssl_context_info_handler(2823) [C35.1.1.1:2][0x12c80c7e0] Client handshake state: TLS 1.3 client read_server_certificate
default	19:32:07.389877+0800	hootowl	boringssl_context_info_handler(2823) [C35.1.1.1:2][0x12c80c7e0] Client handshake state: TLS 1.3 client read_server_certificate_verify
default	19:32:07.390523+0800	hootowl	boringssl_context_evaluate_trust_async(2249) [C35.1.1.1:2][0x12c80c7e0] Performing external trust evaluation
default	19:32:07.390549+0800	hootowl	boringssl_context_evaluate_trust_async_external(2234) [C35.1.1.1:2][0x12c80c7e0] Asyncing for external verify block
default	19:32:07.390583+0800	hootowl	Connection 35: asked to evaluate TLS Trust
default	19:32:07.390603+0800	hootowl	Task <E93AA86D-BF3F-4F68-B469-0C601F66C8CD>.<28> auth completion disp=1 cred=0x0
default	19:32:07.390619+0800	hootowl	(Trust 0x13a3406c0) No pending evals, starting
default	19:32:07.390667+0800	hootowl	[0x11ad7dcc0] activating connection: mach=true listener=false peer=false name=com.apple.trustd
default	19:32:07.390680+0800	hootowl	(Trust 0x13a3406c0) Completed async eval kickoff
default	19:32:07.392488+0800	hootowl	(Trust 0x13a3406c0) trustd returned 4
default	19:32:07.392549+0800	hootowl	System Trust Evaluation yielded status(0)
default	19:32:07.392589+0800	hootowl	(Trust 0x13a340e40) No pending evals, starting
default	19:32:07.392662+0800	hootowl	[0x11ad7fc00] activating connection: mach=true listener=false peer=false name=com.apple.trustd
default	19:32:07.392676+0800	hootowl	(Trust 0x13a340e40) Completed async eval kickoff
default	19:32:07.392708+0800	hootowl	[0x11ad7dcc0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	19:32:07.394449+0800	hootowl	(Trust 0x13a340e40) trustd returned 4
default	19:32:07.394572+0800	hootowl	Connection 35: TLS Trust result 0
default	19:32:07.394598+0800	hootowl	boringssl_context_evaluate_trust_async_external_block_invoke_3(2148) [C35.1.1.1:2][0x12c80c7e0] Returning from external verify block with result: true
default	19:32:07.394646+0800	hootowl	boringssl_context_certificate_verify_callback(2430) [C35.1.1.1:2][0x12c80c7e0] Certificate verification result: OK
default	19:32:07.394673+0800	hootowl	boringssl_context_info_handler(2823) [C35.1.1.1:2][0x12c80c7e0] Client handshake state: TLS 1.3 client read_server_finished
default	19:32:07.394727+0800	hootowl	boringssl_context_info_handler(2823) [C35.1.1.1:2][0x12c80c7e0] Client handshake state: TLS 1.3 client send_end_of_early_data
default	19:32:07.394747+0800	hootowl	boringssl_context_info_handler(2823) [C35.1.1.1:2][0x12c80c7e0] Client handshake state: TLS 1.3 client send_client_encrypted_extensions
default	19:32:07.394761+0800	hootowl	boringssl_context_info_handler(2823) [C35.1.1.1:2][0x12c80c7e0] Client handshake state: TLS 1.3 client send_client_certificate
default	19:32:07.394774+0800	hootowl	boringssl_context_info_handler(2823) [C35.1.1.1:2][0x12c80c7e0] Client handshake state: TLS 1.3 client complete_second_flight
default	19:32:07.515412+0800	hootowl	boringssl_context_info_handler(2823) [C35.1.1.1:2][0x12c80c7e0] Client handshake state: TLS 1.3 client done
default	19:32:07.515562+0800	hootowl	boringssl_context_info_handler(2823) [C35.1.1.1:2][0x12c80c7e0] Client handshake state: TLS client finish_client_handshake
default	19:32:07.515580+0800	hootowl	boringssl_context_info_handler(2823) [C35.1.1.1:2][0x12c80c7e0] Client handshake state: TLS client done
default	19:32:07.515599+0800	hootowl	boringssl_context_info_handler(2812) [C35.1.1.1:2][0x12c80c7e0] Client handshake done
default	19:32:07.515958+0800	hootowl	nw_protocol_boringssl_signal_connected(895) [C35.1.1.1:2][0x12c80c7e0] TLS connected [server(0) version(0x0304) ciphersuite(TLS_AES_256_GCM_SHA384) group(0x0018) signature_alg(0x0804) alpn(nil) resumed(0) offered_ticket(0) in_early_data(0) early_data_accepted(0) false_started(0) ocsp_received(1) sct_received(0) connect_time(327ms) flight_time(285ms) rtt(112ms) write_stalls(0) read_stalls(10) pake(0x0000)]
default	19:32:07.516177+0800	hootowl	nw_flow_connected [C35.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (CFNetworkConnection-4160941018)
default	19:32:07.516330+0800	hootowl	[C35.1.1.1 20.150.22.100:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.488s
default	19:32:07.516499+0800	hootowl	[C35.1.1 tcgbusfs.blob.core.windows.net:443 ready resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.488s
default	19:32:07.516541+0800	hootowl	[C35.1 tcgbusfs.blob.core.windows.net:443 ready transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.488s
default	19:32:07.516679+0800	hootowl	[C35.1.1.1 20.150.22.100:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.489s
default	19:32:07.516783+0800	hootowl	[C35.1.1 tcgbusfs.blob.core.windows.net:443 ready resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.489s
default	19:32:07.516902+0800	hootowl	[C35.1 tcgbusfs.blob.core.windows.net:443 ready transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.489s
default	19:32:07.516971+0800	hootowl	nw_flow_connected [C35 20.150.22.100:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (endpoint_flow)
default	19:32:07.517030+0800	hootowl	[C35 20.150.22.100:443 ready parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_connect @0.489s
default	19:32:07.517390+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C35] reporting state ready
default	19:32:07.517411+0800	hootowl	[C35 20.150.22.100:443 ready parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.490s
default	19:32:07.517438+0800	hootowl	nw_connection_send_viability_changed_on_nw_queue [C35] viability_changed_handler(true)
default	19:32:07.517472+0800	hootowl	[0x11ad7fc00] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	19:32:07.517486+0800	hootowl	Connection 35: connected successfully
default	19:32:07.517498+0800	hootowl	Connection 35: TLS handshake complete
default	19:32:07.517512+0800	hootowl	Connection 35: ready C(N) E(N)
default	19:32:07.517543+0800	hootowl	Task <E93AA86D-BF3F-4F68-B469-0C601F66C8CD>.<28> now using Connection 35
default	19:32:07.517558+0800	hootowl	Connection 35: received viability advisory(Y)
default	19:32:07.517625+0800	hootowl	Task <E93AA86D-BF3F-4F68-B469-0C601F66C8CD>.<28> sent request, body N 0
default	19:32:07.605127+0800	hootowl	Task <E93AA86D-BF3F-4F68-B469-0C601F66C8CD>.<28> received response, status 200 content K
default	19:32:07.966820+0800	hootowl	Task <E93AA86D-BF3F-4F68-B469-0C601F66C8CD>.<28> response ended
default	19:32:07.966842+0800	hootowl	Task <E93AA86D-BF3F-4F68-B469-0C601F66C8CD>.<28> done using Connection 35
default	19:32:07.967070+0800	hootowl	[C35] event: client:connection_idle @1.168s
default	19:32:07.967099+0800	hootowl	nw_protocol_tcp_notify [C35.1.1.1:3] nw_protocol_notification_type_connection_idle is true
default	19:32:07.967140+0800	hootowl	nw_protocol_tcp_set_connection_idle [C35.1.1.1:3] os_nexus_flow_set_connection_idle returned 0
default	19:32:07.967175+0800	hootowl	Task <E93AA86D-BF3F-4F68-B469-0C601F66C8CD>.<28> summary for task success {transaction_duration_ms=1172, response_status=200, connection=35, protocol="http/1.1", domain_lookup_duration_ms=52, connect_duration_ms=430, secure_connection_duration_ms=327, private_relay=false, request_start_ms=494, request_duration_ms=0, response_start_ms=636, response_duration_ms=535, request_bytes=337, request_throughput_kbps=36953, response_bytes=460489, response_throughput_kbps=6874, cache_hit=true}
default	19:32:07.967207+0800	hootowl	[C35] event: client:connection_idle @1.168s
default	19:32:07.967261+0800	hootowl	nw_protocol_tcp_notify [C35.1.1.1:3] nw_protocol_notification_type_connection_idle is true
default	19:32:07.967406+0800	hootowl	nw_protocol_tcp_set_connection_idle [C35.1.1.1:3] os_nexus_flow_set_connection_idle returned 0
default	19:32:07.967478+0800	hootowl	Task <E93AA86D-BF3F-4F68-B469-0C601F66C8CD>.<28> finished successfully
default	19:32:07.967585+0800	hootowl	Mu1Base+Ext 152
taipei 📦 minutely Received 460036 bytes
default	19:32:07.968151+0800	hootowl	Mu1Base+Ext 175
previousHash updated
error	19:32:07.993978+0800	hootowl	333	wireAvailableUpdateFromMunicipal()	⚠️ duplicate parkIds in avail feed (11): 040014(綠寶石區, ?), 040037(綠光河岸區, ?), 040068(玉清宮, ?), 060021(陽光運動公園, ?), 060047(親情河濱公園1區, ?), 060068(萊茵區, ?), 060079(城市車旅新店安德二, ?), 060085(親情河濱公園2區, ?), 060085(親情河濱公園2區, ?), 170120(MITSUI OUTLET PARK 林口二館收費, ?), 170120(MITSUI OUTLET PARK 林口二館收費, ?)
default	19:32:08.012897+0800	hootowl	Municipal+Cyclops 93
🎨 model refreshed — obs:0s car:18 thread:main
default	19:32:08.012955+0800	hootowl	Municipal 130
🐎 minutelyAvailable ["newTaipeiCity ⏳03 19:17 ∑1429", "taipei ⏳03 19:32 ∑1113"]
default	19:32:08.030126+0800	hootowl	Municipal+Cyclops 93
🎨 model refreshed — obs:0s car:18 thread:main
default	19:32:38.007864+0800	hootowl	Connection 35: cleaning up
default	19:32:38.010598+0800	hootowl	[C35 3A8630AC-074B-46BF-A48C-F0B8299835B2 tcgbusfs.blob.core.windows.net:443 quic-connection, url: https://tcgbusfs.blob.core.windows.net/blobtcmsv/TCMSV_allavailable.json, definite, attribution: developer] cancel
default	19:32:38.010782+0800	hootowl	[C35 3A8630AC-074B-46BF-A48C-F0B8299835B2 tcgbusfs.blob.core.windows.net:443 quic-connection, url: https://tcgbusfs.blob.core.windows.net/blobtcmsv/TCMSV_allavailable.json, definite, attribution: developer] cancelled
	[C35.1.1.1 BC7C1F26-67B2-4068-8E38-4C3B9F80EDBB 192.168.50.191:56020<->20.150.22.100:443]
	Connected Path: satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good
	Privacy Stance: Not Eligible
	Duration: 31.207s, DNS @0.002s took 0.052s, TCP @0.059s took 0.100s,  took 0.327s
	bytes in/out: 471562/2357, packets in/out: 85/98, rtt: 0.110s, retransmitted bytes: 0, out-of-order bytes: 162720
	ecn packets sent/acked/marked/lost: 5/3/0/0
default	19:32:38.012789+0800	hootowl	nw_protocol_tcp_log_summary [C35.1.1.1:3] 
	[634C3A18-1305-423D-9561-BA21CC6EF862 192.168.50.191:56020<->20.150.22.100:443]
	Init: 1, Conn_Time: 99.592ms, SYNs: 1, WR_T: 0/0, RD_T: 0/0, TFO: 0/0/0, ECN: 0/1/1, Accurate ECN (client/server): Disabled/Disabled, TS: 1, TSO: 0
	rtt_cache: process, rtt_upd: 4, rtt: 110.187ms, rtt_var: 45.812ms rtt_nc: 110.187ms, rtt_var_nc: 45.812ms base rtt: 65ms
	ACKs-compressed: 11, ACKs delayed: 17 delayed ACKs sent: 0
default	19:32:38.016247+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C35] reporting state cancelled
default	19:32:38.016305+0800	hootowl	Connection 35: done
default	19:32:38.017661+0800	hootowl	tcp_output [C35.1.1.1:3] flags=[F.] seq=3711247764, ack=1926265001, win=7180 state=FIN_WAIT_1 rcv_nxt=1926265001, snd_una=3711247740
default	19:32:38.094125+0800	hootowl	tcp_input [C35.1.1.1:3] flags=[F.] seq=1926265001, ack=3711247765, win=16382 state=FIN_WAIT_2 rcv_nxt=1926265001, snd_una=3711247765
default	19:33:06.761990+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c63b5 posting AVAudioSessionAvailableOutputsChangeNotification
default	19:33:06.778139+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c63b5 posting AVAudioSessionAvailableInputsChangeNotification
default	19:33:06.778224+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c63b5 posting AVAudioSessionAvailableOutputsChangeNotification
default	19:33:06.824533+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c63b5 posting AVAudioSessionAvailableOutputsChangeNotification
default	19:33:06.842190+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c63b5 posting AVAudioSessionAvailableInputsChangeNotification
default	19:33:06.842305+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c63b5 posting AVAudioSessionAvailableOutputsChangeNotification
default	19:33:06.860394+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c63b5 posting AVAudioSessionAvailableOutputsChangeNotification
default	19:33:06.868990+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c63b5 posting AVAudioSessionAvailableInputsChangeNotification
default	19:33:06.869048+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c63b5 posting AVAudioSessionAvailableOutputsChangeNotification
default	19:33:06.969508+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c63b5 posting AVAudioSessionAvailableOutputsChangeNotification
default	19:33:07.080806+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c63b5 posting AVAudioSessionAvailableInputsChangeNotification
default	19:33:07.080868+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c63b5 posting AVAudioSessionAvailableOutputsChangeNotification
default	19:33:07.902029+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c63b5 posting AVAudioSessionAvailableOutputsChangeNotification
default	19:33:07.906400+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c63b5 posting AVAudioSessionAvailableOutputsChangeNotification
default	19:33:08.000622+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c63b5 posting AVAudioSessionAvailableInputsChangeNotification
default	19:33:08.000649+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c63b5 posting AVAudioSessionAvailableOutputsChangeNotification
default	19:33:08.308038+0800	hootowl	tcp_close [C35.1.1.1:3] TCP Packets:
	 rcv    0.000s seq 1926065954:1926068834 ack 3711247740 win 16382 len 2880 [P.]
	 snd    0.000s seq 3711247740:3711247740 ack 1926068834 win 7135  len 0    [.]
	 snd    0.000s seq 3711247740:3711247740 ack 1926068834 win 7180  len 0    [.]
	 rcv    0.001s seq 1926068834:1926073154 ack 3711247740 win 16382 len 4320 [.]
	 snd    0.000s seq 3711247740:3711247740 ack 1926073154 win 7113  len 0    [.]
	 snd    0.000s seq 3711247740:3711247740 ack 1926073154 win 7180  len 0    [.]
	 rcv    0.000s seq 1926073154:1926076034 ack 3711247740 win 16382 len 2880 [.]
	 snd    0.000s seq 3711247740:3711247740 ack 1926076034 win 7135  len 0    [.]
	 snd    0.000s seq 3711247740:3711247740 ack 1926076034 win 7180  len 0    [.]
	 rcv    0.000s seq 1926076034:1926080354 ack 3711247740 win 16382 len 4320 [.]
	 snd    0.000s seq 3711247740:3711247740 ack 1926080354 win 7113  len 0    [.]
	 snd    0.000s seq 3711247740:3711247740 ack 1926080354 win 7180  len 0    [.]
	 rcv    0.000s seq 1926080354:1926087554 ack 3711247740 win 16382 len 7200 [.]
	 snd    0.000s seq 3711247740:3711247740 ack 1926087554 win 7068  len 0    [.]
	 snd    0.000s seq 3711247740:3711247740 ack 1926087554 win 7180  len 0    [.]
	 rcv    0.000s seq 1926087554:1926090434 ack 3711247740 win 16382 len 2880 [.]
	 snd    0.000s seq 3711247740:3711247740 ack 1926090434 win 7135  len 0    [.]
	 snd    0.000s seq 3711247740:3711247740 ack 1926090434 win 7180  len 0    [.]
	 rcv    0.001s seq 1926090434:1926093314 ack 3711247740 win 16382 len 2880 [.]
	 snd    0.000s seq 3711247740:3711247740 ack 1926093314 win 7135  len 0    [.]
	 snd    0.000s seq 3711247740:3711247740 ack 1926093314 win 7180  len 0    [.]
	 rcv    0.000s seq 1926093314:1926094754 ack 3711247740 win 16382 len 1440 [.]
	 snd    0.000s seq 3711247740:3711247740 ack 1926094754 win 7158  len 0    [.]
	 rcv    0.000s seq 1926094754:1926097634 ack 3711247740 win 16382 len 2880 [.]
	 snd    0.000s seq 3711247740:3711247740 ack 1926260354 win 4593  len 0    [.]
	 rcv    0.000s seq 1926260354:1926261794 ack 3711247740 win 16382 len 1440 [.C] ECT0
	 snd    0.000s seq 3711247740:3711247740 ack 1926261794 win 4571  len 0    [.]
	 snd    0.000s seq 3711247740:3711247740 ack 1926261794 win 7180  len 0    [.]
	 rcv    0.013s seq 1926261794:1926263234 ack 3711247740 win 16382 len 1440 [.] ECT0
	 snd    0.000s seq 3711247740:3711247740 ack 1926263234 win 7158  len 0    [.]
	 rcv    0.002s seq 1926263234:1926264674 ack 3711247740 win 16382 len 1440 [.] ECT0
	 snd    0.000s seq 3711247740:3711247740 ack 1926264674 win 7158  len 0    [.]
	 rcv    0.052s seq 1926264674:1926265001 ack 3711247740 win 16382 len 327  [P.] ECT0
	 snd    0.000s seq 3711247740:3711247740 ack 1926265001 win 7175  len 0    [.]
	 rcv    1.135s seq 1926265001:1926265001 ack 3711247740 win 16382 len 0    [.]
	 snd   28.896s seq 3711247740:3711247764 ack 1926265001 win 7180  len 24   [P.] ECT0
	 snd    0.004s seq 3711247764:3711247765 ack 1926265001 win 7180  len 0    [F.]
	 rcv    0.080s seq 1926265001:1926265001 ack 3711247765 win 16382 len 0    [.]
	 rcv    0.000s seq 1926265001:1926265002 ack 3711247765 win 16382 len 0    [F.]
	 snd    0.000s seq 3711247765:3711247765 ack 1926265002 win 7180  len 0    [.]
	Last packet 30106ms ago.
default	19:33:11.032685+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c63b5 posting AVAudioSessionAvailableOutputsChangeNotification
default	19:33:11.057379+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c63b5 posting AVAudioSessionAvailableInputsChangeNotification
default	19:33:11.057460+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c63b5 posting AVAudioSessionAvailableOutputsChangeNotification
default	19:33:11.109708+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c63b5 posting AVAudioSessionAvailableOutputsChangeNotification
default	19:33:11.129334+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c63b5 posting AVAudioSessionAvailableInputsChangeNotification
default	19:33:11.129378+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c63b5 posting AVAudioSessionAvailableOutputsChangeNotification
default	19:33:11.145514+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c63b5 posting AVAudioSessionAvailableOutputsChangeNotification
default	19:33:11.153435+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c63b5 posting AVAudioSessionAvailableInputsChangeNotification
default	19:33:11.153522+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c63b5 posting AVAudioSessionAvailableOutputsChangeNotification
default	19:33:15.561269+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c63b5 posting AVAudioSessionAvailableOutputsChangeNotification
default	19:33:15.577979+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c63b5 posting AVAudioSessionAvailableInputsChangeNotification
default	19:33:15.578085+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c63b5 posting AVAudioSessionAvailableOutputsChangeNotification
default	19:33:15.599462+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c63b5 posting AVAudioSessionAvailableOutputsChangeNotification
default	19:33:15.611377+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c63b5 posting AVAudioSessionAvailableInputsChangeNotification
default	19:33:15.611469+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c63b5 posting AVAudioSessionAvailableOutputsChangeNotification
default	19:33:15.623943+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c63b5 posting AVAudioSessionAvailableOutputsChangeNotification
default	19:33:15.632215+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c63b5 posting AVAudioSessionAvailableInputsChangeNotification
default	19:33:15.632313+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c63b5 posting AVAudioSessionAvailableOutputsChangeNotification
default	19:33:16.875957+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c63b5 posting AVAudioSessionAvailableOutputsChangeNotification
default	19:33:16.889264+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c63b5 posting AVAudioSessionAvailableInputsChangeNotification
default	19:33:16.889426+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c63b5 posting AVAudioSessionAvailableOutputsChangeNotification
default	19:33:16.909169+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c63b5 posting AVAudioSessionAvailableOutputsChangeNotification
default	19:33:16.917680+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c63b5 posting AVAudioSessionAvailableInputsChangeNotification
default	19:33:16.917705+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c63b5 posting AVAudioSessionAvailableOutputsChangeNotification
default	19:33:16.931341+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c63b5 posting AVAudioSessionAvailableOutputsChangeNotification
default	19:33:16.940448+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c63b5 posting AVAudioSessionAvailableInputsChangeNotification
default	19:33:16.940536+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c63b5 posting AVAudioSessionAvailableOutputsChangeNotification
default	19:33:46.302824+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c63b5 posting AVAudioSessionAvailableOutputsChangeNotification
default	19:33:46.319675+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c63b5 posting AVAudioSessionAvailableInputsChangeNotification
default	19:33:46.319806+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c63b5 posting AVAudioSessionAvailableOutputsChangeNotification
default	19:33:46.337038+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c63b5 posting AVAudioSessionAvailableOutputsChangeNotification
default	19:33:46.347532+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c63b5 posting AVAudioSessionAvailableInputsChangeNotification
default	19:33:46.347709+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c63b5 posting AVAudioSessionAvailableOutputsChangeNotification
default	19:33:46.359213+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c63b5 posting AVAudioSessionAvailableOutputsChangeNotification
default	19:33:46.368459+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c63b5 posting AVAudioSessionAvailableInputsChangeNotification
default	19:33:46.368522+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c63b5 posting AVAudioSessionAvailableOutputsChangeNotification
default	19:34:08.012769+0800	hootowl	Task <26CCE2EB-8AE6-4223-9B92-00924FDD7316>.<29> resuming, timeouts(60.0, 604800.0) qos(0x15) voucher((null)) activity(00000000-0000-0000-0000-000000000000)
default	19:34:08.024162+0800	hootowl	Connection 0: creating secure tcp or quic connection
default	19:34:08.025682+0800	hootowl	Connection 36: enabling TLS
default	19:34:08.026015+0800	hootowl	Connection 36: starting, TC(0x0)
default	19:34:08.026124+0800	hootowl	[C36 9B9DE454-A695-4188-A58E-A20562EBDE87 tcgbusfs.blob.core.windows.net:443 quic-connection, url: https://tcgbusfs.blob.core.windows.net/blobtcmsv/TCMSV_allavailable.json, definite, attribution: developer, context: com.apple.CFNetwork.NSURLSession.{4EE848AE-A5DC-4E55-A08E-E23FD8E7E021}{(null)}{Y}{2}{0x0} (private), proc: 1B526020-2DE0-3C65-9122-F1177549D69A, delegated upid: 0] start
default	19:34:08.026314+0800	hootowl	[C36 tcgbusfs.blob.core.windows.net:443 initial parent-flow ((null))] event: path:start @0.000s
default	19:34:08.028165+0800	hootowl	[C36 tcgbusfs.blob.core.windows.net:443 waiting parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.003s, uuid: AF3F2C1E-B60F-4B30-B53A-D50EBD7391A7
default	19:34:08.028438+0800	hootowl	[C36 tcgbusfs.blob.core.windows.net:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_connect @0.004s
default	19:34:08.028588+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C36] reporting state preparing
default	19:34:08.029050+0800	hootowl	[C36 tcgbusfs.blob.core.windows.net:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_child @0.005s
default	19:34:08.029408+0800	hootowl	[C36.1 tcgbusfs.blob.core.windows.net:443 initial path ((null))] event: path:start @0.005s
default	19:34:08.031069+0800	hootowl	[C36.1 tcgbusfs.blob.core.windows.net:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.006s, uuid: AF3F2C1E-B60F-4B30-B53A-D50EBD7391A7
default	19:34:08.031785+0800	hootowl	[C36.1 tcgbusfs.blob.core.windows.net:443 in_progress transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: transform:start @0.007s
default	19:34:08.032865+0800	hootowl	[C36.1.1 tcgbusfs.blob.core.windows.net:443 initial path ((null))] event: path:start @0.008s
default	19:34:08.036052+0800	hootowl	[C36.1.1 tcgbusfs.blob.core.windows.net:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.010s, uuid: 5D588C59-2672-46E5-B8F8-252672ECCA20
default	19:34:08.036688+0800	hootowl	[C36.1.1 tcgbusfs.blob.core.windows.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:start_dns @0.011s
default	19:34:08.036992+0800	hootowl	Task <26CCE2EB-8AE6-4223-9B92-00924FDD7316>.<29> setting up Connection 36
default	19:34:08.067074+0800	hootowl	nw_endpoint_resolver_update [C36.1.1 tcgbusfs.blob.core.windows.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Adding endpoint handler for 20.150.22.100:443
default	19:34:08.067197+0800	hootowl	[C36.1.1 tcgbusfs.blob.core.windows.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:receive_dns @0.043s
default	19:34:08.067348+0800	hootowl	[C36.1.1.1 20.150.22.100:443 initial path ((null))] event: path:start @0.044s
default	19:34:08.067879+0800	hootowl	[C36.1.1.1 20.150.22.100:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.044s, uuid: 455DD8DB-3788-4E17-BAC0-5270922DA156
default	19:34:08.067914+0800	hootowl	[C36.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_nexus @0.044s
default	19:34:08.069258+0800	hootowl	[C36.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:receive_nexus @0.045s
default	19:34:08.070461+0800	hootowl	[C36.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_connect @0.046s
default	19:34:08.070898+0800	hootowl	tcp_output [C36.1.1.1:3] flags=[SEC] seq=2452976271, ack=0, win=65535 state=SYN_SENT rcv_nxt=0, snd_una=2452976271
default	19:34:08.150954+0800	hootowl	tcp_input [C36.1.1.1:3] flags=[S.E] seq=3321417497, ack=2452976272, win=65535 state=SYN_SENT rcv_nxt=0, snd_una=2452976271
default	19:34:08.150976+0800	hootowl	nw_flow_connected [C36.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Transport protocol connected (tcp)
default	19:34:08.151046+0800	hootowl	[C36.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_transport @0.128s
default	19:34:08.151798+0800	hootowl	boringssl_session_apply_protocol_options_for_transport_block_invoke_2(2367) [C36.1.1.1:2][0x12c80c7e0] TLS configured [server(0) min_version(0x0303) max_version(0x0304) name(tcgbusfs.blob.core.windows.net) tickets(false) false_start(false) enforce_ev(false) enforce_ats(false) ats_non_pfs_ciphersuite_allowed(false) cc_mode_enforced(false) ech(false) pqtls(true), pake(false) skip_ats_trust(false)]
default	19:34:08.151886+0800	hootowl	boringssl_context_info_handler(2806) [C36.1.1.1:2][0x12c80c7e0] Client handshake started
default	19:34:08.152048+0800	hootowl	boringssl_context_info_handler(2823) [C36.1.1.1:2][0x12c80c7e0] Client handshake state: TLS client enter_early_data
default	19:34:08.152357+0800	hootowl	boringssl_context_info_handler(2823) [C36.1.1.1:2][0x12c80c7e0] Client handshake state: TLS client read_server_hello
default	19:34:08.263875+0800	hootowl	boringssl_context_info_handler(2823) [C36.1.1.1:2][0x12c80c7e0] Client handshake state: TLS 1.3 client read_hello_retry_request
default	19:34:08.268066+0800	hootowl	boringssl_context_info_handler(2823) [C36.1.1.1:2][0x12c80c7e0] Client handshake state: TLS 1.3 client send_second_client_hello
default	19:34:08.268419+0800	hootowl	boringssl_context_info_handler(2823) [C36.1.1.1:2][0x12c80c7e0] Client handshake state: TLS 1.3 client read_server_hello
default	19:34:08.380211+0800	hootowl	boringssl_context_info_handler(2823) [C36.1.1.1:2][0x12c80c7e0] Client handshake state: TLS 1.3 client read_encrypted_extensions
default	19:34:08.381927+0800	hootowl	boringssl_context_info_handler(2823) [C36.1.1.1:2][0x12c80c7e0] Client handshake state: TLS 1.3 client read_certificate_request
default	19:34:08.381972+0800	hootowl	boringssl_context_info_handler(2823) [C36.1.1.1:2][0x12c80c7e0] Client handshake state: TLS 1.3 client read_server_certificate
default	19:34:08.382088+0800	hootowl	boringssl_context_info_handler(2823) [C36.1.1.1:2][0x12c80c7e0] Client handshake state: TLS 1.3 client read_server_certificate_verify
default	19:34:08.383225+0800	hootowl	boringssl_context_evaluate_trust_async(2249) [C36.1.1.1:2][0x12c80c7e0] Performing external trust evaluation
default	19:34:08.383272+0800	hootowl	boringssl_context_evaluate_trust_async_external(2234) [C36.1.1.1:2][0x12c80c7e0] Asyncing for external verify block
default	19:34:08.383838+0800	hootowl	Connection 36: asked to evaluate TLS Trust
default	19:34:08.383908+0800	hootowl	Task <26CCE2EB-8AE6-4223-9B92-00924FDD7316>.<29> auth completion disp=1 cred=0x0
default	19:34:08.384418+0800	hootowl	(Trust 0x13a341140) No pending evals, starting
default	19:34:08.385035+0800	hootowl	[0x11ad7d540] activating connection: mach=true listener=false peer=false name=com.apple.trustd
default	19:34:08.385632+0800	hootowl	(Trust 0x13a341140) Completed async eval kickoff
default	19:34:08.397907+0800	hootowl	(Trust 0x13a341140) trustd returned 4
default	19:34:08.398022+0800	hootowl	System Trust Evaluation yielded status(0)
default	19:34:08.398088+0800	hootowl	(Trust 0x13a340fc0) No pending evals, starting
default	19:34:08.398300+0800	hootowl	[0x11ad7fc00] activating connection: mach=true listener=false peer=false name=com.apple.trustd
default	19:34:08.398574+0800	hootowl	(Trust 0x13a340fc0) Completed async eval kickoff
default	19:34:08.398963+0800	hootowl	[0x11ad7d540] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	19:34:08.404870+0800	hootowl	(Trust 0x13a340fc0) trustd returned 4
default	19:34:08.405030+0800	hootowl	Connection 36: TLS Trust result 0
default	19:34:08.405071+0800	hootowl	boringssl_context_evaluate_trust_async_external_block_invoke_3(2148) [C36.1.1.1:2][0x12c80c7e0] Returning from external verify block with result: true
default	19:34:08.405205+0800	hootowl	boringssl_context_certificate_verify_callback(2430) [C36.1.1.1:2][0x12c80c7e0] Certificate verification result: OK
default	19:34:08.405236+0800	hootowl	boringssl_context_info_handler(2823) [C36.1.1.1:2][0x12c80c7e0] Client handshake state: TLS 1.3 client read_server_finished
default	19:34:08.405282+0800	hootowl	boringssl_context_info_handler(2823) [C36.1.1.1:2][0x12c80c7e0] Client handshake state: TLS 1.3 client send_end_of_early_data
default	19:34:08.405319+0800	hootowl	boringssl_context_info_handler(2823) [C36.1.1.1:2][0x12c80c7e0] Client handshake state: TLS 1.3 client send_client_encrypted_extensions
default	19:34:08.405330+0800	hootowl	boringssl_context_info_handler(2823) [C36.1.1.1:2][0x12c80c7e0] Client handshake state: TLS 1.3 client send_client_certificate
default	19:34:08.405355+0800	hootowl	boringssl_context_info_handler(2823) [C36.1.1.1:2][0x12c80c7e0] Client handshake state: TLS 1.3 client complete_second_flight
default	19:34:08.405390+0800	hootowl	boringssl_context_info_handler(2823) [C36.1.1.1:2][0x12c80c7e0] Client handshake state: TLS 1.3 client done
default	19:34:08.405517+0800	hootowl	boringssl_context_info_handler(2823) [C36.1.1.1:2][0x12c80c7e0] Client handshake state: TLS client finish_client_handshake
default	19:34:08.405535+0800	hootowl	boringssl_context_info_handler(2823) [C36.1.1.1:2][0x12c80c7e0] Client handshake state: TLS client done
default	19:34:08.405560+0800	hootowl	boringssl_context_info_handler(2812) [C36.1.1.1:2][0x12c80c7e0] Client handshake done
default	19:34:08.405865+0800	hootowl	nw_protocol_boringssl_signal_connected(895) [C36.1.1.1:2][0x12c80c7e0] TLS connected [server(0) version(0x0304) ciphersuite(TLS_AES_256_GCM_SHA384) group(0x0018) signature_alg(0x0804) alpn(nil) resumed(0) offered_ticket(0) in_early_data(0) early_data_accepted(0) false_started(0) ocsp_received(1) sct_received(0) connect_time(254ms) flight_time(221ms) rtt(112ms) write_stalls(0) read_stalls(8) pake(0x0000)]
default	19:34:08.406161+0800	hootowl	nw_flow_connected [C36.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (CFNetworkConnection-4160941018)
default	19:34:08.406260+0800	hootowl	[C36.1.1.1 20.150.22.100:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.383s
default	19:34:08.406394+0800	hootowl	[C36.1.1 tcgbusfs.blob.core.windows.net:443 ready resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.383s
default	19:34:08.406454+0800	hootowl	[C36.1 tcgbusfs.blob.core.windows.net:443 ready transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.383s
default	19:34:08.406553+0800	hootowl	[C36.1.1.1 20.150.22.100:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.383s
default	19:34:08.406630+0800	hootowl	[C36.1.1 tcgbusfs.blob.core.windows.net:443 ready resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.383s
default	19:34:08.406686+0800	hootowl	[C36.1 tcgbusfs.blob.core.windows.net:443 ready transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.383s
default	19:34:08.406882+0800	hootowl	nw_flow_connected [C36 20.150.22.100:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (endpoint_flow)
default	19:34:08.406914+0800	hootowl	[C36 20.150.22.100:443 ready parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_connect @0.383s
default	19:34:08.407139+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C36] reporting state ready
default	19:34:08.407150+0800	hootowl	[C36 20.150.22.100:443 ready parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.383s
default	19:34:08.407167+0800	hootowl	nw_connection_send_viability_changed_on_nw_queue [C36] viability_changed_handler(true)
default	19:34:08.407208+0800	hootowl	[0x11ad7fc00] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	19:34:08.407243+0800	hootowl	Connection 36: connected successfully
default	19:34:08.407269+0800	hootowl	Connection 36: TLS handshake complete
default	19:34:08.407299+0800	hootowl	Connection 36: ready C(N) E(N)
default	19:34:08.407458+0800	hootowl	Task <26CCE2EB-8AE6-4223-9B92-00924FDD7316>.<29> now using Connection 36
default	19:34:08.407485+0800	hootowl	Connection 36: received viability advisory(Y)
default	19:34:08.407604+0800	hootowl	Task <26CCE2EB-8AE6-4223-9B92-00924FDD7316>.<29> sent request, body N 0
default	19:34:08.487092+0800	hootowl	Task <26CCE2EB-8AE6-4223-9B92-00924FDD7316>.<29> received response, status 304 content K
default	19:34:08.487766+0800	hootowl	Task <26CCE2EB-8AE6-4223-9B92-00924FDD7316>.<29> done using Connection 36
default	19:34:08.488130+0800	hootowl	[C36] event: client:connection_idle @0.464s
default	19:34:08.488481+0800	hootowl	nw_protocol_tcp_notify [C36.1.1.1:3] nw_protocol_notification_type_connection_idle is true
default	19:34:08.488641+0800	hootowl	Task <26CCE2EB-8AE6-4223-9B92-00924FDD7316>.<29> summary for task success {transaction_duration_ms=473, response_status=304, connection=36, protocol="http/1.1", domain_lookup_duration_ms=32, connect_duration_ms=337, secure_connection_duration_ms=254, private_relay=false, request_start_ms=393, request_duration_ms=0, response_start_ms=472, response_duration_ms=0, request_bytes=337, request_throughput_kbps=44961, response_bytes=308, response_throughput_kbps=3844, cache_hit=true}
default	19:34:08.488693+0800	hootowl	nw_protocol_tcp_set_connection_idle [C36.1.1.1:3] os_nexus_flow_set_connection_idle returned 0
default	19:34:08.488967+0800	hootowl	[C36] event: client:connection_idle @0.464s
default	19:34:08.489507+0800	hootowl	nw_protocol_tcp_notify [C36.1.1.1:3] nw_protocol_notification_type_connection_idle is true
default	19:34:08.489546+0800	hootowl	nw_protocol_tcp_set_connection_idle [C36.1.1.1:3] os_nexus_flow_set_connection_idle returned 0
default	19:34:08.489567+0800	hootowl	Task <26CCE2EB-8AE6-4223-9B92-00924FDD7316>.<29> finished successfully
default	19:34:08.489587+0800	hootowl	Mu1Base+Ext 152
taipei 📦 minutely Received 460036 bytes
default	19:34:08.490648+0800	hootowl	Mu1Base+Ext 177
previousHash not changed
default	19:34:08.503293+0800	hootowl	Municipal+Cyclops 93
🎨 model refreshed — obs:0s car:18 thread:main
default	19:34:38.907040+0800	hootowl	Connection 36: cleaning up
default	19:34:38.907325+0800	hootowl	[C36 9B9DE454-A695-4188-A58E-A20562EBDE87 tcgbusfs.blob.core.windows.net:443 quic-connection, url: https://tcgbusfs.blob.core.windows.net/blobtcmsv/TCMSV_allavailable.json, definite, attribution: developer] cancel
default	19:34:38.907798+0800	hootowl	[C36 9B9DE454-A695-4188-A58E-A20562EBDE87 tcgbusfs.blob.core.windows.net:443 quic-connection, url: https://tcgbusfs.blob.core.windows.net/blobtcmsv/TCMSV_allavailable.json, definite, attribution: developer] cancelled
	[C36.1.1.1 455DD8DB-3788-4E17-BAC0-5270922DA156 192.168.50.191:56023<->20.150.22.100:443]
	Connected Path: satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good
	Privacy Stance: Not Eligible
	Duration: 30.884s, DNS @0.011s took 0.032s, TCP @0.046s took 0.082s,  took 0.254s
	bytes in/out: 10765/2357, packets in/out: 8/13, rtt: 0.086s, retransmitted bytes: 0, out-of-order bytes: 0
	ecn packets sent/acked/marked/lost: 5/3/0/0
default	19:34:38.908401+0800	hootowl	nw_protocol_tcp_log_summary [C36.1.1.1:3] 
	[29B91FF9-AF7C-4153-AAD3-26A06CACB139 192.168.50.191:56023<->20.150.22.100:443]
	Init: 1, Conn_Time: 80.814ms, SYNs: 1, WR_T: 0/0, RD_T: 0/0, TFO: 0/0/0, ECN: 0/1/1, Accurate ECN (client/server): Disabled/Disabled, TS: 1, TSO: 0
	rtt_cache: process, rtt_upd: 4, rtt: 86.812ms, rtt_var: 27.812ms rtt_nc: 86.812ms, rtt_var_nc: 27.812ms base rtt: 65ms
	ACKs-compressed: 0, ACKs delayed: 0 delayed ACKs sent: 0
default	19:34:38.908997+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C36] reporting state cancelled
default	19:34:38.909003+0800	hootowl	Connection 36: done
default	19:34:38.909209+0800	hootowl	tcp_output [C36.1.1.1:3] flags=[F.] seq=2452978653, ack=3321428263, win=2048 state=FIN_WAIT_1 rcv_nxt=3321428263, snd_una=2452978629
default	19:34:39.101931+0800	hootowl	tcp_input [C36.1.1.1:3] flags=[F.] seq=3321428263, ack=2452978654, win=16382 state=FIN_WAIT_2 rcv_nxt=3321428263, snd_una=2452978654
default	19:35:09.199884+0800	hootowl	tcp_close [C36.1.1.1:3] TCP Packets:
	 snd    0.000s seq 2452976271:2452976272 ack 0          win 65535 len 0    [SEC]
	 rcv    0.081s seq 3321417497:3321417498 ack 2452976272 win 65535 len 0    [S.E] ECT0
	 snd    0.000s seq 2452976272:2452976272 ack 3321417498 win 2053  len 0    [.]
	 snd    0.001s seq 2452976272:2452977700 ack 3321417498 win 2053  len 1428 [.] ECT0
	 snd    0.000s seq 2452977700:2452977811 ack 3321417498 win 2053  len 111  [P.] ECT0
	 rcv    0.111s seq 3321417498:3321417498 ack 2452977811 win 16385 len 0    [.]
	 rcv    0.000s seq 3321417498:3321417597 ack 2452977811 win 16385 len 99   [P.] ECT0
	 snd    0.000s seq 2452977811:2452977811 ack 3321417597 win 2052  len 0    [.]
	 snd    0.005s seq 2452977811:2452978196 ack 3321417597 win 2052  len 385  [P.] ECT0
	 rcv    0.109s seq 3321417597:3321420477 ack 2452978196 win 16384 len 2880 [.] ECT0
	 snd    0.000s seq 2452978196:2452978196 ack 3321420477 win 2007  len 0    [.]
	 rcv    0.004s seq 3321420477:3321427830 ack 2452978196 win 16384 len 7353 [P.] ECT0
	 snd    0.000s seq 2452978196:2452978196 ack 3321427830 win 1934  len 0    [.]
	 snd    0.000s seq 2452978196:2452978196 ack 3321427830 win 2048  len 0    [.]
	 snd    0.025s seq 2452978196:2452978270 ack 3321427830 win 2048  len 74   [P.] ECT0
	 snd    0.002s seq 2452978270:2452978629 ack 3321427830 win 2048  len 359  [P.] ECT0
	 rcv    0.078s seq 3321427830:3321427830 ack 2452978629 win 16382 len 0    [.]
	 rcv    0.000s seq 3321427830:3321428263 ack 2452978629 win 16382 len 433  [P.] ECT0
	 snd    0.000s seq 2452978629:2452978629 ack 3321428263 win 2042  len 0    [.]
	 rcv    0.635s seq 3321428263:3321428263 ack 2452978629 win 16382 len 0    [.]
	 snd   29.776s seq 2452978629:2452978653 ack 3321428263 win 2048  len 24   [P.] ECT0
	 snd    0.001s seq 2452978653:2452978654 ack 3321428263 win 2048  len 0    [F.]
	 rcv    0.193s seq 3321428263:3321428263 ack 2452978654 win 16382 len 0    [.]
	 rcv    0.000s seq 3321428263:3321428264 ack 2452978654 win 16382 len 0    [F.]
	 snd    0.000s seq 2452978654:2452978654 ack 3321428264 win 2048  len 0    [.]
	Last packet 30098ms ago.
default	19:35:30.575164+0800	hootowl	Evaluating dispatch of UIEvent: 0x139100a00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:35:30.575237+0800	hootowl	Evaluating dispatch of UIEvent: 0x139100a00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:35:31.466701+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c63b5 posting AVAudioSessionAvailableInputsChangeNotification
default	19:35:31.467113+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c63b5 posting AVAudioSessionAvailableOutputsChangeNotification
default	19:35:31.630999+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c63b5 posting AVAudioSessionAvailableOutputsChangeNotification
default	19:35:31.632704+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c63b5 posting AVAudioSessionAvailableInputsChangeNotification
default	19:35:31.632755+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c63b5 posting AVAudioSessionAvailableOutputsChangeNotification
default	19:35:31.750226+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c63b5 posting AVAudioSessionAvailableOutputsChangeNotification
default	19:35:38.926500+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c63b5 posting AVAudioSessionAvailableInputsChangeNotification
default	19:35:38.926733+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c63b5 posting AVAudioSessionAvailableOutputsChangeNotification
default	19:36:01.171932+0800	hootowl	Evaluating dispatch of UIEvent: 0x139100a00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:01.202985+0800	hootowl	TX focusApplication (peekAppEvent) stealKB:Y scene:com.sharkda.hootowl-1B8F959F-618F-4A0D-AD89-E09DEC0EAB34
default	19:36:01.209183+0800	hootowl	Evaluating dispatch of UIEvent: 0x139100a00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:01.209484+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	19:36:01.209670+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:01.448494+0800	hootowl	App is being debugged, do not track this hang
default	19:36:01.448518+0800	hootowl	Hang detected: 0.28s (debugger attached, not reporting)
default	19:36:01.457365+0800	hootowl	Evaluating dispatch of UIEvent: 0x139100a00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:01.457410+0800	hootowl	Evaluating dispatch of UIEvent: 0x139100a00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:01.457432+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	19:36:01.457451+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:01.482496+0800	hootowl	<UIWindowScene: 0x10c450200> (1B8F959F-618F-4A0D-AD89-E09DEC0EAB34) Scene updated orientation preferences: ( Pu Ll Lr ) -> ( Pu )
default	19:36:01.728632+0800	hootowl	App is being debugged, do not track this hang
default	19:36:01.728645+0800	hootowl	Hang detected: 0.27s (debugger attached, not reporting)
default	19:36:02.233299+0800	hootowl	<UIWindowScene: 0x10c450200> (1B8F959F-618F-4A0D-AD89-E09DEC0EAB34) Scene updated orientation preferences: ( Pu ) -> ( Pu Ll Lr )
default	19:36:03.104820+0800	hootowl	TX focusApplication (peekAppEvent) stealKB:Y scene:com.sharkda.hootowl-1B8F959F-618F-4A0D-AD89-E09DEC0EAB34
default	19:36:03.104908+0800	hootowl	Evaluating dispatch of UIEvent: 0x139100a00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:03.104957+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	19:36:03.105118+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:03.132833+0800	hootowl	Evaluating dispatch of UIEvent: 0x139100a00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:03.185810+0800	hootowl	Evaluating dispatch of UIEvent: 0x139100a00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 1
default	19:36:03.218561+0800	hootowl	Evaluating dispatch of UIEvent: 0x139100a00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:03.219737+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	19:36:03.219779+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:03.240030+0800	hootowl	Evaluating dispatch of UIEvent: 0x139100a00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:03.240077+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	19:36:03.240571+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:03.249710+0800	hootowl	Evaluating dispatch of UIEvent: 0x139100a00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:03.249727+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	19:36:03.249741+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:03.289597+0800	hootowl	activate generator with style: TurnOn; activationCount: 0 -> 1; styleActivationCount: 0 -> 1; <_UIClickPresentationFeedbackGenerator: 0x12cbf1680>
default	19:36:03.289612+0800	hootowl	activate engine <_UIFeedbackCoreHapticsEngine: 0x11c018e00>, clientCount: 0 -> 1
default	19:36:03.290055+0800	hootowl	activating engine <_UIFeedbackCoreHapticsEngine: 0x11c018e00>
default	19:36:03.290075+0800	hootowl	engine <_UIFeedbackCoreHapticsEngine: 0x11c018e00> state changed: Inactive -> Activating
default	19:36:03.290086+0800	hootowl	starting core haptics engine for <_UIFeedbackCoreHapticsEngine: 0x11c018e00>
default	19:36:03.290100+0800	hootowl	creating core haptics engine for <_UIFeedbackCoreHapticsEngine: 0x11c018e00>
default	19:36:03.290128+0800	hootowl	deactivate generator with style: TurnOn; activationCount: 1 -> 0; styleActivationCount: 1 -> 0; <_UIClickPresentationFeedbackGenerator: 0x12cbf1680>
default	19:36:03.290241+0800	hootowl	Evaluating dispatch of UIEvent: 0x139100a00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:03.290286+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	19:36:03.290302+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:03.290640+0800	hootowl	        CHHapticEngine.mm:1532  -[CHHapticEngine initWithAudioSession:sessionIsShared:options:error:]: Creating engine 0x1391371e0 with unshared audio session 0x0
default	19:36:03.290663+0800	hootowl	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	19:36:03.291349+0800	hootowl	[0x11ad943c0] activating connection: mach=false listener=false peer=false name=com.apple.audio.AudioConverterService.HighCapacity
default	19:36:03.291512+0800	hootowl	Ignoring beginScrollingWithRegion: <UIPointerRegion: 0x13a3e5e00; rect = (0 0; 393 793); identifier = UIScrollView.scrollingPointerRegion> because pointer state is disabled
default	19:36:03.291520+0800	hootowl	[C:3] Alloc com.apple.PointerUI.pointeruid.service
default	19:36:03.291527+0800	hootowl	[0x104284780] activating connection: mach=false listener=false peer=false name=(anonymous)
default	19:36:03.297597+0800	hootowl	<UIWindowScene: 0x10c450200> (1B8F959F-618F-4A0D-AD89-E09DEC0EAB34) Scene updated orientation preferences: ( Pu Ll Lr ) -> ( Pu )
default	19:36:03.507240+0800	hootowl	[0x11ad943c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	19:36:03.507550+0800	hootowl	[0x11ade03c0] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	19:36:03.639993+0800	hootowl	    SessionCore_Create.mm:99    Created session 0x10438bd70 with ID: 0x77c63b9
default	19:36:03.640888+0800	hootowl	Evaluating dispatch of UIEvent: 0x139100a00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:03.645553+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	19:36:03.646831+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:03.648092+0800	hootowl	<<<< AVInputDeviceDiscoverySession >>>> -[AVInputDeviceDiscoverySession setFastDiscoveryEnabled:]: called (session=0x139285ec0, setFastDiscoveryEnabled=NO)
default	19:36:03.648205+0800	hootowl	<<<< AVInputDeviceDiscoverySession (FigRouteDiscoverer) >>>> -[AVFigRouteDiscovererInputDeviceDiscoverySessionImpl inputDeviceDiscoverySessionFastDiscoveryDidChange:]: Setting fastDiscoveryEnabled to NO (client: hootowl) for session=0x11c25d140
default	19:36:03.648279+0800	hootowl	<<<< AVOutputDeviceDiscoverySession >>>> -[AVOutputDeviceDiscoverySession setFastDiscoveryEnabled:]: called (session=0x10438a330, setFastDiscoveryEnabled=NO)
default	19:36:03.648345+0800	hootowl	<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> -[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl outputDeviceDiscoverySessionFastDiscoveryDidChange:]: Setting fastDiscoveryEnabled to NO (client: hootowl) for session=0x10438a330
default	19:36:03.649177+0800	hootowl	[0x11ade3e80] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
default	19:36:03.649215+0800	hootowl	Evaluating dispatch of UIEvent: 0x139100a00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:03.649357+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	19:36:03.649394+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:03.720810+0800	hootowl	    AVAudioSession_iOS.mm:3459  enableNotifications: inValue = 0
default	19:36:03.724761+0800	hootowl	Evaluating dispatch of UIEvent: 0x139100a00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:03.724771+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	19:36:03.724787+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:03.726041+0800	hootowl	[0x11ad97340] activating connection: mach=true listener=false peer=false name=com.apple.audio.hapticd
default	19:36:03.726133+0800	hootowl	[0x11ad95b80] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	19:36:03.726913+0800	hootowl	    HapticServerConfig.mm:40    -[HapticServerConfig initWithHapticPlayer:withOptions:error:]: Querying server for capabilities with 'FullGamut' Locality
default	19:36:03.726922+0800	hootowl	    HapticServerConfig.mm:106   -[HapticServerConfig initWithHapticPlayer:withOptions:error:]: Querying server for UsageCategory of 'UIFeedback'
default	19:36:03.726928+0800	hootowl	        AVHapticPlayer.mm:313   -[AVHapticPlayer queryServerCapabilities:reply:]: clientID: 0x10090d6
default	19:36:03.728053+0800	hootowl	        CHHapticEngine.mm:879   -[CHHapticEngine updateEngineBehavior]: Setting player's behavior to 0x0
default	19:36:03.728070+0800	hootowl	        AVHapticPlayer.mm:323   -[AVHapticPlayer setBehavior:error:]: clientID: 0x10090d6 behavior: 0
default	19:36:03.728128+0800	hootowl	        CHHapticEngine.mm:879   -[CHHapticEngine updateEngineBehavior]: Setting player's behavior to 0x4
default	19:36:03.728147+0800	hootowl	        AVHapticPlayer.mm:323   -[AVHapticPlayer setBehavior:error:]: clientID: 0x10090d6 behavior: 4
default	19:36:03.728766+0800	hootowl	        CHHapticEngine.mm:1302  -[CHHapticEngine startWithCompletionHandler:]: Called on engine 0x1391371e0
default	19:36:03.728796+0800	hootowl	        CHHapticEngine.mm:1251  -[CHHapticEngine doStartWithCompletionHandler:]: Starting underlying Haptic Player
default	19:36:03.728804+0800	hootowl	activate engine <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c01a280>, clientCount: 0 -> 1
default	19:36:03.728811+0800	hootowl	        CHHapticEngine.mm:885   -[CHHapticEngine updateEngineBehaviorWithError:]: Setting player's behavior to 0x4
default	19:36:03.728816+0800	hootowl	activating engine <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c01a280>
default	19:36:03.728823+0800	hootowl	        AVHapticPlayer.mm:323   -[AVHapticPlayer setBehavior:error:]: clientID: 0x10090d6 behavior: 4
default	19:36:03.728830+0800	hootowl	engine <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c01a280> state changed: Inactive -> Activating
default	19:36:03.728836+0800	hootowl	        AVHapticPlayer.mm:675   -[AVHapticPlayer startRunningWithCompletionHandler:]: start running: clientID: 0x10090d6
default	19:36:03.728842+0800	hootowl	starting core haptics engine for <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c01a280>
default	19:36:03.729520+0800	hootowl	        AVHapticClient.mm:363   -[AVHapticClient startRunning:]: Client 0x10090d6 starting
default	19:36:03.729881+0800	hootowl	creating core haptics engine for <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c01a280>
default	19:36:03.730499+0800	hootowl	        CHHapticEngine.mm:1532  -[CHHapticEngine initWithAudioSession:sessionIsShared:options:error:]: Creating engine 0x1391372c0 with unshared audio session 0x0
default	19:36:03.732003+0800	hootowl	[0x11ad96080] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	19:36:03.741252+0800	hootowl	    SessionCore_Create.mm:99    Created session 0x10438b8b0 with ID: 0x77c63ba
default	19:36:03.747318+0800	hootowl	<<<< AVInputDeviceDiscoverySession >>>> -[AVInputDeviceDiscoverySession setFastDiscoveryEnabled:]: called (session=0x139286e40, setFastDiscoveryEnabled=NO)
default	19:36:03.749777+0800	hootowl	<<<< AVInputDeviceDiscoverySession (FigRouteDiscoverer) >>>> -[AVFigRouteDiscovererInputDeviceDiscoverySessionImpl inputDeviceDiscoverySessionFastDiscoveryDidChange:]: Setting fastDiscoveryEnabled to NO (client: hootowl) for session=0x13d58b780
default	19:36:03.749797+0800	hootowl	<<<< AVOutputDeviceDiscoverySession >>>> -[AVOutputDeviceDiscoverySession setFastDiscoveryEnabled:]: called (session=0x10438b830, setFastDiscoveryEnabled=NO)
default	19:36:03.749830+0800	hootowl	<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> -[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl outputDeviceDiscoverySessionFastDiscoveryDidChange:]: Setting fastDiscoveryEnabled to NO (client: hootowl) for session=0x10438b830
default	19:36:03.754782+0800	hootowl	Evaluating dispatch of UIEvent: 0x139100a00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:03.755338+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	19:36:03.755371+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:03.758204+0800	hootowl	Evaluating dispatch of UIEvent: 0x139100a00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:03.758228+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	19:36:03.758248+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:03.766192+0800	hootowl	Evaluating dispatch of UIEvent: 0x139100a00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:03.774255+0800	hootowl	cannot migrate AudioUnit assets for current process
default	19:36:03.774463+0800	hootowl	Evaluating dispatch of UIEvent: 0x139100a00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:03.774490+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	19:36:03.774569+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:03.799253+0800	hootowl	Received state update for 37078 (app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>, unknown-NotVisible
default	19:36:03.807893+0800	hootowl	Evaluating dispatch of UIEvent: 0x139100a00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:03.828869+0800	hootowl	Evaluating dispatch of UIEvent: 0x139100a00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:03.828907+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	19:36:03.828924+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:03.839474+0800	hootowl	Evaluating dispatch of UIEvent: 0x139100a00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:03.841116+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	19:36:03.841310+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:03.844027+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c63b5 posting AVAudioSessionAvailableOutputsChangeNotification
default	19:36:03.844041+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c63b9 posting AVAudioSessionAvailableOutputsChangeNotification
default	19:36:03.849873+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c63ba posting AVAudioSessionAvailableOutputsChangeNotification
default	19:36:03.859158+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c63b5 posting AVAudioSessionAvailableInputsChangeNotification
default	19:36:03.859194+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c63b5 posting AVAudioSessionAvailableOutputsChangeNotification
default	19:36:03.859364+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c63b9 posting AVAudioSessionAvailableInputsChangeNotification
default	19:36:03.859433+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c63b9 posting AVAudioSessionAvailableOutputsChangeNotification
default	19:36:03.859596+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c63ba posting AVAudioSessionAvailableInputsChangeNotification
default	19:36:03.859800+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c63ba posting AVAudioSessionAvailableOutputsChangeNotification
default	19:36:03.859828+0800	hootowl	Ignoring endScrollingWithRegion: <UIPointerRegion: 0x13a3e5e00; rect = (0 0; 393 793); identifier = UIScrollView.scrollingPointerRegion> because scrollingRegion does not match: (null)
default	19:36:03.879642+0800	hootowl	    AVAudioSession_iOS.mm:3459  enableNotifications: inValue = 0
default	19:36:03.880747+0800	hootowl	[0x11ad94b40] activating connection: mach=true listener=false peer=false name=com.apple.audio.hapticd
default	19:36:03.912086+0800	hootowl	    HapticServerConfig.mm:40    -[HapticServerConfig initWithHapticPlayer:withOptions:error:]: Querying server for capabilities with 'FullGamut' Locality
default	19:36:03.912126+0800	hootowl	    HapticServerConfig.mm:106   -[HapticServerConfig initWithHapticPlayer:withOptions:error:]: Querying server for UsageCategory of 'UIFeedback'
default	19:36:03.912158+0800	hootowl	        AVHapticPlayer.mm:313   -[AVHapticPlayer queryServerCapabilities:reply:]: clientID: 0x20090d6
default	19:36:03.939889+0800	hootowl	        CHHapticEngine.mm:879   -[CHHapticEngine updateEngineBehavior]: Setting player's behavior to 0x0
default	19:36:03.939943+0800	hootowl	        AVHapticPlayer.mm:323   -[AVHapticPlayer setBehavior:error:]: clientID: 0x20090d6 behavior: 0
default	19:36:03.940148+0800	hootowl	        CHHapticEngine.mm:879   -[CHHapticEngine updateEngineBehavior]: Setting player's behavior to 0x4
default	19:36:03.940222+0800	hootowl	        AVHapticPlayer.mm:323   -[AVHapticPlayer setBehavior:error:]: clientID: 0x20090d6 behavior: 4
default	19:36:03.942533+0800	hootowl	        CHHapticEngine.mm:1302  -[CHHapticEngine startWithCompletionHandler:]: Called on engine 0x1391372c0
default	19:36:03.942543+0800	hootowl	        CHHapticEngine.mm:1251  -[CHHapticEngine doStartWithCompletionHandler:]: Starting underlying Haptic Player
default	19:36:03.942558+0800	hootowl	deactivate engine <_UIFeedbackCoreHapticsEngine: 0x11c018e00>, clientCount: 1 -> 0
default	19:36:03.942625+0800	hootowl	        CHHapticEngine.mm:885   -[CHHapticEngine updateEngineBehaviorWithError:]: Setting player's behavior to 0x5
default	19:36:03.942642+0800	hootowl	_internal_deactivateEngineIfPossible <_UIFeedbackCoreHapticsEngine: 0x11c018e00>, clientCount: 0, suspended: 0
default	19:36:03.942747+0800	hootowl	        AVHapticPlayer.mm:323   -[AVHapticPlayer setBehavior:error:]: clientID: 0x20090d6 behavior: 5
default	19:36:03.942950+0800	hootowl	deactivate engine <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c01a280>, clientCount: 1 -> 0
default	19:36:03.943041+0800	hootowl	_internal_deactivateEngineIfPossible <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c01a280>, clientCount: 0, suspended: 0
default	19:36:03.943054+0800	hootowl	core haptics engine STARTED for <_UIFeedbackCoreHapticsEngine: 0x11c018e00>
default	19:36:03.943062+0800	hootowl	engine <_UIFeedbackCoreHapticsEngine: 0x11c018e00> state changed: Activating -> Running
default	19:36:03.943265+0800	hootowl	_internal_deactivateEngineIfPossible <_UIFeedbackCoreHapticsEngine: 0x11c018e00>, clientCount: 0, suspended: 0
default	19:36:03.943279+0800	hootowl	_internal_teardownUnderlyingPlayerIfPossible <_UIFeedbackCoreHapticsEngine: 0x11c018e00>
default	19:36:03.943381+0800	hootowl	engine <_UIFeedbackCoreHapticsEngine: 0x11c018e00> state changed: Running -> Deactivating
default	19:36:03.943413+0800	hootowl	        CHHapticEngine.mm:1461  -[CHHapticEngine notifyWhenPlayersFinished:]: Called on engine 0x1391371e0 with finishedHandler 0x11c14a740
default	19:36:03.943492+0800	hootowl	        AVHapticPlayer.mm:762   -[AVHapticPlayer finishWithCompletionHandler:]: finish with comp handler: clientID: 0x10090d6
default	19:36:03.943607+0800	hootowl	        AVHapticClient.mm:421   -[AVHapticClient finish:]: Client 0x10090d6 finishing
default	19:36:03.944117+0800	hootowl	        AVHapticPlayer.mm:675   -[AVHapticPlayer startRunningWithCompletionHandler:]: start running: clientID: 0x20090d6
default	19:36:03.944226+0800	hootowl	        AVHapticClient.mm:426   -[AVHapticClient finish:]_block_invoke: completionCallback set to 0x1043156b0
default	19:36:03.944293+0800	hootowl	        AVHapticClient.mm:363   -[AVHapticClient startRunning:]: Client 0x20090d6 starting
default	19:36:03.944313+0800	hootowl	        AVHapticClient.mm:453   -[AVHapticClient finish:]: Client 0x10090d6 done with finish
default	19:36:03.954615+0800	hootowl	core haptics engine STARTED for <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c01a280>
default	19:36:03.954760+0800	hootowl	engine <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c01a280> state changed: Activating -> Running
default	19:36:03.954785+0800	hootowl	_internal_deactivateEngineIfPossible <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c01a280>, clientCount: 0, suspended: 0
default	19:36:03.954804+0800	hootowl	_internal_teardownUnderlyingPlayerIfPossible <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c01a280>
default	19:36:03.954854+0800	hootowl	engine <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c01a280> state changed: Running -> Deactivating
default	19:36:03.954885+0800	hootowl	        CHHapticEngine.mm:1461  -[CHHapticEngine notifyWhenPlayersFinished:]: Called on engine 0x1391372c0 with finishedHandler 0x11c149680
default	19:36:03.955050+0800	hootowl	        AVHapticPlayer.mm:762   -[AVHapticPlayer finishWithCompletionHandler:]: finish with comp handler: clientID: 0x20090d6
default	19:36:03.955068+0800	hootowl	        AVHapticClient.mm:421   -[AVHapticClient finish:]: Client 0x20090d6 finishing
default	19:36:03.955110+0800	hootowl	        AVHapticClient.mm:426   -[AVHapticClient finish:]_block_invoke: completionCallback set to 0x12c864330
default	19:36:03.955351+0800	hootowl	        AVHapticClient.mm:453   -[AVHapticClient finish:]: Client 0x20090d6 done with finish
default	19:36:03.956593+0800	hootowl	        AVHapticClient.mm:1472  -[AVHapticClient clientCompletedWithError:]: Client-side (async) finish completion callback for client 0x10090d6 called from server
default	19:36:03.956645+0800	hootowl	        AVHapticClient.mm:1477  -[AVHapticClient clientCompletedWithError:]_block_invoke: Async dispatch: preparing to call completionCallback for client 0x10090d6
default	19:36:03.956666+0800	hootowl	        AVHapticClient.mm:1479  -[AVHapticClient clientCompletedWithError:]_block_invoke: Calling completionCallback 0x1042922e0 and then setting to nil
default	19:36:03.956883+0800	hootowl	core haptics engine finished for <_UIFeedbackCoreHapticsEngine: 0x11c018e00>
default	19:36:03.957278+0800	hootowl	stopping core haptics engine for <_UIFeedbackCoreHapticsEngine: 0x11c018e00>
default	19:36:03.957384+0800	hootowl	        CHHapticEngine.mm:1439  -[CHHapticEngine stopWithCompletionHandler:]: Called on engine 0x1391371e0
default	19:36:03.957959+0800	hootowl	        CHHapticEngine.mm:1403  -[CHHapticEngine doStopWithCompletionHandler:]: Stopping underlying Haptic Player
default	19:36:03.958076+0800	hootowl	_internal_deactivateEngineIfPossible <_UIFeedbackCoreHapticsEngine: 0x11c018e00> tearedDown: 1
default	19:36:03.958091+0800	hootowl	        AVHapticPlayer.mm:739   -[AVHapticPlayer stopRunningWithCompletionHandler:]: stop running: clientID: 0x10090d6
default	19:36:03.958121+0800	hootowl	engine <_UIFeedbackCoreHapticsEngine: 0x11c018e00> state changed: Deactivating -> Inactive
default	19:36:03.958592+0800	hootowl	        AVHapticClient.mm:398   -[AVHapticClient stopRunning:]: Client 0x10090d6 stopping
default	19:36:03.962088+0800	hootowl	        AVHapticClient.mm:1472  -[AVHapticClient clientCompletedWithError:]: Client-side (async) finish completion callback for client 0x10090d6 called from server
default	19:36:03.962105+0800	hootowl	        AVHapticClient.mm:1477  -[AVHapticClient clientCompletedWithError:]_block_invoke: Async dispatch: preparing to call completionCallback for client 0x10090d6
default	19:36:03.962404+0800	hootowl	        AVHapticClient.mm:1484  -[AVHapticClient clientCompletedWithError:]_block_invoke: strongSelf.completionCallback is nil
default	19:36:03.962711+0800	hootowl	        AVHapticClient.mm:1472  -[AVHapticClient clientCompletedWithError:]: Client-side (async) finish completion callback for client 0x20090d6 called from server
default	19:36:03.962726+0800	hootowl	        AVHapticClient.mm:1477  -[AVHapticClient clientCompletedWithError:]_block_invoke: Async dispatch: preparing to call completionCallback for client 0x20090d6
default	19:36:03.962738+0800	hootowl	        AVHapticClient.mm:1479  -[AVHapticClient clientCompletedWithError:]_block_invoke: Calling completionCallback 0x12c864330 and then setting to nil
default	19:36:03.962841+0800	hootowl	core haptics engine finished for <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c01a280>
default	19:36:03.962909+0800	hootowl	stopping core haptics engine for <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c01a280>
default	19:36:03.962945+0800	hootowl	        CHHapticEngine.mm:1439  -[CHHapticEngine stopWithCompletionHandler:]: Called on engine 0x1391372c0
default	19:36:03.963049+0800	hootowl	        CHHapticEngine.mm:1403  -[CHHapticEngine doStopWithCompletionHandler:]: Stopping underlying Haptic Player
default	19:36:03.963099+0800	hootowl	_internal_deactivateEngineIfPossible <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c01a280> tearedDown: 1
default	19:36:03.963238+0800	hootowl	        AVHapticPlayer.mm:739   -[AVHapticPlayer stopRunningWithCompletionHandler:]: stop running: clientID: 0x20090d6
default	19:36:03.963269+0800	hootowl	engine <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c01a280> state changed: Deactivating -> Inactive
default	19:36:03.963964+0800	hootowl	        AVHapticClient.mm:398   -[AVHapticClient stopRunning:]: Client 0x20090d6 stopping
default	19:36:04.004492+0800	hootowl	        AVHapticClient.mm:1472  -[AVHapticClient clientCompletedWithError:]: Client-side (async) finish completion callback for client 0x20090d6 called from server
default	19:36:04.018017+0800	hootowl	core haptics engine STOPPED for <_UIFeedbackCoreHapticsEngine: 0x11c018e00>
default	19:36:04.018044+0800	hootowl	        AVHapticClient.mm:1477  -[AVHapticClient clientCompletedWithError:]_block_invoke: Async dispatch: preparing to call completionCallback for client 0x20090d6
default	19:36:04.018068+0800	hootowl	        AVHapticClient.mm:1484  -[AVHapticClient clientCompletedWithError:]_block_invoke: strongSelf.completionCallback is nil
default	19:36:04.040235+0800	hootowl	core haptics engine STOPPED for <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c01a280>
default	19:36:04.156321+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c63b5 posting AVAudioSessionAvailableOutputsChangeNotification
default	19:36:04.156373+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c63b9 posting AVAudioSessionAvailableOutputsChangeNotification
default	19:36:04.156423+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c63ba posting AVAudioSessionAvailableOutputsChangeNotification
default	19:36:04.204351+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c63b5 posting AVAudioSessionAvailableInputsChangeNotification
default	19:36:04.204389+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c63b5 posting AVAudioSessionAvailableOutputsChangeNotification
default	19:36:04.209429+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c63b9 posting AVAudioSessionAvailableInputsChangeNotification
default	19:36:04.213327+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c63b9 posting AVAudioSessionAvailableOutputsChangeNotification
default	19:36:04.214291+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c63ba posting AVAudioSessionAvailableInputsChangeNotification
default	19:36:04.214304+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c63ba posting AVAudioSessionAvailableOutputsChangeNotification
default	19:36:04.237972+0800	hootowl	Received state update for 37078 (app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>, unknown-NotVisible
default	19:36:04.383553+0800	hootowl	<UIWindowScene: 0x10c450200> (1B8F959F-618F-4A0D-AD89-E09DEC0EAB34) Scene updated orientation preferences: ( Pu ) -> ( Pu Ll Lr )
default	19:36:04.605153+0800	hootowl	TX focusApplication (peekAppEvent) stealKB:Y scene:com.sharkda.hootowl-1B8F959F-618F-4A0D-AD89-E09DEC0EAB34
default	19:36:04.605196+0800	hootowl	Evaluating dispatch of UIEvent: 0x139100a00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:04.606081+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	19:36:04.606139+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:04.611841+0800	hootowl	[0x11ad1bac0] activating connection: mach=true listener=false peer=false name=com.apple.DragUI.druid.source
default	19:36:04.634047+0800	hootowl	_UIInternalDraggingSessionSource: Drag session state changing from New to Connecting
default	19:36:04.634176+0800	hootowl	[0x11ad19180] activating connection: mach=true listener=false peer=false name=com.apple.DragUI.druid.source
default	19:36:04.634376+0800	hootowl	_UIDruidSourceConnection beginDragWithTouches:items:completion:
default	19:36:04.635462+0800	hootowl	[0x11ad183c0] activating connection: mach=false listener=true peer=false name=(anonymous)
default	19:36:04.635502+0800	hootowl	[0x11ad183c0] Connection returned listener port: 0xc813
default	19:36:04.637456+0800	hootowl	Evaluating dispatch of UIEvent: 0x139100a00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:04.646245+0800	hootowl	_UIDruidSourceConnection beginDragWithTouches:items:completion: got replyHandler with sessionID 2941674395
default	19:36:04.646445+0800	hootowl	_UIInternalDraggingSessionSource: Drag session state changing from Connecting to Dragging
default	19:36:04.664575+0800	hootowl	Evaluating dispatch of UIEvent: 0x139100a00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:04.664829+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	19:36:04.665234+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:04.665855+0800	hootowl	_UIDruidSourceConnection requestDragPreviewsForIndexSet:reply: <NSMutableIndexSet: 0x139286c40>[number of indexes: 1 (in 1 ranges), indexes: (0)]
default	19:36:04.673022+0800	hootowl	Received state update for 37078 (app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>, unknown-NotVisible
default	19:36:04.674088+0800	hootowl	RX setKeyboardDisabled:Y
default	19:36:04.674235+0800	hootowl	setDeactivatedKeyboard: 1 forScene: (null) forSuppressionAssertion: 0
default	19:36:04.678124+0800	hootowl	Change from input view set: (null)
default	19:36:04.678132+0800	hootowl	Change to input view set: (null)
default	19:36:04.678977+0800	hootowl	_moveGuideOffscreenAtEdge: 4
default	19:36:04.679030+0800	hootowl	changeOffsetConstants: offset is changing to {0, 0} [previous offset: {-1, -1}]
default	19:36:04.679157+0800	hootowl	changeSizingConstants: size is changing [not transitioning] to {393, 0} [previous size: {1, 0}]
default	19:36:04.680198+0800	hootowl	setDeactivatedKeyboard, shouldUpdatePlacement: 1
default	19:36:04.680216+0800	hootowl	setPlacementChangeDisabled: 1, placement: <UITrackingElementPlacementInitialPosition> (self: <UITrackingElementWindowController: 0x10420de00>)
default	19:36:04.680315+0800	hootowl	Moving from placement: <UITrackingElementPlacementInitialPosition> to placement: <UITrackingElementPlacementInitialPosition> (currentPlacement: <UITrackingElementPlacementInitialPosition>)
default	19:36:04.680398+0800	hootowl	KeyboardTrackingCoordinator: Creating tracking coordinator for <UIWindowScene: 0x10c450200; role: UIWindowSceneSessionRoleApplication; persistentIdentifier: 1B8F959F-618F-4A0D-AD89-E09DEC0EAB34; activationState: UISceneActivationStateForegroundActive>
default	19:36:04.881089+0800	hootowl	[0x13a3ead00] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0x11ad183c0.peer[36148].0x13a3ead00
default	19:36:04.882833+0800	hootowl	updatePlacementWithPlacement: <UITrackingElementPlacementInitialPosition>
default	19:36:04.883735+0800	hootowl	KeyboardTrackingCoordinator: Creating tracking provider for <UIWindowScene: 0x10c450200; role: UIWindowSceneSessionRoleApplication; persistentIdentifier: 1B8F959F-618F-4A0D-AD89-E09DEC0EAB34; activationState: UISceneActivationStateForegroundActive>
default	19:36:04.884543+0800	hootowl	Tracking provider: moveFromPlacement: <UITrackingElementPlacementInitialPosition> toPlacement: <UITrackingElementPlacementInitialPosition> update to {{0, 852}, {393, 0}}
default	19:36:04.884641+0800	hootowl	Updating tracking clients for start <TUIKeyboardTrackingCoordinator:0x11ace8500 state=<TUIKeyboardState: 0x12cb7c980 State: offscreen; is docked>; frame={{0, 852}, {393, 0}}; animation=<TUIKeyboardAnimationInfo: 0x13d5c4f00, duration: 0.38, from local keyboard, is not rotating, should animate, type: 0, notificationInfo: {
    UIKeyboardAnimationCurveUserInfoKey = 7;
    UIKeyboardAnimationDurationUserInfoKey = "0.3833";
    UIKeyboardBoundsUserInfoKey = "NSRect: {{0, 0}, {393, 0}}";
    UIKeyboardCenterBeginUserInfoKey = "NSPoint: {196.5, 426}";
    UIKeyboardCenterEndUserInfoKey = "NSPoint: {196.5, 852}";
    UIKeyboardFrameBeginUserInfoKey = "NSRect: {{196.5, 426}, {0, 0}}";
    UIKeyboardFrameEndUserInfoKey = "NSRect: {{0, 852}, {393, 0}}";
    UIKeyboardIsLocalUserInfoKey = 1;
}notificationsDebug: >>
default	19:36:04.885936+0800	hootowl	Received state update for 37078 (app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>, unknown-NotVisible
default	19:36:04.924698+0800	hootowl	Init Service connection: <BSServiceConnectionEndpoint: 0x11acfa2e0; target: NL:com.apple.AccessibilityUIServer; service: com.apple.AccessibilityUIServer>
default	19:36:04.924738+0800	hootowl	[C:4] Alloc com.apple.AccessibilityUIServer
default	19:36:04.924760+0800	hootowl	[0x11ad64280] activating connection: mach=false listener=false peer=false name=(anonymous)
default	19:36:04.928114+0800	hootowl	Connection activated to <BSXPC(com.apple.AccessibilityUIServer[C:4-1])-as(com.apple.AccessibilityUIServer):0x13d5c1e00>
error	19:36:04.930675+0800	hootowl	Got a keyboard will change frame notification, but keyboard was not even present.
error	19:36:04.931173+0800	hootowl	Got a keyboard will hide notification, but keyboard was not even present.
default	19:36:04.935255+0800	hootowl	ClientConnection registered client SpeakThisClientIdentifier-37078
default	19:36:04.937761+0800	hootowl	Posted notification willHide with {
    UIKeyboardAnimationCurveUserInfoKey = 7;
    UIKeyboardAnimationDurationUserInfoKey = "0.3833";
    UIKeyboardBoundsUserInfoKey = "NSRect: {{0, 0}, {393, 0}}";
    UIKeyboardCenterBeginUserInfoKey = "NSPoint: {196.5, 426}";
    UIKeyboardCenterEndUserInfoKey = "NSPoint: {196.5, 852}";
    UIKeyboardFrameBeginUserInfoKey = "NSRect: {{196.5, 426}, {0, 0}}";
    UIKeyboardFrameEndUserInfoKey = "NSRect: {{0, 852}, {393, 0}}";
    UIKeyboardIsLocalUserInfoKey = 1;
} (null)
default	19:36:04.938041+0800	hootowl	App is being debugged, do not track this hang
default	19:36:04.938199+0800	hootowl	Hang detected: 0.26s (debugger attached, not reporting)
default	19:36:04.942186+0800	hootowl	Requesting calls from host
default	19:36:04.942327+0800	hootowl	Remote touch surface type has been initialized to: Unknown
default	19:36:04.942404+0800	hootowl	Remote microphone capability has been initialized to: NO
default	19:36:04.944256+0800	hootowl	[0x11ad65e00] activating connection: mach=true listener=false peer=false name=com.apple.callkit.callcontrollerhost
default	19:36:04.947354+0800	hootowl	nw_path_evaluator_start [B7A53684-7F0F-43BB-8966-A8AEDB5780CC <NULL> generic, multipath service: handover, attribution: developer]
	path: satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good
default	19:36:04.947720+0800	hootowl	[0x11ad66800] activating connection: mach=true listener=false peer=false name=com.apple.SystemConfiguration.NetworkInformation
default	19:36:04.948328+0800	hootowl	Received requested calls from host: (
)
default	19:36:04.952363+0800	hootowl	[0x11ad66e40] activating connection: mach=true listener=false peer=false name=com.apple.TextInput
default	19:36:05.064285+0800	hootowl	<_UIKBFeedbackGenerator: 0x13d5015c0>: Updating mode. Haptics: supported. Haptics: enabled. Ringer: on. Sound: disabled. Mode: haptics only
default	19:36:05.065391+0800	hootowl	-[UIDictationController setIgnoreFinalizePhrases:] Setting ignoreFinalizePhrases flag 1
default	19:36:05.065551+0800	hootowl	Posted notification didHide with {
    UIKeyboardAnimationCurveUserInfoKey = 7;
    UIKeyboardAnimationDurationUserInfoKey = "0.3833";
    UIKeyboardBoundsUserInfoKey = "NSRect: {{0, 0}, {393, 0}}";
    UIKeyboardCenterBeginUserInfoKey = "NSPoint: {196.5, 426}";
    UIKeyboardCenterEndUserInfoKey = "NSPoint: {196.5, 852}";
    UIKeyboardFrameBeginUserInfoKey = "NSRect: {{196.5, 426}, {0, 0}}";
    UIKeyboardFrameEndUserInfoKey = "NSRect: {{0, 852}, {393, 0}}";
    UIKeyboardIsLocalUserInfoKey = 1;
} (null)
default	19:36:05.072413+0800	hootowl	[0x11ad67ac0] activating connection: mach=true listener=false peer=false name=com.apple.DragUI.druid.destination
default	19:36:05.072659+0800	hootowl	Evaluating dispatch of UIEvent: 0x11acdcd00; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:05.072829+0800	hootowl	Evaluating dispatch of UIEvent: 0x11acdcd00; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:05.073261+0800	hootowl	_UIDruidDestinationConnection: sawFirstDragEvent reply with session <_NSXPCDistantObject: 0x13d5c25d0>
default	19:36:05.075706+0800	hootowl	_UIInternalDraggingSessionDestination: State changing from Connecting to Dragging
default	19:36:05.080468+0800	hootowl	_UIDruidDestinationConnection takePotentialDrop:<_DUIPotentialDrop 0x139287e40: operation=16 forbidden=0 precise=0 prefersFullSizePreview=1 preferredBadgeStyle=0>
default	19:36:05.081253+0800	hootowl	Evaluating dispatch of UIEvent: 0x11acdcd00; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:05.081724+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	19:36:05.081748+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:05.081867+0800	hootowl	Evaluating dispatch of UIEvent: 0x11acdcd00; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:05.082350+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	19:36:05.082484+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:05.085899+0800	hootowl	Evaluating dispatch of UIEvent: 0x11acdcd00; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:05.086111+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	19:36:05.086220+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:05.089210+0800	hootowl	Evaluating dispatch of UIEvent: 0x11acdcd00; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:05.089653+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	19:36:05.090387+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:05.091887+0800	hootowl	Evaluating dispatch of UIEvent: 0x11acdcd00; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:05.091907+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	19:36:05.091921+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:05.094239+0800	hootowl	Evaluating dispatch of UIEvent: 0x11acdcd00; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:05.094391+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	19:36:05.094849+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:05.100070+0800	hootowl	Evaluating dispatch of UIEvent: 0x11acdcd00; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:05.100442+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	19:36:05.100477+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:05.108158+0800	hootowl	Evaluating dispatch of UIEvent: 0x11acdcd00; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:05.108262+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	19:36:05.108338+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:05.111573+0800	hootowl	Received state update for 37078 (app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>, unknown-NotVisible
default	19:36:05.116538+0800	hootowl	Evaluating dispatch of UIEvent: 0x11acdcd00; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:05.116553+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	19:36:05.116622+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:05.124982+0800	hootowl	Evaluating dispatch of UIEvent: 0x11acdcd00; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:05.125231+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	19:36:05.125246+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:05.133409+0800	hootowl	Evaluating dispatch of UIEvent: 0x11acdcd00; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:05.133423+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	19:36:05.133430+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:05.141664+0800	hootowl	Evaluating dispatch of UIEvent: 0x11acdcd00; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:05.141690+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	19:36:05.141721+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:05.149883+0800	hootowl	Evaluating dispatch of UIEvent: 0x11acdcd00; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:05.149888+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	19:36:05.149893+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:05.158107+0800	hootowl	Evaluating dispatch of UIEvent: 0x11acdcd00; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:05.158124+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	19:36:05.158488+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:05.166539+0800	hootowl	Evaluating dispatch of UIEvent: 0x11acdcd00; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:05.166546+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	19:36:05.166551+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:05.173711+0800	hootowl	RX keyboardChangeCompleted
default	19:36:05.174990+0800	hootowl	Evaluating dispatch of UIEvent: 0x11acdcd00; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:05.175076+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	19:36:05.175250+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:05.177231+0800	hootowl	Received state update for 37078 (app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>, unknown-NotVisible
default	19:36:05.183094+0800	hootowl	Evaluating dispatch of UIEvent: 0x11acdcd00; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:05.183096+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	19:36:05.183099+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:05.191562+0800	hootowl	Evaluating dispatch of UIEvent: 0x11acdcd00; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:05.191728+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	19:36:05.191781+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:05.200159+0800	hootowl	Evaluating dispatch of UIEvent: 0x11acdcd00; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:05.200177+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	19:36:05.200198+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:05.208548+0800	hootowl	Evaluating dispatch of UIEvent: 0x11acdcd00; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:05.208583+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	19:36:05.208607+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:05.217133+0800	hootowl	Evaluating dispatch of UIEvent: 0x11acdcd00; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:05.217153+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	19:36:05.217175+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:05.224836+0800	hootowl	Evaluating dispatch of UIEvent: 0x11acdcd00; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:05.224875+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	19:36:05.224895+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:05.233886+0800	hootowl	Evaluating dispatch of UIEvent: 0x11acdcd00; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:05.233931+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	19:36:05.237911+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:05.238367+0800	hootowl	activate generator with style: TurnOn; activationCount: 0 -> 1; styleActivationCount: 0 -> 1; <_UIDragSnappingFeedbackGenerator: 0x12cbf0000>
default	19:36:05.238418+0800	hootowl	activate generator with style: TurnOn; activationCount: 1 -> 2; styleActivationCount: 1 -> 2; <_UIDragSnappingFeedbackGenerator: 0x12cbf0000>
default	19:36:05.238442+0800	hootowl	activate engine <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c01a280>, clientCount: 0 -> 1
default	19:36:05.238507+0800	hootowl	activating engine <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c01a280>
default	19:36:05.239998+0800	hootowl	engine <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c01a280> state changed: Inactive -> Activating
default	19:36:05.240217+0800	hootowl	starting core haptics engine for <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c01a280>
default	19:36:05.240283+0800	hootowl	        CHHapticEngine.mm:1302  -[CHHapticEngine startWithCompletionHandler:]: Called on engine 0x1391372c0
default	19:36:05.240360+0800	hootowl	        CHHapticEngine.mm:1251  -[CHHapticEngine doStartWithCompletionHandler:]: Starting underlying Haptic Player
default	19:36:05.240377+0800	hootowl	        CHHapticEngine.mm:885   -[CHHapticEngine updateEngineBehaviorWithError:]: Setting player's behavior to 0x5
default	19:36:05.240478+0800	hootowl	        AVHapticPlayer.mm:323   -[AVHapticPlayer setBehavior:error:]: clientID: 0x20090d6 behavior: 5
default	19:36:05.240504+0800	hootowl	        AVHapticPlayer.mm:675   -[AVHapticPlayer startRunningWithCompletionHandler:]: start running: clientID: 0x20090d6
default	19:36:05.240535+0800	hootowl	        AVHapticClient.mm:363   -[AVHapticClient startRunning:]: Client 0x20090d6 starting
default	19:36:05.245027+0800	hootowl	playing feedback without gesture recognizer (<nil: 0x0>) or at null point
default	19:36:05.245048+0800	hootowl	activate generator with style: TurnOn; activationCount: 2 -> 3; styleActivationCount: 2 -> 3; <_UIDragSnappingFeedbackGenerator: 0x12cbf0000>
default	19:36:05.245158+0800	hootowl	generator <_UIDragSnappingFeedbackGenerator: 0x12cbf0000> cannot play feedback <nil: 0x0> (enabled=1)
default	19:36:05.246547+0800	hootowl	Evaluating dispatch of UIEvent: 0x11acdcd00; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:05.246577+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	19:36:05.246588+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:05.249785+0800	hootowl	Evaluating dispatch of UIEvent: 0x11acdcd00; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:05.249794+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	19:36:05.249802+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:05.250183+0800	hootowl	generator <_UIDragSnappingFeedbackGenerator: 0x12cbf0000> cannot play feedback <nil: 0x0> (enabled=1)
default	19:36:05.258218+0800	hootowl	Evaluating dispatch of UIEvent: 0x11acdcd00; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:05.258295+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	19:36:05.258375+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:05.265165+0800	hootowl	core haptics engine STARTED for <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c01a280>
default	19:36:05.265224+0800	hootowl	engine <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c01a280> state changed: Activating -> Running
default	19:36:05.265288+0800	hootowl	playing feedback without gesture recognizer (<nil: 0x0>) or at null point
default	19:36:05.265295+0800	hootowl	activate generator with style: TurnOn; activationCount: 3 -> 4; styleActivationCount: 3 -> 4; <_UIDragSnappingFeedbackGenerator: 0x12cbf0000>
default	19:36:05.265304+0800	hootowl	deactivate generator with style: TurnOn; activationCount: 4 -> 3; styleActivationCount: 4 -> 3; <_UIDragSnappingFeedbackGenerator: 0x12cbf0000>
default	19:36:05.265316+0800	hootowl	generator <_UIDragSnappingFeedbackGenerator: 0x12cbf0000> playing feedback <_UIFeedbackPattern: 0x13d5ad540>
default	19:36:05.265322+0800	hootowl	player dequeue needed - initial request for feedback <_UIFeedbackPattern: 0x13d5ad540>
default	19:36:05.265480+0800	hootowl	player dequeue finished for feedback <_UIFeedbackPattern: 0x13d5ad540> with player <_UIFeedbackCoreHapticsPlayer: 0x13d58a730>
default	19:36:05.265546+0800	hootowl	generator <_UIDragSnappingFeedbackGenerator: 0x12cbf0000> playing feedback <_UIDiscreteFeedback: 0x13d5ad5e0>
default	19:36:05.269452+0800	hootowl	deactivate generator with style: TurnOn; activationCount: 3 -> 2; styleActivationCount: 3 -> 2; <_UIDragSnappingFeedbackGenerator: 0x12cbf0000>
default	19:36:05.269925+0800	hootowl	deactivate generator with style: TurnOn; activationCount: 2 -> 1; styleActivationCount: 2 -> 1; <_UIDragSnappingFeedbackGenerator: 0x12cbf0000>
default	19:36:05.270514+0800	hootowl	        AVHapticPlayer.mm:150   -[AVHapticPlayerChannel resetAtTime:error:]: sending reset event: clientID: 0x20090d6 time: 643617.359
default	19:36:05.270533+0800	hootowl	        AVHapticPlayer.mm:91    -[AVHapticPlayerChannel sendEvents:atTime:error:]: sending event array: clientID: 0x20090d6 atTime: 643617.359
default	19:36:05.270569+0800	hootowl	        AVHapticPlayer.mm:762   -[AVHapticPlayer finishWithCompletionHandler:]: finish with comp handler: clientID: 0x20090d6
default	19:36:05.270585+0800	hootowl	        AVHapticClient.mm:421   -[AVHapticClient finish:]: Client 0x20090d6 finishing
default	19:36:05.270603+0800	hootowl	        AVHapticClient.mm:426   -[AVHapticClient finish:]_block_invoke: completionCallback set to 0x11aff8f30
default	19:36:05.270632+0800	hootowl	        AVHapticClient.mm:453   -[AVHapticClient finish:]: Client 0x20090d6 done with finish
default	19:36:05.270720+0800	hootowl	player dequeue needed - initial request for feedback <_UIDiscreteFeedback: 0x13d5ad5e0>
default	19:36:05.270817+0800	hootowl	played feedback <_UIFeedbackPattern: 0x13d5ad540> with engine <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c01a280> at time 643617.358542
default	19:36:05.270838+0800	hootowl	player dequeue finished for feedback <_UIDiscreteFeedback: 0x13d5ad5e0> with player <_UIFeedbackCoreHapticsPlayer: 0x13d58a9a0>
default	19:36:05.271105+0800	hootowl	Evaluating dispatch of UIEvent: 0x11acdcd00; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:05.271116+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	19:36:05.271549+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:05.271943+0800	hootowl	        AVHapticPlayer.mm:150   -[AVHapticPlayerChannel resetAtTime:error:]: sending reset event: clientID: 0x20090d6 time: 643617.359
default	19:36:05.271987+0800	hootowl	        AVHapticPlayer.mm:91    -[AVHapticPlayerChannel sendEvents:atTime:error:]: sending event array: clientID: 0x20090d6 atTime: 643617.359
default	19:36:05.272224+0800	hootowl	        AVHapticPlayer.mm:762   -[AVHapticPlayer finishWithCompletionHandler:]: finish with comp handler: clientID: 0x20090d6
default	19:36:05.272314+0800	hootowl	        AVHapticClient.mm:421   -[AVHapticClient finish:]: Client 0x20090d6 finishing
default	19:36:05.272336+0800	hootowl	generator <_UIDragSnappingFeedbackGenerator: 0x12cbf0000> cannot play feedback <nil: 0x0> (enabled=1)
default	19:36:05.272350+0800	hootowl	        AVHapticClient.mm:426   -[AVHapticClient finish:]_block_invoke: completionCallback set to 0x11affb1b0
default	19:36:05.272377+0800	hootowl	        AVHapticClient.mm:453   -[AVHapticClient finish:]: Client 0x20090d6 done with finish
default	19:36:05.275779+0800	hootowl	played feedback <_UIDiscreteFeedback: 0x13d5ad5e0> with engine <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c01a280> at time 643617.358852
default	19:36:05.275950+0800	hootowl	Evaluating dispatch of UIEvent: 0x11acdcd00; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:05.275988+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	19:36:05.282201+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:05.293400+0800	hootowl	Evaluating dispatch of UIEvent: 0x11acdcd00; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:05.293406+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	19:36:05.293427+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:05.295255+0800	hootowl	generator <_UIDragSnappingFeedbackGenerator: 0x12cbf0000> cannot play feedback <nil: 0x0> (enabled=1)
default	19:36:05.296185+0800	hootowl	Evaluating dispatch of UIEvent: 0x11acdcd00; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:05.296205+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	19:36:05.303992+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:05.304744+0800	hootowl	Evaluating dispatch of UIEvent: 0x11acdcd00; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:05.304788+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	19:36:05.305146+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:05.305247+0800	hootowl	generator <_UIDragSnappingFeedbackGenerator: 0x12cbf0000> cannot play feedback <nil: 0x0> (enabled=1)
default	19:36:05.308275+0800	hootowl	Evaluating dispatch of UIEvent: 0x11acdcd00; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:05.308418+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	19:36:05.309587+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:05.315562+0800	hootowl	Received state update for 37078 (app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>, unknown-NotVisible
default	19:36:05.316796+0800	hootowl	Evaluating dispatch of UIEvent: 0x11acdcd00; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:05.316834+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	19:36:05.317678+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:05.318094+0800	hootowl	generator <_UIDragSnappingFeedbackGenerator: 0x12cbf0000> cannot play feedback <nil: 0x0> (enabled=1)
default	19:36:05.324935+0800	hootowl	Evaluating dispatch of UIEvent: 0x11acdcd00; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:05.325087+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	19:36:05.325094+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:05.327636+0800	hootowl	        AVHapticClient.mm:1472  -[AVHapticClient clientCompletedWithError:]: Client-side (async) finish completion callback for client 0x20090d6 called from server
default	19:36:05.327646+0800	hootowl	        AVHapticClient.mm:1477  -[AVHapticClient clientCompletedWithError:]_block_invoke: Async dispatch: preparing to call completionCallback for client 0x20090d6
default	19:36:05.327666+0800	hootowl	        AVHapticClient.mm:1479  -[AVHapticClient clientCompletedWithError:]_block_invoke: Calling completionCallback 0x11affb1b0 and then setting to nil
default	19:36:05.333590+0800	hootowl	Evaluating dispatch of UIEvent: 0x11acdcd00; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:05.333807+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	19:36:05.336131+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:05.336524+0800	hootowl	generator <_UIDragSnappingFeedbackGenerator: 0x12cbf0000> cannot play feedback <nil: 0x0> (enabled=1)
default	19:36:05.389767+0800	hootowl	Evaluating dispatch of UIEvent: 0x11acdcd00; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:05.389831+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	19:36:05.389846+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:05.389965+0800	hootowl	generator <_UIDragSnappingFeedbackGenerator: 0x12cbf0000> cannot play feedback <nil: 0x0> (enabled=1)
default	19:36:05.399806+0800	hootowl	generator <_UIDragSnappingFeedbackGenerator: 0x12cbf0000> cannot play feedback <nil: 0x0> (enabled=1)
default	19:36:05.416618+0800	hootowl	generator <_UIDragSnappingFeedbackGenerator: 0x12cbf0000> cannot play feedback <nil: 0x0> (enabled=1)
default	19:36:05.439501+0800	hootowl	Evaluating dispatch of UIEvent: 0x11acdcd00; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:05.439577+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	19:36:05.440074+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:05.441310+0800	hootowl	generator <_UIDragSnappingFeedbackGenerator: 0x12cbf0000> cannot play feedback <nil: 0x0> (enabled=1)
default	19:36:05.442950+0800	hootowl	Evaluating dispatch of UIEvent: 0x11acdcd00; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:05.442992+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	19:36:05.443593+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:05.449819+0800	hootowl	generator <_UIDragSnappingFeedbackGenerator: 0x12cbf0000> cannot play feedback <nil: 0x0> (enabled=1)
default	19:36:05.458429+0800	hootowl	Evaluating dispatch of UIEvent: 0x11acdcd00; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:05.458451+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	19:36:05.460084+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:05.466600+0800	hootowl	Evaluating dispatch of UIEvent: 0x11acdcd00; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:05.466610+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	19:36:05.466619+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:05.467228+0800	hootowl	generator <_UIDragSnappingFeedbackGenerator: 0x12cbf0000> cannot play feedback <nil: 0x0> (enabled=1)
default	19:36:05.486943+0800	hootowl	generator <_UIDragSnappingFeedbackGenerator: 0x12cbf0000> cannot play feedback <nil: 0x0> (enabled=1)
default	19:36:05.500539+0800	hootowl	generator <_UIDragSnappingFeedbackGenerator: 0x12cbf0000> cannot play feedback <nil: 0x0> (enabled=1)
default	19:36:05.516592+0800	hootowl	generator <_UIDragSnappingFeedbackGenerator: 0x12cbf0000> cannot play feedback <nil: 0x0> (enabled=1)
default	19:36:05.549088+0800	hootowl	Evaluating dispatch of UIEvent: 0x11acdcd00; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:05.549181+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	19:36:05.549206+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:05.549324+0800	hootowl	Evaluating dispatch of UIEvent: 0x11acdcd00; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:05.549334+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	19:36:05.549350+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:05.549468+0800	hootowl	_UIDruidDestinationConnection requestDropWithOperation:16
default	19:36:05.549485+0800	hootowl	_UIDruidDestinationConnection sawDragEndEvent
default	19:36:05.549839+0800	hootowl	_UIInternalDraggingSessionDestination: State changing from Dragging to Ending
default	19:36:05.550040+0800	hootowl	generator <_UIDragSnappingFeedbackGenerator: 0x12cbf0000> cannot play feedback <nil: 0x0> (enabled=1)
default	19:36:05.550272+0800	hootowl	_UIDruidDestinationConnection performDropWithItemCollection:...
default	19:36:05.550285+0800	hootowl	_UIInternalDraggingSessionDestination: State changing from Ending to Dropped
default	19:36:05.550539+0800	hootowl	_UIDruidDestinationConnection performDropWithItemCollection: calling dropPerformBlock
default	19:36:05.551826+0800	hootowl	deactivate generator with style: TurnOn; activationCount: 1 -> 0; styleActivationCount: 1 -> 0; <_UIDragSnappingFeedbackGenerator: 0x12cbf0000>
default	19:36:05.551853+0800	hootowl	deactivate engine <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c01a280>, clientCount: 1 -> 0
default	19:36:05.551863+0800	hootowl	_internal_deactivateEngineIfPossible <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c01a280>, clientCount: 0, suspended: 0
default	19:36:05.552436+0800	hootowl	_internal_teardownUnderlyingPlayerIfPossible <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c01a280>
default	19:36:05.552697+0800	hootowl	engine <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c01a280> state changed: Running -> Deactivating
default	19:36:05.553134+0800	hootowl	        CHHapticEngine.mm:1461  -[CHHapticEngine notifyWhenPlayersFinished:]: Called on engine 0x1391372c0 with finishedHandler 0x13b084bc0
default	19:36:05.553333+0800	hootowl	        AVHapticPlayer.mm:762   -[AVHapticPlayer finishWithCompletionHandler:]: finish with comp handler: clientID: 0x20090d6
default	19:36:05.553354+0800	hootowl	        AVHapticClient.mm:421   -[AVHapticClient finish:]: Client 0x20090d6 finishing
default	19:36:05.553380+0800	hootowl	        AVHapticClient.mm:426   -[AVHapticClient finish:]_block_invoke: completionCallback set to 0x11bd394d0
default	19:36:05.553394+0800	hootowl	        AVHapticClient.mm:453   -[AVHapticClient finish:]: Client 0x20090d6 done with finish
default	19:36:05.553462+0800	hootowl	        AVHapticClient.mm:1472  -[AVHapticClient clientCompletedWithError:]: Client-side (async) finish completion callback for client 0x20090d6 called from server
default	19:36:05.553478+0800	hootowl	        AVHapticClient.mm:1477  -[AVHapticClient clientCompletedWithError:]_block_invoke: Async dispatch: preparing to call completionCallback for client 0x20090d6
default	19:36:05.553502+0800	hootowl	        AVHapticClient.mm:1479  -[AVHapticClient clientCompletedWithError:]_block_invoke: Calling completionCallback 0x11bd394d0 and then setting to nil
default	19:36:05.554263+0800	hootowl	core haptics engine finished for <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c01a280>
default	19:36:05.554270+0800	hootowl	stopping core haptics engine for <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c01a280>
default	19:36:05.554286+0800	hootowl	        CHHapticEngine.mm:1439  -[CHHapticEngine stopWithCompletionHandler:]: Called on engine 0x1391372c0
default	19:36:05.554776+0800	hootowl	        CHHapticEngine.mm:1403  -[CHHapticEngine doStopWithCompletionHandler:]: Stopping underlying Haptic Player
default	19:36:05.555372+0800	hootowl	_internal_deactivateEngineIfPossible <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c01a280> tearedDown: 1
default	19:36:05.555722+0800	hootowl	        AVHapticPlayer.mm:739   -[AVHapticPlayer stopRunningWithCompletionHandler:]: stop running: clientID: 0x20090d6
default	19:36:05.555751+0800	hootowl	engine <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c01a280> state changed: Deactivating -> Inactive
default	19:36:05.555768+0800	hootowl	        AVHapticClient.mm:398   -[AVHapticClient stopRunning:]: Client 0x20090d6 stopping
default	19:36:05.557615+0800	hootowl	Municipal+Cyclops 93
🎨 model refreshed — obs:117s car:18 thread:main
default	19:36:05.558878+0800	hootowl	        AVHapticClient.mm:1472  -[AVHapticClient clientCompletedWithError:]: Client-side (async) finish completion callback for client 0x20090d6 called from server
default	19:36:05.558898+0800	hootowl	        AVHapticClient.mm:1477  -[AVHapticClient clientCompletedWithError:]_block_invoke: Async dispatch: preparing to call completionCallback for client 0x20090d6
default	19:36:05.559088+0800	hootowl	        AVHapticClient.mm:1484  -[AVHapticClient clientCompletedWithError:]_block_invoke: strongSelf.completionCallback is nil
default	19:36:05.572906+0800	hootowl	core haptics engine STOPPED for <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c01a280>
default	19:36:05.572931+0800	hootowl	_UIDruidDestinationConnection performDropWithItemCollection: sending reply to druid
default	19:36:05.572962+0800	hootowl	RX setKeyboardDisabled:N
default	19:36:05.572971+0800	hootowl	setDeactivatedKeyboard: 0 forScene: (null) forSuppressionAssertion: 0
default	19:36:05.572978+0800	hootowl	setDeactivatedKeyboard, shouldUpdatePlacement: 1
default	19:36:05.572988+0800	hootowl	setPlacementChangeDisabled: 0, placement: <UITrackingElementPlacementInitialPosition> (self: <UITrackingElementWindowController: 0x10420de00>)
default	19:36:05.573029+0800	hootowl	Moving from placement: <UITrackingElementPlacementInitialPosition> to placement: <UITrackingElementPlacementInitialPosition> (currentPlacement: <UITrackingElementPlacementInitialPosition>)
default	19:36:05.573240+0800	hootowl	updatePlacementWithPlacement: <UITrackingElementPlacementInitialPosition>
default	19:36:05.573520+0800	hootowl	Tracking provider: moveFromPlacement: <UITrackingElementPlacementInitialPosition> toPlacement: <UITrackingElementPlacementInitialPosition> update to {{0, 852}, {393, 0}}
default	19:36:05.573576+0800	hootowl	_UIDruidDestinationConnection handOffDroppedItems:withFence:completion:
default	19:36:05.573606+0800	hootowl	Updating tracking clients for start <TUIKeyboardTrackingCoordinator:0x11ace8500 state=<TUIKeyboardState: 0x1393f6320 State: offscreen; is docked>; frame={{0, 852}, {393, 0}}; animation=<TUIKeyboardAnimationInfo: 0x13d5c6b00, duration: 0.38, from local keyboard, is not rotating, should animate, type: 0, notificationInfo: {
    UIKeyboardAnimationCurveUserInfoKey = 7;
    UIKeyboardAnimationDurationUserInfoKey = "0.3833";
    UIKeyboardBoundsUserInfoKey = "NSRect: {{0, 0}, {393, 0}}";
    UIKeyboardCenterBeginUserInfoKey = "NSPoint: {196.5, 852}";
    UIKeyboardCenterEndUserInfoKey = "NSPoint: {196.5, 852}";
    UIKeyboardFrameBeginUserInfoKey = "NSRect: {{0, 852}, {393, 0}}";
    UIKeyboardFrameEndUserInfoKey = "NSRect: {{0, 852}, {393, 0}}";
    UIKeyboardIsLocalUserInfoKey = 1;
}notificationsDebug: >>
default	19:36:05.573628+0800	hootowl	_UIDruidDestinationConnection: dragEnded
default	19:36:05.573679+0800	hootowl	_UIDruidSourceConnection dragEndedWithOperation:16
default	19:36:05.575061+0800	hootowl	_UIInternalDraggingSessionDestination: State changing from Dropped to Ended
default	19:36:05.579310+0800	hootowl	MncplCyclopsScreen 66
🏠 body eval — items:6 firstObs:117s firstCar:18
default	19:36:05.600099+0800	hootowl	[(FBSceneManager):sceneID:com.sharkda.hootowl-1B8F959F-618F-4A0D-AD89-E09DEC0EAB34] Sending action(s): BLSInvalidateFrameSpecifiersAction
default	19:36:05.607645+0800	hootowl	Received state update for 37078 (app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>, unknown-NotVisible
default	19:36:05.615324+0800	hootowl	_UIInternalDraggingSessionSource: Drag session state changing from Dragging to Dropped
default	19:36:05.669449+0800	hootowl	Received state update for 37078 (app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>, unknown-NotVisible
default	19:36:06.639105+0800	hootowl	Data transfer finished for dragging session destination 0x11ad67e80
default	19:36:06.645814+0800	hootowl	[0x11ad19180] Re-initialization successful; calling out to event handler with XPC_ERROR_CONNECTION_INTERRUPTED
default	19:36:06.645828+0800	hootowl	[0x11ad19180] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	19:36:06.645843+0800	hootowl	_UIDruidSourceConnection connection invalidated
default	19:36:06.645859+0800	hootowl	[0x11ad67ac0] Re-initialization successful; calling out to event handler with XPC_ERROR_CONNECTION_INTERRUPTED
default	19:36:06.646296+0800	hootowl	[0x11ad67ac0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	19:36:06.648727+0800	hootowl	_UIDruidDestinationConnection connection invalidated
default	19:36:06.649275+0800	hootowl	Data transfer began for dragging session destination 0x11ad67e80
default	19:36:06.649312+0800	hootowl	[0x13a3ead00] invalidated because the client process (pid 36148) either cancelled the connection or exited
default	19:36:06.649524+0800	hootowl	[0x11ad183c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	19:36:06.750662+0800	hootowl	Received state update for 37078 (app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>, unknown-NotVisible
default	19:36:08.440325+0800	hootowl	TX focusApplication (peekAppEvent) stealKB:Y scene:com.sharkda.hootowl-1B8F959F-618F-4A0D-AD89-E09DEC0EAB34
default	19:36:08.440362+0800	hootowl	Evaluating dispatch of UIEvent: 0x139100a00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:08.440395+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	19:36:08.440429+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:08.475615+0800	hootowl	Evaluating dispatch of UIEvent: 0x139100a00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:08.505575+0800	hootowl	Task <A51C842C-C6FA-4870-B8F6-C29C99ABFDBF>.<30> resuming, timeouts(60.0, 604800.0) qos(0x15) voucher((null)) activity(00000000-0000-0000-0000-000000000000)
default	19:36:08.510587+0800	hootowl	Connection 0: creating secure tcp or quic connection
default	19:36:08.510812+0800	hootowl	Connection 37: enabling TLS
default	19:36:08.510845+0800	hootowl	Connection 37: starting, TC(0x0)
default	19:36:08.510880+0800	hootowl	[C37 AF8AC90D-82BC-468C-A095-B836DE925C77 tcgbusfs.blob.core.windows.net:443 quic-connection, url: https://tcgbusfs.blob.core.windows.net/blobtcmsv/TCMSV_allavailable.json, definite, attribution: developer, context: com.apple.CFNetwork.NSURLSession.{4EE848AE-A5DC-4E55-A08E-E23FD8E7E021}{(null)}{Y}{2}{0x0} (private), proc: 1B526020-2DE0-3C65-9122-F1177549D69A, delegated upid: 0] start
default	19:36:08.510917+0800	hootowl	[C37 tcgbusfs.blob.core.windows.net:443 initial parent-flow ((null))] event: path:start @0.000s
default	19:36:08.512758+0800	hootowl	[C37 tcgbusfs.blob.core.windows.net:443 waiting parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.001s, uuid: AA57BA89-62CC-426D-BA32-5AA6E1BAC468
default	19:36:08.513051+0800	hootowl	[C37 tcgbusfs.blob.core.windows.net:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_connect @0.001s
default	19:36:08.513060+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C37] reporting state preparing
default	19:36:08.513113+0800	hootowl	[C37 tcgbusfs.blob.core.windows.net:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_child @0.002s
default	19:36:08.513258+0800	hootowl	[C37.1 tcgbusfs.blob.core.windows.net:443 initial path ((null))] event: path:start @0.002s
default	19:36:08.513427+0800	hootowl	[C37.1 tcgbusfs.blob.core.windows.net:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.002s, uuid: AA57BA89-62CC-426D-BA32-5AA6E1BAC468
default	19:36:08.513505+0800	hootowl	[C37.1 tcgbusfs.blob.core.windows.net:443 in_progress transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: transform:start @0.002s
default	19:36:08.513586+0800	hootowl	[C37.1.1 tcgbusfs.blob.core.windows.net:443 initial path ((null))] event: path:start @0.002s
default	19:36:08.514031+0800	hootowl	[C37.1.1 tcgbusfs.blob.core.windows.net:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.002s, uuid: BAE3676D-81C2-4A94-A91C-A2E533757DAA
default	19:36:08.514152+0800	hootowl	[C37.1.1 tcgbusfs.blob.core.windows.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:start_dns @0.003s
default	19:36:08.514182+0800	hootowl	Task <A51C842C-C6FA-4870-B8F6-C29C99ABFDBF>.<30> setting up Connection 37
default	19:36:08.525594+0800	hootowl	Evaluating dispatch of UIEvent: 0x139100a00; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	19:36:08.525612+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	19:36:08.525623+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1041f0800>; contextId: 0xB8FA928D
default	19:36:08.526524+0800	hootowl	Evaluating dispatch of UIEvent: 0x139100a00; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 1
default	19:36:08.530519+0800	hootowl	<UIWindowScene: 0x10c450200> (1B8F959F-618F-4A0D-AD89-E09DEC0EAB34) Scene updated orientation preferences: ( Pu Ll Lr ) -> ( Pu )
default	19:36:08.571050+0800	hootowl	nw_endpoint_resolver_update [C37.1.1 tcgbusfs.blob.core.windows.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Adding endpoint handler for 20.150.22.100:443
default	19:36:08.571140+0800	hootowl	[C37.1.1 tcgbusfs.blob.core.windows.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:receive_dns @0.059s
default	19:36:08.571373+0800	hootowl	[C37.1.1.1 20.150.22.100:443 initial path ((null))] event: path:start @0.059s
default	19:36:08.572802+0800	hootowl	[C37.1.1.1 20.150.22.100:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.061s, uuid: 1FDAFDC1-0DB8-40A8-A266-40A215410F17
default	19:36:08.572910+0800	hootowl	[C37.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_nexus @0.061s
default	19:36:08.573295+0800	hootowl	[C37.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:receive_nexus @0.062s
default	19:36:08.573611+0800	hootowl	[C37.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_connect @0.062s
default	19:36:08.573946+0800	hootowl	tcp_output [C37.1.1.1:3] flags=[SEC] seq=3491459970, ack=0, win=65535 state=SYN_SENT rcv_nxt=0, snd_una=3491459970
default	19:36:08.581103+0800	hootowl	endInputSession completion is disabled
default	19:36:08.713207+0800	hootowl	tcp_input [C37.1.1.1:3] flags=[S.E] seq=1679972672, ack=3491459971, win=65535 state=SYN_SENT rcv_nxt=0, snd_una=3491459970
default	19:36:08.713393+0800	hootowl	nw_flow_connected [C37.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Transport protocol connected (tcp)
default	19:36:08.713650+0800	hootowl	[C37.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_transport @0.201s
default	19:36:08.713910+0800	hootowl	boringssl_session_apply_protocol_options_for_transport_block_invoke_2(2367) [C37.1.1.1:2][0x11c3fde60] TLS configured [server(0) min_version(0x0303) max_version(0x0304) name(tcgbusfs.blob.core.windows.net) tickets(false) false_start(false) enforce_ev(false) enforce_ats(false) ats_non_pfs_ciphersuite_allowed(false) cc_mode_enforced(false) ech(false) pqtls(true), pake(false) skip_ats_trust(false)]
default	19:36:08.714173+0800	hootowl	boringssl_context_info_handler(2806) [C37.1.1.1:2][0x11c3fde60] Client handshake started
default	19:36:08.714364+0800	hootowl	boringssl_context_info_handler(2823) [C37.1.1.1:2][0x11c3fde60] Client handshake state: TLS client enter_early_data
default	19:36:08.714447+0800	hootowl	boringssl_context_info_handler(2823) [C37.1.1.1:2][0x11c3fde60] Client handshake state: TLS client read_server_hello
default	19:36:08.731302+0800	hootowl	[C37.1.1 tcgbusfs.blob.core.windows.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:receive_dns @0.219s
default	19:36:08.848294+0800	hootowl	boringssl_context_info_handler(2823) [C37.1.1.1:2][0x11c3fde60] Client handshake state: TLS 1.3 client read_hello_retry_request
default	19:36:08.849335+0800	hootowl	boringssl_context_info_handler(2823) [C37.1.1.1:2][0x11c3fde60] Client handshake state: TLS 1.3 client send_second_client_hello
default	19:36:08.849423+0800	hootowl	boringssl_context_info_handler(2823) [C37.1.1.1:2][0x11c3fde60] Client handshake state: TLS 1.3 client read_server_hello
default	19:36:08.949454+0800	hootowl	boringssl_context_info_handler(2823) [C37.1.1.1:2][0x11c3fde60] Client handshake state: TLS 1.3 client read_encrypted_extensions
default	19:36:08.970698+0800	hootowl	boringssl_context_info_handler(2823) [C37.1.1.1:2][0x11c3fde60] Client handshake state: TLS 1.3 client read_certificate_request
default	19:36:08.970715+0800	hootowl	boringssl_context_info_handler(2823) [C37.1.1.1:2][0x11c3fde60] Client handshake state: TLS 1.3 client read_server_certificate
default	19:36:08.970725+0800	hootowl	boringssl_context_info_handler(2823) [C37.1.1.1:2][0x11c3fde60] Client handshake state: TLS 1.3 client read_server_certificate_verify
default	19:36:08.971029+0800	hootowl	boringssl_context_evaluate_trust_async(2249) [C37.1.1.1:2][0x11c3fde60] Performing external trust evaluation
default	19:36:08.971055+0800	hootowl	boringssl_context_evaluate_trust_async_external(2234) [C37.1.1.1:2][0x11c3fde60] Asyncing for external verify block
default	19:36:08.971445+0800	hootowl	Connection 37: asked to evaluate TLS Trust
default	19:36:08.971677+0800	hootowl	Task <A51C842C-C6FA-4870-B8F6-C29C99ABFDBF>.<30> auth completion disp=1 cred=0x0
default	19:36:08.972363+0800	hootowl	(Trust 0x13d4e7e40) No pending evals, starting
default	19:36:08.972435+0800	hootowl	[0x11ae588c0] activating connection: mach=true listener=false peer=false name=com.apple.trustd
default	19:36:08.972620+0800	hootowl	(Trust 0x13d4e7e40) Completed async eval kickoff
default	19:36:08.976677+0800	hootowl	nothing happened to generator for 5 sec, auto-deactivating it with activationCount: 0; <_UIClickPresentationFeedbackGenerator: 0x12cbf1680>
default	19:36:09.030973+0800	hootowl	(Trust 0x13d4e7e40) trustd returned 4
default	19:36:09.040693+0800	hootowl	System Trust Evaluation yielded status(0)
default	19:36:09.042115+0800	hootowl	(Trust 0x13d4e6400) No pending evals, starting
default	19:36:09.048388+0800	hootowl	[0x11ae58a00] activating connection: mach=true listener=false peer=false name=com.apple.trustd
default	19:36:09.048460+0800	hootowl	(Trust 0x13d4e6400) Completed async eval kickoff
default	19:36:09.053911+0800	hootowl	[0x11ae588c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	19:36:09.065820+0800	hootowl	(Trust 0x13d4e6400) trustd returned 4
default	19:36:09.065881+0800	hootowl	Connection 37: TLS Trust result 0
default	19:36:09.066205+0800	hootowl	boringssl_context_evaluate_trust_async_external_block_invoke_3(2148) [C37.1.1.1:2][0x11c3fde60] Returning from external verify block with result: true
default	19:36:09.070931+0800	hootowl	boringssl_context_certificate_verify_callback(2430) [C37.1.1.1:2][0x11c3fde60] Certificate verification result: OK
default	19:36:09.072148+0800	hootowl	boringssl_context_info_handler(2823) [C37.1.1.1:2][0x11c3fde60] Client handshake state: TLS 1.3 client read_server_finished
default	19:36:09.072289+0800	hootowl	boringssl_context_info_handler(2823) [C37.1.1.1:2][0x11c3fde60] Client handshake state: TLS 1.3 client send_end_of_early_data
default	19:36:09.072361+0800	hootowl	boringssl_context_info_handler(2823) [C37.1.1.1:2][0x11c3fde60] Client handshake state: TLS 1.3 client send_client_encrypted_extensions
default	19:36:09.072479+0800	hootowl	boringssl_context_info_handler(2823) [C37.1.1.1:2][0x11c3fde60] Client handshake state: TLS 1.3 client send_client_certificate
default	19:36:09.072510+0800	hootowl	boringssl_context_info_handler(2823) [C37.1.1.1:2][0x11c3fde60] Client handshake state: TLS 1.3 client complete_second_flight
default	19:36:09.073474+0800	hootowl	boringssl_context_info_handler(2823) [C37.1.1.1:2][0x11c3fde60] Client handshake state: TLS 1.3 client done
default	19:36:09.080425+0800	hootowl	boringssl_context_info_handler(2823) [C37.1.1.1:2][0x11c3fde60] Client handshake state: TLS client finish_client_handshake
default	19:36:09.080471+0800	hootowl	boringssl_context_info_handler(2823) [C37.1.1.1:2][0x11c3fde60] Client handshake state: TLS client done
default	19:36:09.081469+0800	hootowl	boringssl_context_info_handler(2812) [C37.1.1.1:2][0x11c3fde60] Client handshake done
default	19:36:09.084203+0800	hootowl	nw_protocol_boringssl_signal_connected(895) [C37.1.1.1:2][0x11c3fde60] TLS connected [server(0) version(0x0304) ciphersuite(TLS_AES_256_GCM_SHA384) group(0x0018) signature_alg(0x0804) alpn(nil) resumed(0) offered_ticket(0) in_early_data(0) early_data_accepted(0) false_started(0) ocsp_received(1) sct_received(0) connect_time(362ms) flight_time(233ms) rtt(134ms) write_stalls(0) read_stalls(10) pake(0x0000)]
default	19:36:09.089946+0800	hootowl	nw_flow_connected [C37.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (CFNetworkConnection-4160941018)
default	19:36:09.090081+0800	hootowl	[C37.1.1.1 20.150.22.100:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.569s
default	19:36:09.091000+0800	hootowl	[C37.1.1 tcgbusfs.blob.core.windows.net:443 ready resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.569s
default	19:36:09.091125+0800	hootowl	[C37.1 tcgbusfs.blob.core.windows.net:443 ready transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.569s
default	19:36:09.092206+0800	hootowl	[C37.1.1.1 20.150.22.100:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.571s
default	19:36:09.094249+0800	hootowl	[C37.1.1 tcgbusfs.blob.core.windows.net:443 ready resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.571s
default	19:36:09.094269+0800	hootowl	<UIWindowScene: 0x10c450200> (1B8F959F-618F-4A0D-AD89-E09DEC0EAB34) Scene updated orientation preferences: ( Pu ) -> ( Pu Ll Lr )
default	19:36:09.094293+0800	hootowl	[C37.1 tcgbusfs.blob.core.windows.net:443 ready transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.578s
default	19:36:09.094316+0800	hootowl	nw_flow_connected [C37 20.150.22.100:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (endpoint_flow)
default	19:36:09.094371+0800	hootowl	[C37 20.150.22.100:443 ready parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_connect @0.578s
default	19:36:09.094482+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C37] reporting state ready
default	19:36:09.094491+0800	hootowl	[C37 20.150.22.100:443 ready parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.578s
default	19:36:09.094667+0800	hootowl	nw_connection_send_viability_changed_on_nw_queue [C37] viability_changed_handler(true)
default	19:36:09.094707+0800	hootowl	[0x11ae58a00] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	19:36:09.094728+0800	hootowl	Connection 37: connected successfully
default	19:36:09.094743+0800	hootowl	Connection 37: TLS handshake complete
default	19:36:09.094772+0800	hootowl	Connection 37: ready C(N) E(N)
default	19:36:09.094918+0800	hootowl	Task <A51C842C-C6FA-4870-B8F6-C29C99ABFDBF>.<30> now using Connection 37
default	19:36:09.094952+0800	hootowl	Connection 37: received viability advisory(Y)
default	19:36:09.094965+0800	hootowl	Task <A51C842C-C6FA-4870-B8F6-C29C99ABFDBF>.<30> sent request, body N 0
default	19:36:09.512609+0800	hootowl	Task <A51C842C-C6FA-4870-B8F6-C29C99ABFDBF>.<30> received response, status 200 content K
default	19:36:10.190596+0800	hootowl	Task <A51C842C-C6FA-4870-B8F6-C29C99ABFDBF>.<30> response ended
default	19:36:10.190665+0800	hootowl	Task <A51C842C-C6FA-4870-B8F6-C29C99ABFDBF>.<30> done using Connection 37
default	19:36:10.190752+0800	hootowl	[C37] event: client:connection_idle @1.679s
default	19:36:10.190841+0800	hootowl	nw_protocol_tcp_notify [C37.1.1.1:3] nw_protocol_notification_type_connection_idle is true
default	19:36:10.190918+0800	hootowl	Task <A51C842C-C6FA-4870-B8F6-C29C99ABFDBF>.<30> summary for task success {transaction_duration_ms=1684, response_status=200, connection=37, protocol="http/1.1", domain_lookup_duration_ms=56, connect_duration_ms=516, secure_connection_duration_ms=362, private_relay=false, request_start_ms=585, request_duration_ms=0, response_start_ms=1006, response_duration_ms=678, request_bytes=337, request_throughput_kbps=11140, response_bytes=460488, response_throughput_kbps=5429, cache_hit=true}
default	19:36:10.190994+0800	hootowl	nw_protocol_tcp_set_connection_idle [C37.1.1.1:3] os_nexus_flow_set_connection_idle returned 0
default	19:36:10.191036+0800	hootowl	[C37] event: client:connection_idle @1.679s
default	19:36:10.191227+0800	hootowl	nw_protocol_tcp_notify [C37.1.1.1:3] nw_protocol_notification_type_connection_idle is true
default	19:36:10.191246+0800	hootowl	nw_protocol_tcp_set_connection_idle [C37.1.1.1:3] os_nexus_flow_set_connection_idle returned 0
default	19:36:10.191277+0800	hootowl	Task <A51C842C-C6FA-4870-B8F6-C29C99ABFDBF>.<30> finished successfully
default	19:36:10.191318+0800	hootowl	Mu1Base+Ext 152
taipei 📦 minutely Received 460035 bytes
default	19:36:10.191920+0800	hootowl	Mu1Base+Ext 175
previousHash updated
error	19:36:10.220408+0800	hootowl	333	wireAvailableUpdateFromMunicipal()	⚠️ duplicate parkIds in avail feed (11): 040014(綠寶石區, ?), 040037(綠光河岸區, ?), 040068(玉清宮, ?), 060021(陽光運動公園, ?), 060047(親情河濱公園1區, ?), 060068(萊茵區, ?), 060079(城市車旅新店安德二, ?), 060085(親情河濱公園2區, ?), 060085(親情河濱公園2區, ?), 170120(MITSUI OUTLET PARK 林口二館收費, ?), 170120(MITSUI OUTLET PARK 林口二館收費, ?)
default	19:36:10.224596+0800	hootowl	Municipal+Cyclops 93
🎨 model refreshed — obs:0s car:18 thread:main
default	19:36:10.228521+0800	hootowl	Municipal 130
🐎 minutelyAvailable ["newTaipeiCity ⏳03 19:17 ∑1429", "taipei ⏳03 19:36 ∑1113"]
default	19:36:10.239332+0800	hootowl	Municipal+Cyclops 93
🎨 model refreshed — obs:0s car:18 thread:main

```