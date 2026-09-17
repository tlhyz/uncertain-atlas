# 例：看见 Code 非零 is not already out-of-block interchangeable / not already unindexed interchangeable / not already checktx-scale interchangeable

**层次**：实现 / Code 非零 not already out-of-block / not already unindexed / not already checktx-scale 正式三事（316 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Transaction Results / ExecTxResult。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「Code 非零 not already out-of-block / not already unindexed / not already checktx-scale 正式三事（316 余量）/ not 1014 exectx-notout interchangeable / not 316 exectxresult-vs-consensus bundled interchangeable」，不是 ExecTxResult bundled（316），也不是 MaxGas 已经在执行（315），也不是 CheckTx 绿就已经永远有效（301/994）。不要另写怎样编回执或怎样建索引。

## 官方三件事

1. **看见 Code ≠ 0 / 看见标成无效 这份回执 is not already 已经没进块 interchangeable，也不是已经 ExecTxResult bundled（316） interchangeable / 1014 exectx-notout interchangeable / 1013 exectx-notorder interchangeable / 316 exectx item 1 结果列表 interchangeable，也不是已经 Code 非零 not already out-of-block / not already unindexed / not already checktx-scale 正式三事 bundled（316 item 2 余量） interchangeable / 316 exectx item 2 interchangeable。**  
   官方写：FinalizeBlock 把已决定块连同全部交易同步交给应用。若 Code ≠ 0，这笔会被标成无效，但仍在块里。看见标成无效，不是已经没进块 interchangeable——本页从 316 item 2 侧钉 not already out-of-block 单句。316 exectxresult vs consensus bundled unbundling 在本页 item 2 续。

2. **看见没索引 / 看见标成无效 / 这份回执 is not already 已经没进共识 interchangeable，也不是已经 ExecTxResult bundled（316） interchangeable / 1014 exectx-notout interchangeable / 316 exectx item 3 Code Data interchangeable / 1015 exectx-notheader interchangeable，也不是已经 MaxGas 已经在执行 interchangeable / 315 maxgas interchangeable。**  
   官方把无效交易不建索引和已经没进共识分开。看见没索引，不是已经没进共识 interchangeable。本页钉 not already unindexed 单句。

3. **看见类比 CheckTx / 看见标成无效 / 这份回执 is not already 已经和池门同一把尺 interchangeable，也不是已经 ExecTxResult bundled（316） interchangeable / 1014 exectx-notout interchangeable / 1013 exectx-notorder interchangeable，也不是已经 CheckTx 绿就已经永远有效 interchangeable / 301/994 proposed-notforever interchangeable。**  
   官方把类比 CheckTx 和已经和池门同一把尺分开。看见类比 CheckTx，不是已经和池门同一把尺 interchangeable。316 exectxresult vs consensus bundled unbundling 在本页 item 2 续。

怎样编回执、怎样建索引、怎样算 LastResultsHash 是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **Code 非零 not already out-of-block ≠ 已经没进块 interchangeable：** 官方把标无效、仍在块里、不建索引分开。
- **看见没索引 not already unindexed ≠ 已经没进共识 interchangeable：** 官方把不建索引和已经没进共识分开。
- **看见类比 CheckTx not already checktx-scale ≠ 已经和池门同一把尺 interchangeable：** 官方把类比 CheckTx 和已经和池门同一把尺分开；316 exectxresult vs consensus bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Code ≠ 0 仍在块里 | 不是已经没进块，也不是已经建了索引 | 不是 MaxGas 已经在执行（315） |
| 看见没索引 | 不是已经没进共识 | 不是 CheckTx 绿就已经永远有效（301/994） |
| 看见类比 CheckTx | 不是已经和池门同一把尺 | 不是 Code/Data 就已经印进本头（1015） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Code 非零 not already out-of-block / not already unindexed / not already checktx-scale 正式三事（316 余量），必须分开是不是已经没进块、是不是已经没进共识、是不是已经和池门同一把尺。可以跳过「看见回了就已经对上顺序」。不要另写怎样编回执或怎样建索引。316 exectxresult vs consensus bundled unbundling 在本页 item 2 续；续 [`worked-example-exectx-notheader-vs-bundled.md`](worked-example-exectx-notheader-vs-bundled.md)（不变量 1015 item 3）。

## 本页不抄

- 怎样编回执、怎样建索引、怎样算 LastResultsHash。
- ExecTxResult bundled。那是不变量 316。
- MaxGas 已经在执行。那是不变量 315。
- CheckTx 绿就已经永远有效。那是不变量 301/994。
