# 例：看见标成无效 / 没索引 / 类比 CheckTx is not already already excluded from block interchangeable / already excluded from consensus interchangeable / already same as CheckTx gate interchangeable

**层次**：实现 / Code 非零不是已经没进块 not already excluded from block / not already excluded from consensus / not already same as CheckTx gate 正式三事（316 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Transaction Results / Specifics of `ExecTxResult`。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Code 非零不是已经没进块 not already excluded from block / not already excluded from consensus / not already same as CheckTx gate 正式三事（316 余量）/ not 708 exectxresult-notexcluded interchangeable / not 316 exectxresult bundled interchangeable」，不是 ExecTxResult vs consensus bundled（316），也不是结果列表不是已经同一顺序（707 item 1 余量）或 Code / Data 不是已经印进本头（709 item 3 余量）。不要另写怎样编回执或怎样建索引。

## 官方三件事

规范把 Requirements 里若 `Code ≠ 0` 这笔会被标成无效、**但仍在块里**、无效交易**不建索引**、官方把它类比成没过 `CheckTx` 的那些 和「已经是标成无效就已经没进块 interchangeable / 已经是没索引就已经没进共识 interchangeable / 已经是类比 CheckTx 就已经和池门同一把尺 interchangeable / 已经是 ExecTxResult vs consensus bundled interchangeable」分开写成三件独立的实现事，不是「看见 Code 非零 就已经没进块 interchangeable / 就已经没进共识 interchangeable / 就已经和池门同一把尺 interchangeable」一件事：

1. **看见标成无效 / 看见 Code ≠ 0 / 看见标成无效交易 is not already 已经没进块 interchangeable / 已经 excluded from block interchangeable / 已经从块里删掉 interchangeable / 316 exectxresult bundled interchangeable / 33 four gates interchangeable / exectxresult-sold-as-consensus interchangeable，也不是已经 ExecTxResult vs consensus bundled（316） interchangeable / 708 exectxresult-notexcluded interchangeable / 316 exectxresult item 2 interchangeable，也不是已经 Code 非零不是已经没进块 not already excluded from block / not already excluded from consensus / not already same as CheckTx gate 正式三事 bundled（316 item 2 余量） interchangeable / 316 exectxresult item 2 interchangeable，也不是已经结果列表不是已经同一顺序（707） interchangeable / 709 exectxresult-notheader interchangeable / 315 maxgas interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：若 `Code ≠ 0`，这笔会被标成无效，**但仍在块里**。看见标成无效，不是已经没进块 interchangeable——316 钉 bundled 三事，本页从 item 2 侧钉 not already excluded from block 单句。看见 Code ≠ 0，不是已经 ExecTxResult vs consensus bundled（316） interchangeable——316 钉 bundled，本页钉 item 2 第一件事。看见标成无效交易，不是已经结果列表不是已经同一顺序（707） interchangeable——707 另钉 item 1，本页钉 item 2 第一件事。316 exectxresult vs consensus bundled unbundling 在本页 item 2 续。

2. **看见没索引 / 看见无效交易不建索引 / 看见不建索引 is not already 已经没进共识 interchangeable / 已经 excluded from consensus interchangeable / 已经没进 Agreement 那份 interchangeable / 316 exectxresult bundled interchangeable / 707 exectxresult-notorder interchangeable，也不是已经 ExecTxResult vs consensus bundled（316） interchangeable / 708 exectxresult-notexcluded interchangeable / 316 exectxresult item 1 顺序 interchangeable / 316 exectxresult item 3 Code Data interchangeable，也不是已经 Code 非零不是已经没进块 not already excluded from block / not already excluded from consensus / not already same as CheckTx gate 正式三事 bundled（316 item 2 余量） interchangeable / 316 exectxresult item 2 interchangeable，也不是已经没进块（本页第一件事） interchangeable。**  
   官方把不建索引和已经没进共识路径分开——没索引，不等于已经没进共识；正确节点上这块（因而交易顺序）由共识的 Agreement 保证同一份。看见没索引，不是已经没进共识 interchangeable——本页钉 not already excluded from consensus 单句。看见无效交易不建索引，不是已经结果列表不是已经同一顺序（707） interchangeable——707 另钉 item 1，本页钉 item 2 第二件事。看见不建索引，不是已经 Code / Data 不是已经印进本头（709） interchangeable——709 另钉 item 3，本页钉 item 2 第二件事。316 exectxresult vs consensus bundled unbundling 在本页 item 2 续。

3. **看见类比 CheckTx / 看见官方把它类比成没过 CheckTx / 看见类比池门 is not already 已经和池门同一把尺 interchangeable / 已经 same as CheckTx gate interchangeable / 已经和 CheckTx 同一门 interchangeable / 316 exectxresult bundled interchangeable / 33 four gates interchangeable，也不是已经 ExecTxResult vs consensus bundled（316） interchangeable / 708 exectxresult-notexcluded interchangeable / 316 exectxresult item 1 / 316 exectxresult item 3，也不是已经 Code 非零不是已经没进块 not already excluded from block / not already excluded from consensus / not already same as CheckTx gate 正式三事 bundled（316 item 2 余量） interchangeable / 316 exectxresult item 2 interchangeable，也不是已经没进块（本页第一件事） interchangeable / 已经没进共识（本页第二件事） interchangeable。**  
   官方把类比成没过 CheckTx 的那些和已经和池门同一把尺路径分开——类比 CheckTx，不等于已经和池门同一把尺。看见类比 CheckTx，不是已经和池门同一把尺 interchangeable——本页钉 not already same as CheckTx gate 单句。看见官方把它类比成没过 CheckTx，不是已经没进块（本页第一件事） interchangeable——三件事分开钉。看见类比池门，不是已经四门已经结算（33） interchangeable——33 另钉。316 exectxresult vs consensus bundled unbundling 在本页 item 2 完成。

怎样编回执、怎样建索引、怎样算 LastResultsHash 是规范里的取值或做法，本页不抄。ExecTxResult vs consensus bundled（316）、结果列表不是已经同一顺序（316 item 1 余量 / 707）、Code / Data 不是已经印进本头（316 item 3 余量 / 709）、四门已经结算（33）、MaxGas（315）是另外那套，本页不抄。

## 官方为什么这样拆

- **标成无效 not already excluded from block ≠ 316 / 33 interchangeable：** 官方把仍在块里单句和已经没进块路径分开。
- **没索引 not already excluded from consensus ≠ 已经没进共识 interchangeable：** 官方把不建索引单句和已经没进共识路径分开。
- **类比 CheckTx not already same as CheckTx gate ≠ 已经和池门同一把尺 interchangeable：** 官方把类比单句和已经同一门路径分开；316 exectxresult vs consensus bundled unbundling 在本页 item 2 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 标成无效 | 不是 already excluded from block | 不是同一顺序 alone（707） |
| 没索引 | 不是 already excluded from consensus | 不是 Code/Data 印本头 alone（709） |
| 类比 CheckTx | 不是 already same as CheckTx gate | 不是四门 alone（33） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Code 非零不是已经没进块 not already excluded from block / not already excluded from consensus / not already same as CheckTx gate 正式三事（316 余量），必须分开标成无效 是不是 already excluded from block interchangeable / 316 exectxresult bundled interchangeable / exectxresult-sold-as-consensus interchangeable、没索引 是不是 already excluded from consensus interchangeable、类比 CheckTx 是不是 already same as CheckTx gate interchangeable。可以跳过「看见 Code 非零就已经没进块 interchangeable / 就已经没进共识 interchangeable / 就已经和池门同一把尺 interchangeable」。不要另写怎样建索引。316 exectxresult vs consensus bundled unbundling 在本页 item 2 完成；续 [`worked-example-exectxresult-notheader-vs-bundled.md`](worked-example-exectxresult-notheader-vs-bundled.md)（不变量 709 item 3，待写）。

## 本页不抄

- 怎样编回执、怎样建索引、怎样算 LastResultsHash。
- ExecTxResult vs consensus bundled。那是不变量 316。
- 结果列表不是已经同一顺序。那是不变量 316 item 1 余量 / 707。
- Code / Data 不是已经印进本头。那是不变量 316 item 3 余量 / 709。
- 四门已经结算。那是不变量 33。
- MaxGas。那是不变量 315。
