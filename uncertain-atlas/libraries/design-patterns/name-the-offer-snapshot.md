# 模式：把 OfferSnapshot 请求三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) OfferSnapshot。  
**例**：[OfferSnapshot 请求 snapshot 是拿来装回的那份快照 ≠ 已经是本地清单](../../tracks/implementation/worked-example-offersnap-vs-listed.md)。

## 三个名字

1. **OfferSnapshot 请求 snapshot 是拿来装回的那份快照不是已经是本地清单：** 看见填了 snapshot 不是已经是同一份。
2. **OfferSnapshot 回包 result 是这次 Offer 的结果不是已经装完：** 看见回了 result 不是已经收下。
3. **OfferSnapshot 在用 state sync 引导节点时叫不是已经必须实现快照连接：** 看见在引导时叫了不是已经切进共识。

## 为什么要分开叫

官方把 OfferSnapshot 请求 `snapshot` 是拿来装回的那份快照、回包 `result` 是这次 Offer 的结果、Usage 是在用 state sync 引导节点时叫写成三件事。把它们叫成一个「看见填了 OfferSnapshot 请求就已经是本地清单」，会把本地清单、Offer 收下就已经装完和门在就必须实现一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 OfferSnapshot 请求就已经是本地清单」，先数清问的是 OfferSnapshot 请求 snapshot 是拿来装回的那份快照不是已经是本地清单、OfferSnapshot 回包 result 是这次 Offer 的结果不是已经装完，还是 OfferSnapshot 在用 state sync 引导节点时叫不是已经必须实现快照连接，再决定要不要同一次发布。
