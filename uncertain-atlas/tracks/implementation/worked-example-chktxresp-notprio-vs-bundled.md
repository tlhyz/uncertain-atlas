# 例：看见 Priority is not already consensus-order interchangeable / not already in-block interchangeable / not already deleted interchangeable

**层次**：实现 / Priority not already consensus-order / not already in-block / not already deleted 正式三事（317 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Specifics of CheckTxResponse。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「Priority not already consensus-order / not already in-block / not already deleted 正式三事（317 余量）/ not 1018 chktxresp-notprio interchangeable / not 317 checktxresponse-vs-exec bundled interchangeable」，不是 CheckTxResponse bundled（317），也不是提案收了已经从池里删掉（301/992），也不是单笔 CheckTx 绿已经整包可提案（69）。不要另写怎样实现 Priority 或怎样编 Data。

## 官方三件事

1. **看见 Priority / 看见排进提案优先 这份回执 is not already 已经是共识顺序 interchangeable，也不是已经 CheckTxResponse bundled（317） interchangeable / 1018 chktxresp-notprio interchangeable / 1016 chktxresp-notused interchangeable / 317 checktx item 1 Data interchangeable，也不是已经 Priority not already consensus-order / not already in-block / not already deleted 正式三事 bundled（317 item 3 余量） interchangeable / 317 checktx item 3 interchangeable。**  
   官方写：从 v0.34.x 起，CheckTxResponse 有 Priority 字段，用来在内存池里显式给交易排优先，好进一块提案。看见有 Priority，不是已经是共识顺序 interchangeable——本页从 317 item 3 侧钉 not already consensus-order 单句。317 checktxresponse vs exec bundled unbundling 在本页 item 3 完成。

2. **看见排在前面 / 看见 Priority / 这份回执 is not already 已经进了块 interchangeable，也不是已经 CheckTxResponse bundled（317） interchangeable / 1018 chktxresp-notprio interchangeable / 317 checktx item 2 Data 不确定 interchangeable / 1017 chktxresp-notfork interchangeable，也不是已经提案收了已经从池里删掉 interchangeable / 301/992 proposed-notdel interchangeable。**  
   官方把排在前面和已经进了块分开。看见排在前面，不是已经进了块 interchangeable。本页钉 not already in-block 单句。

3. **看见能优先 / 看见 Priority / 这份回执 is not already 已经从池里删掉 interchangeable，也不是已经 CheckTxResponse bundled（317） interchangeable / 1018 chktxresp-notprio interchangeable / 1016 chktxresp-notused interchangeable，也不是已经单笔 CheckTx 绿已经整包可提案 interchangeable / 69 package interchangeable。**  
   官方把能优先和已经从池里删掉分开。看见能优先，不是已经从池里删掉 interchangeable。317 checktxresponse vs exec bundled unbundling 在本页 item 3 完成。

怎样实现 Priority、怎样给内存池排序、怎样编 Data 是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **Priority not already consensus-order ≠ 已经是共识顺序 interchangeable：** 官方把池里显式优先和已经进块分开。
- **看见排在前面 not already in-block ≠ 已经进了块 interchangeable：** 官方把排在前面和已经进了块分开。
- **看见能优先 not already deleted ≠ 已经从池里删掉 interchangeable：** 官方把能优先和已经从池里删掉分开；317 checktxresponse vs exec bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Priority | 不是已经是共识顺序 | 不是提案收了已经从池里删掉（301/992） |
| 看见排在前面 | 不是已经进了块 | 不是单笔 CheckTx 绿已经整包可提案（69） |
| 看见能优先 | 不是已经从池里删掉 | 不是 CheckTx 的 Data 已经被引擎用了（1016） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Priority not already consensus-order / not already in-block / not already deleted 正式三事（317 余量），必须分开是不是已经是共识顺序、是不是已经进了块、是不是已经从池里删掉。可以跳过「看见回了就已经被引擎用了」。不要另写怎样实现 Priority 或怎样编 Data。317 checktxresponse vs exec bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样实现 Priority、怎样给内存池排序、怎样编 Data。
- CheckTxResponse bundled。那是不变量 317。
- 提案收了已经从池里删掉。那是不变量 301/992。
- 单笔 CheckTx 绿已经整包可提案。那是不变量 69。
