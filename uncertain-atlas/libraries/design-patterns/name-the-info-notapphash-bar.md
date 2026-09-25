# 模式：把 app_version 进每块头不是已经印进本头 AppHash not already apphash / not already settled / not already algo 正式三事（370 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Usage。  
**例**：[有版本 not already apphash ≠ bundled（370）](../../tracks/implementation/worked-example-info-notapphash-vs-bundled.md)。

## 三个名字

1. **有版本 不是 already apphash：** 看见有版本 / 回的 `app_version` 会写进每一块的头 / 有 app_version，不是已经印进本头 AppHash interchangeable / 已经 apphash interchangeable / 已经印进本头 AppHash 交差 interchangeable，不是 370 info bundled interchangeable / info-sold-as-handshake interchangeable。

2. **进了头 不是 already settled：** 看见进了头 / 会写进每一块的 Header / 进头了，不是已经是本高度交差 interchangeable / 已经 settled interchangeable / 已经是本高度交差交差 interchangeable，不是 147 apphash interchangeable / 857 info-notstatesync interchangeable。

3. **字段在 不是 already algo：** 看见字段在 / app_version 字段在 / 版本字段在，不是已经选型 interchangeable / 已经 algo interchangeable / 已经选型交差 interchangeable，不是 859 info-notpersist interchangeable / 389 infover interchangeable。

官方把有版本、不是已经是本高度交差、不是已经选型写成三个名字。把它们叫成一个「看见有版本就已经印进本头 AppHash interchangeable / 就已经是本高度交差 interchangeable / 就已经选型 interchangeable」，会把 not already apphash、not already settled、not already algo 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 app_version 进每块头不是已经印进本头 AppHash not already apphash / not already settled / not already algo 正式三事（370 余量），先数清问的是有版本 是不是 already apphash / 370 / info-sold-as-handshake，是不是进了头 是不是 already settled，还是字段在 是不是 already algo，再决定要不要同一次发布。370 info-vs-handshake bundled unbundling 在本页 item 2 续。
