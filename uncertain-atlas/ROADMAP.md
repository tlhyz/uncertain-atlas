# Uncertain Atlas 优化路线图

本文件把 [`GOAL.md`](GOAL.md) 的两个目的拆成**一个极大目标**与**可执行小目标**。  
状态：2026-09-17 启动；与 [`ARCHITECTURE.md`](ARCHITECTURE.md) 同步维护。

---

## 极大目标（North Star）

**建成可验证的「全球区块链架构图谱 + 不确定链设计参考库」：**

- 目的 A：用户本人能讲清「一笔交易从钱包到最终确认」的因果链，而不是背名词。
- 目的 B：为「不确定 / Uncertain」后量子结算机积累**可测试、可决策、可复用**的设计储备——每个重要判断能回溯到规范/源码/事故，且决策矩阵与威胁模型能驱动 v1 选型。

完成标准（事实 + 建议混合，见各条标注）：

1. 五条轨（index / courses / protocols / tracks / libraries）互相指认，无孤立读书笔记。
2. CometBFT ABCI++ 不变量拆完（目标 ~793 句；当前 ~1036）。
3. 决策矩阵「不确定候选」列填完**建议档**（非最终选型）。
4. 对抗语料 C01–C1014+ 有 runner，能批量扫描文案/测试钩子。
5. 过滤器页链（Cardano / Babylon / EigenLayer 等）要么补 19 节，要么在 index 明确「永久过滤器」。
6. 单一 canonical 分支 + 清晰 merge 策略（见 Phase 0）。

---

## 架构评估摘要（2026-09-17）

### 已完善

| 维度 | 证据 | 评级 |
|---|---|---|
| 目录隔离 | `uncertain-atlas/` 与 `qtb/` 分离；GOAL 门禁 | 强 |
| 课程 L0–L10 | 77 模块正文；A–J 结构 | 强 |
| 协议档案 | 20+ 链/品类 19 节模板 | 强 |
| 横向专题 | 16 tracks；failure-museum 92+ 案 | 强 |
| 模式/反模式 | 500+ design-patterns；650+ anti-patterns | 强 |
| 不变量库 | 1036+ 可测试句；ABCI++ 主线 | 进行中（强） |
| 通读路径 | `index/04-study-path.md` 六通 | 强 |

### 需调整

| 缺口 | 影响 | 优先级 |
|---|---|---|
| KB 不在 `main`，285+ cometbft 快照分支 | 找不到「当前版」 | P0 |
| `ARCHITECTURE.md` 进度表过时（写 12+13 模式） | 误导维护者 | P0 |
| 决策矩阵候选列空 | 目的 B 无法落地 | P0 |
| adversarial-corpus 无 runner | 676 条 invariant 无法自动验 | P1 |
| 威胁模型草稿 | L10 第六通缺锚 | P1 |
| PQ CPU / 尺寸实测空 | L10.2 工程账本 incomplete | P2 |
| 过滤器页链无 19 节 | 知识树声称与档案不一致 | P2 |
| 无全文检索 / 索引服务 | 2000+ 文件难导航 | P3 |
| exams 后置但未统一格式 | 低（用户要求后置） | P4 |

---

## 阶段与小目标

### Phase 0 — 治理与 canonical（本周）

| ID | 小目标 | 完成标准 |
|---|---|---|
| P0-1 | 指定 canonical 分支 | README + index 写清：`cursor/uncertain-atlas-optimization-5ee2` 承接 atlas+cometbft tip |
| P0-2 | 更新 ARCHITECTURE 进度表 | 数字与 `index/03-knowledge-assets.md` 一致 |
| P0-3 | 发布 ROADMAP + index/05 | 本文件可被 agent/人追踪 |
| P0-4 | 决策矩阵填建议档 | consensus + state-model 不确定列有内容且标「建议」 |
| P0-5 | adversarial runner v0 | 能 parse Cxx 表、list、validate |

### Phase 1 — 目的 B 可决策（接下来）

| ID | 小目标 | 完成标准 |
|---|---|---|
| P1-1 | 威胁模型 v1 | `libraries/threat-model/` _actor / _asset / _boundary 三页 |
| P1-2 | settlement-copy 与矩阵对齐 | L10.3 清单 ↔ 矩阵行可互链 |
| P1-3 | ABCI++ 拆完 677–1036 | AUDIT_LOG 连续；invariants README 更新 |
| P1-4 | runner 接 pytest | 至少 10 条 Cxx 有占位测试 |
| P1-5 | PQ 尺寸卡补 CPU 列 | `tracks/post-quantum/engineering-ledger.md` 有测量方法 |

### Phase 2 — 知识完整性

| ID | 小目标 | 完成标准 |
|---|---|---|
| P2-1 | Cardano 19 节或永久过滤器声明 | protocols + index 一致 |
| P2-2 | Babylon / EigenLayer 补档案或降级 | 同上 |
| P2-3 | tracks 对照表回填第 9 波 | 每新增 invariant 同步一行 |
| P2-4 | L8.4 数学节（可选） | 用户触发后再开 |

### Phase 3 — 可用性

| ID | 小目标 | 完成标准 |
|---|---|---|
| P3-1 | 本地 Markdown 索引脚本 | `tools/atlas_index.py` 生成 JSON 目录 |
| P3-2 | invariant ↔ corpus 双向链接校验 | CI 脚本 |
| P3-3 | merge KB → long-lived branch | 不再 285 个 snapshot 分支 |

---

## 执行记录

| 日期 | 完成项 |
|---|---|
| 2026-09-17 | ROADMAP；ARCHITECTURE 更新；index/05；决策矩阵建议档；tools/adversarial_runner.py v0 |
| 2026-09-17 | REVIEW_LOOP.md + review_audit.py；小时定时器协议；威胁模型 v1（INDEX/actors/assets/boundaries） |
| 2026-09-17 | P1-2 settlement-copy 对齐；P1-4 pytest 钩子；P2 永久过滤器声明 |
| 2026-09-17 | P1-3 677–679 Query Usage 拆句（487 item 1/2/3）；P1-5 CPU 测量方法；P3-1 atlas_index.py |
| 2026-09-17 | P1-3 680–682 CheckTx validate-no-apply 拆句（486 item 1/2/3）；P3-2 invariant_corpus_links.py；P1-4 10 条 Cxx pytest |
| 2026-09-17 | P1-3 683–685 CheckTx tx source 拆句（488 item 1/2/3） |
| 2026-09-17 | P1-3 686–688 CheckTx Code≠0 rejected 拆句（489 item 1/2/3） |
| 2026-09-17 | P1-3 689–691 CheckTx Guardian 拆句（490 item 1/2/3） |
| 2026-09-17 | P1-3 692–694 Commit retain_height caution 拆句（491 item 1/2/3） |
| 2026-09-17 | P1-3 695–697 InitChain Usage 拆句（495 item 1/2/3） |
| 2026-09-17 | P1-3 698–700 InitChain decide 拆句（496 item 1/2/3） |
| 2026-09-17 | P1-3 701–703 Commit persist signal 拆句（481 item 1/2/3） |
| 2026-09-17 | P1-3 704–706 CheckTx lane_id 拆句（482 item 1/2/3） |
| 2026-09-17 | P1-3 707–709 CheckTx Request type 拆句（484 item 1/2/3） |
| 2026-09-17 | P1-3 710–712 Finalize consensus_param_updates 拆句（471 item 1/2/3） |
| 2026-09-17 | P1-3 713–715 ProposalStatus 拆句（376 item 1/2/3） |
| 2026-09-17 | P1-3 716–718 Prepare 回包校验 拆句（357 item 1/2/3） |
| 2026-09-17 | P1-3 719–721 ApplySnapshotChunk Result 拆句（398 item 1/2/3） |
| 2026-09-17 | P1-3 722–724 OfferSnapshot Result 拆句（400 item 1/2/3） |
| 2026-09-17 | P1-3 725–727 OfferSnapshot Result 余量拆句（402 item 1/2/3） |
| 2026-09-17 | P1-3 728–730 Offer 收下之后拆句（401 item 1/2/3） |
| 2026-09-17 | P1-3 731–733 Commit 空请求拆句（399 item 1/2/3） |
| 2026-09-17 | P1-3 734–736 ListSnapshots 空请求拆句（395 item 1/2/3） |
| 2026-09-17 | P1-3 737–739 OfferSnapshot 请求拆句（396 item 1/2/3） |
| 2026-09-17 | P1-3 740–742 ApplySnapshotChunk 请求拆句（397 item 1/2/3） |
| 2026-09-17 | P1-3 743–745 ProofOp 键拆句（390 item 1/2/3） |
| 2026-09-17 | P1-3 746–748 ExecTxResult 气拆句（393 item 1/2/3） |
| 2026-09-17 | P1-3 749–751 ExtendedCommitInfo 轮拆句（394 item 1/2/3） |
| 2026-09-17 | P1-3 752–754 CheckTx 请求余栏拆句（391 item 1/2/3） |
| 2026-09-17 | P1-3 755–757 InitChain 回包余栏拆句（392 item 1/2/3） |
| 2026-09-17 | P1-3 758–760 ExecTxResult 日志栏拆句（414 item 1/2/3） |
| 2026-09-17 | P1-3 761–763 Info 回包余栏拆句（389 item 1/2/3） |
| 2026-09-17 | P1-3 764–766 InitChain 请求余栏拆句（388 item 1/2/3） |
| 2026-09-17 | P1-3 767–769 InitChain 请求拆句（387 item 1/2/3） |
| 2026-09-17 | P1-3 770–772 ConsensusParams 余栏拆句（386 item 1/2/3） |
| 2026-09-17 | P1-3 773–775 ConsensusParams 字段拆句（385 item 1/2/3） |
| 2026-09-17 | P1-3 776–778 Query 回包码拆句（384 item 1/2/3） |
| 2026-09-17 | P1-3 779–781 Query 证明回包拆句（383 item 1/2/3） |
| 2026-09-17 | P1-3 782–784 Finalize 请求回包拆句（382 item 1/2/3） |
| 2026-09-17 | P1-3 785–787 CheckTx 回包拆句（381 item 1/2/3） |
| 2026-09-17 | P1-3 788–790 Query 回包拆句（380 item 1/2/3） |
| 2026-09-17 | P1-3 791–793 Info 请求版本拆句（379 item 1/2/3） |
| 2026-09-17 | P1-3 794–796 ApplySnapshotChunk 再拉拆句（378 item 1/2/3） |
| 2026-09-17 | P1-3 797–799 Query 路径拆句（377 item 1/2/3） |
| 2026-09-17 | P1-3 800–802 LoadSnapshotChunk 拆句（375 item 1/2/3） |
| 2026-09-17 | P1-3 803–805 Flush 拆句（374 item 1/2/3） |
| 2026-09-17 | P1-3 806–808 CheckTx 可选拆句（373 item 1/2/3） |
| 2026-09-17 | P1-3 809–811 Misbehavior 拆句（372 item 1/2/3） |
| 2026-09-17 | P1-3 812–814 Query 高度拆句（371 item 1/2/3） |
| 2026-09-17 | P1-3 815–817 Info 握手拆句（370 item 1/2/3） |
| 2026-09-17 | P1-3 818–820 ExtendedVoteInfo 拆句（369 item 1/2/3） |
| 2026-09-17 | P1-3 821–823 Snapshot 类型拆句（368 item 1/2/3） |
| 2026-09-17 | P1-3 824–826 Info 车道拆句（367 item 1/2/3） |
| 2026-09-17 | P1-3 827–829 Commit 保留高度拆句（366 item 1/2/3） |
| 2026-09-17 | P1-3 830–832 VoteInfo 拆句（365 item 1/2/3） |
| 2026-09-17 | P1-3 833–835 Validator 类型拆句（364 item 1/2/3） |
| 2026-09-17 | P1-3 836–838 Finalize 回包义务拆句（363 item 1/2/3） |
| 2026-09-17 | P1-3 839–841 Finalize 何时调用拆句（362 item 1/2/3） |
| 2026-09-17 | P1-3 842–844 ExtendVote 何时调用拆句（361 item 1/2/3） |
| 2026-09-17 | P1-3 845–847 Prepare 请求字段拆句（359 item 1/2/3） |
| 2026-09-17 | P1-3 848–850 两份扩展两份签拆句（358 item 1/2/3） |
| 2026-09-17 | P1-3 851–853 validValue 跳过 Prepare 拆句（356 item 1/2/3） |
| 2026-09-17 | P1-3 854–856 Prepare 改列表拆句（355 item 1/2/3） |
| 2026-09-17 | P1-3 857–859 Process 何时调用拆句（354 item 1/2/3） |
| 2026-09-17 | P1-3 860–862 Process 也会在提议者那边叫拆句（351 item 1/2/3） |
| 2026-09-17 | P1-3 863–865 一轮一份扩展拆句（350 item 1/2/3） |
| 2026-09-17 | P1-3 866–868 Req 9 无副作用拆句（349 item 1/2/3） |
| 2026-09-17 | P1-3 869–871 Req 6 Extend–Verify 一致性拆句（348 item 1/2/3） |
| 2026-09-17 | P1-3 872–874 Req 3 Prepare–Process 一致性拆句（347 item 1/2/3） |
| 2026-09-17 | P1-3 875–877 ABCI 2.0 协调升级拆句（346 item 1/2/3） |
| 2026-09-17 | P1-3 878–880 Req 2 Prepare 回包上限拆句（345 item 1/2/3） |
| 2026-09-17 | P1-3 881–883 MaxBytes 开销与投递拆句（344 item 1/2/3） |
| 2026-09-17 | P1-3 884–886 PbtsEnableHeight 拆句（343 item 1/2/3） |
| 2026-09-17 | P1-3 887–889 FinalizeBlock 确定性拆句（342 item 1/2/3） |
| 2026-09-17 | P1-3 890–892 VerifyVoteExtension 确定性拆句（341 item 1/2/3） |
| 2026-09-17 | P1-3 893–895 ProcessProposal 确定性拆句（340 item 1/2/3） |
| 2026-09-17 | P1-3 896–898 Prepare/ExtendVote 无确定性拆句（338 item 1/2/3） |
| 2026-09-17 | P1-3 899–901 PrepareProposal 及时性拆句（327 item 1/2/3） |
| 2026-09-17 | P1-3 902–904 Finalize 落盘禁令拆句（335 item 1/2/3） |
| 2026-09-17 | P1-3 905–907 ValidatorUpdate 拆句（318 item 1/2/3） |
| 2026-09-17 | P1-3 908–910 ConsensusParams 更新拆句（319 item 1/2/3） |
| 2026-09-17 | P1-3 911–913 ConsensusParams 生效延迟拆句（333 item 1/2/3） |
| 2026-09-17 | P1-3 914–916 MaxGas 气限拆句（315 item 1/2/3） |
| 2026-09-17 | P1-3 917–919 BlockParams.MaxBytes 上限拆句（337 item 1/2/3） |
| 2026-09-17 | P1-3 920–922 EvidenceParams.MaxBytes 拆句（331 item 1/2/3） |
| 2026-09-17 | P1-3 923–925 SynchronyParams Precision/MessageDelay 拆句（336 item 1/2/3） |
| 2026-09-17 | P1-3 926–928 VoteExtensionsEnableHeight 拆句（330 item 1/2/3） |
| 2026-09-17 | P1-3 929–931 CheckTx 弱过滤器拆句（339 item 1/2/3） |
| 2026-09-17 | P1-3 932–934 Snapshot Connection 可选拆句（334 item 1/2/3） |
| 2026-09-17 | P1-3 935–937 Snapshot Verification 早验拆句（332 item 1/2/3） |
| 2026-09-17 | P1-3 938–940 Query 本地读拆句（329 item 1/2/3） |
| 2026-09-17 | P1-3 941–943 CheckTx 最终不再振荡拆句（328 item 1/2/3） |
| 2026-09-17 | P1-3 944–946 Peer Filtering 两道查询拆句（326 item 1/2/3） |
| 2026-09-17 | P1-3 947–949 Query Proofs 三锚拆句（325 item 1/2/3） |
| 2026-09-17 | P1-3 950–952 Taking Snapshots 拍后交差拆句（324 item 1/2/3） |
| 2026-09-17 | P1-3 953–955 Transition to Consensus 截断历史拆句（323 item 1/2/3） |
| 2026-09-17 | P1-3 956–958 Snapshot Discovery 每节点 10 份拆句（322 item 1/2/3） |
| 2026-09-17 | P1-3 959–961 Snapshot Restoration 收下未装完拆句（321 item 1/2/3） |
| 2026-09-17 | P1-3 962–964 QueryState 只读副本拆句（314 item 1/2/3） |
| 2026-09-17 | P1-3 965–967 Replay Protection 尽力去重拆句（313 item 1/2/3） |
| 2026-09-17 | P1-3 968–970 CheckTxState 两份状态拆句（312 item 1/2/3） |
| 2026-09-17 | P1-3 971–973 候选状态 立刻执行拆句（311 item 1/2/3） |
| 2026-09-17 | P1-3 974–976 Commit 锁与 RPC 拆句（310 item 1/2/3） |
| 2026-09-17 | P1-3 977–979 ABCI 传输四门拆句（307 item 1/2/3） |
| 2026-09-17 | P1-3 980–982 WAL 写下与回放拆句（298 item 1/2/3） |
| 2026-09-17 | P1-3 983–985 本地 State 与流言拆句（300 item 1/2/3） |
| 2026-09-17 | P1-3 986–988 创世文件与应用段拆句（303 item 1/2/3） |
| 2026-09-17 | P1-3 989–991 先装证据与两条上限拆句（299 item 1/2/3） |
| 2026-09-17 | P1-3 992–994 提案收了与 commit 后再验拆句（301 item 1/2/3） |
| 2026-09-17 | P1-3 995–997 同一高度换轮与新加入拆句（302 item 1/2/3） |
| 2026-09-17 | P1-3 998–1000 票上时间戳与冲突提案拆句（304 item 1/2/3） |
| 2026-09-17 | P1-3 1001–1003 InitPeer 与 Receive 先于 AddPeer 拆句（305 item 1/2/3） |
| 2026-09-17 | P1-3 1004–1006 Peer 句柄与 Broadcast 回通道拆句（306 item 1/2/3） |
| 2026-09-17 | P1-3 1007–1009 NumPeers 与按名拿到反应堆拆句（308 item 1/2/3） |
| 2026-09-17 | P1-3 1010–1012 HasChannel 与 Send/TrySend 回假拆句（309 item 1/2/3） |
| 2026-09-17 | P1-3 1013–1015 ExecTxResult 列表与 Code 非零拆句（316 item 1/2/3） |
| 2026-09-17 | P1-3 1016–1018 CheckTxResponse Data 与 Priority 拆句（317 item 1/2/3） |
| 2026-09-17 | P1-3 1019–1021 Crash Recovery 应用领先与三步拆句（320 item 1/2/3） |
| 2026-09-17 | P1-3 1022–1024 ExtendVoteRequest hash/height/time 拆句（410 item 1/2/3） |
| 2026-09-17 | P1-3 1025–1027 ProcessProposalRequest txs/hash/height 拆句（419 item 1/2/3） |
| 2026-09-17 | P1-3 1028–1030 ProcessProposalRequest last_commit/time/misbehavior 拆句（420 item 1/2/3） |
| 2026-09-17 | P1-3 1031–1033 ExtendVote 请求对应与 ACCEPT 拆句（409 item 1/2/3） |
| 2026-09-17 | P1-3 1034–1036 ExtendVoteRequest txs/last_commit/next_hash 拆句（411 item 1/2/3） |

下一批默认：**P1-3 ABCI++ 不变量 1037+**（继续 cometbft 拆句）。  
唤醒后先跑 `python3 tools/review_audit.py`，见 [`REVIEW_LOOP.md`](REVIEW_LOOP.md)。

---

## 禁止事项（GOAL 重申）

- 不在 `qtb/` 写协议教材
- 决策矩阵禁止填「愿望」；必须标 事实 / 推断 / 建议
- 不出题进正文；exams 后置
- 不把 benchmark TPS 当事实
