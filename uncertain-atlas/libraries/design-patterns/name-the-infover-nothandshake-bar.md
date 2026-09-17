# 模式：把 abci_version not already handshake / not already prioritized / not already settled 正式三事（379 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Request。  
**例**：[abci_version ≠ bundled（379）](../../tracks/implementation/worked-example-infover-nothandshake-vs-bundled.md)。

## 三个名字

1. **abci_version 不是已经是握手对齐：** 看见写了语义版本，不是已经 370 interchangeable / 793 infover-nothandshake interchangeable。
2. **看见写了语义版本 不是已经排了优先：** 看见显示成 X.X.x，不是已经 367 interchangeable。
3. **看见有脚注 不是已经交差：** 看见 abci_version，不是已经交差 interchangeable。

官方把 Info 请求 version / block_version / p2p_version / abci_version 三条核心句拆成三个名字。把它们叫成一个「看见 Info 请求带了版本就已经是 app_version」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 abci_version 正式三事（379 余量），先数清问的是是不是已经是握手对齐 / 370、是不是已经排了优先 / 367、还是看见有脚注是不是已经交差，再决定要不要同一次发布。379 infover vs appversion bundled unbundling 在本页 item 3 完成。
