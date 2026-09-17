# 例：看见 gRPC 最容易 is not already fast interchangeable / not already no-overhead interchangeable / not already settled interchangeable

**层次**：实现 / gRPC 最容易 not already fast / not already no-overhead / not already settled 正式三事（307 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Client and Server](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_client_server.md) ABCI transport / four connections。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「gRPC 最容易 not already fast / not already no-overhead / not already settled 正式三事（307 余量）/ not 978 abci-conn-notfast interchangeable / not 307 abci-conn-vs-gates bundled interchangeable」，不是传输 bundled（307），也不是 post-commit 等待已经是槽位（52），也不是 Snapshot Connection 已经必开（334）。不要另写怎样开套接字或怎样编 protobuf。

## 官方三件事

1. **看见语言里有 gRPC / 看见这是最容易的做法 这份传输 is not already 已经是高性能路径 interchangeable，也不是已经传输 bundled（307） interchangeable / 978 abci-conn-notfast interchangeable / 977 abci-conn-notsock interchangeable / 307 abci-conn item 1 同进程 interchangeable，也不是已经 gRPC 最容易 not already fast / not already no-overhead / not already settled 正式三事 bundled（307 item 2 余量） interchangeable / 307 abci-conn item 2 interchangeable。**  
   官方写：不用 Go 时，若语言里有 gRPC，这是最容易的做法，但会有显著的性能开销。看见最容易，不是已经快 interchangeable——本页从 307 item 2 侧钉 not already fast 单句。307 abci-conn vs gates bundled unbundling 在本页 item 2 续。

2. **看见能回话 / 看见最容易 / 这份传输 is not already 已经没有开销 interchangeable，也不是已经传输 bundled（307） interchangeable / 978 abci-conn-notfast interchangeable / 307 abci-conn item 3 一条连接 interchangeable / 979 abci-conn-notgates interchangeable，也不是已经 post-commit 等待已经是槽位 interchangeable / 52 slot interchangeable。**  
   官方把能回话和已经没有开销分开。看见能回话，不是已经没有开销 interchangeable。本页钉 not already no-overhead 单句。

3. **看见套接字那套前缀 / 看见最容易 / 这份传输 is not already 已经交差 interchangeable，也不是已经传输 bundled（307） interchangeable / 978 abci-conn-notfast interchangeable / 977 abci-conn-notsock interchangeable，也不是已经 Snapshot Connection 已经必开 interchangeable / 334 snapshot-conn interchangeable。**  
   官方把长度前缀方案和已经套在 gRPC 上分开。看见套接字那套前缀，不是已经交差 interchangeable。307 abci-conn vs gates bundled unbundling 在本页 item 2 续。

长度前缀做法、protobuf 字段表、ABCI-CLI 命令是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **gRPC 最容易 not already fast ≠ 已经是高性能路径 interchangeable：** 官方把容易和显著开销分开。
- **看见能回话 not already no-overhead ≠ 已经没有开销 interchangeable：** 官方把能回话和已经没有开销分开。
- **看见套接字那套前缀 not already settled ≠ 已经交差 interchangeable：** 官方把长度前缀和 gRPC 分开；307 abci-conn vs gates bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| gRPC 最容易 | 不是已经高性能 | 不是 post-commit 等待已经是槽位（52） |
| 看见能回话 | 不是已经没有开销 | 不是 Snapshot Connection 已经必开（334） |
| 看见套接字那套前缀 | 不是已经交差 | 不是一条连接就已经是四门（979） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 gRPC 最容易 not already fast / not already no-overhead / not already settled 正式三事（307 余量），必须分开是不是已经快、是不是已经没有开销、是不是已经交差。可以跳过「看见应用已经接上就已经是四门」。不要另写怎样开套接字或怎样编 protobuf。307 abci-conn vs gates bundled unbundling 在本页 item 2 续；续 [`worked-example-abci-conn-notgates-vs-bundled.md`](worked-example-abci-conn-notgates-vs-bundled.md)（不变量 979 item 3）。

## 本页不抄

- protobuf 字段表、怎样开套接字、怎样编 protobuf。
- 传输 bundled。那是不变量 307。
- post-commit 等待已经是槽位。那是不变量 52。
- Snapshot Connection 已经必开。那是不变量 334。
