# 例：看见 Echo a string to test an ABCI client/server implementation 不是已经 Flush；看见 Request Message 是要回显的字符串 不是已经 Response Message interchangeable；看见 Response Message 是入参那串 不是已经测实现就已经刷完

**层次**：实现 / Echo Usage 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Echo Request / Response / Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Echo a string to test implementation 不是已经 Flush / Request Message 不是 Response Message interchangeable / Response Message 不是已经测实现就已经刷完 / not 674 echousage-notflush interchangeable / not 492 echousage-vs-flush bundled interchangeable」，不是 Commit 空请求 bundled 三事（399），也不是 Echo 请求 Message 就已经是 Flush（394）。不要另写怎样写 Echo、怎样测实现。

## 官方三件事

规范把 Echo Usage、Echo Request `Message`、Echo Response `Message` 写成三件独立的实现事，不是「看见 Echo 了就已经 Flush、已经是入参字段、已经刷完」一件事：

1. **看见 Echo a string to test an ABCI client/server implementation / 看见 Echo 用来测客户端/服务端实现 不是已经 Flush 那种把客户端排队的消息冲到服务端 interchangeable，也不是已经 Commit 空请求 bundled（399）第三件事 interchangeable，也不是已经送到 / 已经能往下走 interchangeable。**  
   官方 Usage 写：Echo a string to test an ABCI client/server implementation。看见 Echo 用来测实现，不是已经 Flush 要把客户端排队的消息冲到服务端（374） interchangeable。看见测 client/server implementation，不是已经 Commit 不带参数 就等于已经落盘（399） bundled 第一二件事 interchangeable——399 钉 Commit 空请求全段，本页钉 Methods Echo Usage 单句。看见 Echo 能叫，不是已经 Flush 回包回来就算这次同步 interchangeable。
2. **看见 Request `Message (string)`: A string to echo back / 看见 Echo 请求 Message 是要回显的字符串 不是已经 Response `Message`: The input string interchangeable，也不是已经 Echo 请求 Message 就已经是 Flush（394） interchangeable，也不是已经填了 Message 就代表已经回显 interchangeable。**  
   官方 Request 写：`Message (string)`: A string to echo back。看见 Request Message 是要回显的字符串，不是已经 Response Message 是入参那串（399）那种回包侧 interchangeable——399 钉回包栏，本页钉请求栏。看见填了 Message，不是已经 Flush（394） interchangeable。看见 string to echo back，不是已经 Response 侧 the input string 就代表请求已经交差 interchangeable。
3. **看见 Response `Message (string)`: The input string / 看见 Echo 回包 Message 是入参那串 不是已经 Echo 用来测实现就已经刷完 interchangeable，也不是已经 Request Message 字段 interchangeable，也不是已经 Flush 回包回来就算同步 interchangeable。**  
   官方 Response 写：`Message (string)`: The input string。看见 the input string，不是已经 Echo Usage 测实现 就等于已经刷完（399 bundled 第三件事） interchangeable——399 钉 Commit 空请求语境，本页钉 Response 栏。看见回包 Message 是入参那串，不是已经 Request Message 是要回显的字符串 interchangeable——394 钉 Request vs Flush，本页钉 Request vs Response。看见回了 Message，不是已经 Flush 就已经送到 interchangeable。

怎样写 Echo、怎样填 Message、怎样测 client/server 是规范里的做法，本页不抄。Commit 空请求（399）、Echo 请求 Message 就已经是 Flush（394）、Flush 要把客户端排队的消息冲到服务端（374）是另外那套，本页不抄。

## 官方为什么这样拆

- **Echo a string to test implementation ≠ 已经 Flush / 已经送到：** 官方把 Echo 测实现和 Flush 冲队列分开。
- **Request Message string to echo back ≠ Response Message the input string：** 官方把请求要回显的字符串和回包入参那串分开。
- **Response Message the input string ≠ 已经测实现就已经刷完：** 官方把回包栏语义和 Usage 测实现交差分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Echo a string to test implementation | 不是已经 Flush | 不是 Commit 空请求 bundled（399） |
| Request Message string to echo back | 不是 Response Message interchangeable | 不是 Echo 请求 Message 就已经是 Flush（394） |
| Response Message the input string | 不是已经测实现就已经刷完 | 不是 Flush 回包回来就算同步（374） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Echo 了就已经 Flush、已经是入参字段、已经刷完」，必须分开 Echo a string to test implementation 是不是已经 Flush flush queue / commit-empty-echo bundled / Flush sync response interchangeable、Request Message string to echo back 是不是 Response Message interchangeable / 已经是 Flush、Response Message the input string 是不是已经测实现就已经刷完 interchangeable。可以跳过「看见 Echo 了就已经 Flush」。不要另写怎样写 Echo。492 echousage vs flush bundled unbundling 完成（674 item 1 / 675 item 2 / 676 item 3）；精读 [`worked-example-echousage-notdone-vs-bundled.md`](worked-example-echousage-notdone-vs-bundled.md)（不变量 676 item 3）。

## 本页不抄

- 怎样写 Echo、怎样填 Message、怎样测 client/server。
- Commit 空请求。那是不变量 399。
- Echo 请求 Message 就已经是 Flush。那是不变量 394。
- Flush 要把客户端排队的消息冲到服务端。那是不变量 374。
- Commit 不带参数就等于已经落盘。那是不变量 335 / 399。
