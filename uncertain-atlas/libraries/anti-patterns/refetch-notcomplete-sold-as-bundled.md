# 反模式：把 refetch_chunks not already complete / not already settled / not already same snapshot 正式三事（378 余量） 卖成 已经齐 / 已经交差 / 已经是同一份

**层次**：实现 / ApplySnapshotChunk 再拉。  
**分类**：建议（产品）。  
**对应例**：[worked-example-refetch-notcomplete-vs-bundled.md](../../tracks/implementation/worked-example-refetch-notcomplete-vs-bundled.md)。

官方把应用可以再拉块或封邻居、引擎不自己做 / refetch_chunks 不论 result / reject_senders 不论 Result 三条核心句写成三件独立的实现事。把它们卖成已经齐 / 已经交差 / 已经是同一份，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 refetch_chunks 正式三事（378 余量），必须分开 not already complete、not already settled、not already same snapshot 三件事，不要和 378 / 332 / 398 / 719 / 375 / 794 / 796 糊成一句。

## 和相邻反模式

- [refetch-notbanned-sold-as-bundled](refetch-notbanned-sold-as-bundled.md) 是引擎不自己做单句边界（794 item 1），不是本页 refetch_chunks 边界。
- [applyretry-notrefetch-sold-as-bundled](applyretry-notrefetch-sold-as-bundled.md) 是 RETRY 就已经 refetch 不论 result（398/719），不是本页 refetch_chunks 边界。
