# 反模式：把 可以用 decided_last_commit 和 misbehavior 定奖惩 not already slashed / not already LastCommit +2/3 / not already settled 正式三事（363 余量） 卖成 已经罚没 / 已经是本头 LastCommit 就已经是本高 +2/3 / 已经交差

**层次**：实现 / Finalize 回包义务。  
**分类**：建议（产品）。  
**对应例**：[worked-example-finalize-equiv-notslashed-vs-bundled.md](../../tracks/implementation/worked-example-finalize-equiv-notslashed-vs-bundled.md)。

官方把 Finalize 等价于 ABCI 1.0 那三步 / 可以用 decided_last_commit 和 misbehavior 定奖惩 / 必须回四列三条核心句写成三件独立的实现事。把它们卖成已经罚没 / 已经是本头 LastCommit 就已经是本高 +2/3 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看可以用 decided_last_commit 和 misbehavior 定奖惩 正式三事（363 余量），必须分开 not already slashed、not already LastCommit +2/3、not already settled 三件事，不要和 363 / 21 / 365 / 830 / 372 / 836 / 838 糊成一句。

## 和相邻反模式

- [finalize-equiv-notgates-sold-as-bundled](finalize-equiv-notgates-sold-as-bundled.md) 是收成一门单句边界（836 item 1），不是本页定奖惩边界。
- [voteinfo-notslashed-sold-as-bundled](voteinfo-notslashed-sold-as-bundled.md) 是 VoteInfo 定奖惩（365/830），不是本页 decided_last_commit 边界。
