# 模式：把 Info 请求 version 是 CometBFT 软件语义版本不是已经是 app_version not already appversion / not already matched / not already settled 正式三事（379 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Request。  
**例**：[填了 version not already appversion ≠ bundled（379）](../../tracks/implementation/worked-example-infover-notappversion-vs-bundled.md)。

## 三个名字

1. **填了 version 不是 already appversion：** 看见填了 version / Info 请求 version 是 CometBFT 软件语义版本 / 填了 version 字段，不是已经是 app_version interchangeable / 已经 appversion interchangeable / 已经是 app_version 交差 interchangeable，不是 379 infover bundled interchangeable / infover-sold-as-appversion interchangeable。

2. **有软件版本 不是 already matched：** 看见有软件版本 / 有 CometBFT 软件语义版本 / 有版本字符串，不是已经印进本头 AppHash interchangeable / 已经 matched interchangeable / 已经印进每块头交差 interchangeable，不是 147 apphash-this-block interchangeable / 370 info-handshake interchangeable。

3. **能回 不是 already settled：** 看见能回 / 能回 Info / 有回包，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 323 transition interchangeable / 379 infover item 2 interchangeable。

官方把填了 version、不是已经印进本头 AppHash、不是已经交差写成三个名字。把它们叫成一个「看见填了 version 就已经是 app_version interchangeable / 就已经印进本头 AppHash interchangeable / 就已经交差 interchangeable」，会把 not already appversion、not already matched、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info 请求 version 是 CometBFT 软件语义版本不是已经是 app_version not already appversion / not already matched / not already settled 正式三事（379 余量），先数清问的是填了 version 是不是 already appversion / 379 / infover-sold-as-appversion，是不是有软件版本 是不是 already matched，还是能回 是不是 already settled，再决定要不要同一次发布。379 infover-vs-appversion bundled unbundling 在本页 item 1 启动。
