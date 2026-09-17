# 模式：点名 引擎按当前高度决定存什么要什么 not already genesis configured / not already app decides / not already settled 正式三事（346 余量）

**层次**：实现 / ABCI 2.0 协调升级。  
**分类**：建议（产品）。  
**对应例**：[worked-example-abci20-upgrade-notgenesis-vs-bundled.md](../../tracks/implementation/worked-example-abci20-upgrade-notgenesis-vs-bundled.md)。

引擎按当前高度决定存什么要什么 not already genesis configured / not already app decides / not already settled 正式三事（346 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **按当前高度存/要 不是已经按创世配好了：** 看见引擎按当前高度决定存什么要什么，不是已经按创世配好了 interchangeable / 877 abci20-upgrade-notgenesis interchangeable。
- **看见应用配了参数 不是已经是应用自己决定存什么：** 看见应用配了参数，不是已经是应用自己决定存什么 interchangeable。
- **看见当前高度在 不是已经交差：** 看见当前高度在，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看引擎按当前高度决定存什么要什么 正式三事（346 余量），先数清问的是是不是已经按创世配好了、是不是已经是应用自己决定存什么、还是看见当前高度在是不是已经交差，再决定要不要同一次发布。346 abci20 vs height bundled unbundling 在本页 item 3 完成。
