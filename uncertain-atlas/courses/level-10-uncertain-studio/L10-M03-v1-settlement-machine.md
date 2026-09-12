# L10.3 第一版最小结算机

优先级：重要  
先修：L10.1，GOAL「不确定」主线

---

## A. 先修知识

建议（不是事实）：第一版像可验证结算机，不像世界计算机。  
本课把「像」写成包含/排除清单，仍允许以后推翻——但推翻必须走 L10.1 记录。

---

## B. 核心问题

**最小可上实验网的结算机，必须有什么？什么永远不要发明？什么以后再发明？**

---

## C. 直觉（ELI15）

先做能被复算的柜台：收一张签字条，按短规则改余额，全员同一本。  
不要先做游乐园、不要先做隐形斗篷、不要先做高速公路。

---

## D. 正式定义

**第一版应包含（建议）**

1. 明确的 `Apply(S, T) → S'`，确定性禁令。  
2. 一种最终性，且产品文案只使用这一种。  
3. 应用/共识分离（或同等清晰的边界）。  
4. 状态根 / 应用哈希。  
5. 崩溃原子高度。  
6. 验签配额与规范编码。  
7. 升级能加算法标识，不能静默改供给。  
8. 第二实现的位置（哪怕先是参考解释器）。  
9. 默认可跑的全节点验证路径。  
10. L9.7 那六条最小测试。  
11. 状态字段白名单；若允许任意 `data`，先有占用不等式（L2.6）。  
12. 用户签与投票签分域，即使第一版算法相同。  
13. 若用 FIPS 204/205：每角色一个非空、互不相同的 `ctx`（或一把钥只服务一个角色）；共识只走外部 API（不变量 18）。  
14. Prevote 与 Precommit（或 attestation 与 proposer）必须是两封被签字节；同一块哈希再签一次不得在另一步 Verify 为真（不变量 19）。  
15. 默认结算角色 = 全节点。若提供 BFT 轻客户端：跳过必须重叠旧 `NextValidators`，信任期必须短于解绑期（不变量 20）；不得把新委员会自己的 2/3 写成「已验证」。  
16. 双签与轻客户端攻击必须能写成可验证据；引擎提交 `Misbehavior`，应用写罚没。证据上链 ≠ 已 slash（不变量 21）。  
17. 若提供「同步委员会」式轻客户端：必须写出抽样大小、任期、签名域；抽样的 2/3 不得写成全验证者集合的 2/3（不变量 22）。第一版默认不要抄 Altair 轻客户端。  
18. 再声明同一份抵押（restake / AVS）与原生验证者质押、与「BTC UTXO 仍在比特币」不是同一对象；AVS 自定、非客观可归属的罚没不得写成协议罚没。  
19. 若提供短时 DA / blob：必须写出服务窗（epoch）、EVM 看见的是 hash 还是字节、可用性是「下 sidecar」还是「抽列/抽份额」。KZG 承诺不得写成 Celestia 式 DAS；过窗的 hash 不得写成永存档案（不变量 23）。第一版不要抄配对 KZG 当默认 DA。  
20. 若提供检查点同步或长期离线后再跟上：检查点必须在路径上且未过弱主观 / 信任期（不变量 24）。过期检查点不得写成「和从创世复算同一安全」。检查点从哪来写进部署假设。  
21. 若提供 IBD 加速：必须写出跳过的是脚本、UTXO 重放还是别的；是否强迫某块在链上；如何关闭（如 `-assumevalid=0`）；快照是否还有背景全验（不变量 25）。不要把 assumevalid / assumeutxo / 弱主观 / 旧 checkpoint 写成一个开关。  
22. 验证者票的可罚关系必须写成客观谓词（同高同轮同步不同类型值，或 Casper double / 顺序固定的 surround，或同 slot 双头）。必须写清谁执行 slash：信标状态还是 ABCI 应用（不变量 21、26）。不要默认抄 surround；不要把任意两张签或同步委员会聚合写成同一刀。  
23. 必须写出谁写交易顺序。若拆「排序」与「签头」：必须写提议者签的是全载荷还是 header、列表何时揭示、揭示失败时谁被信任（不变量 27）。不要抄域外 Builder API 当 v1；不要写「PBS 解决了 MEV」。  
24. 若用有效性证明更新根：必须写出结算合约锁住的 program / circuit hash，以及租户「已收」与房东「已更新」是两个对象（不变量 28）。改哈希是升级。不要抄有效性 rollup 当 v1；不要把 L2 accepted 写成可提款。  
25. 若块时间检查掺入对等偏移：必须写出上限，且算术测得到（不变量 29）。节点拒块必须能点名是钟还是共识。  
26. 未确认对象的索取必须能在超时后换对等节点（不变量 30）。本节点看不见不得写成链拒绝。  
27. 头或其它廉价证书进永久索引之前必须先过工作量或显式配额（不变量 31）。不要把旧检查点三份工作糊成一个开关。  
28. 未确认依赖/孤儿解析必须可中断，验证代价必须有配额（不变量 32）。不要把「节点忙」写成链在重组。  
29. 若抄 ABCI 分离：必须分开 `CheckTx`（池）、`PrepareProposal`（可改列表）、`ProcessProposal`（不可改；REJECT = prevote nil）、`FinalizeBlock`+`Commit`（才改提交状态）（不变量 33）。Process 默认 Accept。不要把 CheckTx 写成已进块，不要把 Prepare 写成 PBS。  
30. 若启用 vote extension：必须写出扩展是另一份签、Verify REJECT 丢掉整张 precommit、`s_h` 不得依赖本高度收到的扩展（不变量 34）。Verify 默认 Accept。第一版可以不启用。不要把扩展写成块非法或本块 Apply 输入。  
31. 验证者集合更新必须写出哪一高度改哪一个哈希、哪一次计票（不变量 8、35）。不要把 H 的 `validator_updates` 写成 H+1 立刻投票；不要和共识参数更新（H→H+1）糊成一拍。  
32. 新块（或等价大证书）宣布后的索取必须能换对等节点（不变量 36）。宣布 ≠ 已收到。不要把 compact / 部分块重建写成共识，也不要和未确认交易索取（不变量 30）糊成一词。  
33. 若做短 ID / 部分下载：重建失败后必须丢掉该实例；对等路径禁止用断言当过滤器（不变量 37）。短 ID 碰撞必须当诚实可能。节点崩溃不得写成共识拒块。  
34. 若提供应用快照同步：必须写出跳过了历史块重放，锚是轻客户端验过的 `AppHash`，信任期须盖住快照高度（不变量 38）。`Snapshot.hash` 不是钢印。不要把 assumeutxo 的背景全验安过来，除非另写重放路径。第一版默认可从创世。  
35. 若做部分下载：下载/重建状态必须按 (对等节点, 对象) 隔离（不变量 39）。未请求的变异块不得清掉其他对等节点的补齐。不要和 2012-2459 同根、52922 卡住、35202 断言糊成一词。  
36. 必须点名块时间算法（不变量 40）。若抄 PBTS：写出 timely 两不等式、不 timely = prevote `nil`、再提议不再验、启用后不能关。若抄 BFT Time：时间从上一高度 `LastCommit` 复算。不要把 MTP 或对等调整钟安到 BFT 头上；不要把「BFT 时间」四个字当成一种算法。`PRECISION` / `MSGDELAY` 先空着，测过再填。  
37. 若学 Bitcoin 时间：必须分开太早（父 MTP）、BIP113 之后的 locktime（也是父 MTP，不是本块 nTime）、太新（本节点钟 + 宽限）（不变量 41）。不要写「我们用 MTP」。不要把跨度或宽限秒数抄进第一版。  
38. 拒绝路径上的 info/warning/error 必须有日志配额（不变量 42）。共识拒绝 ≠ 不占磁盘。不要把检查点或健全性失败写成已经解决灌盘。不要把某次发行的每源每小时字节数抄成共识。  
39. 若并行验签/验脚本：作业若只握指针，任何返回路径必须先汇合队列（不变量 43）。不要只测合法块。节点崩溃不得写成共识已安全拒绝。  
40. 入池前拒绝若不踢对等节点，必须有验代价配额（不变量 44）。非标准 / CheckTx 拒绝 ≠ 便宜 ≠ 已断开。不要和进池之后的孤儿扫描（不变量 32）糊成一词。  
41. 库存宣布必须分开三个方向并各写配额（不变量 45）：入站宣布触发的回复有界；入站索取不得单连接死循环；出站待宣布能丢掉过期对象且排空跟得上。不要写「我们有 INV」。不要和 52913 / 52922 / 52921 糊成一词。  
42. 若收证据：过期必须写成高度**且**时间；窗必须盖住解绑（不变量 46）。不要把仓库默认 `EvidenceParams` 写成已经够罚。这和「上链 ≠ slash」（16）以及「信任期 < 解绑」（15）不是同一句话。  
43. 若点名超时：必须写清它们是**本地**等待，不是锁、不是块时间、不是最终性（不变量 47）。`timeout_commit` 是已经 commit 之后再收迟到票。`skip_timeout_commit` 不论某条发布线还在不在，语义都是「像 `timeout_commit=0`」。不要抄文档秒数或 Alice/Bob 玩具。不要把 `create_empty_blocks` 的「大约每秒一块」写成结算 SLA。  
44. 若点名最大消息长度：必须另写读完载荷前的接收分配上限（不变量 48）。最大序列化长度 ≠ 每连接预分配。不要把 32 / 2 / 4 MiB 抄进第一版。这和发送缓冲（41）、日志盘（38）、头索引（27）不是同一句话。  
45. 若地址 / 库存 / 证据表用递增插入 ID：必须先写回绕谓词（不变量 49）。限速只改代价，不是宽度已够。不要把「短测插不爆」写成 overflow 已消失。不要抄每对等节点每 10 秒 1 条或「一年以上」。  
46. 若自动惩罚对等节点：不得写入可枚举、可持久、可被便宜身份灌的 map（不变量 50）。手动封禁和自动 discourage 必须分开。不要写「我们会 ban」交差。不要抄 GETADDR 返回条数。  
47. 对象「有多大」必须用固定宽度整数，32-bit 与 64-bit 对同一规范化对象必须同拒或同收（不变量 51）。内存池 / 缓存旋钮可以降利用面，不能代替检查宽度。不要抄 GB / GiB / `-maxmempool` 数字。  
48. 若抄较新线 ABCI：post-commit 等待可以由 `FinalizeBlock` 回 `next_block_delay`（不变量 52）。必须标非确定性，点名本条发布线有没有该字段。仍不是最终性，不是全网槽位，不得写进 `app_hash`。不要抄规范「保持旧行为」的常量秒数。ADR 已写恒定间隔做不到。  
49. 结算全节点默认不要开 UPnP / NAT-PMP / 同类自动打洞（不变量 53）。少几个 IPv4 入口不是没在验证。若运维打开，必须写成「局域网对手」，不要和互联网 P2P 糊成一类。  
50. 若配置出站代理：必须写成另一类信任对象，不是 P2P 对等节点（不变量 54）。明文网上的任意代理本身就可被截获。不要把「走了 Tor / SOCKS 所以更安全」写成协议已缩小攻击面。不要抄握手缓冲长度。  
51. 第一版可以不提供付款 URI / 远程取单（不变量 55）。若提供：必须写成钱包辅助，下载自带界；打开链接不是 `Apply`，取单失败不是共识拒绝。删掉该协议可以是正确修法。  
52. 若提供 state sync：除轻验 AppHash（不变量 38）外，必须写清提议者选择字段如何交叉核对（不变量 56）。对不上必须失败，不得带着错日程进共识。不要把「集合哈希对上」写成「下一轮谁提议已一致」。  
53. 若启用 vote extensions：新路径必须复用旧票字段检查（不变量 57），尤其是会当集合下标的字段。不要把「默认关着」或「上游发不出」写成启用后已安全。p2p ban 不能代替接收路径检查。这和 Verify 拒扩展丢掉票（不变量 34）不是同一句。  
54. 若把扩展启用高度做成可治理参数：必须先写合法转移谓词（不变量 58）。过不了必须拒参数，不得 panic。治理通过 ≠ 实现已经能吃。不要抄 66.7% 当不确定法定人数。这和集合更新延迟（不变量 35）不是同一句。  
55. 若块/票走「分片 + Merkle 证明」：外层下标必须等于证明下标（不变量 59）。对不上必须拒，不得标已收到、不得再流言。不要把验根写成「这就是第 i 片」。不要抄分片字节大小。  
56. 对等消息里凡是「声明长度 + 实际容器」的对象，必须在流言之前验完（不变量 60）。对不上丢弃。不要先传后验。防火墙 ban 不能代替接收谓词。  
57. 若抄 BFT Time：Verify(Commit) 与 MedianTime 必须吃同一规范化集合（不变量 61）。不要把「中位数复算通过」写成故障者不能抬高 Time。不要写怎样抬高。这和点名算法（不变量 40）不是同一句。  
58. 若提供 blocksync / 追尖：目标高度必须可归因到仍连着的对等节点，来源改低或断开必须重算（不变量 62）。不要把邻居 `latest` 写成全网尖。不要因后来标 Informational 就删这句。  
59. 必须自己写 `BlockParams.MaxBytes`，并让 `timeout_propose` 对照该上限（不变量 63）。仓库默认不是第一轮活性 SLA。超限必须拒。不要抄示例兆字节。这和证据体积 MaxBytes、接收分配（44）、timeout_commit（43）不是同一句。  
60. 若证据对象带时间戳或其它身份字段：必须取自已经最终、全网能复算的对象（不变量 64）。不要用仍在飞行中的块的 last commit 拼 `DuplicateVoteEvidence`。发现双签不得让诚实者因辅助字段分叉而互踢。这和上链≠slash（16）、默认窗（42）、块 Time 两条路径（57）不是同一句。  
61. Commit / LastCommit 每个槽位必须是对本块本 ChainID 的有效签，或显式缺席（不变量 65）。+2/3 是安全门槛，不是其余槽位的许可证。应用若按「谁签了」发奖，必须写清引擎是否验完整个 Commit。轻客户端凑齐 2/3+ 就停不是全节点已验完。复用 ChainID 不是重置。不要抄奖金公式。这和锁、证据身份（60）、块 Time 两条路径（57）不是同一句。  
62. 若提供 BFT 轻客户端：收下坏头必须能形成证据（不变量 66）。证据不得只依赖「同一高度已经出了另一块」。朝前高度的坏 commit 仍须能问责。验过头 ≠ 已经能提交。安全模型外不是免检。停链后若还要交证据，取块必须带时间。不要抄 ⅓ 当不确定门槛。这和重叠旧集合（15）、上链≠slash（16）、证据身份（60）不是同一句。  
63. 入站连接请求在变成 Peer 之前就必须有配额（不变量 67）。对等 ID 必须在连接启动前认领，并在所有退出路径归还。不要把入站邻居上限写成握手已有界。公开 RPC 另写 HTTP 配额。不要抄 65535 或咨询里的 XXX 字节。这和接收分配（44）、封禁表（46）、库存（41）、地址表回绕（45）不是同一句。  
64. 若启用 vote extensions 并在 ProcessProposal 读权重：必须读已提交集合（不变量 68）。不要从提议者注入的扩展推断总值或每人值。默认 SDK 助手不是规范保证。扩展签名为真 ≠ 权重已对齐。这和拒扩展丢票（30）、快路径下标（53）、启用高度治理（54）不是同一句。  
65. 若按发送者序号装箱：Prepare 必须交出诚实 Process 会 Accept 的前缀（不变量 69）。不要把单笔 CheckTx 绿写成整包可提案。默认 Prepare handler + 默认 nonce 池不是规范保证。这和四门定义（29）、块上限 SLA（59）、注入扩展权重（64）不是同一句。  
66. 若消息可嵌套（Any / 内部消息 / 合约放出的消息）：外层 `max_tx_bytes` 不是内层已有界（不变量 70）。解码必须有递归上限。内部消息与恶意验证者块放出的消息必须另写界。不要把「进门交易够短」写成 UnpackAny 已安全。这和四门 Req 2（29）、接收分配（44）、块上限 SLA（59）、位图先验（56）不是同一句。  
67. 若启用带 EndBlocker 的可选模块：该模块里的错误必须写成可能停链（不变量 71）。不要把「只是治理/群组模块」写成局部失败。能与该模块交互的用户集合就是能引入停链状态的集合。不要抄 `x/group`。这和治理改启用高度 panic（54）、位图先流言（56）、外层解码（66）不是同一句。  
68. 若做委托 / 再委托：待执行罚没必须跟着过错当时的质押走（不变量 72）。再委托不是洗白。「验证者还没被 slash」不是委托人已经干净。第一版可以不做再委托。不要把咨询 Low 写成可忽略。这和上链≠slash（16）、两票谓词（22）、默认证据窗（42）不是同一句。  
69. 若提供「不变量失败则停链」模块：必须写清停发生在交易内还是 EndBlock（不变量 73）。交易内 panic 可被恢复，不是已经停链。需要真停可以写链下协调。不要把 `MsgVerifyInvariant` 写成已停。不要抄 `--inv-check-period`。这和可选模块 EndBlocker 出错会停（67）不是同一句。  
70. 若有验证者奖励池 / 分配模块：入金溢出必须拒，不得变成停链（不变量 74）。能向该池存款的验证者是活性对手。不要抄 `x/distribution`。这和输出求和必须拒（不变量 7）、固定宽度（不变量 51）、EndBlocker 可选模块（67）、停链交易被恢复（69）不是同一句。  
71. 若有模块账户 / 被挡地址：必须在创世或迁移时初始化（不变量 75）。禁止对未初始化的被挡地址建定期归属账户。authz / feegrant 是同一面。不要把「并不常见」写成已安全。这和可选模块 EndBlocker（67）、停链交易（69）、奖励池溢出（70）不是同一句。  
72. 若金额用两套可互转的数（整数 / 小数）：必须对齐最大位宽（不变量 76）。Dec 进 Int 不得 panic。数学库补丁是否要硬分叉，以官方该页为准（本条出处：1.3.0→1.4.0 可只改依赖；更低版本先协调升级）。不要抄位宽。这和输出求和拒块（不变量 7）、固定宽度尺寸（不变量 51）、奖励池溢出（70）不是同一句。  
73. 若提供跨链确认 / IBC 类 ack：反序列化必须确定性（不变量 77）。能开通道的用户是活性对手。只修 transfer 不够。中间件若自己编 ack，必须与应用同一 codec，否则补丁可能变成协调升级。第一版可以不装 IBC。这和一般确定性（1）、外层解码（66）、可选模块 EndBlocker（67）不是同一句。  
74. 若提供跨链超时回调 / 挂钩中间件：回调不得在包承诺删除前重入同一超时（不变量 78）。第一版可以不装 CosmWasm、不装 ibc-hooks。许可上传不是已安全。这和 ack 确定性（73）、供给守恒（不变量 2）不是同一句。  
75. 若提供跨链 Merkle 证明语言（ICS-23 类）：必须先写 soundness；Verify 绿不得单独充当「对岸没收到」（不变量 79）。伪造超时不是 ICS-20 已结算。升依赖版本不是证明库已经换。+⅓ 打补丁变成停链可见，不是谓词已齐。第一版可以不装 IBC。不要抄 ⅓。这和挂钩重入（74）、ack 确定性（73）、验证明≠供给（不变量 13）、Merkle 同根（不变量 12）不是同一句。  
76. 若提供升级高度上的二进制管家：默认禁止从网上拉可执行文件（不变量 80）。验证者角色不得打开自动下载。校验和默认不强制不是已有强保证。管家换程序不是共识已经换完。第一版可以不提供自动换二进制。不要抄 Cosmovisor。这和软/硬分叉分类（L9.4）、ics23 replace（75）不是同一句。  
77. 若提供授权代发 / 包装执行：内层消息必须再跑与直接投递相同的基本校验（不变量 81）。授权过了不是内层已合法。同一天打包的其它补丁不是本条已齐。第一版可以不装授权代发。不要抄 authz。这和被挡账户（71）、ics23 soundness（75）、ValidateBasic 读钟（78）不是同一句。  
78. 若状态机或入门校验要判断过期：只读块头时间（不变量 82）。ValidateBasic 读节点本地钟不是已确定。资金安全不是链不会停。不要把「额外防守」写成可以读墙钟。这和一般确定性（1）、PBTS（不变量 40）、漏掉 ValidateBasic（77）不是同一句。  
79. 若提供定期归属 / 他人可初始化的账户子类型：账户类型必须由权利人或创世初始化（不变量 83）。空地址不是还没有类型。入金不是还能取出。33% 打补丁不是全网已齐。第一版可以不装归属账户。不要抄 33/66。不要抄 vesting。这和被挡模块账户（71）、授权代发（77）不是同一句。  
80. 若产品句写「停链」：必须从停链面地图点名路径（不变量 84）。交易内 panic 可被恢复；EndBlocker 出错会停；非确定会停；版本差会停；锁钱不是停。不要把 ⅓ / 33 / 66 抄进不确定法定人数。地图：[`../../tracks/failure-museum/worked-example-halt-surfaces.md`](../../tracks/failure-museum/worked-example-halt-surfaces.md)。这和停链交易（69）、可选模块 EndBlocker（67）不是同一句——那两句是表里的两行，不是本条。  
81. 若提供不过期 / durable nonce：失败路径必须与成功路径一样推进或作废同一链上对象（不变量 85）。当普通 recent-blockhash 处理、nonce 未推进，不是已消费。进块付费不是票根已撕。近期缓存不是全网同一对象。一边收一边拒、超过 33% 不够 66% 是停链，不是 Tower / PoH 已经一致。第一版可以不提供不过期 nonce。不要写怎样走双路径。不要抄 33/66。馆藏：[`../../tracks/failure-museum/solana-2022-06-01-durable-nonce.md`](../../tracks/failure-museum/solana-2022-06-01-durable-nonce.md)。这和一般确定性（1）、ack JSON（73）、ValidateBasic 读钟（78）、非法提案（69）不是同一句。  
82. 若同槽可能出现两份不同块：必须写出谁赢、赢了之后下一领导者必须能把它当父块（不变量 86）。确认 ≠ 可建。投票还在、根不前进，不是 Tower / PoH 已经一致。同一身份两台同时出块不是高可用。关掉故障提议者不是边角已消失。不要抄 80/90。馆藏：[`../../tracks/failure-museum/solana-2022-09-30-duplicate-fork.md`](../../tracks/failure-museum/solana-2022-09-30-duplicate-fork.md)。这和 durable nonce 双路径（81）、非法提案（65）、宣布≠收到（32）不是同一句。锁规则见不变量 4。  
83. 若块要切成数据碎片 + 恢复碎片：两类对象必须各自写过滤谓词（不变量 87）。恢复碎片缺父槽字段，不是已按父槽滤掉。坐在过滤前面的转发 / 中继是另一信任对象。vote-only / 落到后备补洞不是高度已停，也不是已最终经济交易被回滚。不要把「刚过 ⅔ 升上某版」写成根因。不要抄 400 槽或 66%。馆藏：[`../../tracks/failure-museum/solana-2023-02-25-turbine-recovery.md`](../../tracks/failure-museum/solana-2023-02-25-turbine-recovery.md)。这和 durable nonce（81）、重复槽不能当父块（82）、宣布≠收到（32）不是同一句。  
84. 若程序缓存用有效槽 / 哨兵世代：插入键必须与查找键是同一对象（不变量 88）。账户不保留部署槽时，不得用会被挡在「已卸载」后面的哨兵 0。再编译完成不是已可见。协作加载若让交易进块，必须测全网回放，不得只测 leader。关掉旧加载器部署是拆前提，不是缓存已修。不要抄 95% 或乐观确认槽号。馆藏：[`../../tracks/failure-museum/solana-2024-02-06-legacy-loader-loop.md`](../../tracks/failure-museum/solana-2024-02-06-legacy-loader-loop.md)。这和恢复 shred（83）、并行验签寿命（不变量 43）不是同一句。  
85. 若产品句写「洪水 / 拥堵 / 高 TPS」：必须再点名停在票不够、分叉不回收，还是单节点 OOM（不变量 89）。入站数字不是停链谓词。重启后分叉仍超能力不是自动恢复。固定地板价 + 先到先得必须写成经济对手会灌包。不要抄官网 TPS。不要把 QUIC / 加权 QoS / 本地费写成已完成。馆藏：[`../../tracks/failure-museum/solana-2022-04-30-fork-cleanup-oom.md`](../../tracks/failure-museum/solana-2022-04-30-fork-cleanup-oom.md)。这和 vote-only（83）、握手 OOM（63）、库存配额（41）不是同一句。  
86. 若做共享对象拥塞控制 / 执行代价估算：估值失败必须拒或排队，不得 assert 崩进程（不变量 90）。估值为 0 必须当合法边角。owned 快路径绿了不是共享路径已安全。换估值模式必须重测边角。不要抄协议版本或恢复分钟数。馆藏：[`../../tracks/failure-museum/sui-2024-11-21-zero-cost-assert.md`](../../tracks/failure-museum/sui-2024-11-21-zero-cost-assert.md)。这和断言当过滤器（33）、检查点隔离（87）不是同一句。  
87. 若执行效果要等检查点 / 提交认证才最终：未认证不得当结算（不变量 91）。隔离区拒证、进度停住，不是用户已看见分叉。RPC 读上一份已认证状态不是新交易已执行。共识提交的优化路径必须与慢路径同输出。不要抄 ⅓。馆藏：[`../../tracks/failure-museum/sui-2026-01-14-commit-divergence.md`](../../tracks/failure-museum/sui-2026-01-14-commit-divergence.md)。这和拥塞控制 assert（86）、durable nonce（81）、提交≠兑付（不变量 9）不是同一句。  
88. 若气费可从地址余额与币对象混合划出，或取消路径仍会改余额：因余额不足取消不是已经不再扣款（不变量 92）。取消路径上的 gas smash 不是守恒已成立。只认一种取消理由的临时补丁不是下溢已消失。结算负增量加到零余额上崩进程，不是已经拒交易。第一版可以只用一种付费对象。不要抄 1.72。不要写怎样竞态。馆藏：[`../../tracks/failure-museum/sui-2026-05-gas-smash-cancel.md`](../../tracks/failure-museum/sui-2026-05-gas-smash-cancel.md)。这和估值 0 assert（86）、检查点隔离（87）、DKG 未落盘（89）、供给口号（不变量 2）不是同一句。  
89. 若提供链上随机信标 / DKG：失败裁决必须落盘，重启后仍有效（不变量 93）。按设计关掉不是重启后还记得。依赖随机性的交易在已关 / 未知时必须能取消，不得只挂起。纪元结束不得无界等待一条永远不来的队列。一次强制关纪元不是常备能力。现有换纪元安全模式不是整条重配置已覆盖。第一版可以不提供 DKG。不要抄门槛。馆藏：[`../../tracks/failure-museum/sui-2026-05-dkg-verdict-disk.md`](../../tracks/failure-museum/sui-2026-05-dkg-verdict-disk.md)。这和取消后仍砸气费（88）、原子高度（不变量 5）、检查点隔离（87）不是同一句。  
90. 若块 / 银行 / repair 用高度或槽号当主键：必须改成内容哈希当身份（不变量 94）。同槽两份不同块必须能像不同槽的分叉一样互修。Turbine / 传播按「已传过」去重必须点名按哪个身份。乐观确认不是已经 rooted，也不是重启必保留。不要抄官网吞吐。馆藏：[`../../tracks/failure-museum/solana-2020-12-04-slot-as-block-id.md`](../../tracks/failure-museum/solana-2020-12-04-slot-as-block-id.md)。这和确认了不能当父块（82）、恢复 shred（83）、同根不同列表（不变量 12）不是同一句。  
91. 若提供机密余额 / 链上非交互证明：Fiat-Shamir transcript 必须纳入验证时当已绑定的全部代数分量（不变量 95）。验绿不是不可铸 / 不可偷。应用层未改不是证明程序已齐。先前审计与未见利用不是 transcript 已绑完。第一版可以不提供机密余额。不要写怎样伪造。馆藏：[`../../tracks/failure-museum/solana-2025-05-02-elgamal-fiat-shamir.md`](../../tracks/failure-museum/solana-2025-05-02-elgamal-fiat-shamir.md)。这和 Sprout 构造可靠性（不变量 13）、ICS-23 验绿（75）、有效性点名程序哈希（不变量 28）不是同一句。  
92. 若执行与共识分开、用 RPC / Engine API 出块：出块通道尺寸必须与入池单笔上限、块计量上限分开写，且各实现同拒或同收（不变量 96）。单笔低于入池上限不是拼块已被所有客户端接受。把各家收到同一低值不是许多小交易不能顶满。多数拒、少数收按分叉审。不要抄 413。馆藏：[`../../tracks/failure-museum/ethereum-2024-03-sepolia-engine-rpc.md`](../../tracks/failure-museum/ethereum-2024-03-sepolia-engine-rpc.md)。这和执行别名错根（不变量 3）、接收分配（44）、默认 MaxBytes（59）不是同一句。  
93. 若有交易解码深度 / 嵌套 batch：深度计数器只走交易对象，不得套在 runtime API 整块参数上（不变量 97）。出块收下不是导入 check_inherents 已能解。导入失败不是邻居已经作恶。拉黑一个哈希不是同类不会再来。第一版可以不做嵌套 batch。不要抄深度数字。馆藏：[`../../tracks/failure-museum/polkadot-2025-05-runtime-api-decode-depth.md`](../../tracks/failure-museum/polkadot-2025-05-runtime-api-decode-depth.md)。这和外层字节不是内层已有界（66）、自动封禁无界表（46）、Engine API 尺寸（92）不是同一句。  
94. 若出块要按组剔除已禁用者的票：组下标不是票向量下标（不变量 98）。票可以比组少。create_inherent 回 None 不是客户端已报错。生产关日志不是错误已可见。第一版可以不做平行链 backing 过滤。馆藏：[`../../tracks/failure-museum/kusama-2025-08-24-group-index-votes.md`](../../tracks/failure-museum/kusama-2025-08-24-group-index-votes.md)。这和分片下标（56）、解码深度（93）、Active≠Confirmed（95）不是同一句。  
95. 若做争议状态机 / 禁用验证者：导入、Active、Confirmed 必须分开（不变量 99）。只被 Disabled 发起不得标 Active。GRANDPA 跳过含 Active 的叉不是最终性还在走。测试必须另断言最终性。第一版可以不做争议禁用。不要抄 ⅓。馆藏：[`../../tracks/failure-museum/kusama-2024-02-15-disabled-active-dispute.md`](../../tracks/failure-museum/kusama-2024-02-15-disabled-active-dispute.md)。这和形状≠slash（不变量 21）、组下标（94）、票还在根不前进（82）不是同一句。  
96. 若做链下 / 内存争议禁用：只挡未确认不是已确认已经不参与（不变量 100）。重启清空名单不是已经禁用。训练轮触发不是最终性还在走。预期旧节点会争议不是禁用表已经挡住。第一版可以不做争议禁用。不要抄确认门槛 / ⅓。馆藏：[`../../tracks/failure-museum/kusama-2025-05-09-offchain-disable.md`](../../tracks/failure-museum/kusama-2025-05-09-offchain-disable.md)。这和 Active≠Confirmed（95）、DKG 未落盘（89）、升级下载管家（不变量 80）不是同一句。  
97. 若做资源计量 / 通用 VM：必须点名钉的是字节、步数还是墙钟（不变量 101）。块 gas 上限不是墙钟已有界。状态访问的常数 gas 不是磁盘已是 O(1)。无条件涨价不是已够。未命中罚金不是已付查找。快照默认开不是 gas 已经等于时间。第一版可以不做通用 VM。不要抄 gas / 秒数。馆藏：[`../../tracks/failure-museum/ethereum-2021-05-state-gas-not-time.md`](../../tracks/failure-museum/ethereum-2021-05-state-gas-not-time.md)。这和洪水≠停（85）、Engine API 尺寸（92）、估值 0（86）不是同一句。  
98. 若做电路 / 屏蔽池：陈述、电路、验证钥必须分开（不变量 102）。电路实现不是已经写明的陈述。旧钥过验不是新电路已安全。关池热修不是陈述已改。第一版可以不做屏蔽池。不要抄高度 / 证明长度。馆藏：[`../../tracks/failure-museum/zcash-2026-orchard-circuit-not-statement.md`](../../tracks/failure-museum/zcash-2026-orchard-circuit-not-statement.md)。这和 Sprout 构造（不变量 13）、FS 漏哈希（91）、程序哈希（不变量 28）不是同一句。  
99. 若做可失败的状态机 / 自动删空账户：失败路径必须撤回本笔每一种改动（不变量 103）。OOG 结束不是空账户删除已回滚。journaling 只记成功不是失败已撤。第一版可以不自动删空账户。不要抄块号。馆藏：[`../../tracks/failure-museum/ethereum-2016-11-oog-empty-account.md`](../../tracks/failure-museum/ethereum-2016-11-oog-empty-account.md)。这和执行别名（不变量 3）、崩溃半块（不变量 5）、gas≠墙钟（97）不是同一句。  
100. 若做多池闸门 / 链价值跟踪：初始化必须在去重之后（不变量 104）。重复头复位跟踪不是闸门还在转。规范写着 ZIP 209 不是实现字段仍有效。盘上增量不是启动已核对。第一版可以不做多池闸门。不要抄版本 / 高度 / 规范金额上限。馆藏：[`../../tracks/failure-museum/zcash-2026-zip209-header-reset.md`](../../tracks/failure-museum/zcash-2026-zip209-header-reset.md)。这和供给口号（不变量 2）、验证明≠供给（不变量 13）、奖励池溢出（70）、电路≠陈述（98）、归一化≠编码（101）不是同一句。  
101. 若字段「在某条件下必须为 0」：检查必须读规范编码，不得先改再验（不变量 105）。反序列化归一化成零不是编码必须为零。检查跑在改写后的字段上不是规则已经开火。一家拒一家收不是多实现已经同根。第一版可以不做屏蔽余额栏。不要抄版本号。馆藏：[`../../tracks/failure-museum/zcash-2026-valuebalance-normalized.md`](../../tracks/failure-museum/zcash-2026-valuebalance-normalized.md)。这和确定性别名（不变量 3）、同根不同列表（不变量 12）、电路≠陈述（98）、跟踪复位（100）不是同一句。  
102. 若头承诺两个根（交易列表 / 授权数据）：体可变拒绝不得先于对应承诺、把诚实头写入永久非法表（不变量 106）。Merkle 根对上不是授权数据已承诺。诚实头被拉黑不是块已经非法。第一版可以不做第二承诺根。不要抄版本 / 触发路径。馆藏：[`../../tracks/failure-museum/zcash-2026-nu5-body-poison.md`](../../tracks/failure-museum/zcash-2026-nu5-body-poison.md)。这和同根不同列表（不变量 12）、变异清别人下载（不变量 39）、Engine API 尺寸（92）、跟踪复位（100）不是同一句。  
103. 若规范允许某曲线点编码进验证明：公开输入转换必须覆盖或入口显式拒，不得恐慌（不变量 107）。规范允许身份 `rk` 不是验证明已经能吃。电路支持零点不是转换已经写对。排除零点是收紧，不是陈述本来就禁止。第一版可以不做屏蔽授权随机化点。不要抄版本 / 曲线方程。馆藏：[`../../tracks/failure-museum/zcash-2026-identity-rk-panic.md`](../../tracks/failure-museum/zcash-2026-identity-rk-panic.md)。这和电路≠陈述（98）、`ephemeralKey`（104）、估值 0（86）不是同一句。  
104. 若规范要求字段是合法非零点：两实现必须同拒无效编码（不变量 108）。一家收下不是规范已经允许。先拒零点不是全部无效编码已挡。与 `rk` 同曲线不是同一对象。第一版可以不做一次性密钥点栏。不要抄版本号。馆藏：[`../../tracks/failure-museum/zcash-2026-ephemeralkey-split.md`](../../tracks/failure-museum/zcash-2026-ephemeralkey-split.md)。这和身份 `rk`（103）、归一化（101）、电路≠陈述（98）不是同一句。  
105. 若供给与池是两本账：对不上必须拒并停在上一高度，不得中止成崩溃循环（不变量 109）。coinbase 正屏蔽余额不是供给已经对齐。`ConnectBlock` 对不上不是重启能起来。活性崩溃不是合法集已改。第一版可以不做 coinbase 进屏蔽池。不要抄版本 / 规范金额上限。馆藏：[`../../tracks/failure-museum/zcash-2026-coinbase-balance-crash.md`](../../tracks/failure-museum/zcash-2026-coinbase-balance-crash.md)。这和原子高度（不变量 5）、奖励池溢出（70）、跟踪复位（100）不是同一句。  
106. 若做链上选举 / 许可冷冻 / 质量地板：改可达分的治理必须同时带地板（不变量 110）。改冻结门槛不是选举地板已经配对。出块还在不是纪元已经转。诚实解被 ScoreTooLow 罚不是提交者作恶。第一版可以不做这三件套。不要抄金额 / 公投号。馆藏：[`../../tracks/failure-museum/polkadot-2026-06-election-score-floor.md`](../../tracks/failure-museum/polkadot-2026-06-election-score-floor.md)。这和集合延迟（不变量 35）、治理 panic（54）、EndBlocker 停链（67）、争议禁用（95/96）不是同一句。  
107. 若钱包可连远程节点：交出站历史的 RPC 必须先看 trusted（不变量 111）。从文件加载不是出站 TXID 已经不泄漏。trusted 标记不是这条 RPC 已经检查。环库回填还在不是只给旧钱包跑一次。第一版可以不连远程守护进程。不要转复现步骤。馆藏：[`../../tracks/failure-museum/monero-2025-08-find-and-save-rings.md`](../../tracks/failure-museum/monero-2025-08-find-and-save-rings.md)。这和付款 URI（51）、代理（50）、隐私广播（108）不是同一句。  
108. 若提供隐私广播 / 单笔另开连接：每一次降级重连必须仍走同一代理谓词（不变量 112）。开关不是 IP 已经不暴露。v2 失败后的 v1 重连不是仍走代理。第一次走 Tor 不是降级已覆盖。第一版可以不提供该开关。不要抄版本 / 端口。馆藏：[`../../tracks/failure-museum/bitcoin-2026-06-privatebroadcast-v1-retry.md`](../../tracks/failure-museum/bitcoin-2026-06-privatebroadcast-v1-retry.md)。这和代理当对等（50）、付款 URI（51）、钱包泄 TXID（107）不是同一句。  
109. 若做跨共识消息 / XCM：保留 origin 的旗标必须对应一条确定的出站指令（不变量 113）。当前 origin 为空必须失败关闭。`preserve_origin` 为真不是出站已经带了改 origin 的指令。静默跳过不是 BadOrigin。目的地用运输发送者不是用户 origin 已经清掉。第一版可以不做 XCM。不要写怎样拼指令。馆藏：[`../../tracks/failure-museum/polkadot-2026-03-xcm-preserve-origin.md`](../../tracks/failure-museum/polkadot-2026-03-xcm-preserve-origin.md)。这和提交≠兑付（不变量 9）、IBC 确认（73）、授权代发（77）、解码深度（93）不是同一句。  
110. 若废弃仍可能被旧节点调用的 runtime API：返回编码必须与仍在外的调用方兼容，或入口失败且送块不得依赖它（不变量 114）。废弃还在不是返回编码已经兼容。整理者还能写块不是中继已经收到。支持窗不是更老节点编码已保证。第一版可以不做平行链双代 API。不要抄版本 / 个数。馆藏：[`../../tracks/failure-museum/polkadot-2026-03-deprecated-runtime-api-scale.md`](../../tracks/failure-museum/polkadot-2026-03-deprecated-runtime-api-scale.md)。这和解码深度（93）、确定性（1）、Engine API 尺寸（92）、XCM origin（109）不是同一句。  
111. 若一层引擎只看见可花、另一层允许锁定去质押：写回必须用同一对象，委托额大于视图必须拒（不变量 115）。StateDB 可花不是锁定已经从同一笔写回排除。回绕后的数不是银行账已经对齐。主分支静默补丁不是发布线已经打上。第一版可以不做通用 EVM / 归属 / 质押预编译。不要写怎样委托锁定。馆藏：[`../../tracks/failure-museum/cosmos-evm-2026-08-statedb-vesting.md`](../../tracks/failure-museum/cosmos-evm-2026-08-statedb-vesting.md)。这和求和拒回绕（不变量 7）、奖励池溢出（70）、空地址归属（79）、被挡账户（71）不是同一句。  
112. 若验未信任曲线点 / 配对预编译：必须先在曲线上、再在子群里（不变量 116）。子群过了不是点已经在曲线上。原生加速不是两家已经同根。只影响一家不是共识已经安全。第一版可以不做配对预编译。不要写怎样造点。馆藏：[`../../tracks/failure-museum/cve-2025-30147.md`](../../tracks/failure-museum/cve-2025-30147.md)。这和确定性（1）、电路（98）、屏蔽点编码（103/104）不是同一句。  
113. 若一层引擎调另一层有状态预编译：失败必须撤回两边（不变量 117）。预编译中途出错不是 SDK 已写入已经撤回。领奖转出不是可领已经清零。更低 gas 不是已经更安全。第一版可以不做跨 VM 预编译。不要写怎样调 gas。馆藏：[`../../tracks/failure-museum/isa-2025-004.md`](../../tracks/failure-museum/isa-2025-004.md)。这和 OOG 删户（99）、可花≠锁定（111）、嵌套外层看不见（114）不是同一句。  
114. 若嵌套执行跨模块预编译：内层更新必须对外层同一对象立刻可见（不变量 118）。内层改过不是外层已经看见。同一笔里余额还在不是不能再花一次。关掉预编译不是嵌套写回已经齐。第一版可以不做 ICS20 预编译。不要写怎样嵌套。馆藏：[`../../tracks/failure-museum/asa-2026-002.md`](../../tracks/failure-museum/asa-2026-002.md)。这和预编译半写入（113）、IBC 确认（73）、可花≠锁定（111）不是同一句。  
115. 若有状态预编译允许 `DELEGATECALL` / `CALLCODE`：必须写清授权看的是 EVM 语义调用者还是原始调用者，或入口直接拒绝委托（不变量 119）。正确兑现委托语义不是预编译信任模型已经跟着改过。库换了正确语义不是旧假设已经更新。热修 / 硬升级不是谓词本来就齐。第一版可以不做有状态预编译 / 委托调用进特权入口。不要写怎样冒充。馆藏：[`../../tracks/failure-museum/avalanche-2025-delegatecall-precompile.md`](../../tracks/failure-museum/avalanche-2025-delegatecall-precompile.md)。这和预编译半写入（113）、嵌套外层看不见（114）、授权代发（不变量 81）不是同一句。  
116. 若提供钱包格式迁移：失败清理必须只覆盖这次失败的对象（不变量 120）。迁移失败不是目录里其它钱包已经安全。现有用户不受影响不是迁移路径已经安全。下架二进制不是已安装副本已经修。第一版可以不提供迁移器。不要写怎样踩失败。馆藏：[`../../tracks/failure-museum/bitcoin-2026-01-wallet-migration-delete.md`](../../tracks/failure-museum/bitcoin-2026-01-wallet-migration-delete.md)。这和加载泄 TXID（不变量 111）、付款 URI（不变量 55）、隐私广播（不变量 112）不是同一句。  
117. 若用对等节点送来的时限做 `Instant + Duration`：存进去与以后加余量必须同一套检查加法（不变量 121）。插入路径做了检查加法不是心跳加上余量已经安全。解析当时没崩不是心跳不会崩。成了协议对等节点不是已经认证。第一版可以不抄该 Gossipsub。不要写怎样拼控制消息。馆藏：[`../../tracks/failure-museum/cve-2026-34219.md`](../../tracks/failure-museum/cve-2026-34219.md)。这和拼块断言（不变量 37）、验签崩溃（不变量 43）、估值 0（不变量 90）不是同一句。  
118. 若做乐观并行执行：必须先有共识序列 L，提交写集必须等于单线程按 L 的结果（不变量 122）。STM 跑完不是已经最终。未事先声明写集不是已经不需要 L。不要求 opacity 不是中间态可以给人看。第一版可以不上 STM。不要抄加速比。精读：[`../../tracks/parallelism/worked-example-block-stm.md`](../../tracks/parallelism/worked-example-block-stm.md)。这和确定性口号（1）、池预检（不变量 33）、头即结算不是同一句。  
119. 若做递归 / 简短验证：必须点名证明覆盖哪一本账（不变量 123）。区块链 SNARK 验绿不是最新 staged 已经被证明。进块 Apply 不是已经进入 SNARKed ledger。Pickles 不是 Kimchi。验 π 不是已经有账户与路径。第一版可以不上递归 L1。不要抄 22kB。精读：[`../../tracks/light-clients/worked-example-snarked-vs-staged.md`](../../tracks/light-clients/worked-example-snarked-vs-staged.md)。这和验证明≠供给（不变量 13）、两层 accepted（不变量 28）、短时 DA（不变量 23）、快照≠创世（不变量 38）不是同一句。  
120. 若做抽样 / 命名空间 DA：必须点名问的是整块可用、命名空间齐了、编码诚实，还是历史检索（不变量 124）。NMT 齐了不是扩展方阵已经可用。DAS 抽样过关不是已经拿到自己的 blob，也不是编码已经诚实。新块 DA 不是历史已经有人存。第一版可以不当别人的 DA 房东。不要抄方阵边长 / FAQ 百分比。精读：[`../../tracks/light-clients/worked-example-nmt-vs-das.md`](../../tracks/light-clients/worked-example-nmt-vs-das.md)。这和 KZG≠纠删 DAS（不变量 23）、头即结算、提交≠兑付（不变量 9）不是同一句。  
121. 若做平行链 / 共享安全：用户可见的「到了」必须点名停在哪一行（不变量 125）。Backed 不是已经可用。可用不是已经有效。Included 不是已经批准。批准不是已经 GRANDPA 最终。中继头有回执不是 PoV 在链上。第一版可以不做平行链。不要抄秒数 / 门槛数字。精读：[`../../tracks/finality/worked-example-backed-vs-available.md`](../../tracks/finality/worked-example-backed-vs-available.md)。这和提交≠兑付（不变量 9）、Active≠Confirmed（不变量 99）、废弃 API（不变量 114）、NMT≠DAS（不变量 124）不是同一句。  
122. 若拆出块与最终两套装置：用户可见的「到了」必须点名是出块还是最终（不变量 126）。BABE 出块不是已经 GRANDPA。最长链不是 hybrid 最终头之后的尺子。BEEFY 绿不是已经解释了 GRANDPA。第一版可以保持 CometBFT 式同路径出块+终局。不要抄槽秒数 / 百万块 / 超多数数字。精读：[`../../tracks/consensus/worked-example-babe-vs-grandpa.md`](../../tracks/consensus/worked-example-babe-vs-grandpa.md)。这和每高度 commit（L4.6）、Gasper 三词（L5.2）、平行链管道（不变量 125）、出块还在≠纪元已转（不变量 110）、中继最终≠平行已出（不变量 114）不是同一句。  
123. 若头可摆 + 检查点最终：用户可见的「到了」必须点名是 head / justified / finalized 中的哪一等（不变量 127）。出块不是已经 justified。justified 不是已经 finalized。JSON-RPC `latest` / `safe` / `finalized` 不是同一标签。一张 attestation 的头票不是已经投了最终。第一版可以不卖三等确认。不要抄槽秒数 / epoch 长度 / 美元。精读：[`../../tracks/finality/worked-example-head-vs-justified-vs-finalized.md`](../../tracks/finality/worked-example-head-vs-justified-vs-finalized.md)。这和 BABE≠GRANDPA（不变量 126）、弱主观性（不变量 24）、抽样委员会（不变量 22）、两票谓词（不变量 26）不是同一句。  
124. 若做对象所有权 / 快路径：必须点名版本走快路径还是共识（不变量 128）。单地址所有不是已经走快路径。引用 shared 不是已经授权。进了共识块不是这笔已被接受。第一版可以不卖快路径 / party / shared 三套「到了」。不要抄测试 TPS。精读：[`../../tracks/parallelism/worked-example-owned-vs-fastpath.md`](../../tracks/parallelism/worked-example-owned-vs-fastpath.md)。这和 STM 跑完≠最终（不变量 122）、估值 0（不变量 90）、隔离拒证（不变量 91）、Gasper 三等（不变量 127）不是同一句。
125. 若做提名选人 / 债券质押：必须先点名超多数的单位是验证者还是质押（不变量 129）。NPoS 当选不是共识票已经按质押加权。⅔ 验证者不是 ⅔ 质押。提名时的加权不是当选后的等权。BABE 按质押抽槽不是 GRANDPA 也按质押。提名不是治理权已经交出。第一版不要发明「所有 PoS 都按人数」或「所有 PoS 都按质押」。不要抄验证者上限 / 提名数 / 示例 DOT。精读：[`../../tracks/consensus/worked-example-npos-equal-weight.md`](../../tracks/consensus/worked-example-npos-equal-weight.md)。这和出块≠最终（不变量 126）、选举地板（不变量 110）、抽样委员会（不变量 22）、Gasper ⅔ 总质押（不变量 127）不是同一句。
126. 若用检查点最终：必须另写终局推迟时怎么办（不变量 130）。终局推迟不是高度已经停。Inactivity leak 不是 slash。没 attestation 不是已经可罚。两边都 leak 到 finalized 不是协议已经选出唯一规范链。第一版不要抄 epoch 个数或美元。不要写怎样扣块或双投。精读：[`../../tracks/finality/worked-example-inactivity-leak.md`](../../tracks/finality/worked-example-inactivity-leak.md)。这和三等确认（不变量 127）、两票谓词（不变量 26）、停链面（不变量 84）、选举地板（不变量 110）、弱主观性（不变量 24）不是同一句。
127. 若对照抽样固化：必须点名问的是样本置信还是可转发证书（不变量 131）。抽样 α 多数不是全集 +2/3 证书。连续 β 轮不是一张 QC。Preference 不是已经接受。出块窗不是已经决定。第一版不要同时卖 QC 与抽样固化。不要抄样本个数 / 亚秒。精读：[`../../tracks/consensus/worked-example-snow-sample-vs-qc.md`](../../tracks/consensus/worked-example-snow-sample-vs-qc.md)。这和抽样委员会（不变量 22）、每高度 commit（L4.6）、Gasper 三等（不变量 127）、C-Chain 委托事故（不变量 119）不是同一句。
128. 若拆传播与排序：必须点名停在批次传播、已认证、已排序、已执行还是已落盘（不变量 132）。已认证批次不是已经写出 L。传播齐了不是已经 commit。去掉领袖数据瓶颈不是已经没有领袖。进了提议块不是已经落盘。第一版可以不拆传播层。不要抄吞吐。不要写怎样扣批次。精读：[`../../tracks/consensus/worked-example-quorum-store-vs-order.md`](../../tracks/consensus/worked-example-quorum-store-vs-order.md)。这和 STM 跑完≠最终（不变量 122）、谁写顺序（不变量 27）、进块≠接受（不变量 128）、抽样 α≠QC（不变量 131）不是同一句。
129. 若用可验时序钟再投票：必须点名问的是钟还是票（不变量 133）。PoH / 槽钟不是已经投票。`processed` 不是已经 confirmed。`confirmed` 不是已经 finalized / 已经 root。超多数票不是已经最大 lockout。第一版不要同时卖三套「到了」。不要抄槽秒数或官网 TPS。不要把 Alpenglow 计划写成已经切完。精读：[`../../tracks/consensus/worked-example-poh-vs-tower.md`](../../tracks/consensus/worked-example-poh-vs-tower.md)。这和 Gasper 三等（不变量 127）、BABE≠GRANDPA（不变量 126）、槽号≠块身份（不变量 94）、停机里的 Tower/PoH 已一致（不变量 85 / 86）不是同一句。
130. 若用 VRF 私下抽委员会：必须点名停在抽中、最低哈希、soft vote 还是 certify（不变量 134）。抽中不是已经认证。最低 VRF 提案不是已经 soft vote。Soft vote 不是已经落账。参与钥不是花费钥。按 Algo 抽签不是一人一票，也不是问邻居。第一版可以不上 VRF 委员会。不要抄超时或官网快慢句。精读：[`../../tracks/consensus/worked-example-vrf-sortition-vs-certified.md`](../../tracks/consensus/worked-example-vrf-sortition-vs-certified.md)。这和 Snow 抽样（不变量 131）、Altair 委员会（不变量 22）、NPoS 等权（不变量 129）、BABE 抽槽（不变量 126）不是同一句。
131. 若头上同时印较快确认和 BFT 最终：必须点名问的是哪一枚哈希、哪一条谓词、哪一档 RPC（不变量 135）。`last_ds_final_block` 不是已经 `last_final_block`。`near-final` / Doomslug 不是已经 `final` / 已经 Nomicon 两高度谓词。`optimistic` 不是已经不可逆。出新头不是已经 commit。第一版不要同时卖两枚头哈希。不要抄超时或秒数。精读：[`../../tracks/finality/worked-example-doomslug-vs-bft.md`](../../tracks/finality/worked-example-doomslug-vs-bft.md)。这和 BABE≠GRANDPA（不变量 126）、Gasper 三等（不变量 127）、PoH 三档（不变量 133）不是同一句。
132. 若共识热路径不跑 `Apply`：必须点名问的是官方顺序还是已经交差的状态（不变量 136）。顺序已定不是本块根已经交差。投票时可以还没执行。延迟 D 块根不是轻客户端能证 N。投机 `eth_call` 不是协议最终。第一版可以保持投票前先跑完。不要抄 `D` 或执行预算表。不要写 19 节。精读：[`../../tracks/consensus/worked-example-order-vs-state.md`](../../tracks/consensus/worked-example-order-vs-state.md)。这和 STM 跑完≠最终（不变量 122）、批次≠L（不变量 132）、谁写顺序（不变量 27）不是同一句。
133. 若留下并行块再线性化：必须点名问的是 DAG 成员、mergeset、蓝还是 selected chain（不变量 137）。进了某个块不是已经在 selected chain。并行块留下不是已经 orphan。蓝不是 QC。GHOSTDAG 不是 Avalanche 抽样。第一版不必上高块率 DAG。不要抄 BPS。精读：[`../../tracks/consensus/worked-example-dag-vs-selected-chain.md`](../../tracks/consensus/worked-example-dag-vs-selected-chain.md)。这和最重链孤块（L3.1）、Snow 抽样（不变量 131）、先定序再揭开（不变量 136）不是同一句。
134. 若当有效性租户或对照 ZK 绿勾：必须点名问的是 `CANDIDATE`、`PRE_CONFIRMED`、`ACCEPTED_ON_L2` 还是 `ACCEPTED_ON_L1`（不变量 138）。排序者回执不是已经共识最终。L2 accepted 不是已经 L1。验证明必须写出当前登记的 program hash（不变量 28）。有证明不是不需要状态差。第一版不要当别人的有效性租户。不要抄 TTL 或现行 hash。不要写 19 节。精读：[`../../tracks/finality/worked-example-l2-status-vs-l1.md`](../../tracks/finality/worked-example-l2-status-vs-l1.md)。这和两层 accepted 短句（不变量 28）、Gasper 三等（不变量 127）、PoH 三档（不变量 133）、Doomslug≠BFT（不变量 135）不是同一句。
135. 若用外链 BTC 当质押：必须点名问的是 Bitcoin 锁、k-deep 票权、解绑意图还是租户 commit（不变量 139）。UTXO 仍在 Bitcoin 不是已经 wrap。k-deep 包含证明不是已经 CometBFT commit。解绑意图不是已经 k-deep。浅重组不是已经恢复票权。契约连署不是没有第三人。第一版不要靠外链 BTC 当质押。不要抄 `k`。不要写 19 节。精读：[`../../tracks/economic/worked-example-btc-lock-vs-commit.md`](../../tracks/economic/worked-example-btc-lock-vs-commit.md)。这和 k 确认（L3.1）、证据≠slash（不变量 21）、中继质押（不变量 125）、EigenLayer restake 不是同一句。
136. 若把已有质押再声明给另一套服务：必须点名问的是 restake 声明、Unique Stake、AVS 自定罚还是 Casper / 证据形状（不变量 140）。AVS 罚没不是已经协议罚没。任何理由不是必须链上可证。restake 不是已经变成另一个信标最终。协议不提供否决。第一版不要把任意 AVS 再声明当默认模块。不要抄 TVL。不要写 19 节。精读：[`../../tracks/economic/worked-example-avs-slash-vs-casper.md`](../../tracks/economic/worked-example-avs-slash-vs-casper.md)。这和证据≠slash（不变量 21）、Casper 两票（不变量 26）、中继质押（不变量 125）、BTC 锁（不变量 139）不是同一句。
137. 若当乐观租户或对照同名 RPC 三档：必须点名问的是 `unsafe` / `latest`、能从当前 canonical L1 推导的 `safe`，还是能从 L1 已 finalized 部分推导的 `finalized`（不变量 141）。排序者出块不是已经从 L1 推导。OP `safe` 不是已经 `finalized`，也不是 Gasper justified。L2 `finalized` 不是桥已经兑付。Standard Bridge 等待不是 L2 交易还没 finalized。第一版不要当别人的乐观租户。不要抄秒数或桥等待天数。不要另写 19 节。精读：[`../../tracks/finality/worked-example-unsafe-vs-derived.md`](../../tracks/finality/worked-example-unsafe-vs-derived.md)。这和提交≠兑付（不变量 9）、Gasper 三等（不变量 127）、Starknet 四档（不变量 138）、PoH 三档（不变量 133）不是同一句。
138. 若对照委员会 DA：必须点名问的是父链全文、DACert，还是凑不齐签后的回退贴文（不变量 142）。DACert 不是全文已经贴上父链。AnyTrust 不是已经 Rollup DA。Inbox 收下证书不是子链已经读到数据。证书过期窗不是已经永存。第一版不要靠外部 DA 委员会。不要抄人数或过期天数。不要另写 19 节。精读：[`../../tracks/light-clients/worked-example-dacert-vs-posted.md`](../../tracks/light-clients/worked-example-dacert-vs-posted.md)。这和提交≠兑付（不变量 9）、短时 blob（不变量 23）、NMT/DAS（不变量 124）、OP 推导头（不变量 141）不是同一句。
139. 若对照 UTXO 访问集 / 声明调度：必须点名问的是谓词、脚本、只读重叠、写集相交还是顺序副作用（不变量 143）。谓词通过不是脚本已经跑完。只读重叠不是写冲突。写集相交不是可以并行。并行验证不是已经不需要顺序 L。`scriptLength == 0` 不是已经没有合约。第一版不要把短槽 + 声明调度当默认。不要抄上限或官网 TPS。不要另写 19 节。精读：[`../../tracks/parallelism/worked-example-utxo-access-list.md`](../../tracks/parallelism/worked-example-utxo-access-list.md)。这和 STM 跑完≠最终（不变量 122）、所有权快路径（不变量 128）、顺序≠状态（不变量 136）、认证批次（不变量 132）不是同一句。
140. 若提供未确认转发 / 费用市场：必须点名问的是策略、共识、费率还是本节点筐（不变量 144）。策略拒绝不是共识非法。策略通过不是已经进块。费率高不是更正确。策略不作用于块内交易。第一版必须把本地错 / 池拒绝 / 共识非法三套文案分开。不要抄默认费率。不要另写 19 节。精读：[`../../tracks/mempool/worked-example-policy-vs-consensus.md`](../../tracks/mempool/worked-example-policy-vs-consensus.md)。这和入池拒绝代价（不变量 44）、IBD 跳脚本（不变量 25）、洪水≠停（不变量 89）、谓词≠脚本（不变量 143）不是同一句。
141. 若挂短时大数据袋 / 对照 4844：必须点名问的是普通 gas、blob gas、versioned hash 还是 sidecar 字节（不变量 145）。blob gas 不是普通执行 gas。EVM 能读承诺不是已经读到袋里的字节。付了 blob fee 不是数据已经永存。执行层不负责持久化 blob。第一版不要把短时 blob 当默认 DA。不要抄上限或官网倍数。不要另写 19 节。精读：[`../../tracks/light-clients/worked-example-blob-fee-vs-gas.md`](../../tracks/light-clients/worked-example-blob-fee-vs-gas.md)。这和短时承诺≠永存（不变量 23）、策略≠共识（不变量 144）、提交≠兑付（不变量 9）、gas≠墙钟（不变量 101）不是同一句。
142. 若装 IBC / 对照跨链四层：必须点名问的是客户端、连接、通道还是数据包（不变量 146）。轻客户端不是已经开连接。连接不是已经开通道。通道不是已经送达数据包。发出承诺不是对岸已经 recv。第一版可以不装 IBC。不要把握手超时抄进不确定。不要另写 19 节。精读：[`../../tracks/economic/worked-example-ibc-client-vs-packet.md`](../../tracks/economic/worked-example-ibc-client-vs-packet.md)。这和 ack 确定性（不变量 77）、超时挂钩（不变量 78）、ICS-23 soundness（不变量 79）、提交≠兑付（不变量 9）、XCM（不变量 113）不是同一句。ICS-20 代币机见第 151 条。
143. 若抄 CometBFT 头 / 对照本头状态根：必须点名问的是本头 AppHash、本块 DataHash，还是本高度 FinalizeBlock 刚回的根（不变量 147）。本头 AppHash 不是本高度交易已经交差。本块 DataHash 有这笔不是效果已经进本头。本高度 Finalize 回的根不是已经印在本头。第一版若抄这套头，必须写清滞后一块。不要抄哈希宽度。不要另写 19 节。精读：[`../../tracks/consensus/worked-example-apphash-vs-this-block.md`](../../tracks/consensus/worked-example-apphash-vs-this-block.md)。这和四门（不变量 33）、快照锚（不变量 38）、轻验≠日程（不变量 56）、顺序≠状态（不变量 136）、集合延迟（不变量 35）不是同一句。
144. 若抄 CometBFT 头 / 对照块上的 Commit：必须点名问的是本头 LastCommit、本地 subjective commit，还是本高度要等下一块才印的那份（不变量 148）。本头 LastCommit 不是本高度已经 +2/3。本地那份不是已经 canonical。第一块空 LastCommit 不是已经没有最终。第一版若抄这套头，必须写清本块票是上一高度。不要抄票槽上限或超时秒数。不要另写 19 节。精读：[`../../tracks/consensus/worked-example-lastcommit-vs-this-block.md`](../../tracks/consensus/worked-example-lastcommit-vs-this-block.md)。这和其余槽位已签（不变量 65）、本头 AppHash（不变量 147）、timeout_commit（不变量 47）、锁（不变量 4）、BFT Time（不变量 40）不是同一句。
145. 若拆 EL/CL / 对照 Engine API：必须点名问的是处理一块、`POS_FORKCHOICE_UPDATED` 点名的头，还是同一事件里的 finalized（不变量 149）。处理完一块不是已经改规范头。没有该事件不是已经改 fork choice。事件里的 head 不是已经 finalized。禁止对头做乐观更新。第一版可以保持投票前先跑完、提交和头同一条路径。不要抄过渡总难度。不要另写 19 节。精读：[`../../tracks/finality/worked-example-processed-vs-forkchoice.md`](../../tracks/finality/worked-example-processed-vs-forkchoice.md)。这和通道尺寸（不变量 96）、Gasper 三等（不变量 127）、OP unsafe≠推导（不变量 141）、本头 AppHash（不变量 147）、多客户端同根（不变量 3）不是同一句。
146. 若做 eUTXO / 对照引用输入：必须点名问的是花费、引用，还是花费条件（不变量 150）。引用输入不是已经花费。看见 datum / 值不是已经检查花费条件。同一枚不得既花又引用。被引用输出通过后仍在 UTXO。第一版可以不做 eUTXO / 引用输入。不要抄字段号。不要另写 19 节。精读：[`../../tracks/state-models/worked-example-refinput-vs-spent.md`](../../tracks/state-models/worked-example-refinput-vs-spent.md)。这和谓词≠脚本（不变量 143）、所有权快路径（不变量 128）、占用（不变量 15）、策略≠共识（不变量 144）不是同一句。
147. 若上 Move / 对照资源能力：必须点名问的是 `copy`、`drop`、`store` 还是 `key`（不变量 151）。`store` 不是已经是顶层资源。`key` 不是模块外谁都能 `move_to`。结构体写了 `has copy` 不是这个实例能复制。字段是整数不是外层资源能复制。第一版可以不上 Move。不要另写 19 节。精读：[`../../tracks/state-models/worked-example-ability-vs-resource.md`](../../tracks/state-models/worked-example-ability-vs-resource.md)。这和所有权快路径（不变量 128）、STM（不变量 122）、占用（不变量 15）、谓词≠脚本（不变量 143）、引用≠花费（不变量 150）不是同一句。
148. 若把大签放进旧节点不理解的附件 / 对照 SegWit：必须点名问的是 txid、wtxid，还是头上的 txid Merkle（不变量 152）。txid 不是 wtxid。改见证不是已经改交易身份。头上的 txid Merkle 不是已经承诺 wtxid。旧节点看见 txid 不是已经验过见证。第一版必须写清哪一个 ID 承诺了附件。不要抄重量公式。不要另写 19 节。精读：[`../../tracks/implementation/worked-example-txid-vs-wtxid.md`](../../tracks/implementation/worked-example-txid-vs-wtxid.md)。这和策略≠共识（不变量 144）、同根不同列表（不变量 12）、多客户端同根（不变量 3）、跳脚本（不变量 25）、blob 承诺≠字节（不变量 145）不是同一句。
149. 若做「一个输出、多条条件」/ 对照 Taproot：必须点名问的是钥匙路径、脚本路径，还是链上那个输出（不变量 153）。钥匙路径不是已经揭开有没有脚本树。脚本路径不是已经揭开全部脚本。看见 Taproot 输出不是已经分辨付款给钥还是付款给脚本。第一版可以不上 Taproot / MAST。不要抄控制块长度或叶子版本。不要另写 19 节。精读：[`../../tracks/implementation/worked-example-keypath-vs-scriptpath.md`](../../tracks/implementation/worked-example-keypath-vs-scriptpath.md)。这和 txid≠wtxid（不变量 152）、策略≠共识（不变量 144）、同根不同列表（不变量 12）、跳脚本（不变量 25）、BTC 锁≠commit（不变量 139）不是同一句。
150. 若让共识往执行推余额 / 对照信标提款：必须点名问的是系统操作、用户交易，还是共识层出队（不变量 154）。提款操作不是用户交易。信标链出队不是执行账户已经加钱。无 gas / 不得失败不是已经跑过 EVM。第一版可以保持一条路径、不发明 CL 推送操作。不要抄每块条数。不要另写 19 节。精读：[`../../tracks/economic/worked-example-withdrawal-vs-tx.md`](../../tracks/economic/worked-example-withdrawal-vs-tx.md)。这和处理≠改头（不变量 149）、提交≠兑付（不变量 9）、blob 费≠执行气（不变量 145）、L2 finalized≠桥兑付（不变量 141）、顺序≠状态（不变量 136）不是同一句。
151. 若做同质跨链 / 对照 ICS-20：必须点名问的是托管、铸券、烧掉还是解锁（不变量 155）。源链托管不是对岸已经铸券。对岸券不是源链已解锁的原币。带端口/通道前缀的 denom 不是原来的 denom。超时退款不是对岸已经有可花余额。send 包发出不是对岸已经 recv 并铸券。A→B→D 不是已经能走 D→C→A 赎回。第一版可以不装 IBC / ICS-20。不要抄通道版本或实现仓库版本。不要另写 19 节。精读：[`../../tracks/economic/worked-example-escrow-vs-voucher.md`](../../tracks/economic/worked-example-escrow-vs-voucher.md)。这和客户端≠数据包（不变量 146）、ack 确定性（不变量 77）、超时挂钩（不变量 78）、ICS-23（不变量 79）、提交≠兑付（不变量 9）、提款≠交易（不变量 154）、XCM（不变量 113）不是同一句。
152. 若把共识根暴露进执行 VM / 对照信标根进 EVM：必须点名问的是父信标根、当前头，还是 finalized（不变量 156）。头里的父根不是当前信标头。合约里读到的根不是已经 finalized。环缓冲过期不是根已经永久可查。`BLOCKHASH` 不是已经改成信标根。第一版可以不把共识根暴露进执行 VM。不要抄环长或分叉时间戳。不要另写 19 节。精读：[`../../tracks/light-clients/worked-example-parent-root-vs-head.md`](../../tracks/light-clients/worked-example-parent-root-vs-head.md)。这和提款≠交易（不变量 154）、处理≠改头（不变量 149）、head≠justified≠finalized（不变量 127）、弱主观检查点（不变量 24）、blob 承诺≠字节（不变量 145）不是同一句。
153. 若把共识随机暴露进执行 VM / 对照 PREVRANDAO：必须点名问的是工作量、上一块 mix，还是应用公平（不变量 157）。合并后的 `difficulty` 不是工作量。`PREVRANDAO` 不是本块刚掷的骰子。信标 RANDAO 不是应用级无偏随机。历史 mix 不是不可预测。第一版可以不把共识随机暴露进执行 VM。不要抄阈值或前瞻 epoch。不要另写 19 节。精读：[`../../tracks/crypto/worked-example-prevrandao-vs-difficulty.md`](../../tracks/crypto/worked-example-prevrandao-vs-difficulty.md)。这和父根≠头（不变量 156）、处理≠改头（不变量 149）、确定性（不变量 3）、DKG（不变量 93）、VRF 抽签（不变量 134）不是同一句。
154. 若做费用市场 / 对照 EIP-1559：必须点名问的是基础费、小费，还是弹性上限（不变量 158）。基础费不是已经给了出块者。弹性块大小不是整套费用市场已经齐。烧掉不是 MEV 已经解决。`GASPRICE` 不是出块者实收。第一版可以不抄烧掉基础费的市场。不要抄倍数。不要另写 19 节。精读：[`../../tracks/mempool/worked-example-basefee-vs-tip.md`](../../tracks/mempool/worked-example-basefee-vs-tip.md)。这和 blob 费≠执行气（不变量 145）、Bitcoin base fee（不变量 144）、gas≠墙钟（不变量 101）、谁写列表（不变量 27）不是同一句。
155. 若做交易级草稿 / 对照瞬时存储：必须点名问的是瞬时店、持久店，还是 memory（不变量 159）。`TSTORE` 不是已经进账户。本笔结束丢掉不是本笔里从未存在。同合约各帧共用一份不是 memory。帧回滚不是已经落盘。第一版可以不上瞬时存储指令。不要抄气价。不要另写 19 节。精读：[`../../tracks/state-models/worked-example-transient-vs-storage.md`](../../tracks/state-models/worked-example-transient-vs-storage.md)。这和 OOG 回滚（不变量 103）、内层可见性（不变量 118）、委托信任（不变量 119）、脚本无持久存储（不变量 143）、Move `store`（不变量 151）不是同一句。

**以后再发明**

- 通用 VM、STM、短槽切块传播。  
- 完整屏蔽池。  
- 递归证明链。  
- 作为别人的 DA 房东或执行租户。

**永远不要发明（建议，可在记录里反驳）**

- 用官网 TPS 当安全。  
- 管理员钥改余额而无时锁与审计。  
- 把 RPC 绿勾当协议最终。  
- 自研未经评审的「新型密码」。  
- 无 DA 的「头即结算」。  
- 把「形式化过」写成实现与 `Apply` 已正确。  
- 两个角色共用空 `ctx` 还宣称已经域分离。  
- 把「顺序已最终」写成「余额已到」（共识若先定序、后 Apply）。  
- 把抽样委员会 2/3 写成全验证者 2/3。  
- 把 restake / AVS 自定罚没写成和 Casper / CometBFT 协议罚没同一对象。  
- 把 KZG / versioned hash 写成纠删抽样 DAS，或把短时 blob 当成永存档案室。  
- 把过期检查点或「PoS 已最终」写成和从创世复算同一安全。  
- 把跳过脚本或 UTXO 重放的同步写成「已从创世全验证」。  
- 把任意两张验证者签写成已经可罚，或不写谁执行 slash。  
- 把域外 Builder API 写成信标共识，或把签了盲头写成提议者选过每一笔。  
- 把 L2 accepted 写成 L1 已更新 / 可提款，或把有效性证明写成与程序哈希无关的物理定律。  
- 把实现调整钟拒块写成共识改了 MTP。  
- 把本节点看不见未确认交易写成链拒绝。  
- 把廉价头写成可以无界入库，或把检查点当成已经解决头垃圾。  
- 把不可中断的孤儿扫描写成节点仍活着 / 已同步。  
- 把 CheckTx / Prepare / Process 写成已结算或 PBS，或把 Process REJECT 当成没有活性代价的过滤器。  
- 把 vote extension 验收失败写成块非法，或把本高度 Finalize 写成依赖本高度收到的扩展。  
- 把 H 的验证者更新写成下一高度立刻按新名单计票。  
- 把对等节点宣布了新块写成已经收到 / 链已非法。  
- 把部分重建失败后的断言崩溃写成共识拒绝了非法块。  
- 把应用快照同步写成从创世重放，或把 snapshot.hash 写成轻验 AppHash。  
- 把未请求的变异块写成已经处理完这块，或让一个对等节点清掉别人的下载状态。  
- 把 PBTS 写成 MTP / BFT Time 中位数 / 墙上现在，或把不 timely 写成块非法 / 已 slash。  
- 把 Bitcoin 的太早、locktime、太新写成同一把 MTP，或把 locktime 写成创世就看中位。  
- 把「块已非法」写成磁盘已经安全，或让拒绝路径无上限打日志。  
- 把提前 return 写成后台验签已经汇合，或把崩溃写成共识已安全拒块。  
- 把非标准 / CheckTx 拒绝写成已经免费或已经断开。  
- 把 INV / GETDATA / 待宣布写成同一个免费开关，或把单连接空转写成全节点已死。  
- 把默认证据窗写成已经盖住解绑，或把过期写成高度或时间。  
- 把 `timeout_commit` 写成还没最终 / 全网必须同一秒数，或把 `skip_timeout_commit` 写成第三种最终性。  
- 把最大序列化消息长度写成每连接接收 RAM 已经有上限。  
- 把插入限速写成递增 ID 不会回绕，或把 v22 限速写成 overflow 已消失。  
- 把「行为不好就 ban」写成惩罚表已经有界，或让自动惩罚写入可枚举无界 map。  
- 把 32-bit 内存池旋钮写成尺寸检查已经固定宽度，或让 32-bit 与 64-bit 对同一对象意见不同。  
- 把 `next_block_delay` 写成全网槽位 / 第三条最终性 / 已复制参数，或把 `main` 规范写成所有发布线都有该字段。  
- 把默认关 UPnP 写成节点没在验证，或把局域网打洞辅助写成和互联网 P2P 同一攻击面。  
- 把因余额不足取消写成已经不再扣款，或把一种取消理由的临时补丁写成下溢已消失。  
- 把 DKG 按设计关掉写成重启后还记得，或把一次强制关纪元写成常备能力。  
- 把槽号 / 高度写成块身份，或把乐观确认写成已经 rooted。  
- 把证明程序验绿写成不可铸 / 不可偷，或把应用层未改写成证明层已齐。  
- 把单笔低于入池上限写成拼块已被所有客户端接受，或把各家 RPC 收到同一低值写成许多小交易不能顶满。  
- 把交易解码深度有界写成 runtime API 再解整块已安全，或把导入失败写成邻居已经作恶。  
- 把组下标写成票向量下标，或把 create_inherent 回 None 写成客户端已报错。  
- 把 Active 争议写成已经 Confirmed，或把禁用测试绿写成最终性已绿。  
- 把链下内存禁用写成已确认争议已经不参与，或把训练轮触发写成最终性还在走。  
- 把块 gas 上限写成墙钟已有界，或把状态访问的常数 gas 写成磁盘已是 O(1)。  
- 把电路实现写成已经写明的陈述，或把旧验证钥过验写成新电路已安全。  
- 把 out-of-gas 结束写成空账户删除已经回滚。  
- 把重复头复位跟踪写成闸门还在转，或把 ZIP 209 写在规范里写成实现字段仍有效。  
- 把反序列化归一化成零写成编码必须为零，或把检查跑在改写后的字段上写成规则已经开火。  
- 把体可变拒绝先于授权承诺写成头已经绑死，或把诚实头写进永久非法表写成块已经非法。  
- 把规范允许身份 `rk` 写成验证明已经能吃，或把公开输入转换恐慌写成电路不支持零点。  
- 把一家收下无效 `ephemeralKey` 写成规范已经允许，或把与 `rk` 同曲线写成同一对象。  
- 把 coinbase 正屏蔽余额写成供给已经对齐，或把 `ConnectBlock` 对不上写成重启能起来。  
- 把改冻结门槛写成选举地板已经配对，或把出块还在写成纪元已经转。  
- 把从文件加载钱包写成出站 TXID 已经不泄漏，或把 trusted 标记写成这条 RPC 已经检查。  
- 把 privatebroadcast 开关写成 IP 已经不暴露，或把 v2 失败后的 v1 重连写成仍走代理。  
- 把 `preserve_origin` 写成出站已经带了改 origin 的指令，或把静默跳过写成 BadOrigin。  
- 把废弃 runtime API 还在写成返回编码已经兼容，或把整理者还能写块写成中继已经收到。  
- 把 StateDB 可花写成锁定已经从同一笔写回排除，或把回绕后的数写成银行账已经对齐。  
- 把子群检查写成点已经在曲线上，或把原生预编译加速写成两家已经同根。  
- 把预编译中途出错写成 SDK 已写入已经撤回，或把领奖转出写成可领已经清零。  
- 把内层预编译改过账写成外层已经看见，或把关掉预编译写成嵌套写回已经齐。  
- 把正确兑现的 `DELEGATECALL` 语义写成预编译信任模型已经跟着改过，或把库换了正确语义写成旧假设已经更新。  
- 把迁移失败写成目录里其它钱包已经安全，或把现有用户不受影响写成迁移路径已经安全。  
- 把插入路径的检查加法写成心跳加余量已经安全，或把解析当时没崩写成心跳不会崩。  
- 把 STM 跑完写成已经最终，或把未事先声明写集写成已经不需要 L。  
- 把区块链 SNARK 验绿写成最新 staged 已经被证明，或把 Pickles 写成 Kimchi，或把 22kB 写成账户库。  
- 把 NMT 命名空间齐了写成扩展方阵已经可用，或把 DAS 抽样过关写成已经拿到自己的 blob / 编码已经诚实 / 历史已经有人存。  
- 把 backed 写成已经可用 / 已经有效 / 已经最终，或把中继头有回执写成 PoV 在链上。  
- 把 BABE 出块写成已经 GRANDPA 最终，或把最长链写成 hybrid 的分叉选择，或把 BEEFY 绿写成已经解释了 GRANDPA。  
- 把出块 / justified / RPC `safe` 写成已经 finalized，或把 `safe` 写成官方已经等于 justified。  
- 把单地址所有写成已经走快路径，或把引用 shared 写成已经授权，或把进共识块写成这笔已被接受。
- 把 NPoS 当选写成共识已经按质押加权，或把 ⅔ 质押写成官方链投票已经过，或把 BABE 按质押抽槽写成 GRANDPA 也按质押，或把提名写成治理权已经交出。
- 把终局推迟写成高度已经停，或把 inactivity leak 写成已经 slash，或把两边都 leak 到 finalized 写成协议已经选出唯一链。
- 把抽样 α 多数写成全集 +2/3 证书，或把连续 β 轮写成可转发 QC，或把出块窗写成已经决定，或把「也是 BFT」写成已经和 CometBFT 同一把尺子。
- 把 Quorum Store 传开写成已经写出 L，或把已认证批次写成已经排序 / 已经 commit，或把去掉领袖瓶颈写成已经没有领袖，或把进了提议块写成已经落盘。
- 把 PoH / 槽钟写成已经投票或已经 BFT，或把 `processed` 写成已经不可逆，或把 `confirmed` 写成已经 `finalized` / 已经 root，或把 Alpenglow 计划写成现行已经切完。
- 把 VRF 抽中写成已经认证，或把最低 VRF 提案 / soft vote 写成已经落账，或把抽签写成问邻居，或把参与钥写成花费钥。
- 把 `last_ds_final_block` / `near-final` / Doomslug 写成已经 BFT 最终或已经 `final`，或把出新头写成已经 commit。
- 把官方顺序已定写成本块状态根已经交差，或把投机 `eth_call` 写成协议最终，或把延迟根写成能证高度 N。
- 把进了 DAG 块写成已经在 selected chain 或已经最终，或把并行块写成已经 orphan，或把蓝写成 QC，或把 GHOSTDAG 写成 Avalanche。
- 把 `CANDIDATE` / `PRE_CONFIRMED` 写成已经 `ACCEPTED_ON_L2`，或把 `ACCEPTED_ON_L2` 写成已经 `ACCEPTED_ON_L1` / 可提款，或把验证明写成与当前 program hash 无关的物理定律。
- 把仍在 Bitcoin 的 UTXO 写成已经 wrap，或把 k-deep 包含证明写成已经租户 commit，或把解绑意图写成已经 k-deep / 浅重组能恢复票权。
- 把 AVS 按任何理由罚写成 Casper / 协议罚没，或把 restake 写成已经变成另一个信标最终，或把协议写成已经提供否决。
- 把 OP `unsafe` / RPC `latest` 写成已经从 L1 推导，或把 OP `safe` 写成已经 `finalized` / 已经 Gasper justified，或把桥等待写成 L2 交易还没 finalized。
- 把 AnyTrust DACert 写成全文已经贴上父链，或把 AnyTrust 写成已经 Rollup DA / 已经 DAS，或把凑不齐签回退写成已经只走委员会。
- 把谓词通过写成脚本已经跑完，或把只读访问集重叠写成必须串行，或把写集相交写成可以并行，或把并行验证写成已经不需要顺序 L。
- 把策略拒绝写成共识非法，或把费率高写成更正确，或把策略写成已经作用于块内交易。
- 把 blob gas 写成普通执行 gas，或把 `BLOBHASH` 写成已经读到 sidecar 字节，或把付了 blob fee 写成数据已经永存。
- 把 IBC 轻客户端写成已经开连接，或把连接写成已经开通道，或把 `sendPacket` 写成对岸已经 recv。
- 把本头 AppHash 写成本高度交易已经交差，或把本块 DataHash 有这笔写成效果已经进本头，或把 FinalizeBlock 刚回的根写成已经印在本头。
- 把本头 LastCommit 写成本高度已经 +2/3，或把本地 subjective commit 写成已经是链上 canonical，或把第一块空 LastCommit 写成已经没有最终。
- 把执行层刚跑完一块 / Engine API `VALID` 写成已经改规范头，或把 `POS_FORKCHOICE_UPDATED` 里的 head 写成已经 finalized，或对头做乐观更新。
- 把引用输入写成已经花费，或把脚本看见 datum / 值写成已经检查花费条件，或把同一枚输出写成可以既花又引用。
- 把 `store` 写成已经是顶层资源，或把结构体写了 `has copy` 写成这个实例能复制，或把整数字段写成外层资源能复制。
- 把 txid 写成已经含见证，或把改见证写成已经改交易身份，或把头上的 txid Merkle 写成已经承诺 wtxid。
- 把钥匙路径写成已经揭开有没有脚本树，或把脚本路径写成已经揭开全部脚本，或把看见 Taproot 输出写成已经分辨付款给钥还是付款给脚本。
- 把提款操作写成用户交易，或把信标链出队写成执行账户已经加钱，或把无 gas / 不得失败写成已经跑过 EVM。  
- 把源链托管写成对岸已经铸出原币，或把对岸券写成源链已经解锁，或把带通道前缀的 denom 写成原来的名字。  
- 把头里的父信标根写成当前信标头，或把合约里读到的根写成已经 finalized，或把环缓冲写成永存。  
- 把合并后的 `difficulty` 写成工作量，或把 `PREVRANDAO` 写成本块刚掷的公平骰子，或把信标 RANDAO 写成应用级无偏随机。  
- 把基础费写成已经给了出块者，或把弹性块大小写成整套费用市场已经齐，或把烧掉写成 MEV 已经解决。  
- 把 `TSTORE` 写成已经进账户，或把交易结束丢掉写成本笔里从未存在，或把同合约共用一份瞬时店写成 memory。

---

## E. 最小案例

实验网用户问：「支持智能合约吗？」  
正确回答：「第一版不支持。这是为了让状态根与测试集保持可审计。合约是以后的候选，见决策记录。」  
错误回答：「支持，和以太坊一样，而且更快、还后量子。」

---

## F. 真实项目

对照偷：Bitcoin 的小规则；CometBFT 的锁与 ABCI；Ethereum 的同根纪律。  
对照不偷：各家吞吐广告、隐私口号、模块化叙事。

---

## G. 源码入口

未来 `uncertain` 仓库应以 `Apply`、共识适配、测试向量开头。现不存在则不编路径。

---

## H. 攻击者模型

- 用功能列表逼项目变世界计算机。  
- 用「缺功能」攻击融资叙事，从而破坏纪律。

---

## I. 代价

第一版难卖。  
这是教学与工程的共同选择：先能复算，再谈独特。

---

## J. 对「不确定」的意义

本课是目的 B 的收口。目的 A（用户真懂）用 L0–L9 服务。  
两者冲突时：宁可不写功能，也不写假保证。

---

## 精密检查

| 层 | 本课钉在哪 |
|---|---|
| 密码学 | 清单要求敏捷 + 分域，不选 OID |
| 协议 | 一百五十五条是建议最小机，不是已选 CometBFT + 账户 |
| 实现 | 必须留下第二个实现能对上的位置 |
| 部署 | 默认全节点验证 |
| 经济 | 占用白名单；一次费 ≠ 永存 |

**禁止假学习：** 「最小结算机 = 已经选型 CometBFT + 账户。」  
**边界：** 清单是建议。矩阵列仍空。
