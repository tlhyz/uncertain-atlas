# 模式：点名 h_e 必须高于当前 not already current height / not already height-H Prepare / not already settled 正式三事（346 余量）

**层次**：实现 / ABCI 2.0 协调升级。  
**分类**：建议（产品）。  
**对应例**：[worked-example-abci20-upgrade-notcurrent-vs-bundled.md](../../tracks/implementation/worked-example-abci20-upgrade-notcurrent-vs-bundled.md)。

h_e 必须高于当前 not already current height / not already height-H Prepare / not already settled 正式三事（346 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **h_e 必须高于当前 不是已经能写成当前高度：** 看见 *h<sub>e</sub>* 必须高于当前，不是已经能写成当前高度 interchangeable / 876 abci20-upgrade-notcurrent interchangeable。
- **看见必须比当前高 不是已经是到了 H 才 Prepare 带扩展：** 看见必须比当前高，不是已经是到了 H 才 Prepare 带扩展 interchangeable。
- **看见升级过了 不是已经交差：** 看见升级过了，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 h_e 必须高于当前 正式三事（346 余量），先数清问的是是不是已经能写成当前高度、是不是已经是到了 H 才 Prepare 带扩展、还是看见升级过了是不是已经交差，再决定要不要同一次发布。346 abci20 vs height bundled unbundling 在本页 item 2 续。
