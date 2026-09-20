# 例：看见规范写了三条路径 / 看见有 /store / 看见能带数据 is not already already all-paths-used interchangeable / already is-filter interchangeable / already filter-has-data interchangeable

**层次**：实现 / 有 /store 路径不是已经是引擎在用 not already all-paths-used / not already is-filter / not already filter-has-data 正式三事（326 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Peer Filtering、Paths。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「有 /store 路径不是已经是引擎在用 not already all-paths-used / not already is-filter / not already filter-has-data 正式三事（326 余量）/ not 736 peerfilter-notenginepath interchangeable / not 326 peerfilter bundled interchangeable」，不是 Peer Filtering bundled（326），也不是发了 addr 过滤查询不是已经收下这个人（734 item 1 余量）或 id 过滤查询绿了不是已经过了 addr（735 item 2 余量）。不要另写怎样写过滤或怎样配路径。

## 官方三件事

规范把 Requirements 里查询对着路径走、高层路径可以有 `/p2p` / `/store` / `/app`、眼下 CometBFT 只用 `/p2p` 用来过滤邻居 和「已经是规范写了三条路径就已经三条都在用 interchangeable / 已经是有 /store 就已经是过滤 interchangeable / 已经是能带数据就已经两道过滤带了数据 interchangeable / 已经是 Peer Filtering bundled interchangeable」分开写成三件独立的实现事，不是「看见有 /store 路径就已经是引擎在用 interchangeable / 就已经是过滤 interchangeable / 就已经过滤带了数据 interchangeable」一件事：

1. **看见规范写了三条路径 / 看见有 `/p2p`、`/store`、`/app` / 看见高层路径表 is not already 已经三条都在用 interchangeable / 已经 all-paths-used interchangeable / 已经引擎三条都开交差 interchangeable / 326 peerfilter bundled interchangeable / 33 four gates interchangeable / peerfilter-sold-as-connected interchangeable，也不是已经 Peer Filtering bundled（326） interchangeable / 736 peerfilter-notenginepath interchangeable / 326 peerfilter item 3 interchangeable，也不是已经有 /store 路径不是已经是引擎在用 not already all-paths-used / not already is-filter / not already filter-has-data 正式三事 bundled（326 item 3 余量） interchangeable / 326 peerfilter item 3 interchangeable，也不是已经发了 addr 不是已经收下（734） interchangeable / 735 peerfilter-notaddrpassed interchangeable / 314 querystate interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：高层路径可以有 `/p2p`、`/store`、`/app`；**眼下 CometBFT 只用 `/p2p`**。看见规范写了三条路径，不是已经 all-paths-used interchangeable——326 钉 bundled 三事，本页从 item 3 侧钉 not already all-paths-used 单句。看见有 `/p2p`、`/store`、`/app`，不是已经 Peer Filtering bundled（326） interchangeable——326 钉 bundled，本页钉 item 3 第一件事。看见高层路径表，不是已经 QueryState 已经是 ExecuteTxState（314） interchangeable——314 另钉查询状态。326 peerfilter vs query bundled unbundling 在本页 item 3 完成。

2. **看见有 /store / 看见有 `/app` / 看见路径名在表里 is not already 已经是过滤 interchangeable / 已经 is-filter interchangeable / 已经邻居过滤交差 interchangeable / 326 peerfilter bundled interchangeable / 50 banlist interchangeable，也不是已经 Peer Filtering bundled（326） interchangeable / 736 peerfilter-notenginepath interchangeable / 326 peerfilter item 1 addr interchangeable / 326 peerfilter item 2 id interchangeable，也不是已经有 /store 路径不是已经是引擎在用 not already all-paths-used / not already is-filter / not already filter-has-data 正式三事 bundled（326 item 3 余量） interchangeable / 326 peerfilter item 3 interchangeable，也不是已经三条都在用（本页第一件事） interchangeable。**  
   官方写：眼下 CometBFT 只用 `/p2p`，用来过滤邻居。看见有 /store，不是已经 is-filter interchangeable——有路径名不等于已经是过滤。看见有 `/app`，不是已经三条都在用（本页第一件事） interchangeable——三件事分开钉。看见路径名在表里，不是已经自动封禁表已经有界（50） interchangeable——50 另钉封禁表。326 peerfilter vs query bundled unbundling 在本页 item 3 完成。

3. **看见能带数据 / 看见 Query 还可以另带数据 / 看见路径外还能带数据 is not already 已经两道过滤带了数据 interchangeable / 已经 filter-has-data interchangeable / 已经 addr/id 过滤带数据交差 interchangeable / 326 peerfilter bundled interchangeable / 305 initpeer interchangeable，也不是已经 Peer Filtering bundled（326） interchangeable / 736 peerfilter-notenginepath interchangeable / 326 peerfilter item 1 / 326 peerfilter item 2，也不是已经有 /store 路径不是已经是引擎在用 not already all-paths-used / not already is-filter / not already filter-has-data 正式三事 bundled（326 item 3 余量） interchangeable / 326 peerfilter item 3 interchangeable，也不是已经三条都在用（本页第一件事） interchangeable / 已经是过滤（本页第二件事） interchangeable。**  
   官方写：查询对着路径走，还可以另带数据；两道过滤查询**没有额外数据**。看见能带数据，不是已经 filter-has-data interchangeable——一般 Query 能带数据，不等于这两道过滤已经带了数据。看见 Query 还可以另带数据，不是已经是过滤（本页第二件事） interchangeable——三件事分开钉。看见路径外还能带数据，不是已经 InitPeer 已经能交互（305） interchangeable——305 另钉 InitPeer。326 peerfilter vs query bundled unbundling 在本页 item 3 完成。

怎样写过滤逻辑、怎样配 Cosmos-SDK Query、怎样拼 IP:端口是规范里的取值或做法，本页不抄。Peer Filtering bundled（326）、发了 addr 过滤查询不是已经收下这个人（326 item 1 余量 / 734）、id 过滤查询绿了不是已经过了 addr（326 item 2 余量 / 735）、InitPeer 已经能交互（305）、自动封禁表已经有界（50）、QueryState 已经是 ExecuteTxState（314）是另外那套，本页不抄。

## 官方为什么这样拆

- **三条路径 not already all-paths-used ≠ 326 / 33 interchangeable：** 官方把可以有的高层路径和眼下只用 `/p2p` 分开。
- **有 /store not already is-filter ≠ 已经是过滤 interchangeable：** 官方把路径名在表里和已经是邻居过滤分开。
- **能带数据 not already filter-has-data ≠ 已经两道过滤带了数据 interchangeable：** 官方把一般 Query 能带数据和两道过滤没有额外数据分开；326 peerfilter vs query bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 规范写了三条路径 | 不是 already all-paths-used | 不是 QueryState alone（314） |
| 有 /store | 不是 already is-filter | 不是封禁表 alone（50） |
| 能带数据 | 不是 already filter-has-data | 不是 InitPeer alone（305） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看有 /store 路径不是已经是引擎在用 not already all-paths-used / not already is-filter / not already filter-has-data 正式三事（326 余量），必须分开规范写了三条路径 是不是 already all-paths-used interchangeable / 326 peerfilter bundled interchangeable / peerfilter-sold-as-connected interchangeable、有 /store 是不是 already is-filter interchangeable、能带数据 是不是 already filter-has-data interchangeable。可以跳过「看见有 /store 路径就已经是引擎在用 interchangeable / 就已经是过滤 interchangeable / 就已经过滤带了数据 interchangeable」。不要另写怎样写过滤。326 peerfilter vs query bundled unbundling 在本页 item 3 完成（734 + 735 + 736）。

## 本页不抄

- 怎样写过滤逻辑、怎样配 Cosmos-SDK Query、怎样拼 IP:端口。
- Peer Filtering bundled。那是不变量 326。
- 发了 addr 过滤查询不是已经收下这个人。那是不变量 326 item 1 余量 / 734。
- id 过滤查询绿了不是已经过了 addr。那是不变量 326 item 2 余量 / 735。
- InitPeer 已经能交互。那是不变量 305。
- 自动封禁表已经有界。那是不变量 50。
- QueryState 已经是 ExecuteTxState。那是不变量 314。
