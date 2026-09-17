# 例：看见有 /store 路径 is not already engine-used interchangeable / not already filtering interchangeable / not already settled interchangeable

**层次**：实现 / 有 /store 路径 not already engine-used / not already filtering / not already settled 正式三事（326 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Peer Filtering、Paths。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「有 /store 路径 not already engine-used / not already filtering / not already settled 正式三事（326 余量）/ not 946 peerfilter-notstore interchangeable / not 326 peerfilter-vs-query bundled interchangeable」，不是过滤 bundled（326），也不是 QueryState 已经是 ExecuteTxState（314），也不是实现了 Query 就已经是正常运转必须有（329/940）。不要另写怎样写过滤或怎样配路径。

## 官方三件事

1. **看见有 /store / /app 路径 / 看见 Query 能带路径 这份路径 is not already 已经是引擎在用 interchangeable，也不是已经过滤 bundled（326） interchangeable / 946 peerfilter-notstore interchangeable / 944 peerfilter-notaccept interchangeable / 326 peerfilter item 1 addr interchangeable，也不是已经有 /store 路径 not already engine-used / not already filtering / not already settled 正式三事 bundled（326 item 3 余量） interchangeable / 326 peerfilter item 3 interchangeable。**  
   官方写：查询对着路径走，还可以另带数据。高层路径可以有 /p2p、/store、/app。眼下 CometBFT 只用 /p2p，用来过滤邻居。看见规范写了三条路径，不是已经三条都在用 interchangeable——本页从 326 item 3 侧钉 not already engine-used 单句。326 peerfilter vs query bundled unbundling 在本页 item 3 完成。

2. **看见有 /store / 看见能带数据 / 这份路径 is not already 已经是过滤 interchangeable，也不是已经过滤 bundled（326） interchangeable / 946 peerfilter-notstore interchangeable / 326 peerfilter item 2 id 绿了 interchangeable / 945 peerfilter-notaddr interchangeable，也不是已经 QueryState 已经是 ExecuteTxState interchangeable / 314 querystate interchangeable。**  
   官方把有 /store 和已经是过滤分开——326 bundled 第三件事常与 314 混成「看见有 /store 就已经是引擎在用或已经是 ExecuteTxState interchangeable」，本页钉 not already filtering 单句。

3. **看见能带数据 / 看见有 /store / 这份路径 is not already 已经交差 interchangeable，也不是已经过滤 bundled（326） interchangeable / 946 peerfilter-notstore interchangeable / 944 peerfilter-notaccept interchangeable，也不是已经实现了 Query 就已经是正常运转必须有 interchangeable / 329/940 query-notmust interchangeable。**  
   官方把能带数据和这两道过滤已经带了数据 / 已经交差分开。看见能带数据，不是已经交差 interchangeable。326 peerfilter vs query bundled unbundling 在本页 item 3 完成。

怎样写过滤逻辑、怎样配 Cosmos-SDK Query、怎样拼 IP:端口是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **有 /store 路径 not already engine-used ≠ 已经是引擎在用 interchangeable：** 官方把可以有的高层路径和眼下只用 /p2p 分开。
- **看见有 /store not already filtering ≠ 已经是过滤 interchangeable：** 官方把有 /store 和已经是过滤分开。
- **看见能带数据 not already settled ≠ 已经交差 interchangeable：** 官方把能带数据和这两道过滤已经带了数据分开；326 peerfilter vs query bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 有 /store 路径 | 不是已经是引擎在用 | 不是 QueryState 已经是 ExecuteTxState（314） |
| 看见规范写了三条路径 | 不是已经是过滤 | 不是实现了 Query 就已经是正常运转必须有（329/940） |
| 看见能带数据 | 不是已经交差 | 不是发了 addr 就已经收下（944） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看有 /store 路径 not already engine-used / not already filtering / not already settled 正式三事（326 余量），必须分开是不是已经是引擎在用、是不是已经是过滤、是不是已经交差。可以跳过「看见有路径就已经在用」。不要另写怎样写过滤或怎样配路径。326 peerfilter vs query bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写过滤逻辑、怎样配 Cosmos-SDK Query、怎样拼 IP:端口。
- 过滤 bundled。那是不变量 326。
- 发了 addr 就已经收下。那是不变量 326 item 1 余量 / 944。
- QueryState 已经是 ExecuteTxState。那是不变量 314。
- 实现了 Query 就已经是正常运转必须有。那是不变量 329/940。
