# 例：看见一条 ABCI 连接 is not already enough interchangeable / not already four-gates interchangeable / not already settled interchangeable

**层次**：实现 / 一条连接 not already enough / not already four-gates / not already settled 正式三事（307 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Client and Server](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_client_server.md) ABCI transport / four connections。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「一条连接 not already enough / not already four-gates / not already settled 正式三事（307 余量）/ not 979 abci-conn-notgates interchangeable / not 307 abci-conn-vs-gates bundled interchangeable」，不是传输 bundled（307），也不是 CheckTx 已经进提案（33），也不是 Info 车道已经齐（367）。不要另写怎样开套接字或怎样编 protobuf。

## 官方三件事

1. **看见一条 ABCI 连接 / 看见已经能回话 这份传输 is not already 已经够用 interchangeable，也不是已经传输 bundled（307） interchangeable / 979 abci-conn-notgates interchangeable / 977 abci-conn-notsock interchangeable / 978 abci-conn-notfast interchangeable / 307 abci-conn item 1 同进程 interchangeable，也不是已经一条连接 not already enough / not already four-gates / not already settled 正式三事 bundled（307 item 3 余量） interchangeable / 307 abci-conn item 3 interchangeable。**  
   官方写：ABCI 服务器必须能处理多条连接，因为 CometBFT 用四条。看见回了一句，不是已经齐了连接 interchangeable——本页从 307 item 3 侧钉 not already enough 单句。307 abci-conn vs gates bundled unbundling 在本页 item 3 完成。

2. **看见四条连接 / 看见已经能回话 / 这份传输 is not already 已经是 Prepare / Process / Finalize / Extend 那四门 interchangeable，也不是已经传输 bundled（307） interchangeable / 979 abci-conn-notgates interchangeable / 307 abci-conn item 2 gRPC 最容易 interchangeable / 978 abci-conn-notfast interchangeable，也不是已经 CheckTx 已经进提案 interchangeable / 33 four-gates interchangeable。**  
   官方把四条连接和已经是四门方法分开。看见四条连接，不是已经是四门 interchangeable。本页钉 not already four-gates 单句。

3. **看见客户端 / 看见已经能回话 / 这份传输 is not already 已经交差 interchangeable，也不是已经传输 bundled（307） interchangeable / 979 abci-conn-notgates interchangeable / 977 abci-conn-notsock interchangeable，也不是已经 Info 车道已经齐 interchangeable / 367 Info lane interchangeable。**  
   官方把客户端和已经只是共识引擎分开；测试工具也是一种 ABCI 客户端。看见客户端，不是已经交差 interchangeable。307 abci-conn vs gates bundled unbundling 在本页 item 3 完成。

长度前缀做法、protobuf 字段表、ABCI-CLI 命令是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **一条连接 not already enough ≠ 已经够用 interchangeable：** 官方把必须能处理多条连接，和回了一句分开。
- **看见四条连接 not already four-gates ≠ 已经是四门 interchangeable：** 官方把四条连接和四门方法分开。
- **看见客户端 not already settled ≠ 已经交差 interchangeable：** 官方把客户端和已经只是共识引擎分开；307 abci-conn vs gates bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 一条连接 / 四条连接 | 不是已经够用，也不是已经是四门 | 不是 CheckTx 已经进提案（33） |
| 看见四条连接 | 不是已经是四门 | 不是 Info 车道已经齐（367） |
| 看见客户端 | 不是已经交差 | 不是同进程就已经隔离（977） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看一条连接 not already enough / not already four-gates / not already settled 正式三事（307 余量），必须分开是不是已经够用、是不是已经是四门、是不是已经交差。可以跳过「看见应用已经接上就已经是四门」。不要另写怎样开套接字或怎样编 protobuf。307 abci-conn vs gates bundled unbundling 在本页 item 3 完成。

## 本页不抄

- protobuf 字段表、怎样开套接字、怎样编 protobuf。
- 传输 bundled。那是不变量 307。
- CheckTx 已经进提案。那是不变量 33。
- Info 车道已经齐。那是不变量 367。
