# Snapshot 分支库存（P3-3）

**层次**：治理 / canonical。  
**分类**：事实（计数）+ 推断（后继关系）+ 建议（回收顺序）。  
**不要写进**：`qtb/`、考试、把 285 条 remote 当已经合并。

本页是量过的库存，不是已经把 74 条平行线快进进 HEAD，也不是已经可以删 remote。

量法：`python3 tools/snapshot_branch_inventory.py`。对照分支是 `origin/cursor/cometbft-*`。首次测量 HEAD 是 `f8a91c71`（Homestead 1346–1349 之后）。本回合已把 unique 9 簇文件收回 canonical，并把 `extappgen` 拆成不变量 1350–1352。其余 8 簇仍是未拆的官方三事父页。

---

## 事实（2026-09-18 量过）

| 项 | 数 | 说明 |
|---|---:|---|
| remote `origin/cursor/cometbft-*` | 285 | 只计 remote；工作树里的同名本地枝另算 |
| 已是 HEAD 祖先 | 211 | `git merge-base --is-ancestor $ref HEAD` 为真；知识已在 canonical |
| 平行（非祖先） | 74 | 与 HEAD 分叉；最肥 tip 是 `finfields-nothandshake-575` |
| 最肥平行 tip 的 atlas 文件 | 1797 | `origin/cursor/cometbft-finfields-nothandshake-575-2f0b` |
| tip 有、工作树没有（回收前） | 107 | 37 implementation + 35 anti-patterns + 35 design-patterns |
| 本回合收回 unique | 27 文件 / 9 簇 | 实现页 + 配套模式/反模式；`extappgen` 已拆 1350–1352 |
| 回收后仍缺（全是 superseded） | 80 | 见「不要抄」；不要再 checkout |

前五肥平行 tip（atlas 文件数）：

| 文件数 | ref |
|---:|---|
| 1797 | `origin/cursor/cometbft-finfields-nothandshake-575-2f0b` |
| 1794 | `origin/cursor/cometbft-finfields-notdeterministic-574-2f0b` |
| 1791 | `origin/cursor/cometbft-finfields-notsettled-573-2f0b` |
| 1788 | `origin/cursor/cometbft-finproc-notcand-572-2f0b` |
| 1785 | `origin/cursor/cometbft-finproc-notproposer-571-2f0b` |

`origin/cursor/cometbft-echousage-notdone-676-2f0b` **是** HEAD 祖先。不要再把它当平行线。

---

## 推断：unique 簇（无 HEAD 后继）

这 9 份实现页在最肥 tip 上，HEAD 没有同 stem、也没有后继前缀。快照正文把它们标成不变量 439–446 一带，但 canonical `libraries/invariants/README.md` 编号头从 437 跳到 460。建议（产品）：回收时发给 **新号 1350+**，不要在 README 中段回填 439–446。

| 快照页 | 快照自称 | 对象边界（事实） | 不要糊成 |
|---|---|---|---|
| `worked-example-extappgen-vs-signed.md` | 439 | ExtendVoteResponse 是应用生成、**将**被签名 | 已经签过 / 已经包进 CanonicalVoteExtension（418）/ 已经广播（438） |
| `worked-example-extcinotes-vs-order.md` | ExtendedCommitInfo Notes | ExtendedVoteInfo 按投票权降序、引擎保证、从 store 再装 | CommitInfo Notes（444）/ 从块里抽出（365） |
| `worked-example-cinotes-vs-order.md` | 444 | CommitInfo.votes 按投票权降序、引擎保证、从 store 再装 | ExtendedCommitInfo Notes / 从块里抽出 |
| `worked-example-cifields-vs-notes.md` | 445 | CommitInfo Fields 的 round / votes 栏 | Notes 票序（444）/ InitChain app_hash（392） |
| `worked-example-exectxevents-vs-header.md` | 446 | ExecTxResult.events 逐笔、非确定、索引 | LastResultsHash（316）/ 块级 events（431）/ CheckTx events（381） |
| `worked-example-extviusage-vs-expose.md` | ExtendedVoteInfo Usage 暴露签 | 引擎已验签、暴露给应用再处理、没 non_rp 就签空切片 | 表栏 421 / 抽出路径 369 / extvicol 收集栏 |
| `worked-example-prepevents-vs-finalize.md` | Prepare 事件保留 | MAY 产出、MUST 留到决定、经 Finalize 交回 | Prepare 回包只有 txs（357）/ Finalize events 栏（431） |
| `worked-example-validatorusage-vs-gates.md` | Validator Usage 四门 | Process CommitInfo ≠ Finalize decided ≠ Prepare Extended | Validator address（364）/ VoteInfo 抽出（442） |
| `worked-example-viusageavail-vs-extractpath.md` | availability 同句、抽取异路 | 两份 Usage 同一句 availability、两条抽出路径 | 365 奖罚完 / 369 从本进程抽出就已经从块里抽出 |

每份实现页在 tip 上还有配套 `libraries/design-patterns/name-the-*` 与 `libraries/anti-patterns/*-sold-as-*`。回收时三件一起搬，不要只抄精读页。

---

## 推断：superseded（不要抄）

| 快照前缀 | HEAD 后继 | 为什么不要 `git checkout` |
|---|---|---|
| `finfields-not*` | `ffields-not*`（1109–1111） | 后继前缀已拆完 |
| `htmatch-not*` | `htmt-not*`（1097–1099） | 后继前缀已拆完 |
| `finlock-vs-commit` | `finlock-vs-commitlock` + `finlock-not*` | 文件名已改 |
| `procaccept-vs-req3` | `procaccept-shouldaccept` / `default` | 后继页已在 |
| `verifyaccept-vs-req6` | `verifyaccept-shouldaccept` / `default` | 后继页已在 |
| `finempty` / `finexec` / `finfill` / `finht` / `finnewfields` / `finproc` / `finreward` / `fincand` / `finvaldelay` | 各 `not*` / `fndelay-not*` | 已在 HEAD |
| `misbheighttime` / `misbtvp` / `misbtype` / `misbvalidator` | `misbehavior-not*` / `finmisbeh-notvoteinfo` | 过错枚举后继已在 |
| `proccand` / `procfull` / `procht` | 各 `not*` | 已在 HEAD |

`git diff HEAD...branch --diff-filter=A` 会把平行史上「曾经新增」算进来。权威对照是 `git ls-tree` ∪ `Path.exists()`。

---

## 建议（产品，不是选定）

1. **先回收 unique 9 簇**，发给 1350+，按官方三事拆 `not*` 儿页。本回合默认先拆 `extappgen`（和 418 / 358 / 438 边界最干净）。
2. **不要合并 74 条平行线。** 冲突面会吞掉后面的拆句。
3. **不要删 285 条 remote。** 库存页在，分支当只读备份。
4. P3-3「不再 285 个 snapshot 分支」仍未完成。本页只把数量和 unique/superseded 写成可核对句。

---

## 本页不抄

- 怎样 `git merge` 74 条平行线。
- 怎样删 remote。
- 把 439–446 空号当成已经有编号头。
- 把 107 份缺失文件整包 checkout。
