# 例：看见回了字节 / 字段名也叫 Data / 看见有结果 is not already already used by engine interchangeable / already ExecTxResult.Data interchangeable / already in LastResultsHash interchangeable

**层次**：实现 / CheckTx Data 不是已经被引擎用了 not already used by engine / not already ExecTxResult.Data / not already in LastResultsHash 正式三事（317 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Specifics of `CheckTxResponse`。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「CheckTx Data 不是已经被引擎用了 not already used by engine / not already ExecTxResult.Data / not already in LastResultsHash 正式三事（317 余量）/ not 710 checktxresponse-notused interchangeable / not 317 checktxresponse bundled interchangeable」，不是 CheckTxResponse vs exec bundled（317），也不是各节点 Data 不一样不是已经分叉（711 item 2 余量）或 Priority 不是已经是共识顺序（712 item 3 余量）。不要另写怎样实现 Priority 或怎样编 Data。

## 官方三件事

规范把 Requirements 里 `CheckTxResponse.Data` 装着 CheckTx 执行的结果（如果有）、**CometBFT 忽略**这份值、字段名也叫 Data 不是已经和 Finalize 那份同一把尺、看见有结果不是已经进了下一头的 `LastResultsHash` 和「已经是回了字节就已经被引擎用了 interchangeable / 已经是字段名也叫 Data 就已经是 ExecTxResult.Data interchangeable / 已经是有结果就已经进了 LastResultsHash interchangeable / 已经是 CheckTxResponse vs exec bundled interchangeable」分开写成三件独立的实现事，不是「看见回了 Data 就已经被引擎用了 interchangeable / 就已经是 Finalize Data interchangeable / 就已经进了下一头 interchangeable」一件事：

1. **看见回了字节 / 看见 CheckTxResponse.Data / 看见回了结果字节 is not already 已经被引擎用了 interchangeable / 已经 used by engine interchangeable / 已经进了引擎路径 interchangeable / 317 checktxresponse bundled interchangeable / 33 four gates interchangeable / checktxresponse-sold-as-exec interchangeable，也不是已经 CheckTxResponse vs exec bundled（317） interchangeable / 710 checktxresponse-notused interchangeable / 317 checktxresponse item 1 interchangeable，也不是已经 CheckTx Data 不是已经被引擎用了 not already used by engine / not already ExecTxResult.Data / not already in LastResultsHash 正式三事 bundled（317 item 1 余量） interchangeable / 317 checktxresponse item 1 interchangeable，也不是已经各节点 Data 不一样不是已经分叉（711） interchangeable / 712 checktxresponse-notpriority interchangeable / 316 exectxresult interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：`Data` 装着 CheckTx 执行的结果（如果有）。**CometBFT 忽略** `CheckTxResponse` 里这个值。看见回了字节，不是已经被引擎用了 interchangeable——317 钉 bundled 三事，本页从 item 1 侧钉 not already used by engine 单句。看见 CheckTxResponse.Data，不是已经 CheckTxResponse vs exec bundled（317） interchangeable——317 钉 bundled，本页钉 item 1 第一件事。看见回了结果字节，不是已经各节点 Data 不一样不是已经分叉（711） interchangeable——711 另钉 item 2，本页钉 item 1 第一件事。317 checktxresponse vs exec bundled unbundling 在本页 item 1 启动。

2. **看见字段名也叫 Data / 看见也叫 Data / 看见和 Finalize 同名 is not already 已经是 ExecTxResult.Data interchangeable / 已经和 Finalize 那份同一把尺 interchangeable / 已经 same as Finalize Data interchangeable / 317 checktxresponse bundled interchangeable / 316 exectxresult interchangeable，也不是已经 CheckTxResponse vs exec bundled（317） interchangeable / 710 checktxresponse-notused interchangeable / 317 checktxresponse item 2 分叉 interchangeable / 317 checktxresponse item 3 Priority interchangeable，也不是已经 CheckTx Data 不是已经被引擎用了 not already used by engine / not already ExecTxResult.Data / not already in LastResultsHash 正式三事 bundled（317 item 1 余量） interchangeable / 317 checktxresponse item 1 interchangeable，也不是已经被引擎用了（本页第一件事） interchangeable。**  
   官方把字段名也叫 Data 和已经是 ExecTxResult.Data 路径分开——字段名一样，不等于已经和 Finalize 那份同一把尺。看见字段名也叫 Data，不是已经是 ExecTxResult.Data interchangeable——本页钉 not already ExecTxResult.Data 单句。看见也叫 Data，不是已经 Priority 不是已经是共识顺序（712） interchangeable——712 另钉 item 3，本页钉 item 1 第二件事。看见和 Finalize 同名，不是已经 ExecTxResult vs consensus bundled（316） interchangeable——316 另钉，本页钉 item 1 第二件事。317 checktxresponse vs exec bundled unbundling 在本页 item 1 启动。

3. **看见有结果 / 看见 CheckTx 回了结果 / 看见有结果字节 is not already 已经进了下一头的 LastResultsHash interchangeable / 已经 in LastResultsHash interchangeable / 已经印进下一头 interchangeable / 317 checktxresponse bundled interchangeable / 316 exectxresult interchangeable / 709 exectxresult-notheader interchangeable，也不是已经 CheckTxResponse vs exec bundled（317） interchangeable / 710 checktxresponse-notused interchangeable / 317 checktxresponse item 2 / 317 checktxresponse item 3，也不是已经 CheckTx Data 不是已经被引擎用了 not already used by engine / not already ExecTxResult.Data / not already in LastResultsHash 正式三事 bundled（317 item 1 余量） interchangeable / 317 checktxresponse item 1 interchangeable，也不是已经被引擎用了（本页第一件事） interchangeable / 已经是 ExecTxResult.Data（本页第二件事） interchangeable。**  
   官方把看见有结果和已经进了下一头的 `LastResultsHash` 路径分开——有结果，不等于已经进了那份哈希。看见有结果，不是已经进了 LastResultsHash interchangeable——本页钉 not already in LastResultsHash 单句。看见 CheckTx 回了结果，不是已经被引擎用了（本页第一件事） interchangeable——三件事分开钉。看见有结果字节，不是已经 Code / Data 不是已经印进本头（709） interchangeable——709 另钉 Finalize 侧。317 checktxresponse vs exec bundled unbundling 在本页 item 1 完成。

怎样实现 Priority、怎样给内存池排序、怎样编 Data 是规范里的取值或做法，本页不抄。CheckTxResponse vs exec bundled（317）、各节点 Data 不一样不是已经分叉（317 item 2 余量 / 711）、Priority 不是已经是共识顺序（317 item 3 余量 / 712）、ExecTxResult vs consensus（316）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **回了字节 not already used by engine ≠ 317 / 33 interchangeable：** 官方把 CometBFT 忽略单句和已经被引擎用了路径分开。
- **字段名也叫 Data not already ExecTxResult.Data ≠ 已经和 Finalize 同一把尺 interchangeable：** 官方把同名单句和已经是 Finalize Data 路径分开。
- **有结果 not already in LastResultsHash ≠ 已经进了下一头 interchangeable：** 官方把有结果单句和已经进了 LastResultsHash 路径分开；317 checktxresponse vs exec bundled unbundling 在本页 item 1 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 回了字节 | 不是 already used by engine | 不是各节点分叉 alone（711） |
| 字段名也叫 Data | 不是 already ExecTxResult.Data | 不是 Priority 共识 alone（712） |
| 有结果 | 不是 already in LastResultsHash | 不是 Finalize 印本头 alone（316 / 709） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Data 不是已经被引擎用了 not already used by engine / not already ExecTxResult.Data / not already in LastResultsHash 正式三事（317 余量），必须分开回了字节 是不是 already used by engine interchangeable / 317 checktxresponse bundled interchangeable / checktxresponse-sold-as-exec interchangeable、字段名也叫 Data 是不是 already ExecTxResult.Data interchangeable、有结果 是不是 already in LastResultsHash interchangeable。可以跳过「看见回了就已经被引擎用了 interchangeable / 就已经是 Finalize Data interchangeable / 就已经进了下一头 interchangeable」。不要另写怎样编 Data。317 checktxresponse vs exec bundled unbundling 在本页 item 1 完成；续 [`worked-example-checktxresponse-notfork-vs-bundled.md`](worked-example-checktxresponse-notfork-vs-bundled.md)（不变量 711 item 2，待写）。

## 本页不抄

- 怎样实现 Priority、怎样给内存池排序、怎样编 Data。
- CheckTxResponse vs exec bundled。那是不变量 317。
- 各节点 Data 不一样不是已经分叉。那是不变量 317 item 2 余量 / 711。
- Priority 不是已经是共识顺序。那是不变量 317 item 3 余量 / 712。
- ExecTxResult vs consensus / Code Data 印本头。那是不变量 316 / 709。
- 四门已经结算。那是不变量 33。
