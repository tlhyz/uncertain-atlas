# 模式：把必须协调升级不是已经只改 VoteExtensionsEnableHeight not already only-veheight / not already single-node / not already field-filled 正式三事（346 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Application configuration required to switch to ABCI 2.0。  
**例**：[必须协调升级 not already only-veheight ≠ bundled（346）](../../tracks/implementation/worked-example-abci20-notonlyveheight-vs-bundled.md)。

## 三个名字

1. **必须协调升级 不是 already only-veheight：** 看见必须协调升级 / 切到带扩展的 CometBFT / 字段已经在参数表里，不是已经只改 `VoteExtensionsEnableHeight` interchangeable / 已经 only-veheight interchangeable / 已经只改字段交差 interchangeable，不是 346 abci20upgrade bundled interchangeable / abci20upgrade-sold-as-height interchangeable。

2. **一个节点升了二进制 不是 already single-node：** 看见一个节点升了二进制 / 单节点升了版本 / 本机已经换了带扩展的二进制，不是已经是单节点能切 interchangeable / 已经 single-node interchangeable / 已经单节点切完交差 interchangeable，不是 58 enable-height interchangeable / 330 veheight interchangeable。

3. **能改启用高度 不是 already field-filled：** 看见能改启用高度 / 字段填了 / `VoteExtensionsEnableHeight` 可写，不是已经做了这次升级 interchangeable / 已经 field-filled interchangeable / 已经 field-filled 交差 interchangeable，不是 792 abci20-notwritecurrent interchangeable / 793 abci20-notgenesiscfg interchangeable。

官方把换二进制的协调升级、不是单节点能切、不是已经做了这次升级写成三个名字。把它们叫成一个「看见填了启用高度就已经切到 ABCI 2.0 interchangeable / 就已经单节点能切 interchangeable / 就已经做了这次升级 interchangeable」，会把 not already only-veheight、not already single-node、not already field-filled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看必须协调升级不是已经只改 VoteExtensionsEnableHeight not already only-veheight / not already single-node / not already field-filled 正式三事（346 余量），先数清问的是必须协调升级 是不是 already only-veheight / 346 / abci20upgrade-sold-as-height，是不是一个节点升了二进制 是不是 already single-node，还是能改启用高度 是不是 already field-filled，再决定要不要同一次发布。346 abci20 vs height bundled unbundling 在本页 item 1 启动。
