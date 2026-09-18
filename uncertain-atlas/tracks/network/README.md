# 横向：点对点网络

课：L9.1、L3.4。  
精读：[`worked-example-eclipse.md`](worked-example-eclipse.md)（六个邻居都是对手）；[`worked-example-adjusted-time.md`](worked-example-adjusted-time.md)（调整钟拒收真块 ≠ 日蚀 / 分区）。  
库存三方向：[`worked-example-inventory-quotas.md`](worked-example-inventory-quotas.md)（入站 INV ≠ 入站 GETDATA ≠ 出站待宣布）。  
最大消息 ≠ 接收分配：[`../failure-museum/cve-2015-3641.md`](../failure-museum/cve-2015-3641.md)。  
地址表递增 ID：[`../failure-museum/cve-2024-52919.md`](../failure-museum/cve-2024-52919.md)（限速 ≠ 宽度）。  
无界封禁表：[`../failure-museum/cve-2020-14198.md`](../failure-museum/cve-2020-14198.md)（自动 ban ≠ 有界）。  
局域网打洞辅助 ≠ P2P：[`../failure-museum/cve-2015-20111.md`](../failure-museum/cve-2015-20111.md)（默认关 UPnP 是结构风险决策）。  
出站代理 ≠ 对等节点：[`../failure-museum/cve-2017-18350.md`](../failure-museum/cve-2017-18350.md)（须先配置；明文网上的任意代理本身就可被截获）。  
宣布新块 ≠ 已收到：[`../failure-museum/cve-2024-52922.md`](../failure-museum/cve-2024-52922.md)。  
拼块 ≠ 共识验块：[`worked-example-compact-block.md`](worked-example-compact-block.md)（52922 / 35202 / 52921）。  
分片外层下标 ≠ 证明下标：[`../failure-museum/asa-2025-002.md`](../failure-museum/asa-2025-002.md)（验根通过不是第 i 片已对齐）。  
结构必须先验再传：[`../failure-museum/asa-2025-003.md`](../failure-museum/asa-2025-003.md)（非法 BitArray 先流言会停网）。  
blocksync 目标必须可归因：[`../failure-museum/asa-2025-001.md`](../failure-museum/asa-2025-001.md)（邻居 latest ≠ 全网尖）。  
握手请求 ≠ 已接受邻居：[`../failure-museum/cve-2020-5303.md`](../failure-museum/cve-2020-5303.md)（入站上限不是握手配额；ID 必须先认领、全路径归还）。  
对等历史窗 ≠ 已改共识：[`worked-example-history-window-vs-consensus.md`](worked-example-history-window-vs-consensus.md)（看见对等节点宣布历史窗不是已经删历史；线上无布隆不是已经改共识收据；7642 ≠ 23 ≠ 25 ≠ 195）。  
忽略版本 ≠ 已经在说新协议：[`worked-example-eip8-vs-already-new.md`](worked-example-eip8-vs-already-new.md)（看见能吞多余字段不是已经谈成新线协议；跟 Homestead 一起上不是已经改共识；仍收旧握手不是已经退役旧格式；8 ≠ 2 ≠ 7642）。
分叉标识 ≠ 已经同一条链：[`worked-example-forkid-vs-same-chain.md`](worked-example-forkid-vs-same-chain.md)（看见分叉标识对上不是已经同一条链；通告了下一分叉不是已经兼容；2124 ≠ 8 ≠ 7642 ≠ 7910）。
签过的节点记录 ≠ 已经最新：[`worked-example-enr-vs-newest.md`](worked-example-enr-vs-newest.md)（看见签过的记录不是已经是最新一份；能多写键不是已经换了身份方案；778 ≠ 2124 ≠ 8 ≠ 7642）。
ping 序号 ≠ 已经有当前记录：[`worked-example-enr-request-vs-have.md`](worked-example-enr-request-vs-have.md)（看见 ping 里的记录序号不是已经有当前记录；能发请求不是已经解析；FindNode 找到人不是已经有记录；868 ≠ 778 ≠ 2124 ≠ 8）。
第 2 版传输 ≠ 已经私人：[`worked-example-v2-transport-vs-private.md`](worked-example-v2-transport-vs-private.md)（看见机会主义未认证加密不是已经私人；伪随机字节流不是已经认不出；仍收下第 1 版不是已经退役旧线；324 ≠ 112 ≠ 8 ≠ 868）。
后继地址流言 ≠ 已经连得上：[`worked-example-addr155-notreach-vs-bundled.md`](worked-example-addr155-notreach-vs-bundled.md)（流言≠already connected/reachable/old-retired；≠246 bundled；不变量 1232）。
sendaddrv2 ≠ 已经只收后继格式：[`worked-example-addr155-notpref-vs-bundled.md`](worked-example-addr155-notpref-vs-bundled.md)（信号≠already only-v2/old-retired/unsolicited-pref；≠246 bundled；不变量 1233）。
传了某种网 ≠ 已经连上那种网：[`worked-example-addr155-notnet-vs-bundled.md`](worked-example-addr155-notnet-vs-bundled.md)（传网≠already connected-to-net/two-peers/hidden-service；≠246 bundled；不变量 1234）。
后继地址 ≠ 已经连得上：[`worked-example-addrv2-vs-reachable.md`](worked-example-addrv2-vs-reachable.md)（看见后继地址流言不是已经连得上；发了 sendaddrv2 不是已经只收后继格式；在传某种网上的地址不是已经连上那种网；155 ≠ 324 ≠ 112 ≠ 868）。
sendheaders ≠ 已经改用头通告：[`worked-example-hdr130-notswitch-vs-bundled.md`](worked-example-hdr130-notswitch-vs-bundled.md)（信号≠already switched/have-block/headers-first；≠247 bundled；不变量 1235）。
许可 ≠ 已经照做：[`worked-example-hdr130-notmust-vs-bundled.md`](worked-example-hdr130-notmust-vs-bundled.md)（许可≠already must/sending/forever；≠247 bundled；不变量 1236）。
头通告新尖 ≠ 已经有块：[`worked-example-hdr130-nothave-vs-bundled.md`](worked-example-hdr130-nothave-vs-bundled.md)（先发头≠already have-block/have-middle/reorg-done；≠247 bundled；不变量 1237）。
头通告偏好 ≠ 已经有块：[`worked-example-sendheaders-vs-have.md`](worked-example-sendheaders-vs-have.md)（看见发了 sendheaders 不是已经改用头通告；用头通告新尖不是已经有块；重组时先发头不是中间块已经在手里；130 ≠ 36 ≠ 155 ≠ compact）。
按 wtxid 通告 ≠ 已经有那笔交易：[`worked-example-wtx339-nothave-vs-bundled.md`](worked-example-wtx339-nothave-vs-bundled.md)（通告≠already have/accepted/never-again；≠248 bundled；不变量 1247）。
发了 wtxidrelay ≠ 已经改口：[`worked-example-wtx339-notswitch-vs-bundled.md`](worked-example-wtx339-notswitch-vs-bundled.md)（信号≠already switched/negotiated/using；≠248 bundled；不变量 1248）。
仍用旧类型要父交易 ≠ 旧库存已经退役：[`worked-example-wtx339-notold-vs-bundled.md`](worked-example-wtx339-notold-vs-bundled.md)（旧索取≠already retired/have-wit/net-wide；≠248 bundled；不变量 1249）。
按 wtxid 通告 ≠ 已经有交易：[`worked-example-wtxidrelay-vs-have.md`](worked-example-wtxidrelay-vs-have.md)（看见按 wtxid 通告不是已经有那笔交易；发了 wtxidrelay 不是已经改口；仍用旧类型要父交易不是旧库存已经退役；339 ≠ 152 ≠ 130 ≠ 133）。
一次对账 ≠ 已经有那些交易：[`worked-example-erl330-nothave-vs-bundled.md`](worked-example-erl330-nothave-vs-bundled.md)（对账≠already have/flood-retired/net-wide；≠249 bundled；不变量 1250）。
发了 sendtxrcncl ≠ 已经在对账：[`worked-example-erl330-notsig-vs-bundled.md`](worked-example-erl330-notsig-vs-bundled.md)（信号≠already reconciling/opened/aligned；≠249 bundled；不变量 1251）。
对账失败退回洪水 ≠ 库存通告已经退役：[`worked-example-erl330-notflood-vs-bundled.md`](worked-example-erl330-notflood-vs-bundled.md)（失败≠already retired/have/wtxid；≠249 bundled；不变量 1252）。
对账素描 ≠ 已经有交易：[`worked-example-erlay-vs-have.md`](worked-example-erlay-vs-have.md)（看见对账素描不是已经有那些交易；发了 sendtxrcncl 不是已经在对账；对账失败退回洪水不是库存通告已经退役；330 ≠ 339 ≠ 133 ≠ 36）。
有限服务位 ≠ 已经能服任意旧块：[`worked-example-lim159-notarch-vs-bundled.md`](worked-example-lim159-notarch-vs-bundled.md)（有限位≠already any-old/genesis-body/archive；≠250 bundled；不变量 1253）。
有限服务位 ≠ 已经剪枝：[`worked-example-lim159-notprune-vs-bundled.md`](worked-example-lim159-notprune-vs-bundled.md)（有限位≠already pruned/same-service/unusable；≠250 bundled；不变量 1254）。
服了最近一块 ≠ 已经暴露了剪到哪：[`worked-example-lim159-notcut-vs-bundled.md`](worked-example-lim159-notcut-vs-bundled.md)（最近一块≠already leaked/ibd-done/light-checked；≠250 bundled；不变量 1255）。
有限服务位 ≠ 已经是归档：[`worked-example-limited-service-vs-archive.md`](worked-example-limited-service-vs-archive.md)（看见有限服务位不是已经能服任意旧块；只保证最近窗口不是已经剪枝；服了最近一块不是已经暴露剪点；159 ≠ 207 ≠ 243 ≠ 25）。
带见证的线上序列化 ≠ 已经有见证：[`worked-example-wit144-nothave-vs-bundled.md`](worked-example-wit144-nothave-vs-bundled.md)（序列化≠already have/accepted/no-capability；≠251 bundled；不变量 1256）。
开了能提供见证那一位 ≠ 已经在传：[`worked-example-wit144-notsend-vs-bundled.md`](worked-example-wit144-notsend-vs-bundled.md)（服务位≠already sending/have/old-retired；≠251 bundled；不变量 1257）。
库存通告仍用旧类型 ≠ 线上已经没有见证：[`worked-example-wit144-notold-vs-bundled.md`](worked-example-wit144-notold-vs-bundled.md)（旧通告≠already no-wit/wtxid-ann/verified；≠251 bundled；不变量 1258）。
带见证的线上序列化 ≠ 已经有见证：[`worked-example-witness-wire-vs-have.md`](worked-example-witness-wire-vs-have.md)（看见带见证的线上序列化不是已经有见证；能提供见证不是已经在传；库存通告仍用旧类型不是线上已经没有见证；144 ≠ 141 ≠ 339 ≠ 130）。
拒收 ≠ 已经共识非法：[`worked-example-rej61-notill-vs-bundled.md`](worked-example-rej61-notill-vs-bundled.md)（拒收≠already illegal/net-wide/best-chain；≠254 bundled；不变量 1265）。
一条拒收理由 ≠ 已经该弹给用户：[`worked-example-rej61-notuser-vs-bundled.md`](worked-example-rej61-notuser-vs-bundled.md)（理由≠already official/consensus/for-users；≠254 bundled；不变量 1266）。
策略拒收 ≠ 已经共识非法：[`worked-example-rej61-notpol-vs-bundled.md`](worked-example-rej61-notpol-vs-bundled.md)（策略码≠already illegal/net-illegal/notify；≠254 bundled；不变量 1267）。
拒收消息 ≠ 已经共识非法：[`worked-example-reject-vs-consensus.md`](worked-example-reject-vs-consensus.md)（看见拒收消息不是已经共识非法；调试理由不是已经该给用户看；没拒收不是已经是当前最好链；61 ≠ 144 ≠ 133 ≠ 35）。
版本关掉转发 ≠ 已经终身只传块：[`worked-example-dis338-notlife-vs-bundled.md`](worked-example-dis338-notlife-vs-bundled.md)（版本字段≠already lifetime/implemented/default-on；≠256 bundled；不变量 1241）。
停交易 ≠ 已经没有紧凑块：[`worked-example-dis338-notcmpct-vs-bundled.md`](worked-example-dis338-notcmpct-vs-bundled.md)（停交易≠already no-compact/tx-illegal/no-block；≠256 bundled；不变量 1242）。
建议关掉地址 ≠ 已经禁止：[`worked-example-dis338-notaddr-vs-bundled.md`](worked-example-dis338-notaddr-vs-bundled.md)（建议≠already forbidden/disconnected/illegal；≠256 bundled；不变量 1243）。
停交易转发 ≠ 已经终身只传块：[`worked-example-disabletx-vs-lifetime.md`](worked-example-disabletx-vs-lifetime.md)（看见版本里关掉转发不是已经终身只传块；发了停交易转发不是已经没有紧凑块；建议关掉地址不是已经禁止；338 ≠ 133 ≠ 35 ≠ 152）。
协议版本够了 ≠ 已经支持某项功能：[`worked-example-feat434-notver-vs-bundled.md`](worked-example-feat434-notver-vs-bundled.md)（版本≠already support/sent-page/merged-old；≠259 bundled；不变量 1244）。
通告了 feature ≠ 已经启用：[`worked-example-feat434-noton-vs-bundled.md`](worked-example-feat434-noton-vs-bundled.md)（通告≠already enabled/understood/illegal；≠259 bundled；不变量 1245）。
verack 之后才来的 feature ≠ 已经是本页协商：[`worked-example-feat434-notlate-vs-bundled.md`](worked-example-feat434-notlate-vs-bundled.md)（晚到≠already this-handshake/enabled/implemented；≠259 bundled；不变量 1246）。
协议版本够了 ≠ 已经支持某项功能：[`worked-example-feature-vs-enabled.md`](worked-example-feature-vs-enabled.md)（看见通告了 feature 不是已经启用；verack 之后才来的 feature 不是已经是本页协商；434 ≠ 339 ≠ 155 ≠ 338）。
协议版本够了 ≠ 已经会带 nonce 的 ping：[`worked-example-pong31-notver-vs-bundled.md`](worked-example-pong31-notver-vs-bundled.md)（版本≠already nonce-ping/will-pong/merged-feature；≠262 bundled；不变量 1268）。
一条 pong ≠ 已经对上那一次 ping：[`worked-example-pong31-notmatch-vs-bundled.md`](worked-example-pong31-notmatch-vs-bundled.md)（pong≠already matched/this-ping/rtt；≠262 bundled；不变量 1269）。
回了 pong ≠ 已经还活着：[`worked-example-pong31-notlive-vs-bundled.md`](worked-example-pong31-notlive-vs-bundled.md)（回了≠already alive/unstuck/forever；≠262 bundled；不变量 1270）。
看见 pong ≠ 已经还活着：[`worked-example-pong-vs-live.md`](worked-example-pong-vs-live.md)（协议版本够了不是已经会回 pong；回显 nonce 不是已经对上那一次；31 ≠ 434 ≠ 868）。
协议版本 ≠ 已经是客户端版本：[`worked-example-ua-vs-protocol.md`](worked-example-ua-vs-protocol.md)（user agent 不是已经可以按实现改行为；同一协议版本不是已经是同一套实现；14 ≠ 434 ≠ 31）。
InitPeer ≠ 已经能交互：[`worked-example-initpeer-nothot-vs-bundled.md`](worked-example-initpeer-nothot-vs-bundled.md)（跑着≠already hot-add/another-name/restart；≠305 bundled；不变量 1003）。[`worked-example-initpeer-notadd-vs-bundled.md`](worked-example-initpeer-notadd-vs-bundled.md)（Receive≠already AddPeer/joined/forbidden-early；≠305 bundled；不变量 1002）。[`worked-example-initpeer-nottalk-vs-bundled.md`](worked-example-initpeer-nottalk-vs-bundled.md)（InitPeer≠already talking/connected/added；≠305 bundled；不变量 1001）。[`worked-example-initpeer-vs-addpeer.md`](worked-example-initpeer-vs-addpeer.md)（看见 InitPeer 不是已经能跟它对说；看见已经在 Receive 不是已经过了 AddPeer；看见节点已经在跑不是已经能再登记一个反应堆；305 ≠ 67 ≠ 36）。
Peer 句柄 ≠ 已经是那个人：[`worked-example-peerhand-notgone-vs-bundled.md`](worked-example-peerhand-notgone-vs-bundled.md)（踢≠already gone/forgotten/clean；≠306 bundled；不变量 1006）。[`worked-example-peerhand-notsent-vs-bundled.md`](worked-example-peerhand-notsent-vs-bundled.md)（Broadcast≠already delivered/named/current；≠306 bundled；不变量 1005）。[`worked-example-peerhand-notsame-vs-bundled.md`](worked-example-peerhand-notsame-vs-bundled.md)（句柄≠already same-person/same-handle/new-id；≠306 bundled；不变量 1004）。[`worked-example-peer-handler-vs-node.md`](worked-example-peer-handler-vs-node.md)（看见 Peer 句柄不是已经是那个人；看见 Broadcast 回了通道不是已经送到每一家；看见 StopPeerForError 不是已经对持久邻居也断干净；306 ≠ 305 ≠ 36 ≠ 67）。
NumPeers ≠ 已经数完：[`worked-example-numpeers-notheight-vs-bundled.md`](worked-example-numpeers-notheight-vs-bundled.md)（PeerState≠already verified/evidence-ready/spec-height；≠308 bundled；不变量 1009）。[`worked-example-numpeers-notindep-vs-bundled.md`](worked-example-numpeers-notindep-vs-bundled.md)（按名拿到≠already independent/recommended/current；≠308 bundled；不变量 1008）。[`worked-example-numpeers-notall-vs-bundled.md`](worked-example-numpeers-notall-vs-bundled.md)（NumPeers≠already all-neighbors/unconditional/dialing-ok；≠308 bundled；不变量 1007）。[`worked-example-numpeers-vs-all.md`](worked-example-numpeers-vs-all.md)（看见 NumPeers 不是已经数完所有邻居；看见能按名字拿到反应堆不是已经独立；看见 PeerState 不是已经验过高度；308 ≠ 306 ≠ 305 ≠ 67）。
HasChannel ≠ 已经入队：[`worked-example-sendq-notsame-vs-bundled.md`](worked-example-sendq-notsame-vs-bundled.md)（TrySend≠already stopped/same-scale/delivered；≠309 bundled；不变量 1012）。[`worked-example-sendq-notdisc-vs-bundled.md`](worked-example-sendq-notdisc-vs-bundled.md)（Send回假≠already disconnected/known-reason/delivered；≠309 bundled；不变量 1011）。[`worked-example-sendq-notqueued-vs-bundled.md`](worked-example-sendq-notqueued-vs-bundled.md)（HasChannel≠already queued/delivered/sent；≠309 bundled；不变量 1010）。[`worked-example-send-vs-enqueued.md`](worked-example-send-vs-enqueued.md)（看见 HasChannel 为真不是已经入队；看见 Send 回了假不是已经断开；看见 TrySend 回了假不是已经和 Send 同一把尺；309 ≠ 306 ≠ 308 ≠ 67）。
