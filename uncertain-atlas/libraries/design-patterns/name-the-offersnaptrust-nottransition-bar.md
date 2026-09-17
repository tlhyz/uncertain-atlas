# 模式：把 OfferSnapshot Usage verified AppHash at end not Info during load / not Transition to Consensus bundled / not Offer restored bundled 正式三事（483 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) OfferSnapshot Usage。  
**例**：[OfferSnapshot Usage verified AppHash at end not Info during load ≠ bundled（483）](../../tracks/implementation/worked-example-offersnaptrust-nottransition-vs-bundled.md)。

## 三个名字

1. **verified AppHash at end 不是 Info during load：** 看见 The verified `AppHash` is automatically checked against the restored application at the end of snapshot restoration，不是已经在装 chunk 过程中 Info 对了 interchangeable，不是 332 snapshotverify interchangeable / 485 applysnapusage verify/Info/unable interchangeable，也不是 483 offersnaptrust bundled interchangeable / 652 offersnaptrust-nottransition interchangeable / 651 offersnaptrust-notverify interchangeable。
2. **verified AppHash at end 不是 Transition to Consensus bundled：** 看见 at the end of snapshot restoration / automatically checked at the end，不是已经 Transition to Consensus 那套 ChainID / 版本核对 interchangeable，不是 323 transition interchangeable / 370 infover interchangeable，也不是 321 offerrestored interchangeable / 322 listsnap interchangeable。
3. **verified AppHash at end 不是 Offer 装完 / Offer 收下之后 bundled：** 看见 automatically checked at the end，不是已经 Offer 收下就已经装完 interchangeable，不是 321 offerrestored interchangeable / 401 offerafter interchangeable / 648 offersnapusage-notrestored interchangeable / 378 applysnap bundled interchangeable。

## 为什么要分开叫

官方把 OfferSnapshot Usage verified AppHash at end、装过程中 Info 核对、Transition to Consensus Info 核对、Offer 装完 / Offer 收下之后 bundled 写成三个名字。把它们叫成一个「看见 verified AppHash at end 就已经装块时就 Info 对了 interchangeable / 就已经切进共识 interchangeable / 就已经 Offer 装完 interchangeable」，会把 not Info during load、not Transition to Consensus bundled、not Offer restored bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 OfferSnapshot Usage verified AppHash at end not Info during load / not Transition to Consensus bundled / not Offer restored bundled 正式三事（483 余量），先数清问的是 verified AppHash at end 是不是 Info during load / 332 / 485，是不是 Transition to Consensus bundled / 323 / 370，还是 verified AppHash at end 是不是 Offer 装完 / Offer 收下之后 / 321 / 401 / 648，再决定要不要同一次发布。483 offersnaptrust unbundling 在本页 item 3 完成。
