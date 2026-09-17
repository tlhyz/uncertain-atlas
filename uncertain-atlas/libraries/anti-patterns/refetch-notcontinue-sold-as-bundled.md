# 反模式：把 reject_senders not already can continue / not already halted / not already complete 正式三事（378 余量） 卖成 已经能接着装 / 已经停 / 已经齐

**层次**：实现 / ApplySnapshotChunk 再拉。  
**分类**：建议（产品）。  
**对应例**：[worked-example-refetch-notcontinue-vs-bundled.md](../../tracks/implementation/worked-example-refetch-notcontinue-vs-bundled.md)。

官方把应用可以再拉块或封邻居、引擎不自己做 / refetch_chunks 不论 result / reject_senders 不论 Result 三条核心句写成三件独立的实现事。把它们卖成已经能接着装 / 已经停 / 已经齐，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 reject_senders 正式三事（378 余量），必须分开 not already can continue、not already halted、not already complete 三件事，不要和 378 / 375 / 400 / 723 / 397 / 741 / 794 / 795 糊成一句。

## 和相邻反模式

- [refetch-notcomplete-sold-as-bundled](refetch-notcomplete-sold-as-bundled.md) 是 refetch_chunks 单句边界（795 item 2），不是本页 reject_senders 边界。
- [applychunk-notsenders-sold-as-bundled](applychunk-notsenders-sold-as-bundled.md) 是 Apply 请求 sender 就已经拒了人（397/741），不是本页 reject_senders 边界。
