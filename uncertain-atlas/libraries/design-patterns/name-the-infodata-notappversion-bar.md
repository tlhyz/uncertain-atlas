# 模式：把 Info 回包 version not already app_version / not already header AppHash / not already settled 正式三事（389 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Response / Query Response。  
**例**：[Info ≠ bundled（389）](../../tracks/implementation/worked-example-infodata-notappversion-vs-bundled.md)。

## 三个名字

1. **version 不是已经是 app_version：** 看见回了应用版本，不是已经 379 interchangeable / 762 infodata-notappversion interchangeable。
2. **看见回了应用版本 不是已经印进本头：** 看见有语义版本，不是已经印进每块头 interchangeable。
3. **看见能回 不是已经交差：** 看见 Info 回包 version，不是已经交差 interchangeable。

官方把 Info 回包 data / Info 回包 version / Query 回包 codespace 三条核心句拆成三个名字。把它们叫成一个「看见回了 Info 余栏就已经是握手对齐」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info 回包 version 正式三事（389 余量），先数清问的是 version 是不是已经是 app_version / 379、是不是已经印进本头、还是看见能回是不是已经交差，再决定要不要同一次发布。389 infodata vs appversion bundled unbundling 在本页 item 2 续。
