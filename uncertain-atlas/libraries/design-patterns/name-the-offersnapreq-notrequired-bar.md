# 模式：把 OfferSnapshot 引导时叫 not Snapshot Connection required / not already transitioned / not Usage bootstrap 正式三事（396 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) OfferSnapshot。  
**例**：[OfferSnapshot ≠ bundled（396）](../../tracks/implementation/worked-example-offersnapreq-notrequired-vs-bundled.md)。

## 三个名字

1. **引导时叫 不是已经必须实现快照连接：** 看见在引导时叫了，不是已经 334 interchangeable / 739 offersnapreq-notrequired interchangeable。
2. **看见在引导时叫了 不是已经切进共识：** 看见能叫，不是已经 323 interchangeable。
3. **看见能填 不是已经 Usage bootstrap：** 看见引导时叫，不是已经 499 / 647 interchangeable。

官方把 OfferSnapshot 请求 snapshot / 回包 result / 引导时叫三条核心句拆成三个名字。把它们叫成一个「看见填了 OfferSnapshot 请求就已经是本地清单」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 OfferSnapshot 引导时叫 正式三事（396 余量），先数清问的是引导时叫是不是已经必须实现快照连接 / 334、是不是已经切进共识 / 323、还是看见能填是不是已经 Usage bootstrap / 499 / 647，再决定要不要同一次发布。396 offersnap vs listed bundled unbundling 在本页 item 3 完成。
