# 模式：把 GasUsed 不是已经算进共识 not already in consensus / not already practical-gas checked / not already engine-enforced inequality 正式三事（315 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Gas。  
**例**：[有 GasUsed not already in consensus ≠ bundled（315）](../../tracks/implementation/worked-example-maxgas-notgasused-vs-bundled.md)。

## 三个名字

1. **有 GasUsed 不是 already in consensus：** 看见回包 GasUsed / GasUsed 字段在，不是已经算进共识 interchangeable / 已经被 CometBFT 用进共识 interchangeable，不是 315 maxgas bundled interchangeable / 704 maxgas-notenforced interchangeable / maxgas-sold-as-enforced interchangeable。

2. **GasWanted 过了池门 不是 already practical-gas checked：** 看见每笔 GasWanted <= MaxGas / 提议一块 GasWanted 之和 <= MaxGas，不是已经按实用气验过 interchangeable / 已经按 GasUsed 验过 interchangeable，不是 315 maxgas item 1 interchangeable / 704 maxgas-notenforced interchangeable。

3. **应用应强制 不是 already engine-enforced inequality：** 看见官方写应用应强制 GasUsed <= GasWanted / 执行或校验应在用超之前失败，不是已经由引擎强制该不等式 interchangeable / 已经 CometBFT 强制 GasUsed <= GasWanted interchangeable，不是 315 maxgas item 3 interchangeable / 706 maxgas-notcommitted interchangeable。

官方把有 GasUsed 单句、already in consensus、already practical-gas checked、already engine-enforced inequality 写成三个名字。把它们叫成一个「看见有 GasUsed 就已经算进共识 interchangeable / 就已经按实用气验过 interchangeable / 就已经由引擎强制不等式 interchangeable」，会把 not already in consensus、not already practical-gas checked、not already engine-enforced inequality 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 GasUsed 不是已经算进共识 not already in consensus / not already practical-gas checked / not already engine-enforced inequality 正式三事（315 余量），先数清问的是有 GasUsed 是不是 already in consensus / 315 / maxgas-sold-as-enforced，是不是 GasWanted 过了池门 是不是 already practical-gas checked，还是应用应强制 是不是 already engine-enforced inequality，再决定要不要同一次发布。315 maxgas vs enforced bundled unbundling 在本页 item 2 完成。
