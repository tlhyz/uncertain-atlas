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
2. CometBFT ABCI++ 不变量拆完（目标 ~793 句；当前 ~745）。
3. 决策矩阵「不确定候选」列填完**建议档**（非最终选型）。
4. 对抗语料 C01–C723+ 有 runner，能批量扫描文案/测试钩子。
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
| 不变量库 | 745+ 可测试句；ABCI++ 主线 | 进行中（强） |
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
| P1-3 | ABCI++ 拆完 677–793 | AUDIT_LOG 连续；invariants README 更新 |
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

下一批默认：**P1-3 ABCI++ 不变量 746+**（继续 cometbft 拆句）。  
唤醒后先跑 `python3 tools/review_audit.py`，见 [`REVIEW_LOOP.md`](REVIEW_LOOP.md)。

---

## 禁止事项（GOAL 重申）

- 不在 `qtb/` 写协议教材
- 决策矩阵禁止填「愿望」；必须标 事实 / 推断 / 建议
- 不出题进正文；exams 后置
- 不把 benchmark TPS 当事实
