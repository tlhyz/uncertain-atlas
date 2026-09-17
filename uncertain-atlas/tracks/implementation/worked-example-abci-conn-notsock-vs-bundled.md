# 例：看见同进程 is not already socket-isolated interchangeable / not already other-transport interchangeable / not already settled interchangeable

**层次**：实现 / 同进程 not already socket-isolated / not already other-transport / not already settled 正式三事（307 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Client and Server](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_client_server.md) ABCI transport / four connections。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「同进程 not already socket-isolated / not already other-transport / not already settled 正式三事（307 余量）/ not 977 abci-conn-notsock interchangeable / not 307 abci-conn-vs-gates bundled interchangeable」，不是传输 bundled（307），也不是半写已经原子（5），也不是默认锁就已经 RPC 安全（310/974）。不要另写怎样开套接字或怎样编 protobuf。

## 官方三件事

1. **看见同进程 / 看见编进同一个二进制 这份传输 is not already 已经有套接字隔离 interchangeable，也不是已经传输 bundled（307） interchangeable / 977 abci-conn-notsock interchangeable / 978 abci-conn-notfast interchangeable / 307 abci-conn item 2 gRPC 最容易 interchangeable，也不是已经同进程 not already socket-isolated / not already other-transport / not already settled 正式三事 bundled（307 item 1 余量） interchangeable / 307 abci-conn item 1 interchangeable。**  
   官方写：最简单的实现是用 Go 的函数调用。Go 写的应用可以和 CometBFT 链进同一个二进制。看见同进程，不是已经有套接字边界 interchangeable——本页从 307 item 1 侧钉 not already socket-isolated 单句。307 abci-conn vs gates bundled unbundling 在本页 item 1 启动。

2. **看见一个进程 / 看见链在一起 / 这份传输 is not already 已经是另一条传输 interchangeable，也不是已经传输 bundled（307） interchangeable / 977 abci-conn-notsock interchangeable / 307 abci-conn item 3 一条连接 interchangeable / 979 abci-conn-notgates interchangeable，也不是已经半写已经原子 interchangeable / 5 atomic interchangeable。**  
   官方把一个进程和已经是另一条传输分开——307 bundled 第一件事常与 5 混成「看见同进程就已经隔离或已经半写原子 interchangeable」，本页钉 not already other-transport 单句。

3. **看见链在一起 / 看见同进程 / 这份传输 is not already 已经交差 interchangeable，也不是已经传输 bundled（307） interchangeable / 977 abci-conn-notsock interchangeable / 978 abci-conn-notfast interchangeable，也不是已经默认锁就已经 RPC 安全 interchangeable / 310/974 commit-lock-notrpc interchangeable。**  
   官方把链在一起和已经换了信任对象分开。看见链在一起，不是已经交差 interchangeable。307 abci-conn vs gates bundled unbundling 在本页 item 1 启动。

长度前缀做法、protobuf 字段表、ABCI-CLI 命令是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **同进程 not already socket-isolated ≠ 已经有套接字隔离 interchangeable：** 官方把函数调用和套接字 / gRPC 分开。
- **看见一个进程 not already other-transport ≠ 已经是另一条传输 interchangeable：** 官方把一个进程和已经是另一条传输分开。
- **看见链在一起 not already settled ≠ 已经交差 interchangeable：** 官方把链在一起和已经换了信任对象分开；307 abci-conn vs gates bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 同进程一个二进制 | 不是已经有套接字隔离 | 不是半写已经原子（5） |
| 看见一个进程 | 不是已经是另一条传输 | 不是默认锁就已经 RPC 安全（310/974） |
| 看见链在一起 | 不是已经交差 | 不是 gRPC 最容易就已经快（978） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看同进程 not already socket-isolated / not already other-transport / not already settled 正式三事（307 余量），必须分开是不是已经隔离、是不是已经是另一条传输、是不是已经交差。可以跳过「看见应用已经接上就已经是四门」。不要另写怎样开套接字或怎样编 protobuf。307 abci-conn vs gates bundled unbundling 在本页 item 1 启动；续 [`worked-example-abci-conn-notfast-vs-bundled.md`](worked-example-abci-conn-notfast-vs-bundled.md)（不变量 978 item 2）。

## 本页不抄

- protobuf 字段表、怎样开套接字、怎样编 protobuf。
- 传输 bundled。那是不变量 307。
- 半写已经原子。那是不变量 5。
- 默认锁就已经 RPC 安全。那是不变量 310/974。
