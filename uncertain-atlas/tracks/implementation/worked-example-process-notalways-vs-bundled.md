# 例：看见进了这一轮 / 看见叫了 Process / 看见失败了 is not already already every-round interchangeable / already this-prepare interchangeable / already crossed interchangeable

**层次**：实现 / 失败时可能对上更早一次或根本不调不是已经每轮都会叫 not already every-round / not already this-prepare / not already crossed 正式三事（351 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「失败时可能对上更早一次或根本不调不是已经每轮都会叫 not already every-round / not already this-prepare / not already crossed 正式三事（351 余量）/ not 808 process-notalways interchangeable / not 351 processalso bundled interchangeable」，不是 Process 也会在提议者那边叫 bundled（351），也不是 Process 也会在提议者那边叫不是已经不用再 Process（806 item 1 余量）或通常紧跟 Prepare、列表对得上不是已经保证是这一次（807 item 2 余量）。不要另写怎样写 Process。

## 官方三件事

规范把 Methods 里失败时不保证、`ProcessProposalRequest` 可能对上更早一次 Prepare 的回包或根本不调 Process 和「已经是进了这一轮就已经每轮都会叫 interchangeable / 已经是叫了 Process 就已经是这一次刚回的那份 interchangeable / 已经是失败了就已经交差 interchangeable / 已经是 processalso bundled interchangeable」分开写成三件独立的实现事，不是「看见进了这一轮就已经每轮都会叫 interchangeable / 就已经是这一次刚回的那份 interchangeable / 就已经交差 interchangeable」一件事：

1. **看见进了这一轮 / 看见失败时可能对上更早一次或根本不调 / 看见失败时不保证 is not already 已经每轮都会叫 Process interchangeable / 已经 every-round interchangeable / 已经每轮都会叫交差 interchangeable / 351 processalso bundled interchangeable / 33 fourgates interchangeable / processalso-sold-as-matched interchangeable，也不是已经 Process 也会在提议者那边叫 bundled（351） interchangeable / 808 process-notalways interchangeable / 351 processalso item 3 interchangeable，也不是已经失败时可能对上更早一次或根本不调不是已经每轮都会叫 not already every-round / not already this-prepare / not already crossed 正式三事 bundled（351 item 3 余量） interchangeable / 351 processalso item 3 interchangeable，也不是已经不用再 Process（806） interchangeable / 807 process-notguaranteed interchangeable / 311 candidate interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：失败时不保证。看见进了这一轮，不是已经会叫。看见失败时可能对上更早一次或根本不调，不是已经 every-round interchangeable——351 钉 bundled 三事，本页从 item 3 侧钉 not already every-round 单句。看见失败时不保证，不是已经 Process 也会在提议者那边叫 bundled（351） interchangeable——351 钉 bundled，本页钉 item 3 第一件事。看见进了这一轮，不是已经不用再 Process（806） interchangeable——806 另钉 item 1。看见进了这一轮，不是已经通常对得上（807） interchangeable——807 另钉 item 2。351 processalso vs prepare bundled unbundling 在本页 item 3 完成。

2. **看见叫了 Process / 看见 `ProcessProposalRequest` 可能对上更早一次 Prepare 的回包 / 看见对上更早一次 is not already 已经是这一次刚回的那份 interchangeable / 已经 this-prepare interchangeable / 已经是这一次交差 interchangeable / 351 processalso bundled interchangeable / 347 req3coherence interchangeable，也不是已经 Process 也会在提议者那边叫 bundled（351） interchangeable / 808 process-notalways interchangeable / 351 processalso item 1 跳过 interchangeable / 351 processalso item 2 对得上 interchangeable，也不是已经失败时可能对上更早一次或根本不调不是已经每轮都会叫 not already every-round / not already this-prepare / not already crossed 正式三事 bundled（351 item 3 余量） interchangeable / 351 processalso item 3 interchangeable，也不是已经每轮都会叫（本页第一件事） interchangeable。**  
   官方写：`ProcessProposalRequest` 可能对上更早一次 Prepare 的回包。看见叫了 Process，不是已经是这一次刚回的那份。看见对上更早一次，不是已经 this-prepare interchangeable——本页钉 not already this-prepare 单句。看见可能对上更早一次，不是已经每轮都会叫（本页第一件事） interchangeable——三件事分开钉。351 processalso vs prepare bundled unbundling 在本页 item 3 完成。

3. **看见失败了 / 看见根本不调 Process / 看见不调 is not already 已经交差 interchangeable / 已经 crossed interchangeable / 已经交差交差 interchangeable / 351 processalso bundled interchangeable / 311 candidate interchangeable，也不是已经 Process 也会在提议者那边叫 bundled（351） interchangeable / 808 process-notalways interchangeable / 351 processalso item 1 / 351 processalso item 2，也不是已经失败时可能对上更早一次或根本不调不是已经每轮都会叫 not already every-round / not already this-prepare / not already crossed 正式三事 bundled（351 item 3 余量） interchangeable / 351 processalso item 3 interchangeable，也不是已经每轮都会叫（本页第一件事） interchangeable / 已经是这一次刚回的那份（本页第二件事） interchangeable。**  
   官方写：或者根本不调 Process。看见失败了，不是已经交差。看见根本不调，不是已经 crossed interchangeable——本页钉 not already crossed 单句。看见不调，不是已经是这一次刚回的那份（本页第二件事） interchangeable——三件事分开钉。351 processalso vs prepare bundled unbundling 在本页 item 3 完成。

怎样写 `ProcessProposal`、怎样缓存候选、怎样测失败路径是规范里的做法，本页不抄。Process 也会在提议者那边叫 bundled（351）、Process 也会在提议者那边叫不是已经不用再 Process（351 item 1 余量 / 806）、通常紧跟 Prepare、列表对得上不是已经保证是这一次（351 item 2 余量 / 807）、四门已经结算（33）、正确提议者的准备提案必须被正确接收者 Accept（347）、候选已经是 ExecuteTxState（311）是另外那套，本页不抄。

## 官方为什么这样拆

- **进了这一轮 / 失败时可能对上更早一次或根本不调 not already every-round ≠ 351 / 33 interchangeable：** 官方把失败时不保证和已经每轮都会叫分开。
- **叫了 Process / 可能对上更早一次 not already this-prepare ≠ 已经是这一次刚回的那份 interchangeable：** 官方把叫了 Process 和已经是这一次刚回的那份分开。
- **失败了 / 根本不调 not already crossed ≠ 已经交差 interchangeable：** 官方把失败了和已经交差分开；351 processalso vs prepare bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 进了这一轮 / 失败时可能对上更早一次或根本不调 | 不是 already every-round | 不是四门已经结算 alone（33） |
| 叫了 Process / 可能对上更早一次 | 不是 already this-prepare | 不是通常对得上 already guaranteed-this alone（807） |
| 失败了 / 根本不调 | 不是 already crossed | 不是不用再 Process already skip alone（806） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看失败时可能对上更早一次或根本不调不是已经每轮都会叫 not already every-round / not already this-prepare / not already crossed 正式三事（351 余量），必须分开进了这一轮 / 失败时可能对上更早一次或根本不调 是不是 already every-round interchangeable / 351 processalso bundled interchangeable / processalso-sold-as-matched interchangeable、叫了 Process / 可能对上更早一次 是不是 already this-prepare interchangeable、失败了 / 根本不调 是不是 already crossed interchangeable。可以跳过「看见进了这一轮就已经每轮都会叫 interchangeable / 就已经是这一次刚回的那份 interchangeable / 就已经交差 interchangeable」。不要另写怎样写 Process。351 processalso vs prepare bundled unbundling 在本页 item 3 完成（806 + 807 + 808）。

## 本页不抄

- 怎样写 `ProcessProposal`、怎样缓存候选、怎样测失败路径。
- Process 也会在提议者那边叫 bundled。那是不变量 351。
- Process 也会在提议者那边叫不是已经不用再 Process。那是不变量 351 item 1 余量 / 806。
- 通常紧跟 Prepare、列表对得上不是已经保证是这一次。那是不变量 351 item 2 余量 / 807。
- 四门已经结算。那是不变量 33。
- 正确提议者的准备提案必须被正确接收者 Accept。那是不变量 347。
- 候选已经是 ExecuteTxState。那是不变量 311。
