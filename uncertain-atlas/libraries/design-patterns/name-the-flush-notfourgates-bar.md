# 模式：把定期 Flush 是为了让异步请求真发出去不是已经是四门 not already fourgates / not already received / not already settled 正式三事（374 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Flush Usage。  
**例**：[定期在冲 not already fourgates ≠ bundled（374）](../../tracks/implementation/worked-example-flush-notfourgates-vs-bundled.md)。

## 三个名字

1. **定期在冲 不是 already fourgates：** 看见定期在冲 / 定期 Flush 是为了让异步请求真发出去 / 定期在冲队列，不是已经是四门 interchangeable / 已经 fourgates interchangeable / 已经是四门交差 interchangeable，不是 374 flush bundled interchangeable / flush-sold-as-sent interchangeable。

2. **发出去了 不是 already received：** 看见发出去了 / 异步请求真发出去 / 发出去，不是已经收到 interchangeable / 已经 received interchangeable / 已经收到交差 interchangeable，不是 309 HasChannel interchangeable / 869 flush-notsent interchangeable。

3. **异步 不是 already settled：** 看见异步 / 异步请求 / 异步在冲，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 33 four gates interchangeable / 374 flush item 3 interchangeable。

官方把定期在冲、不是已经收到、不是已经交差写成三个名字。把它们叫成一个「看见定期在冲就已经是四门 interchangeable / 就已经收到 interchangeable / 就已经交差 interchangeable」，会把 not already fourgates、not already received、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看定期 Flush 是为了让异步请求真发出去不是已经是四门 not already fourgates / not already received / not already settled 正式三事（374 余量），先数清问的是定期在冲 是不是 already fourgates / 374 / flush-sold-as-sent，是不是发出去了 是不是 already received，还是异步 是不是 already settled，再决定要不要同一次发布。374 flush-vs-sent bundled unbundling 在本页 item 2 续。
