# Invariant Library

只收能写成测试的句子。

已收：

1. **无双花：** 同一花费授权在 canonical 历史上不得被接受两次。  
2. **供给守恒：** 除协议允许的发行规则外，不得凭空多出可花费余额。  
3. **确定性：** 同一已排序输入，两实现状态哈希相同。  
4. **锁：** 诚实节点不得在同一高度对两个冲突值发出违反锁规则的承诺。  
5. **原子高度：** 崩溃恢复后，应用高度与引擎高度一致，无半块状态。  
6. **域分离：** 验证者投票字节不得被当成用户交易。  
7. **金额不回绕：** 任何余额/输出求和溢出必须拒绝，不得模回绕后当作合法。  
8. **集合版本：** 同一高度的计票只使用唯一的 `V(h)`，且该哈希被状态/头承诺。  
9. **提交≠兑付：** 租户状态根被包含到房东头，不等于桥可兑付。  
10. **迁移不可单旧签：** 算法 A 危急后，不得只凭 A 的签名把账户迁到新 pk。  
11. **算法标识：** 共识验签必须先读明确的算法标签，禁止隐式默认两种实现各猜各的。  
12. **Merkle 叶列表唯一：** 规范允许的填充不得让两个不同叶列表承诺到同一根；变异块必须拒绝，且不得把同哈希的合法块永久拉黑（CVE-2012-2459）。  
13. **验证明 ≠ 供给：** `VerifyProof=接受` 不得单独充当供给守恒（CVE-2019-7167）。  
14. **升级不得改供给解释：** 升级交易可增加算法标识，不得静默改 `SupplyFormula` 或历史余额含义。  
15. **状态占用有界：** 若协议允许任意 `data` 进活状态，必须有占用不等式或等价回收；禁止只收一次执行费而要求全节点永存。  
16. **投票流量先算：** 宣称 PQ-BFT 可上主网之前，必须写出 `每高度票数 × |σ_vote|`（参数集 + FIPS 版本）；未写不得用「已后量子」当结算文案。  
17. **OTS 叶子不复用：** 若路径使用有状态哈希签名（XMSS/LMS 等），canonical 历史上同一 `(pk, ots_index)` 不得再授权另一笔不同消息；实现必须先持久化 index 再输出 σ（RFC 8391；SP 800-208）。  
18. **FIPS ctx 按角色：** 使用 FIPS 204/205 外部 API 时，`Verify` 必须传入规范写明的 `ctx`（≤255 B）。同一把钥上的用户签与投票签不得都用空 `ctx`；pure 与 pre-hash 必须由算法标签区分（FIPS 204 Alg. 2；FIPS 205 Alg. 22）。  
19. **投票步类型进被签字节：** Prevote 的 SignBytes（或 attestation 的 domain）不得使 Precommit / proposer 路径 Verify 为真。同一高度两步不是「再签一次同一哈希」（CometBFT signing.md；consensus-specs `compute_domain`）。  
20. **BFT 轻客户端重叠旧集合：** 跳过中间高度时，新 commit 必须含 trusted `NextValidators` 中 **> max(1/3, trustThreshold)** 的投票权，且 trusted 仍在 `trustingPeriod` 内；紧邻后继必须集合哈希相接且旧集合 +2/3。只数新委员会自己的 2/3 不得接受（verification_001_published `LCV-FUNC-VALID.1`）。  
21. **双签证据形状成立 ≠ 已罚没：** 同一 `(addr, height, round, type)`、不同 `BlockID`、本链 `ChainID` 上两张合法签，必须能被验为 `DuplicateVoteEvidence`；同 BlockID 或错链必须拒。引擎提交 `Misbehavior`，应用决定 slash。过期按规范的年龄参数忽略（CometBFT evidence.md）。  
22. **轻客户端必须点名信任对象：** 产品句须写清是「已信任全集的重叠」（CometBFT 跳过）、「同步委员会样本」（Altair）还是证明系统。样本的 2/3 不得写成全验证者集合的 2/3（altair/light-client/sync-protocol.md）。  
23. **短时承诺不是永存 DA，且 KZG 不是纠删 DAS：** 头或 versioned hash 被最终确定，不得单独充当「数据永远可重建」。4844 sidecar 的服务窗是 `MIN_EPOCHS_FOR_BLOB_SIDECARS_REQUESTS`（4096 epoch）。PeerDAS 抽到列不得写成执行正确，也不得写成与 Celestia 二维 DAS 同一对象（EIP-4844；deneb/p2p-interface.md；fulu/das-core.md）。  
24. **检查点同步必须落在弱主观或信任期内：** 从检查点起步时，检查点必须在同步路径上，且对当前时间仍 `is_within_weak_subjectivity_period`（或 CometBFT `trusted.Time > now - trustingPeriod`）。过期或对不上不得当「和从创世复算同一安全」；对不上路径按规范应致命退出。检查点从哪来是部署对象（phase0/weak-subjectivity.md；verification_001_published）。  
25. **跳过验证必须点名跳过了哪条规则：** assumevalid 只跳祖先脚本/签名，且仅当该哈希在被选中的链上；不强制那条链。assumeutxo 暂时跳 UTXO 重放，背景链须验到快照基块并核编译哈希。二者都不是旧 checkpoint（强迫块在链上），也不是弱主观周期。产品句缺「跳过什么 / 如何关闭」不得当全验证（Bitcoin Core 0.14.0 发行说明；assumeutxo 设计文档）。  
26. **可罚关系必须写成客观的两票谓词：** Casper 证明是「同 target epoch 不同 data」或「attestation_1 包住 attestation_2」（顺序不对称）；提议者是同 slot 不同头。信标状态执行 `slash_validator`。CometBFT 是同 height/round/Type 不同 BlockID，引擎只交证据。任意两张签、同步委员会聚合，不得自动当成同一套罚没（phase0 `is_slashable_attestation_data`；evidence.md）。  
27. **排序权必须点名谁写列表、谁签头：** 签一份只含 `ExecutionPayloadHeader` 的盲块，不等于提议者选过每一笔交易。Builder API 是域外临时接口，信任高于协议内 PBS，不是 `process_block`。揭示失败是部署/信任，不是新的分叉选择。同 slot 两份不同头仍走 proposer slashing（builder-specs README；Bellatrix `builder.md`）。  
28. **有效性证明必须点名被锁程序，且两层 accepted 不得混：** 结算合约只接受其当前登记的 program / circuit hash 所证明的根。改哈希是升级。`ACCEPTED_ON_L2` 不得写成 `ACCEPTED_ON_L1`。验证明 ≠ 可提款（仍要 DA 与桥），≠ 供给守恒（不变量 13）。Starknet 文档：SNOS / applicative bootloader；Core `programHash`（docs.starknet.io SNOS / Transactions）。  
29. **网络调整钟不得绕过上限：** 若「块是否太未来」掺入对等节点时间偏移，偏移必须有显式上限，且有符号溢出 / `abs(INT64_MIN)` 不得绕过。被前 N 个对等节点带偏而拒收规范新块，是实现/部署事故，不是协议改了 MTP（CVE-2024-52912）。  
30. **未确认索取不得被单一对等节点永久独占：** 对同一未确认对象的 `GETDATA` 超时后必须能向其他已宣布的对等节点再要。有界「已索取」表被挤出，不得重置为只向原对等节点再要。本节点看不见 ≠ 共识非法（CVE-2024-52913）。  
31. **头必须先够工作量才进永久索引：** 实现不得把任意低难度头链无界写入内存/块索引。检查点曾是反垃圾缓兵，不是第三种锁死历史的共识。先验工作量再入库；先存后查会回归（CVE-2019-25220；CVE-2024-52916）。  
32. **孤儿解析必须可中断，且验代价有配额：** 接受一笔新交易后，不得对孤儿缓存做「每输出 × 全缓存 × 昂贵验」而不让出事件循环。孤儿可以是无效且验起来贵。本节点卡住 ≠ 共识非法（CVE-2024-52914）。  
33. **池预检、提案改写、提案验收、提交执行必须分开：** `CheckTx` 成功不得写成已进块。`PrepareProposal` 可以改 raw 列表（且可不确定），返回总字节不得超过本次 `max_tx_bytes`。`ProcessProposal` 不得改列表，Accept/Reject 只依赖请求 + `s_{h-1}`；诚实准备的提案，诚实 Process 必须 Accept；REJECT 走 prevote `nil`。立即执行不得替换已提交状态，直到 `FinalizeBlock` + `Commit`（ABCI++ Req 2–5、9）。  
34. **扩展验收失败丢掉整张 precommit，且本高度状态不得依赖本高度收到的扩展：** `VerifyVoteExtension` REJECT 使整张 Precommit 无效，不是「块非法」。诚实扩展必须被诚实 Verify 接受。`s_h` 不得依赖本高度收到的 *e*；扩展最早在 *h+1* 的 Prepare 使用。`CanonicalVoteExtension` 不是 `CanonicalVote`。空扩展仍验签（ABCI++ Req 6–10；data_structures）。  
35. **集合更新必须写出哪一高度改哪一个哈希：** 高度 H 的 `validator_updates` 不得写成 H+1 立刻计票。CometBFT：H+1 更新 `NextValidatorsHash`，H+2 新集合投票（`ValidatorsHash`），H+3 `*_last_commit` 才带新集合。`consensus_param_updates` 是另一条（H 的更新用于 H+1）。计票仍只承认唯一 `V(h)`（不变量 8；ABCI++ FinalizeBlock / Validator Updates）。  
36. **新块宣布后的索取不得被单一宣布者独占：** headers / compact block 宣布 ≠ 已收到块。宣布者不交付时必须能向其他已宣布的对等节点再要。本节点还没拼出块 ≠ 共识非法，也 ≠ 未确认交易看不见（不变量 30）（CVE-2024-52922）。  
37. **部分下载对象必须一次终结，且断言不得当对等过滤器：** compact / 部分块重建失败（短 ID 碰撞，或 `blocktxn` 含未被 Merkle 根承诺的交易）后，必须丢掉该实例再走整块或其他对等节点。同一实例不得靠 `assert` 挡第二次填充。节点崩溃 ≠ 共识拒块 ≠ 分叉。短 ID 碰撞必须当诚实可能，不得因此罚对等节点（CVE-2024-35202）。  
38. **应用快照必须点名跳过了历史重放，且锚是轻验 AppHash：** ABCI state sync 用快照代替历史块 `FinalizeBlock`。`OfferSnapshot` 里只有轻客户端验过的 `app_hash` 可信任；`Snapshot.hash` / `metadata` 可伪造。装完必须用 `Info` 对 `LastBlockAppHash` / Height。对上快照元数据 ≠ 从创世重放 ≠ assumeutxo 背景全验（ABCI++ OfferSnapshot；state-sync P2P）。  
39. **对等节点的块下载状态必须隔离：** 一个对等节点送来的变异块（Merkle 根或 witness 承诺对不上交易）不得清掉对其他对等节点的下载/重建状态。未请求的变异块不得让正在进行的 compact 补齐作废。变异 ≠ 共识已拒绝合法块，也 ≠ 2012-2459 的同根构造（CVE-2024-52921）。  
40. **块时间必须点名算法：** 「BFT 时间」四个字不是一种算法。PBTS：提议者本地钟；timely 相对本节点的 `proposalReceiveTime`；不 timely → prevote `nil`；已在更早轮拿到 +2/3 prevote 再提议的块不再验 timely；`PbtsEnableHeight` 启用后不能关。BFT Time：块 H 时间是 H-1 `LastCommit` 时间戳的加权中位数，必须可复算。Bitcoin MTP 与实现对等调整钟是另外两把尺。不 timely ≠ 块非法 ≠ 已有罚没谓词。不得把未标注版本的 `PRECISION` / `MSGDELAY` / 1 ms 写成永恒共识。  
41. **MTP 的两份工作必须与太新窗分开：** 新块太早：`nTime <=` 父块 `GetMedianTimePast` → `time-too-old` / `BLOCK_INVALID_HEADER`。BIP 113（CSV 之后）：交易 locktime 看父 MTP，不看本块 `nTime`。太新：本节点钟 + 命名宽限 → `time-too-new` / `BLOCK_TIME_FUTURE`（注释写也可能是本节点钟坏了）。三把尺糊成「Bitcoin 时间」或「MTP」一个词即错。跨度 / 宽限秒数是 Bitcoin 命名常数，不是不确定默认。  
42. **共识拒绝不得默认无上限写盘：** 健全性失败或检查点前分叉被拒之后，实现不得对每次拒绝无条件写 info/warning/error 直到磁盘满。拒绝 ≠ 不占磁盘。检查点挡头索引 ≠ 日志安全。日志配额是实现/部署对象，不是共识改了拒绝规则（CVE-2025-54605；同类：CVE-2025-54604 自连接日志）。  
43. **后台验签必须先于它指向的预计算数据结束：** 并行脚本/验签作业若只握指针，任何返回路径（含「另一项检查已失败」的提前 return）必须先汇合队列。合法块会 Wait、非法块提前走，是实现倒挂。节点崩溃 ≠ 共识已安全拒绝（CVE-2024-52911）。  
44. **入池前拒绝若不踢人，则必须有验代价配额：** 非标准 / CheckTx 拒绝不得写成免费。拒了仍连着，就可以重复送，挤掉块传播。最坏脚本哈希是入池配额，不是共识已经结束。这不是进池之后的孤儿扫描（不变量 32）（CVE-2025-46598）。  
45. **库存宣布的三个方向必须各自有配额：** 入站 INV 不得在一次处理里灌满发送缓冲（回复风暴 + 对方拒收）（CVE-2024-52915）。入站 GETDATA 不得让单连接死循环；单连接不前进 ≠ 全节点已死（CVE-2024-52920）。出站待宣布集合不得大到排序卡住 P2P 线程；只听不宣布的对等节点会放大（2023-05 inv-to-send）。这不是索取独占（30）、宣布块不交付（36）、或变异清别人下载（39）。  
46. **证据有效窗必须盖住解绑，且过期是合取：** 仅当高度与时间**都**超过才忽略证据（`CurrentHeight - MaxAgeNumBlocks > EvidenceHeight` 且 `CurrentTime - MaxAgeDuration > EvidenceTime`）。`> 0` 是下限，不是盖住解绑。默认 `EvidenceParams` 不是「已经够罚」（ASA-2024-004；无代码补丁）。这不是「上链 ≠ slash」（不变量 21），也不是轻客户端信任期 < 解绑（不变量 20）。  
47. **本地超时不是最终性，commit 后再等更不是锁：** 规范把超时写成**本地**等待：`timeoutProposeR`（随 round 增加）到点 → Prevote，没好提案就 prevote `nil`；任意 +2/3 prevote 后再等 `timeoutPrevote` → Precommit；任意 +2/3 precommit 后再等 `timeoutPrecommit` → 下一轮，或 +2/3 对某块 → **Commit**。Commit 之后先等到**块到齐**（这一步不是 `timeout_commit`），再进入 NewHeight：`StartTime = CommitTime + timeoutCommit`，为的是收迟到的 precommit。官方配置：成功一轮里「无论发生什么都要等」的，**只有** `timeout_commit`；它是已经 commit 之后、开新高度之前再等。`skip_timeout_commit=true` 的官方语义是「像 TimeoutCommit=0」。[PR #2892](https://github.com/cometbft/cometbft/pull/2892) 在较新的线上删该键；现行 `main` 仍可能保留该字段（Deprecated）。本地超时 ≠ PBTS timely ≠ 区块时间算法 ≠ 锁定值。不一致的 `timeout_propose` / `timeout_commit` 是激励问题，不是第三条最终性。  
48. **接收缓冲必须在读完载荷前有界；最大序列化长度不是接收分配上限：** Bitcoin Core [CVE-2015-3641](https://bitcoincore.org/en/2024/07/03/disclose_receive_buffer_oom/)（Medium）：接收尺寸一度只受「消息最大序列化长度」约束，攻击者可以按连接逼节点分配到这个上限。修法（#5843，0.10.1）是在**读完载荷之前**收紧允许的接收大小。后来 Segwit BIP144 又把该上限调回更大一档——那是实现/部署数字，不是「洞又开了」。这不是出站发送缓冲（不变量 45 / 52915）、不是日志盘（不变量 42 / 54605）、不是头索引（25220）。「最大消息长度」可以仍然很大；接收分配必须另写更紧的界。  
49. **攻击者可推动的插入计数不得用会回绕的窄整数当主键：** Bitcoin Core [CVE-2024-52919](https://bitcoincore.org/en/2024/07/31/disclose-addrman-int-overflow/)（High）+ [part 2](https://bitcoincore.org/en/2025/04/28/disclose-cve-2024-52919/)（Low）：地址表用递增 `nIdCount` 当新条目标识。32-bit 回绕 → 断言崩溃。v22.0 限速只改代价；v29.0 才改 64-bit 宽度。限速 ≠ 回绕谓词已成立。这不是接收分配（48）、不是发送缓冲（45）、不是无界封禁表（50）、不是部分块断言（37）。  
50. **自动惩罚不得写入攻击者可撑大的无界身份表：** Bitcoin Core [CVE-2020-14198](https://bitcoincore.org/en/2024/07/03/disclose-unbounded-banlist/)（High）：封禁 IP 列表无上限，对手可灌（IPv6 尤其便宜）；`GETADDR` 对每条待返回地址扫完整张表。无界 map + 全表扫描 = 内存与 CPU。后来拆成手动 ban 与自动 discourage（有界、不可枚举）。这不是地址表递增 ID（49）、不是发送缓冲（45）、不是接收分配（48）、不是头索引（31）。  
51. **尺寸检查必须用固定宽度，32-bit 与 64-bit 对同一对象必须同拒或同收：** Bitcoin Core [CVE-2025-46597](https://bitcoincore.org/en/2025/10/24/disclose-cve-2025-46597/)（Low）：写盘前的尺寸检查在 32-bit 上对超大块溢出。不能走 `BLOCK` 消息；理论上 compact + 非默认超大内存池。落地修法是**间接**卡住 32-bit `-maxmempool`。卡住旋钮 ≠ 溢出谓词已改成固定宽度。这不是接收分配（48）、不是部分块断言（37）、不是递增 ID 回绕（49）。  
52. **应用回的 post-commit 等待必须标非确定性，不得写成槽位或最终性：** 现行 `main` [abci++_methods.md](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) 把 `FinalizeBlockResponse.next_block_delay` 标 **Deterministic = No**。语义仍是 Commit 之后、开下一高度之前再等（以前是本地 `timeout_commit`）。各节点可以回不同值。ADR-115：恒定出块间隔做不到；不要做成 `ConsensusParams`。不是所有发布线都有该字段。这不是本地超时本身（47），不是 PBTS（40），不是 `app_hash`。  

来源：L0–L10 课 + 档案 + 博物馆。每条应对 L9.7 的自动测试。用例目录：[`../adversarial-corpus/README.md`](../adversarial-corpus/README.md)。

**对不确定（建议，不是选型）：** 第 16 条在选定 PQ 算法之前就算一遍。第 17 条：投票与热钱包不要用有状态 HBS。第 18 条：每个签名角色一个 `ctx` 常量（或一把钥只服务一个角色）；不要只靠「消息里已经写了 domain」。空 `ctx` 是 FIPS 默认，不是已分离。第 19 条：步类型进 `M`；签名器记住上次 `(height, round, type)`。第 20 条：轻客户端默认不是结算角色；若启用，跳过必须重叠旧集合，信任期必须短于解绑期。第 21 条：证据上链只通知应用；罚没公式写在 ABCI 一侧。第 22 条：轻客户端文案点名样本还是全集；不要抄 Altair 当第一版默认。第 23 条：短时 DA 必须写服务窗；不要抄 KZG blob 当后量子默认 DA。第 24 条：检查点同步必须写新鲜度；不要把 finalized 写成「从创世一样安全」。第 25 条：IBD 加速必须点名跳过的规则；默认不要跳脚本。第 26 条：先写两票谓词和谁执行，再谈罚金；不要默认抄 surround。第 27 条：先写谁排序；不要抄域外 Builder API 当 v1，也不要写「PBS 解决了 MEV」。第 28 条：有效性证明先写程序哈希和两层 accepted；不要抄有效性 rollup 当 v1。第 29 条：掺对等偏移的钟必须测上限；拒块须点名是钟还是共识。第 30 条：索取状态机必须能换对等节点；看不见不得写成链拒绝。第 31 条：头/证书进永久索引必须先过工作量或配额；不要靠「检查点」三个字挡垃圾。第 32 条：依赖解析必须可中断；后量子更要先写孤儿配额。第 33 条：若抄 ABCI++，必须写四门；Process 默认 Accept；不要把 CheckTx 或 Prepare 写成已结算或 PBS。第 34 条：第一版可以不启用扩展；启用则必须写 Req 10，且不变量 16 把扩展 σ 算进每高度票字节。第 35 条：后量子换验证者钥必须写出 H+1/H+2/H+3；不要发明「Finalize 当下换人」。第 36 条：大块/部分块的索取必须能换对等节点；宣布不是收到。第 37 条：部分下载失败必须清实例；对等路径禁止断言当过滤器。第 38 条：第一版默认可从创世；若提供 state sync，必须写轻验 AppHash 与信任期，不要假装背景还会全验。第 39 条：部分下载状态按 (对等节点, 对象) 隔离；未请求的变异块不得拆诚实补齐。第 40 条：文档必须点名 PBTS / BFT Time / MTP / 调整钟中的哪一把；不要写「BFT 时间」交差，也不要发明时间乱填就 slash。第 41 条：若学 Bitcoin 时间，必须分开太早 / locktime / 太新；不要把 MTP 窗口抄进 BFT。第 42 条：拒绝路径必须有日志配额；不要把「已非法」写成磁盘安全。第 43 条：并行验签先写寿命与汇合；不要只测合法块。第 44 条：入池前拒绝要么踢人，要么记这个对等节点的验代价；不要把「非标准」写成免费。第 45 条：入站宣布、入站索取、出站待宣布各写配额；不要写「我们有 INV」。第 46 条：证据窗按解绑重算，过期写「且」；不要把仓库默认写成已经够用。第 47 条：若点名超时，必须写清它们是本地等待；`timeout_commit` 是 commit 之后再收迟到票，不是锁、不是最终性、不是 PBTS。`skip_timeout_commit` 不论某条发布线还在不在，语义都是「像 timeout_commit=0」。不要抄文档秒数或 Alice/Bob 玩具当产品事实。第 48 条：若点名最大消息长度，必须另写读载荷前的接收分配上限；不要把 32/2/4 MiB 当不确定常量。第 49 条：若地址/库存/证据表用递增 ID，必须先写回绕谓词；限速只是代价，不是宽度已够。不要抄「每 10 秒 1 条」或「一年以上」当产品证明。第 50 条：若自动惩罚对等节点，不得写入可枚举、可持久、可被便宜身份灌的 map；手动封禁和自动 discourage 必须分开。不要抄 GETADDR 返回条数当不确定常数。第 51 条：对象有多大必须用规范写死的整数宽度；不要让 32-bit / 64-bit 对同一份字节意见不同。内存池旋钮可以降利用面，不能代替检查宽度。第 52 条：若让应用回 post-commit 等待，必须标非确定性、点名发布线有没有该字段；不要写成全网槽位或第三条最终性。不要抄规范里的 1s。
