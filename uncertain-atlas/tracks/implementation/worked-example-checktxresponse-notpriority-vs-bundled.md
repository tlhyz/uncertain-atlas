# 例：看见有 Priority / 排在前面 / 能优先 is not already already consensus order interchangeable / already in block interchangeable / already removed from mempool interchangeable

**层次**：实现 / Priority 不是已经是共识顺序 not already consensus order / not already in block / not already removed from mempool 正式三事（317 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Specifics of `CheckTxResponse`。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Priority 不是已经是共识顺序 not already consensus order / not already in block / not already removed from mempool 正式三事（317 余量）/ not 712 checktxresponse-notpriority interchangeable / not 317 checktxresponse bundled interchangeable」，不是 CheckTxResponse vs exec bundled（317），也不是 CheckTx Data 不是已经被引擎用了（710 item 1 余量）或各节点 Data 不一样不是已经分叉（711 item 2 余量）。不要另写怎样实现 Priority 或怎样编 Data。

## 官方三件事

规范把 Requirements 里从 v0.34.x 起 `CheckTxResponse` 有 `Priority` 字段、用来在内存池里**显式**给交易排优先好进一块提案 和「已经是有 Priority 就已经是共识顺序 interchangeable / 已经是排在前面就已经进了块 interchangeable / 已经是能优先就已经从池里删掉 interchangeable / 已经是 CheckTxResponse vs exec bundled interchangeable」分开写成三件独立的实现事，不是「看见 Priority 就已经是共识顺序 interchangeable / 就已经进了块 interchangeable / 就已经从池里删掉 interchangeable」一件事：

1. **看见有 Priority / 看见 Priority 字段 / 看见排进提案优先 is not already 已经是共识顺序 interchangeable / 已经 consensus order interchangeable / 已经进了 Agreement 顺序 interchangeable / 317 checktxresponse bundled interchangeable / 33 four gates interchangeable / checktxresponse-sold-as-exec interchangeable，也不是已经 CheckTxResponse vs exec bundled（317） interchangeable / 712 checktxresponse-notpriority interchangeable / 317 checktxresponse item 3 interchangeable，也不是已经 Priority 不是已经是共识顺序 not already consensus order / not already in block / not already removed from mempool 正式三事 bundled（317 item 3 余量） interchangeable / 317 checktxresponse item 3 interchangeable，也不是已经 CheckTx Data 不是已经被引擎用了（710） interchangeable / 711 checktxresponse-notfork interchangeable / 301 mempool interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：从 v0.34.x 起，`CheckTxResponse` 有 `Priority` 字段，用来在内存池里**显式**给交易排优先，好进一块提案。看见有 Priority，不是已经是共识顺序 interchangeable——317 钉 bundled 三事，本页从 item 3 侧钉 not already consensus order 单句。看见 Priority 字段，不是已经 CheckTxResponse vs exec bundled（317） interchangeable——317 钉 bundled，本页钉 item 3 第一件事。看见排进提案优先，不是已经 CheckTx Data 不是已经被引擎用了（710） interchangeable——710 另钉 item 1，本页钉 item 3 第一件事。317 checktxresponse vs exec bundled unbundling 在本页 item 3 启动。

2. **看见排在前面 / 看见优先排进提案 / 看见池里靠前 is not already 已经进了块 interchangeable / 已经 in block interchangeable / 已经进了决定块 interchangeable / 317 checktxresponse bundled interchangeable / 301 mempool interchangeable，也不是已经 CheckTxResponse vs exec bundled（317） interchangeable / 712 checktxresponse-notpriority interchangeable / 317 checktxresponse item 1 被引擎用 interchangeable / 317 checktxresponse item 2 分叉 interchangeable，也不是已经 Priority 不是已经是共识顺序 not already consensus order / not already in block / not already removed from mempool 正式三事 bundled（317 item 3 余量） interchangeable / 317 checktxresponse item 3 interchangeable，也不是已经是共识顺序（本页第一件事） interchangeable。**  
   官方把池里显式优先和已经进了块路径分开——排在前面，不等于已经进了块。看见排在前面，不是已经进了块 interchangeable——本页钉 not already in block 单句。看见优先排进提案，不是已经各节点 Data 不一样不是已经分叉（711） interchangeable——711 另钉 item 2，本页钉 item 3 第二件事。看见池里靠前，不是已经提案收了已经从池里删掉（301） interchangeable——301 另钉，本页钉 item 3 第二件事。317 checktxresponse vs exec bundled unbundling 在本页 item 3 启动。

3. **看见能优先 / 看见显式优先 / 看见 Priority 能排 is not already 已经从池里删掉 interchangeable / 已经 removed from mempool interchangeable / 已经出池 interchangeable / 317 checktxresponse bundled interchangeable / 301 mempool interchangeable / 33 four gates interchangeable，也不是已经 CheckTxResponse vs exec bundled（317） interchangeable / 712 checktxresponse-notpriority interchangeable / 317 checktxresponse item 1 / 317 checktxresponse item 2，也不是已经 Priority 不是已经是共识顺序 not already consensus order / not already in block / not already removed from mempool 正式三事 bundled（317 item 3 余量） interchangeable / 317 checktxresponse item 3 interchangeable，也不是已经是共识顺序（本页第一件事） interchangeable / 已经进了块（本页第二件事） interchangeable。**  
   官方把能优先和好进一块提案写成池里排序，不是已经从池里删掉——能优先，不等于已经出池。看见能优先，不是已经从池里删掉 interchangeable——本页钉 not already removed from mempool 单句。看见显式优先，不是已经是共识顺序（本页第一件事） interchangeable——三件事分开钉。看见 Priority 能排，不是已经提案收了已经从池里删掉（301） interchangeable——301 另钉交接。317 checktxresponse vs exec bundled unbundling 在本页 item 3 完成。

怎样实现 Priority、怎样给内存池排序、怎样编 Data 是规范里的取值或做法，本页不抄。CheckTxResponse vs exec bundled（317）、CheckTx Data 不是已经被引擎用了（317 item 1 余量 / 710）、各节点 Data 不一样不是已经分叉（317 item 2 余量 / 711）、内存池交接（301）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **有 Priority not already consensus order ≠ 317 / 33 interchangeable：** 官方把池里显式优先单句和已经是共识顺序路径分开。
- **排在前面 not already in block ≠ 已经进了块 interchangeable：** 官方把排优先单句和已经进块路径分开。
- **能优先 not already removed from mempool ≠ 已经从池里删掉 interchangeable：** 官方把好进提案单句和已经出池路径分开；317 checktxresponse vs exec bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 有 Priority | 不是 already consensus order | 不是被引擎用 alone（710） |
| 排在前面 | 不是 already in block | 不是各节点分叉 alone（711） |
| 能优先 | 不是 already removed from mempool | 不是提案收了出池 alone（301） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Priority 不是已经是共识顺序 not already consensus order / not already in block / not already removed from mempool 正式三事（317 余量），必须分开有 Priority 是不是 already consensus order interchangeable / 317 checktxresponse bundled interchangeable / checktxresponse-sold-as-exec interchangeable、排在前面 是不是 already in block interchangeable、能优先 是不是 already removed from mempool interchangeable。可以跳过「看见 Priority 就已经是共识顺序 interchangeable / 就已经进了块 interchangeable / 就已经从池里删掉 interchangeable」。不要另写怎样实现 Priority。317 checktxresponse vs exec bundled unbundling 在本页 item 3 完成（710 + 711 + 712）。

## 本页不抄

- 怎样实现 Priority、怎样给内存池排序、怎样编 Data。
- CheckTxResponse vs exec bundled。那是不变量 317。
- CheckTx Data 不是已经被引擎用了。那是不变量 317 item 1 余量 / 710。
- 各节点 Data 不一样不是已经分叉。那是不变量 317 item 2 余量 / 711。
- 提案收了已经从池里删掉。那是不变量 301。
- 四门已经结算。那是不变量 33。
