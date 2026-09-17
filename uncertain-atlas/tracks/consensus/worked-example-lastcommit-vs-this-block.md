# 工作实例：本头 LastCommit 不是本高度已经 +2/3

> **事实 / 推断 / 建议** 已分开。
> 对照：[L4.2](../../courses/level-04-bft/L04-M02-rounds-and-steps.md)、[CometBFT 档案](../../protocols/cometbft/README.md)、[本头 AppHash](worked-example-apphash-vs-this-block.md)、[+2/3 ≠ 其余已签](../failure-museum/cve-2020-15091.md)、[本地超时](worked-example-timeouts.md)。
> 主文献：CometBFT 官方 [Byzantine Consensus Algorithm](https://github.com/cometbft/cometbft/blob/main/spec/consensus/consensus.md)、[data structures](https://github.com/cometbft/cometbft/blob/main/spec/core/data_structures.md)。BFT Time 页只钉「H 的 Commit 进 H+1 的块」。资料层级是共识规范。不另写 19 节。
> 本页钉 **本头 LastCommit ≠ 本高度已经 +2/3**、**本地 subjective commit ≠ 链上 canonical LastCommit**、**第一块空 LastCommit ≠ 已经没有最终**。不抄票槽上限、超时秒数、哈希宽度。不写怎样拼 LastCommit 或扣 precommit。

---

## 0. 先修

- [L4.2](../../courses/level-04-bft/L04-M02-rounds-and-steps.md) 高度、轮、步
- [不变量 65](../../libraries/invariants/README.md) +2/3 不是其余槽位已签
- [不变量 147](../../libraries/invariants/README.md) 本头 AppHash 不是本块已交差
- [不变量 148](../../libraries/invariants/README.md)

---

## 1. 核心问题

阿比看见高度 H 的块里有一份 `LastCommit`，或看见本节点刚凑齐 +2/3 precommit，以为**这一份**就是本高度已经盖章；或把钱包里「我看见过 +2/3」写成链上那份唯一的 Commit。

官方句（事实）：

- 共识规范 *Canonical vs subjective commit*：subjective commit 是每个验证者**本地**决定 commit 一块时看见的那份票。canonical commit 是**下一块提议者**写进该块 `LastCommit` 字段的那份。正是写进下一块，才让全网对「哪一份算数」对齐——即使它和某验证者当初据以 commit 的那份 +2/3 **不一样**。每一块带的是上一块的 canonical +2/3 commit。
- 数据结构：`LastCommit` 每个验证者一票；票必须是上一块、nil 或缺席。投上一块的必须有对应签名。投了的投票权之和必须大于全集的 2/3。**初始高度必须空**。
- `LastCommitHash` 是 lastCommit 签名的 Merkle 根；这些签名代表验证者对**上一块**的 commit。第一块该哈希为空。
- BFT Time 页（只钉这一句）：高度 H 的一份 `Commit` 被写进高度 H+1 提议的块。
- NewHeight：把本高度的 `Precommits` 挪进 `LastCommit`，再加高度。
- 规范**没有**把本头 `LastCommit` 写成本高度已经 +2/3，也没有把本地看见的 +2/3 写成已经是链上那一份，也没有把第一块空 `LastCommit` 写成「这条链还没有最终」。

本头里的上一块票、本地据以落笔的那份票、本高度自己要等下一块才印上去的票，是三件东西。

---

## 2. 直觉（ELI15）

今天会议纪要后面订着的，是**昨天**决议的签字页。  
你自己口袋里那张「我看见过三分之二举手」的小便签，不必和纪要后面订着的那一页逐名相同。  
今天这份决议的签字页，要等**明天**的纪要才订上去。

看见今天纪要后面有签字页，不是今天这份已经在这一页上盖完章。

---

## 3. 对象

| 名字 | 是什么 | 不是什么 |
|---|---|---|
| 本头 / 本块 `LastCommit` | 上一块的 canonical +2/3 | 本高度已经 +2/3；本块自己的 precommit 已经印在本块 |
| subjective commit | 某验证者本地据以进入 Commit 步的那份 +2/3 | 已经是全网对齐的那一份；已经写进链 |
| canonical LastCommit | 下一块提议者写进 `LastCommit` 的那份 | 必须等于每个人口袋里的那份 |
| 第一块 `LastCommit` | 必须空 | 已经没有最终；创世还没 commit |
| `LastCommitHash` | 上一块 commit 签名的根 | 本块投票已经进本头 |

---

## 4. 最小案例

一条 CometBFT 链要对齐「高度 H 已经最终」。

1. 验证者在高度 H 看见 +2/3 precommit，进入 Commit 步。规范：这是 subjective commit。不是已经写进高度 H 的块。
2. 高度 H 的块里有一份 `LastCommit`。规范：那是高度 H−1 的 canonical +2/3。不是高度 H 已经 +2/3。
3. NewHeight：把高度 H 的 Precommits 挪进 `LastCommit`，高度变成 H+1。规范：高度 H 的 canonical commit 要等高度 H+1 的块才带上。
4. 下一块提议者写进的那份，可以和某验证者口袋里的那份不完全相同。规范：写进下一块才叫 canonical，全网对齐的是这一份。
5. 有人把这听成「已经 +2/3 所以其余槽位也签过」（不变量 65），或听成「本头 AppHash 是本块已交差」（不变量 147）。那些是验完整个 Commit、以及应用根滞后。本页是**哪一份票、印在哪一块上**。
6. 有人把 `timeout_commit` 还在等听成还没最终（不变量 47）。那是本地再收迟到票。本页是字段语义。

「块里有 LastCommit 所以本高度已经盖章」是假学习。

---

## 5. 五层

| 层 | 本页 |
|---|---|
| 密码学 | LastCommit 里上一块的签必须能验；nil / 缺席是显式槽位 |
| 协议 | 必须点名问的是本头上一块票、本地那份，还是下一块才印的 canonical |
| 实现 | NewHeight 才把 Precommits 挪进 LastCommit；字段名 `Last` 不是笔误 |
| 部署 | 浏览器若把本块 LastCommit 画成本块已最终，运维会把滞后听成分叉 |
| 经济 | 按「谁签了」发奖必须写清看的是哪一份、验没验完（65） |

**推断：** 产品句若只写「块上有 Commit」，读者会把昨天的签字页听成今天已经盖章。  
**建议：** 若抄 CometBFT 头，必须写清本块 `LastCommit` 是上一高度。不要把本地 +2/3 写成已经是链上那一份。不要抄 `timeout_commit` 秒数。

---

## 6. 和另外几句不是同一句

1. **+2/3 ≠ 其余已签**（不变量 65）：一份 Commit 内部每个槽位都要验。本页是这份 Commit 印在哪一块上。
2. **本头 AppHash ≠ 本块已交差**（不变量 147）：应用根滞后一块。本页是票滞后一块。
3. **timeout_commit ≠ 最终性**（不变量 47）：commit 之后再等迟到票。本页不是本地等待。
4. **锁**（不变量 4）：同一高度不得对两值违锁承诺。本页不是解锁。
5. **BFT Time**（不变量 40）：用 LastCommit 时间戳算本块 Time。本页不是钟。
6. **飞行中 last commit ≠ 证据身份**（不变量 64）：证据字段从哪取。本页不是证据。

不要抄票槽上限、超时秒数、哈希宽度。不要写怎样拼 LastCommit 或扣票。不编博物馆页。不另写 19 节。JSet / full commit 备选算法标成另一对象。

---

## 7. 「不确定」测试句（建议）

```text
本头 LastCommit ≠ 本高度已经 +2/3
本地 subjective commit ≠ 链上 canonical LastCommit
第一块 LastCommit 必须空 ≠ 已经没有最终
高度 H 的 Commit 进 H+1 的块
LastCommitHash 是上一块的签 ≠ 本块投票已经进本头
```

语料：[C152](../../libraries/adversarial-corpus/README.md)。

---

## 精密检查

**禁止假学习：** 「块里有 LastCommit = 本高度已经盖章。」「我看见过 +2/3 = 已经是链上那一份。」「第一块 LastCommit 空 = 这条链还没有最终。」  
**边界：** 不讲某一版 `CommitSig` 位图。不抄票槽上限。不另写 19 节。不写怎样拼 LastCommit。槽位验完、AppHash、timeout_commit、BFT Time 另标。
