# 例：看见发了 addr / 看见 TCP 已经连上 / 看见只问了地址 is not already already accepted interchangeable / already query-passed interchangeable / already id-asked interchangeable

**层次**：实现 / 发了 addr 过滤查询不是已经收下这个人 not already accepted / not already query-passed / not already id-asked 正式三事（326 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Peer Filtering、Paths。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「发了 addr 过滤查询不是已经收下这个人 not already accepted / not already query-passed / not already id-asked 正式三事（326 余量）/ not 734 peerfilter-notaccepted interchangeable / not 326 peerfilter bundled interchangeable」，不是 Peer Filtering bundled（326），也不是 id 过滤查询绿了不是已经过了 addr（735 item 2 余量）或有 /store 路径不是已经是引擎在用（736 item 3 余量）。不要另写怎样写过滤或怎样配路径。

## 官方三件事

规范把 Requirements 里 CometBFT 连上一个人时用 Query 发两道查询、第一道是 `/p2p/filter/addr/`、没有额外数据 和「已经是发了 addr 就已经收下这个人 interchangeable / 已经是 TCP 连上就已经过了 Query interchangeable / 已经是只问了地址就已经问了 id interchangeable / 已经是 Peer Filtering bundled interchangeable」分开写成三件独立的实现事，不是「看见发了 addr 过滤查询就已经收下 interchangeable / 就已经过了 Query interchangeable / 就已经问了 id interchangeable」一件事：

1. **看见发了 addr / 看见发了 `/p2p/filter/addr` / 看见问了 IP 和端口 is not already 已经收下这个人 interchangeable / 已经 accepted interchangeable / 已经收下交差 interchangeable / 326 peerfilter bundled interchangeable / 33 four gates interchangeable / peerfilter-sold-as-connected interchangeable，也不是已经 Peer Filtering bundled（326） interchangeable / 734 peerfilter-notaccepted interchangeable / 326 peerfilter item 1 interchangeable，也不是已经发了 addr 过滤查询不是已经收下这个人 not already accepted / not already query-passed / not already id-asked 正式三事 bundled（326 item 1 余量） interchangeable / 326 peerfilter item 1 interchangeable，也不是已经 id 过滤查询绿了不是已经过了 addr（735） interchangeable / 736 peerfilter-notenginepath interchangeable / 305 initpeer interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：CometBFT 连上一个人时，会用 Query 发**两道**查询；第一道是 `/p2p/filter/addr/`，后面跟这个连接的 IP 和端口。看见发了 addr，不是已经 accepted interchangeable——326 钉 bundled 三事，本页从 item 1 侧钉 not already accepted 单句。看见发了 `/p2p/filter/addr`，不是已经 Peer Filtering bundled（326） interchangeable——326 钉 bundled，本页钉 item 1 第一件事。看见问了 IP 和端口，不是已经 InitPeer 已经能交互（305） interchangeable——305 另钉 InitPeer。326 peerfilter vs query bundled unbundling 在本页 item 1 启动。

2. **看见 TCP 已经连上 / 看见连上了一个人 / 看见 TCP 通了 is not already 已经过了 Query interchangeable / 已经 query-passed interchangeable / 已经两道 Query 交差 interchangeable / 326 peerfilter bundled interchangeable / 50 banlist interchangeable，也不是已经 Peer Filtering bundled（326） interchangeable / 734 peerfilter-notaccepted interchangeable / 326 peerfilter item 2 id 绿了 interchangeable / 326 peerfilter item 3 路径 interchangeable，也不是已经发了 addr 过滤查询不是已经收下这个人 not already accepted / not already query-passed / not already id-asked 正式三事 bundled（326 item 1 余量） interchangeable / 326 peerfilter item 1 interchangeable，也不是已经收下（本页第一件事） interchangeable。**  
   官方把 TCP 连上和用 Query 发两道查询分开——TCP 通了，不等于已经过了 Query。看见 TCP 已经连上，不是已经 query-passed interchangeable——本页钉 not already query-passed 单句。看见连上了一个人，不是已经收下（本页第一件事） interchangeable——三件事分开钉。看见 TCP 通了，不是已经自动封禁表已经有界（50） interchangeable——50 另钉封禁表。326 peerfilter vs query bundled unbundling 在本页 item 1 启动。

3. **看见只问了地址 / 看见第一道是 addr / 看见没有问 id is not already 已经问了 id interchangeable / 已经 id-asked interchangeable / 已经两道都问过交差 interchangeable / 326 peerfilter bundled interchangeable / 314 querystate interchangeable，也不是已经 Peer Filtering bundled（326） interchangeable / 734 peerfilter-notaccepted interchangeable / 326 peerfilter item 2 / 326 peerfilter item 3，也不是已经发了 addr 过滤查询不是已经收下这个人 not already accepted / not already query-passed / not already id-asked 正式三事 bundled（326 item 1 余量） interchangeable / 326 peerfilter item 1 interchangeable，也不是已经收下（本页第一件事） interchangeable / 已经过了 Query（本页第二件事） interchangeable。**  
   官方写：两道查询**没有额外数据**；第一道只问地址。看见只问了地址，不是已经 id-asked interchangeable——本页钉 not already id-asked 单句。看见第一道是 addr，不是已经收下（本页第一件事） interchangeable——三件事分开钉。看见没有问 id，不是已经 QueryState 已经是 ExecuteTxState（314） interchangeable——314 另钉查询状态。326 peerfilter vs query bundled unbundling 在本页 item 1 完成。

怎样写过滤逻辑、怎样配 Cosmos-SDK Query、怎样拼 IP:端口是规范里的取值或做法，本页不抄。Peer Filtering bundled（326）、id 过滤查询绿了不是已经过了 addr（326 item 2 余量 / 735）、有 /store 路径不是已经是引擎在用（326 item 3 余量 / 736）、InitPeer 已经能交互（305）、自动封禁表已经有界（50）、QueryState 已经是 ExecuteTxState（314）是另外那套，本页不抄。

## 官方为什么这样拆

- **发了 addr not already accepted ≠ 326 / 33 interchangeable：** 官方把发了 addr 查询和已经收下这个人分开。
- **TCP 连上 not already query-passed ≠ 已经过了 Query interchangeable：** 官方把 TCP 连上和两道 Query 分开。
- **只问了地址 not already id-asked ≠ 已经问了 id interchangeable：** 官方把第一道 addr 和第二道 id 分开；326 peerfilter vs query bundled unbundling 在本页 item 1 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 发了 addr | 不是 already accepted | 不是 InitPeer alone（305） |
| TCP 连上 | 不是 already query-passed | 不是封禁表 alone（50） |
| 只问了地址 | 不是 already id-asked | 不是 QueryState alone（314） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看发了 addr 过滤查询不是已经收下这个人 not already accepted / not already query-passed / not already id-asked 正式三事（326 余量），必须分开发了 addr 是不是 already accepted interchangeable / 326 peerfilter bundled interchangeable / peerfilter-sold-as-connected interchangeable、TCP 连上 是不是 already query-passed interchangeable、只问了地址 是不是 already id-asked interchangeable。可以跳过「看见发了 addr 过滤查询就已经收下 interchangeable / 就已经过了 Query interchangeable / 就已经问了 id interchangeable」。不要另写怎样写过滤。326 peerfilter vs query bundled unbundling 在本页 item 1 启动；续 [`worked-example-peerfilter-notaddrpassed-vs-bundled.md`](worked-example-peerfilter-notaddrpassed-vs-bundled.md)（不变量 735 item 2）已写。

## 本页不抄

- 怎样写过滤逻辑、怎样配 Cosmos-SDK Query、怎样拼 IP:端口。
- Peer Filtering bundled。那是不变量 326。
- id 过滤查询绿了不是已经过了 addr。那是不变量 326 item 2 余量 / 735。
- 有 /store 路径不是已经是引擎在用。那是不变量 326 item 3 余量 / 736。
- InitPeer 已经能交互。那是不变量 305。
- 自动封禁表已经有界。那是不变量 50。
- QueryState 已经是 ExecuteTxState。那是不变量 314。
