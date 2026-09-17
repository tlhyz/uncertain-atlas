# 反模式：把 FinalizeBlock When CometBFT hashes into ResultHash not Code / Data 印进本头 LastResultsHash / not this header LastResultsHash 正式三事（587 余量）说成已经 Code / Data 印进本头 / 已经是本头 LastResultsHash / 已经 finreturn bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[FinalizeBlock When CometBFT hashes into ResultHash not Code / Data 印进本头 ≠ bundled（587）](../../tracks/implementation/worked-example-finreturn-notresulthash-vs-bundled.md)。

## 错在哪里

把 CometBFT hashes all the transaction outputs and stores it in ResultHash 写成已经 Code / Data 印进本头 LastResultsHash interchangeable，或已经 tx_results Code Data 编进 LastResultsHash interchangeable；把 hashes into ResultHash 写成已经是本头 LastResultsHash interchangeable，或已经本头 LastResultsHash 就代表本高度 tx 已经交差 interchangeable；把 hashes into ResultHash 写成已经是 FinalizeBlock When AppHash tx outputs ResultHash persist 正式三事 bundled（587） interchangeable，或已经 finreturn bundled interchangeable，或已经和 Application returns AppHash + tx outputs / CometBFT persists tx outputs / AppHash / ResultsHash / 316 / 614 / 616 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When CometBFT hashes into ResultHash not Code / Data 印进本头 LastResultsHash / not this header LastResultsHash 正式三事（587 余量），必须分开 not Code / Data 印进本头、not this header LastResultsHash、not finreturn bundled 三件事，不要和 587 / 316 / 614 / 616 糊成一句。

## 和相邻反模式

- [finreturn-notheader-sold-as-bundled](finreturn-notheader-sold-as-bundled.md) 是 587 finreturn item 1 Application returns，不是本页 When 第 5 步 hashes into ResultHash 单句边界。
- [finreturn-sold-as-header](finreturn-sold-as-header.md) 是 587 finreturn bundled 三事专用，不是本页 587 item 2 单句边界。
- [exectxresult-sold-as-consensus](exectxresult-sold-as-consensus.md) 是 Code / Data 就已经印进本头（316），不是本页 hashes into ResultHash 单句边界。
