# 反模式：把 OfferSnapshot Usage bootstrap accept/reject 正式三事卖成 OfferSnapshot 请求 bundled interchangeable / 已经装完 / 已经必须实现快照连接

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[bootstrapping state sync / may accept or reject ≠ OfferSnapshot 请求 bundled](../../tracks/implementation/worked-example-offersnapusage-bootstrap-vs-bundled.md)。

## 卖法

- 「看见 OfferSnapshot is called when bootstrapping a node using state sync / application may accept or reject snapshots as appropriate / 用 state sync 引导节点时会叫 OfferSnapshot、应用可以按情况接受或拒绝 就已经 OfferSnapshot 请求 snapshot 是本地清单 interchangeable / 回包 result 是这次 Offer 的结果 interchangeable / 已经必须实现快照连接 interchangeable。」
- 「看见 Upon accepting, CometBFT will retrieve and apply snapshot chunks via ApplySnapshotChunk / Accept 之后引擎会去拉块并装 就已经 Offer 收下就已经装完 interchangeable / Offer 收下之后 bundled interchangeable / 已经齐 interchangeable。」
- 「看见 reject a snapshot in the chunk response / prepared to accept further OfferSnapshot calls / 在装 chunk 的回包里拒掉这份、还要再收 Offer 就已经 Offer 收下之后 bundled interchangeable / 已经 ABORT interchangeable / 已经 REJECT_SNAPSHOT interchangeable。」

## 为什么错

官方把 OfferSnapshot Usage 第一段核心句写成三件独立的实现事。把它们卖成 OfferSnapshot 请求 bundled interchangeable / 已经装完 / 已经必须实现快照连接，会把 bootstrap accept/reject、upon accepting 拉块装块、chunk response reject 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 OfferSnapshot Usage bootstrap accept/reject 正式三事，必须分开 bootstrapping state sync / may accept or reject、Upon accepting retrieve and apply chunks、reject in chunk response prepared for further Offer 三个名字，不要把它们卖成 OfferSnapshot 请求 bundled interchangeable / 已经装完 / 已经必须实现快照连接。

## 和相邻反模式

- [offersnap-sold-as-listed](offersnap-sold-as-listed.md) 是 OfferSnapshot 请求 bundled 三事，不是本页 Methods OfferSnapshot Usage bootstrap 单句专用边界。
- [offersnaptrust-sold-as-metadata](offersnaptrust-sold-as-metadata.md) 是 OfferSnapshot Usage trust 正式三事 part 2，不是本页 bootstrap accept/reject 专用边界。
