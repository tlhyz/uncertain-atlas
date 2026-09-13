# 模式：把 OfferSnapshot Usage bootstrap accept/reject 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) OfferSnapshot Usage。  
**例**：[bootstrapping state sync / may accept or reject ≠ OfferSnapshot 请求 bundled](../../tracks/implementation/worked-example-offersnapusage-bootstrap-vs-bundled.md)。

## 三个名字

1. **bootstrapping state sync / may accept or reject 不是 OfferSnapshot 请求 bundled：** 看见 Methods OfferSnapshot Usage bootstrap，不是 396 请求 bundled interchangeable。
2. **Upon accepting retrieve and apply chunks 不是 Offer 收下就已经装完：** 看见 Accept 后拉块装块，不是 321 已经装完 interchangeable。
3. **reject in chunk response / further Offer 不是 Offer 收下之后 bundled：** 看见 chunk response reject 还要再收 Offer，不是 401 bundled interchangeable。

## 为什么要分开叫

官方把 OfferSnapshot Usage 第一段、OfferSnapshot 请求 bundled（396）、Offer 收下之后 bundled（401）、Offer 收下就已经装完（321）写成三个名字。把它们叫成一个「看见 Offer 了就已经本地清单 interchangeable、已经装完、已经必须实现快照连接」，会把 bootstrap accept/reject、upon accepting 拉块装块、chunk response reject 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 OfferSnapshot Usage bootstrap accept/reject 正式三事，先数清问的是 bootstrapping state sync / may accept or reject 是不是 OfferSnapshot 请求 bundled interchangeable / 已经本地清单、Upon accepting retrieve and apply chunks 是不是 Offer 收下就已经装完 interchangeable / 已经齐、reject in chunk response prepared for further Offer 是不是 Offer 收下之后 bundled interchangeable / 已经 ABORT / 已经 REJECT_SNAPSHOT，再决定要不要同一次发布。
