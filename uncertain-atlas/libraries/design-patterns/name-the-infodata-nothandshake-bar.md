# 模式：把 Info 回包 data not already handshake / not already snapshot replay / not already settled 正式三事（389 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Response / Query Response。  
**例**：[Info ≠ bundled（389）](../../tracks/implementation/worked-example-infodata-nothandshake-vs-bundled.md)。

## 三个名字

1. **data 不是已经握手对齐：** 看见回了 data，不是已经 370 interchangeable / 761 infodata-nothandshake interchangeable。
2. **看见回了 data 不是已经是快照重放：** 看见有任意字段，不是已经 370 interchangeable。
3. **看见能填 不是已经交差：** 看见 Info 回包 data，不是已经交差 interchangeable。

官方把 Info 回包 data / Info 回包 version / Query 回包 codespace 三条核心句拆成三个名字。把它们叫成一个「看见回了 Info 余栏就已经是握手对齐」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info 回包 data 正式三事（389 余量），先数清问的是 data 是不是已经握手对齐 / 370、是不是已经是快照重放 / 370、还是看见能填是不是已经交差，再决定要不要同一次发布。389 infodata vs appversion bundled unbundling 在本页 item 1 启动。
