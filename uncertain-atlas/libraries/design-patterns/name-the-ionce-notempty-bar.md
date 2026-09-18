# 模式：点名 ionce-notempty 杠

**层次**：实现 / InitChain may-choose-set not already no-set / not already genesis-used / not already app-checked 正式三事（412 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Usage。  
**对应**：[`../tracks/implementation/worked-example-ionce-notempty-vs-bundled.md`](../tracks/implementation/worked-example-ionce-notempty-vs-bundled.md)。

- **may-choose-set 不是已经没有集合：** 看见能决定，不是已经没有集合 interchangeable / 1092 ionce-notempty interchangeable。
- **看见能算另一套 不是已经用了创世文件：** 看见能算另一套，不是已经用了创世文件里的验证者 interchangeable。
- **看见有创世应用信息 不是已经验过应用状态：** 看见有创世应用信息，不是已经验过应用状态 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 may-choose-set 正式三事（412 余量），先数清问的是是不是已经没有集合、是不是已经用了创世文件、还是看见有创世应用信息是不是已经验过应用状态，再决定要不要同一次发布。412 initonce vs crash bundled unbundling 在本页 item 2 续。
