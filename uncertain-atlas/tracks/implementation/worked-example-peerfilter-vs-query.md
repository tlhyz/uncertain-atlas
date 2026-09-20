# 例：看见发了 addr 过滤查询不是已经收下这个人；看见 id 过滤查询绿了不是已经过了 addr；看见有 /store 路径不是已经是引擎在用

**层次**：实现 / Peer Filtering。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Peer Filtering、Paths。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「发了 addr 过滤查询不是已经收下这个人 / id 过滤查询绿了不是已经过了 addr / 有 /store 路径不是已经是引擎在用」，不是自动封禁表已经有界，也不是 InitPeer 已经能交互。不要另写怎样写过滤或怎样配路径。 326 peerfilter vs query bundled unbundling 启动（734）；精读 [`worked-example-peerfilter-notaccepted-vs-bundled.md`](worked-example-peerfilter-notaccepted-vs-bundled.md)（不变量 734 item 1）。

## 官方三件事

规范把连上一个人时的两道查询和路径写成三件独立的实现事，不是「看见连上了就已经收下、已经过了两道、已经在用所有路径」一件事：

1. **看见发了 `/p2p/filter/addr` / 看见 TCP 已经连上 不是已经收下这个人，也不是已经过了 id 那一道。**  
   官方写：CometBFT 连上一个人时，会用 Query 发**两道**查询，**没有额外数据**。第一道是 `/p2p/filter/addr/`，后面跟这个连接的 IP 和端口。看见发了 addr，不是已经收下。看见 TCP 连上，不是已经过了 Query。看见只问了地址，不是已经问了 id。
2. **看见发了 `/p2p/filter/id` / 看见公钥地址对上 不是已经过了 addr 那一道，也不是已经能交互。**  
   官方写：第二道是 `/p2p/filter/id/`，后面跟对等节点 ID（也就是对端公钥的 `Address()`）。**任意一道**回了非零 ABCI 码，CometBFT **拒连**。看见 id 绿了，不是 addr 已经绿。看见公钥地址对上，不是已经能交互。看见拒连，不是已经写进持久封禁表。
3. **看见有 `/store` / `/app` 路径 / 看见 Query 能带路径 不是已经是引擎在用，也不是已经是过滤。**  
   官方写：查询对着路径走，还可以另带数据。高层路径可以有 `/p2p`、`/store`、`/app`。**眼下 CometBFT 只用 `/p2p`**，用来过滤邻居。看见规范写了三条路径，不是已经三条都在用。看见有 `/store`，不是已经是过滤。看见能带数据，不是这两道过滤已经带了数据。

怎样写过滤逻辑、怎样配 Cosmos-SDK Query、怎样拼 IP:端口是规范里的取值或做法，本页不抄。自动封禁表已经有界是不变量 50，本页不抄。

## 官方为什么这样拆

- **发了 addr 过滤查询 ≠ 已经收下这个人：** 官方把 TCP 连上和两道 Query 分开；一道绿不是两道都绿。
- **id 过滤查询绿了 ≠ 已经过了 addr：** 官方把地址过滤和节点 ID 过滤写成两道独立查询。
- **有 /store 路径 ≠ 已经是引擎在用：** 官方把可以有的高层路径和眼下只用 `/p2p` 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 发了 addr 过滤查询 | 不是已经收下这个人 | 不是 InitPeer 已经能交互（305） |
| id 过滤查询绿了 | 不是已经过了 addr | 不是自动封禁表已经有界（50） |
| 有 /store 路径 | 不是已经是引擎在用 | 不是 QueryState 已经是 ExecuteTxState（314） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「连上就已经过滤过」，必须分开发了 addr 过滤查询是不是已经收下这个人、id 过滤查询绿了是不是已经过了 addr、有 /store 路径是不是已经是引擎在用。可以跳过「看见连上了就已经收下」。不要另写怎样写过滤或怎样配路径。 326 peerfilter vs query bundled unbundling 启动（734 item 1）。

## 本页不抄

- 怎样写过滤逻辑、怎样配 Cosmos-SDK Query、怎样拼 IP:端口。
- 自动封禁表已经有界。那是不变量 50。
- InitPeer 已经能交互。那是不变量 305。
- QueryState 已经是 ExecuteTxState。那是不变量 314。
