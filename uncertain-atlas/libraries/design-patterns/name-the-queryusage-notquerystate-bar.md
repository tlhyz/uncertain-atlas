# 模式：把 Query Usage Query for data at current or past height not QueryState / not replicated / not QueryState is ExecuteTxState 正式三事（487 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Usage。  
**例**：[Query for data at current or past height not QueryState ≠ bundled（487）](../../tracks/implementation/worked-example-queryusage-notquerystate-vs-bundled.md)。

## 三个名字

1. **Query for data at current or past height 不是 QueryState：** 看见 Methods Usage 侧查当前或过去高度，不是已经是 Query Request height 栏 bundled 或 QueryState 那份只读副本 interchangeable，不是 371 queryheight interchangeable / 677 queryusage-notquerystate interchangeable。

2. **查应用在当前或过去高度 不是已经复制到各节点：** 看见 Query for data at current or past height，不是已经 Query 回了就已经复制到各节点 interchangeable，不是 329 query-vs-replicated interchangeable。

3. **看见能查 不是 QueryState 就是 ExecuteTxState：** 看见 Usage 查哪一高度，不是已经 QueryState 就是 ExecuteTxState interchangeable，不是 314 querystate interchangeable / 668 infousage-notquerystate interchangeable。

官方把 Query Usage 查哪一高度、Query Request height / QueryState 只读副本、Query 回了就已经复制 写成三个名字。把它们叫成一个「看见能查 就已经 QueryState interchangeable / 就已经 replicated interchangeable / 就已经 QueryState is ExecuteTxState interchangeable」，会把 not QueryState、not replicated、not QueryState is ExecuteTxState 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query Usage Query for data at current or past height not QueryState / not replicated / not QueryState is ExecuteTxState 正式三事（487 余量），先数清问的是 Query for data at current or past height 是不是 QueryState / 371、是不是已经复制到各节点 / 329，还是看见能查 是不是 QueryState 就是 ExecuteTxState / 314，再决定要不要同一次发布。487 queryusage vs querystate bundled unbundling 在本页 item 1 启动。
