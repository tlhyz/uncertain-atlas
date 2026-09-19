# 例：看见 Code Data / Events / Info Log is not already already in this header interchangeable / already in LastResultsHash interchangeable / already consensus field interchangeable

**层次**：实现 / Code Data 不是已经印进本头 not already in this header / not already in LastResultsHash / not already consensus field 正式三事（316 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Transaction Results / Specifics of `ExecTxResult`。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Code Data 不是已经印进本头 not already in this header / not already in LastResultsHash / not already consensus field 正式三事（316 余量）/ not 709 exectxresult-notheader interchangeable / not 316 exectxresult bundled interchangeable」，不是 ExecTxResult vs consensus bundled（316），也不是结果列表不是已经同一顺序（707 item 1 余量）或 Code 非零不是已经没进块（708 item 2 余量）。不要另写怎样编回执或怎样算 LastResultsHash。

## 官方三件事

规范把 Requirements 里 `Code` 和 `Data` 会编进一份结构、再哈希进**下一高度**块头的 `LastResultsHash`、`Events` 只供建索引以后按事件查询、`Info` 和 `Log` 是非确定的调试字段、CometBFT 会记日志**此外忽略** 和「已经是 Code / Data 就已经印进本头 interchangeable / 已经是 Events 就已经进了那份哈希 interchangeable / 已经是 Info / Log 就已经是共识字段 interchangeable / 已经是 ExecTxResult vs consensus bundled interchangeable」分开写成三件独立的实现事，不是「看见 Code / Data 就已经印进本头 interchangeable / 就已经进了那份哈希 interchangeable / 就已经是共识 interchangeable」一件事：

1. **看见 Code / Data / 看见回了 Code 和 Data is not already 已经印进本头 interchangeable / 已经 in this header interchangeable / 已经进本头 LastResultsHash interchangeable / 316 exectxresult bundled interchangeable / 147 apphash interchangeable / exectxresult-sold-as-consensus interchangeable，也不是已经 ExecTxResult vs consensus bundled（316） interchangeable / 709 exectxresult-notheader interchangeable / 316 exectxresult item 3 interchangeable，也不是已经 Code Data 不是已经印进本头 not already in this header / not already in LastResultsHash / not already consensus field 正式三事 bundled（316 item 3 余量） interchangeable / 316 exectxresult item 3 interchangeable，也不是已经结果列表不是已经同一顺序（707） interchangeable / 708 exectxresult-notexcluded interchangeable / 33 four gates interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：`Code` 和 `Data` 会编进一份结构，再哈希进**下一高度**块头的 `LastResultsHash`。看见 Code / Data，不是已经印进本头 interchangeable——316 钉 bundled 三事，本页从 item 3 侧钉 not already in this header 单句。看见回了 Code 和 Data，不是已经 ExecTxResult vs consensus bundled（316） interchangeable——316 钉 bundled，本页钉 item 3 第一件事。看见 Code / Data，不是已经本头 AppHash 已经是本高度交差（147） interchangeable——147 另钉，本页钉下一高度 LastResultsHash 边界。316 exectxresult vs consensus bundled unbundling 在本页 item 3 启动。

2. **看见 Events / 看见执行里产出了事件 / 看见按事件查询 is not already 已经进了那份哈希 interchangeable / 已经 in LastResultsHash interchangeable / 已经编进 LastResultsHash interchangeable / 316 exectxresult bundled interchangeable / 147 apphash interchangeable，也不是已经 ExecTxResult vs consensus bundled（316） interchangeable / 709 exectxresult-notheader interchangeable / 316 exectxresult item 1 顺序 interchangeable / 316 exectxresult item 2 Code 非零 interchangeable，也不是已经 Code Data 不是已经印进本头 not already in this header / not already in LastResultsHash / not already consensus field 正式三事 bundled（316 item 3 余量） interchangeable / 316 exectxresult item 3 interchangeable，也不是已经印进本头（本页第一件事） interchangeable。**  
   官方把 Events 只供建索引、以后按事件查询和已经进了那份哈希路径分开——Events，不等于已经编进 LastResultsHash。看见 Events，不是已经进了那份哈希 interchangeable——本页钉 not already in LastResultsHash 单句。看见执行里产出了事件，不是已经结果列表不是已经同一顺序（707） interchangeable——707 另钉 item 1，本页钉 item 3 第二件事。看见按事件查询，不是已经 Code 非零不是已经没进块（708） interchangeable——708 另钉 item 2，本页钉 item 3 第二件事。316 exectxresult vs consensus bundled unbundling 在本页 item 3 启动。

3. **看见 Info / Log / 看见调试字段 / 看见非确定调试字段 is not already 已经是共识字段 interchangeable / 已经 consensus field interchangeable / 已经进共识 interchangeable / 316 exectxresult bundled interchangeable / 33 four gates interchangeable，也不是已经 ExecTxResult vs consensus bundled（316） interchangeable / 709 exectxresult-notheader interchangeable / 316 exectxresult item 1 / 316 exectxresult item 2，也不是已经 Code Data 不是已经印进本头 not already in this header / not already in LastResultsHash / not already consensus field 正式三事 bundled（316 item 3 余量） interchangeable / 316 exectxresult item 3 interchangeable，也不是已经印进本头（本页第一件事） interchangeable / 已经进了那份哈希（本页第二件事） interchangeable。**  
   官方写：`Info` 和 `Log` 是非确定的调试字段，CometBFT 会记日志，**此外忽略**。看见 Info / Log，不是已经是共识字段 interchangeable——本页钉 not already consensus field 单句。看见调试字段，不是已经印进本头（本页第一件事） interchangeable——三件事分开钉。看见非确定调试字段，不是已经四门已经结算（33） interchangeable——33 另钉。316 exectxresult vs consensus bundled unbundling 在本页 item 3 完成。

怎样编回执、怎样建索引、怎样算 LastResultsHash 是规范里的取值或做法，本页不抄。ExecTxResult vs consensus bundled（316）、结果列表不是已经同一顺序（316 item 1 余量 / 707）、Code 非零不是已经没进块（316 item 2 余量 / 708）、本头 AppHash（147）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **Code / Data not already in this header ≠ 316 / 147 interchangeable：** 官方把下一高度 LastResultsHash 单句和已经印进本头路径分开。
- **Events not already in LastResultsHash ≠ 已经进了那份哈希 interchangeable：** 官方把只供建索引单句和已经编进哈希路径分开。
- **Info / Log not already consensus field ≠ 已经是共识字段 interchangeable：** 官方把此外忽略单句和已经是共识路径分开；316 exectxresult vs consensus bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Code / Data | 不是 already in this header | 不是同一顺序 alone（707） |
| Events | 不是 already in LastResultsHash | 不是没进块 alone（708） |
| Info / Log | 不是 already consensus field | 不是本头 AppHash alone（147） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Code Data 不是已经印进本头 not already in this header / not already in LastResultsHash / not already consensus field 正式三事（316 余量），必须分开 Code / Data 是不是 already in this header interchangeable / 316 exectxresult bundled interchangeable / 147 apphash interchangeable、Events 是不是 already in LastResultsHash interchangeable、Info / Log 是不是 already consensus field interchangeable。可以跳过「看见 Code / Data 就已经印进本头 interchangeable / 就已经进了那份哈希 interchangeable / 就已经是共识 interchangeable」。不要另写怎样算 LastResultsHash。316 exectxresult vs consensus bundled unbundling 在本页 item 3 完成（707 + 708 + 709）。

## 本页不抄

- 怎样编回执、怎样建索引、怎样算 LastResultsHash。
- ExecTxResult vs consensus bundled。那是不变量 316。
- 结果列表不是已经同一顺序。那是不变量 316 item 1 余量 / 707。
- Code 非零不是已经没进块。那是不变量 316 item 2 余量 / 708。
- 本头 AppHash 已经是本高度交差。那是不变量 147。
- 四门已经结算。那是不变量 33。
