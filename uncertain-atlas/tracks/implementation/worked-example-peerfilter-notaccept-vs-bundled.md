# 例：看见发了 addr 过滤查询 is not already accepted interchangeable / not already past-id interchangeable / not already settled interchangeable

**层次**：实现 / 发了 addr 过滤查询 not already accepted / not already past-id / not already settled 正式三事（326 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Peer Filtering、Paths。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「发了 addr 过滤查询 not already accepted / not already past-id / not already settled 正式三事（326 余量）/ not 944 peerfilter-notaccept interchangeable / not 326 peerfilter-vs-query bundled interchangeable」，不是过滤 bundled（326），也不是 InitPeer 已经能交互（305），也不是 Query 回了就已经复制（329/938）。不要另写怎样写过滤或怎样配路径。

## 官方三件事

1. **看见发了 /p2p/filter/addr / 看见 TCP 已经连上 这份查询 is not already 已经收下这个人 interchangeable，也不是已经过滤 bundled（326） interchangeable / 944 peerfilter-notaccept interchangeable / 945 peerfilter-notaddr interchangeable / 326 peerfilter item 2 id 绿了 interchangeable，也不是已经发了 addr 过滤查询 not already accepted / not already past-id / not already settled 正式三事 bundled（326 item 1 余量） interchangeable / 326 peerfilter item 1 interchangeable。**  
   官方写：CometBFT 连上一个人时，会用 Query 发两道查询，没有额外数据。第一道是 /p2p/filter/addr/，后面跟这个连接的 IP 和端口。看见发了 addr，不是已经收下 interchangeable——本页从 326 item 1 侧钉 not already accepted 单句。326 peerfilter vs query bundled unbundling 在本页 item 1 启动。

2. **看见 TCP 连上 / 看见只问了地址 / 这份查询 is not already 已经过了 id 那一道 interchangeable，也不是已经过滤 bundled（326） interchangeable / 944 peerfilter-notaccept interchangeable / 326 peerfilter item 3 /store interchangeable / 946 peerfilter-notstore interchangeable，也不是已经 InitPeer 已经能交互 interchangeable / 305 initpeer interchangeable。**  
   官方把 TCP 连上和已经过了 Query 分开——326 bundled 第一件事常与 305 混成「看见发了 addr 就已经收下或已经能交互 interchangeable」，本页钉 not already past-id 单句。

3. **看见只问了地址 / 看见 TCP 连上 / 这份查询 is not already 已经交差 interchangeable，也不是已经过滤 bundled（326） interchangeable / 944 peerfilter-notaccept interchangeable / 945 peerfilter-notaddr interchangeable，也不是已经 Query 回了就已经复制 interchangeable / 329/938 query-notrepl interchangeable。**  
   官方把只问了地址和已经问了 id / 已经交差分开。看见只问了地址，不是已经交差 interchangeable。326 peerfilter vs query bundled unbundling 在本页 item 1 启动。

怎样写过滤逻辑、怎样配 Cosmos-SDK Query、怎样拼 IP:端口是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **发了 addr 过滤查询 not already accepted ≠ 已经收下这个人 interchangeable：** 官方把 TCP 连上和两道 Query 分开。
- **看见 TCP 连上 not already past-id ≠ 已经过了 id 那一道 interchangeable：** 官方把只问了地址和已经过了 id 分开。
- **看见只问了地址 not already settled ≠ 已经交差 interchangeable：** 官方把只问了地址和已经交差分开；326 peerfilter vs query bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 发了 addr 过滤查询 | 不是已经收下这个人 | 不是 InitPeer 已经能交互（305） |
| 看见 TCP 连上 | 不是已经过了 id 那一道 | 不是 Query 回了就已经复制（329/938） |
| 看见只问了地址 | 不是已经交差 | 不是 id 绿了就已经过了 addr（945） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看发了 addr 过滤查询 not already accepted / not already past-id / not already settled 正式三事（326 余量），必须分开是不是已经收下这个人、是不是已经过了 id 那一道、是不是已经交差。可以跳过「看见连上了就已经收下」。不要另写怎样写过滤或怎样配路径。326 peerfilter vs query bundled unbundling 在本页 item 1 启动；续 [`worked-example-peerfilter-notaddr-vs-bundled.md`](worked-example-peerfilter-notaddr-vs-bundled.md)（不变量 945 item 2）。

## 本页不抄

- 怎样写过滤逻辑、怎样配 Cosmos-SDK Query、怎样拼 IP:端口。
- 过滤 bundled。那是不变量 326。
- id 绿了就已经过了 addr。那是不变量 326 item 2 余量 / 945。
- InitPeer 已经能交互。那是不变量 305。
