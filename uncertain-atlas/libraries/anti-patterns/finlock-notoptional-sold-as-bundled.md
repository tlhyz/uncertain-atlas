# 反模式：把 FinalizeBlock When no calls to CheckTx on new transactions not CheckTx optional / not already in pool / not finlock bundled 正式三事（588 余量）说成已经 CheckTx 可选 / 已经进池 / 已经 finlock bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[FinalizeBlock When no calls to CheckTx on new transactions not CheckTx optional ≠ bundled（588）](../../tracks/implementation/worked-example-finlock-notoptional-vs-bundled.md)。

## 错在哪里

把 no calls to `CheckTx` on new transactions / 新交易不再进 CheckTx 写成已经 CheckTx 技术上可选 interchangeable，或已经 CheckTx optional / not involved in processing blocks interchangeable；把 no calls on new transactions 写成已经进了池 interchangeable，或已经开始了流言 interchangeable；把 no calls on new transactions 写成已经是 FinalizeBlock When locks mempool 正式三事 bundled（588） interchangeable，或已经 finlock bundled interchangeable，或已经和 locks the mempool / locks mempool after persist / 373 / 312 / 33 / 629 / 631 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When no calls to CheckTx on new transactions not CheckTx optional / not already in pool / not finlock bundled 正式三事（588 余量），必须分开 not CheckTx optional、not already in pool、not finlock bundled 三件事，不要和 588 / 373 / 312 / 33 / 629 / 631 糊成一句。

## 和相邻反模式

- [finlock-notsettled-sold-as-bundled](finlock-notsettled-sold-as-bundled.md) 是 588 item 1 余量 / 629 专用，不是本页 588 item 2 单句边界。
- [checktxopt-sold-as-block](checktxopt-sold-as-block.md) 是 CheckTx 可选（373），不是本页 When 第 7 步 no calls on new transactions 单句边界。
- [finlock-sold-as-settled](finlock-sold-as-settled.md) 是 588 finlock bundled 三事专用，不是本页 item 2 单句边界。
- [finalizeafter-sold-as-commit](finalizeafter-sold-as-commit.md) 是 Finalize 之后 bundled（403），不是本页 no calls on new transactions 单句边界。
