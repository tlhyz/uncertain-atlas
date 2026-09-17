# 例：看见节点已经在跑 is not already hot-add interchangeable / not already another-name interchangeable / not already restart interchangeable

**层次**：网络 / 跑着 not already hot-add / not already another-name / not already restart 正式三事（305 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Reactor API](https://github.com/cometbft/cometbft/blob/main/spec/p2p/reactor-api/reactor.md) reactor / InitPeer vs AddPeer。  
**对应课文**：[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「跑着 not already hot-add / not already another-name / not already restart 正式三事（305 余量）/ not 1003 initpeer-nothot interchangeable / not 305 initpeer-vs-addpeer bundled interchangeable」，不是反应堆时序 bundled（305），也不是握手请求已经是已接受邻居（67），也不是 Peer 句柄就已经是那个人（306）。不要另写怎样实现 Receive 并发或怎样发 Envelope。

## 官方三件事

1. **看见节点已经在跑 / 看见反应堆已经登记过名字 这份时序 is not already 已经能再登记一个 interchangeable，也不是已经反应堆时序 bundled（305） interchangeable / 1003 initpeer-nothot interchangeable / 1001 initpeer-nottalk interchangeable / 305 initpeer item 1 InitPeer interchangeable，也不是已经跑着 not already hot-add / not already another-name / not already restart 正式三事 bundled（305 item 3 余量） interchangeable / 305 initpeer item 3 interchangeable。**  
   官方写：登记必须用 Switch.AddReactor，而且必须发生在节点、尤其是 p2p 层启动之前。运行中的节点不支持再登记一个反应堆。看见进程起来了，不是已经能热加 interchangeable——本页从 305 item 3 侧钉 not already hot-add 单句。305 initpeer vs addpeer bundled unbundling 在本页 item 3 完成。

2. **看见名字已经占了 / 看见跑着 / 这份时序 is not already 已经能再占一个 interchangeable，也不是已经反应堆时序 bundled（305） interchangeable / 1003 initpeer-nothot interchangeable / 305 initpeer item 2 Receive interchangeable / 1002 initpeer-notadd interchangeable，也不是已经握手请求已经是已接受邻居 interchangeable / 67 handshake interchangeable。**  
   官方把名字已经占了和已经能再占一个分开。看见名字已经占了，不是已经能再占一个 interchangeable。本页钉 not already another-name 单句。

3. **看见停过了 / 看见跑着 / 这份时序 is not already 已经能再开 interchangeable，也不是已经反应堆时序 bundled（305） interchangeable / 1003 initpeer-nothot interchangeable / 1001 initpeer-nottalk interchangeable，也不是已经 Peer 句柄就已经是那个人 interchangeable / 306 peer-handler interchangeable。**  
   官方把 OnStart / OnStop 各只能一次和已经能再开分开。看见停过了，不是已经能再开 interchangeable。305 initpeer vs addpeer bundled unbundling 在本页 item 3 完成。

通道号、Quint 模型、ABNF 文法、信封字段表是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **跑着 not already hot-add ≠ 已经能再登记一个 interchangeable：** 官方把起步登记和运行中热加分开。
- **看见名字已经占了 not already another-name ≠ 已经能再占一个 interchangeable：** 官方把名字已经占了和已经能再占一个分开。
- **看见停过了 not already restart ≠ 已经能再开 interchangeable：** 官方把 OnStart / OnStop 各只能一次和已经能再开分开；305 initpeer vs addpeer bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 运行中再登记 | 不是已经能再加反应堆 | 不是握手请求已经是已接受邻居（67） |
| 看见名字已经占了 | 不是已经能再占一个 | 不是 Peer 句柄就已经是那个人（306） |
| 看见停过了 | 不是已经能再开 | 不是 InitPeer 就已经能对说（1001） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看跑着 not already hot-add / not already another-name / not already restart 正式三事（305 余量），必须分开是不是已经能再登记、是不是已经能再占一个、是不是已经能再开。可以跳过「看见对等节点对象就已经加进去」。不要另写怎样实现 Receive 并发或怎样发 Envelope。305 initpeer vs addpeer bundled unbundling 在本页 item 3 完成。

## 本页不抄

- Quint 模型、ABNF 文法、通道号、信封字段表。
- 反应堆时序 bundled。那是不变量 305。
- 握手请求已经是已接受邻居。那是不变量 67。
- Peer 句柄就已经是那个人。那是不变量 306。
