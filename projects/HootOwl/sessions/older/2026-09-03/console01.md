```
default	18:37:39.421269+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c63ab posting AVAudioSessionAvailableOutputsChangeNotification
default	18:37:39.442538+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c63ab posting AVAudioSessionAvailableInputsChangeNotification
default	18:37:39.442647+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c63ab posting AVAudioSessionAvailableOutputsChangeNotification
default	18:37:39.474025+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c63ab posting AVAudioSessionAvailableOutputsChangeNotification
default	18:37:39.492387+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c63ab posting AVAudioSessionAvailableInputsChangeNotification
default	18:37:39.492398+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c63ab posting AVAudioSessionAvailableOutputsChangeNotification
default	18:37:39.529432+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c63ab posting AVAudioSessionAvailableOutputsChangeNotification
default	18:37:39.544913+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c63ab posting AVAudioSessionAvailableInputsChangeNotification
default	18:37:39.545069+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c63ab posting AVAudioSessionAvailableOutputsChangeNotification
default	18:37:45.718683+0800	hootowl	quic_frame_write_CONNECTION_CLOSE [C10.1.1.1:2] [-ebe5177080beb266] sending APPLICATION_CLOSE, code 0x100, reason <null>
default	18:37:45.718791+0800	hootowl	[C11 DCA4E2E1-B563-4346-ABDC-EC16E00519FA 142.250.66.66:443 quic-connection, url: https://googleads.g.doubleclick.net/pagead/interaction/, tls, definite, known tracker, attribution: developer] cancel
default	18:37:45.719079+0800	hootowl	[C11 DCA4E2E1-B563-4346-ABDC-EC16E00519FA 142.250.66.66:443 quic-connection, url: https://googleads.g.doubleclick.net/pagead/interaction/, tls, definite, known tracker, attribution: developer] cancelled
	[C11 06DE3AF1-CCA0-4FA4-8126-E99E64FEE653 192.168.50.191:63665<->142.250.66.66:443]
	Connected Path: satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good
	Duration: 120.186s, QUIC @0.000s took 0.000s, TLS 1.3 took 0.082s
	bytes in/out: 10673/6811, packets in/out: 16/19, rtt: 0.035s, retransmitted bytes: 0, out-of-order bytes: 1233
	ecn packets sent/acked/marked/lost: 6/6/0/0
default	18:37:45.720083+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C11] reporting state cancelled
default	18:37:45.720982+0800	hootowl	quic_conn_log_summary [C10.1.1.1:2] [-ebe5177080beb266] 
	Connection attempts: 1, RETRY received: no, PTOs: 0
	Early data: no, Keep-alives sent/acknowledged: 0/0, ECN state: handshake validation succeeded, L4S: disabled
	RTT: base 9 ms, network 14 ms, latest 39 ms, minimum 9 ms, smoothed 35 ms (variance 27 ms)
	Path MTU: 1280, minimum MSS: 1252
	Migration events: 0, paths validated: 0
	Inbound unidirectional/bidirectional streams: 3/0
	Outbound unidirectional/bidirectional streams: 3/1
	DATA_BLOCKED frames sent/received: 0/0
	STREAM_DATA_BLOCKED frames sent/received: 0/0
default	18:37:45.722997+0800	hootowl	quic_conn_drain [C10.1.1.1:2] [-ebe5177080beb266] QUIC Packets:
	snd    0.000s LH<initial, 0>
			CRYPTO[0;999]
			PADDING[-1]
	snd    0.000s LH<initial, 1>
			CRYPTO[999;1490]
			PADDING[-1]
	rcv    0.051s LH<initial, 1>
			ACK[0]
				(0, 0)
	rcv    0.007s LH<initial, 2>
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
	snd    0.001s LH<initial, 2>
			ACK[5]
				(1, 5)
			PADDING[-1]
	rcv    0.000s LH<handshake, 6>
			CRYPTO[0;1162]
	rcv    0.000s LH<handshake, 7>
			CRYPTO[1162;2323]
	snd    0.000s LH<handshake, 0>
			ACK[7]
				(6, 7)
	rcv    0.009s LH<handshake, 8>
			CRYPTO[2323;3484]
	snd    0.000s LH<handshake, 1>
			ACK[8]
				(6, 8)
	rcv    0.011s LH<handshake, 9>
			CRYPTO[3484;4340]
	snd    0.000s LH<handshake, 2>
			ACK[9]
				(6, 9)
	snd    0.003s LH<handshake, 3>
			CRYPTO[0;52]
	rcv    0.002s SH<10>
			S3[0;44]
	snd    0.001s SH<0>
			ACK[10]
				(10, 10)
	snd    0.000s SH<1>
			S2[0;25]
	snd    0.000s SH<2>
			S0[0;1166]
	snd    0.000s SH<3>
			S0[1166;1387] FIN
	snd    0.001s SH<4>
			S6[0;5]
	rcv    0.006s SH<11>
			CRYPTO[0;624]
	snd    0.001s SH<5>
			ACK[11]
				(10, 11)
	rcv    0.003s SH<12>
			PADDING[0]
			PADDING[0]
			NEW_CONNECTION_ID[seq=1, retire=0]
	snd    0.000s SH<6>
			ACK[12]
				(10, 12)
	snd    0.000s SH<7>
			PADDING[0]
			PADDING[-1]
	rcv    0.000s SH<13>
			ACK[2]
				(0, 2)
	rcv    0.001s SH<14>
			ACK[4]
				(0, 4)
	rcv    0.009s SH<15>
			ACK[7]
				(0, 7)
			S11[0;304]
			S0[0;64]
	snd    0.000s SH<8>
			ACK[15]
				(10, 15)
	snd    0.000s SH<9>
			S10[0;2]
	rcv    0.002s SH<16>
			S0[64;64] FIN
	snd    0.029s SH<10>
			ACK[16]
				(10, 16)
	rcv    0.009s SH<17>
			ACK[9]
				(8, 9)
	snd  120.000s SH<11>
			APPLICATION_CLOSE[code=256, type=0]
default	18:37:45.723171+0800	hootowl	Connection 10: cleaning up
default	18:37:45.723212+0800	hootowl	[C10 6165323C-E6D4-402F-A627-7D8E81240B03 googleads.g.doubleclick.net:443 quic-connection, url: https://googleads.g.doubleclick.net/pagead/interaction/, definite, attribution: developer] cancel
default	18:37:45.723367+0800	hootowl	[C10 6165323C-E6D4-402F-A627-7D8E81240B03 googleads.g.doubleclick.net:443 quic-connection, url: https://googleads.g.doubleclick.net/pagead/interaction/, definite, attribution: developer] cancelled
	[C10.1.1.1 06DE3AF1-CCA0-4FA4-8126-E99E64FEE653 192.168.50.191:63665<->142.250.66.66:443]
	Connected Path: satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good
	Privacy Stance: Not Eligible
	Duration: 120.209s, DNS @0.002s took 0.014s, QUIC @0.017s took 0.087s
	bytes in/out: 10673/6811, packets in/out: 16/19, rtt: 0.035s, retransmitted bytes: 0, out-of-order bytes: 1233
	ecn packets sent/acked/marked/lost: 6/6/0/0
default	18:37:45.724489+0800	hootowl	quic_path_destroy [C10.1.1.1:2] [-ebe5177080beb266] destroying path 0x13bcb41c0
default	18:37:45.724613+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C10] reporting state cancelled
default	18:37:54.027687+0800	hootowl	Task <37192245-8640-49DA-9D6F-D75AD4E5B88E>.<7> resuming, timeouts(60.0, 604800.0) qos(0x15) voucher((null)) activity(00000000-0000-0000-0000-000000000000)
default	18:37:54.036058+0800	hootowl	Connection 0: creating secure tcp or quic connection
default	18:37:54.037132+0800	hootowl	Connection 13: enabling TLS
default	18:37:54.037153+0800	hootowl	Connection 13: starting, TC(0x0)
default	18:37:54.037180+0800	hootowl	[C13 881A0D95-9A6E-4552-8385-67DE682F2D09 tcgbusfs.blob.core.windows.net:443 quic-connection, url: https://tcgbusfs.blob.core.windows.net/blobtcmsv/TCMSV_allavailable.json, definite, attribution: developer, context: com.apple.CFNetwork.NSURLSession.{C8A30AB7-8A8F-46A2-A794-FF53331E2689}{(null)}{Y}{2}{0x0} (private), proc: 1B526020-2DE0-3C65-9122-F1177549D69A, delegated upid: 0] start
default	18:37:54.037236+0800	hootowl	[C13 tcgbusfs.blob.core.windows.net:443 initial parent-flow ((null))] event: path:start @0.000s
default	18:37:54.038687+0800	hootowl	[C13 tcgbusfs.blob.core.windows.net:443 waiting parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.001s, uuid: 441BEB41-8D8F-4120-93D0-C134DFA7DD06
default	18:37:54.038824+0800	hootowl	[C13 tcgbusfs.blob.core.windows.net:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_connect @0.002s
default	18:37:54.038841+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C13] reporting state preparing
default	18:37:54.038949+0800	hootowl	[C13 tcgbusfs.blob.core.windows.net:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_child @0.002s
default	18:37:54.039000+0800	hootowl	[C13.1 tcgbusfs.blob.core.windows.net:443 initial path ((null))] event: path:start @0.002s
default	18:37:54.039318+0800	hootowl	[C13.1 tcgbusfs.blob.core.windows.net:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.002s, uuid: 441BEB41-8D8F-4120-93D0-C134DFA7DD06
default	18:37:54.039707+0800	hootowl	[C13.1 tcgbusfs.blob.core.windows.net:443 in_progress transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: transform:start @0.002s
default	18:37:54.039793+0800	hootowl	[C13.1.1 tcgbusfs.blob.core.windows.net:443 initial path ((null))] event: path:start @0.002s
default	18:37:54.040337+0800	hootowl	[C13.1.1 tcgbusfs.blob.core.windows.net:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.003s, uuid: FBF01939-42C9-4C9E-8558-B7E973DAD22A
default	18:37:54.040582+0800	hootowl	[C13.1.1 tcgbusfs.blob.core.windows.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:start_dns @0.003s
default	18:37:54.040796+0800	hootowl	Task <37192245-8640-49DA-9D6F-D75AD4E5B88E>.<7> setting up Connection 13
default	18:37:54.069859+0800	hootowl	nw_endpoint_resolver_update [C13.1.1 tcgbusfs.blob.core.windows.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Adding endpoint handler for 20.150.22.100:443
default	18:37:54.069958+0800	hootowl	[C13.1.1 tcgbusfs.blob.core.windows.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:receive_dns @0.032s
default	18:37:54.071305+0800	hootowl	[C13.1.1.1 20.150.22.100:443 initial path ((null))] event: path:start @0.032s
default	18:37:54.073693+0800	hootowl	[C13.1.1.1 20.150.22.100:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.034s, uuid: 83FCFAD5-92A2-439E-9EA8-7B29A695B6EE
default	18:37:54.073962+0800	hootowl	[C13.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_nexus @0.035s
default	18:37:54.075382+0800	hootowl	[C13.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:receive_nexus @0.037s
default	18:37:54.106240+0800	hootowl	[C13.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_connect @0.040s
default	18:37:54.107008+0800	hootowl	tcp_output [C13.1.1.1:3] flags=[SEC] seq=473800828, ack=0, win=65535 state=SYN_SENT rcv_nxt=0, snd_una=473800828
default	18:37:54.174458+0800	hootowl	tcp_input [C13.1.1.1:3] flags=[S.E] seq=1238332398, ack=473800829, win=65535 state=SYN_SENT rcv_nxt=0, snd_una=473800828
default	18:37:54.174559+0800	hootowl	nw_flow_connected [C13.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Transport protocol connected (tcp)
default	18:37:54.174860+0800	hootowl	[C13.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_transport @0.137s
default	18:37:54.175152+0800	hootowl	boringssl_session_apply_protocol_options_for_transport_block_invoke_2(2367) [C13.1.1.1:2][0x11c0539e0] TLS configured [server(0) min_version(0x0303) max_version(0x0304) name(tcgbusfs.blob.core.windows.net) tickets(false) false_start(false) enforce_ev(false) enforce_ats(false) ats_non_pfs_ciphersuite_allowed(false) cc_mode_enforced(false) ech(false) pqtls(true), pake(false) skip_ats_trust(false)]
default	18:37:54.175317+0800	hootowl	boringssl_context_info_handler(2806) [C13.1.1.1:2][0x11c0539e0] Client handshake started
default	18:37:54.175640+0800	hootowl	boringssl_context_info_handler(2823) [C13.1.1.1:2][0x11c0539e0] Client handshake state: TLS client enter_early_data
default	18:37:54.175936+0800	hootowl	boringssl_context_info_handler(2823) [C13.1.1.1:2][0x11c0539e0] Client handshake state: TLS client read_server_hello
default	18:37:54.245735+0800	hootowl	boringssl_context_info_handler(2823) [C13.1.1.1:2][0x11c0539e0] Client handshake state: TLS 1.3 client read_hello_retry_request
default	18:37:54.246908+0800	hootowl	boringssl_context_info_handler(2823) [C13.1.1.1:2][0x11c0539e0] Client handshake state: TLS 1.3 client send_second_client_hello
default	18:37:54.246948+0800	hootowl	boringssl_context_info_handler(2823) [C13.1.1.1:2][0x11c0539e0] Client handshake state: TLS 1.3 client read_server_hello
default	18:37:54.343226+0800	hootowl	boringssl_context_info_handler(2823) [C13.1.1.1:2][0x11c0539e0] Client handshake state: TLS 1.3 client read_encrypted_extensions
default	18:37:54.346920+0800	hootowl	boringssl_context_info_handler(2823) [C13.1.1.1:2][0x11c0539e0] Client handshake state: TLS 1.3 client read_certificate_request
default	18:37:54.347054+0800	hootowl	boringssl_context_info_handler(2823) [C13.1.1.1:2][0x11c0539e0] Client handshake state: TLS 1.3 client read_server_certificate
default	18:37:54.347089+0800	hootowl	boringssl_context_info_handler(2823) [C13.1.1.1:2][0x11c0539e0] Client handshake state: TLS 1.3 client read_server_certificate_verify
default	18:37:54.347685+0800	hootowl	boringssl_context_evaluate_trust_async(2249) [C13.1.1.1:2][0x11c0539e0] Performing external trust evaluation
default	18:37:54.347733+0800	hootowl	boringssl_context_evaluate_trust_async_external(2234) [C13.1.1.1:2][0x11c0539e0] Asyncing for external verify block
default	18:37:54.347899+0800	hootowl	Connection 13: asked to evaluate TLS Trust
default	18:37:54.348297+0800	hootowl	Task <37192245-8640-49DA-9D6F-D75AD4E5B88E>.<7> auth completion disp=1 cred=0x0
default	18:37:54.349055+0800	hootowl	(Trust 0x1098d6a00) No pending evals, starting
default	18:37:54.349529+0800	hootowl	[0x11212e440] activating connection: mach=true listener=false peer=false name=com.apple.trustd
default	18:37:54.349910+0800	hootowl	(Trust 0x1098d6a00) Completed async eval kickoff
default	18:37:54.360606+0800	hootowl	(Trust 0x1098d6a00) trustd returned 4
default	18:37:54.360703+0800	hootowl	System Trust Evaluation yielded status(0)
default	18:37:54.360786+0800	hootowl	(Trust 0x1098d7900) No pending evals, starting
default	18:37:54.361056+0800	hootowl	[0x11212d900] activating connection: mach=true listener=false peer=false name=com.apple.trustd
default	18:37:54.361294+0800	hootowl	(Trust 0x1098d7900) Completed async eval kickoff
default	18:37:54.361505+0800	hootowl	[0x11212e440] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	18:37:54.368351+0800	hootowl	(Trust 0x1098d7900) trustd returned 4
default	18:37:54.368434+0800	hootowl	Connection 13: TLS Trust result 0
default	18:37:54.368463+0800	hootowl	boringssl_context_evaluate_trust_async_external_block_invoke_3(2148) [C13.1.1.1:2][0x11c0539e0] Returning from external verify block with result: true
default	18:37:54.368571+0800	hootowl	boringssl_context_certificate_verify_callback(2430) [C13.1.1.1:2][0x11c0539e0] Certificate verification result: OK
default	18:37:54.368652+0800	hootowl	boringssl_context_info_handler(2823) [C13.1.1.1:2][0x11c0539e0] Client handshake state: TLS 1.3 client read_server_finished
default	18:37:54.368694+0800	hootowl	boringssl_context_info_handler(2823) [C13.1.1.1:2][0x11c0539e0] Client handshake state: TLS 1.3 client send_end_of_early_data
default	18:37:54.368717+0800	hootowl	boringssl_context_info_handler(2823) [C13.1.1.1:2][0x11c0539e0] Client handshake state: TLS 1.3 client send_client_encrypted_extensions
default	18:37:54.368737+0800	hootowl	boringssl_context_info_handler(2823) [C13.1.1.1:2][0x11c0539e0] Client handshake state: TLS 1.3 client send_client_certificate
default	18:37:54.368752+0800	hootowl	boringssl_context_info_handler(2823) [C13.1.1.1:2][0x11c0539e0] Client handshake state: TLS 1.3 client complete_second_flight
default	18:37:54.368788+0800	hootowl	boringssl_context_info_handler(2823) [C13.1.1.1:2][0x11c0539e0] Client handshake state: TLS 1.3 client done
default	18:37:54.369025+0800	hootowl	boringssl_context_info_handler(2823) [C13.1.1.1:2][0x11c0539e0] Client handshake state: TLS client finish_client_handshake
default	18:37:54.369048+0800	hootowl	boringssl_context_info_handler(2823) [C13.1.1.1:2][0x11c0539e0] Client handshake state: TLS client done
default	18:37:54.369070+0800	hootowl	boringssl_context_info_handler(2812) [C13.1.1.1:2][0x11c0539e0] Client handshake done
default	18:37:54.369321+0800	hootowl	nw_protocol_boringssl_signal_connected(895) [C13.1.1.1:2][0x11c0539e0] TLS connected [server(0) version(0x0304) ciphersuite(TLS_AES_256_GCM_SHA384) group(0x0018) signature_alg(0x0804) alpn(nil) resumed(0) offered_ticket(0) in_early_data(0) early_data_accepted(0) false_started(0) ocsp_received(1) sct_received(0) connect_time(193ms) flight_time(163ms) rtt(70ms) write_stalls(0) read_stalls(11) pake(0x0000)]
default	18:37:54.369379+0800	hootowl	nw_flow_connected [C13.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (CFNetworkConnection-398509258)
default	18:37:54.369625+0800	hootowl	[C13.1.1.1 20.150.22.100:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.332s
default	18:37:54.369786+0800	hootowl	[C13.1.1 tcgbusfs.blob.core.windows.net:443 ready resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.332s
default	18:37:54.369824+0800	hootowl	[C13.1 tcgbusfs.blob.core.windows.net:443 ready transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.332s
default	18:37:54.369931+0800	hootowl	[C13.1.1.1 20.150.22.100:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.333s
default	18:37:54.369987+0800	hootowl	[C13.1.1 tcgbusfs.blob.core.windows.net:443 ready resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.333s
default	18:37:54.370029+0800	hootowl	[C13.1 tcgbusfs.blob.core.windows.net:443 ready transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.333s
default	18:37:54.370081+0800	hootowl	nw_flow_connected [C13 20.150.22.100:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (endpoint_flow)
default	18:37:54.370142+0800	hootowl	[C13 20.150.22.100:443 ready parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_connect @0.333s
default	18:37:54.370341+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C13] reporting state ready
default	18:37:54.370455+0800	hootowl	[C13 20.150.22.100:443 ready parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.333s
default	18:37:54.370477+0800	hootowl	nw_connection_send_viability_changed_on_nw_queue [C13] viability_changed_handler(true)
default	18:37:54.370501+0800	hootowl	[0x11212d900] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	18:37:54.370559+0800	hootowl	Connection 13: connected successfully
default	18:37:54.370568+0800	hootowl	Connection 13: TLS handshake complete
default	18:37:54.370594+0800	hootowl	Connection 13: ready C(N) E(N)
default	18:37:54.370680+0800	hootowl	Task <37192245-8640-49DA-9D6F-D75AD4E5B88E>.<7> now using Connection 13
default	18:37:54.370718+0800	hootowl	Connection 13: received viability advisory(Y)
default	18:37:54.370887+0800	hootowl	Task <37192245-8640-49DA-9D6F-D75AD4E5B88E>.<7> sent request, body N 0
default	18:37:54.459777+0800	hootowl	Task <37192245-8640-49DA-9D6F-D75AD4E5B88E>.<7> received response, status 200 content K
default	18:37:55.097841+0800	hootowl	Task <37192245-8640-49DA-9D6F-D75AD4E5B88E>.<7> response ended
default	18:37:55.098336+0800	hootowl	Task <37192245-8640-49DA-9D6F-D75AD4E5B88E>.<7> done using Connection 13
default	18:37:55.099800+0800	hootowl	[C13] event: client:connection_idle @1.060s
default	18:37:55.099965+0800	hootowl	Task <37192245-8640-49DA-9D6F-D75AD4E5B88E>.<7> summary for task success {transaction_duration_ms=1068, response_status=200, connection=13, protocol="http/1.1", domain_lookup_duration_ms=29, connect_duration_ms=293, secure_connection_duration_ms=193, private_relay=false, request_start_ms=342, request_duration_ms=0, response_start_ms=430, response_duration_ms=637, request_bytes=337, request_throughput_kbps=43491, response_bytes=460408, response_throughput_kbps=5775, cache_hit=true}
default	18:37:55.102279+0800	hootowl	nw_protocol_tcp_notify [C13.1.1.1:3] nw_protocol_notification_type_connection_idle is true
default	18:37:55.102333+0800	hootowl	nw_protocol_tcp_set_connection_idle [C13.1.1.1:3] os_nexus_flow_set_connection_idle returned 0
default	18:37:55.103365+0800	hootowl	[C13] event: client:connection_idle @1.063s
default	18:37:55.103379+0800	hootowl	Task <37192245-8640-49DA-9D6F-D75AD4E5B88E>.<7> finished successfully
default	18:37:55.104254+0800	hootowl	nw_protocol_tcp_notify [C13.1.1.1:3] nw_protocol_notification_type_connection_idle is true
default	18:37:55.104279+0800	hootowl	Mu1Base+Ext 152
taipei 📦 minutely Received 459955 bytes
default	18:37:55.104302+0800	hootowl	Mu1Base+Ext 175
previousHash updated
default	18:37:55.104424+0800	hootowl	nw_protocol_tcp_set_connection_idle [C13.1.1.1:3] os_nexus_flow_set_connection_idle returned 0
error	18:37:55.128230+0800	hootowl	333	wireAvailableUpdateFromMunicipal()	⚠️ duplicate parkIds in avail feed (11): 040014(綠寶石區, ?), 040037(綠光河岸區, ?), 040068(玉清宮, ?), 060021(陽光運動公園, ?), 060047(親情河濱公園1區, ?), 060068(萊茵區, ?), 060079(城市車旅新店安德二, ?), 060085(親情河濱公園2區, ?), 060085(親情河濱公園2區, ?), 170120(MITSUI OUTLET PARK 林口二館收費, ?), 170120(MITSUI OUTLET PARK 林口二館收費, ?)
default	18:37:55.131252+0800	hootowl	Municipal+Cyclops 79
🎨 model refreshed — obs:0s car:18 thread:main
default	18:37:55.131784+0800	hootowl	Municipal 130
🐎 minutelyAvailable ["newTaipeiCity ⏳03 18:35 ∑1429", "taipei ⏳03 18:37 ∑1113"]
default	18:37:55.143539+0800	hootowl	Municipal+Cyclops 79
🎨 model refreshed — obs:0s car:18 thread:main
default	18:38:04.838224+0800	hootowl	TX focusApplication (peekAppEvent) stealKB:Y scene:com.sharkda.hootowl-1B8F959F-618F-4A0D-AD89-E09DEC0EAB34
default	18:38:04.845736+0800	hootowl	Evaluating dispatch of UIEvent: 0x11cfa2200; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	18:38:04.845875+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	18:38:04.845912+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1099f0400>; contextId: 0x6EC72245
default	18:38:04.846116+0800	hootowl	Evaluating dispatch of UIEvent: 0x11cfa2200; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	18:38:04.846292+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	18:38:04.846514+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1099f0400>; contextId: 0x6EC72245
default	18:38:04.847023+0800	hootowl	Evaluating dispatch of UIEvent: 0x11cfa2200; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	18:38:04.847193+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	18:38:04.847300+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1099f0400>; contextId: 0x6EC72245
default	18:38:04.849435+0800	hootowl	Evaluating dispatch of UIEvent: 0x11cfa2200; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	18:38:04.849467+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	18:38:04.849510+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1099f0400>; contextId: 0x6EC72245
default	18:38:04.866388+0800	hootowl	Evaluating dispatch of UIEvent: 0x11cfa2200; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	18:38:04.866409+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	18:38:04.866420+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1099f0400>; contextId: 0x6EC72245
default	18:38:04.883341+0800	hootowl	Evaluating dispatch of UIEvent: 0x11cfa2200; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	18:38:04.883687+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	18:38:04.883863+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1099f0400>; contextId: 0x6EC72245
default	18:38:04.899718+0800	hootowl	Evaluating dispatch of UIEvent: 0x11cfa2200; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	18:38:04.899765+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	18:38:04.900002+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1099f0400>; contextId: 0x6EC72245
default	18:38:04.916357+0800	hootowl	Not push traits update to screen for new style 1, <UIWindowScene: 0x10cc50200> (1B8F959F-618F-4A0D-AD89-E09DEC0EAB34)
default	18:38:04.918467+0800	hootowl	sceneOfRecord: sceneID: sceneID:com.sharkda.hootowl-1B8F959F-618F-4A0D-AD89-E09DEC0EAB34  persistentID: 1B8F959F-618F-4A0D-AD89-E09DEC0EAB34
default	18:38:04.918477+0800	hootowl	Deactivation reason added: 0; deactivation reasons: 0 -> 1; animating application lifecycle event: 1
default	18:38:04.918479+0800	hootowl	App transitioned to background, suspending HangTracing.
default	18:38:04.918483+0800	hootowl	App with bundleID:com.sharkda.hootowl is no longer foreground at time=15363288740931, attempting to emit telemetry with emission type: HTFGUpdateAppBackgrounded
default	18:38:04.926409+0800	hootowl	Deactivation reason added: 12; deactivation reasons: 1 -> 4097; animating application lifecycle event: 1
default	18:38:04.926465+0800	hootowl	UseInterruptCal,platformDefault,0,overrideSet,0,final,0
default	18:38:04.926518+0800	hootowl	Evaluating dispatch of UIEvent: 0x11cfa2200; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	18:38:04.926572+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	18:38:04.927161+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1099f0400>; contextId: 0x6EC72245
default	18:38:04.927179+0800	hootowl	Evaluating dispatch of UIEvent: 0x11cfa2200; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	18:38:04.928013+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	18:38:04.928020+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1099f0400>; contextId: 0x6EC72245
default	18:38:05.136248+0800	hootowl	sceneOfRecord: sceneID: sceneID:com.sharkda.hootowl-1B8F959F-618F-4A0D-AD89-E09DEC0EAB34  persistentID: 1B8F959F-618F-4A0D-AD89-E09DEC0EAB34
default	18:38:05.141391+0800	hootowl	policyStatus:<BKSHIDEventDeliveryPolicyObserver: 0x10cd94660; environment: keyboardFocus; status: none> was:target
default	18:38:05.141824+0800	hootowl	policyStatus:<BKSHIDEventDeliveryPolicyObserver: 0x1098623a0; token: com.apple.frontboard.systemappservices/FBSceneManager:sceneID%3Acom.sharkda.hootowl-1B8F959F-618F-4A0D-AD89-E09DEC0EAB34; status: none> was:ancestor
default	18:38:05.145621+0800	hootowl	Scene target of keyboard event deferring environment did change: 0; scene: UIWindowScene: 0x10cc50200; scene identity: com.apple.frontboard.systemappservices/FBSceneManager:sceneID%3Acom.sharkda.hootowl-1B8F959F-618F-4A0D-AD89-E09DEC0EAB34
default	18:38:05.146100+0800	hootowl	policyStatus:<BKSHIDEventDeliveryPolicyObserver: 0x10cd94de0; environment: keyboardFocus; status: none> was:target
default	18:38:05.148369+0800	hootowl	sceneOfRecord: sceneID: sceneID:com.sharkda.hootowl-1B8F959F-618F-4A0D-AD89-E09DEC0EAB34  persistentID: 1B8F959F-618F-4A0D-AD89-E09DEC0EAB34
default	18:38:05.154442+0800	hootowl	sceneOfRecord: sceneID: sceneID:com.sharkda.hootowl-1B8F959F-618F-4A0D-AD89-E09DEC0EAB34  persistentID: 1B8F959F-618F-4A0D-AD89-E09DEC0EAB34
default	18:38:05.163431+0800	hootowl	sceneOfRecord: sceneID: sceneID:com.sharkda.hootowl-1B8F959F-618F-4A0D-AD89-E09DEC0EAB34  persistentID: 1B8F959F-618F-4A0D-AD89-E09DEC0EAB34
default	18:38:05.166202+0800	hootowl	Deactivation reason added: 5; deactivation reasons: 4097 -> 4129; animating application lifecycle event: 1
default	18:38:05.167032+0800	hootowl	sceneOfRecord: sceneID: sceneID:com.sharkda.hootowl-1B8F959F-618F-4A0D-AD89-E09DEC0EAB34  persistentID: 1B8F959F-618F-4A0D-AD89-E09DEC0EAB34
default	18:38:05.167119+0800	hootowl	Deactivation reason removed: 0; deactivation reasons: 4129 -> 4128; animating application lifecycle event: 1
default	18:38:05.890218+0800	hootowl	sceneOfRecord: sceneID: sceneID:com.sharkda.hootowl-1B8F959F-618F-4A0D-AD89-E09DEC0EAB34  persistentID: 1B8F959F-618F-4A0D-AD89-E09DEC0EAB34
default	18:38:05.890244+0800	hootowl	Deactivation reason added: 3; deactivation reasons: 4128 -> 4136; animating application lifecycle event: 1
default	18:38:05.891884+0800	hootowl	sceneOfRecord: sceneID: sceneID:com.sharkda.hootowl-1B8F959F-618F-4A0D-AD89-E09DEC0EAB34  persistentID: 1B8F959F-618F-4A0D-AD89-E09DEC0EAB34
default	18:38:05.892466+0800	hootowl	Deactivation reason removed: 5; deactivation reasons: 4136 -> 4104; animating application lifecycle event: 0
default	18:38:05.943849+0800	hootowl	sceneOfRecord: sceneID: sceneID:com.sharkda.hootowl-1B8F959F-618F-4A0D-AD89-E09DEC0EAB34  persistentID: 1B8F959F-618F-4A0D-AD89-E09DEC0EAB34
default	18:38:06.893485+0800	hootowl	sceneOfRecord: sceneID: sceneID:com.sharkda.hootowl-1B8F959F-618F-4A0D-AD89-E09DEC0EAB34  persistentID: 1B8F959F-618F-4A0D-AD89-E09DEC0EAB34
default	18:38:06.893585+0800	hootowl	Deactivation reason added: 5; deactivation reasons: 4104 -> 4136; animating application lifecycle event: 1
default	18:38:06.932857+0800	hootowl	sceneOfRecord: sceneID: sceneID:com.sharkda.hootowl-1B8F959F-618F-4A0D-AD89-E09DEC0EAB34  persistentID: 1B8F959F-618F-4A0D-AD89-E09DEC0EAB34
default	18:38:06.933425+0800	hootowl	Deactivation reason removed: 3; deactivation reasons: 4136 -> 4128; animating application lifecycle event: 1
default	18:38:06.985455+0800	hootowl	RX sceneBecameFocused:(null)
default	18:38:07.312932+0800	hootowl	Received state update for 36996 (app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>, unknown-NotVisible
default	18:38:07.596412+0800	hootowl	[(FBSceneManager):sceneID:com.sharkda.hootowl-1B8F959F-618F-4A0D-AD89-E09DEC0EAB34] Received action(s) in scene-update: <FBSceneSnapshotAction: 0x6c283f61>
default	18:38:07.618139+0800	hootowl	sceneOfRecord: sceneID: sceneID:com.sharkda.hootowl-1B8F959F-618F-4A0D-AD89-E09DEC0EAB34  persistentID: 1B8F959F-618F-4A0D-AD89-E09DEC0EAB34
default	18:38:07.618149+0800	hootowl	Deactivation reason added: 11; deactivation reasons: 4128 -> 6176; animating application lifecycle event: 0
default	18:38:07.618164+0800	hootowl	[0x10ce90c80] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	18:38:07.618171+0800	hootowl	[0x10cd20e60] Session canceled.
default	18:38:07.622513+0800	hootowl	{"msg":"CLLocationManager", "event":"activity", "_cmd":"onDidEnterBackground:", "self":"0x1038ead60", "notification":"NSConcreteNotification 0x13bc78ba0 {name = UIApplicationDidEnterBackgroundNotification; object = <_TtC7SwiftUIP33_ACC2C5639A7D76F611E170E831FCA49118SwiftUIApplication: 0x10cc50000>}"}
default	18:38:07.622977+0800	hootowl	Will add backgroundTask with taskName: com.apple.asset_manager.cache_resource_cleanup, expirationHandler: <__NSMallocBlock__: 0x11cff8330>
default	18:38:07.622996+0800	hootowl	Creating new assertion because there is no existing background assertion.
default	18:38:07.624072+0800	hootowl	Creating new background assertion
default	18:38:07.624877+0800	hootowl	Created new background assertion <BKSProcessAssertion: 0x139989130>
default	18:38:07.625355+0800	hootowl	agent connection cancelled (details: Session manually canceled)
default	18:38:07.625502+0800	hootowl	[0x10cd20e60] Disposing of session
default	18:38:07.633753+0800	hootowl	Incrementing reference count for background assertion <BKSProcessAssertion: 0x139989130>
default	18:38:07.633768+0800	hootowl	Created background task <_UIBackgroundTaskInfo: 0x13bc75040>: taskID = 3, taskName = com.apple.asset_manager.cache_resource_cleanup, creationTime = 640139 (elapsed = 0).
default	18:38:07.633780+0800	hootowl	Ending background task with UIBackgroundTaskIdentifier: 3
default	18:38:07.633790+0800	hootowl	Ending task with identifier 3 and description: <_UIBackgroundTaskInfo: 0x13bc75040>: taskID = 3, taskName = com.apple.asset_manager.cache_resource_cleanup, creationTime = 640139 (elapsed = 0), _expireHandler: <__NSMallocBlock__: 0x11cff8330>
default	18:38:07.634382+0800	hootowl	Decrementing reference count for assertion <BKSProcessAssertion: 0x139989130> (used by background task with identifier 3: <_UIBackgroundTaskInfo: 0x13bc75040>: taskID = 3, taskName = com.apple.asset_manager.cache_resource_cleanup, creationTime = 640139 (elapsed = 0))
default	18:38:07.634505+0800	hootowl	Will invalidate assertion: <BKSProcessAssertion: 0x139989130> for task identifier: 3
default	18:38:07.634705+0800	hootowl	Will add backgroundTask with taskName: _UIRemoteKeyboard XPC disconnection, expirationHandler: (null)
default	18:38:07.635045+0800	hootowl	Creating new assertion because there is no existing background assertion.
default	18:38:07.635111+0800	hootowl	Creating new background assertion
default	18:38:07.639319+0800	hootowl	Created new background assertion <BKSProcessAssertion: 0x1399892c0>
default	18:38:07.645339+0800	hootowl	Incrementing reference count for background assertion <BKSProcessAssertion: 0x1399892c0>
default	18:38:07.645786+0800	hootowl	Created background task <_UIBackgroundTaskInfo: 0x13bc75100>: taskID = 4, taskName = _UIRemoteKeyboard XPC disconnection, creationTime = 640139 (elapsed = 0).
default	18:38:07.645941+0800	hootowl	com.sharkda.hootowl(36996) invalidateConnection (appDidSuspend)
default	18:38:07.645987+0800	hootowl	[0x11212fd40] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	18:38:07.646123+0800	hootowl	Will add backgroundTask with taskName: com.apple.asset_manager.cache_resource_cleanup, expirationHandler: <__NSMallocBlock__: 0x11cff8bd0>
default	18:38:07.646823+0800	hootowl	Reusing background assertion <BKSProcessAssertion: 0x1399892c0>
default	18:38:07.658272+0800	hootowl	Incrementing reference count for background assertion <BKSProcessAssertion: 0x1399892c0>
default	18:38:07.658303+0800	hootowl	Created background task <_UIBackgroundTaskInfo: 0x13bc751c0>: taskID = 5, taskName = com.apple.asset_manager.cache_resource_cleanup, creationTime = 640139 (elapsed = 0).
default	18:38:07.658314+0800	hootowl	Ending background task with UIBackgroundTaskIdentifier: 5
default	18:38:07.658344+0800	hootowl	Ending task with identifier 5 and description: <_UIBackgroundTaskInfo: 0x13bc751c0>: taskID = 5, taskName = com.apple.asset_manager.cache_resource_cleanup, creationTime = 640139 (elapsed = 0), _expireHandler: <__NSMallocBlock__: 0x11cff8bd0>
default	18:38:07.658365+0800	hootowl	Decrementing reference count for assertion <BKSProcessAssertion: 0x1399892c0> (used by background task with identifier 5: <_UIBackgroundTaskInfo: 0x13bc751c0>: taskID = 5, taskName = com.apple.asset_manager.cache_resource_cleanup, creationTime = 640139 (elapsed = 0))
default	18:38:07.659151+0800	hootowl	[0x10ce912c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	18:38:07.660012+0800	hootowl	Will add backgroundTask with taskName: com.apple.asset_manager.cache_resource_cleanup, expirationHandler: <__NSMallocBlock__: 0x11cff8bd0>
default	18:38:07.660475+0800	hootowl	Reusing background assertion <BKSProcessAssertion: 0x1399892c0>
default	18:38:07.661273+0800	hootowl	Incrementing reference count for background assertion <BKSProcessAssertion: 0x1399892c0>
default	18:38:07.661693+0800	hootowl	Created background task <_UIBackgroundTaskInfo: 0x13bc76e40>: taskID = 6, taskName = com.apple.asset_manager.cache_resource_cleanup, creationTime = 640139 (elapsed = 0).
default	18:38:07.661750+0800	hootowl	Ending background task with UIBackgroundTaskIdentifier: 6
default	18:38:07.662470+0800	hootowl	Ending task with identifier 6 and description: <_UIBackgroundTaskInfo: 0x13bc76e40>: taskID = 6, taskName = com.apple.asset_manager.cache_resource_cleanup, creationTime = 640139 (elapsed = 0), _expireHandler: <__NSMallocBlock__: 0x11cff8bd0>
default	18:38:07.662555+0800	hootowl	Decrementing reference count for assertion <BKSProcessAssertion: 0x1399892c0> (used by background task with identifier 6: <_UIBackgroundTaskInfo: 0x13bc76e40>: taskID = 6, taskName = com.apple.asset_manager.cache_resource_cleanup, creationTime = 640139 (elapsed = 0))
default	18:38:07.663918+0800	hootowl	Will add backgroundTask with taskName: com.apple.asset_manager.cache_resource_cleanup, expirationHandler: <__NSMallocBlock__: 0x11cff8bd0>
default	18:38:07.665646+0800	hootowl	Reusing background assertion <BKSProcessAssertion: 0x1399892c0>
default	18:38:07.667797+0800	hootowl	Incrementing reference count for background assertion <BKSProcessAssertion: 0x1399892c0>
default	18:38:07.667983+0800	hootowl	Created background task <_UIBackgroundTaskInfo: 0x13bc751c0>: taskID = 7, taskName = com.apple.asset_manager.cache_resource_cleanup, creationTime = 640139 (elapsed = 0).
default	18:38:07.669118+0800	hootowl	Ending background task with UIBackgroundTaskIdentifier: 7
default	18:38:07.669138+0800	hootowl	Ending task with identifier 7 and description: <_UIBackgroundTaskInfo: 0x13bc751c0>: taskID = 7, taskName = com.apple.asset_manager.cache_resource_cleanup, creationTime = 640139 (elapsed = 0), _expireHandler: <__NSMallocBlock__: 0x11cff8bd0>
default	18:38:07.669159+0800	hootowl	Decrementing reference count for assertion <BKSProcessAssertion: 0x1399892c0> (used by background task with identifier 7: <_UIBackgroundTaskInfo: 0x13bc751c0>: taskID = 7, taskName = com.apple.asset_manager.cache_resource_cleanup, creationTime = 640139 (elapsed = 0))
default	18:38:07.669534+0800	hootowl	0x10cd19c18 - [pageProxyID=2087, webPageID=2088, PID=37010] WebPageProxy::applicationWillEnterForegroundForMedia: isSuspendedUnderLock? 0
default	18:38:07.674370+0800	hootowl	Deactivation reason removed: 5; deactivation reasons: 6176 -> 6144; animating application lifecycle event: 0
default	18:38:07.683777+0800	hootowl	Municipal+Lifecycle 25
⏸️ app → background: pausing GPS + 2 active proto timer(s)
default	18:38:07.684398+0800	hootowl	{"msg":"CLLocationManager", "event":"activity", "_cmd":"stopUpdatingLocation", "self":"0x1038ead60"}
default	18:38:07.702725+0800	hootowl	Will add backgroundTask with taskName: com.apple.uikit.applicationSnapshot, expirationHandler: <__NSMallocBlock__: 0x11c379f80>
default	18:38:07.702769+0800	hootowl	Reusing background assertion <BKSProcessAssertion: 0x1399892c0>
default	18:38:07.702788+0800	hootowl	Incrementing reference count for background assertion <BKSProcessAssertion: 0x1399892c0>
default	18:38:07.702801+0800	hootowl	Created background task <_UIBackgroundTaskInfo: 0x13bc75fc0>: taskID = 8, taskName = com.apple.uikit.applicationSnapshot, creationTime = 640139 (elapsed = 0).
default	18:38:07.702816+0800	hootowl	Push traits update to screen for new style 1, <UIWindowScene: 0x10cc50200> (1B8F959F-618F-4A0D-AD89-E09DEC0EAB34)
default	18:38:07.703974+0800	hootowl	Should not send trait collection or coordinate space update, interface style 1 -> 1, <UIWindowScene: 0x10cc50200> (1B8F959F-618F-4A0D-AD89-E09DEC0EAB34)
default	18:38:07.721164+0800	hootowl	Performing snapshot request 0x109b31d40 (type 1)
default	18:38:07.721352+0800	hootowl	[(FBSceneManager):sceneID:com.sharkda.hootowl-1B8F959F-618F-4A0D-AD89-E09DEC0EAB34] Sending action(s): <FBSSceneSnapshotRequestAction: 0x90840000>
default	18:38:07.723978+0800	hootowl	Received state update for 36996 (app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>, unknown-NotVisible
default	18:38:07.750174+0800	hootowl	Received state update for 36996 (app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>, unknown-NotVisible
default	18:38:07.762355+0800	hootowl	Snapshot request 0x109b31d40 complete
default	18:38:07.762635+0800	hootowl	Push traits update to screen for new style 1, <UIWindowScene: 0x10cc50200> (1B8F959F-618F-4A0D-AD89-E09DEC0EAB34)
default	18:38:07.770232+0800	hootowl	Should not send trait collection or coordinate space update, interface style 2 -> 2, <UIWindowScene: 0x10cc50200> (1B8F959F-618F-4A0D-AD89-E09DEC0EAB34)
default	18:38:07.778903+0800	hootowl	MncplCyclopsScreen 62
🏠 body eval — items:6 firstObs:12s firstCar:18
default	18:38:07.799578+0800	hootowl	Performing snapshot request 0x109afd740 (type 1)
default	18:38:07.799819+0800	hootowl	[(FBSceneManager):sceneID:com.sharkda.hootowl-1B8F959F-618F-4A0D-AD89-E09DEC0EAB34] Sending action(s): <FBSSceneSnapshotRequestAction: 0x90840001>
default	18:38:07.839838+0800	hootowl	Snapshot request 0x109afd740 complete
default	18:38:07.839876+0800	hootowl	Ending background task with UIBackgroundTaskIdentifier: 8
default	18:38:07.840091+0800	hootowl	Ending task with identifier 8 and description: <_UIBackgroundTaskInfo: 0x13bc75fc0>: taskID = 8, taskName = com.apple.uikit.applicationSnapshot, creationTime = 640139 (elapsed = 0), _expireHandler: <__NSMallocBlock__: 0x11c379f80>
default	18:38:07.840220+0800	hootowl	Decrementing reference count for assertion <BKSProcessAssertion: 0x1399892c0> (used by background task with identifier 8: <_UIBackgroundTaskInfo: 0x13bc75fc0>: taskID = 8, taskName = com.apple.uikit.applicationSnapshot, creationTime = 640139 (elapsed = 0))
default	18:38:07.842855+0800	hootowl	Push traits update to screen for new style 1, <UIWindowScene: 0x10cc50200> (1B8F959F-618F-4A0D-AD89-E09DEC0EAB34)
default	18:38:07.843735+0800	hootowl	Should not send trait collection or coordinate space update, interface style 1 -> 1, <UIWindowScene: 0x10cc50200> (1B8F959F-618F-4A0D-AD89-E09DEC0EAB34)
default	18:38:07.851737+0800	hootowl	MncplCyclopsScreen 62
🏠 body eval — items:6 firstObs:12s firstCar:18
default	18:38:07.868309+0800	hootowl	[0x10ce1c690] [keyboardFocus] Disabling event deferring records requested: adding recreation reason: detachedContext; for reason: _UIEventDeferringManager: 0x10ce1c690: disabling keyboardFocus: context detached for window: 0x1099f0400; contextID: 0x6EC72245
default	18:38:07.870372+0800	hootowl	Will add backgroundTask with taskName: com.apple.UIKit.CABackingStoreCollect, expirationHandler: (null)
default	18:38:07.870481+0800	hootowl	Reusing background assertion <BKSProcessAssertion: 0x1399892c0>
default	18:38:07.870611+0800	hootowl	Incrementing reference count for background assertion <BKSProcessAssertion: 0x1399892c0>
default	18:38:07.870702+0800	hootowl	Created background task <_UIBackgroundTaskInfo: 0x13bc77f00>: taskID = 9, taskName = com.apple.UIKit.CABackingStoreCollect, creationTime = 640139 (elapsed = 0).
default	18:38:07.874111+0800	hootowl	sceneOfRecord: sceneID: sceneID:com.sharkda.hootowl-1B8F959F-618F-4A0D-AD89-E09DEC0EAB34  persistentID: 1B8F959F-618F-4A0D-AD89-E09DEC0EAB34
default	18:38:07.875637+0800	hootowl	Not push traits update to screen for new style 1, <UIWindowScene: 0x10cc50200> (1B8F959F-618F-4A0D-AD89-E09DEC0EAB34)
default	18:38:07.875855+0800	hootowl	Target list changed:
default	18:38:07.876329+0800	hootowl	Ending background task with UIBackgroundTaskIdentifier: 4
default	18:38:07.876571+0800	hootowl	Ending task with identifier 4 and description: <_UIBackgroundTaskInfo: 0x13bc75100>: taskID = 4, taskName = _UIRemoteKeyboard XPC disconnection, creationTime = 640139 (elapsed = 0), _expireHandler: (null)
default	18:38:07.876621+0800	hootowl	Decrementing reference count for assertion <BKSProcessAssertion: 0x1399892c0> (used by background task with identifier 4: <_UIBackgroundTaskInfo: 0x13bc75100>: taskID = 4, taskName = _UIRemoteKeyboard XPC disconnection, creationTime = 640139 (elapsed = 0))
default	18:38:07.889043+0800	hootowl	Ending background task with UIBackgroundTaskIdentifier: 9
default	18:38:07.889107+0800	hootowl	Ending task with identifier 9 and description: <_UIBackgroundTaskInfo: 0x13bc77f00>: taskID = 9, taskName = com.apple.UIKit.CABackingStoreCollect, creationTime = 640139 (elapsed = 1), _expireHandler: (null)
default	18:38:07.889137+0800	hootowl	Decrementing reference count for assertion <BKSProcessAssertion: 0x1399892c0> (used by background task with identifier 9: <_UIBackgroundTaskInfo: 0x13bc77f00>: taskID = 9, taskName = com.apple.UIKit.CABackingStoreCollect, creationTime = 640139 (elapsed = 1))
default	18:38:07.889163+0800	hootowl	Will invalidate assertion: <BKSProcessAssertion: 0x1399892c0> for task identifier: 9
default	18:38:07.964657+0800	hootowl	Received state update for 36996 (app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>, unknown-NotVisible
fault	18:38:08.068723+0800	hootowl	__delegate_identifier__:Performance Diagnostics__:::____message__:{"message":"Interprocess communication on the main thread can cause non-deterministic delays.","antipattern trigger":"-[CLLocationManager authorizationStatus]","message type":"suppressable","issue type":1,"category type":17,"subcategory type":0,"show in console":"0"}'36 91 78 76 BF CE 3E E2 B9 46 9E 92 90 98 95 3C 38 86 16 00 36 91 78 76 BF CE 3E E2 B9 46 9E 92 90 98 95 3C 50 20 0C 00 36 91 78 76 BF CE 3E E2 B9 46 9E 92 90 98 95 3C A8 60 36 00 82 A2 1C E4 4E 43 38 FB 98 62 F0 BE 7B 90 9D F1 0C 7F 21 00 82 A2 1C E4 4E 43 38 FB 98 62 F0 BE 7B 90 9D F1 90 8D 21 00 82 A2 1C E4 4E 43 38 FB 98 62 F0 BE 7B 90 9D F1 54 00 01 00 82 A2 1C E4 4E 43 38 FB 98 62 F0 BE 7B 90 9D F1 D4 CB 01 00 82 A2 1C E4 4E 43 38 FB 98 62 F0 BE 7B 90 9D F1 18 C8 01 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 04 2D 1E 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D BC EB 01 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 24 EB 01 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC A0 81 04 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC EC 8A 04 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC A0 70 04 00 8F 1E 0B 3F AD D6 37 10 A7 90 00 93 33 59 7A B4 A4 D8 2B 00 8F 1E 0B 3F AD D6 37 10 A7 90 00 93 33 59 7A B4 F4 D3 2B 00 8F 1E 0B 3F AD D6 37 10 A7 90 00 93 33 59 7A B4 00 F8 0A 00 8F 1E 0B 3F AD D6 37 10 A7 90 00 93 33 59 7A B4 98 E1 06 00 8F 1E 0B 3F AD D6 37 10 A7 90 00 93 33 59 7A B4 20 A5 09 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC F8 25 0E 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 78 42 60 01 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC E0 CB B1 01 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 58 CA B1 01 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC EC 92 19 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC E0 8F 19 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 64 97 24 00 CD B8 0F 7A 3D E2 32 F4 9A 09 7D E0 61 00 97 0C 7C 0A 02 00 CD B8 0F 7A 3D E2 32 F4 9A 09 7D E0 61 00 97 0C AC 08 02 00 CD B8 0F 7A 3D E2 32 F4 9A 09 7D E0 61 00 97 0C E8 04 02 00 CD B8 0F 7A 3D E2 32 F4 9A 09 7D E0 61 00 97 0C 8C D3 02 00 CD B8 0F 7A 3D E2 32 F4 9A 09 7D E0 61 00 97 0C 18 D1 02 00 CD B8 0F 7A 3D E2 32 F4 9A 09 7D E0 61 00 97 0C 20 45 02 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 C0 84 00 00 2F E3 5D 43 52 CF 3D 5A BF BF 04 B3 94 3C 4A F1 84 BF 02 00 2F E3 5D 43 52 CF 3D 5A BF BF 04 B3 94 3C 4A F1 00 BE 02 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 90 03 0A 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 04 03 0A 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 D8 55 06 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 A0 F1 02 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 4C E5 02 00 41 11 65 E2 EE 8E 38 0E B2 54 99 77 27 39 71 E3 98 14 00 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 70 16 12 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 58 C1 08 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 70 05 03 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D F4 D0 02 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 48 CC 02 00 36 91 78 76 BF CE 3E E2 B9 46 9E 92 90 98 95 3C F8 71 36 00 36 91 78 76 BF CE 3E E2 B9 46 9E 92 90 98 95 3C A4 72 36 00 0F 8D 35 B6 55 6F 3E 34 8E AA 80 AB 54 04 7D C5 1C 4C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
default	18:38:08.187701+0800	hootowl	Received state update for 36996 (app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>, unknown-NotVisible
fault	18:38:08.192817+0800	hootowl	__delegate_identifier__:Performance Diagnostics__:::____message__:{"message":"Interprocess communication on the main thread can cause non-deterministic delays.","antipattern trigger":"-[CLLocationManager authorizationStatus]","message type":"suppressable","issue type":4,"category type":17,"subcategory type":0,"show in console":"0"}'36 91 78 76 BF CE 3E E2 B9 46 9E 92 90 98 95 3C 38 86 16 00 36 91 78 76 BF CE 3E E2 B9 46 9E 92 90 98 95 3C 50 20 0C 00 36 91 78 76 BF CE 3E E2 B9 46 9E 92 90 98 95 3C A8 60 36 00 82 A2 1C E4 4E 43 38 FB 98 62 F0 BE 7B 90 9D F1 0C 7F 21 00 82 A2 1C E4 4E 43 38 FB 98 62 F0 BE 7B 90 9D F1 90 8D 21 00 82 A2 1C E4 4E 43 38 FB 98 62 F0 BE 7B 90 9D F1 54 00 01 00 82 A2 1C E4 4E 43 38 FB 98 62 F0 BE 7B 90 9D F1 D4 CB 01 00 82 A2 1C E4 4E 43 38 FB 98 62 F0 BE 7B 90 9D F1 18 C8 01 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 04 2D 1E 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D BC EB 01 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 24 EB 01 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC A0 81 04 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC EC 8A 04 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC A0 70 04 00 8F 1E 0B 3F AD D6 37 10 A7 90 00 93 33 59 7A B4 A4 D8 2B 00 8F 1E 0B 3F AD D6 37 10 A7 90 00 93 33 59 7A B4 F4 D3 2B 00 8F 1E 0B 3F AD D6 37 10 A7 90 00 93 33 59 7A B4 00 F8 0A 00 8F 1E 0B 3F AD D6 37 10 A7 90 00 93 33 59 7A B4 98 E1 06 00 8F 1E 0B 3F AD D6 37 10 A7 90 00 93 33 59 7A B4 20 A5 09 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC F8 25 0E 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 78 42 60 01 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC E0 CB B1 01 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 58 CA B1 01 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC EC 92 19 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC E0 8F 19 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 64 97 24 00 CD B8 0F 7A 3D E2 32 F4 9A 09 7D E0 61 00 97 0C 7C 0A 02 00 CD B8 0F 7A 3D E2 32 F4 9A 09 7D E0 61 00 97 0C AC 08 02 00 CD B8 0F 7A 3D E2 32 F4 9A 09 7D E0 61 00 97 0C E8 04 02 00 CD B8 0F 7A 3D E2 32 F4 9A 09 7D E0 61 00 97 0C 8C D3 02 00 CD B8 0F 7A 3D E2 32 F4 9A 09 7D E0 61 00 97 0C 18 D1 02 00 CD B8 0F 7A 3D E2 32 F4 9A 09 7D E0 61 00 97 0C 20 45 02 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 C0 84 00 00 2F E3 5D 43 52 CF 3D 5A BF BF 04 B3 94 3C 4A F1 84 BF 02 00 2F E3 5D 43 52 CF 3D 5A BF BF 04 B3 94 3C 4A F1 00 BE 02 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 90 03 0A 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 04 03 0A 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 D8 55 06 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 A0 F1 02 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 4C E5 02 00 41 11 65 E2 EE 8E 38 0E B2 54 99 77 27 39 71 E3 98 14 00 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 70 16 12 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 58 C1 08 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 70 05 03 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D F4 D0 02 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 48 CC 02 00 36 91 78 76 BF CE 3E E2 B9 46 9E 92 90 98 95 3C F8 71 36 00 36 91 78 76 BF CE 3E E2 B9 46 9E 92 90 98 95 3C A4 72 36 00 0F 8D 35 B6 55 6F 3E 34 8E AA 80 AB 54 04 7D C5 1C 4C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
fault	18:38:08.223098+0800	hootowl	__delegate_identifier__:Performance Diagnostics__:::____message__:{"message":"Performing I/O on the main thread can cause hangs.","antipattern trigger":"+[NSKeyedArchiver archivedDataWithRootObject:requiringSecureCoding:error:]","message type":"suppressable","issue type":1,"category type":17,"subcategory type":3,"show in console":"0"}'D4 8C 7E F8 2B B4 38 1E A7 DF B4 C6 4A 7A 2C 23 98 86 00 00 D4 8C 7E F8 2B B4 38 1E A7 DF B4 C6 4A 7A 2C 23 1C 86 00 00 DC 4F 50 56 DB E7 36 8A 99 ED A6 79 F2 C1 4F B0 00 75 02 00 DC 4F 50 56 DB E7 36 8A 99 ED A6 79 F2 C1 4F B0 30 74 02 00 DC 4F 50 56 DB E7 36 8A 99 ED A6 79 F2 C1 4F B0 CC 73 02 00 DC 4F 50 56 DB E7 36 8A 99 ED A6 79 F2 C1 4F B0 38 AB 00 00 DC 4F 50 56 DB E7 36 8A 99 ED A6 79 F2 C1 4F B0 94 28 01 00 DC 4F 50 56 DB E7 36 8A 99 ED A6 79 F2 C1 4F B0 80 27 01 00 36 91 78 76 BF CE 3E E2 B9 46 9E 92 90 98 95 3C 78 87 16 00 36 91 78 76 BF CE 3E E2 B9 46 9E 92 90 98 95 3C 50 20 0C 00 36 91 78 76 BF CE 3E E2 B9 46 9E 92 90 98 95 3C A8 60 36 00 82 A2 1C E4 4E 43 38 FB 98 62 F0 BE 7B 90 9D F1 0C 7F 21 00 82 A2 1C E4 4E 43 38 FB 98 62 F0 BE 7B 90 9D F1 90 8D 21 00 82 A2 1C E4 4E 43 38 FB 98 62 F0 BE 7B 90 9D F1 54 00 01 00 82 A2 1C E4 4E 43 38 FB 98 62 F0 BE 7B 90 9D F1 D4 CB 01 00 82 A2 1C E4 4E 43 38 FB 98 62 F0 BE 7B 90 9D F1 18 C8 01 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 04 2D 1E 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D BC EB 01 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 24 EB 01 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC A0 81 04 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC EC 8A 04 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC A0 70 04 00 8F 1E 0B 3F AD D6 37 10 A7 90 00 93 33 59 7A B4 A4 D8 2B 00 8F 1E 0B 3F AD D6 37 10 A7 90 00 93 33 59 7A B4 F4 D3 2B 00 8F 1E 0B 3F AD D6 37 10 A7 90 00 93 33 59 7A B4 00 F8 0A 00 8F 1E 0B 3F AD D6 37 10 A7 90 00 93 33 59 7A B4 98 E1 06 00 8F 1E 0B 3F AD D6 37 10 A7 90 00 93 33 59 7A B4 20 A5 09 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC F8 25 0E 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 78 42 60 01 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC E0 CB B1 01 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 58 CA B1 01 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC EC 92 19 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC E0 8F 19 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 64 97 24 00 CD B8 0F 7A 3D E2 32 F4 9A 09 7D E0 61 00 97 0C 7C 0A 02 00 CD B8 0F 7A 3D E2 32 F4 9A 09 7D E0 61 00 97 0C AC 08 02 00 CD B8 0F 7A 3D E2 32 F4 9A 09 7D E0 61 00 97 0C E8 04 02 00 CD B8 0F 7A 3D E2 32 F4 9A 09 7D E0 61 00 97 0C 8C D3 02 00 CD B8 0F 7A 3D E2 32 F4 9A 09 7D E0 61 00 97 0C 18 D1 02 00 CD B8 0F 7A 3D E2 32 F4 9A 09 7D E0 61 00 97 0C 20 45 02 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 C0 84 00 00 2F E3 5D 43 52 CF 3D 5A BF BF 04 B3 94 3C 4A F1 84 BF 02 00 2F E3 5D 43 52 CF 3D 5A BF BF 04 B3 94 3C 4A F1 00 BE 02 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 90 03 0A 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 04 03 0A 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 D8 55 06 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 A0 F1 02 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 4C E5 02 00 41 11 65 E2 EE 8E 38 0E B2 54 99 77 27 39 71 E3 98 14 00 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 70 16 12 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 58 C1 08 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 70 05 03 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D F4 D0 02 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 48 CC 02 00 36 91 78 76 BF CE 3E E2 B9 46 9E 92 90 98 95 3C F8 71 36 00 36 91 78 76 BF CE 3E E2 B9 46 9E 92 90 98 95 3C A4 72 36 00 0F 8D 35 B6 55 6F 3E 34 8E AA 80 AB 54 04 7D C5 1C 4C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
fault	18:38:08.237071+0800	hootowl	__delegate_identifier__:Performance Diagnostics__:::____message__:{"message":"Performing I/O on the main thread can cause slow launches.","antipattern trigger":"+[NSKeyedArchiver archivedDataWithRootObject:requiringSecureCoding:error:]","message type":"suppressable","issue type":4,"category type":17,"subcategory type":3,"show in console":"0"}'D4 8C 7E F8 2B B4 38 1E A7 DF B4 C6 4A 7A 2C 23 98 86 00 00 D4 8C 7E F8 2B B4 38 1E A7 DF B4 C6 4A 7A 2C 23 1C 86 00 00 DC 4F 50 56 DB E7 36 8A 99 ED A6 79 F2 C1 4F B0 00 75 02 00 DC 4F 50 56 DB E7 36 8A 99 ED A6 79 F2 C1 4F B0 30 74 02 00 DC 4F 50 56 DB E7 36 8A 99 ED A6 79 F2 C1 4F B0 CC 73 02 00 DC 4F 50 56 DB E7 36 8A 99 ED A6 79 F2 C1 4F B0 38 AB 00 00 DC 4F 50 56 DB E7 36 8A 99 ED A6 79 F2 C1 4F B0 94 28 01 00 DC 4F 50 56 DB E7 36 8A 99 ED A6 79 F2 C1 4F B0 80 27 01 00 36 91 78 76 BF CE 3E E2 B9 46 9E 92 90 98 95 3C 78 87 16 00 36 91 78 76 BF CE 3E E2 B9 46 9E 92 90 98 95 3C 50 20 0C 00 36 91 78 76 BF CE 3E E2 B9 46 9E 92 90 98 95 3C A8 60 36 00 82 A2 1C E4 4E 43 38 FB 98 62 F0 BE 7B 90 9D F1 0C 7F 21 00 82 A2 1C E4 4E 43 38 FB 98 62 F0 BE 7B 90 9D F1 90 8D 21 00 82 A2 1C E4 4E 43 38 FB 98 62 F0 BE 7B 90 9D F1 54 00 01 00 82 A2 1C E4 4E 43 38 FB 98 62 F0 BE 7B 90 9D F1 D4 CB 01 00 82 A2 1C E4 4E 43 38 FB 98 62 F0 BE 7B 90 9D F1 18 C8 01 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 04 2D 1E 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D BC EB 01 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 24 EB 01 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC A0 81 04 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC EC 8A 04 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC A0 70 04 00 8F 1E 0B 3F AD D6 37 10 A7 90 00 93 33 59 7A B4 A4 D8 2B 00 8F 1E 0B 3F AD D6 37 10 A7 90 00 93 33 59 7A B4 F4 D3 2B 00 8F 1E 0B 3F AD D6 37 10 A7 90 00 93 33 59 7A B4 00 F8 0A 00 8F 1E 0B 3F AD D6 37 10 A7 90 00 93 33 59 7A B4 98 E1 06 00 8F 1E 0B 3F AD D6 37 10 A7 90 00 93 33 59 7A B4 20 A5 09 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC F8 25 0E 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 78 42 60 01 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC E0 CB B1 01 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 58 CA B1 01 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC EC 92 19 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC E0 8F 19 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 64 97 24 00 CD B8 0F 7A 3D E2 32 F4 9A 09 7D E0 61 00 97 0C 7C 0A 02 00 CD B8 0F 7A 3D E2 32 F4 9A 09 7D E0 61 00 97 0C AC 08 02 00 CD B8 0F 7A 3D E2 32 F4 9A 09 7D E0 61 00 97 0C E8 04 02 00 CD B8 0F 7A 3D E2 32 F4 9A 09 7D E0 61 00 97 0C 8C D3 02 00 CD B8 0F 7A 3D E2 32 F4 9A 09 7D E0 61 00 97 0C 18 D1 02 00 CD B8 0F 7A 3D E2 32 F4 9A 09 7D E0 61 00 97 0C 20 45 02 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 CC DC 01 00 05 13 53 ED 07 42 38 96 91 C0 79 46 53 83 7A 30 C0 84 00 00 2F E3 5D 43 52 CF 3D 5A BF BF 04 B3 94 3C 4A F1 84 BF 02 00 2F E3 5D 43 52 CF 3D 5A BF BF 04 B3 94 3C 4A F1 00 BE 02 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 90 03 0A 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 04 03 0A 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 D8 55 06 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 A0 F1 02 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 4C E5 02 00 41 11 65 E2 EE 8E 38 0E B2 54 99 77 27 39 71 E3 98 14 00 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 70 16 12 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 58 C1 08 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 70 05 03 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D F4 D0 02 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 48 CC 02 00 36 91 78 76 BF CE 3E E2 B9 46 9E 92 90 98 95 3C F8 71 36 00 36 91 78 76 BF CE 3E E2 B9 46 9E 92 90 98 95 3C A4 72 36 00 0F 8D 35 B6 55 6F 3E 34 8E AA 80 AB 54 04 7D C5 1C 4C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
default	18:38:10.796658+0800	hootowl	sceneOfRecord: sceneID: sceneID:com.sharkda.hootowl-1B8F959F-618F-4A0D-AD89-E09DEC0EAB34  persistentID: 1B8F959F-618F-4A0D-AD89-E09DEC0EAB34
default	18:38:10.796891+0800	hootowl	Deactivation reason added: 5; deactivation reasons: 6144 -> 6176; animating application lifecycle event: 1
default	18:38:10.796937+0800	hootowl	Ignoring already applied deactivation reason: 12; deactivation reasons: 6176
default	18:38:10.797147+0800	hootowl	{"msg":"CLLocationManager", "event":"activity", "_cmd":"onWillEnterForeground:", "self":"0x1038ead60", "notification":"NSConcreteNotification 0x13bc7ae60 {name = UIApplicationWillEnterForegroundNotification; object = <_TtC7SwiftUIP33_ACC2C5639A7D76F611E170E831FCA49118SwiftUIApplication: 0x10cc50000>}"}
default	18:38:10.797190+0800	hootowl	0x10cd19c18 - [pageProxyID=2087, webPageID=2088, PID=37010] WebPageProxy::applicationWillEnterForegroundForMedia: isSuspendedUnderLock? 0
default	18:38:10.797236+0800	hootowl	Deactivation reason removed: 11; deactivation reasons: 6176 -> 4128; animating application lifecycle event: 1
default	18:38:10.797257+0800	hootowl	establishing connection to agent
default	18:38:10.797285+0800	hootowl	[0x139c843c0] Session created.
default	18:38:10.797300+0800	hootowl	[0x139c843c0] Session created from connection [0x11bc84dc0]
default	18:38:10.797350+0800	hootowl	[0x11bc84dc0] activating connection: mach=true listener=false peer=false name=com.apple.uiintelligencesupport.agent
default	18:38:10.797378+0800	hootowl	[0x139c843c0] Session activated
default	18:38:10.797760+0800	hootowl	[0x10ce1c690] [keyboardFocus] Recreation of event deferring records requested: removing recreation reason: detachedContext; for reason: _UIEventDeferringManager: 0x10ce1c690: recreating keyboardFocus: context attached for window: 0x1099f0400; contextID: 0x6989FC6
default	18:38:10.798031+0800	hootowl	Connection established with agent PID: 36406
default	18:38:10.804254+0800	hootowl	Received state update for 36996 (app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>, unknown-NotVisible
default	18:38:10.821199+0800	hootowl	Target list changed: <CADisplay:LCD primary>
default	18:38:10.823581+0800	hootowl	startConnection
default	18:38:10.824400+0800	hootowl	[0x112198dc0] activating connection: mach=true listener=false peer=false name=com.apple.UIKit.KeyboardManagement.hosted
default	18:38:10.824493+0800	hootowl	sceneOfRecord: sceneID: sceneID:com.sharkda.hootowl-1B8F959F-618F-4A0D-AD89-E09DEC0EAB34  persistentID: 1B8F959F-618F-4A0D-AD89-E09DEC0EAB34
default	18:38:10.825509+0800	hootowl	Not push traits update to screen for new style 1, <UIWindowScene: 0x10cc50200> (1B8F959F-618F-4A0D-AD89-E09DEC0EAB34)
default	18:38:10.825575+0800	hootowl	sceneOfRecord: sceneID: sceneID:com.sharkda.hootowl-1B8F959F-618F-4A0D-AD89-E09DEC0EAB34  persistentID: 1B8F959F-618F-4A0D-AD89-E09DEC0EAB34
default	18:38:10.830957+0800	hootowl	handleKeyboardChange: set currentKeyboard:N (wasKeyboard:N)
default	18:38:10.830998+0800	hootowl	forceReloadInputViews
default	18:38:10.832137+0800	hootowl	Reloading input views for key-window scene responder: <(null): 0x0; > force:Y
default	18:38:10.893491+0800	hootowl	Received state update for 36996 (app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>, unknown-NotVisible
default	18:38:11.125515+0800	hootowl	Not push traits update to screen for new style 1, <UIWindowScene: 0x10cc50200> (1B8F959F-618F-4A0D-AD89-E09DEC0EAB34)
default	18:38:11.125602+0800	hootowl	sceneOfRecord: sceneID: sceneID:com.sharkda.hootowl-1B8F959F-618F-4A0D-AD89-E09DEC0EAB34  persistentID: 1B8F959F-618F-4A0D-AD89-E09DEC0EAB34
default	18:38:11.125618+0800	hootowl	Deactivation reason removed: 12; deactivation reasons: 4128 -> 32; animating application lifecycle event: 1
default	18:38:11.125636+0800	hootowl	Send setDeactivating: N (-DeactivationReason:SuspendedEventsOnly)
default	18:38:11.126733+0800	hootowl	Deactivation reason removed: 5; deactivation reasons: 32 -> 0; animating application lifecycle event: 0
default	18:38:11.126796+0800	hootowl	App transitioned to foreground, resuming HangTracing.
default	18:38:11.126843+0800	hootowl	Updating event->rollingFGTimestamp from INVALID_FOREGROUND_TIMESTAMP to 15363436859891
default	18:38:11.129512+0800	hootowl	{"msg":"CLLocationManager", "event":"activity", "_cmd":"onDidBecomeActive:", "self":"0x1038ead60", "notification":"NSConcreteNotification 0x11218a7a0 {name = UIApplicationDidBecomeActiveNotification; object = <_TtC7SwiftUIP33_ACC2C5639A7D76F611E170E831FCA49118SwiftUIApplication: 0x10cc50000>}"}
default	18:38:11.131046+0800	hootowl	PlaybackSessionManagerProxy::applicationDidBecomeActive(2906663760)
default	18:38:11.131095+0800	hootowl	PlaybackSessionManagerProxy::applicationDidBecomeActive(3164541321)
default	18:38:11.131546+0800	hootowl	Municipal+Lifecycle 33
▶️ app → active: resuming GPS + 2 active proto timer(s)
default	18:38:11.136632+0800	hootowl	{"msg":"CLLocationManager", "event":"activity", "_cmd":"startUpdatingLocation", "self":"0x1038ead60"}
default	18:38:11.144598+0800	hootowl	Task <8ED8F810-00F1-44AC-937C-960FE4E73BDB>.<8> resuming, timeouts(60.0, 604800.0) qos(0x15) voucher((null)) activity(00000000-0000-0000-0000-000000000000)
default	18:38:11.145759+0800	hootowl	{"msg":"#CLLocationManager invoking #delegate", "self":"0x1038ead60", "delegate":"0x109a28000", "selector":"locationManager:didUpdateLocations:", "location":{"floor":2147483647,"lifespan":-1,"rawLat":25.0007528808197,"integrity":0,"referenceFrame":"Unknown","lon":121.56465855825979,"speed":-1,"type":"GPS","altitude":0,"rawCourse":-1,"confidence":100,"suitability":"Any","ellipsoidalAltitude":0,"timestamp":810124690.49766898,"rawReferenceFrame":"Unknown","lat":25.0007528808197,"verticalAccuracy":-1,"rawLon":121.56465855825979,"horizontalAccuracy":5,"speedAccuracy":-1,"courseAccuracy":-1,"fromSimulationController":true,"course":-1}, "eventType":"kCLConnectionMessageLocation"}
default	18:38:11.145849+0800	hootowl	Task <87251BE6-DA76-471C-9AC5-B78E5BC71236>.<9> resuming, timeouts(60.0, 604800.0) qos(0x15) voucher((null)) activity(00000000-0000-0000-0000-000000000000)
error	18:38:11.146089+0800	hootowl	138	assessFences(l2d:)	no fences are availabe
default	18:38:11.175877+0800	hootowl	Connection 0: creating secure tcp or quic connection
default	18:38:11.176459+0800	hootowl	Connection 14: enabling TLS
default	18:38:11.176743+0800	hootowl	Connection 14: starting, TC(0x0)
default	18:38:11.176796+0800	hootowl	[C14 DD8B19D5-AF5B-42B2-8B4F-4AFCE8BDBD1D data.ntpc.gov.tw:443 quic-connection, url: https://data.ntpc.gov.tw/api/datasets/e09b35a5-a738-48cc-b0f5-570b67ad9c78/csv/file, definite, attribution: developer, context: com.apple.CFNetwork.NSURLSession.{C8A30AB7-8A8F-46A2-A794-FF53331E2689}{(null)}{Y}{2}{0x0} (private), proc: 1B526020-2DE0-3C65-9122-F1177549D69A, delegated upid: 0] start
default	18:38:11.177412+0800	hootowl	[C14 data.ntpc.gov.tw:443 initial parent-flow ((null))] event: path:start @0.000s
default	18:38:11.177994+0800	hootowl	[C14 data.ntpc.gov.tw:443 waiting parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.004s, uuid: 38DBD408-A51F-4C75-B54C-C461EC15852B
default	18:38:11.178293+0800	hootowl	[C14 data.ntpc.gov.tw:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_connect @0.004s
default	18:38:11.178328+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C14] reporting state preparing
default	18:38:11.178631+0800	hootowl	[C14 data.ntpc.gov.tw:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_child @0.005s
default	18:38:11.178909+0800	hootowl	[C14.1 data.ntpc.gov.tw:443 initial path ((null))] event: path:start @0.005s
default	18:38:11.179994+0800	hootowl	[C14.1 data.ntpc.gov.tw:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.006s, uuid: 38DBD408-A51F-4C75-B54C-C461EC15852B
default	18:38:11.180531+0800	hootowl	[C14.1 data.ntpc.gov.tw:443 in_progress transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: transform:start @0.006s
default	18:38:11.181315+0800	hootowl	[C14.1.1 data.ntpc.gov.tw:443 initial path ((null))] event: path:start @0.007s
default	18:38:11.183480+0800	hootowl	[C14.1.1 data.ntpc.gov.tw:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.009s, uuid: 560C0EDE-423F-418B-900E-242D8ABD2BFD
default	18:38:11.184156+0800	hootowl	[C14.1.1 data.ntpc.gov.tw:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:start_dns @0.010s
default	18:38:11.184353+0800	hootowl	Task <87251BE6-DA76-471C-9AC5-B78E5BC71236>.<9> setting up Connection 14
default	18:38:11.184951+0800	hootowl	[C13] event: client:connection_idle @17.147s
default	18:38:11.185286+0800	hootowl	nw_protocol_tcp_notify [C13.1.1.1:3] nw_protocol_notification_type_connection_idle is true
default	18:38:11.185301+0800	hootowl	nw_protocol_tcp_set_connection_idle [C13.1.1.1:3] os_nexus_flow_set_connection_idle returned 0
default	18:38:11.185367+0800	hootowl	Task <8ED8F810-00F1-44AC-937C-960FE4E73BDB>.<8> now using Connection 13
default	18:38:11.185745+0800	hootowl	[C13] event: client:connection_reused @17.148s
default	18:38:11.186101+0800	hootowl	nw_protocol_tcp_notify [C13.1.1.1:3] nw_protocol_notification_type_connection_idle is false
default	18:38:11.186356+0800	hootowl	nw_protocol_tcp_set_connection_idle [C13.1.1.1:3] os_nexus_flow_set_connection_idle returned 0
default	18:38:11.205250+0800	hootowl	Task <8ED8F810-00F1-44AC-937C-960FE4E73BDB>.<8> sent request, body N 0
default	18:38:11.205421+0800	hootowl	nw_endpoint_resolver_update [C14.1.1 data.ntpc.gov.tw:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Adding endpoint handler for 61.60.98.243:443
default	18:38:11.206444+0800	hootowl	[C14.1.1 data.ntpc.gov.tw:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:receive_dns @0.027s
default	18:38:11.206968+0800	hootowl	[C14.1.1.1 61.60.98.243:443 initial path ((null))] event: path:start @0.031s
default	18:38:11.207432+0800	hootowl	[C14.1.1.1 61.60.98.243:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.033s, uuid: C1D2FD7C-A4C4-4ACB-B4FE-7597B31E1123
default	18:38:11.207622+0800	hootowl	[C14.1.1.1 61.60.98.243:443 in_progress channel-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_nexus @0.033s
default	18:38:11.209538+0800	hootowl	[C14.1.1.1 61.60.98.243:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:receive_nexus @0.035s
default	18:38:11.211057+0800	hootowl	[C14.1.1.1 61.60.98.243:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_connect @0.037s
default	18:38:11.211646+0800	hootowl	tcp_output [C14.1.1.1:3] flags=[SEC] seq=279489320, ack=0, win=65535 state=SYN_SENT rcv_nxt=0, snd_una=279489320
default	18:38:11.219082+0800	hootowl	tcp_input [C14.1.1.1:3] flags=[S.E] seq=2202185412, ack=279489321, win=14520 state=SYN_SENT rcv_nxt=0, snd_una=279489320
default	18:38:11.219098+0800	hootowl	nw_flow_connected [C14.1.1.1 61.60.98.243:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Transport protocol connected (tcp)
default	18:38:11.219163+0800	hootowl	[C14.1.1.1 61.60.98.243:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_transport @0.046s
default	18:38:11.219357+0800	hootowl	boringssl_session_apply_protocol_options_for_transport_block_invoke_2(2367) [C14.1.1.1:2][0x11c25d960] TLS configured [server(0) min_version(0x0303) max_version(0x0304) name(data.ntpc.gov.tw) tickets(false) false_start(false) enforce_ev(false) enforce_ats(false) ats_non_pfs_ciphersuite_allowed(false) cc_mode_enforced(false) ech(false) pqtls(true), pake(false) skip_ats_trust(false)]
default	18:38:11.219404+0800	hootowl	boringssl_context_info_handler(2806) [C14.1.1.1:2][0x11c25d960] Client handshake started
default	18:38:11.219527+0800	hootowl	boringssl_context_info_handler(2823) [C14.1.1.1:2][0x11c25d960] Client handshake state: TLS client enter_early_data
default	18:38:11.219583+0800	hootowl	boringssl_context_info_handler(2823) [C14.1.1.1:2][0x11c25d960] Client handshake state: TLS client read_server_hello
default	18:38:11.234364+0800	hootowl	boringssl_context_info_handler(2823) [C14.1.1.1:2][0x11c25d960] Client handshake state: TLS client read_session_ticket
default	18:38:11.234417+0800	hootowl	boringssl_context_info_handler(2823) [C14.1.1.1:2][0x11c25d960] Client handshake state: TLS client process_change_cipher_spec
default	18:38:11.234482+0800	hootowl	boringssl_context_info_handler(2823) [C14.1.1.1:2][0x11c25d960] Client handshake state: TLS client read_server_finished
default	18:38:11.234551+0800	hootowl	boringssl_context_info_handler(2823) [C14.1.1.1:2][0x11c25d960] Client handshake state: TLS client send_client_finished
default	18:38:11.234575+0800	hootowl	boringssl_context_info_handler(2823) [C14.1.1.1:2][0x11c25d960] Client handshake state: TLS client finish_flight
default	18:38:11.234628+0800	hootowl	boringssl_context_info_handler(2823) [C14.1.1.1:2][0x11c25d960] Client handshake state: TLS client finish_client_handshake
default	18:38:11.234637+0800	hootowl	boringssl_context_info_handler(2823) [C14.1.1.1:2][0x11c25d960] Client handshake state: TLS client done
default	18:38:11.234647+0800	hootowl	boringssl_context_info_handler(2812) [C14.1.1.1:2][0x11c25d960] Client handshake done
default	18:38:11.235095+0800	hootowl	nw_protocol_boringssl_signal_connected(895) [C14.1.1.1:2][0x11c25d960] TLS connected [server(0) version(0x0303) ciphersuite(TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256) group(0x0017) signature_alg(0x0401) alpn(nil) resumed(1) offered_ticket(0) in_early_data(0) early_data_accepted(0) false_started(0) ocsp_received(0) sct_received(0) connect_time(15ms) flight_time(15ms) rtt(15ms) write_stalls(0) read_stalls(6) pake(0x0000)]
default	18:38:11.235160+0800	hootowl	nw_flow_connected [C14.1.1.1 61.60.98.243:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (CFNetworkConnection-398509258)
default	18:38:11.235513+0800	hootowl	[C14.1.1.1 61.60.98.243:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.062s
default	18:38:11.235577+0800	hootowl	[C14.1.1 data.ntpc.gov.tw:443 ready resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.062s
default	18:38:11.235594+0800	hootowl	[C14.1 data.ntpc.gov.tw:443 ready transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.062s
default	18:38:11.235785+0800	hootowl	[C14.1.1.1 61.60.98.243:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.063s
default	18:38:11.236298+0800	hootowl	[C14.1.1 data.ntpc.gov.tw:443 ready resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.063s
default	18:38:11.236327+0800	hootowl	[C14.1 data.ntpc.gov.tw:443 ready transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.063s
default	18:38:11.236351+0800	hootowl	nw_flow_connected [C14 61.60.98.243:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (endpoint_flow)
default	18:38:11.236486+0800	hootowl	[C14 61.60.98.243:443 ready parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_connect @0.063s
default	18:38:11.236569+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C14] reporting state ready
default	18:38:11.236579+0800	hootowl	[C14 61.60.98.243:443 ready parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.063s
default	18:38:11.236588+0800	hootowl	nw_connection_send_viability_changed_on_nw_queue [C14] viability_changed_handler(true)
default	18:38:11.236598+0800	hootowl	Connection 14: connected successfully
default	18:38:11.236613+0800	hootowl	Connection 14: TLS handshake complete
default	18:38:11.236624+0800	hootowl	Connection 14: ready C(N) E(N)
default	18:38:11.236649+0800	hootowl	Task <87251BE6-DA76-471C-9AC5-B78E5BC71236>.<9> now using Connection 14
default	18:38:11.236665+0800	hootowl	Connection 14: received viability advisory(Y)
default	18:38:11.236706+0800	hootowl	Task <87251BE6-DA76-471C-9AC5-B78E5BC71236>.<9> sent request, body N 0
default	18:38:11.280935+0800	hootowl	Task <8ED8F810-00F1-44AC-937C-960FE4E73BDB>.<8> received response, status 304 content K
default	18:38:11.281097+0800	hootowl	Task <8ED8F810-00F1-44AC-937C-960FE4E73BDB>.<8> done using Connection 13
default	18:38:11.281305+0800	hootowl	[C13] event: client:connection_idle @17.244s
default	18:38:11.281493+0800	hootowl	nw_protocol_tcp_notify [C13.1.1.1:3] nw_protocol_notification_type_connection_idle is true
default	18:38:11.281683+0800	hootowl	nw_protocol_tcp_set_connection_idle [C13.1.1.1:3] os_nexus_flow_set_connection_idle returned 0
default	18:38:11.281713+0800	hootowl	Task <8ED8F810-00F1-44AC-937C-960FE4E73BDB>.<8> summary for task success {transaction_duration_ms=112, response_status=304, connection=13, reused=1, reused_after_ms=0, request_start_ms=16, request_duration_ms=13, response_start_ms=111, response_duration_ms=0, request_bytes=337, request_throughput_kbps=197, response_bytes=308, response_throughput_kbps=13994, cache_hit=true}
default	18:38:11.281866+0800	hootowl	[C13] event: client:connection_idle @17.244s
default	18:38:11.282378+0800	hootowl	nw_protocol_tcp_notify [C13.1.1.1:3] nw_protocol_notification_type_connection_idle is true
default	18:38:11.282469+0800	hootowl	Task <8ED8F810-00F1-44AC-937C-960FE4E73BDB>.<8> finished successfully
default	18:38:11.282754+0800	hootowl	nw_protocol_tcp_set_connection_idle [C13.1.1.1:3] os_nexus_flow_set_connection_idle returned 0
default	18:38:11.282771+0800	hootowl	Mu1Base+Ext 152
taipei 📦 minutely Received 459955 bytes
default	18:38:11.282799+0800	hootowl	Mu1Base+Ext 177
previousHash not changed
default	18:38:11.287650+0800	hootowl	Municipal+Cyclops 79
🎨 model refreshed — obs:0s car:18 thread:main
fault	18:38:11.313909+0800	hootowl	__delegate_identifier__:Performance Diagnostics__:::____message__:{"message":"Performing I/O on the main thread can cause hangs.","antipattern trigger":"+[NSKeyedArchiver archivedDataWithRootObject:requiringSecureCoding:error:]","message type":"suppressable","issue type":1,"category type":17,"subcategory type":3,"show in console":"0"}'D4 8C 7E F8 2B B4 38 1E A7 DF B4 C6 4A 7A 2C 23 98 86 00 00 D4 8C 7E F8 2B B4 38 1E A7 DF B4 C6 4A 7A 2C 23 1C 86 00 00 DC 4F 50 56 DB E7 36 8A 99 ED A6 79 F2 C1 4F B0 00 75 02 00 DC 4F 50 56 DB E7 36 8A 99 ED A6 79 F2 C1 4F B0 30 74 02 00 DC 4F 50 56 DB E7 36 8A 99 ED A6 79 F2 C1 4F B0 CC 73 02 00 DC 4F 50 56 DB E7 36 8A 99 ED A6 79 F2 C1 4F B0 38 AB 00 00 DC 4F 50 56 DB E7 36 8A 99 ED A6 79 F2 C1 4F B0 8C D0 00 00 DC 4F 50 56 DB E7 36 8A 99 ED A6 79 F2 C1 4F B0 C0 CB 00 00 36 91 78 76 BF CE 3E E2 B9 46 9E 92 90 98 95 3C 40 88 16 00 36 91 78 76 BF CE 3E E2 B9 46 9E 92 90 98 95 3C A0 23 0C 00 36 91 78 76 BF CE 3E E2 B9 46 9E 92 90 98 95 3C 6C 60 36 00 82 A2 1C E4 4E 43 38 FB 98 62 F0 BE 7B 90 9D F1 0C 7F 21 00 82 A2 1C E4 4E 43 38 FB 98 62 F0 BE 7B 90 9D F1 90 8D 21 00 82 A2 1C E4 4E 43 38 FB 98 62 F0 BE 7B 90 9D F1 54 00 01 00 82 A2 1C E4 4E 43 38 FB 98 62 F0 BE 7B 90 9D F1 D4 CB 01 00 82 A2 1C E4 4E 43 38 FB 98 62 F0 BE 7B 90 9D F1 18 C8 01 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 04 2D 1E 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D BC EB 01 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 24 EB 01 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC A0 81 04 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC EC 8A 04 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC A0 70 04 00 8F 1E 0B 3F AD D6 37 10 A7 90 00 93 33 59 7A B4 A4 D8 2B 00 8F 1E 0B 3F AD D6 37 10 A7 90 00 93 33 59 7A B4 F4 D3 2B 00 8F 1E 0B 3F AD D6 37 10 A7 90 00 93 33 59 7A B4 00 F8 0A 00 8F 1E 0B 3F AD D6 37 10 A7 90 00 93 33 59 7A B4 98 E1 06 00 8F 1E 0B 3F AD D6 37 10 A7 90 00 93 33 59 7A B4 20 A5 09 00 8F 1E 0B 3F AD D6 37 10 A7 90 00 93 33 59 7A B4 74 90 0A 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC F0 25 0E 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 24 25 0E 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC D4 B6 0F 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 60 8C 0F 00 26 FA B8 14 4C 8F 3A 06 B4 5E CB A2 71 02 0D C4 6C 15 00 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 90 03 0A 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 04 03 0A 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 3C 56 06 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 A0 F1 02 00 10 1E B2 F1 19 15 34 A0 8B C9 63 1D 03 75 3B 84 4C E5 02 00 41 11 65 E2 EE 8E 38 0E B2 54 99 77 27 39 71 E3 98 14 00 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 70 16 12 00 0D 94 42 2F FE 7C 30 2E B8 96 3B C5 87 3C 0C FC 58 C1 08 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 70 05 03 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D F4 D0 02 00 17 AD C5 4E 93 AB 3F 13 B4 69 E3 F5 31 81 FC 4D 48 CC 02 00 36 91 78 76 BF CE 3E E2 B9 46 9E 92 90 98 95 3C F8 71 36 00 36 91 78 76 BF CE 3E E2 B9 46 9E 92 90 98 95 3C A4 72 36 00 0F 8D 35 B6 55 6F 3E 34 8E AA 80 AB 54 04 7D C5 1C 4C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
default	18:38:11.365400+0800	hootowl	Task <87251BE6-DA76-471C-9AC5-B78E5BC71236>.<9> received response, status 200 content C
default	18:38:11.365720+0800	hootowl	Task <87251BE6-DA76-471C-9AC5-B78E5BC71236>.<9> response ended
default	18:38:11.365736+0800	hootowl	Task <87251BE6-DA76-471C-9AC5-B78E5BC71236>.<9> done using Connection 14
default	18:38:11.365792+0800	hootowl	[C14] event: client:connection_idle @0.193s
default	18:38:11.366210+0800	hootowl	Task <87251BE6-DA76-471C-9AC5-B78E5BC71236>.<9> summary for task success {transaction_duration_ms=212, response_status=200, connection=14, protocol="http/1.1", domain_lookup_duration_ms=17, connect_duration_ms=26, secure_connection_duration_ms=15, private_relay=false, request_start_ms=82, request_duration_ms=0, response_start_ms=211, response_duration_ms=0, request_bytes=391, request_throughput_kbps=104540, response_bytes=21862, response_throughput_kbps=351915, cache_hit=true}
default	18:38:11.366247+0800	hootowl	nw_protocol_tcp_notify [C14.1.1.1:3] nw_protocol_notification_type_connection_idle is true
default	18:38:11.366486+0800	hootowl	nw_protocol_tcp_set_connection_idle [C14.1.1.1:3] os_nexus_flow_set_connection_idle returned 0
default	18:38:11.366513+0800	hootowl	Task <87251BE6-DA76-471C-9AC5-B78E5BC71236>.<9> finished successfully
default	18:38:11.366586+0800	hootowl	Mu1Base+Ext 152
newTaipeiCity 📦 minutely Received 20047 bytes
default	18:38:11.366597+0800	hootowl	[C14] event: client:connection_idle @0.193s
default	18:38:11.366652+0800	hootowl	nw_protocol_tcp_notify [C14.1.1.1:3] nw_protocol_notification_type_connection_idle is true
default	18:38:11.366709+0800	hootowl	Mu1Base+Ext 177
previousHash not changed
default	18:38:11.366720+0800	hootowl	nw_protocol_tcp_set_connection_idle [C14.1.1.1:3] os_nexus_flow_set_connection_idle returned 0
default	18:38:11.373102+0800	hootowl	Municipal+Cyclops 79
🎨 model refreshed — obs:0s car:18 thread:main
default	18:38:11.443622+0800	hootowl	policyStatus:<BKSHIDEventDeliveryPolicyObserver: 0x10cd94660; environment: keyboardFocus; status: target> was:none
default	18:38:11.444226+0800	hootowl	policyStatus:<BKSHIDEventDeliveryPolicyObserver: 0x1098623a0; token: com.apple.frontboard.systemappservices/FBSceneManager:sceneID%3Acom.sharkda.hootowl-1B8F959F-618F-4A0D-AD89-E09DEC0EAB34; status: ancestor> was:none
default	18:38:11.444812+0800	hootowl	Scene target of keyboard event deferring environment did change: 1; scene: UIWindowScene: 0x10cc50200; scene identity: com.apple.frontboard.systemappservices/FBSceneManager:sceneID%3Acom.sharkda.hootowl-1B8F959F-618F-4A0D-AD89-E09DEC0EAB34
default	18:38:11.445005+0800	hootowl	[0x10ce1c690] Scene target of event deferring environments did update: scene: 0x10cc50200; current systemShellManagesKeyboardFocus: 1; systemShellManagesKeyboardFocusForScene: 1; eligibleForRecordRemoval: 1;
default	18:38:11.445024+0800	hootowl	Scene became target of keyboard event deferring environment: UIWindowScene: 0x10cc50200; scene identity: com.apple.frontboard.systemappservices/FBSceneManager:sceneID%3Acom.sharkda.hootowl-1B8F959F-618F-4A0D-AD89-E09DEC0EAB34
default	18:38:11.445039+0800	hootowl	policyStatus:<BKSHIDEventDeliveryPolicyObserver: 0x10cd94de0; environment: keyboardFocus; status: target> was:none
default	18:38:11.446358+0800	hootowl	sceneOfRecord: sceneID: sceneID:com.sharkda.hootowl-1B8F959F-618F-4A0D-AD89-E09DEC0EAB34  persistentID: 1B8F959F-618F-4A0D-AD89-E09DEC0EAB34
default	18:38:11.471052+0800	hootowl	sceneOfRecord: sceneID: sceneID:com.sharkda.hootowl-1B8F959F-618F-4A0D-AD89-E09DEC0EAB34  persistentID: 1B8F959F-618F-4A0D-AD89-E09DEC0EAB34
default	18:38:11.484987+0800	hootowl	sceneOfRecord: sceneID: sceneID:com.sharkda.hootowl-1B8F959F-618F-4A0D-AD89-E09DEC0EAB34  persistentID: 1B8F959F-618F-4A0D-AD89-E09DEC0EAB34
default	18:38:16.381139+0800	hootowl	tcp_input [C14.1.1.1:3] flags=[F.] seq=2202207515, ack=279491317, win=16516 state=ESTABLISHED rcv_nxt=2202207515, snd_una=279491317
default	18:38:16.381388+0800	hootowl	nw_protocol_tcp_log_summary [C14.1.1.1:3] 
	[A65A5108-67DC-44AC-86C5-ED78C5E6BDA4 192.168.50.191:55869<->61.60.98.243:443]
	Init: 1, Conn_Time: 8.083ms, SYNs: 1, WR_T: 0/0, RD_T: 0/0, TFO: 0/0/0, ECN: 0/1/1, Accurate ECN (client/server): Disabled/Disabled, TS: 1, TSO: 0
	rtt_cache: process, rtt_upd: 4, rtt: 8.968ms, rtt_var: 2.937ms rtt_nc: 8.968ms, rtt_var_nc: 2.937ms base rtt: 8ms
	ACKs-compressed: 1, ACKs delayed: 0 delayed ACKs sent: 0
default	18:38:16.383367+0800	hootowl	Connection 14: read-side closed
default	18:38:16.383759+0800	hootowl	Connection 14: cleaning up
default	18:38:16.384037+0800	hootowl	[C14 DD8B19D5-AF5B-42B2-8B4F-4AFCE8BDBD1D data.ntpc.gov.tw:443 quic-connection, url: https://data.ntpc.gov.tw/api/datasets/e09b35a5-a738-48cc-b0f5-570b67ad9c78/csv/file, definite, attribution: developer] cancel
default	18:38:16.389206+0800	hootowl	[C14 DD8B19D5-AF5B-42B2-8B4F-4AFCE8BDBD1D data.ntpc.gov.tw:443 quic-connection, url: https://data.ntpc.gov.tw/api/datasets/e09b35a5-a738-48cc-b0f5-570b67ad9c78/csv/file, definite, attribution: developer] cancelled
	[C14.1.1.1 C1D2FD7C-A4C4-4ACB-B4FE-7597B31E1123 192.168.50.191:55869<->61.60.98.243:443]
	Connected Path: satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good
	Privacy Stance: Not Eligible
	Duration: 5.208s, DNS @0.010s took 0.017s, TCP @0.037s took 0.009s,  took 0.015s
	bytes in/out: 22102/1996, packets in/out: 15/16, rtt: 0.008s, retransmitted bytes: 0, out-of-order bytes: 505
	ecn packets sent/acked/marked/lost: 4/4/0/0
default	18:38:16.393104+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C14] reporting state cancelled
default	18:38:16.393232+0800	hootowl	tcp_output [C14.1.1.1:3] flags=[F.] seq=279491348, ack=2202207516, win=2048 state=LAST_ACK rcv_nxt=2202207516, snd_una=279491317
default	18:38:16.441878+0800	hootowl	tcp_close [C14.1.1.1:3] TCP Packets:
	 snd    0.000s seq  279489320:279489321  ack 0          win 65535 len 0    [SEC]
	 rcv    0.008s seq 2202185412:2202185413 ack 279489321  win 14520 len 0    [S.E]
	 snd    0.000s seq  279489321:279489321  ack 2202185413 win 2070  len 0    [.]
	 snd    0.000s seq  279489321:279490761  ack 2202185413 win 2070  len 1440 [.] ECT0
	 snd    0.000s seq  279490761:279490846  ack 2202185413 win 2070  len 85   [P.] ECT0
	 rcv    0.013s seq 2202185413:2202185413 ack 279490846  win 16045 len 0    [.]
	 rcv    0.002s seq 2202185413:2202185564 ack 279490846  win 16045 len 151  [P.] ECT0
	 snd    0.000s seq  279490846:279490846  ack 2202185564 win 2068  len 0    [.]
	 snd    0.000s seq  279490846:279490897  ack 2202185564 win 2068  len 51   [P.] ECT0
	 snd    0.002s seq  279490897:279491317  ack 2202185564 win 2068  len 420  [P.] ECT0
	 rcv    0.009s seq 2202185564:2202185564 ack 279490897  win 16096 len 0    [.]
	 rcv    0.000s seq 2202185564:2202185564 ack 279491317  win 16516 len 0    [.]
	 rcv    0.000s seq 2202185564:2202185564 ack 279490897  win 16096 len 0    [.]
	 rcv    0.000s seq 2202185564:2202185564 ack 279491317  win 16516 len 0    [.]
	 rcv    0.069s seq 2202185564:2202186988 ack 279491317  win 16516 len 1424 [.] ECT0
	 snd    0.000s seq  279491317:279491317  ack 2202186988 win 2046  len 0    [.]
	 rcv    0.002s seq 2202186988:2202199880 ack 279491317  win 16516 len 12892 [P.] ECT0
	 snd    0.000s seq  279491317:279491317  ack 2202199880 win 1847  len 0    [.]
	 snd    0.000s seq  279491317:279491317  ack 2202199880 win 2048  len 0    [.]
	 rcv    0.015s seq 2202199880:2202201320 ack 279491317  win 16516 len 1440 [.] ECT0
	 snd    0.000s seq  279491317:279491317  ack 2202201320 win 2026  len 0    [.]
	 rcv    0.034s seq 2202201320:2202205570 ack 279491317  win 16516 len 4250 [.] ECT0
	 snd    0.000s seq  279491317:279491317  ack 2202205570 win 1982  len 0    [.]
	 rcv    0.000s seq 2202207010:2202207515 ack 279491317  win 16516 len 505  [P.] ECT0
	 snd    0.000s seq  279491317:279491317  ack 2202205570 win 1982  len 0    [.]
	 rcv    0.000s seq 2202205570:2202207010 ack 279491317  win 16516 len 1440 [.] ECT0
	 snd    0.000s seq  279491317:279491317  ack 2202207515 win 1952  len 0    [.]
	 snd    0.000s seq  279491317:279491317  ack 2202207515 win 2048  len 0    [.]
	 rcv    0.517s seq 2202207515:2202207515 ack 279491317  win 16516 len 0    [.]
	 rcv    4.492s seq 2202207515:2202207516 ack 279491317  win 16516 len 0    [F.]
	 snd    0.000s seq  279491317:279491317  ack 2202207516 win 2048  len 0    [.]
	 snd    0.008s seq  279491317:279491348  ack 2202207516 win 2048  len 31   [P.] ECT0
	 snd    0.005s seq  279491348:279491349  ack 2202207516 win 2048  len 0    [F.]
	 rcv    0.047s seq 2202207516:2202207516 ack 279491348  win 16547 len 0    [.]
	 rcv    0.000s seq 2202207516:2202207516 ack 279491349  win 16547 len 0    [.]
	Last packet 0ms ago.
default	18:38:41.804537+0800	hootowl	Connection 13: cleaning up
default	18:38:41.804790+0800	hootowl	[C13 881A0D95-9A6E-4552-8385-67DE682F2D09 tcgbusfs.blob.core.windows.net:443 quic-connection, url: https://tcgbusfs.blob.core.windows.net/blobtcmsv/TCMSV_allavailable.json, definite, attribution: developer] cancel
default	18:38:41.805510+0800	hootowl	[C13 881A0D95-9A6E-4552-8385-67DE682F2D09 tcgbusfs.blob.core.windows.net:443 quic-connection, url: https://tcgbusfs.blob.core.windows.net/blobtcmsv/TCMSV_allavailable.json, definite, attribution: developer] cancelled
	[C13.1.1.1 83FCFAD5-92A2-439E-9EA8-7B29A695B6EE 192.168.50.191:55865<->20.150.22.100:443]
	Connected Path: satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good
	Privacy Stance: Not Eligible
	Duration: 47.768s, DNS @0.003s took 0.029s, TCP @0.040s took 0.097s,  took 0.193s
	bytes in/out: 471811/2716, packets in/out: 70/57, rtt: 0.080s, retransmitted bytes: 0, out-of-order bytes: 0
	ecn packets sent/acked/marked/lost: 6/5/0/0
default	18:38:41.806955+0800	hootowl	nw_protocol_tcp_log_summary [C13.1.1.1:3] 
	[07544665-67C2-42AB-A731-877F51735C25 192.168.50.191:55865<->20.150.22.100:443]
	Init: 1, Conn_Time: 74.136ms, SYNs: 1, WR_T: 0/0, RD_T: 0/0, TFO: 0/0/0, ECN: 0/1/1, Accurate ECN (client/server): Disabled/Disabled, TS: 1, TSO: 0
	rtt_cache: process, rtt_upd: 6, rtt: 80.562ms, rtt_var: 18.812ms rtt_nc: 80.562ms, rtt_var_nc: 18.812ms base rtt: 66ms
	ACKs-compressed: 6, ACKs delayed: 41 delayed ACKs sent: 0
default	18:38:41.807744+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C13] reporting state cancelled
default	18:38:41.807763+0800	hootowl	Connection 13: done
default	18:38:41.808006+0800	hootowl	tcp_output [C13.1.1.1:3] flags=[F.] seq=473803569, ack=1238804210, win=4257 state=FIN_WAIT_1 rcv_nxt=1238804210, snd_una=473803545
default	18:38:41.897867+0800	hootowl	tcp_input [C13.1.1.1:3] flags=[F.] seq=1238804210, ack=473803570, win=16380 state=FIN_WAIT_2 rcv_nxt=1238804210, snd_una=473803570
default	18:39:11.988354+0800	hootowl	tcp_close [C13.1.1.1:3] TCP Packets:
	 snd    0.000s seq  473803186:473803186  ack 1238672594 win 4213  len 0    [.]
	 rcv    0.000s seq 1238672594:1238675474 ack 473803186  win 16382 len 2880 [.] ECT0
	 rcv    0.000s seq 1238675474:1238678354 ack 473803186  win 16382 len 2880 [.] ECT0
	 snd    0.000s seq  473803186:473803186  ack 1238678354 win 4213  len 0    [.]
	 rcv    0.000s seq 1238678354:1238681234 ack 473803186  win 16382 len 2880 [.] ECT0
	 snd    0.000s seq  473803186:473803186  ack 1238681234 win 4213  len 0    [.]
	 rcv    0.006s seq 1238681234:1238688434 ack 473803186  win 16382 len 7200 [.] ECT0
	 snd    0.000s seq  473803186:473803186  ack 1238688434 win 4213  len 0    [.]
	 rcv    0.001s seq 1238688434:1238689874 ack 473803186  win 16382 len 1440 [.] ECT0
	 rcv    0.002s seq 1238689874:1238705714 ack 473803186  win 16382 len 15840 [.] ECT0
	 snd    0.000s seq  473803186:473803186  ack 1238705714 win 4213  len 0    [.]
	 rcv    0.134s seq 1238705714:1238707154 ack 473803186  win 16382 len 1440 [.] ECT0
	 snd    0.000s seq  473803186:473803186  ack 1238707154 win 4235  len 0    [.]
	 rcv    0.006s seq 1238707154:1238708594 ack 473803186  win 16382 len 1440 [.] ECT0
	 rcv    0.000s seq 1238708594:1238712914 ack 473803186  win 16382 len 4320 [.] ECT0
	 rcv    0.000s seq 1238712914:1238714354 ack 473803186  win 16382 len 1440 [.] ECT0
	 rcv    0.000s seq 1238714354:1238718674 ack 473803186  win 16382 len 4320 [.] ECT0
	 rcv    0.000s seq 1238718674:1238720114 ack 473803186  win 16382 len 1440 [.] ECT0
	 snd    0.000s seq  473803186:473803186  ack 1238720114 win 4257  len 0    [.]
	 rcv    0.002s seq 1238720114:1238721554 ack 473803186  win 16382 len 1440 [.] ECT0
	 rcv    0.001s seq 1238721554:1238737394 ack 473803186  win 16382 len 15840 [.] ECT0
	 rcv    0.000s seq 1238737394:1238753234 ack 473803186  win 16382 len 15840 [.] ECT0
	 snd    0.000s seq  473803186:473803186  ack 1238753234 win 4257  len 0    [.]
	 rcv    0.003s seq 1238753234:1238769074 ack 473803186  win 16382 len 15840 [.] ECT0
	 rcv    0.000s seq 1238769074:1238784914 ack 473803186  win 16382 len 15840 [.] ECT0
	 rcv    0.000s seq 1238784914:1238794994 ack 473803186  win 16382 len 10080 [.] ECT0
	 rcv    0.000s seq 1238794994:1238799314 ack 473803186  win 16382 len 4320 [.] ECT0
	 snd    0.000s seq  473803186:473803186  ack 1238799314 win 4257  len 0    [.]
	 rcv    0.005s seq 1238799314:1238803880 ack 473803186  win 16382 len 4566 [P.] ECT0
	 snd    0.000s seq  473803186:473803186  ack 1238803880 win 4257  len 0    [.]
	 rcv    0.695s seq 1238803880:1238803880 ack 473803186  win 16382 len 0    [.]
	 snd   15.392s seq  473803186:473803545  ack 1238803880 win 4257  len 359  [P.] ECT0
	 rcv    0.095s seq 1238803880:1238804210 ack 473803545  win 16381 len 330  [P.] ECT0
	 snd    0.000s seq  473803545:473803545  ack 1238804210 win 4252  len 0    [.]
	 rcv    0.625s seq 1238804210:1238804210 ack 473803545  win 16381 len 0    [.]
	 snd   29.888s seq  473803545:473803569  ack 1238804210 win 4257  len 24   [P.] ECT0
	 snd    0.003s seq  473803569:473803570  ack 1238804210 win 4257  len 0    [F.]
	 rcv    0.088s seq 1238804210:1238804210 ack 473803570  win 16380 len 0    [.]
	 rcv    0.002s seq 1238804210:1238804211 ack 473803570  win 16380 len 0    [F.]
	 snd    0.000s seq  473803570:473803570  ack 1238804211 win 4257  len 0    [.]
	Last packet 30088ms ago.
default	18:39:38.712373+0800	hootowl	quic_frame_write_CONNECTION_CLOSE [C4.1.1.1:2] [-e1e14ca760996567] sending APPLICATION_CLOSE, code 0x100, reason <null>
default	18:39:38.712601+0800	hootowl	[C6 FF803A97-0D75-4F8E-9DD4-D7F9FFEAA632 142.250.66.66:443 quic-connection, url: https://pubads.g.doubleclick.net/gampad, tls, definite, known tracker, attribution: developer] cancel
default	18:39:38.713443+0800	hootowl	[C6 FF803A97-0D75-4F8E-9DD4-D7F9FFEAA632 142.250.66.66:443 quic-connection, url: https://pubads.g.doubleclick.net/gampad, tls, definite, known tracker, attribution: developer] cancelled
	[C6 9A0AC64C-6CDA-4396-B3C4-588087802F52 192.168.50.191:56924<->142.250.66.66:443]
	Connected Path: satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good
	Duration: 240.205s, QUIC @0.000s took 0.000s, TLS 1.3 took 0.065s
	bytes in/out: 10798/5514, packets in/out: 16/17, rtt: 0.056s, retransmitted bytes: 0, out-of-order bytes: 1494
	ecn packets sent/acked/marked/lost: 5/5/0/0
default	18:39:38.715229+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C6] reporting state cancelled
default	18:39:38.715965+0800	hootowl	quic_conn_log_summary [C4.1.1.1:2] [-e1e14ca760996567] 
	Connection attempts: 1, RETRY received: no, PTOs: 0
	Early data: no, Keep-alives sent/acknowledged: 0/0, ECN state: handshake validation succeeded, L4S: disabled
	RTT: base 41 ms, network 125 ms, latest 150 ms, minimum 41 ms, smoothed 56 ms (variance 32 ms)
	Path MTU: 1280, minimum MSS: 1252
	Migration events: 0, paths validated: 0
	Inbound unidirectional/bidirectional streams: 3/0
	Outbound unidirectional/bidirectional streams: 3/1
	DATA_BLOCKED frames sent/received: 0/0
	STREAM_DATA_BLOCKED frames sent/received: 0/0
default	18:39:38.717986+0800	hootowl	quic_conn_drain [C4.1.1.1:2] [-e1e14ca760996567] QUIC Packets:
	snd    0.000s LH<initial, 0>
			CRYPTO[0;999]
			PADDING[-1]
	snd    0.000s LH<initial, 1>
			CRYPTO[999;1487]
			PADDING[-1]
	rcv    0.042s LH<initial, 1>
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
	rcv    0.000s LH<handshake, 6>
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
	rcv    0.016s LH<handshake, 8>
			CRYPTO[2323;3484]
	rcv    0.000s LH<handshake, 9>
			CRYPTO[3484;4343]
	snd    0.000s LH<handshake, 1>
			ACK[9]
				(6, 9)
	snd    0.007s LH<handshake, 2>
			CRYPTO[0;52]
	rcv    0.003s SH<10>
			S3[0;47]
	snd    0.000s SH<0>
			ACK[10]
				(10, 10)
	snd    0.001s SH<1>
			S2[0;21]
	snd    0.001s SH<2>
			S0[0;159] FIN
	snd    0.000s SH<3>
			S6[0;5]
	rcv    0.006s SH<11>
			CRYPTO[0;624]
	rcv    0.001s SH<12>
			PADDING[0]
			PADDING[0]
			NEW_CONNECTION_ID[seq=1, retire=0]
	snd    0.000s SH<4>
			ACK[12]
				(10, 12)
	snd    0.000s SH<5>
			PADDING[0]
			PADDING[-1]
	rcv    0.058s SH<13>
			ACK[3]
				(0, 3)
	rcv    0.000s SH<14>
			ACK[5]
				(0, 5)
			S11[0;231]
			S0[0;14] FIN
	snd    0.003s SH<6>
			ACK[14]
				(10, 14)
	snd    0.000s SH<7>
			S10[0;2]
	rcv    0.151s SH<16>
			S11[0;231]
			S0[0;14] FIN
	rcv    0.000s SH<17>
			ACK[7]
				(6, 7)
	snd    0.000s SH<8>
			ACK[17]
				(16, 17)
				(10, 14)
	rcv    0.002s SH<19>
			PADDING[1]
			PADDING[0]
	snd    0.000s SH<9>
			ACK[19]
				(19, 19)
				(16, 17)
				(10, 14)
	snd  239.872s SH<10>
			APPLICATION_CLOSE[code=256, type=0]
default	18:39:38.718157+0800	hootowl	Connection 4: cleaning up
default	18:39:38.718195+0800	hootowl	[C4 D0E4EBCE-CBEA-4A34-97B6-DA2030E70F19 pubads.g.doubleclick.net:443 quic-connection, url: https://pubads.g.doubleclick.net/gampad, definite, attribution: developer] cancel
default	18:39:38.718281+0800	hootowl	[C4 D0E4EBCE-CBEA-4A34-97B6-DA2030E70F19 pubads.g.doubleclick.net:443 quic-connection, url: https://pubads.g.doubleclick.net/gampad, definite, attribution: developer] cancelled
	[C4.1.1.1 9A0AC64C-6CDA-4396-B3C4-588087802F52 192.168.50.191:56924<->142.250.66.66:443]
	Connected Path: satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good
	Privacy Stance: Not Eligible
	Duration: 240.242s, DNS @0.008s took 0.005s, QUIC @0.031s took 0.068s
	bytes in/out: 10798/5514, packets in/out: 16/17, rtt: 0.056s, retransmitted bytes: 0, out-of-order bytes: 1494
	ecn packets sent/acked/marked/lost: 5/5/0/0
default	18:39:38.718985+0800	hootowl	quic_path_destroy [C4.1.1.1:2] [-e1e14ca760996567] destroying path 0x11c0496c0
default	18:39:38.719175+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C4] reporting state cancelled
default	18:39:38.719304+0800	hootowl	quic_frame_write_CONNECTION_CLOSE [C3.1.1.1:2] [-f1a787e9603c94c7] sending APPLICATION_CLOSE, code 0x100, reason <null>
default	18:39:38.719322+0800	hootowl	[C5 4EE5FDE6-4773-40D2-8FA5-138F79A53E12 142.250.192.130:443 quic-connection, url: https://googleads.g.doubleclick.net/mads, tls, definite, known tracker, attribution: developer] cancel
default	18:39:38.719402+0800	hootowl	[C5 4EE5FDE6-4773-40D2-8FA5-138F79A53E12 142.250.192.130:443 quic-connection, url: https://googleads.g.doubleclick.net/mads, tls, definite, known tracker, attribution: developer] cancelled
	[C5 97F15861-5FD0-4EA1-8C68-FC353CDC2159 192.168.50.191:58588<->142.250.192.130:443]
	Connected Path: satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good
	Duration: 240.222s, QUIC @0.000s took 0.000s, TLS 1.3 took 0.065s
	bytes in/out: 62607/27852, packets in/out: 75/44, rtt: 0.067s, retransmitted bytes: 0, out-of-order bytes: 2524
	ecn packets sent/acked/marked/lost: 35/29/0/0
default	18:39:38.720297+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C5] reporting state cancelled
default	18:39:38.720530+0800	hootowl	quic_conn_log_summary [C3.1.1.1:2] [-f1a787e9603c94c7] 
	Connection attempts: 1, RETRY received: no, PTOs: 1
	Early data: no, Keep-alives sent/acknowledged: 0/0, ECN state: capable, L4S: disabled
	RTT: base 11 ms, network 30 ms, latest 30 ms, minimum 11 ms, smoothed 67 ms (variance 22 ms)
	Path MTU: 1350, minimum MSS: 1252
	Migration events: 0, paths validated: 0
	Inbound unidirectional/bidirectional streams: 3/0
	Outbound unidirectional/bidirectional streams: 3/3
	DATA_BLOCKED frames sent/received: 0/0
	STREAM_DATA_BLOCKED frames sent/received: 0/0
default	18:39:38.725848+0800	hootowl	quic_conn_drain [C3.1.1.1:2] [-f1a787e9603c94c7] QUIC Packets:
	snd    0.000s LH<initial, 0>
			CRYPTO[0;999]
			PADDING[-1]
	snd    0.000s LH<initial, 1>
			CRYPTO[999;1490]
			PADDING[-1]
	rcv    0.033s LH<initial, 1>
			ACK[0]
				(0, 0)
	rcv    0.014s LH<initial, 2>
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
	rcv    0.001s LH<handshake, 6>
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
	rcv    0.009s LH<handshake, 8>
			CRYPTO[2323;3484]
	rcv    0.001s LH<handshake, 9>
			CRYPTO[3484;4333]
	snd    0.000s LH<handshake, 1>
			ACK[9]
				(6, 9)
	snd    0.003s LH<handshake, 2>
			CRYPTO[0;52]
	rcv    0.003s SH<10>
			S3[0;45]
	snd    0.000s SH<0>
			ACK[10]
				(10, 10)
	snd    0.001s SH<1>
			S2[0;25]
	snd    0.001s SH<2>
			S0[0;160] FIN
	snd    0.000s SH<3>
			S6[0;5]
	rcv    0.011s SH<11>
			CRYPTO[0;624]
	rcv    0.000s SH<12>
			PADDING[0]
			PADDING[0]
			NEW_CONNECTION_ID[seq=1, retire=0]
	rcv    0.000s SH<13>
			ACK[3]
				(0, 3)
	snd    0.000s SH<4>
			PADDING[0]
			PADDING[-1]
	snd    0.000s SH<5>
			ACK[13]
				(10, 13)
	snd    0.131s SH<6>
			PADDING[0]
			PADDING[-1]
	rcv    0.087s SH<14>
			ACK[5]
				(4, 5)
	rcv    0.001s SH<15>
			S11[0;87]
			S0[0;8] FIN
	rcv    0.000s SH<17>
			S11[0;87]
			S0[0;8] FIN
	rcv    0.000s SH<18>
			ACK[6]
				(4, 6)
	snd    0.000s SH<7>
			ACK[18]
				(17, 18)
				(10, 15)
	snd    0.001s SH<8>
			S10[0;2]
	snd    0.000s SH<9>
			S10[2;3]
	rcv    0.059s SH<19>
			ACK[9]
				(7, 9)
	snd    5.292s SH<10>
			S4[0;1218]
	snd    0.000s SH<11>
			S4[1218;2435]
	snd    0.000s SH<12>
			S4[2435;3652]
	snd    0.000s SH<13>
			S4[3652;4869]
	snd    0.000s SH<14>
			S4[4869;6086]
	snd    0.000s SH<15>
			PADDING[0]
			PADDING[-1]
	snd    0.000s SH<16>
			S4[6086;7303]
	snd    0.000s SH<17>
			S4[7303;8520]
	snd    0.000s SH<18>
			S4[8520;8854] FIN
	rcv    0.098s SH<20>
			ACK[11]
				(7, 11)
	rcv    0.000s SH<21>
			ACK[13]
				(7, 13)
	rcv    0.000s SH<22>
			ACK[15]
				(7, 15)
	rcv    0.000s SH<23>
			ACK[17]
				(7, 17)
	rcv    0.000s SH<24>
			ACK[18]
				(7, 18)
	rcv    0.273s SH<25>
			S11[87;510]
			S4[0;747]
	rcv    0.000s SH<26>
			S4[747;1925]
	rcv    0.000s SH<27>
			S4[1925;3103]
	rcv    0.000s SH<28>
			S4[3103;4281]
	rcv    0.000s SH<29>
			S4[4281;5459]
	rcv    0.000s SH<30>
			S4[5459;6637]
	rcv    0.000s SH<31>
			S4[6637;7815]
	rcv    0.000s SH<32>
			S4[7815;8993]
	rcv    0.000s SH<33>
			S4[8993;10171]
	rcv    0.000s SH<34>
			S4[10171;11349]
	rcv    0.000s SH<35>
			S4[11349;12527]
	rcv    0.000s SH<36>
			S4[12527;13705]
	rcv    0.000s SH<37>
			S4[13705;14883]
	rcv    0.000s SH<38>
			S4[14883;16061]
	rcv    0.000s SH<39>
			S4[16061;17239]
	rcv    0.000s SH<40>
			S4[17239;18415]
	rcv    0.000s SH<41>
			S4[18415;19591]
	rcv    0.000s SH<42>
			S4[19591;20767]
	rcv    0.000s SH<43>
			S4[20767;21943]
	rcv    0.000s SH<44>
			S4[21943;23119]
	rcv    0.000s SH<45>
			S4[23119;24295]
	rcv    0.000s SH<46>
			PADDING[13]
			S4[24295;24380] FIN
	snd    0.000s SH<19>
			ACK[46]
				(17, 46)
				(10, 15)
	snd    0.078s SH<20>
			S10[3;4]
	snd    0.002s SH<21>
			S10[4;5]
	rcv    0.075s SH<47>
			ACK[21]
				(19, 21)
	snd    0.334s SH<22>
			S6[5;212]
	snd    0.001s SH<23>
			S8[0;1238]
	snd    0.000s SH<24>
			S8[1238;2475]
	snd    0.000s SH<25>
			S8[2475;3712]
	snd    0.000s SH<26>
			S8[3712;4949]
	snd    0.000s SH<27>
			S8[4949;6186]
	snd    0.000s SH<28>
			PADDING[0]
			PADDING[-1]
	snd    0.000s SH<29>
			S8[6186;7423]
	snd    0.000s SH<30>
			S8[7423;8653] FIN
	rcv    0.084s SH<48>
			ACK[23]
				(19, 23)
	rcv    0.000s SH<49>
			ACK[25]
				(19, 25)
	rcv    0.000s SH<50>
			ACK[27]
				(19, 27)
	rcv    0.000s SH<51>
			ACK[29]
				(19, 29)
	rcv    0.005s SH<52>
			ACK[30]
				(19, 30)
			S7[0;2]
	rcv    0.102s SH<54>
			S7[0;2]
	snd    0.000s SH<31>
			ACK[54]
				(54, 54)
				(17, 52)
				(10, 15)
	rcv    0.207s SH<55>
			S11[510;561]
			S8[0;1119]
	snd    0.000s SH<32>
			ACK[55]
				(54, 55)
				(17, 52)
				(10, 15)
	rcv    0.000s SH<56>
			S8[1119;2296]
	rcv    0.000s SH<57>
			S8[2296;3473]
	rcv    0.000s SH<58>
			S8[3473;4650]
	rcv    0.000s SH<59>
			S8[4650;5827]
	rcv    0.000s SH<60>
			S8[5827;7004]
	rcv    0.000s SH<61>
			S8[7004;8181]
	rcv    0.000s SH<62>
			S8[8181;9358]
	rcv    0.000s SH<63>
			S8[9358;10535]
	rcv    0.000s SH<64>
			S8[10535;11712]
	rcv    0.000s SH<65>
			S8[11712;12889]
	rcv    0.000s SH<66>
			S8[12889;14066]
	rcv    0.000s SH<67>
			S8[14066;15243]
	rcv    0.000s SH<68>
			S8[15243;16420]
	rcv    0.000s SH<69>
			S8[16420;17595]
	rcv    0.000s SH<70>
			S8[17595;18770]
	rcv    0.000s SH<71>
			S8[18770;19945]
	rcv    0.000s SH<72>
			S8[19945;21120]
	rcv    0.000s SH<73>
			S8[21120;22295]
	rcv    0.000s SH<74>
			S8[22295;23470]
	rcv    0.000s SH<75>
			PADDING[233]
			S8[23470;24411] FIN
	rcv    0.001s SH<76>
			PADDING[20]
	snd    0.000s SH<33>
			ACK[76]
				(54, 76)
				(17, 52)
				(10, 15)
	snd    0.000s SH<34>
			S10[5;6]
	snd    0.000s SH<35>
			S10[6;7]
	rcv    0.026s SH<78>
			S11[510;561]
			S8[0;1119]
	snd    0.000s SH<36>
			ACK[78]
				(78, 78)
				(54, 76)
				(17, 52)
				(10, 15)
	rcv    0.005s SH<79>
			ACK[35]
				(31, 35)
	snd  233.216s SH<37>
			APPLICATION_CLOSE[code=256, type=0]
default	18:39:38.726149+0800	hootowl	Connection 3: cleaning up
default	18:39:38.726175+0800	hootowl	[C3 DF85E802-17D6-479B-8FB4-626BDB40B4CC googleads.g.doubleclick.net:443 quic-connection, url: https://googleads.g.doubleclick.net/mads, definite, attribution: developer] cancel
default	18:39:38.726274+0800	hootowl	[C3 DF85E802-17D6-479B-8FB4-626BDB40B4CC googleads.g.doubleclick.net:443 quic-connection, url: https://googleads.g.doubleclick.net/mads, definite, attribution: developer] cancelled
	[C3.1.1.1 97F15861-5FD0-4EA1-8C68-FC353CDC2159 192.168.50.191:58588<->142.250.192.130:443]
	Connected Path: satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good
	Privacy Stance: Not Eligible
	Duration: 240.253s, DNS @0.005s took 0.014s, QUIC @0.024s took 0.071s
	bytes in/out: 62607/27852, packets in/out: 75/44, rtt: 0.067s, retransmitted bytes: 0, out-of-order bytes: 2524
	ecn packets sent/acked/marked/lost: 35/29/0/0
default	18:39:38.726628+0800	hootowl	quic_path_destroy [C3.1.1.1:2] [-f1a787e9603c94c7] destroying path 0x11c0481c0
default	18:39:38.726712+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C3] reporting state cancelled
default	18:39:39.653136+0800	hootowl	Connection 7: cleaning up
default	18:39:39.653187+0800	hootowl	[C7 AD1BC174-14E2-4D23-A783-04805D366070 gist.githubusercontent.com:443 quic-connection, url: https://gist.githubusercontent.com/sharkda/1abaa9806dae0f34205725b51f21ad87/raw, definite, attribution: developer] cancel
default	18:39:39.653697+0800	hootowl	[C7 AD1BC174-14E2-4D23-A783-04805D366070 gist.githubusercontent.com:443 quic-connection, url: https://gist.githubusercontent.com/sharkda/1abaa9806dae0f34205725b51f21ad87/raw, definite, attribution: developer] cancelled
	[C7.1.1.1 DFB2AD02-1B14-47ED-9116-121ECE3961B2 192.168.50.191:55835<->185.199.109.133:443]
	Connected Path: satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good
	Privacy Stance: Not Eligible
	Duration: 241.113s, DNS @0.007s took 0.020s, TCP @0.028s took 0.228s,  took 0.587s
	bytes in/out: 6398/3492, packets in/out: 10/16, rtt: 0.219s, retransmitted bytes: 1535, out-of-order bytes: 0
	ecn packets sent/acked/marked/lost: 0/0/0/0
default	18:39:39.656616+0800	hootowl	nw_protocol_tcp_log_summary [C7.1.1.1:3] 
	[75615939-D45E-4962-B4B3-11225D80B621 192.168.50.191:55835<->185.199.109.133:443]
	Init: 1, Conn_Time: 226.914ms, SYNs: 1, WR_T: 0/0, RD_T: 0/0, TFO: 0/0/0, ECN: 0/0/1, Accurate ECN (client/server): Disabled/Disabled, TS: 1, TSO: 0
	rtt_cache: none, rtt_upd: 5, rtt: 219.531ms, rtt_var: 59.687ms rtt_nc: 219.531ms, rtt_var_nc: 59.687ms base rtt: 167ms
	ACKs-compressed: 0, ACKs delayed: 0 delayed ACKs sent: 0
default	18:39:39.657908+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C7] reporting state cancelled
default	18:39:39.658030+0800	hootowl	tcp_output [C7.1.1.1:3] flags=[F.] seq=1258121700, ack=3969321253, win=2048 state=FIN_WAIT_1 rcv_nxt=3969321253, snd_una=1258121637
default	18:39:39.789052+0800	hootowl	tcp_close [C7.1.1.1:3] TCP Packets:
	 snd    0.000s seq 1258119718:1258119719 ack 0          win 65535 len 0    [SEC]
	 rcv    0.227s seq 3969314854:3969314855 ack 1258119719 win 65535 len 0    [S.]
	 snd    0.000s seq 1258119719:1258119719 ack 3969314855 win 2059  len 0    [.]
	 snd    0.001s seq 1258119719:1258121167 ack 3969314855 win 2059  len 1448 [.]
	 snd    0.000s seq 1258121167:1258121254 ack 3969314855 win 2059  len 87   [P.]
	 snd    0.001s seq 1258119719:1258121159 ack 3969314855 win 2059  len 1440 [.]
	 snd    0.000s seq 1258121159:1258121254 ack 3969314855 win 2059  len 95   [P.]
	 rcv    0.159s seq 3969314855:3969314855 ack 1258119719 win 285   len 0    [.]
	 rcv    0.075s seq 3969314855:3969314855 ack 1258121254 win 283   len 0    [.]
	 rcv    0.000s seq 3969314855:3969317735 ack 1258121254 win 283   len 2880 [P.]
	 snd    0.000s seq 1258121254:1258121254 ack 3969317735 win 2014  len 0    [.]
	 rcv    0.004s seq 3969317735:3969320850 ack 1258121254 win 283   len 3115 [P.]
	 snd    0.000s seq 1258121254:1258121254 ack 3969320850 win 2000  len 0    [.]
	 snd    0.000s seq 1258121254:1258121254 ack 3969320850 win 2048  len 0    [.]
	 snd    0.251s seq 1258121254:1258121318 ack 3969320850 win 2048  len 64   [P.]
	 snd    0.186s seq 1258121318:1258121606 ack 3969320850 win 2048  len 288  [P.]
	 rcv    0.003s seq 3969320850:3969320850 ack 1258121318 win 283   len 0    [.]
	 rcv    0.164s seq 3969320850:3969320915 ack 1258121606 win 283   len 65   [P.]
	 snd    0.000s seq 1258121606:1258121606 ack 3969320915 win 2047  len 0    [.]
	 snd    0.005s seq 1258121606:1258121637 ack 3969320915 win 2048  len 31   [P.]
	 rcv    0.244s seq 3969320915:3969320915 ack 1258121637 win 283   len 0    [.]
	 rcv    0.000s seq 3969320915:3969321253 ack 1258121637 win 283   len 338  [P.]
	 snd    0.000s seq 1258121637:1258121637 ack 3969321253 win 2043  len 0    [.]
	 rcv    1.167s seq 3969321253:3969321253 ack 1258121637 win 283   len 0    [.]
	 snd  238.592s seq 1258121637:1258121676 ack 3969321253 win 2048  len 39   [P.]
	 snd    0.001s seq 1258121676:1258121700 ack 3969321253 win 2048  len 24   [P.]
	 snd    0.002s seq 1258121700:1258121701 ack 3969321253 win 2048  len 0    [F.]
	 rcv    0.132s seq 3969321253:3969321253 ack 1258121676 win 283   len 0    [.]
	 rcv    0.000s seq 3969321253:3969321253 ack 1258121700 win 283   len 0    [.]
	 rcv    0.000s seq 3969321253:3969321277 ack 1258121701 win 283   len 24   [P.]
	Last packet 0ms ago.
default	18:39:39.789242+0800	hootowl	tcp_input [C7.1.1.1:3] flags=[F.] seq=3969321277, ack=1258121701, win=283 state=CLOSED rcv_nxt=3969321253, snd_una=1258121700
default	18:39:45.010636+0800	hootowl	quic_frame_write_CONNECTION_CLOSE [C8.1.1.1:2] [-e8d0fb177d19a704] sending APPLICATION_CLOSE, code 0x100, reason <null>
default	18:39:45.010741+0800	hootowl	[C9 B580544B-64C7-4E6D-9E83-A8D0B1481C7A 216.239.36.54:443 quic-connection, url: https://us-central1-tataro2.cloudfunctions.net/verifyReceipt, tls, definite, attribution: developer] cancel
default	18:39:45.010943+0800	hootowl	[C9 B580544B-64C7-4E6D-9E83-A8D0B1481C7A 216.239.36.54:443 quic-connection, url: https://us-central1-tataro2.cloudfunctions.net/verifyReceipt, tls, definite, attribution: developer] cancelled
	[C9 88DDA971-F480-4D59-825E-762F1EA495A8 192.168.50.191:60152<->216.239.36.54:443]
	Connected Path: satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good
	Duration: 240.590s, QUIC @0.000s took 0.000s, TLS 1.3 took 0.445s
	bytes in/out: 17142/9169, packets in/out: 24/21, rtt: 0.062s, retransmitted bytes: 0, out-of-order bytes: 1838
	ecn packets sent/acked/marked/lost: 12/10/0/0
default	18:39:45.011287+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C9] reporting state cancelled
default	18:39:45.011744+0800	hootowl	quic_conn_log_summary [C8.1.1.1:2] [-e8d0fb177d19a704] 
	Connection attempts: 1, RETRY received: no, PTOs: 1
	Early data: no, Keep-alives sent/acknowledged: 0/0, ECN state: capable, L4S: disabled
	RTT: base 9 ms, network 91 ms, latest 91 ms, minimum 9 ms, smoothed 62 ms (variance 48 ms)
	Path MTU: 1280, minimum MSS: 1252
	Migration events: 0, paths validated: 0
	Inbound unidirectional/bidirectional streams: 3/0
	Outbound unidirectional/bidirectional streams: 3/1
	DATA_BLOCKED frames sent/received: 0/0
	STREAM_DATA_BLOCKED frames sent/received: 0/0
default	18:39:45.012999+0800	hootowl	quic_conn_drain [C8.1.1.1:2] [-e8d0fb177d19a704] QUIC Packets:
	snd    0.000s LH<initial, 0>
			CRYPTO[0;999]
			PADDING[-1]
	snd    0.000s LH<initial, 1>
			CRYPTO[999;1501]
			PADDING[-1]
	rcv    0.096s LH<initial, 1>
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
	rcv    0.001s LH<handshake, 6>
			CRYPTO[0;1162]
	rcv    0.001s LH<handshake, 7>
			CRYPTO[1162;2323]
	snd    0.000s LH<initial, 2>
			ACK[5]
				(1, 5)
			PADDING[-1]
	snd    0.000s LH<handshake, 0>
			ACK[7]
				(6, 7)
	rcv    0.089s LH<handshake, 8>
			CRYPTO[2323;3484]
	rcv    0.065s LH<handshake, 9>
			CRYPTO[3484;4645]
	rcv    0.000s LH<handshake, 10>
			CRYPTO[4645;5806]
	rcv    0.000s LH<handshake, 11>
			CRYPTO[5806;6967]
	rcv    0.000s LH<handshake, 12>
			CRYPTO[6967;8128]
	rcv    0.000s LH<handshake, 13>
			CRYPTO[8128;9289]
	rcv    0.000s LH<handshake, 14>
			CRYPTO[9289;10410]
	snd    0.002s LH<handshake, 1>
			ACK[14]
				(6, 14)
	snd    0.099s LH<handshake, 2>
			PADDING[0]
			PADDING[2]
	rcv    0.066s LH<handshake, 17>
			ACK[2]
				(0, 2)
	snd    0.025s LH<handshake, 3>
			CRYPTO[0;52]
	rcv    0.004s SH<15>
			S3[0;19]
	rcv    0.000s SH<16>
			S3[19;46]
	snd    0.000s SH<0>
			ACK[16]
				(15, 16)
	snd    0.001s SH<1>
			S2[0;25]
	snd    0.000s SH<2>
			S0[0;155]
	snd    0.001s SH<3>
			S6[0;5]
	snd    0.000s SH<4>
			S0[155;1320]
	snd    0.000s SH<5>
			S0[1320;2485]
	snd    0.000s SH<6>
			S0[2485;3650]
	snd    0.000s SH<7>
			S0[3650;3679] FIN
	rcv    0.005s SH<18>
			CRYPTO[0;624]
	rcv    0.000s SH<19>
			PADDING[0]
			PADDING[0]
			NEW_CONNECTION_ID[seq=1, retire=0]
	snd    0.001s SH<8>
			ACK[19]
				(18, 19)
				(15, 16)
	snd    0.000s SH<9>
			PADDING[0]
			PADDING[-1]
	rcv    0.004s SH<20>
			ACK[2]
				(0, 2)
	rcv    0.000s SH<21>
			ACK[4]
				(0, 4)
	rcv    0.006s SH<22>
			ACK[6]
				(0, 6)
	rcv    0.000s SH<23>
			ACK[9]
				(0, 9)
	rcv    0.313s SH<24>
			S11[0;149]
			S0[0;338] FIN
	snd    0.001s SH<10>
			ACK[24]
				(18, 24)
				(15, 16)
	snd    0.001s SH<11>
			S10[0;2]
	snd    0.000s SH<12>
			S10[2;3]
	rcv    0.091s SH<25>
			ACK[12]
				(10, 12)
	snd  239.616s SH<13>
			APPLICATION_CLOSE[code=256, type=0]
default	18:39:45.013145+0800	hootowl	Connection 8: cleaning up
default	18:39:45.013178+0800	hootowl	[C8 56107502-02D4-4B28-8247-C3F98E686154 us-central1-tataro2.cloudfunctions.net:443 quic-connection, url: https://us-central1-tataro2.cloudfunctions.net/verifyReceipt, definite, attribution: developer] cancel
default	18:39:45.013230+0800	hootowl	[C8 56107502-02D4-4B28-8247-C3F98E686154 us-central1-tataro2.cloudfunctions.net:443 quic-connection, url: https://us-central1-tataro2.cloudfunctions.net/verifyReceipt, definite, attribution: developer] cancelled
	[C8.1.1.1 88DDA971-F480-4D59-825E-762F1EA495A8 192.168.50.191:60152<->216.239.36.54:443]
	Connected Path: satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good
	Privacy Stance: Not Eligible
	Duration: 240.860s, DNS @0.002s took 0.096s, QUIC @0.206s took 0.510s
	bytes in/out: 17142/9169, packets in/out: 24/21, rtt: 0.062s, retransmitted bytes: 0, out-of-order bytes: 1838
	ecn packets sent/acked/marked/lost: 12/10/0/0
default	18:39:45.014185+0800	hootowl	quic_path_destroy [C8.1.1.1:2] [-e8d0fb177d19a704] destroying path 0x139610540
default	18:39:45.014363+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C8] reporting state cancelled
default	18:40:11.289186+0800	hootowl	Task <E7F4025A-0D22-456A-AA16-87D005FD2803>.<10> resuming, timeouts(60.0, 604800.0) qos(0x15) voucher((null)) activity(00000000-0000-0000-0000-000000000000)
default	18:40:11.293438+0800	hootowl	Connection 0: creating secure tcp or quic connection
default	18:40:11.293772+0800	hootowl	Connection 15: enabling TLS
default	18:40:11.293793+0800	hootowl	Connection 15: starting, TC(0x0)
default	18:40:11.293842+0800	hootowl	[C15 5FFB743E-4C84-44E1-B23F-BF6452E84CCC tcgbusfs.blob.core.windows.net:443 quic-connection, url: https://tcgbusfs.blob.core.windows.net/blobtcmsv/TCMSV_allavailable.json, definite, attribution: developer, context: com.apple.CFNetwork.NSURLSession.{C8A30AB7-8A8F-46A2-A794-FF53331E2689}{(null)}{Y}{2}{0x0} (private), proc: 1B526020-2DE0-3C65-9122-F1177549D69A, delegated upid: 0] start
default	18:40:11.293898+0800	hootowl	[C15 tcgbusfs.blob.core.windows.net:443 initial parent-flow ((null))] event: path:start @0.000s
default	18:40:11.295190+0800	hootowl	[C15 tcgbusfs.blob.core.windows.net:443 waiting parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.001s, uuid: 8E2D7817-3EAD-4BFD-9452-1A67EC6ABFE1
default	18:40:11.295340+0800	hootowl	[C15 tcgbusfs.blob.core.windows.net:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_connect @0.001s
default	18:40:11.295357+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C15] reporting state preparing
default	18:40:11.295438+0800	hootowl	[C15 tcgbusfs.blob.core.windows.net:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_child @0.001s
default	18:40:11.295523+0800	hootowl	[C15.1 tcgbusfs.blob.core.windows.net:443 initial path ((null))] event: path:start @0.001s
default	18:40:11.296432+0800	hootowl	[C15.1 tcgbusfs.blob.core.windows.net:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.001s, uuid: 8E2D7817-3EAD-4BFD-9452-1A67EC6ABFE1
default	18:40:11.296488+0800	hootowl	[C15.1 tcgbusfs.blob.core.windows.net:443 in_progress transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: transform:start @0.001s
default	18:40:11.296632+0800	hootowl	[C15.1.1 tcgbusfs.blob.core.windows.net:443 initial path ((null))] event: path:start @0.001s
default	18:40:11.297815+0800	hootowl	[C15.1.1 tcgbusfs.blob.core.windows.net:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.003s, uuid: 299AC001-BF0F-4C48-9832-8F32722EDBDF
default	18:40:11.297894+0800	hootowl	[C15.1.1 tcgbusfs.blob.core.windows.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:start_dns @0.003s
default	18:40:11.297916+0800	hootowl	Task <E7F4025A-0D22-456A-AA16-87D005FD2803>.<10> setting up Connection 15
default	18:40:11.350620+0800	hootowl	nw_endpoint_resolver_update [C15.1.1 tcgbusfs.blob.core.windows.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Adding endpoint handler for 20.150.22.100:443
default	18:40:11.351465+0800	hootowl	[C15.1.1 tcgbusfs.blob.core.windows.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:receive_dns @0.056s
default	18:40:11.351655+0800	hootowl	[C15.1.1.1 20.150.22.100:443 initial path ((null))] event: path:start @0.057s
default	18:40:11.352241+0800	hootowl	[C15.1.1.1 20.150.22.100:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.058s, uuid: 8EE3833C-4527-409F-A0BC-0E1CAA0FFBE3
default	18:40:11.352385+0800	hootowl	[C15.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_nexus @0.058s
default	18:40:11.354088+0800	hootowl	[C15.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:receive_nexus @0.059s
default	18:40:11.354656+0800	hootowl	[C15.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_connect @0.060s
default	18:40:11.355360+0800	hootowl	tcp_output [C15.1.1.1:3] flags=[SEC] seq=4036403936, ack=0, win=65535 state=SYN_SENT rcv_nxt=0, snd_una=4036403936
default	18:40:11.428236+0800	hootowl	[C15.1.1 tcgbusfs.blob.core.windows.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:receive_dns @0.131s
default	18:40:11.463673+0800	hootowl	tcp_input [C15.1.1.1:3] flags=[S.E] seq=4157855184, ack=4036403937, win=65535 state=SYN_SENT rcv_nxt=0, snd_una=4036403936
default	18:40:11.463792+0800	hootowl	nw_flow_connected [C15.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Transport protocol connected (tcp)
default	18:40:11.464219+0800	hootowl	[C15.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_transport @0.169s
default	18:40:11.465341+0800	hootowl	boringssl_session_apply_protocol_options_for_transport_block_invoke_2(2367) [C15.1.1.1:2][0x11c25cce0] TLS configured [server(0) min_version(0x0303) max_version(0x0304) name(tcgbusfs.blob.core.windows.net) tickets(false) false_start(false) enforce_ev(false) enforce_ats(false) ats_non_pfs_ciphersuite_allowed(false) cc_mode_enforced(false) ech(false) pqtls(true), pake(false) skip_ats_trust(false)]
default	18:40:11.465559+0800	hootowl	boringssl_context_info_handler(2806) [C15.1.1.1:2][0x11c25cce0] Client handshake started
default	18:40:11.465763+0800	hootowl	boringssl_context_info_handler(2823) [C15.1.1.1:2][0x11c25cce0] Client handshake state: TLS client enter_early_data
default	18:40:11.466129+0800	hootowl	boringssl_context_info_handler(2823) [C15.1.1.1:2][0x11c25cce0] Client handshake state: TLS client read_server_hello
default	18:40:11.563899+0800	hootowl	boringssl_context_info_handler(2823) [C15.1.1.1:2][0x11c25cce0] Client handshake state: TLS 1.3 client read_hello_retry_request
default	18:40:11.567315+0800	hootowl	boringssl_context_info_handler(2823) [C15.1.1.1:2][0x11c25cce0] Client handshake state: TLS 1.3 client send_second_client_hello
default	18:40:11.567634+0800	hootowl	boringssl_context_info_handler(2823) [C15.1.1.1:2][0x11c25cce0] Client handshake state: TLS 1.3 client read_server_hello
default	18:40:11.647913+0800	hootowl	boringssl_context_info_handler(2823) [C15.1.1.1:2][0x11c25cce0] Client handshake state: TLS 1.3 client read_encrypted_extensions
default	18:40:11.649243+0800	hootowl	boringssl_context_info_handler(2823) [C15.1.1.1:2][0x11c25cce0] Client handshake state: TLS 1.3 client read_certificate_request
default	18:40:11.649319+0800	hootowl	boringssl_context_info_handler(2823) [C15.1.1.1:2][0x11c25cce0] Client handshake state: TLS 1.3 client read_server_certificate
default	18:40:11.649388+0800	hootowl	boringssl_context_info_handler(2823) [C15.1.1.1:2][0x11c25cce0] Client handshake state: TLS 1.3 client read_server_certificate_verify
default	18:40:11.650589+0800	hootowl	boringssl_context_evaluate_trust_async(2249) [C15.1.1.1:2][0x11c25cce0] Performing external trust evaluation
default	18:40:11.650945+0800	hootowl	boringssl_context_evaluate_trust_async_external(2234) [C15.1.1.1:2][0x11c25cce0] Asyncing for external verify block
default	18:40:11.651465+0800	hootowl	Connection 15: asked to evaluate TLS Trust
default	18:40:11.651729+0800	hootowl	Task <E7F4025A-0D22-456A-AA16-87D005FD2803>.<10> auth completion disp=1 cred=0x0
default	18:40:11.652302+0800	hootowl	(Trust 0x11be3a940) No pending evals, starting
default	18:40:11.652779+0800	hootowl	[0x112193700] activating connection: mach=true listener=false peer=false name=com.apple.trustd
default	18:40:11.653140+0800	hootowl	(Trust 0x11be3a940) Completed async eval kickoff
default	18:40:11.663794+0800	hootowl	(Trust 0x11be3a940) trustd returned 4
default	18:40:11.663882+0800	hootowl	System Trust Evaluation yielded status(0)
default	18:40:11.664045+0800	hootowl	(Trust 0x11be3b0c0) No pending evals, starting
default	18:40:11.664345+0800	hootowl	[0x112190b40] activating connection: mach=true listener=false peer=false name=com.apple.trustd
default	18:40:11.664562+0800	hootowl	(Trust 0x11be3b0c0) Completed async eval kickoff
default	18:40:11.664868+0800	hootowl	[0x112193700] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	18:40:11.671097+0800	hootowl	(Trust 0x11be3b0c0) trustd returned 4
default	18:40:11.671183+0800	hootowl	Connection 15: TLS Trust result 0
default	18:40:11.671226+0800	hootowl	boringssl_context_evaluate_trust_async_external_block_invoke_3(2148) [C15.1.1.1:2][0x11c25cce0] Returning from external verify block with result: true
default	18:40:11.671341+0800	hootowl	boringssl_context_certificate_verify_callback(2430) [C15.1.1.1:2][0x11c25cce0] Certificate verification result: OK
default	18:40:11.671381+0800	hootowl	boringssl_context_info_handler(2823) [C15.1.1.1:2][0x11c25cce0] Client handshake state: TLS 1.3 client read_server_finished
default	18:40:11.671447+0800	hootowl	boringssl_context_info_handler(2823) [C15.1.1.1:2][0x11c25cce0] Client handshake state: TLS 1.3 client send_end_of_early_data
default	18:40:11.671457+0800	hootowl	boringssl_context_info_handler(2823) [C15.1.1.1:2][0x11c25cce0] Client handshake state: TLS 1.3 client send_client_encrypted_extensions
default	18:40:11.671464+0800	hootowl	boringssl_context_info_handler(2823) [C15.1.1.1:2][0x11c25cce0] Client handshake state: TLS 1.3 client send_client_certificate
default	18:40:11.671499+0800	hootowl	boringssl_context_info_handler(2823) [C15.1.1.1:2][0x11c25cce0] Client handshake state: TLS 1.3 client complete_second_flight
default	18:40:11.671539+0800	hootowl	boringssl_context_info_handler(2823) [C15.1.1.1:2][0x11c25cce0] Client handshake state: TLS 1.3 client done
default	18:40:11.671675+0800	hootowl	boringssl_context_info_handler(2823) [C15.1.1.1:2][0x11c25cce0] Client handshake state: TLS client finish_client_handshake
default	18:40:11.671689+0800	hootowl	boringssl_context_info_handler(2823) [C15.1.1.1:2][0x11c25cce0] Client handshake state: TLS client done
default	18:40:11.671715+0800	hootowl	boringssl_context_info_handler(2812) [C15.1.1.1:2][0x11c25cce0] Client handshake done
default	18:40:11.672128+0800	hootowl	nw_protocol_boringssl_signal_connected(895) [C15.1.1.1:2][0x11c25cce0] TLS connected [server(0) version(0x0304) ciphersuite(TLS_AES_256_GCM_SHA384) group(0x0018) signature_alg(0x0804) alpn(nil) resumed(0) offered_ticket(0) in_early_data(0) early_data_accepted(0) false_started(0) ocsp_received(1) sct_received(0) connect_time(207ms) flight_time(174ms) rtt(98ms) write_stalls(0) read_stalls(8) pake(0x0000)]
default	18:40:11.672250+0800	hootowl	nw_flow_connected [C15.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (CFNetworkConnection-398509258)
default	18:40:11.672451+0800	hootowl	[C15.1.1.1 20.150.22.100:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.378s
default	18:40:11.672581+0800	hootowl	[C15.1.1 tcgbusfs.blob.core.windows.net:443 ready resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.378s
default	18:40:11.672643+0800	hootowl	[C15.1 tcgbusfs.blob.core.windows.net:443 ready transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.378s
default	18:40:11.672724+0800	hootowl	[C15.1.1.1 20.150.22.100:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.378s
default	18:40:11.672805+0800	hootowl	[C15.1.1 tcgbusfs.blob.core.windows.net:443 ready resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.378s
default	18:40:11.672909+0800	hootowl	[C15.1 tcgbusfs.blob.core.windows.net:443 ready transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.378s
default	18:40:11.672929+0800	hootowl	nw_flow_connected [C15 20.150.22.100:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (endpoint_flow)
default	18:40:11.672991+0800	hootowl	[C15 20.150.22.100:443 ready parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_connect @0.379s
default	18:40:11.673233+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C15] reporting state ready
default	18:40:11.673316+0800	hootowl	[C15 20.150.22.100:443 ready parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.379s
default	18:40:11.673326+0800	hootowl	nw_connection_send_viability_changed_on_nw_queue [C15] viability_changed_handler(true)
default	18:40:11.673343+0800	hootowl	[0x112190b40] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	18:40:11.673377+0800	hootowl	Connection 15: connected successfully
default	18:40:11.673415+0800	hootowl	Connection 15: TLS handshake complete
default	18:40:11.673450+0800	hootowl	Connection 15: ready C(N) E(N)
default	18:40:11.673587+0800	hootowl	Task <E7F4025A-0D22-456A-AA16-87D005FD2803>.<10> now using Connection 15
default	18:40:11.673625+0800	hootowl	Connection 15: received viability advisory(Y)
default	18:40:11.673742+0800	hootowl	Task <E7F4025A-0D22-456A-AA16-87D005FD2803>.<10> sent request, body N 0
default	18:40:11.747950+0800	hootowl	Task <E7F4025A-0D22-456A-AA16-87D005FD2803>.<10> received response, status 304 content K
default	18:40:11.748702+0800	hootowl	Task <E7F4025A-0D22-456A-AA16-87D005FD2803>.<10> done using Connection 15
default	18:40:11.749000+0800	hootowl	[C15] event: client:connection_idle @0.454s
default	18:40:11.749174+0800	hootowl	nw_protocol_tcp_notify [C15.1.1.1:3] nw_protocol_notification_type_connection_idle is true
default	18:40:11.749315+0800	hootowl	Task <E7F4025A-0D22-456A-AA16-87D005FD2803>.<10> summary for task success {transaction_duration_ms=458, response_status=304, connection=15, protocol="http/1.1", domain_lookup_duration_ms=53, connect_duration_ms=319, secure_connection_duration_ms=207, private_relay=false, request_start_ms=384, request_duration_ms=0, response_start_ms=457, response_duration_ms=0, request_bytes=337, request_throughput_kbps=44872, response_bytes=308, response_throughput_kbps=3716, cache_hit=true}
default	18:40:11.749368+0800	hootowl	nw_protocol_tcp_set_connection_idle [C15.1.1.1:3] os_nexus_flow_set_connection_idle returned 0
default	18:40:11.749902+0800	hootowl	[C15] event: client:connection_idle @0.454s
default	18:40:11.750149+0800	hootowl	Task <E7F4025A-0D22-456A-AA16-87D005FD2803>.<10> finished successfully
default	18:40:11.750216+0800	hootowl	Mu1Base+Ext 152
taipei 📦 minutely Received 459955 bytes
default	18:40:11.750243+0800	hootowl	nw_protocol_tcp_notify [C15.1.1.1:3] nw_protocol_notification_type_connection_idle is true
default	18:40:11.750365+0800	hootowl	nw_protocol_tcp_set_connection_idle [C15.1.1.1:3] os_nexus_flow_set_connection_idle returned 0
default	18:40:11.751193+0800	hootowl	Mu1Base+Ext 177
previousHash not changed
default	18:40:11.765837+0800	hootowl	Municipal+Cyclops 79
🎨 model refreshed — obs:0s car:18 thread:main
default	18:40:42.782547+0800	hootowl	Connection 15: cleaning up
default	18:40:42.782707+0800	hootowl	[C15 5FFB743E-4C84-44E1-B23F-BF6452E84CCC tcgbusfs.blob.core.windows.net:443 quic-connection, url: https://tcgbusfs.blob.core.windows.net/blobtcmsv/TCMSV_allavailable.json, definite, attribution: developer] cancel
default	18:40:42.783906+0800	hootowl	[C15 5FFB743E-4C84-44E1-B23F-BF6452E84CCC tcgbusfs.blob.core.windows.net:443 quic-connection, url: https://tcgbusfs.blob.core.windows.net/blobtcmsv/TCMSV_allavailable.json, definite, attribution: developer] cancelled
	[C15.1.1.1 8EE3833C-4527-409F-A0BC-0E1CAA0FFBE3 192.168.50.191:55880<->20.150.22.100:443]
	Connected Path: satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good
	Privacy Stance: Not Eligible
	Duration: 31.490s, DNS @0.003s took 0.053s, TCP @0.060s took 0.109s,  took 0.207s
	bytes in/out: 10765/2357, packets in/out: 8/14, rtt: 0.096s, retransmitted bytes: 0, out-of-order bytes: 0
	ecn packets sent/acked/marked/lost: 5/4/0/0
default	18:40:42.784790+0800	hootowl	nw_protocol_tcp_log_summary [C15.1.1.1:3] 
	[A1A99F59-FA76-42B9-8F3B-87C34AE9F91A 192.168.50.191:55880<->20.150.22.100:443]
	Init: 1, Conn_Time: 108.873ms, SYNs: 1, WR_T: 0/0, RD_T: 0/0, TFO: 0/0/0, ECN: 0/1/1, Accurate ECN (client/server): Disabled/Disabled, TS: 1, TSO: 0
	rtt_cache: process, rtt_upd: 5, rtt: 96.093ms, rtt_var: 35.875ms rtt_nc: 96.093ms, rtt_var_nc: 35.875ms base rtt: 66ms
	ACKs-compressed: 0, ACKs delayed: 0 delayed ACKs sent: 0
default	18:40:42.785732+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C15] reporting state cancelled
default	18:40:42.786107+0800	hootowl	Connection 15: done
default	18:40:42.786266+0800	hootowl	tcp_output [C15.1.1.1:3] flags=[F.] seq=4036406318, ack=4157865950, win=2048 state=FIN_WAIT_1 rcv_nxt=4157865950, snd_una=4036406294
default	18:40:42.913510+0800	hootowl	tcp_input [C15.1.1.1:3] flags=[F.] seq=4157865950, ack=4036406319, win=16382 state=FIN_WAIT_2 rcv_nxt=4157865950, snd_una=4036406319
default	18:41:09.401745+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c63ab posting AVAudioSessionAvailableOutputsChangeNotification
default	18:41:09.422133+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c63ab posting AVAudioSessionAvailableInputsChangeNotification
default	18:41:09.422252+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c63ab posting AVAudioSessionAvailableOutputsChangeNotification
default	18:41:09.483333+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c63ab posting AVAudioSessionAvailableOutputsChangeNotification
default	18:41:09.499891+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c63ab posting AVAudioSessionAvailableInputsChangeNotification
default	18:41:09.500124+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c63ab posting AVAudioSessionAvailableOutputsChangeNotification
default	18:41:09.528193+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c63ab posting AVAudioSessionAvailableOutputsChangeNotification
default	18:41:09.546103+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c63ab posting AVAudioSessionAvailableInputsChangeNotification
default	18:41:09.547573+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c63ab posting AVAudioSessionAvailableOutputsChangeNotification
default	18:41:09.561608+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c63ab posting AVAudioSessionAvailableOutputsChangeNotification
default	18:41:09.574412+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c63ab posting AVAudioSessionAvailableInputsChangeNotification
default	18:41:09.574501+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c63ab posting AVAudioSessionAvailableOutputsChangeNotification
default	18:41:13.007940+0800	hootowl	tcp_close [C15.1.1.1:3] TCP Packets:
	 snd    0.000s seq 4036403936:4036403937 ack 0          win 65535 len 0    [SEC]
	 rcv    0.109s seq 4157855184:4157855185 ack 4036403937 win 65535 len 0    [S.E] ECT0
	 snd    0.000s seq 4036403937:4036403937 ack 4157855185 win 2053  len 0    [.]
	 snd    0.002s seq 4036403937:4036405365 ack 4157855185 win 2053  len 1428 [.] ECT0
	 snd    0.000s seq 4036405365:4036405476 ack 4157855185 win 2053  len 111  [P.] ECT0
	 rcv    0.098s seq 4157855185:4157855185 ack 4036405476 win 16385 len 0    [.]
	 rcv    0.000s seq 4157855185:4157855284 ack 4036405476 win 16385 len 99   [P.] ECT0
	 snd    0.000s seq 4036405476:4036405476 ack 4157855284 win 2052  len 0    [.]
	 snd    0.004s seq 4036405476:4036405861 ack 4157855284 win 2052  len 385  [P.] ECT0
	 rcv    0.076s seq 4157855284:4157856724 ack 4036405861 win 16384 len 1440 [.] ECT0
	 snd    0.000s seq 4036405861:4036405861 ack 4157856724 win 2030  len 0    [.]
	 rcv    0.005s seq 4157856724:4157865517 ack 4036405861 win 16384 len 8793 [P.] ECT0
	 snd    0.000s seq 4036405861:4036405861 ack 4157865517 win 1911  len 0    [.]
	 snd    0.000s seq 4036405861:4036405861 ack 4157865517 win 2048  len 0    [.]
	 snd    0.023s seq 4036405861:4036405935 ack 4157865517 win 2048  len 74   [P.] ECT0
	 snd    0.002s seq 4036405935:4036406294 ack 4157865517 win 2048  len 359  [P.] ECT0
	 rcv    0.066s seq 4157865517:4157865620 ack 4036405935 win 16383 len 103  [P.] ECT0
	 snd    0.000s seq 4036406294:4036406294 ack 4157865620 win 2047  len 0    [.]
	 rcv    0.008s seq 4157865620:4157865950 ack 4036406294 win 16382 len 330  [P.] ECT0
	 snd    0.000s seq 4036406294:4036406294 ack 4157865950 win 2043  len 0    [.]
	 rcv    0.771s seq 4157865950:4157865950 ack 4036406294 win 16382 len 0    [.]
	 snd   30.256s seq 4036406294:4036406318 ack 4157865950 win 2048  len 24   [P.] ECT0
	 snd    0.003s seq 4036406318:4036406319 ack 4157865950 win 2048  len 0    [F.]
	 rcv    0.112s seq 4157865950:4157865950 ack 4036406319 win 16382 len 0    [.]
	 rcv    0.015s seq 4157865950:4157865951 ack 4036406319 win 16382 len 0    [F.]
	 snd    0.000s seq 4036406319:4036406319 ack 4157865951 win 2048  len 0    [.]
	Last packet 30094ms ago.
default	18:41:53.927711+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c63ab posting AVAudioSessionAvailableOutputsChangeNotification
default	18:41:53.945457+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c63ab posting AVAudioSessionAvailableInputsChangeNotification
default	18:41:53.945478+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c63ab posting AVAudioSessionAvailableOutputsChangeNotification
default	18:41:53.978707+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c63ab posting AVAudioSessionAvailableOutputsChangeNotification
default	18:41:53.995156+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c63ab posting AVAudioSessionAvailableInputsChangeNotification
default	18:41:53.995301+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c63ab posting AVAudioSessionAvailableOutputsChangeNotification
default	18:41:54.025544+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c63ab posting AVAudioSessionAvailableOutputsChangeNotification
default	18:41:54.042860+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c63ab posting AVAudioSessionAvailableInputsChangeNotification
default	18:41:54.042918+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c63ab posting AVAudioSessionAvailableOutputsChangeNotification
default	18:42:11.765017+0800	hootowl	Task <AC8BA4C4-170C-4708-8C04-64469D722B37>.<11> resuming, timeouts(60.0, 604800.0) qos(0x15) voucher((null)) activity(00000000-0000-0000-0000-000000000000)
default	18:42:11.778532+0800	hootowl	Connection 0: creating secure tcp or quic connection
default	18:42:11.779731+0800	hootowl	Connection 16: enabling TLS
default	18:42:11.779980+0800	hootowl	Connection 16: starting, TC(0x0)
default	18:42:11.780172+0800	hootowl	[C16 252DDCCB-F04C-4CBB-BCBB-860289CF37CA tcgbusfs.blob.core.windows.net:443 quic-connection, url: https://tcgbusfs.blob.core.windows.net/blobtcmsv/TCMSV_allavailable.json, definite, attribution: developer, context: com.apple.CFNetwork.NSURLSession.{C8A30AB7-8A8F-46A2-A794-FF53331E2689}{(null)}{Y}{2}{0x0} (private), proc: 1B526020-2DE0-3C65-9122-F1177549D69A, delegated upid: 0] start
default	18:42:11.780599+0800	hootowl	[C16 tcgbusfs.blob.core.windows.net:443 initial parent-flow ((null))] event: path:start @0.000s
default	18:42:11.781419+0800	hootowl	[C16 tcgbusfs.blob.core.windows.net:443 waiting parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.003s, uuid: 5761654E-E101-447B-B5A8-B54861480F59
default	18:42:11.781574+0800	hootowl	[C16 tcgbusfs.blob.core.windows.net:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_connect @0.003s
default	18:42:11.781590+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C16] reporting state preparing
default	18:42:11.781807+0800	hootowl	[C16 tcgbusfs.blob.core.windows.net:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_child @0.004s
default	18:42:11.781874+0800	hootowl	[C16.1 tcgbusfs.blob.core.windows.net:443 initial path ((null))] event: path:start @0.004s
default	18:42:11.782114+0800	hootowl	[C16.1 tcgbusfs.blob.core.windows.net:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.004s, uuid: 5761654E-E101-447B-B5A8-B54861480F59
default	18:42:11.782183+0800	hootowl	[C16.1 tcgbusfs.blob.core.windows.net:443 in_progress transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: transform:start @0.004s
default	18:42:11.782584+0800	hootowl	[C16.1.1 tcgbusfs.blob.core.windows.net:443 initial path ((null))] event: path:start @0.005s
default	18:42:11.783442+0800	hootowl	[C16.1.1 tcgbusfs.blob.core.windows.net:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.006s, uuid: 9D2C7733-E4FD-4485-A91A-90D905755BFD
default	18:42:11.783647+0800	hootowl	[C16.1.1 tcgbusfs.blob.core.windows.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:start_dns @0.006s
default	18:42:11.783838+0800	hootowl	Task <AC8BA4C4-170C-4708-8C04-64469D722B37>.<11> setting up Connection 16
default	18:42:11.829989+0800	hootowl	nw_endpoint_resolver_update [C16.1.1 tcgbusfs.blob.core.windows.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Adding endpoint handler for 20.150.22.100:443
default	18:42:11.830797+0800	hootowl	[C16.1.1 tcgbusfs.blob.core.windows.net:443 in_progress resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: resolver:receive_dns @0.052s
default	18:42:11.832012+0800	hootowl	[C16.1.1.1 20.150.22.100:443 initial path ((null))] event: path:start @0.053s
default	18:42:11.834398+0800	hootowl	[C16.1.1.1 20.150.22.100:443 waiting path (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: path:satisfied @0.055s, uuid: 93E1120B-D651-48B9-AB9C-47A4FF204064
default	18:42:11.835927+0800	hootowl	[C16.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_nexus @0.056s
default	18:42:11.837343+0800	hootowl	[C16.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:receive_nexus @0.058s
default	18:42:11.838547+0800	hootowl	[C16.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:start_connect @0.061s
default	18:42:11.839062+0800	hootowl	tcp_output [C16.1.1.1:3] flags=[SEC] seq=1720023913, ack=0, win=65535 state=SYN_SENT rcv_nxt=0, snd_una=1720023913
default	18:42:11.962012+0800	hootowl	tcp_input [C16.1.1.1:3] flags=[S.E] seq=497560527, ack=1720023914, win=65535 state=SYN_SENT rcv_nxt=0, snd_una=1720023913
default	18:42:11.962409+0800	hootowl	nw_flow_connected [C16.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Transport protocol connected (tcp)
default	18:42:11.962770+0800	hootowl	[C16.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_transport @0.185s
default	18:42:11.964893+0800	hootowl	boringssl_session_apply_protocol_options_for_transport_block_invoke_2(2367) [C16.1.1.1:2][0x11c25cce0] TLS configured [server(0) min_version(0x0303) max_version(0x0304) name(tcgbusfs.blob.core.windows.net) tickets(false) false_start(false) enforce_ev(false) enforce_ats(false) ats_non_pfs_ciphersuite_allowed(false) cc_mode_enforced(false) ech(false) pqtls(true), pake(false) skip_ats_trust(false)]
default	18:42:11.965019+0800	hootowl	boringssl_context_info_handler(2806) [C16.1.1.1:2][0x11c25cce0] Client handshake started
default	18:42:11.965637+0800	hootowl	boringssl_context_info_handler(2823) [C16.1.1.1:2][0x11c25cce0] Client handshake state: TLS client enter_early_data
default	18:42:11.966712+0800	hootowl	boringssl_context_info_handler(2823) [C16.1.1.1:2][0x11c25cce0] Client handshake state: TLS client read_server_hello
default	18:42:12.066450+0800	hootowl	boringssl_context_info_handler(2823) [C16.1.1.1:2][0x11c25cce0] Client handshake state: TLS 1.3 client read_hello_retry_request
default	18:42:12.073815+0800	hootowl	boringssl_context_info_handler(2823) [C16.1.1.1:2][0x11c25cce0] Client handshake state: TLS 1.3 client send_second_client_hello
default	18:42:12.075237+0800	hootowl	boringssl_context_info_handler(2823) [C16.1.1.1:2][0x11c25cce0] Client handshake state: TLS 1.3 client read_server_hello
default	18:42:12.158876+0800	hootowl	boringssl_context_info_handler(2823) [C16.1.1.1:2][0x11c25cce0] Client handshake state: TLS 1.3 client read_encrypted_extensions
default	18:42:12.189805+0800	hootowl	boringssl_context_info_handler(2823) [C16.1.1.1:2][0x11c25cce0] Client handshake state: TLS 1.3 client read_certificate_request
default	18:42:12.190877+0800	hootowl	boringssl_context_info_handler(2823) [C16.1.1.1:2][0x11c25cce0] Client handshake state: TLS 1.3 client read_server_certificate
default	18:42:12.193474+0800	hootowl	boringssl_context_info_handler(2823) [C16.1.1.1:2][0x11c25cce0] Client handshake state: TLS 1.3 client read_server_certificate_verify
default	18:42:12.198757+0800	hootowl	boringssl_context_evaluate_trust_async(2249) [C16.1.1.1:2][0x11c25cce0] Performing external trust evaluation
default	18:42:12.199004+0800	hootowl	boringssl_context_evaluate_trust_async_external(2234) [C16.1.1.1:2][0x11c25cce0] Asyncing for external verify block
default	18:42:12.199796+0800	hootowl	Connection 16: asked to evaluate TLS Trust
default	18:42:12.200330+0800	hootowl	Task <AC8BA4C4-170C-4708-8C04-64469D722B37>.<11> auth completion disp=1 cred=0x0
default	18:42:12.200397+0800	hootowl	(Trust 0x11be3b900) No pending evals, starting
default	18:42:12.200920+0800	hootowl	[0x112190b40] activating connection: mach=true listener=false peer=false name=com.apple.trustd
default	18:42:12.200938+0800	hootowl	(Trust 0x11be3b900) Completed async eval kickoff
default	18:42:12.217211+0800	hootowl	(Trust 0x11be3b900) trustd returned 4
default	18:42:12.218471+0800	hootowl	System Trust Evaluation yielded status(0)
default	18:42:12.218820+0800	hootowl	(Trust 0x11be3b3c0) No pending evals, starting
default	18:42:12.220408+0800	hootowl	[0x112193700] activating connection: mach=true listener=false peer=false name=com.apple.trustd
default	18:42:12.220510+0800	hootowl	(Trust 0x11be3b3c0) Completed async eval kickoff
default	18:42:12.221877+0800	hootowl	[0x112190b40] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	18:42:12.235380+0800	hootowl	(Trust 0x11be3b3c0) trustd returned 4
default	18:42:12.235728+0800	hootowl	Connection 16: TLS Trust result 0
default	18:42:12.235852+0800	hootowl	boringssl_context_evaluate_trust_async_external_block_invoke_3(2148) [C16.1.1.1:2][0x11c25cce0] Returning from external verify block with result: true
default	18:42:12.236310+0800	hootowl	boringssl_context_certificate_verify_callback(2430) [C16.1.1.1:2][0x11c25cce0] Certificate verification result: OK
default	18:42:12.236485+0800	hootowl	boringssl_context_info_handler(2823) [C16.1.1.1:2][0x11c25cce0] Client handshake state: TLS 1.3 client read_server_finished
default	18:42:12.237138+0800	hootowl	boringssl_context_info_handler(2823) [C16.1.1.1:2][0x11c25cce0] Client handshake state: TLS 1.3 client send_end_of_early_data
default	18:42:12.237549+0800	hootowl	boringssl_context_info_handler(2823) [C16.1.1.1:2][0x11c25cce0] Client handshake state: TLS 1.3 client send_client_encrypted_extensions
default	18:42:12.237570+0800	hootowl	boringssl_context_info_handler(2823) [C16.1.1.1:2][0x11c25cce0] Client handshake state: TLS 1.3 client send_client_certificate
default	18:42:12.238559+0800	hootowl	boringssl_context_info_handler(2823) [C16.1.1.1:2][0x11c25cce0] Client handshake state: TLS 1.3 client complete_second_flight
default	18:42:12.239641+0800	hootowl	boringssl_context_info_handler(2823) [C16.1.1.1:2][0x11c25cce0] Client handshake state: TLS 1.3 client done
default	18:42:12.240325+0800	hootowl	boringssl_context_info_handler(2823) [C16.1.1.1:2][0x11c25cce0] Client handshake state: TLS client finish_client_handshake
default	18:42:12.240339+0800	hootowl	boringssl_context_info_handler(2823) [C16.1.1.1:2][0x11c25cce0] Client handshake state: TLS client done
default	18:42:12.240773+0800	hootowl	boringssl_context_info_handler(2812) [C16.1.1.1:2][0x11c25cce0] Client handshake done
default	18:42:12.242768+0800	hootowl	nw_protocol_boringssl_signal_connected(895) [C16.1.1.1:2][0x11c25cce0] TLS connected [server(0) version(0x0304) ciphersuite(TLS_AES_256_GCM_SHA384) group(0x0018) signature_alg(0x0804) alpn(nil) resumed(0) offered_ticket(0) in_early_data(0) early_data_accepted(0) false_started(0) ocsp_received(1) sct_received(0) connect_time(277ms) flight_time(185ms) rtt(100ms) write_stalls(0) read_stalls(10) pake(0x0000)]
default	18:42:12.242948+0800	hootowl	nw_flow_connected [C16.1.1.1 20.150.22.100:443 in_progress channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (CFNetworkConnection-398509258)
default	18:42:12.243247+0800	hootowl	[C16.1.1.1 20.150.22.100:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.465s
default	18:42:12.243411+0800	hootowl	[C16.1.1 tcgbusfs.blob.core.windows.net:443 ready resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.465s
default	18:42:12.243628+0800	hootowl	[C16.1 tcgbusfs.blob.core.windows.net:443 ready transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:child_finish_connect @0.466s
default	18:42:12.244074+0800	hootowl	[C16.1.1.1 20.150.22.100:443 ready channel-flow (satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.466s
default	18:42:12.244220+0800	hootowl	[C16.1.1 tcgbusfs.blob.core.windows.net:443 ready resolver (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.466s
default	18:42:12.244373+0800	hootowl	[C16.1 tcgbusfs.blob.core.windows.net:443 ready transform (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.466s
default	18:42:12.244532+0800	hootowl	nw_flow_connected [C16 20.150.22.100:443 in_progress parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] Output protocol connected (endpoint_flow)
default	18:42:12.244836+0800	hootowl	[C16 20.150.22.100:443 ready parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:finish_connect @0.467s
default	18:42:12.245516+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C16] reporting state ready
default	18:42:12.245610+0800	hootowl	[C16 20.150.22.100:443 ready parent-flow (satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good)] event: flow:changed_viability @0.467s
default	18:42:12.245816+0800	hootowl	nw_connection_send_viability_changed_on_nw_queue [C16] viability_changed_handler(true)
default	18:42:12.246066+0800	hootowl	[0x112193700] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	18:42:12.246082+0800	hootowl	Connection 16: connected successfully
default	18:42:12.246088+0800	hootowl	Connection 16: TLS handshake complete
default	18:42:12.246221+0800	hootowl	Connection 16: ready C(N) E(N)
default	18:42:12.246249+0800	hootowl	Task <AC8BA4C4-170C-4708-8C04-64469D722B37>.<11> now using Connection 16
default	18:42:12.246773+0800	hootowl	Connection 16: received viability advisory(Y)
default	18:42:12.246787+0800	hootowl	Task <AC8BA4C4-170C-4708-8C04-64469D722B37>.<11> sent request, body N 0
default	18:42:12.386229+0800	hootowl	Task <AC8BA4C4-170C-4708-8C04-64469D722B37>.<11> received response, status 200 content K
default	18:42:12.825567+0800	hootowl	Task <AC8BA4C4-170C-4708-8C04-64469D722B37>.<11> response ended
default	18:42:12.825609+0800	hootowl	Task <AC8BA4C4-170C-4708-8C04-64469D722B37>.<11> done using Connection 16
default	18:42:12.825683+0800	hootowl	[C16] event: client:connection_idle @1.048s
default	18:42:12.825938+0800	hootowl	Task <AC8BA4C4-170C-4708-8C04-64469D722B37>.<11> summary for task success {transaction_duration_ms=1059, response_status=200, connection=16, protocol="http/1.1", domain_lookup_duration_ms=46, connect_duration_ms=406, secure_connection_duration_ms=277, private_relay=false, request_start_ms=480, request_duration_ms=0, response_start_ms=619, response_duration_ms=439, request_bytes=337, request_throughput_kbps=12365, response_bytes=460399, response_throughput_kbps=8389, cache_hit=true}
default	18:42:12.826172+0800	hootowl	nw_protocol_tcp_notify [C16.1.1.1:3] nw_protocol_notification_type_connection_idle is true
default	18:42:12.826257+0800	hootowl	nw_protocol_tcp_set_connection_idle [C16.1.1.1:3] os_nexus_flow_set_connection_idle returned 0
default	18:42:12.826498+0800	hootowl	[C16] event: client:connection_idle @1.048s
default	18:42:12.826678+0800	hootowl	nw_protocol_tcp_notify [C16.1.1.1:3] nw_protocol_notification_type_connection_idle is true
default	18:42:12.826731+0800	hootowl	nw_protocol_tcp_set_connection_idle [C16.1.1.1:3] os_nexus_flow_set_connection_idle returned 0
default	18:42:12.826812+0800	hootowl	Task <AC8BA4C4-170C-4708-8C04-64469D722B37>.<11> finished successfully
default	18:42:12.826999+0800	hootowl	Mu1Base+Ext 152
taipei 📦 minutely Received 459946 bytes
default	18:42:12.828346+0800	hootowl	Mu1Base+Ext 175
previousHash updated
error	18:42:12.857465+0800	hootowl	333	wireAvailableUpdateFromMunicipal()	⚠️ duplicate parkIds in avail feed (11): 040014(綠寶石區, ?), 040037(綠光河岸區, ?), 040068(玉清宮, ?), 060021(陽光運動公園, ?), 060047(親情河濱公園1區, ?), 060068(萊茵區, ?), 060079(城市車旅新店安德二, ?), 060085(親情河濱公園2區, ?), 060085(親情河濱公園2區, ?), 170120(MITSUI OUTLET PARK 林口二館收費, ?), 170120(MITSUI OUTLET PARK 林口二館收費, ?)
default	18:42:12.864264+0800	hootowl	Municipal+Cyclops 79
🎨 model refreshed — obs:0s car:21 thread:main
default	18:42:12.864711+0800	hootowl	Municipal 130
🐎 minutelyAvailable ["newTaipeiCity ⏳03 18:35 ∑1429", "taipei ⏳03 18:42 ∑1113"]
default	18:42:12.877379+0800	hootowl	Municipal+Cyclops 79
🎨 model refreshed — obs:0s car:21 thread:main
default	18:42:22.432497+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c63ab posting AVAudioSessionAvailableOutputsChangeNotification
default	18:42:22.456099+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c63ab posting AVAudioSessionAvailableInputsChangeNotification
default	18:42:22.456146+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c63ab posting AVAudioSessionAvailableOutputsChangeNotification
default	18:42:22.488197+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c63ab posting AVAudioSessionAvailableOutputsChangeNotification
default	18:42:22.500869+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c63ab posting AVAudioSessionAvailableInputsChangeNotification
default	18:42:22.501023+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c63ab posting AVAudioSessionAvailableOutputsChangeNotification
default	18:42:22.521945+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c63ab posting AVAudioSessionAvailableOutputsChangeNotification
default	18:42:22.531817+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c63ab posting AVAudioSessionAvailableInputsChangeNotification
default	18:42:22.531924+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c63ab posting AVAudioSessionAvailableOutputsChangeNotification
default	18:42:22.573158+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c63ab posting AVAudioSessionAvailableOutputsChangeNotification
default	18:42:22.591351+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c63ab posting AVAudioSessionAvailableInputsChangeNotification
default	18:42:22.591471+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c63ab posting AVAudioSessionAvailableOutputsChangeNotification
default	18:42:43.279989+0800	hootowl	Connection 16: cleaning up
default	18:42:43.280111+0800	hootowl	[C16 252DDCCB-F04C-4CBB-BCBB-860289CF37CA tcgbusfs.blob.core.windows.net:443 quic-connection, url: https://tcgbusfs.blob.core.windows.net/blobtcmsv/TCMSV_allavailable.json, definite, attribution: developer] cancel
default	18:42:43.280633+0800	hootowl	[C16 252DDCCB-F04C-4CBB-BCBB-860289CF37CA tcgbusfs.blob.core.windows.net:443 quic-connection, url: https://tcgbusfs.blob.core.windows.net/blobtcmsv/TCMSV_allavailable.json, definite, attribution: developer] cancelled
	[C16.1.1.1 93E1120B-D651-48B9-AB9C-47A4FF204064 192.168.50.191:55888<->20.150.22.100:443]
	Connected Path: satisfied (Path is satisfied), viable, interface: en0[802.11], ipv4, dns, uses wifi, LQM: good
	Privacy Stance: Not Eligible
	Duration: 31.503s, DNS @0.006s took 0.046s, TCP @0.061s took 0.124s,  took 0.277s
	bytes in/out: 471472/2357, packets in/out: 73/78, rtt: 0.119s, retransmitted bytes: 0, out-of-order bytes: 0
	ecn packets sent/acked/marked/lost: 5/3/0/0
default	18:42:43.281744+0800	hootowl	nw_protocol_tcp_log_summary [C16.1.1.1:3] 
	[DD156664-F10C-43C1-8E7B-0134A28FB89D 192.168.50.191:55888<->20.150.22.100:443]
	Init: 1, Conn_Time: 123.285ms, SYNs: 1, WR_T: 0/0, RD_T: 0/0, TFO: 0/0/0, ECN: 0/1/1, Accurate ECN (client/server): Disabled/Disabled, TS: 1, TSO: 0
	rtt_cache: process, rtt_upd: 4, rtt: 119.781ms, rtt_var: 44.000ms rtt_nc: 119.781ms, rtt_var_nc: 44.000ms base rtt: 63ms
	ACKs-compressed: 9, ACKs delayed: 29 delayed ACKs sent: 0
default	18:42:43.282614+0800	hootowl	nw_connection_report_state_with_handler_on_nw_queue [C16] reporting state cancelled
default	18:42:43.282762+0800	hootowl	Connection 16: done
default	18:42:43.282918+0800	hootowl	tcp_output [C16.1.1.1:3] flags=[F.] seq=1720026295, ack=498032000, win=6288 state=FIN_WAIT_1 rcv_nxt=498032000, snd_una=1720026271
default	18:42:43.446553+0800	hootowl	tcp_input [C16.1.1.1:3] flags=[F.] seq=498032000, ack=1720026296, win=16382 state=FIN_WAIT_2 rcv_nxt=498032000, snd_una=1720026296
default	18:43:05.657198+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c63ab posting AVAudioSessionAvailableOutputsChangeNotification
default	18:43:05.672581+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c63ab posting AVAudioSessionAvailableInputsChangeNotification
default	18:43:05.672668+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c63ab posting AVAudioSessionAvailableOutputsChangeNotification
default	18:43:05.688963+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c63ab posting AVAudioSessionAvailableOutputsChangeNotification
default	18:43:05.698489+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c63ab posting AVAudioSessionAvailableInputsChangeNotification
default	18:43:05.698604+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c63ab posting AVAudioSessionAvailableOutputsChangeNotification
default	18:43:05.710475+0800	hootowl	       SessionCore_iOS.mm:342   Session 0x77c63ab posting AVAudioSessionAvailableOutputsChangeNotification
default	18:43:05.719834+0800	hootowl	       SessionCore_iOS.mm:311   Session 0x77c63ab posting AVAudioSessionAvailableInputsChangeNotification
default	18:43:05.719923+0800	hootowl	       SessionCore_iOS.mm:315   Session 0x77c63ab posting AVAudioSessionAvailableOutputsChangeNotification
default	18:43:13.532499+0800	hootowl	tcp_close [C16.1.1.1:3] TCP Packets:
	 rcv    0.000s seq  497853203:497856083  ack 1720026271 win 16382 len 2880 [.] ECT0
	 snd    0.000s seq 1720026271:1720026271 ack 497856083  win 6288  len 0    [.]
	 rcv    0.004s seq  497856083:497871923  ack 1720026271 win 16382 len 15840 [.] ECT0
	 rcv    0.000s seq  497871923:497887763  ack 1720026271 win 16382 len 15840 [P.] ECT0
	 rcv    0.000s seq  497887763:497894963  ack 1720026271 win 16382 len 7200 [.] ECT0
	 snd    0.000s seq 1720026271:1720026271 ack 497894963  win 6288  len 0    [.]
	 rcv    0.002s seq  497894963:497902163  ack 1720026271 win 16382 len 7200 [.] ECT0
	 snd    0.000s seq 1720026271:1720026271 ack 497902163  win 6288  len 0    [.]
	 rcv    0.006s seq  497902163:497909363  ack 1720026271 win 16382 len 7200 [.] ECT0
	 snd    0.000s seq 1720026271:1720026271 ack 497909363  win 6288  len 0    [.]
	 rcv    0.049s seq  497909363:497913683  ack 1720026271 win 16382 len 4320 [.] ECT0
	 snd    0.000s seq 1720026271:1720026271 ack 497913683  win 6288  len 0    [.]
	 rcv    0.000s seq  497913683:497916563  ack 1720026271 win 16382 len 2880 [.] ECT0
	 rcv    0.000s seq  497916563:497919443  ack 1720026271 win 16382 len 2880 [.] ECT0
	 snd    0.000s seq 1720026271:1720026271 ack 497919443  win 6288  len 0    [.]
	 rcv    0.003s seq  497919443:497929523  ack 1720026271 win 16382 len 10080 [.] ECT0
	 snd    0.000s seq 1720026271:1720026271 ack 497929523  win 6288  len 0    [.]
	 rcv    0.005s seq  497929523:497932403  ack 1720026271 win 16382 len 2880 [.] ECT0
	 snd    0.000s seq 1720026271:1720026271 ack 497932403  win 6288  len 0    [.]
	 rcv    0.003s seq  497932403:497948243  ack 1720026271 win 16382 len 15840 [.] ECT0
	 rcv    0.000s seq  497948243:497956883  ack 1720026271 win 16382 len 8640 [.] ECT0
	 snd    0.000s seq 1720026271:1720026271 ack 497956883  win 6288  len 0    [.]
	 rcv    0.006s seq  497956883:497972723  ack 1720026271 win 16382 len 15840 [.] ECT0
	 snd    0.000s seq 1720026271:1720026271 ack 497972723  win 6288  len 0    [.]
	 rcv    0.001s seq  497972723:497988563  ack 1720026271 win 16382 len 15840 [.] ECT0
	 rcv    0.000s seq  497988563:497991443  ack 1720026271 win 16382 len 2880 [.] ECT0
	 snd    0.000s seq 1720026271:1720026271 ack 497991443  win 6288  len 0    [.]
	 rcv    0.005s seq  497991443:498007283  ack 1720026271 win 16382 len 15840 [.] ECT0
	 rcv    0.000s seq  498007283:498023123  ack 1720026271 win 16382 len 15840 [.] ECT0
	 rcv    0.000s seq  498023123:498026003  ack 1720026271 win 16382 len 2880 [.] ECT0
	 rcv    0.000s seq  498026003:498028883  ack 1720026271 win 16382 len 2880 [.] ECT0
	 snd    0.000s seq 1720026271:1720026271 ack 498028883  win 6288  len 0    [.]
	 rcv    0.001s seq  498028883:498032000  ack 1720026271 win 16382 len 3117 [P.] ECT0
	 snd    0.000s seq 1720026271:1720026271 ack 498032000  win 6288  len 0    [.]
	 rcv    0.655s seq  498032000:498032000  ack 1720026271 win 16382 len 0    [.]
	 snd   29.792s seq 1720026271:1720026295 ack 498032000  win 6288  len 24   [P.] ECT0
	 snd    0.002s seq 1720026295:1720026296 ack 498032000  win 6288  len 0    [F.]
	 rcv    0.152s seq  498032000:498032000  ack 1720026296 win 16382 len 0    [.]
	 rcv    0.000s seq  498032000:498032001  ack 1720026296 win 16382 len 0    [F.]
	 snd    0.000s seq 1720026296:1720026296 ack 498032001  win 6288  len 0    [.]
	Last packet 30097ms ago.
default	18:43:45.689053+0800	hootowl	TX focusApplication (peekAppEvent) stealKB:Y scene:com.sharkda.hootowl-1B8F959F-618F-4A0D-AD89-E09DEC0EAB34
default	18:43:45.689912+0800	hootowl	Evaluating dispatch of UIEvent: 0x11cfa2200; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	18:43:45.690360+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	18:43:45.690376+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1099f0400>; contextId: 0x6989FC6
default	18:43:45.714438+0800	hootowl	Evaluating dispatch of UIEvent: 0x11cfa2200; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	18:43:45.772737+0800	hootowl	Evaluating dispatch of UIEvent: 0x11cfa2200; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 1
default	18:43:45.772763+0800	hootowl	Evaluating dispatch of UIEvent: 0x11cfa2200; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	18:43:45.772787+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	18:43:45.772818+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1099f0400>; contextId: 0x6989FC6
default	18:43:45.783406+0800	hootowl	<UIWindowScene: 0x10cc50200> (1B8F959F-618F-4A0D-AD89-E09DEC0EAB34) Scene updated orientation preferences: ( Pu Ll Lr ) -> ( Pu )
default	18:43:46.394655+0800	hootowl	<UIWindowScene: 0x10cc50200> (1B8F959F-618F-4A0D-AD89-E09DEC0EAB34) Scene updated orientation preferences: ( Pu ) -> ( Pu Ll Lr )
default	18:43:47.536499+0800	hootowl	TX focusApplication (peekAppEvent) stealKB:Y scene:com.sharkda.hootowl-1B8F959F-618F-4A0D-AD89-E09DEC0EAB34
default	18:43:47.537264+0800	hootowl	Evaluating dispatch of UIEvent: 0x11cfa2200; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	18:43:47.537517+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	18:43:47.537663+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1099f0400>; contextId: 0x6989FC6
default	18:43:47.539217+0800	hootowl	[0x112205540] activating connection: mach=true listener=false peer=false name=com.apple.DragUI.druid.source
default	18:43:47.554131+0800	hootowl	_UIInternalDraggingSessionSource: Drag session state changing from New to Connecting
default	18:43:47.554296+0800	hootowl	[0x1121e1a40] activating connection: mach=true listener=false peer=false name=com.apple.DragUI.druid.source
default	18:43:47.554539+0800	hootowl	_UIDruidSourceConnection beginDragWithTouches:items:completion:
default	18:43:47.554862+0800	hootowl	[0x1121e2080] activating connection: mach=false listener=true peer=false name=(anonymous)
default	18:43:47.554882+0800	hootowl	[0x1121e2080] Connection returned listener port: 0xf5c3
default	18:43:47.557810+0800	hootowl	Evaluating dispatch of UIEvent: 0x11cfa2200; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	18:43:47.558026+0800	hootowl	Evaluating dispatch of UIEvent: 0x11cfa2200; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	18:43:47.558124+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	18:43:47.558183+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1099f0400>; contextId: 0x6989FC6
default	18:43:47.560113+0800	hootowl	_UIDruidSourceConnection beginDragWithTouches:items:completion: got replyHandler with sessionID 2941674394
default	18:43:47.560165+0800	hootowl	_UIInternalDraggingSessionSource: Drag session state changing from Connecting to Dragging
default	18:43:47.592173+0800	hootowl	_UIDruidSourceConnection requestDragPreviewsForIndexSet:reply: <NSMutableIndexSet: 0x13bfd68a0>[number of indexes: 1 (in 1 ranges), indexes: (0)]
default	18:43:47.597460+0800	hootowl	[0x11bdca580] activating connection: mach=true listener=false peer=false name=com.apple.DragUI.druid.destination
default	18:43:47.597506+0800	hootowl	Evaluating dispatch of UIEvent: 0x13bfef800; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	18:43:47.597594+0800	hootowl	Evaluating dispatch of UIEvent: 0x13bfef800; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	18:43:47.598299+0800	hootowl	RX setKeyboardDisabled:Y
default	18:43:47.598715+0800	hootowl	setDeactivatedKeyboard: 1 forScene: (null) forSuppressionAssertion: 0
default	18:43:47.599579+0800	hootowl	[0x1120e7c00] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0x1121e2080.peer[36148].0x1120e7c00
default	18:43:47.600172+0800	hootowl	Change from input view set: (null)
default	18:43:47.600325+0800	hootowl	Change to input view set: (null)
default	18:43:47.600343+0800	hootowl	_UIDruidDestinationConnection: sawFirstDragEvent reply with session <_NSXPCDistantObject: 0x139c4d860>
default	18:43:47.600369+0800	hootowl	_moveGuideOffscreenAtEdge: 4
default	18:43:47.600382+0800	hootowl	changeOffsetConstants: offset is changing to {0, 0} [previous offset: {-1, -1}]
default	18:43:47.619323+0800	hootowl	changeSizingConstants: size is changing [not transitioning] to {393, 0} [previous size: {1, 0}]
default	18:43:47.619656+0800	hootowl	setDeactivatedKeyboard, shouldUpdatePlacement: 1
default	18:43:47.619735+0800	hootowl	setPlacementChangeDisabled: 1, placement: <UITrackingElementPlacementInitialPosition> (self: <UITrackingElementWindowController: 0x109a30a00>)
default	18:43:47.619751+0800	hootowl	Moving from placement: <UITrackingElementPlacementInitialPosition> to placement: <UITrackingElementPlacementInitialPosition> (currentPlacement: <UITrackingElementPlacementInitialPosition>)
default	18:43:47.619793+0800	hootowl	KeyboardTrackingCoordinator: Creating tracking coordinator for <UIWindowScene: 0x10cc50200; role: UIWindowSceneSessionRoleApplication; persistentIdentifier: 1B8F959F-618F-4A0D-AD89-E09DEC0EAB34; activationState: UISceneActivationStateForegroundActive>
default	18:43:47.840672+0800	hootowl	updatePlacementWithPlacement: <UITrackingElementPlacementInitialPosition>
default	18:43:47.841170+0800	hootowl	KeyboardTrackingCoordinator: Creating tracking provider for <UIWindowScene: 0x10cc50200; role: UIWindowSceneSessionRoleApplication; persistentIdentifier: 1B8F959F-618F-4A0D-AD89-E09DEC0EAB34; activationState: UISceneActivationStateForegroundActive>
default	18:43:47.841480+0800	hootowl	Tracking provider: moveFromPlacement: <UITrackingElementPlacementInitialPosition> toPlacement: <UITrackingElementPlacementInitialPosition> update to {{0, 852}, {393, 0}}
default	18:43:47.841747+0800	hootowl	Updating tracking clients for start <TUIKeyboardTrackingCoordinator:0x11be03c00 state=<TUIKeyboardState: 0x1394b7e60 State: offscreen; is docked>; frame={{0, 852}, {393, 0}}; animation=<TUIKeyboardAnimationInfo: 0x139e54580, duration: 0.38, from local keyboard, is not rotating, should animate, type: 0, notificationInfo: {
    UIKeyboardAnimationCurveUserInfoKey = 7;
    UIKeyboardAnimationDurationUserInfoKey = "0.3833";
    UIKeyboardBoundsUserInfoKey = "NSRect: {{0, 0}, {393, 0}}";
    UIKeyboardCenterBeginUserInfoKey = "NSPoint: {196.5, 426}";
    UIKeyboardCenterEndUserInfoKey = "NSPoint: {196.5, 852}";
    UIKeyboardFrameBeginUserInfoKey = "NSRect: {{196.5, 426}, {0, 0}}";
    UIKeyboardFrameEndUserInfoKey = "NSRect: {{0, 852}, {393, 0}}";
    UIKeyboardIsLocalUserInfoKey = 1;
}notificationsDebug: >>
default	18:43:47.841815+0800	hootowl	Received state update for 36996 (app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>, unknown-NotVisible
default	18:43:47.856021+0800	hootowl	Init Service connection: <BSServiceConnectionEndpoint: 0x11be29580; target: NL:com.apple.AccessibilityUIServer; service: com.apple.AccessibilityUIServer>
default	18:43:47.856077+0800	hootowl	[C:3] Alloc com.apple.AccessibilityUIServer
default	18:43:47.856154+0800	hootowl	[0x11be01e00] activating connection: mach=false listener=false peer=false name=(anonymous)
default	18:43:47.859457+0800	hootowl	Connection activated to <BSXPC(com.apple.AccessibilityUIServer[C:3-1])-as(com.apple.AccessibilityUIServer):0x112240a50>
error	18:43:47.864118+0800	hootowl	Got a keyboard will change frame notification, but keyboard was not even present.
error	18:43:47.865431+0800	hootowl	Got a keyboard will hide notification, but keyboard was not even present.
default	18:43:47.865603+0800	hootowl	Posted notification willHide with {
    UIKeyboardAnimationCurveUserInfoKey = 7;
    UIKeyboardAnimationDurationUserInfoKey = "0.3833";
    UIKeyboardBoundsUserInfoKey = "NSRect: {{0, 0}, {393, 0}}";
    UIKeyboardCenterBeginUserInfoKey = "NSPoint: {196.5, 426}";
    UIKeyboardCenterEndUserInfoKey = "NSPoint: {196.5, 852}";
    UIKeyboardFrameBeginUserInfoKey = "NSRect: {{196.5, 426}, {0, 0}}";
    UIKeyboardFrameEndUserInfoKey = "NSRect: {{0, 852}, {393, 0}}";
    UIKeyboardIsLocalUserInfoKey = 1;
} (null)
default	18:43:47.867717+0800	hootowl	ClientConnection registered client SpeakThisClientIdentifier-36996
default	18:43:47.868603+0800	hootowl	App is being debugged, do not track this hang
default	18:43:47.868627+0800	hootowl	Hang detected: 0.28s (debugger attached, not reporting)
default	18:43:47.868654+0800	hootowl	Evaluating dispatch of UIEvent: 0x13bfef800; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	18:43:47.868690+0800	hootowl	0x10ce4e800 (pageProxyID=2087) -[WKWebView _updateVisibleContentRects:] - have not received a commit 482.34s after visible content rect update; lastTransactionID 0
default	18:43:47.873116+0800	hootowl	Remote touch surface type has been initialized to: Unknown
default	18:43:47.873130+0800	hootowl	Remote microphone capability has been initialized to: NO
default	18:43:47.873140+0800	hootowl	Requesting calls from host
default	18:43:47.873768+0800	hootowl	[0x11be03480] activating connection: mach=true listener=false peer=false name=com.apple.callkit.callcontrollerhost
default	18:43:47.884038+0800	hootowl	Received requested calls from host: (
)
default	18:43:47.884615+0800	hootowl	nw_path_evaluator_start [52915D24-C605-4C1A-8948-8D9131EFA3E6 <NULL> generic, multipath service: handover, attribution: developer]
	path: satisfied (Path is satisfied), interface: en0[802.11], ipv4, dns, uses wifi, LQM: good
default	18:43:47.884655+0800	hootowl	[0x11be017c0] activating connection: mach=true listener=false peer=false name=com.apple.SystemConfiguration.NetworkInformation
default	18:43:47.887528+0800	hootowl	[0x11be01cc0] activating connection: mach=true listener=false peer=false name=com.apple.TextInput
default	18:43:47.964382+0800	hootowl	<_UIKBFeedbackGenerator: 0x139dd9500>: Updating mode. Haptics: supported. Haptics: enabled. Ringer: on. Sound: disabled. Mode: haptics only
default	18:43:47.964559+0800	hootowl	-[UIDictationController setIgnoreFinalizePhrases:] Setting ignoreFinalizePhrases flag 1
default	18:43:47.964601+0800	hootowl	Posted notification didHide with {
    UIKeyboardAnimationCurveUserInfoKey = 7;
    UIKeyboardAnimationDurationUserInfoKey = "0.3833";
    UIKeyboardBoundsUserInfoKey = "NSRect: {{0, 0}, {393, 0}}";
    UIKeyboardCenterBeginUserInfoKey = "NSPoint: {196.5, 426}";
    UIKeyboardCenterEndUserInfoKey = "NSPoint: {196.5, 852}";
    UIKeyboardFrameBeginUserInfoKey = "NSRect: {{196.5, 426}, {0, 0}}";
    UIKeyboardFrameEndUserInfoKey = "NSRect: {{0, 852}, {393, 0}}";
    UIKeyboardIsLocalUserInfoKey = 1;
} (null)
default	18:43:47.964920+0800	hootowl	Evaluating dispatch of UIEvent: 0x13bfef800; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	18:43:47.964936+0800	hootowl	0x10ce4e800 (pageProxyID=2087) -[WKWebView _updateVisibleContentRects:] - have not received a commit 482.44s after visible content rect update; lastTransactionID 0
default	18:43:47.965224+0800	hootowl	_UIInternalDraggingSessionDestination: State changing from Connecting to Dragging
default	18:43:47.975416+0800	hootowl	_UIDruidDestinationConnection takePotentialDrop:<_DUIPotentialDrop 0x11bd2f800: operation=16 forbidden=0 precise=0 prefersFullSizePreview=1 preferredBadgeStyle=0>
default	18:43:47.977224+0800	hootowl	Evaluating dispatch of UIEvent: 0x13bfef800; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	18:43:47.977356+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	18:43:47.977468+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1099f0400>; contextId: 0x6989FC6
default	18:43:47.978238+0800	hootowl	Evaluating dispatch of UIEvent: 0x13bfef800; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	18:43:47.978378+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	18:43:47.978400+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1099f0400>; contextId: 0x6989FC6
default	18:43:47.982126+0800	hootowl	Received state update for 36996 (app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>, unknown-NotVisible
default	18:43:47.986407+0800	hootowl	Evaluating dispatch of UIEvent: 0x13bfef800; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	18:43:47.986481+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	18:43:47.986511+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1099f0400>; contextId: 0x6989FC6
default	18:43:47.994832+0800	hootowl	Evaluating dispatch of UIEvent: 0x13bfef800; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	18:43:47.995280+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	18:43:47.995338+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1099f0400>; contextId: 0x6989FC6
default	18:43:48.019879+0800	hootowl	Evaluating dispatch of UIEvent: 0x13bfef800; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	18:43:48.020240+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	18:43:48.020283+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1099f0400>; contextId: 0x6989FC6
default	18:43:48.028196+0800	hootowl	Evaluating dispatch of UIEvent: 0x13bfef800; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	18:43:48.028295+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	18:43:48.028526+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1099f0400>; contextId: 0x6989FC6
default	18:43:48.091094+0800	hootowl	RX keyboardChangeCompleted
default	18:43:48.093257+0800	hootowl	Received state update for 36996 (app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>, unknown-NotVisible
default	18:43:48.114871+0800	hootowl	Evaluating dispatch of UIEvent: 0x13bfef800; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	18:43:48.115149+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	18:43:48.115650+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1099f0400>; contextId: 0x6989FC6
default	18:43:48.120893+0800	hootowl	Evaluating dispatch of UIEvent: 0x13bfef800; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	18:43:48.122416+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	18:43:48.122776+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1099f0400>; contextId: 0x6989FC6
default	18:43:48.131141+0800	hootowl	Evaluating dispatch of UIEvent: 0x13bfef800; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	18:43:48.131232+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	18:43:48.131809+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1099f0400>; contextId: 0x6989FC6
default	18:43:48.138581+0800	hootowl	Evaluating dispatch of UIEvent: 0x13bfef800; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	18:43:48.138755+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	18:43:48.138963+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1099f0400>; contextId: 0x6989FC6
default	18:43:48.149347+0800	hootowl	Evaluating dispatch of UIEvent: 0x13bfef800; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	18:43:48.149385+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	18:43:48.149733+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1099f0400>; contextId: 0x6989FC6
default	18:43:48.150016+0800	hootowl	activate generator with style: TurnOn; activationCount: 0 -> 1; styleActivationCount: 0 -> 1; <_UIDragSnappingFeedbackGenerator: 0x13bc01d40>
default	18:43:48.150038+0800	hootowl	activate generator with style: TurnOn; activationCount: 1 -> 2; styleActivationCount: 1 -> 2; <_UIDragSnappingFeedbackGenerator: 0x13bc01d40>
default	18:43:48.150186+0800	hootowl	activate engine <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c022800>, clientCount: 0 -> 1
default	18:43:48.150194+0800	hootowl	activating engine <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c022800>
default	18:43:48.150202+0800	hootowl	engine <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c022800> state changed: Inactive -> Activating
default	18:43:48.150207+0800	hootowl	starting core haptics engine for <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c022800>
default	18:43:48.150213+0800	hootowl	creating core haptics engine for <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c022800>
default	18:43:48.150243+0800	hootowl	        CHHapticEngine.mm:1532  -[CHHapticEngine initWithAudioSession:sessionIsShared:options:error:]: Creating engine 0x112296e60 with unshared audio session 0x0
default	18:43:48.150495+0800	hootowl	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	18:43:48.150516+0800	hootowl	[0x11be03e80] activating connection: mach=false listener=false peer=false name=com.apple.audio.AudioConverterService.HighCapacity
default	18:43:48.150871+0800	hootowl	[0x11be02a80] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	18:43:48.250159+0800	hootowl	    SessionCore_Create.mm:99    Created session 0x109b509d0 with ID: 0x77c63b0
default	18:43:48.250729+0800	hootowl	[0x11be03e80] Re-initialization successful; calling out to event handler with XPC_ERROR_CONNECTION_INTERRUPTED
default	18:43:48.251696+0800	hootowl	[0x11be03e80] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	18:43:48.251972+0800	hootowl	playing feedback without gesture recognizer (<nil: 0x0>) or at null point
default	18:43:48.252357+0800	hootowl	activate generator with style: TurnOn; activationCount: 2 -> 3; styleActivationCount: 2 -> 3; <_UIDragSnappingFeedbackGenerator: 0x13bc01d40>
default	18:43:48.257118+0800	hootowl	<<<< AVInputDeviceDiscoverySession >>>> -[AVInputDeviceDiscoverySession setFastDiscoveryEnabled:]: called (session=0x11218b6a0, setFastDiscoveryEnabled=NO)
default	18:43:48.258198+0800	hootowl	generator <_UIDragSnappingFeedbackGenerator: 0x13bc01d40> cannot play feedback <nil: 0x0> (enabled=1)
default	18:43:48.259474+0800	hootowl	<<<< AVInputDeviceDiscoverySession (FigRouteDiscoverer) >>>> -[AVFigRouteDiscovererInputDeviceDiscoverySessionImpl inputDeviceDiscoverySessionFastDiscoveryDidChange:]: Setting fastDiscoveryEnabled to NO (client: hootowl) for session=0x11c116730
default	18:43:48.261404+0800	hootowl	<<<< AVOutputDeviceDiscoverySession >>>> -[AVOutputDeviceDiscoverySession setFastDiscoveryEnabled:]: called (session=0x109b50970, setFastDiscoveryEnabled=NO)
default	18:43:48.264828+0800	hootowl	<<<< AVOutputDeviceDiscoverySession (FigRouteDiscoverer) >>>> -[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl outputDeviceDiscoverySessionFastDiscoveryDidChange:]: Setting fastDiscoveryEnabled to NO (client: hootowl) for session=0x109b50970
default	18:43:48.332961+0800	hootowl	    AVAudioSession_iOS.mm:3459  enableNotifications: inValue = 0
default	18:43:48.332994+0800	hootowl	[0x11be01180] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
default	18:43:48.335396+0800	hootowl	[0x11be02800] activating connection: mach=true listener=false peer=false name=com.apple.audio.hapticd
default	18:43:48.450613+0800	hootowl	    HapticServerConfig.mm:40    -[HapticServerConfig initWithHapticPlayer:withOptions:error:]: Querying server for capabilities with 'FullGamut' Locality
default	18:43:48.450639+0800	hootowl	    HapticServerConfig.mm:106   -[HapticServerConfig initWithHapticPlayer:withOptions:error:]: Querying server for UsageCategory of 'UIFeedback'
default	18:43:48.450649+0800	hootowl	        AVHapticPlayer.mm:313   -[AVHapticPlayer queryServerCapabilities:reply:]: clientID: 0x1009084
default	18:43:48.450984+0800	hootowl	App is being debugged, do not track this hang
default	18:43:48.451006+0800	hootowl	Hang detected: 0.30s (debugger attached, not reporting)
default	18:43:48.451359+0800	hootowl	Evaluating dispatch of UIEvent: 0x13bfef800; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	18:43:48.451370+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	18:43:48.451386+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1099f0400>; contextId: 0x6989FC6
default	18:43:48.452250+0800	hootowl	[0x11be01900] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	18:43:48.452263+0800	hootowl	Evaluating dispatch of UIEvent: 0x13bfef800; type: 9; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	18:43:48.452275+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to windows: 1
default	18:43:48.452287+0800	hootowl	Sending UIEvent type: 9; subtype: 0; to window: <UIWindow: 0x1099f0400>; contextId: 0x6989FC6
default	18:43:48.452446+0800	hootowl	_UIDruidDestinationConnection requestDropWithOperation:16
default	18:43:48.452548+0800	hootowl	_UIDruidDestinationConnection sawDragEndEvent
default	18:43:48.452580+0800	hootowl	_UIInternalDraggingSessionDestination: State changing from Dragging to Ending
default	18:43:48.453186+0800	hootowl	        CHHapticEngine.mm:879   -[CHHapticEngine updateEngineBehavior]: Setting player's behavior to 0x0
default	18:43:48.453238+0800	hootowl	        AVHapticPlayer.mm:323   -[AVHapticPlayer setBehavior:error:]: clientID: 0x1009084 behavior: 0
default	18:43:48.453389+0800	hootowl	generator <_UIDragSnappingFeedbackGenerator: 0x13bc01d40> cannot play feedback <nil: 0x0> (enabled=1)
default	18:43:48.453465+0800	hootowl	        CHHapticEngine.mm:879   -[CHHapticEngine updateEngineBehavior]: Setting player's behavior to 0x4
default	18:43:48.453476+0800	hootowl	        AVHapticPlayer.mm:323   -[AVHapticPlayer setBehavior:error:]: clientID: 0x1009084 behavior: 4
default	18:43:48.463293+0800	hootowl	_UIDruidDestinationConnection performDropWithItemCollection:...
default	18:43:48.463315+0800	hootowl	_UIInternalDraggingSessionDestination: State changing from Ending to Dropped
default	18:43:48.463349+0800	hootowl	_UIDruidDestinationConnection performDropWithItemCollection: calling dropPerformBlock
default	18:43:48.463423+0800	hootowl	deactivate generator with style: TurnOn; activationCount: 3 -> 2; styleActivationCount: 3 -> 2; <_UIDragSnappingFeedbackGenerator: 0x13bc01d40>
default	18:43:48.463871+0800	hootowl	        CHHapticEngine.mm:1302  -[CHHapticEngine startWithCompletionHandler:]: Called on engine 0x112296e60
default	18:43:48.463886+0800	hootowl	        CHHapticEngine.mm:1251  -[CHHapticEngine doStartWithCompletionHandler:]: Starting underlying Haptic Player
default	18:43:48.463895+0800	hootowl	        CHHapticEngine.mm:885   -[CHHapticEngine updateEngineBehaviorWithError:]: Setting player's behavior to 0x5
default	18:43:48.464332+0800	hootowl	        AVHapticPlayer.mm:323   -[AVHapticPlayer setBehavior:error:]: clientID: 0x1009084 behavior: 5
default	18:43:48.464521+0800	hootowl	        AVHapticPlayer.mm:675   -[AVHapticPlayer startRunningWithCompletionHandler:]: start running: clientID: 0x1009084
default	18:43:48.464544+0800	hootowl	        AVHapticClient.mm:363   -[AVHapticClient startRunning:]: Client 0x1009084 starting
default	18:43:48.467200+0800	hootowl	Municipal+Cyclops 79
🎨 model refreshed — obs:95s car:21 thread:main
default	18:43:48.479763+0800	hootowl	_UIDruidDestinationConnection performDropWithItemCollection: sending reply to druid
default	18:43:48.480134+0800	hootowl	RX setKeyboardDisabled:N
default	18:43:48.480241+0800	hootowl	setDeactivatedKeyboard: 0 forScene: (null) forSuppressionAssertion: 0
default	18:43:48.480261+0800	hootowl	setDeactivatedKeyboard, shouldUpdatePlacement: 1
default	18:43:48.480273+0800	hootowl	setPlacementChangeDisabled: 0, placement: <UITrackingElementPlacementInitialPosition> (self: <UITrackingElementWindowController: 0x109a30a00>)
default	18:43:48.480323+0800	hootowl	Moving from placement: <UITrackingElementPlacementInitialPosition> to placement: <UITrackingElementPlacementInitialPosition> (currentPlacement: <UITrackingElementPlacementInitialPosition>)
default	18:43:48.480520+0800	hootowl	updatePlacementWithPlacement: <UITrackingElementPlacementInitialPosition>
default	18:43:48.481009+0800	hootowl	Tracking provider: moveFromPlacement: <UITrackingElementPlacementInitialPosition> toPlacement: <UITrackingElementPlacementInitialPosition> update to {{0, 852}, {393, 0}}
default	18:43:48.481046+0800	hootowl	Updating tracking clients for start <TUIKeyboardTrackingCoordinator:0x11be03c00 state=<TUIKeyboardState: 0x11223afe0 State: offscreen; is docked>; frame={{0, 852}, {393, 0}}; animation=<TUIKeyboardAnimationInfo: 0x139e56680, duration: 0.38, from local keyboard, is not rotating, should animate, type: 0, notificationInfo: {
    UIKeyboardAnimationCurveUserInfoKey = 7;
    UIKeyboardAnimationDurationUserInfoKey = "0.3833";
    UIKeyboardBoundsUserInfoKey = "NSRect: {{0, 0}, {393, 0}}";
    UIKeyboardCenterBeginUserInfoKey = "NSPoint: {196.5, 852}";
    UIKeyboardCenterEndUserInfoKey = "NSPoint: {196.5, 852}";
    UIKeyboardFrameBeginUserInfoKey = "NSRect: {{0, 852}, {393, 0}}";
    UIKeyboardFrameEndUserInfoKey = "NSRect: {{0, 852}, {393, 0}}";
    UIKeyboardIsLocalUserInfoKey = 1;
}notificationsDebug: >>
default	18:43:48.481132+0800	hootowl	_UIDruidDestinationConnection handOffDroppedItems:withFence:completion:
default	18:43:48.481540+0800	hootowl	_UIDruidSourceConnection dragEndedWithOperation:16
default	18:43:48.481570+0800	hootowl	_UIDruidDestinationConnection: dragEnded
default	18:43:48.482431+0800	hootowl	_UIInternalDraggingSessionSource: Drag session state changing from Dragging to Dropped
default	18:43:48.482465+0800	hootowl	_UIInternalDraggingSessionDestination: State changing from Dropped to Ended
default	18:43:48.487660+0800	hootowl	core haptics engine STARTED for <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c022800>
default	18:43:48.487723+0800	hootowl	engine <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c022800> state changed: Activating -> Running
default	18:43:48.487756+0800	hootowl	MncplCyclopsScreen 62
🏠 body eval — items:6 firstObs:95s firstCar:21
default	18:43:48.492892+0800	hootowl	Received state update for 36996 (app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>, unknown-NotVisible
default	18:43:48.494761+0800	hootowl	Received state update for 36996 (app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>, unknown-NotVisible
default	18:43:48.498642+0800	hootowl	[(FBSceneManager):sceneID:com.sharkda.hootowl-1B8F959F-618F-4A0D-AD89-E09DEC0EAB34] Sending action(s): BLSInvalidateFrameSpecifiersAction
default	18:43:48.500566+0800	hootowl	cannot migrate AudioUnit assets for current process
default	18:43:48.510749+0800	hootowl	playing feedback without gesture recognizer (<nil: 0x0>) or at null point
default	18:43:48.510785+0800	hootowl	activate generator with style: TurnOn; activationCount: 2 -> 3; styleActivationCount: 2 -> 3; <_UIDragSnappingFeedbackGenerator: 0x13bc01d40>
default	18:43:48.510798+0800	hootowl	deactivate generator with style: TurnOn; activationCount: 3 -> 2; styleActivationCount: 3 -> 2; <_UIDragSnappingFeedbackGenerator: 0x13bc01d40>
default	18:43:48.510806+0800	hootowl	generator <_UIDragSnappingFeedbackGenerator: 0x13bc01d40> playing feedback <_UIDiscreteFeedback: 0x139e31360>
default	18:43:48.510842+0800	hootowl	player dequeue needed - initial request for feedback <_UIDiscreteFeedback: 0x139e31360>
default	18:43:48.510962+0800	hootowl	player dequeue finished for feedback <_UIDiscreteFeedback: 0x139e31360> with player <_UIFeedbackCoreHapticsPlayer: 0x139e7cba0>
default	18:43:48.510976+0800	hootowl	generator <_UIDragSnappingFeedbackGenerator: 0x13bc01d40> playing feedback <_UIDiscreteFeedback: 0x139e31180>
default	18:43:48.511616+0800	hootowl	deactivate generator with style: TurnOn; activationCount: 2 -> 1; styleActivationCount: 2 -> 1; <_UIDragSnappingFeedbackGenerator: 0x13bc01d40>
default	18:43:48.511667+0800	hootowl	deactivate generator with style: TurnOn; activationCount: 1 -> 0; styleActivationCount: 1 -> 0; <_UIDragSnappingFeedbackGenerator: 0x13bc01d40>
default	18:43:48.512063+0800	hootowl	        AVHapticPlayer.mm:150   -[AVHapticPlayerChannel resetAtTime:error:]: sending reset event: clientID: 0x1009084 time: 640480.628
default	18:43:48.512079+0800	hootowl	        AVHapticPlayer.mm:91    -[AVHapticPlayerChannel sendEvents:atTime:error:]: sending event array: clientID: 0x1009084 atTime: 640480.628
default	18:43:48.512170+0800	hootowl	        AVHapticPlayer.mm:762   -[AVHapticPlayer finishWithCompletionHandler:]: finish with comp handler: clientID: 0x1009084
default	18:43:48.512180+0800	hootowl	        AVHapticClient.mm:421   -[AVHapticClient finish:]: Client 0x1009084 finishing
default	18:43:48.512187+0800	hootowl	        AVHapticClient.mm:426   -[AVHapticClient finish:]_block_invoke: completionCallback set to 0x10cdfba50
default	18:43:48.512195+0800	hootowl	        AVHapticClient.mm:453   -[AVHapticClient finish:]: Client 0x1009084 done with finish
default	18:43:48.512202+0800	hootowl	player dequeue needed - initial request for feedback <_UIDiscreteFeedback: 0x139e31180>
default	18:43:48.512227+0800	hootowl	played feedback <_UIDiscreteFeedback: 0x139e31360> with engine <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c022800> at time 640480.627838
default	18:43:48.512267+0800	hootowl	player dequeue finished for feedback <_UIDiscreteFeedback: 0x139e31180> with player <_UIFeedbackCoreHapticsPlayer: 0x139e7ce40>
default	18:43:48.512789+0800	hootowl	        AVHapticPlayer.mm:150   -[AVHapticPlayerChannel resetAtTime:error:]: sending reset event: clientID: 0x1009084 time: 640480.628
default	18:43:48.512798+0800	hootowl	        AVHapticPlayer.mm:91    -[AVHapticPlayerChannel sendEvents:atTime:error:]: sending event array: clientID: 0x1009084 atTime: 640480.628
default	18:43:48.512804+0800	hootowl	        AVHapticPlayer.mm:762   -[AVHapticPlayer finishWithCompletionHandler:]: finish with comp handler: clientID: 0x1009084
default	18:43:48.512810+0800	hootowl	        AVHapticClient.mm:421   -[AVHapticClient finish:]: Client 0x1009084 finishing
default	18:43:48.512818+0800	hootowl	        AVHapticClient.mm:426   -[AVHapticClient finish:]_block_invoke: completionCallback set to 0x10cdf8300
default	18:43:48.512824+0800	hootowl	        AVHapticClient.mm:453   -[AVHapticClient finish:]: Client 0x1009084 done with finish
default	18:43:48.512835+0800	hootowl	deactivate engine <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c022800>, clientCount: 1 -> 0
default	18:43:48.512844+0800	hootowl	played feedback <_UIDiscreteFeedback: 0x139e31180> with engine <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c022800> at time 640480.627972
default	18:43:48.512857+0800	hootowl	_internal_deactivateEngineIfPossible <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c022800>, clientCount: 0, suspended: 0
default	18:43:48.512866+0800	hootowl	_internal_teardownUnderlyingPlayerIfPossible <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c022800>
default	18:43:48.512876+0800	hootowl	engine <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c022800> state changed: Running -> Deactivating
default	18:43:48.512885+0800	hootowl	        CHHapticEngine.mm:1461  -[CHHapticEngine notifyWhenPlayersFinished:]: Called on engine 0x112296e60 with finishedHandler 0x1121fb640
default	18:43:48.512893+0800	hootowl	        AVHapticPlayer.mm:762   -[AVHapticPlayer finishWithCompletionHandler:]: finish with comp handler: clientID: 0x1009084
default	18:43:48.512901+0800	hootowl	        AVHapticClient.mm:421   -[AVHapticClient finish:]: Client 0x1009084 finishing
default	18:43:48.512907+0800	hootowl	        AVHapticClient.mm:426   -[AVHapticClient finish:]_block_invoke: completionCallback set to 0x10cdfa7f0
default	18:43:48.512974+0800	hootowl	        AVHapticClient.mm:453   -[AVHapticClient finish:]: Client 0x1009084 done with finish
default	18:43:48.545173+0800	hootowl	        AVHapticClient.mm:1472  -[AVHapticClient clientCompletedWithError:]: Client-side (async) finish completion callback for client 0x1009084 called from server
default	18:43:48.545269+0800	hootowl	        AVHapticClient.mm:1477  -[AVHapticClient clientCompletedWithError:]_block_invoke: Async dispatch: preparing to call completionCallback for client 0x1009084
default	18:43:48.545289+0800	hootowl	        AVHapticClient.mm:1479  -[AVHapticClient clientCompletedWithError:]_block_invoke: Calling completionCallback 0x10cdfa7f0 and then setting to nil
default	18:43:48.546432+0800	hootowl	core haptics engine finished for <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c022800>
default	18:43:48.546441+0800	hootowl	stopping core haptics engine for <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c022800>
default	18:43:48.546457+0800	hootowl	        CHHapticEngine.mm:1439  -[CHHapticEngine stopWithCompletionHandler:]: Called on engine 0x112296e60
default	18:43:48.546468+0800	hootowl	        CHHapticEngine.mm:1403  -[CHHapticEngine doStopWithCompletionHandler:]: Stopping underlying Haptic Player
default	18:43:48.546474+0800	hootowl	_internal_deactivateEngineIfPossible <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c022800> tearedDown: 1
default	18:43:48.546482+0800	hootowl	        AVHapticPlayer.mm:739   -[AVHapticPlayer stopRunningWithCompletionHandler:]: stop running: clientID: 0x1009084
default	18:43:48.546525+0800	hootowl	engine <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c022800> state changed: Deactivating -> Inactive
default	18:43:48.546586+0800	hootowl	        AVHapticClient.mm:398   -[AVHapticClient stopRunning:]: Client 0x1009084 stopping
default	18:43:48.550631+0800	hootowl	        AVHapticClient.mm:1472  -[AVHapticClient clientCompletedWithError:]: Client-side (async) finish completion callback for client 0x1009084 called from server
default	18:43:48.550657+0800	hootowl	        AVHapticClient.mm:1477  -[AVHapticClient clientCompletedWithError:]_block_invoke: Async dispatch: preparing to call completionCallback for client 0x1009084
default	18:43:48.550719+0800	hootowl	        AVHapticClient.mm:1484  -[AVHapticClient clientCompletedWithError:]_block_invoke: strongSelf.completionCallback is nil
default	18:43:48.559856+0800	hootowl	core haptics engine STOPPED for <_UIFeedbackCoreHapticsHapticsOnlyEngine: 0x11c022800>
default	18:43:48.584108+0800	hootowl	Received state update for 36996 (app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>, unknown-NotVisible
default	18:43:49.381958+0800	hootowl	TX focusApplication (peekAppEvent) stealKB:Y scene:com.sharkda.hootowl-1B8F959F-618F-4A0D-AD89-E09DEC0EAB34
default	18:43:49.382028+0800	hootowl	Evaluating dispatch of UIEvent: 0x11cfa2200; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	18:43:49.382098+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	18:43:49.382575+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1099f0400>; contextId: 0x6989FC6
default	18:43:49.420331+0800	hootowl	Evaluating dispatch of UIEvent: 0x11cfa2200; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	18:43:49.432884+0800	hootowl	Evaluating dispatch of UIEvent: 0x11cfa2200; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	18:43:49.432972+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	18:43:49.433307+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1099f0400>; contextId: 0x6989FC6
default	18:43:49.449290+0800	hootowl	Evaluating dispatch of UIEvent: 0x11cfa2200; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	18:43:49.449306+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	18:43:49.449326+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1099f0400>; contextId: 0x6989FC6
default	18:43:49.450612+0800	hootowl	Evaluating dispatch of UIEvent: 0x11cfa2200; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 1
default	18:43:49.450756+0800	hootowl	Evaluating dispatch of UIEvent: 0x11cfa2200; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	18:43:49.450782+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	18:43:49.450831+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1099f0400>; contextId: 0x6989FC6
default	18:43:49.465930+0800	hootowl	Evaluating dispatch of UIEvent: 0x11cfa2200; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	18:43:49.465975+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	18:43:49.466008+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1099f0400>; contextId: 0x6989FC6
default	18:43:49.468811+0800	hootowl	<UIWindowScene: 0x10cc50200> (1B8F959F-618F-4A0D-AD89-E09DEC0EAB34) Scene updated orientation preferences: ( Pu Ll Lr ) -> ( Pu )
default	18:43:49.470637+0800	hootowl	endInputSession completion is disabled
default	18:43:49.470751+0800	hootowl	Evaluating dispatch of UIEvent: 0x11cfa2200; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	18:43:49.470771+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	18:43:49.470782+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1099f0400>; contextId: 0x6989FC6
default	18:43:49.520147+0800	hootowl	<UIWindowScene: 0x10cc50200> (1B8F959F-618F-4A0D-AD89-E09DEC0EAB34) Scene updated orientation preferences: ( Pu ) -> ( Pu Ll Lr )
default	18:43:49.704854+0800	hootowl	Data transfer finished for dragging session destination 0x11bdcbe80
default	18:43:49.718679+0800	hootowl	Data transfer began for dragging session destination 0x11bdcbe80
default	18:43:49.719325+0800	hootowl	[0x1121e1a40] Re-initialization successful; calling out to event handler with XPC_ERROR_CONNECTION_INTERRUPTED
default	18:43:49.719403+0800	hootowl	[0x1121e1a40] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	18:43:49.719630+0800	hootowl	_UIDruidSourceConnection connection invalidated
default	18:43:49.719731+0800	hootowl	[0x11bdca580] Re-initialization successful; calling out to event handler with XPC_ERROR_CONNECTION_INTERRUPTED
default	18:43:49.719892+0800	hootowl	[0x11bdca580] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	18:43:49.720092+0800	hootowl	_UIDruidDestinationConnection connection invalidated
default	18:43:49.720150+0800	hootowl	[0x1120e7c00] invalidated because the client process (pid 36148) either cancelled the connection or exited
default	18:43:49.720329+0800	hootowl	[0x1121e2080] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	18:43:49.821535+0800	hootowl	Received state update for 36996 (app<com.sharkda.hootowl(EEC5E5EC-DCD2-474B-874E-6D44AC91A591)>, unknown-NotVisible
default	18:43:50.498038+0800	hootowl	TX focusApplication (peekAppEvent) stealKB:Y scene:com.sharkda.hootowl-1B8F959F-618F-4A0D-AD89-E09DEC0EAB34
default	18:43:50.498146+0800	hootowl	Evaluating dispatch of UIEvent: 0x11cfa2200; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	18:43:50.498163+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	18:43:50.498197+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1099f0400>; contextId: 0x6989FC6
default	18:43:50.499272+0800	hootowl	Evaluating dispatch of UIEvent: 0x11cfa2200; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	18:43:50.549508+0800	hootowl	Evaluating dispatch of UIEvent: 0x11cfa2200; type: 0; subtype: 0; backing type: 11; shouldSend: 1; ignoreInteractionEvents: 0, systemGestureStateChange: 0
default	18:43:50.549541+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to windows: 1
default	18:43:50.549556+0800	hootowl	Sending UIEvent type: 0; subtype: 0; to window: <UIWindow: 0x1099f0400>; contextId: 0x6989FC6
default	18:43:50.551266+0800	hootowl	Evaluating dispatch of UIEvent: 0x11cfa2200; type: 0; subtype: 0; backing type: 11; shouldSend: 0; ignoreInteractionEvents: 0, systemGestureStateChange: 1
default	18:43:50.570530+0800	hootowl	<UIWindowScene: 0x10cc50200> (1B8F959F-618F-4A0D-AD89-E09DEC0EAB34) Scene updated orientation preferences: ( Pu Ll Lr ) -> ( Pu )
default	18:43:51.126277+0800	hootowl	<UIWindowScene: 0x10cc50200> (1B8F959F-618F-4A0D-AD89-E09DEC0EAB34) Scene updated orientation preferences: ( Pu ) -> ( Pu Ll Lr )

```