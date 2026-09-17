# 反模式：把 Query Usage Query for data at current or past height not QueryState / not replicated / not QueryState is ExecuteTxState 正式三事（487 余量）说成已经 QueryState / 已经 replicated / 已经 QueryState is ExecuteTxState

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Query for data at current or past height not QueryState ≠ bundled（487）](../../tracks/implementation/worked-example-queryusage-notquerystate-vs-bundled.md)。

## 卖法

把 Query for data from the application at current or past height / 查应用在当前或过去高度的数据 写成已经是 QueryState interchangeable / 371 queryheight interchangeable / 371 queryheight item 2 height 默认 0 interchangeable / 已经 Query Request `height` 默认 0 回最新已提交 interchangeable / 已经是 QueryState 那份只读副本 interchangeable；把查应用在当前或过去高度写成已经复制到各节点 interchangeable / 329 query-vs-replicated interchangeable / 已经查到了就已经新鲜 interchangeable；把看见能查写成已经 QueryState 就是 ExecuteTxState interchangeable / 314 querystate interchangeable / 668 infousage-notquerystate interchangeable，或已经和 487 queryusage-vs-querystate bundled / queryusage-notquerystate-sold-as-bundled interchangeable / 677 queryusage-notquerystate interchangeable。

## 为什么错

官方把 Query Usage 查哪一高度、Query Request height / QueryState 只读副本、Query 回了就已经复制、QueryState 就是 ExecuteTxState 写成三件独立的实现事。把它们卖成 QueryState interchangeable / replicated interchangeable / QueryState is ExecuteTxState interchangeable，会把 not QueryState、not replicated、not QueryState is ExecuteTxState 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query Usage Query for data at current or past height not QueryState / not replicated / not QueryState is ExecuteTxState 正式三事（487 余量），必须分开 not QueryState、not replicated、not QueryState is ExecuteTxState 三件事，不要和 487 / 371 / 329 / 314 / 668 / 678 / 679 糊成一句。

## 和相邻反模式

- [queryusage-sold-as-querystate](queryusage-sold-as-querystate.md) 是 Query Usage 正式三事 bundled（487），不是本页 item 1 单句边界。
- [queryusage-notproof-sold-as-bundled](queryusage-notproof-sold-as-bundled.md) 是 Optionally return Merkle proof 单句边界（678 item 2），不是本页查哪一高度边界。
- [queryheight-sold-as-committed](queryheight-sold-as-committed.md) 是 Query Request height 栏，不是本页 Usage 查当前或过去高度。
