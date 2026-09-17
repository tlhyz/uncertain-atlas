# 反模式：把 引擎不自己做 not already banned / not already complete / not already settled 正式三事（378 余量） 卖成 已经封了 / 已经齐 / 已经交差

**层次**：实现 / ApplySnapshotChunk 再拉。  
**分类**：建议（产品）。  
**对应例**：[worked-example-refetch-notbanned-vs-bundled.md](../../tracks/implementation/worked-example-refetch-notbanned-vs-bundled.md)。

官方把应用可以再拉块或封邻居、引擎不自己做 / refetch_chunks 不论 result / reject_senders 不论 Result 三条核心句写成三件独立的实现事。把它们卖成已经封了 / 已经齐 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看引擎不自己做 正式三事（378 余量），必须分开 not already banned、not already complete、not already settled 三件事，不要和 378 / 321 / 502 / 656 / 398 / 719 / 795 / 796 糊成一句。

## 和相邻反模式

- [applysnapusage-notchoose-sold-as-bundled](applysnapusage-notchoose-sold-as-bundled.md) 是 Usage can choose 就已经是 refetch_chunks（502/656），不是本页引擎不自己做边界。
- [applyretry-notrefetch-sold-as-bundled](applyretry-notrefetch-sold-as-bundled.md) 是 RETRY 就已经 refetch 不论 result（398/719），不是本页引擎不自己做边界。
