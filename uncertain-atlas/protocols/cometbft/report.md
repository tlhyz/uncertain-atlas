# CometBFT（Tendermint 家族）· 19 节档案（第一版）

前身常称 Tendermint Core。CometBFT 是其延续实现。细节以当前 CometBFT 规范与仓库为准；本版先钉状态机与锁，不写 IBC 生态。

---

## 1. 一句话定义

一组有投票权的验证者，在同一高度上走 Propose → Prevote → Precommit，用 +2/3 投票权和锁规则，commit **一个**块；应用通过 ABCI 执行 `Apply`，共识引擎不懂余额。

---

## 2. 它解决的问题

Nakamoto 的病（对某些应用）：最终性是概率的，商家要猜确认数；出块期望间隔长。

经典「投个票过 2/3 就完事」的病：说谎者可以让两个值都看起来过门槛，或让节点投出矛盾历史。

Tendermint 要：确定最终、应用可插拔、崩溃可恢复。

---

## 3. 架构图

```text
钱包 / 应用客户端
        ↓
应用节点 RPC
        ↓
mempool（应用 CheckTx + 引擎）
        ↓
proposer 组 raw 块 → PrepareProposal（应用可改序/增/删）
        ↓
ProcessProposal（验收，不能改；REJECT ⇒ prevote nil）
        ↓
+2/3 prevote / precommit
        ↓
Commit  →  ABCI FinalizeBlock / Commit
        ↓
应用状态 + 引擎 WAL
        ↓
该高度确定最终（除非安全假设破）
```

---

## 4. 一笔交易完整生命周期

1. 用户对**应用**的交易字节签名（不是对 CometBFT 投票消息）。  
2. 经 RPC 进某节点 mempool；`CheckTx` 是应用说「现在看起来行」，仍可能被 Prepare 拿掉，或在 Finalize 时失败。  
3. 本轮 proposer 从池取 raw 列表；`PrepareProposal` 可改序/增/删（有 `validValue` 则跳过）。见 [`../../tracks/consensus/worked-example-prepare-process.md`](../../tracks/consensus/worked-example-prepare-process.md)。未处理的证据优先于内存池交易；两条收交易上限不是已经同一条：见 [`../../tracks/consensus/worked-example-evidence-vs-reap.md`](../../tracks/consensus/worked-example-evidence-vs-reap.md)（不变量 299）。提案收了不是已经从池里删掉；本块已 commit 不是已经不用再验剩下的：见 [`../../tracks/mempool/worked-example-proposed-vs-removed.md`](../../tracks/mempool/worked-example-proposed-vs-removed.md)（不变量 301）。  
4. 验证者 `ProcessProposal` 验收（不能改）。REJECT 走 prevote `nil`。  
5. 对 proposal 的块哈希 prevote / precommit。  
6. +2/3 precommit 后 commit。  
7. 应用按确定顺序执行（`FinalizeBlock` + `Commit`）。  
8. 状态哈希进下一轮。  
9. 该高度不应再换块。用户仍可能连到撒谎的 RPC——那是部署/用户层。

---

## 5. 状态模型

**引擎状态：** height、round、step、locked value、valid value、验证者集合与投票权。  
**应用状态：** 任意。Cosmos SDK 常用账户模型，但那不是 CometBFT 的要求。

这是最值钱的分离：**共识不拥有「钱怎么记」的解释权。**

本地 `State` 对象不是已经进了块，也不是已经流言：见 [`../../tracks/implementation/worked-example-state-vs-gossip.md`](../../tracks/implementation/worked-example-state-vs-gossip.md)（不变量 300）。头上的根不是已经有了 State 对象本身。能读本地 State 不是已经进了规范。

创世里的 `app_state` 不是已经验过应用状态；节点起来不是已经过了 `genesis_time`：见 [`../../tracks/implementation/worked-example-genesis-vs-app.md`](../../tracks/implementation/worked-example-genesis-vs-app.md)（不变量 303）。空 `validators` 不是已经没有集合。

---

## 6. 共识

高度 `h` 一个块。每轮有 proposer。步骤：propose、prevote、precommit。

**+2/3：** 投票权，不是人头。任意两个 +2/3 集合相交超过 1/3，因此在 <1/3 投票权拜占庭时，交点含诚实者（事实：标准 n=3f+1 论证）。

**锁：** 一旦在某轮对值 v 发出可被当作依据的 precommit/锁定，不能随便再给 v' 投票，除非规则允许的解锁（例如看到更高轮的新合法证明）。没有锁，「过 2/3」会回到 L0.6 的左右说谎。

**超时：** 部分同步下用**本地**超时换轮，保活性。超时太短会空转，太长会卡。这些数字不是共识参数，也不是最终性。`timeout_commit` 是已经 Commit 之后、开新高度之前再收迟到 precommit。`skip_timeout_commit=true` 的官方语义是「像 TimeoutCommit=0」——某条发布线还列不列该键，不改变「零等待仍是 commit 之后」这句话。见 [`../../tracks/consensus/worked-example-timeouts.md`](../../tracks/consensus/worked-example-timeouts.md)。较新的 `main` 规范把这段等待交给应用回 `next_block_delay`（非确定性，不是槽位，不是所有发布线都有）。见 [`../../tracks/consensus/worked-example-next-block-delay.md`](../../tracks/consensus/worked-example-next-block-delay.md)。不要抄文档示例秒数或「大约每秒一个空块」当结算 SLA。

**确定性最终：** commit 的 `(h, block)` 不应被诚实节点改掉。分区过久：可能停（保安全），而不是两边各 commit 各的。本块 `LastCommit` 是上一块的 canonical +2/3，不是本高度已经盖章；本地看见的那份不必等于链上那份。见 [`../../tracks/consensus/worked-example-lastcommit-vs-this-block.md`](../../tracks/consensus/worked-example-lastcommit-vs-this-block.md)（不变量 148）。

**块时间（必须点名）：** 家族里至少两套算法，都不是墙上现在，也不是 Bitcoin MTP。PBTS：提议者本地钟 + 相对收到 `Proposal` 的 timely 窗；不 timely → prevote `nil`。BFT Time：本块时间是上一高度 `LastCommit` 时间戳的加权中位数，可复算。规范态度是新链用 PBTS，BFT Time **可能**弃用——不是已经弃用。能复算 ≠ 故障者不能抬高 Time（[CSA-2026-001](../../tracks/failure-museum/csa-2026-001.md)）。见 [`../../tracks/consensus/worked-example-pbts.md`](../../tracks/consensus/worked-example-pbts.md)。

完整锁表是 Level 4 的深课。本档案先禁止简化成「投票过 2/3」。

---

## 7. 执行

在应用进程。ABCI 2.0 方法：`CheckTx`、`PrepareProposal`、`ProcessProposal`、`ExtendVote` / `VerifyVoteExtension`、`FinalizeBlock`、`Commit`。扩展见 [`../../tracks/consensus/worked-example-vote-extension.md`](../../tracks/consensus/worked-example-vote-extension.md)。

引擎保证：同一高度同一**已决定**交易列表，按序交给 `FinalizeBlock`。  
Prepare 可以不确定；Process 与 Finalize 必须确定。立即执行只能写候选状态。  
应用必须：相同已决定输入 → 相同状态哈希，否则下一轮共识对不上（实现保证）。

---

## 8. 网络

gossip 共识消息、块、交易。验证者集合已知，和 Bitcoin 的无许可洪水不同。

投票消息在委员会大或签名大时会炸带宽——后量子投票的关键乘法器。

---

## 9. 存储

WAL：先记「我要投什么」，再投票，防崩溃后投出矛盾票。写下每条消息不是已经 fsync；回放时又要签不是已经双签：见 [`../../tracks/implementation/worked-example-wal-vs-signed.md`](../../tracks/implementation/worked-example-wal-vs-signed.md)（不变量 298）。  
应用自己的数据库必须与高度原子对齐。断电半写是部署/实现经典坑。  
本头 `AppHash` 是上一块执行并提交之后的应用根，不是本高度交易已经交差。见 [`../../tracks/consensus/worked-example-apphash-vs-this-block.md`](../../tracks/consensus/worked-example-apphash-vs-this-block.md)（不变量 147）。

State sync：装应用快照、不重放历史块；只有轻验 `AppHash` 可信。见 [`../../tracks/implementation/worked-example-statesync.md`](../../tracks/implementation/worked-example-statesync.md)。

---

## 10. 密码学 primitive

| 零件 | 用途 |
|---|---|
| 验证者签名（常为 Ed25519 等） | 投票、proposal |
| 哈希 | 块 ID、状态哈希 |
| 应用层签名 | 用户交易，引擎不当作共识票 |

算法可换，但消息域必须把 vote 和 tx 分开。  
SignBytes 是 `CanonicalVote`（type / height / round / block_id / timestamp / chain_id），不是块内 Vote 的普通编码。见 [`../../tracks/consensus/worked-example-vote-signbytes.md`](../../tracks/consensus/worked-example-vote-signbytes.md)。票或提案带了 Timestamp 不是已经验过这个时间；冲突提案不是已经有证据：见 [`../../tracks/consensus/worked-example-vote-ts-vs-checked.md`](../../tracks/consensus/worked-example-vote-ts-vs-checked.md)（不变量 304）。

---

## 11. 安全假设

| 假设 | 失效 |
|---|---|
| 拜占庭投票权 < 1/3 | 可双最终或永久停，视攻击 |
| 部分同步最终成立 | 只有安全、没有活性 |
| 应用确定性 | 验证者状态根分裂 |
| 时钟/超时大致可用 | 活性变差；PBTS 另加 `PRECISION` / `MSGDELAY`，估小了可能卡在一高度 |
| 验证者密钥未批量泄漏 | 经济/部署层被接管 |

没有「多数算力」假设。有「验证者集合如何产生」的外层（PoS 质押等），那是应用/经济。

---

## 12. 最大结构性优势

**确定最终 + 应用/共识分离。**  
结算语义干净；「不确定」可以换执行、换用户签名算法，而不必重写投票状态机——若你们守住 ABCI 边界。

---

## 13. 最大具体缺陷

1. 验证者集合是政治与经济对象，不是无许可挖矿。  
2. 分区或 >1/3 掉线/作恶时，倾向停机。  
3. 投票流量随委员会和签名体积线性（或更差）增长。  
4. proposer 审查：能拖交易，尽管不能轻易双花已 commit 的。  
5. 实现复杂：锁、WAL、证据、集合变更高度。

---

## 14. Trade-off

| 得到 | 换 |
|---|---|
| commit 后不改 | 分区停机 |
| 秒级到块级最终（视配置） | 固定委员会、同步假设 |
| 应用可插拔 | 应用写不确定就全网裂 |
| 明确投票权 | 质押集中、审查卡特尔（经济） |

---

## 15. 历史事故

Tendermint/Cosmos 生态有过停机、安全漏洞与应用层事故。第一版不拿传闻填满。  
已收官方咨询：[ASA-2024-004](../../tracks/failure-museum/asa-2024-004.md) — 默认证据窗可能短于解绑，无代码补丁。  
已收：[ASA-2024-009](../../tracks/failure-museum/asa-2024-009.md) — 轻验集合对上 ≠ 提议者选择已对齐。  
已收：[ASA-2024-011](../../tracks/failure-museum/asa-2024-011.md) — 扩展快路径跳过普通票的发送者下标检查。  
已收：[ASA-2024-001](../../tracks/failure-museum/asa-2024-001.md) — 治理改扩展启用高度，验证写错则 panic 停链。  
已收：[ASA-2025-002](../../tracks/failure-museum/asa-2025-002.md) — 分片外层下标必须等于证明下标。  
已收：[ASA-2025-003](../../tracks/failure-museum/asa-2025-003.md) — 位图结构必须先验再传，否则最坏停网。  
已收：[CSA-2026-001](../../tracks/failure-museum/csa-2026-001.md) — Tachyon：验 commit 与推导 Time 路径不一致。Critical。  
已收：[ASA-2025-001](../../tracks/failure-museum/asa-2025-001.md) — blocksync 目标高度必须可归因且可回退。  
已收：[ASA-2023-002](../../tracks/failure-museum/asa-2023-002.md) — 仓库默认 MaxBytes 不是第一轮活性 SLA。  
已收前身：[CVE-2021-21271 / Mulberry](../../tracks/failure-museum/cve-2021-21271.md) — 飞行中的 last commit 不是证据身份。  
已收前身：[CVE-2020-15091 / Syringa](../../tracks/failure-museum/cve-2020-15091.md) — +2/3 不是其余槽位已签。  
已收前身：[Alderfly](../../tracks/failure-museum/alderfly.md) — 验过头不是已经能交证据；朝前 lunatic。  
已收前身：[CVE-2020-5303 / Lavender](../../tracks/failure-museum/cve-2020-5303.md) — 握手请求不是已接受的邻居。InitPeer 不是已经能跟它对说；Receive 不是已经 AddPeer：见 [`../../tracks/network/worked-example-initpeer-vs-addpeer.md`](../../tracks/network/worked-example-initpeer-vs-addpeer.md)（不变量 305）。Peer 句柄不是已经是那个人；Broadcast 回了通道不是已经送到；StopPeerForError 不是已经对持久邻居也断干净：见 [`../../tracks/network/worked-example-peer-handler-vs-node.md`](../../tracks/network/worked-example-peer-handler-vs-node.md)（不变量 306）。NumPeers 不是已经数完所有邻居；按名字拿到反应堆不是已经独立；PeerState 不是已经验过高度：见 [`../../tracks/network/worked-example-numpeers-vs-all.md`](../../tracks/network/worked-example-numpeers-vs-all.md)（不变量 308）。HasChannel 为真不是已经入队；Send 回了假不是已经断开；TrySend 回了假不是已经和 Send 同一把尺：见 [`../../tracks/network/worked-example-send-vs-enqueued.md`](../../tracks/network/worked-example-send-vs-enqueued.md)（不变量 309）。  
已收应用侧：[ASA-2024-006](../../tracks/failure-museum/asa-2024-006.md) — Cosmos SDK 默认助手从提议者注入的扩展推断投票权；不是引擎保证。  
已收应用侧：[ASA-2024-002](../../tracks/failure-museum/asa-2024-002.md) — 默认 Prepare 配默认 nonce 池可能提出非法块；单笔 CheckTx 绿 ≠ 整包可提案。  
已收应用侧：[ASA-2024-0012 / 0013](../../tracks/failure-museum/asa-2024-0012.md) — 外层 `max_tx_bytes` 不是内层解码 / 内部消息已有界。  
已收应用侧：[ISA-2025-002](../../tracks/failure-museum/isa-2025-002.md) — 可选模块 EndBlocker 出错不是局部失败；亲戚 ASA-2025-003（除零）不另立。  
已收应用侧：[ASA-2024-005](../../tracks/failure-museum/asa-2024-005.md) — 再委托不是待执行罚没的洗白。  
已收应用侧：[x/crisis](../../tracks/failure-museum/x-crisis-no-halt.md) — 停链交易不是链已经停；官方不修。  
已收应用侧：[ISA-2025-005](../../tracks/failure-museum/isa-2025-005.md) — 奖励池入金溢出不是只是金额算错。  
已收应用侧：[ASA-2024-003](../../tracks/failure-museum/asa-2024-003.md) — 未初始化的被挡账户不是可归属的地址。  
已收应用侧：[ASA-2024-010](../../tracks/failure-museum/asa-2024-010.md) — Int/Dec 位宽对不齐不是已对齐的数。  
已收应用侧：[ISA-2025-001](../../tracks/failure-museum/isa-2025-001.md) — 跨链确认 JSON 反序列化不是已经确定；含 ASA-2025-004。  
已收应用侧：[ASA-2024-007](../../tracks/failure-museum/asa-2024-007.md) — 超时回调里再跑超时不是 ICS-20 已经原子。  
**待补：** 其它案必须链到官方 postmortem 或安全公告。  
方向：halt（活性）、应用非确定性导致的分裂。

---

## 16. 源码入口（预告）

1. **consensus state machine** — round/step、锁。为什么：这是协议心脏。  
2. **WAL / replay** — 崩溃恢复。写下 ≠ 已经 fsync；回放时再签 ≠ 已经双签：见 [`../../tracks/implementation/worked-example-wal-vs-signed.md`](../../tracks/implementation/worked-example-wal-vs-signed.md)（不变量 298）。  
3. **ABCI 适配** — 引擎与应用的字节契约。  
4. **light client** — 跳过中间头时重叠的是 trusted `NextValidators`，不是新集合自嗨。见 [`../../tracks/light-clients/worked-example-bft-skip.md`](../../tracks/light-clients/worked-example-bft-skip.md)。  
5. **evidence** — `DuplicateVoteEvidence` / `LightClientAttackEvidence`；引擎通知应用，不自动 slash。过期是高度且时间；默认窗可能短于解绑。见 [`../../tracks/economic/worked-example-evidence.md`](../../tracks/economic/worked-example-evidence.md)、[`../../tracks/economic/worked-example-evidence-window.md`](../../tracks/economic/worked-example-evidence-window.md)。  
6. **state sync** — `OfferSnapshot` 只有轻验 AppHash 可信；收尾对 Info。见 [`../../tracks/implementation/worked-example-statesync.md`](../../tracks/implementation/worked-example-statesync.md)。轻验集合对上 ≠ 提议者选择已对齐（ASA-2024-009）。

仓库：CometBFT 上游。打开时核路径。

---

## 17. 关键函数（逻辑级）

**`enterPrevote` / `enterPrecommit` / `tryFinalizeCommit`（逻辑名）**  
输入：当前 height/round、收到的票、超时。  
输出：新票或进入 commit。  
invariant：不在同一高度对两个冲突值做出违反锁的承诺。

**`CheckTx` vs `PrepareProposal` vs `ProcessProposal` vs `FinalizeBlock`**  
invariant：Check 通过不是已进提案；Prepare 可改列表；Process REJECT 是 prevote nil 不是免费过滤；Finalize + Commit 才进提交状态（不变量 33）。同进程不是已经有套接字隔离；一条连接不是已经是四门：见 [`../../tracks/implementation/worked-example-abci-conn-vs-gates.md`](../../tracks/implementation/worked-example-abci-conn-vs-gates.md)（不变量 307）。默认锁不是已经 RPC 安全；Commit 前上锁不是已经解锁；Commit 里等广播不是已经能往下走：见 [`../../tracks/implementation/worked-example-commit-lock-vs-rpc.md`](../../tracks/implementation/worked-example-commit-lock-vs-rpc.md)（不变量 310）。Prepare 没有头哈希不是已经知道本头；候选不是已经是 ExecuteTxState；丢掉不是已经永远不用再执行：见 [`../../tracks/implementation/worked-example-candidate-vs-execute.md`](../../tracks/implementation/worked-example-candidate-vs-execute.md)（不变量 311）。看见 `CheckTx` 过了 / 看见进了池并开始流言 不是已经按 `ExecuteTxState` 验过，也不是已经按将要执行的那份状态验过；`CheckTxState` 和 `ExecuteTxState` 可以并发更新；Commit 之后的再验由 `Type` 标明 `CHECK_TX_TYPE_NEW` 与 `CHECK_TX_TYPE_RECHECK`（不变量 312）。看见旧交易又被送来 / 看见内存池有去重机制 不是已经保证不会重复；过了 CheckTx 不是已经有应用级重放保护；通常不受欢迎不是已经没有幂等例外（不变量 313）。看见 Query 连接不是已经是 ExecuteTxState；看见上次 Commit 不是已经跟上正在跑的块；看见启动对齐不是已经是快照重放（不变量 314）。看见 MaxGas 不是已经在执行；看见 GasUsed 不是已经算进共识；看见已提交块不是已经按气验过（不变量 315）。看见结果列表不是已经同一顺序；看见 Code 非零不是已经没进块；看见 Code / Data 不是已经印进本头（不变量 316）。看见 CheckTx 的 Data 不是已经被引擎用了；看见各节点 Data 不一样不是已经分叉；看见 Priority 不是已经是共识顺序（不变量 317）。看见 InitChain 回了空名单不是已经没有集合；看见同一批重复公钥不是已经能恢复；看见 power 写成 0 不是已经删掉不在集合里的人（不变量 318）。看见 InitChain 回了空 ConsensusParams 不是已经没有参数；看见 Finalize 没回不是已经清掉；看见只改一个字段不是已经只改这一项（不变量 319）。看见应用高度比引擎高不是已经允许；看见块进了 blockstore 不是已经 Commit；看见启动 Info 对上不是已经能跳步（不变量 320）。看见 OfferSnapshot 收下不是已经装完；看见一块 chunk 收下不是已经齐；看见拉失败换一份不是已经能接着装（不变量 321）。看见 ListSnapshots 回了不是已经有了全部快照；看见挑了最高不是已经收下；看见 Offer 被拒不是已经停（不变量 322）。看见快照装完不是已经有了 ChainID；看见 Info 的 AppHash 对上不是已经版本也对上；看见切进共识不是已经有从创世的完整历史（不变量 323）。看见拍了这个高度不是已经交差之后拍的；看见没停链不是已经一致；看见只留最近两份不是已经有了全部历史快照（不变量 324）。看见头上有 AppHash 不是已经是交易默克尔；看见 Query 回了 Proof 不是已经对上 AppHash；看见一层 ProofOp 的根不是已经对上最终 AppHash（不变量 325）。看见发了 addr 过滤查询不是已经收下这个人；看见 id 过滤查询绿了不是已经过了 addr；看见有 /store 路径不是已经是引擎在用（不变量 326）。看见立刻整块执行不是已经离开关键路径；看见填了 TimeoutPropose 不是已经装得下；看见又开一轮不是已经丢了活性（不变量 327）。看见同一高度回了不同码不是已经有了 CheckTxCode；看见还在振荡不是已经过了 h_stable；看见本地不再振荡不是已经各节点同一份 b（不变量 328）。看见 Query 回了不是已经复制到各节点；看见查到了不是已经新鲜；看见实现了 Query 不是已经是正常运转必须有（不变量 329）。看见填了证据 MaxBytes 不是已经落在块上限下面：见 [`../../tracks/implementation/worked-example-evidence-maxbytes-vs-block.md`](../../tracks/implementation/worked-example-evidence-maxbytes-vs-block.md)（不变量 331）。看见 > 0 不是已经盖住解绑。看见证据 MaxBytes 不是已经是块 MaxBytes。看见到了 H 不是已经 Prepare 带了扩展：见 [`../../tracks/implementation/worked-example-ve-height-vs-prepare.md`](../../tracks/implementation/worked-example-ve-height-vs-prepare.md)（不变量 330）。看见 H+1 带了扩展不是已经是本高度刚签的。看见 h < H 带了扩展不是已经合法。

**`ExtendVote` / `VerifyVoteExtension`**  
invariant：扩展是另一份签；Verify REJECT 丢整张 precommit，不是块非法；`s_h` 不读本高度扩展（不变量 34）。

**`validator_updates` 生效高度**  
invariant：H 返回的更新，H+1 改 `NextValidatorsHash`，H+2 才按新集合计票，H+3 `*_last_commit` 带新集合（不变量 35）。见 [`../../tracks/consensus/worked-example-validator-delay.md`](../../tracks/consensus/worked-example-validator-delay.md)。同一高度各轮用同一套，不是已经换成应用刚回的那套；新加入不是已经能跳到队头：见 [`../../tracks/consensus/worked-example-round-vs-set.md`](../../tracks/consensus/worked-example-round-vs-set.md)（不变量 302）。

---

## 18. 如何测试

状态机单元测试、WAL 崩溃回放、拜占庭投票夹具、超时注入。  
「不确定」应偷：锁规则的 property test；断电后不得发出矛盾 precommit。

---

## 19. 「不确定」适用性

| 档 | 内容 |
|---|---|
| 强烈建议研究 | 锁、+2/3 相交、WAL、ABCI 分离、确定最终的用户语义 |
| 可以参考 | mempool CheckTx 与共识分离、Prepare 改列表但 Process 默认 Accept、集合更新的 H+1/H+2/H+3 |
| 暂时不需要 | IBC 全协议、CosmWasm。若对照四层对象：[`../../tracks/economic/worked-example-ibc-client-vs-packet.md`](../../tracks/economic/worked-example-ibc-client-vs-packet.md)（不变量 146）。ICS-20 代币机：[`../../tracks/economic/worked-example-escrow-vs-voucher.md`](../../tracks/economic/worked-example-escrow-vs-voucher.md)（不变量 155） |
| 不建议采用 | 「我们 BFT，所以投个 2/3 就行」；把升级管理员做成可改历史的后门 |

**建议：** 这是「不确定」默认该吃透的引擎家族。还没吃透前不要换更新的 BFT 品牌名。
