# 模式：把 FinalizeBlock When newly received transactions can now be checked not optional recheck outstanding txs / not CheckTx optional / not finunlock bundled 正式三事（592 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When step 10。  
**例**：[FinalizeBlock When newly received transactions can now be checked not optional recheck outstanding txs ≠ bundled（592）](../../tracks/implementation/worked-example-finunlock-notnewly-vs-bundled.md)。

## 三个名字

1. **newly received can now be checked 不是 optional recheck outstanding txs：** 看见 newly received transactions can now be checked / 新收到的交易现在可以 CheckTx，不是已经 optionally re-checks all outstanding transactions in the mempool interchangeable，不是 591 finrecheck interchangeable / 636 finrecheck-notoutstanding interchangeable / 635 finrecheck-notmust interchangeable / 637 finrecheck-nottype interchangeable / 634 notrecheck interchangeable。
2. **newly received can now be checked 不是 CheckTx optional：** 看见 can now be checked，不是已经 CheckTx technically optional — not involved in processing blocks interchangeable，不是 373 checktxopt interchangeable / 312 checktxopt interchangeable / 313 checktxguard interchangeable / 630 notoptional interchangeable / 339 checktxweak interchangeable。
3. **newly received can now be checked 不是 finunlock bundled：** 看见 newly received can now be checked，不是已经 finunlock bundled interchangeable，不是 638 finunlock-notsettled interchangeable / 640 finunlock-notcommitlock interchangeable / 592 finunlock item 1 unlocks the mempool interchangeable / 592 finunlock item 3 unlock after optional recheck interchangeable。

## 为什么要分开叫

官方把 When 第 10 步 newly received transactions can now be checked、optional recheck outstanding / CheckTx optional、592 finunlock bundled 三事 写成三个名字。把它们叫成一个「看见新收到的交易现在可以 CheckTx 就已经 optional recheck outstanding txs interchangeable、就已经 CheckTx 技术上可选 interchangeable、就已经 finunlock bundled interchangeable」，会把 not optional recheck outstanding txs、not CheckTx optional、not finunlock bundled / not 592 item 1 / item 3 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When newly received transactions can now be checked not optional recheck outstanding txs / not CheckTx optional / not finunlock bundled 正式三事（592 余量），先数清问的是 newly received can now be checked 是不是 already optional recheck outstanding txs / 591 / 636 / 635 / 637，是不是 already CheckTx optional / 373 / 630 / 312 / 339，还是 newly received can now be checked 是不是 already finunlock bundled / 638 / 640，再决定要不要同一次发布。592 finunlock unbundling 在本页 item 2 续。
