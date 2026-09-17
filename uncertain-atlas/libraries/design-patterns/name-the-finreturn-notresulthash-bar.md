# 模式：把 FinalizeBlock When CometBFT hashes into ResultHash not Code / Data 印进本头 LastResultsHash / not this header LastResultsHash 正式三事（587 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When step 5。  
**例**：[FinalizeBlock When CometBFT hashes into ResultHash not Code / Data 印进本头 ≠ bundled（587）](../../tracks/implementation/worked-example-finreturn-notresulthash-vs-bundled.md)。

## 三个名字

1. **CometBFT hashes into ResultHash 不是 Code / Data 印进本头：** 看见 hashes all the transaction outputs and stores it in ResultHash 不是已经 Code / Data 印进本头 LastResultsHash interchangeable，不是 316 ExecTxResult interchangeable / 316 Code Data 印进本头 interchangeable / 614 notheader interchangeable。
2. **CometBFT hashes into ResultHash 不是本头 LastResultsHash：** 看见 hashes into ResultHash 不是已经是本头 LastResultsHash interchangeable，不是 147 apphash vs this block interchangeable / 335 finpersist interchangeable / 362 finwhen interchangeable / 601 notsettled interchangeable。
3. **CometBFT hashes into ResultHash 不是 finreturn bundled：** 看见 hashes into ResultHash 不是已经 finreturn bundled interchangeable，不是 614 notheader interchangeable / 616 notpersist interchangeable / 587 finreturn item 1 Application returns interchangeable / 587 finreturn item 3 persists interchangeable。

## 为什么要分开叫

官方把 When 第 5 步 hashes into ResultHash、第 4 步 Application returns AppHash + tx outputs、第 6 步 persists 这三份写成三个名字。把它们叫成一个「看见 hashes into ResultHash 就已经 Code / Data 印进本头 interchangeable、就已经是本头 LastResultsHash interchangeable、就已经 finreturn bundled interchangeable」，会把 not Code / Data 印进本头、not this header LastResultsHash、not finreturn bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When CometBFT hashes into ResultHash not Code / Data 印进本头 LastResultsHash / not this header LastResultsHash 正式三事（587 余量），先数清问的是 hashes into ResultHash 是不是 already Code / Data 印进本头 / 316 / 614，是不是 already 本头 LastResultsHash / 147 / 335，还是 hashes into ResultHash 是不是 already finreturn bundled / 614 / 616，再决定要不要同一次发布。
