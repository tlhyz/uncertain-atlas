# 模式：把 FinalizeBlock When all outstanding transactions in the mempool not new transactions / not CheckTx passed forever valid / not finrecheck bundled 正式三事（591 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When step 9。  
**例**：[FinalizeBlock When all outstanding transactions in the mempool not new transactions ≠ bundled（591）](../../tracks/implementation/worked-example-finrecheck-notoutstanding-vs-bundled.md)。

## 三个名字

1. **outstanding txs 不是 new transactions：** 看见 all outstanding transactions in the mempool / 池里剩下的 outstanding txs，不是已经 no calls to CheckTx on new transactions interchangeable，不是 588 finlock interchangeable / 630 notoptional interchangeable / 633 notlock interchangeable / 312 RECHECK not new txs interchangeable。
2. **outstanding txs 不是 CheckTx 过了就永远有效：** 看见 re-checks outstanding，不是已经 CheckTx 过了就永远有效 interchangeable，不是 301 mempool interchangeable / 301 proposed-sold-as-removed interchangeable / 339 checktxweak interchangeable / 33 four gates interchangeable。
3. **outstanding txs 不是 finrecheck bundled：** 看见 outstanding in mempool，不是已经 finrecheck bundled interchangeable，不是 635 finrecheck-notmust interchangeable / 637 nottype interchangeable / 591 finrecheck item 1 optionally re-checks interchangeable / 591 finrecheck item 3 not Type=RECHECK interchangeable。

## 为什么要分开叫

官方把 When 第 9 步 all outstanding transactions in the mempool、new transactions / no calls on new CheckTx、CheckTx 过了就永远有效、591 finrecheck bundled 三事 写成三个名字。把它们叫成一个「看见池里剩下的 outstanding txs 就已经 new transactions interchangeable、就已经 CheckTx 过了就永远有效 interchangeable、就已经 finrecheck bundled interchangeable」，会把 not new transactions、not CheckTx passed forever valid、not finrecheck bundled / not 591 item 1 / item 3 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When all outstanding transactions in the mempool not new transactions / not CheckTx passed forever valid / not finrecheck bundled 正式三事（591 余量），先数清问的是 outstanding txs 是不是 already new transactions / 588 / 630 / 633，是不是 already CheckTx passed forever valid / 301 / 339，还是 outstanding txs 是不是 already finrecheck bundled / 635 / 637，再决定要不要同一次发布。591 finrecheck unbundling 在本页 item 2 续。
