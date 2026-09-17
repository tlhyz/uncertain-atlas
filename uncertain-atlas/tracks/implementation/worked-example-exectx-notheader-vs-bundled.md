# 例：看见 Code / Data is not already this-header interchangeable / not already in-hash interchangeable / not already consensus interchangeable

**层次**：实现 / Code / Data not already this-header / not already in-hash / not already consensus 正式三事（316 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Transaction Results / ExecTxResult。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「Code / Data not already this-header / not already in-hash / not already consensus 正式三事（316 余量）/ not 1015 exectx-notheader interchangeable / not 316 exectxresult-vs-consensus bundled interchangeable」，不是 ExecTxResult bundled（316），也不是本头 AppHash 已经是本高度交差（147），也不是 CheckTx 的 Data 已经被引擎用了（317）。不要另写怎样编回执或怎样建索引。

## 官方三件事

1. **看见 Code / Data / 看见 Events 这份回执 is not already 已经印进本头 LastResultsHash interchangeable，也不是已经 ExecTxResult bundled（316） interchangeable / 1015 exectx-notheader interchangeable / 1013 exectx-notorder interchangeable / 316 exectx item 1 结果列表 interchangeable，也不是已经 Code / Data not already this-header / not already in-hash / not already consensus 正式三事 bundled（316 item 3 余量） interchangeable / 316 exectx item 3 interchangeable。**  
   官方写：Code 和 Data 会编进一份结构，再哈希进下一高度块头的 LastResultsHash。看见 Code / Data，不是已经印进本头 interchangeable——本页从 316 item 3 侧钉 not already this-header 单句。316 exectxresult vs consensus bundled unbundling 在本页 item 3 完成。

2. **看见 Events / 看见 Code Data / 这份回执 is not already 已经进了那份哈希 interchangeable，也不是已经 ExecTxResult bundled（316） interchangeable / 1015 exectx-notheader interchangeable / 316 exectx item 2 Code 非零 interchangeable / 1014 exectx-notout interchangeable，也不是已经本头 AppHash 已经是本高度交差 interchangeable / 147 apphash interchangeable。**  
   官方把 Events 只供建索引、以后按事件查询和已经进了那份哈希分开。看见 Events，不是已经进了那份哈希 interchangeable。本页钉 not already in-hash 单句。

3. **看见 Info / Log / 看见 Code Data / 这份回执 is not already 已经是共识 interchangeable，也不是已经 ExecTxResult bundled（316） interchangeable / 1015 exectx-notheader interchangeable / 1013 exectx-notorder interchangeable，也不是已经 CheckTx 的 Data 已经被引擎用了 interchangeable / 317 checktxresponse interchangeable。**  
   官方写：Info 和 Log 是非确定的调试字段，CometBFT 会记日志，此外忽略。看见 Info / Log，不是已经是共识 interchangeable。316 exectxresult vs consensus bundled unbundling 在本页 item 3 完成。

怎样编回执、怎样建索引、怎样算 LastResultsHash 是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **Code / Data not already this-header ≠ 已经印进本头 interchangeable：** 官方把下一高度的 LastResultsHash 和本头分开。
- **看见 Events not already in-hash ≠ 已经进了那份哈希 interchangeable：** 官方把 Events 只供建索引和已经进了那份哈希分开。
- **看见 Info / Log not already consensus ≠ 已经是共识 interchangeable：** 官方把 Info / Log 忽略和已经是共识分开；316 exectxresult vs consensus bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Code / Data 进下一头 | 不是已经印进本头 | 不是本头 AppHash 已经是本高度交差（147） |
| 看见 Events | 不是已经进了那份哈希 | 不是 CheckTx 的 Data 已经被引擎用了（317） |
| 看见 Info / Log | 不是已经是共识 | 不是结果列表就已经同一顺序（1013） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Code / Data not already this-header / not already in-hash / not already consensus 正式三事（316 余量），必须分开是不是已经印进本头、是不是已经进了那份哈希、是不是已经是共识。可以跳过「看见回了就已经对上顺序」。不要另写怎样编回执或怎样建索引。316 exectxresult vs consensus bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样编回执、怎样建索引、怎样算 LastResultsHash。
- ExecTxResult bundled。那是不变量 316。
- 本头 AppHash 已经是本高度交差。那是不变量 147。
- CheckTx 的 Data 已经被引擎用了。那是不变量 317。
