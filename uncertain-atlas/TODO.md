# TODO · 大目标与无数小目标

本文件是 [`GOAL.md`](GOAL.md) 的**执行层**：GOAL.md 说「为什么」与「不许怎样」，
本文件说「接着做什么、怎么算做完」。

写法来源：[Mission Breakdown Structure](https://daneshyari.com/article/preview/276401.pdf)
（使命 → 子使命 → 可交付）与 PMI 的
[项目目标层级](https://www.wcu.edu/pmi/1993/93PMI078.PDF)，
落到本库既有的「轨 / 波」习惯上。

---

## 一、三层结构

```text
L1  使命        1 个     GOAL.md 全文。改它要走 L10.1 记录，不在这里改。
L2  轨          7 条     下面第二节。每条有「做完长什么样」。
L3  波          无数    每波 = 一个对象 + 七件固定交付物。见第三节。
```

**为什么这样分：** L1 不动，L2 少动，L3 高频动。波与波之间没有依赖，
所以可以停在任何一波、也可以并行。**不许出现「等某个大重构做完才能继续」的波。**

---

## 二、七条轨（L2）

| 轨 | 做完长什么样（可判定的） | 当前状态 |
|---|---|---|
| **A 不变量前沿** | 每波按契约推进，`check-atlas.ps1` 全绿 | 452 条；本会话从 438 推到 452 |
| **B 规范覆盖** | 覆盖率台账（第六节）里每个对象都标「已挖 / 不适用 / 待挖」，无空白 | **最大缺口**，见下 |
| **C 遗留债** | `AUDIT_LOG` 里所有「留给下一波」都清账 | 1 笔未清（A2135 的 `L10-M03` 目录；实测比记录更严重，见第五节） |
| **D 过程工具** | 闸门能拦住上一轮犯的错 | `check-atlas.ps1` 8 项 + `push-atlas.ps1` 已建 |
| **E 决策库** | 决策矩阵末列不再是空的 | 对照列已扩，**候选列仍空** |
| **F 对抗语料 runner** | C01–C460 能被执行，不再只是目录 | **未建** |
| **G 题库** | GOAL.md 门禁：现在**不出题** | 只有 L0 题，按门禁后置 |

**G 轨现在不许动** —— GOAL.md 第 34 行写明「现在不出题，试题后置」。

---

## 三、波（L3）：七件固定交付物

每波必须凑齐这七件，缺一件算没做完：

1. **一个待挖对象**（规范里的字段 / 枚举 / 方法 / 小节）
2. **一条不变量**（`libraries/invariants/README.md` 追加「第 N 条」）
3. **一条语料**（`libraries/adversarial-corpus/README.md` 追加 `C(N+8)`）
4. **一个模式**（`libraries/design-patterns/name-the-*.md`）
5. **一个反模式**（`libraries/anti-patterns/*-sold-as-*.md`）
6. **一个工作实例**（`tracks/implementation/worked-example-*.md`）
7. **六处回填**：L4.4 / CometBFT 档案 / 实现表 / 停链面地图 / 共识专题 / L10.3 目录
   加 CHANGELOG 与 AUDIT_LOG

### 波的入场条件（先做，撞车即弃）

写之前必须在全库搜一遍待挖对象的关键词。**撞车就换对象，不硬写。**
本会话靠这条拦下 9 次：`retain_height`(366)、`Validator`(364)、`ProofOp.key`(390)、
`CommitInfo.round`(392)、`ExtendedCommitInfo.round`(394)、`votes` 降序(365)、
`Echo`(399)、`Flush`(374)、`FeatureParams`(343 两次)。

### 波的出场条件（客观，不靠感觉）

```powershell
& .\uncertain-atlas\tools\check-atlas.ps1     # 必须 exit 0
& .\uncertain-atlas\tools\push-atlas.ps1      # 必须验证 origin/main == 本地 HEAD
```

**exit code 是唯一的完成信号。** 不写「我觉得做完了」。

---

## 四、B 轨优先：覆盖率台账（最大缺口）

已实测的规范原文规模：**6,467 行**（CometBFT `main` 分支 16 个规范文件）。
已引用次数（全库 grep）：

| 规范文件 | 行数 | 全库引用 | 判断 |
|---|---|---|---|
| `abci/abci++_methods.md` | 954 | **557** | 挖得最深，仍有空白 |
| `abci/abci++_app_requirements.md` | 1113 | **253** | 深 |
| `core/data_structures.md` | 587 | 90 | 中 |
| `core/encoding.md` | 332 | **1** | **基本没挖** |
| `rpc/README.md` | 1264 | 未测 | **没碰** |
| `abci/abci++_basic_concepts.md` | 471 | 未测 | 未知 |
| `consensus/consensus.md` | 350 | 未测 | 未知 |
| `light-client/verification/README.md` | 577 | 未测 | 未知 |
| `light-client/README.md` | 205 | 未测 | 未知 |
| `consensus/evidence.md` | 210 | 未测 | 未知 |
| `core/state.md` | 132 | 未测 | 未知 |
| `consensus/proposer-based-timestamp/README.md` | 132 | 未测 | 未知 |
| `consensus/creating-proposal.md` | 61 | 未测 | 未知 |
| `core/genesis.md` | 38 | 未测 | 未知 |
| `p2p/README.md` | 41 | 未测 | 未知 |

**小节数（已探）：** data_structures 38 · abci 方法 30 · abci 类型 30 · rpc 28 ·
consensus 19 · basic_concepts 18 · encoding 15 · lc/verification 11 · evidence 9 ·
pbts 6 · state 5 · light-client 3。

**按本会话实测速率**（8 波挖 14 条不变量，约 1.75 条/波；单文件内可挖对象数 ≠ 小节数），
B 轨的可见前沿是**几十到上百波**量级 —— 但**不要把它当成已完成的计算**：
每个对象要先过去重预检，实际数字只有挖的时候才知道。

### 下一批已核实的真空候选

| 对象 | 出处 | 已验证 |
|---|---|---|
| `Signature`（`secp256k1eth` 必须恰好 65 字节 `[R \|\| S \|\| V]`） | core/data_structures.md:372 | 未测 |
| `CommitSig` / `ExtendedCommitSig` 表其余栏 | core/data_structures.md:223 | `CommitSig` 全库 1 命中 |
| `Proposal` | core/data_structures.md:338 | 未测 |
| `Commit` / `ExtendedCommit` | core/data_structures.md:198 | 未测 |
| `core/encoding.md` 全篇 | 332 行 | **全库仅 1 引用** |
| `rpc/README.md` 全篇 | 1264 行 | **没碰** |

---

## 五、C 轨：当前未清的债（先清这笔再开新轨）

### C1 `L10-M03` 目录的编号缺陷（AUDIT_LOG A2135，**实测比原记录严重**）

`courses/level-10-uncertain-studio/L10-M03-v1-settlement-machine.md` 是
「若对照本对象，必须点名问的是…」的审阅清单。实测（本文件写入时）：

| 事实 | 值 |
|---|---|
| 总条目数 | 448 |
| 条目号范围 | 1–450 |
| **偏移** | 条目 425–434 覆盖不变量 429–438（**+4**）；条目 437–450 覆盖不变量 439–452（**+2**） |
| **缺失** | **不变量 437（ExtendVote Usage）与 438（ExtendVote When）没有对应条目** |
| **排列** | 尾部 425–434 是**降序**，与全文其余部分的升序不一致 |

**为什么这是真缺陷（不是格式洁癖）：** 437 / 438 两条不变量在
`libraries/invariants/README.md` 里存在，但**从未有过可执行的对照条目** ——
按 GOAL.md「全面」门禁，学完/写完必须能互相指认，这两条现在是断的。

**修法（一次做完，约 30 条移位）：**

1. 为不变量 437 / 438 各写一条对照条目（文案可仿条目 433 / 434 的现行写法，
   它们分别就是 437 / 438 的同一对象）。
2. 把现有条目 **437–450 全部 +2**（437→439 … 450→452），恢复全文统一的
   「条目号 = 不变量号 − 2」。
3. 把尾部整段扶成**升序**。
4. 修完把 `tools/check-atlas.ps1` 里的 `$l10KnownGap` **改回 0**，
   并把该检查从「只比最大值」改成**逐号列缺**（现在只比最大值，会掩盖缺哪两个）。

**风险提示：** 这是几十条的长行移位。本会话曾用脚本改这个文件把换行吃掉过一次
（见 AUDIT_LOG 复审节）。**做的时候必须逐条用 `edit` 或带 CRLF 校验的脚本，
做完跑 `check-atlas.ps1` 确认 [8] 行尾仍为 CRLF。**

### C2 同型相对链接：已确认无残留

本会话修过 `tracks/state-models/worked-example-delegation-vs-code.md` 里
`level-02-accounts` / `level-05-execution` 这类不存在的目录名。
**已全库复查**：非法 `courses/` 目录引用 **0** 条。此项**无需再做**。

---

## 六、怎么用这份文件

- **每次开工先看第二节**：哪条轨最落后。B 轨长期最落后，所以默认从 B 轨取对象。
- **取一个对象走第三节的七件**：入场先搜重，出场跑两个脚本。
- **做完一波更新第六节**：把该对象的行改成「已挖（不变量 N）」，并在本文件
  第二节的状态列改数字。**台账不更新 = 这一波不算完。**
- **撞车三次就换轨**：同一份规范连续三次搜重失败，说明那份挖完了，去别的文件。

---

## 七、边界（与 GOAL.md 一致，别越界）

- 不往库里加回测、下单、策略代码（GOAL.md 第 39 行）。
- 不混用「协议保证 / 实现保证 / 部署保证 / 经济假设 / 密码假设」（第 68 行）。
- 事实 / 推断 / 建议必须分开（第 70 行）。
- 发现规范自己的错（笔误、矛盾、悬空引用、TODO）**按原文记录，不代改、
  不自己补折中定义**。本会话已这样处理 `VersionsParams` / `#featureparms` /
  `Part` 表错位 / `Header` 表 `ValidatorHash` / `ValidatorIndex` 的
  「Must be > 0」这几处。
