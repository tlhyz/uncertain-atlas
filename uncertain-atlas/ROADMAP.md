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
2. CometBFT ABCI++ 不变量拆完（目标 ~793 句；当前 ~1487）。
3. 决策矩阵「不确定候选」列填完**建议档**（非最终选型）。
4. 对抗语料 C01–C1465+ 有 runner，能批量扫描文案/测试钩子。
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
| 不变量库 | 1487+ 可测试句；ABCI++ 主线 | 进行中（强） |
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
| P1-3 | ABCI++ 拆完 677–1114；BIP-44/43/85/49/48/45/67/86/89/383/386/381/382/387/371/388/384/385/328/373/87/129/88/78/69/94/325/127/137/70/38/13/321/322/352/353/47/30/147/155/130/133/338/434/339/330/159/144/111/35/61/31/14/324/157/158 1115–1282；EIP-8 1283–1285；EIP-2124 1286–1288；EIP-778 1289–1291；EIP-868 1292–1294；EIP-100 1295–1297；EIP-150 1298–1300；EIP-658 1301–1303；PrepareUsage 1304–1306；PrepareNochecks 1307–1309；PrepareWhen 1310–1312；PrepareWhenRet 1313–1315；SuggestValidate 1316–1318；LateUnverified 1319–1321；LateMay 1322–1324；VerifyDiscard 1325–1327；VerifyCall 1328–1330；VerifyStatusWhen 1331–1333；VerifyKeep 1334–1336；VerifyAcceptDef 1337–1339；ProcAcceptDef 1340–1342；ExtWhenBcast 1343–1345；EIP-2 Homestead 1346–1349；ExtAppGen 1350–1352；CiNotes 1353–1355；ExtCiNotes 1356–1358；CiFields 1359–1361；ExecTxEv 1362–1364；ExtViUse 1365–1367；PrepEv 1368–1370；ValUse 1371–1373；ViAvail 1374–1376；EIP-7 DELEGATECALL 1377–1379；EIP-140 REVERT 1380–1382；EIP-214 STATICCALL 1383–1385；EIP-211 returndata 1386–1388；EIP-1014 CREATE2 1389–1391；EIP-1052 EXTCODEHASH 1392–1394；EIP-1344 CHAINID 1395–1397；EIP-3198 BASEFEE 1398–1400；EIP-7516 BLOBBASEFEE 1401–1403；EIP-145 SHIFT 1404–1406；EIP-3855 PUSH0 1407–1409；EIP-5656 MCOPY 1410–1412；EIP-3529 refund 1413–1415；EIP-6049 deprecate 1416–1418；EIP-2200 net-meter 1419–1421；EIP-2028 calldata-cut 1422–1424；EIP-2565 modexp-price 1425–1427；EIP-1108 bn128-cut 1428–1430；EIP-1884 SELFBALANCE 1431–1433；EIP-152 BLAKE2F 1434–1436；EIP-3860 initcode 1437–1439；EIP-170 returned 1440–1442；EIP-3541 reserved-prefix 1443–1445；EIP-3651 coinbase 1446–1448；EIP-2929 cold-vs-warm 1449–1451；EIP-2930 listed 1452–1454；EIP-2718 typed-envelope 1455–1457；EIP-7935 default-gas 1458–1460；EIP-7825 tx-gas-cap 1461–1463；EIP-7934 rlp-cap 1464–1466；EIP-7623 calldata-floor 1467–1469；EIP-7939 clz 1470–1472；EIP-7823 modexp-bound 1473–1475；EIP-7928 block-list 1476–1478；EIP-7044 exit-domain 1479–1481；EIP-7917 lookahead 1482–1484；EIP-1559 basefee-vs-tip 1485–1487 | AUDIT_LOG 连续；invariants README 更新 |
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
| 2026-09-17 | P1-3 1037–1039 ExtendVoteRequest misbehavior/proposer/validator 拆句（413 item 1/2/3） |
| 2026-09-17 | P1-3 1040–1042 FinalizeBlockRequest decided_last_commit/height/txs 拆句（422 item 1/2/3） |
| 2026-09-17 | P1-3 1043–1045 ExtendedVoteInfo vote_extension/non_rp/signature 拆句（421 item 1/2/3） |
| 2026-09-17 | P1-3 1046–1048 PrepareProposalRequest max_tx_bytes/txs/height 拆句（423 item 1/2/3） |
| 2026-09-17 | P1-3 1049–1051 PrepareProposalRequest local_last_commit/time/misbehavior 拆句（424 item 1/2/3） |
| 2026-09-18 | P1-3 1052–1054 ExtendedVoteInfo validator/block_id_flag/non_rp_sig 拆句（425 item 1/2/3） |
| 2026-09-18 | P1-3 1055–1057 PrepareProposalRequest next_validators_hash/proposer + Finalize time 拆句（426 item 1/2/3） |
| 2026-09-18 | P1-3 1058–1060 ProcessProposalRequest next_validators_hash/proposer + Prepare resp txs 拆句（427 item 1/2/3） |
| 2026-09-18 | P1-3 1061–1063 FinalizeBlockRequest hash/misbehavior/next_validators_hash 拆句（428 item 1/2/3） |
| 2026-09-18 | P1-3 1064–1066 FinalizeBlockRequest proposer/time/syncing_to_height 拆句（429 item 1/2/3） |
| 2026-09-18 | P1-3 1067–1069 ProcessProposalResponse.status / exclusive / SHOULD Accept 拆句（430 item 1/2/3） |
| 2026-09-18 | P1-3 1070–1072 FinalizeBlockResponse events/tx_results/validator_updates 拆句（431 item 1/2/3） |
| 2026-09-18 | P1-3 1073–1075 FinalizeBlockResponse cparam/app_hash/next_block_delay 拆句（432 item 1/2/3） |
| 2026-09-18 | P1-3 1076–1078 VerifyVoteExtensionResponse.status / exclusive / SHOULD Accept 拆句（433 item 1/2/3） |
| 2026-09-18 | P1-3 1079–1081 VerifyVoteExtensionRequest validator_address/non_rp/raw-sign 拆句（436 item 1/2/3） |
| 2026-09-18 | P1-3 1082–1084 ExtendVoteResponse vote_extension/non_rp + Verify non_rp 拆句（418 item 1/2/3） |
| 2026-09-18 | P1-3 1085–1087 Verify When unsigned-discard / call / ACCEPT-REJECT 拆句（435 item 1/2/3） |
| 2026-09-18 | P1-3 1088–1090 VerifyVoteExtensionRequest height/hash/vote_extension 拆句（415 item 1/2/3） |
| 2026-09-18 | P1-3 1091–1093 InitChain once / may-choose-set / Validators-as-update 拆句（412 item 1/2/3） |
| 2026-09-18 | P1-3 1094–1096 Process When ProposeTimeout / header-first / prevote-or-nil 拆句（416 item 1/2/3） |
| 2026-09-18 | P1-3 1097–1099 头字段 Prepare-first / Process h-t / Finalize h-t 拆句（417 item 1/2/3） |
| 2026-09-18 | P1-3 1100–1102 Finalize app_hash empty-det / Query 锚 / Code==0 拆句（404 item 1/2/3） |
| 2026-09-18 | P1-3 1103–1105 CheckTx 守卫 / 来源不重放 / 自描述 type 拆句（405 item 1/2/3） |
| 2026-09-18 | P1-3 1106–1108 Snapshot.height / metadata / Query 可选证明 拆句（406 item 1/2/3） |
| 2026-09-18 | P1-3 1109–1111 Finalize 刚决定字段 / 必须确定 / Info 回应用状态 拆句（407 item 1/2/3） |
| 2026-09-18 | P1-3 1112–1114 Finalize 执行再交还 / Process 全部执行信息 / 整块像 Finalize 拆句（408 item 1/2/3） |
| 2026-09-18 | P1-3 1115–1117 BIP-44 种子树 / 账户过往 / 发现停搜 拆句（267 item 1/2/3）；479 已用 fintrigger 608–610，不重拆 |
| 2026-09-18 | P1-3 1118–1120 BIP-43 兼容声明 / 子集结构 / 同一前缀 拆句（266 item 1/2/3） |
| 2026-09-18 | P1-3 1121–1123 BIP-85 一份备份 / 根钥不能倒回 / 派生熵不是目标种子 拆句（286 item 1/2/3） |
| 2026-09-18 | P1-3 1124–1126 BIP-49 旧账户再编码 / 专用账户不向后兼容 / 账户出现仍未齐 拆句（268 item 1/2/3） |
| 2026-09-18 | P1-3 1127–1129 BIP-48 现有习惯不搬家 / 脚本类型不是账户 / 本页多签仍排序 拆句（269 item 1/2/3） |
| 2026-09-18 | P1-3 1130–1132 BIP-45 共享主公钥不是本页 / 独立长地址不能独立签 / 前面分支没有交易仍未扫完 拆句（271 item 1/2/3） |
| 2026-09-18 | P1-3 1133–1135 BIP-67 同一套钥不是同一条地址 / 只共享门限仍未够 / 未压缩钥不是本页 拆句（270 item 1/2/3） |
| 2026-09-18 | P1-3 1136–1138 BIP-86 派生钥不是输出钥 / 不需要脚本路径仍承诺 / 种子备份仍未找回 拆句（272 item 1/2/3） |
| 2026-09-18 | P1-3 1139–1141 BIP-89 共享扩展公钥不是链码委托 / 非扩展钥推不出整棵树 / 本笔微调不是盲签 拆句（289 item 1/2/3） |
| 2026-09-18 | P1-3 1142–1144 BIP-383 multi 不是 sortedmulti / 门限不是同一套上限 / 多把扩展钥不是各自编号 拆句（274 item 1/2/3） |
| 2026-09-18 | P1-3 1145–1147 BIP-386 tr 没有树不是脚本路径 / 树表达式不是旧套法 / 压缩钥不是 x-only 拆句（275 item 1/2/3） |
| 2026-09-18 | P1-3 1148–1150 BIP-381 pk 不是同一套放置 / sh 产出不是已经有赎回 / 眼熟不是已经兼容 拆句（276 item 1/2/3） |
| 2026-09-18 | P1-3 1151–1153 BIP-382 wpkh/wsh 不是只能顶层 / 未压缩钥不是已经允许 / wsh 产出不是已经有见证脚本 拆句（277 item 1/2/3） |
| 2026-09-18 | P1-3 1154–1156 BIP-387 multi_a 不是 383 那种 multi / 门限不是同一套编码 / sortedmulti_a 不是 383 那种排序 拆句（278 item 1/2/3） |
| 2026-09-18 | P1-3 1157–1159 BIP-371 旧 PSBT 栏不是已经能装 Taproot / 输出脚本钥不是内部钥 / Taproot 输入不是必须带整笔前交易 拆句（279 item 1/2/3） |
| 2026-09-18 | P1-3 1160–1162 BIP-388 钱包策略不是一条描述符 / 钥占位不是精确公钥 / 登记过不是批准这笔花 拆句（280 item 1/2/3） |
| 2026-09-18 | P1-3 1163–1165 BIP-384 combo 不是一种脚本 / 未压缩钥不是带齐见证对 / 一份 combo 不是一份钱包策略 拆句（281 item 1/2/3） |
| 2026-09-18 | P1-3 1166–1168 BIP-385 raw 不是具名表达式 / addr 不是已经写了输出脚本 / 一份包装不是 combo 拆句（282 item 1/2/3） |
| 2026-09-18 | P1-3 1169–1171 BIP-328 聚合钥不是扩展公钥 / 合成扩展公钥不是已经能硬化 / 子钥不是已经能不带微调去签 拆句（283 item 1/2/3） |
| 2026-09-18 | P1-3 1172–1174 BIP-373 旧栏不是已经能装 MuSig2 / 聚合钥栏不是输出钥 / 参与者钥不是已经有部分签 拆句（284 item 1/2/3） |
| 2026-09-18 | P1-3 1175–1177 BIP-87 脚本各走各的路径不是多签树 / 路径里的脚本类型不是已经必要 / 主种子不是已经够找回 拆句（285 item 1/2/3） |
| 2026-09-18 | P1-3 1178–1180 BIP-129 部分签名包不是跨厂开户 / 指纹对上不是已经核过 KEY / TOKEN 不是已经是钱包种子 拆句（287 item 1/2/3） |
| 2026-09-18 | P1-3 1181–1183 BIP-88 一条路径不是模板 / 写死熟路径不是已经能互操作 / 完整模板不是半截模板 拆句（288 item 1/2/3） |
| 2026-09-18 | P1-3 1184–1186 BIP-78 pj= 不是已经是 payjoin 付款 / 原始包不是提案 / 加输入不是已经另开一笔 拆句（290 item 1/2/3） |
| 2026-09-18 | P1-3 1187–1189 BIP-69 习惯顺序不是字典序标准 / 字典序不是已经是共识 / 字典序不是已经私人 拆句（291 item 1/2/3） |
| 2026-09-18 | P1-3 1190–1192 BIP-94 Testnet 4 不是 Testnet 3 / 20 分钟例外不是已经没有块风暴 / 会 Testnet 3 不是已经能安全跟 拆句（292 item 1/2/3） |
| 2026-09-18 | P1-3 1193–1195 BIP-325 signet 不是 testnet / 不是 regtest / 头上工作量不是已经签过 拆句（265 item 1/2/3） |
| 2026-09-18 | P1-3 1196–1198 BIP-127 储备证明交易不是已经能花 / 其余输入签过不是 258 控制 / POR 栏不是已经是普通花费 拆句（293 item 1/2/3） |
| 2026-09-18 | P1-3 1199–1201 BIP-137 本页这种签不是已经是 322 / 头字节不是已经有地址 / 旧 P2PKH 习惯不是已经互操作 拆句（294 item 1/2/3） |
| 2026-09-18 | P1-3 1202–1204 BIP-70 付款请求不是已经授权 / 付款报文不是已经是回执 / 回执不是已经最终 拆句（295 item 1/2/3） |
| 2026-09-18 | P1-3 1205–1207 BIP-38 加密私钥记录不是已经能用 / 厂家代生成不是已经能兑 / 地址哈希片段不是已经是地址 拆句（296 item 1/2/3） |
| 2026-09-18 | P1-3 1208–1210 BIP-13 本页这种地址不是已经是 16 / 旧软件报无效不是已经付过 / 只有地址不是已经知道付给谁 拆句（297 item 1/2/3） |
| 2026-09-18 | P1-3 1211–1213 BIP-321 付款 URI 不是已经授权 / 路径空不是已经没有指示 / 不认识的必选参数不是已经能付 拆句（255 item 1/2/3） |
| 2026-09-18 | P1-3 1214–1216 BIP-322 签过的消息不是已经控制资金 / 发票将来控制不是已经证明上一笔 / 资金证明清单不是已经齐 拆句（258 item 1/2/3） |
| 2026-09-18 | P1-3 1217–1219 BIP-352 静默付款地址不是已经有输出 / 扫过不是已经收到 / 再用不是已经同一笔 拆句（260 item 1/2/3） |
| 2026-09-18 | P1-3 1220–1222 BIP-353 可读名字不是已经该走 DNS / TXT 不是已经合法指示 / 缓存复制不是已经当前 URI 拆句（261 item 1/2/3） |
| 2026-09-18 | P1-3 1223–1225 BIP-47 付款码不是已经是存款地址 / 通知输出不是已经能花 / 第一次付款不是已经不必再通知 拆句（273 item 1/2/3） |
| 2026-09-18 | P1-3 1226–1228 BIP-30 同一交易标识不是已经唯一 / 还没花光再装不是已经合法 / 花光后再出现不是已经非法 拆句（257 item 1/2/3） |
| 2026-09-18 | P1-3 1229–1231 BIP-147 多余栈元素不是已经随便填 / 隔离见证不是已经没有这条延展 / 转发策略不是已经是共识 拆句（264 item 1/2/3） |
| 2026-09-18 | P1-3 1232–1234 BIP-155 后继地址流言不是已经连得上 / sendaddrv2 不是已经只收后继格式 / 传了某种网不是已经连上那种网 拆句（246 item 1/2/3） |
| 2026-09-18 | P1-3 1235–1237 BIP-130 发了 sendheaders 不是已经改用头通告 / 许可不是已经照做 / 头通告新尖不是已经有块 拆句（247 item 1/2/3） |
| 2026-09-18 | P1-3 1238–1240 BIP-133 跳过库存通告不是已经拒进池 / 许可不是已经照做 / 布隆过了不是已经过了费率门 拆句（245 item 1/2/3） |
| 2026-09-18 | P1-3 1241–1243 BIP-338 版本关掉转发不是已经终身只传块 / 发了本页不是已经没有紧凑块 / 建议关掉地址不是已经禁止 拆句（256 item 1/2/3） |
| 2026-09-18 | P1-3 1244–1246 BIP-434 协议版本够了不是已经支持某项功能 / 通告了 feature 不是已经启用 / verack 之后才来的 feature 不是已经是本页协商 拆句（259 item 1/2/3） |
| 2026-09-18 | P1-3 1247–1249 BIP-339 按 wtxid 通告不是已经有那笔交易 / 发了 wtxidrelay 不是已经改口 / 仍用旧类型要父交易不是旧库存已经退役 拆句（248 item 1/2/3） |
| 2026-09-18 | P1-3 1250–1252 BIP-330 一次对账不是已经有那些交易 / 发了 sendtxrcncl 不是已经在对账 / 对账失败退回洪水不是库存通告已经退役 拆句（249 item 1/2/3） |
| 2026-09-18 | P1-3 1253–1255 BIP-159 有限服务位不是已经能服任意旧块 / 有限位不是已经剪枝 / 服了最近一块不是已经暴露剪点 拆句（250 item 1/2/3） |
| 2026-09-18 | P1-3 1256–1258 BIP-144 带见证的线上序列化不是已经有见证 / 开了能提供见证那一位不是已经在传 / 库存通告仍用旧类型不是线上已经没有见证 拆句（251 item 1/2/3） |
| 2026-09-18 | P1-3 1259–1261 BIP-111 开了布隆服务位不是已经私人 / 没开不是全网已经退役 / 协议版本够了不是已经在遵守 拆句（252 item 1/2/3） |
| 2026-09-18 | P1-3 1262–1264 BIP-35 回了一串库存不是已经有那些交易 / 只肯给最近转发过的不是已经支持整池查询 / 协议版本够了不是已经在答 拆句（253 item 1/2/3） |
| 2026-09-18 | P1-3 1265–1267 BIP-61 拒收不是已经共识非法 / 拒收理由不是已经该弹给用户 / 策略拒收不是已经共识非法 拆句（254 item 1/2/3） |
| 2026-09-18 | P1-3 1268–1270 BIP-31 协议版本够了不是已经会带 nonce 的 ping / pong 不是已经对上那一次 / 回了 pong 不是已经还活着 拆句（262 item 1/2/3） |
| 2026-09-18 | P1-3 1271–1273 BIP-14 协议版本不是已经是客户端版本 / user agent 不是已经可以按实现改行为 / 同一协议版本不是已经是同一套实现 拆句（263 item 1/2/3） |
| 2026-09-18 | P1-3 1274–1276 BIP-324 线上在加密不是已经私人 / 字节看起来随机不是已经认不出 / 支持第 2 版不是已经退役旧线 拆句（242 item 1/2/3） |
| 2026-09-18 | P1-3 1277–1279 BIP-157 过滤器对上不是已经有块 / 过滤器头链对上不是已经写进共识 / 支持客户端侧过滤不是已经验完脚本 拆句（243 item 1/2/3） |
| 2026-09-18 | P1-3 1280–1282 BIP-158 装了花费脚本不是已经有交易 / 对上不是已经在集合里 / 排除 OP_RETURN 不是已经写进共识 拆句（244 item 1/2/3） |
| 2026-09-18 | P1-3 1283–1285 EIP-8 忽略 hello 版本不是已经在说新协议 / 发现能吞多余字段不是已经升级发现 / 能收新握手不是已经退役旧握手 拆句（235 item 1/2/3） |
| 2026-09-18 | P1-3 1286–1288 EIP-2124 分叉哈希对上不是已经同一条链 / 通告了下一分叉不是已经兼容 / 有了分叉标识不是已经改了共识 拆句（239 item 1/2/3） |
| 2026-09-18 | P1-3 1289–1291 EIP-778 能多写键被收下不是已经解释这些键 / 签过的记录不是已经是最新一份 / 默认方案名不是已经换了发现协议 拆句（240 item 1/2/3） |
| 2026-09-18 | P1-3 1292–1294 EIP-868 ping 里有序号不是已经拿到当前记录 / 能发请求不是已经解析完 / FindNode 找到人不是已经有当前记录 拆句（241 item 1/2/3） |
| 2026-09-18 | P1-3 1295–1297 EIP-100 难度把叔块算进去不是已经改了出块奖励 / 头上叔块哈希不是空不是已经数清个数 / 改了分母不是已经量过墙钟 拆句（238 item 1/2/3） |
| 2026-09-18 | P1-3 1298–1300 EIP-150 读树涨价不是已经是磁盘常数时间 / 问超了不是已经耗尽气 / 建议气限不是已经是协议帽 拆句（237 item 1/2/3） |
| 2026-09-18 | P1-3 1301–1303 EIP-658 状态码不是还印着中间状态根 / 还剩气不是已经成功 / RPC 能告诉你成没成不是收据里已经有状态码 拆句（236 item 1/2/3） |
| 2026-09-18 | P1-3 1304–1306 PrepareUsage raw proposal 不是已经 Prepare 改列表 / MAY 超上限不是已经 Req 2 / MUST remove 不是已经引擎会帮你裁 拆句（503 item 1/2/3） |
| 2026-09-18 | P1-3 1307–1309 PrepareNochecks 不再做额外检查不是已经验过重复 / 回包验不过崩溃不是 Process REJECT / MAY 非确定不是必须确定 拆句（504 item 1/2/3） |
| 2026-09-18 | P1-3 1310–1312 PrepareWhen 按优先级收池造头不是 raw proposal / 同步调用不是能返回后再改 / 可以改列表不是 Prepare 改列表 拆句（505 item 1/2/3） |
| 2026-09-18 | P1-3 1313–1315 PrepareWhenRet 回包带列表不是 raw proposal / 返回不是 Process 紧跟 Prepare / 用改过的块当提案不是 validValue 跳过 拆句（506 item 1/2/3） |
| 2026-09-18 | P1-3 1316–1318 SuggestValidate 建议自验不是 must Accept / 同款逻辑不是 step 2 call / 不是引擎再 Verify 不是已经 Verify 过 拆句（520 item 1/2/3） |
| 2026-09-18 | P1-3 1319–1321 LateUnverified +2/3 未 Verify 不是 352 bundled / MAY 用扩展不是已经 Verify / 建议再看不是引擎会再 Verify 拆句（519 item 1/2/3） |
| 2026-09-18 | P1-3 1322–1324 LateMay MAY 写入不再 Verify 不是 352 bundled / round 0 h-1 不是正常 When / 不再叫不是已经又 Verify 拆句（518 item 1/2/3） |
| 2026-09-18 | P1-3 1325–1327 VerifyDiscard 无有效签丢掉不是 Verify When bundled / 0 长有效签不是仍叫 Verify / step 1 在 call 前不是已经验过 拆句（514 item 1/2/3） |
| 2026-09-18 | P1-3 1328–1330 VerifyCall Else 调 Verify 不是 Verify When bundled / 收到他人票不是本地也 Verify / step 2 在回 status 前不是已经 Accept 拆句（515 item 1/2/3） |
| 2026-09-18 | P1-3 1331–1333 VerifyStatusWhen 回 status 不是 Verify When bundled / step 3 在 call 后不是 step 2 call / 在 keep 前不是已经写进 last_commit 拆句（516 item 1/2/3） |
| 2026-09-18 | P1-3 1334–1336 VerifyKeep ACCEPT 留下不是已写 last_commit / h+1 Prepare 填不是已进块 / REJECT 丢掉不是 step 1 discard 拆句（517 item 1/2/3） |
| 2026-09-18 | P1-3 1337–1339 VerifyAcceptDef SHOULD Accept 默认不是不能 Reject / REJECT 路径不是不能 Reject / 默认不是 341 通则 拆句（529 item 1/2/3） |
| 2026-09-18 | P1-3 1340–1342 ProcAcceptDef SHOULD Accept 默认不是不能 Reject / REJECT assumes not valid 不是不能 Reject / 默认不是 340 通则 拆句（532 item 1/2/3） |
| 2026-09-18 | P1-3 1343–1345 ExtWhenBcast 广播不是 constructs Precommit / step 7 顺序不是 construct CanonicalVote / 广播不是 last_commit 拆句（513 item 1/2/3） |
| 2026-09-18 | P1-3 1346–1349 Homestead 交易创建费不是改 CREATE / 拒高 s 不是预编译拒 / 失败不留空合约不是限制代码 / 难度朝均值不是取消炸弹 拆句（234 item 1/2/3/4） |
| 2026-09-18 | P3-3 库存 285 remote / 211 祖先 / 74 平行 / 107 缺失；unique 9 簇回收；不删 remote |
| 2026-09-18 | P1-3 1350–1352 ExtAppGen 应用生成将签名不是已经签过 / non_rp 不是同一签法 / 将挂上不是已经广播 拆句（439 item 1/2/3） |
| 2026-09-18 | P1-3 1353–1355 CiNotes 按投票权降序不是已经进块 / 引擎保证不是应用排过 / 从 store 再装不是从块抽出 拆句（444 item 1/2/3） |
| 2026-09-18 | P1-3 1356–1358 ExtCiNotes Extended 按投票权降序不是已经进块 / 引擎保证不是应用排过 / 从 store 再装不是从块抽出 拆句（441 item 1/2/3） |
| 2026-09-18 | P1-3 1359–1361 CiFields round 不是已经按投票权排 / votes 列表不是已经进块 / Fields 栏不是 Notes 票序 拆句（445 item 1/2/3） |
| 2026-09-18 | P1-3 1362–1364 ExecTxEv 索引事件不是印进本头 / 非确定不是 Code-Data / 逐笔不是块级 events 拆句（446 item 1/2/3） |
| 2026-09-18 | P1-3 1365–1367 ExtViUse 引擎已验可空不是应用验完 / 暴露再处理不是已 Verify / 两份签空切片不是只有一份 拆句（447 item 1/2/3） |
| 2026-09-18 | P1-3 1368–1370 PrepEv MAY 产出不是回包交回 / MUST 留到决定不是 Process 就交 / Finalize 交回不是 CheckTx events 拆句（448 item 1/2/3） |
| 2026-09-18 | P1-3 1371–1373 ValUse Process CommitInfo 不是 Prepare Extended / Finalize decided 不是 Process proposed / Prepare Extended 不是 CommitInfo 拆句（449 item 1/2/3） |
| 2026-09-18 | P1-3 1374–1376 ViAvail availability 同句不是已经奖罚完 / VoteInfo from block 不是 local / ExtendedVoteInfo local 不是 from block 拆句（442 item 1/2/3） |
| 2026-09-18 | P1-3 1377–1379 EIP-7 DELEGATECALL 不是已经是 CALLCODE / 父作用域发送者不是普通 CALL / 可变代码源不是 7702 拆句（233 item 1/2/3） |
| 2026-09-18 | P1-3 1380–1382 EIP-140 REVERT 带回剩余气不是非法指令烧光 / 付不起自己的费不是留下剩余气 / 创建里回滚不是已经部署 拆句（177 item 1/2/3） |
| 2026-09-18 | P1-3 1383–1385 EIP-214 STATICCALL 静态帧不是 view / 没转账不是已经静态 / 静态里改状态不是已经改成 拆句（178 item 1/2/3） |
| 2026-09-18 | P1-3 1386–1388 EIP-211 返回缓冲不是内存 / 本页不是 calldata / 再取失败数据不是已经是 140 拆句（232 item 1/2/3） |
| 2026-09-18 | P1-3 1389–1391 EIP-1014 CREATE2 不是按序号占址 / 算出盐地址不是已经创建 / 碰撞可能不是已经覆盖 拆句（222 item 1/2/3） |
| 2026-09-18 | P1-3 1392–1394 EIP-1052 EXTCODEHASH 不是已经看见代码 / 返回 0 不是没代码账户 / 空数据哈希不是账户不存在 拆句（221 item 1/2/3） |
| 2026-09-18 | P1-3 1395–1397 EIP-1344 CHAINID 不是已经签进哈希 / 返回配置链号不是这笔已绑 155 / 编译期写死不是分叉后仍安全 拆句（220 item 1/2/3） |
| 2026-09-18 | P1-3 1398–1400 EIP-3198 BASEFEE 不是已经改了费用市场 / 能读本块基础费不是已经给了出块者 / 跑前就有这个数不是已经改了头 拆句（218 item 1/2/3） |
| 2026-09-18 | P1-3 1401–1403 EIP-7516 BLOBBASEFEE 不是已经是 3198 / 能读 blob 基础费不是已经并成一套气 / 跑前就有这个数不是已经改了 4844 拆句（219 item 1/2/3） |
| 2026-09-18 | P1-3 1404–1406 EIP-145 SHIFT 不是已经用算术拼过 / 算术右移不是已经是有符号除 / 更便宜不是已经是位域产品 拆句（231 item 1/2/3） |
| 2026-09-18 | P1-3 1407–1409 EIP-3855 PUSH0 不是已经是带立即数的压 0 / 没有立即数不是已经改了跳转分析 / 旧字节碰巧用了这个码不是行为已经不变 拆句（217 item 1/2/3） |
| 2026-09-18 | P1-3 1410–1412 EIP-5656 MCOPY 不是已经是身份预编译 / 像缓冲不是必须真分配 / 能重叠拷不是已经是 calldata 拷 拆句（216 item 1/2/3） |
| 2026-09-18 | P1-3 1413–1415 EIP-3529 refund 不是已经没有退款 / 去掉自毁退款不是已经改了自毁语义 / 退款计数不是执行当中能用 拆句（223 item 1/2/3） |
| 2026-09-18 | P1-3 1416–1418 EIP-6049 deprecate 不是已经改了共识 / 元层页不是已经改了客户端 / 以后可能变不是已经变了 拆句（224 item 1/2/3） |
| 2026-09-18 | P1-3 1419–1421 EIP-2200 net-meter 不是已经是瞬时存储 / 三值不是已经只有当前值 / 津贴帧禁写不是已经能改槽 拆句（225 item 1/2/3） |
| 2026-09-18 | P1-3 1422–1424 EIP-2028 calldata-cut 不是已经给零字节也降价 / 降价不是已经没有块上限 / 降价不是已经不伤延迟安全 拆句（226 item 1/2/3） |
| 2026-09-18 | P1-3 1425–1427 EIP-2565 modexp-price 不是已经是 198 公式 / 更便宜不是已经改了接口 / 最低气价不是已经无限便宜 拆句（227 item 1/2/3） |
| 2026-09-18 | P1-3 1428–1430 EIP-1108 bn128-cut 不是已经换了算法 / 更便宜不是已经在验签 / 本页不是已经是通用曲线算术 拆句（228 item 1/2/3） |
| 2026-09-18 | P1-3 1431–1433 EIP-1884 SELFBALANCE 不是已经是按地址查余额 / 给自己查不是已经按本账户价扣 / 涨价不是已经是本笔冷热 拆句（229 item 1/2/3） |
| 2026-09-18 | P1-3 1434–1436 EIP-152 BLAKE2F 不是已经是哈希 / 本页不是已经能验 Equihash / 定长输入不是已经是任意哈希 API 拆句（230 item 1/2/3） |
| 2026-09-18 | P1-3 1437–1439 EIP-3860 initcode 不是已经是 170 运行时界 / 创建交易超界不是已经是 CREATE 失败 / 分析费不是已经跑完 拆句（176 item 1/2/3） |
| 2026-09-18 | P1-3 1440–1442 EIP-170 returned 不是已经是 initcode 超界 / 耗尽气不是已经整笔非法 / 常数 CALL 气不是已经免费 拆句（185 item 1/2/3） |
| 2026-09-18 | P1-3 1443–1445 EIP-3541 reserved-prefix 不是已经是对象格式已部署 / 已有同首字节不是已经被改 / initcode 出现该字节不是已经是本页失败 拆句（188 item 1/2/3） |
| 2026-09-18 | P1-3 1446–1448 EIP-3651 coinbase 不是已经访问过 / 开跑已热不是已经付钱 / 开跑已热不是 169 预填已含出块者 拆句（187 item 1/2/3） |
| 2026-09-19 | P1-3 1449–1451 EIP-2929 cold-vs-warm 不是已经热 / 再碰不是又是冷访问 / 开跑预填不是任意地址已热 拆句（169 item 1/2/3） |
| 2026-09-19 | P1-3 1452–1454 EIP-2930 listed 不是已经访问过 / 列表外不是已经不能碰 / 预付列表费不是已经跑完读取 拆句（168 item 1/2/3） |
| 2026-09-19 | P1-3 1455–1457 EIP-2718 typed-envelope 不是已经解开内层 / 旧式 RLP 不是已经是信封 / 看见收据不是类型已对上 拆句（167 item 1/2/3） |
| 2026-09-19 | P1-3 1458–1460 EIP-7935 default-gas 不是已经是协议帽 / 绑到硬分叉不是已经改了共识 / 默认齐了不是已经是单笔帽 拆句（211 item 1/2/3） |
| 2026-09-19 | P1-3 1461–1463 EIP-7825 tx-gas-cap 不是已经改了块气 / 入池拒掉不是已经验过块 / 块里超帽不是已经只是策略 拆句（203 item 1/2/3） |
| 2026-09-19 | P1-3 1464–1466 EIP-7934 rlp-cap 不是已经改了气 / 流言不传不是已经执行层非法 / 留边不是已经一份编码 拆句（202 item 1/2/3） |
| 2026-09-19 | P1-3 1467–1469 EIP-7623 calldata-floor 不是已经改了执行气 / 数据为主更贵不是已经普通转账更贵 / 预留不是已经烧到 拆句（197 item 1/2/3） |
| 2026-09-19 | P1-3 1470–1472 EIP-7939 clz 不是已经更便宜ZK / 动机写了后量子不是已经有后量子签 / 能表达最低位不是已经有数尾零 拆句（208 item 1/2/3） |
| 2026-09-19 | P1-3 1473–1475 EIP-7823 modexp-bound 不是已经改了计价 / 超帽不是已经成功返回 / 有界不是已经换成EVM 拆句（206 item 1/2/3） |
| 2026-09-19 | P1-3 1476–1478 EIP-7928 block-list 不是已经并行跑完 / 强制名单不是已经是2930 / 事后差不是已经不跑 拆句（212 item 1/2/3） |
| 2026-09-19 | P1-3 1479–1481 EIP-7044 exit-domain 不是已经永远有效 / 域锁不是已经改了执行层 / 两边重放不是已经丢资金 拆句（213 item 1/2/3） |
| 2026-09-19 | P1-3 1482–1484 EIP-7917 lookahead 不是已经锁死日程 / 余额还能变不是已经排完 / 前瞻名单不是已经预确认 拆句（205 item 1/2/3） |
| 2026-09-19 | P1-3 1485–1487 EIP-1559 basefee-vs-tip 烧掉不是已经给出块者 / 弹性不是市场已齐 / 烧掉不是MEV已解决 拆句（158 item 1/2/3） |

下一批默认：**P1-3 官方三事 1488+**（继续仍捆着的官方对象：history-window，或 P3-3 / P1-5）。  
唤醒后先跑 `python3 tools/review_audit.py`，见 [`REVIEW_LOOP.md`](REVIEW_LOOP.md)。

---

## 禁止事项（GOAL 重申）

- 不在 `qtb/` 写协议教材
- 决策矩阵禁止填「愿望」；必须标 事实 / 推断 / 建议
- 不出题进正文；exams 后置
- 不把 benchmark TPS 当事实
