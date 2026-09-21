# 模式：把填了 Precision 不是已经是 MessageDelay not already message-delay / not already delay-bounded / not already timely 正式三事（336 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / SynchronyParams.Precision / SynchronyParams.MessageDelay。  
**例**：[填了 Precision not already message-delay ≠ bundled（336）](../../tracks/implementation/worked-example-precision-notmsgdelay-vs-bundled.md)。

## 三个名字

1. **填了 Precision 不是 already message-delay：** 看见填了 Precision / `SynchronyParams.Precision` / 钟偏那一栏，不是已经是 MessageDelay interchangeable / 已经填了延迟那一栏交差 interchangeable，不是 336 precision bundled interchangeable / 40 block-time interchangeable / precision-sold-as-msgdelay interchangeable。

2. **钟偏有界 不是 already delay-bounded：** 看见钟偏有界 / 提议者钟偏有界 / 还能出合法提案的钟偏，不是已经延迟有界 interchangeable / 已经消息延迟有界交差 interchangeable，不是 327 preparetimeout interchangeable / 336 precision item 2 interchangeable。

3. **能出合法提案 不是 already timely：** 看见能出合法提案 / 仍能出合法提案 / 钟偏有界仍能提案，不是已经 timely interchangeable / 已经及时交差 interchangeable，不是 330 veheight interchangeable / 336 precision item 3 interchangeable。

官方把填了 Precision 单句、already message-delay、already delay-bounded、already timely 写成三个名字。把它们叫成一个「看见填了 Precision 就已经是 MessageDelay interchangeable / 就已经延迟有界 interchangeable / 就已经 timely interchangeable」，会把 not already message-delay、not already delay-bounded、not already timely 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看填了 Precision 不是已经是 MessageDelay not already message-delay / not already delay-bounded / not already timely 正式三事（336 余量），先数清问的是填了 Precision 是不是 already message-delay / 336 / precision-sold-as-msgdelay，是不是钟偏有界 是不是 already delay-bounded，还是能出合法提案 是不是 already timely，再决定要不要同一次发布。336 precision vs msgdelay bundled unbundling 在本页 item 1 启动。
