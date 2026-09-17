# 例：看见 Request Message string to echo back is not already Response Message interchangeable / Echo request Message is Flush interchangeable / filled Message means echoed interchangeable

**层次**：实现 / Echo Request Message string to echo back not Response Message / not Echo request Message is Flush / not filled Message means echoed 正式三事（492 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Echo Request / Response。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Echo Request Message string to echo back not Response Message / not Echo request Message is Flush / not filled Message means echoed 正式三事（492 余量）/ not 675 echousage-notreqresp interchangeable / not 492 echousage-vs-flush bundled interchangeable」，不是 Echo Usage 正式三事 bundled（492），也不是 Echo Usage Echo a string to test implementation not Flush flush queue（674）或 Echo 请求 Message 就已经是 Flush bundled（394）。不要另写怎样写 Echo、怎样填 Message、怎样测 client/server。

## 官方三件事

规范把 Echo Request 里 `Message (string)`: A string to echo back 和「已经是 Response Message the input string（492） interchangeable / 已经是 Echo 请求 Message 就已经是 Flush（394） interchangeable / 已经填了 Message 就代表已经回显 interchangeable / 已经 Response 侧 the input string 就代表请求已经交差 interchangeable」分开写成三件独立的实现事，不是「看见 Request Message string to echo back 就已经 Response Message interchangeable / 就已经 Echo Message 是 Flush interchangeable / 就已经填了 Message 就代表已经回显 interchangeable」一件事：

1. **看见 Request `Message (string)`: A string to echo back / 看见 Echo 请求 Message 是要回显的字符串 / string to echo back is not already 已经 Response `Message (string)`: The input string（492） interchangeable / 492 echousage-vs-flush interchangeable / 492 echousage item 3 Response Message interchangeable / 已经 Echo 回包 Message 是入参那串 interchangeable / 已经 Echo 回包栏 interchangeable / 399 commit-empty-echo bundled interchangeable / 399 commit-empty-echo item 2 interchangeable / 673 flushusage-notimmediatesync interchangeable / 676 echousage-notdone interchangeable，也不是已经 Echo Usage 正式三事 bundled（492） interchangeable / 675 echousage-notreqresp interchangeable / 674 echousage-notflush interchangeable / 492 echousage item 1 test implementation interchangeable，也不是已经 Request Message string to echo back not Response Message / not Echo request Message is Flush / not filled Message means echoed 正式三事 bundled（492 item 2 余量） interchangeable / 492 echousage item 2 interchangeable，也不是已经 Echo a string to test implementation not Flush flush queue bundled（492 item 1 余量 / 674） interchangeable / 394 echo-message-is-flush interchangeable / 492 echousage bundled interchangeable。**  
   官方 Request 写：`Message (string)`: A string to echo back。看见 Echo 请求 Message 是要回显的字符串，不是已经 Response Message 是入参那串 interchangeable——492 钉 Response 栏，本页从 492 item 2 侧钉 not Response Message 单句。看见 string to echo back，不是已经 Echo Usage 正式三事 bundled（492） interchangeable——492 钉 bundled 三事，本页钉 Methods Echo Request 请求栏。看见 Request Message，不是已经 Echo a string to test implementation（492 item 1 余量 / 674） interchangeable——674 另钉 item 1，本页钉 item 2 第一件事。492 echousage vs flush bundled unbundling 在本页 item 2 启动。

2. **看见 Request Message string to echo back / 看见 Echo 请求 Message 是要回显的字符串 / 看见填了 Message is not already 已经 Echo 请求 Message 就已经是 Flush（394） interchangeable / 394 echo-message-is-flush interchangeable / 已经 Echo 请求 Message 是 Flush interchangeable / 已经 Echo Message 是 Flush interchangeable / 374 flush bundled interchangeable / 374 flush bundled item 1 interchangeable / 493 flushusage-vs-echo interchangeable / 671 flushusage-notechoqueued interchangeable / 671 flushusage-notechoqueued item 3 interchangeable，也不是已经 Echo Usage 正式三事 bundled（492） interchangeable / 675 echousage-notreqresp interchangeable / 492 echousage item 1 test implementation interchangeable / 492 echousage item 3 Response Message interchangeable，也不是已经 Request Message string to echo back not Response Message / not Echo request Message is Flush / not filled Message means echoed 正式三事 bundled（492 item 2 余量） interchangeable / 492 echousage item 2 interchangeable，也不是已经 Flush 要把客户端排队的消息冲到服务端 bundled（374） interchangeable / 493 flushusage item 1 Signals flush interchangeable / 310 commit-lock-vs-rpc interchangeable，也不是已经 ExtendedCommitInfo.round 是提交轮 bundled（394 余量 / extcommitround） interchangeable / 399 commit-empty-echo item 1 interchangeable。**  
   官方把 Request Message string to echo back 单句和 Echo 请求 Message 就已经是 Flush 路径分开——492 bundled 第二件事常与 394 混成「看见 Request Message string to echo back 就已经 Echo 请求 Message 是 Flush interchangeable / 就已经 Echo Message 是 Flush interchangeable / 就已经 Flush 冲队列 interchangeable」，本页钉 not Echo request Message is Flush 单句。看见 Echo 请求 Message 是要回显的字符串，不是已经 Echo 请求 Message 就已经是 Flush interchangeable——394 钉 Request vs Flush，本页钉 Echo Request 请求栏语义。看见填了 Message，不是已经 Signals messages queued should be flushed（671） interchangeable——671 另钉 Flush item 1，本页钉 item 2 第二件事。

3. **看见 Request Message string to echo back / string to echo back / 看见 Echo 请求 Message 是要回显的字符串 is not already 已经填了 Message 就代表已经回显 interchangeable / 已经 Response 侧 the input string 就代表请求已经交差 interchangeable / 已经 Echo 回包 Message 是入参那串 interchangeable / 492 echousage item 3 Response Message interchangeable / 676 echousage-notdone interchangeable / 399 commit-empty-echo item 2 interchangeable / 399 commit-empty-echo bundled interchangeable / 已经测实现就已经刷完 interchangeable，也不是已经 Echo Usage 正式三事 bundled（492） interchangeable / 675 echousage-notreqresp interchangeable / 674 echousage-notflush interchangeable / 492 echousage item 1 test implementation interchangeable，也不是已经 Request Message string to echo back not Response Message / not Echo request Message is Flush / not filled Message means echoed 正式三事 bundled（492 item 2 余量） interchangeable / 492 echousage item 2 interchangeable，也不是已经 Response Message the input string not already test done bundled（492 item 3 余量 / 676） interchangeable / 673 flushusage-notimmediatesync interchangeable / 374 flush-vs-sent interchangeable。**  
   官方把 Request Message string to echo back 单句和「填了 Message 就代表已经回显 / Response 侧 the input string 就代表请求已经交差」路径分开——492 bundled 第二件事常与 492 item 3 / 399 混成「看见 Request Message 就已经填了 Message 就代表已经回显 interchangeable / 就已经 Response the input string 就代表请求已经交差 interchangeable / 就已经测实现就已经刷完 interchangeable」，本页钉 not filled Message means echoed 单句。看见 string to echo back，不是已经 Response Message the input string（676 item 3 余量） interchangeable——676 另钉 item 3，本页钉 item 2 第三件事。看见 Echo 请求 Message，不是已经 Echo 用来测实现就已经刷完 interchangeable——674 钉 Usage 测实现，本页钉 Request 请求栏。492 echousage vs flush bundled unbundling 在本页 item 2 启动。

怎样写 Echo、怎样填 Message、怎样测 client/server 是规范里的做法，本页不抄。Echo Usage 正式三事 bundled（492）、Echo a string to test implementation not Flush flush queue（492 item 1 余量 / 674）、Response Message the input string not already test done（492 item 3 余量 / 676）、Echo 请求 Message 就已经是 Flush bundled（394）、Flush 要把客户端排队的消息冲到服务端 bundled（374）、Flush Usage 正式三事 bundled（493）、Commit 空请求 bundled（399）是另外那套，本页不抄。

## 官方为什么这样拆

- **Request Message string to echo back not Response Message ≠ 492 echousage item 3 Response Message interchangeable：** 官方把 Echo Request 请求要回显的字符串和 Echo Response 回包入参那串分开。
- **Request Message not Echo request Message is Flush ≠ 394 echo-message-is-flush interchangeable：** 官方把 Request Message string to echo back 单句和 Echo 请求 Message 就已经是 Flush 路径分开。
- **Request Message not filled Message means echoed ≠ 676 echousage-notdone interchangeable：** 官方把 Request 请求栏语义和「填了 Message 就代表已经回显 / Response the input string 就代表请求已经交差」路径分开；492 echousage vs flush bundled unbundling 在本页 item 2 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Request Message string to echo back | 不是 Response Message the input string（492 item 3） | 不是 Echo test implementation（674/492 item 1） |
| Echo 请求 Message 是要回显的字符串 | 不是 Echo request Message is Flush（394） | 不是 Flush flush queue（374/671） |
| string to echo back / 填了 Message | 不是 filled Message means echoed | 不是 Response already test done（676/492 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Echo Request Message string to echo back not Response Message / not Echo request Message is Flush / not filled Message means echoed 正式三事（492 余量），必须分开 Request Message string to echo back 是不是 Response Message interchangeable / 492 echousage item 3 Response Message interchangeable / 399 commit-empty-echo bundled interchangeable、Echo 请求 Message 是要回显的字符串 是不是 Echo request Message is Flush interchangeable / 394 echo-message-is-flush interchangeable / 374 flush bundled interchangeable / 671 flushusage-notechoqueued interchangeable、string to echo back / 填了 Message 是不是 filled Message means echoed interchangeable / 676 echousage-notdone interchangeable / 673 flushusage-notimmediatesync interchangeable。可以跳过「看见 Request Message string to echo back 就已经 Response Message interchangeable / 就已经 Echo Message 是 Flush interchangeable / 就已经填了 Message 就代表已经回显 interchangeable」。不要另写怎样写 Echo。492 echousage vs flush bundled unbundling 在本页 item 2 完成；续 [`worked-example-echousage-notdone-vs-bundled.md`](worked-example-echousage-notdone-vs-bundled.md)（不变量 676 item 3）。

## 本页不抄

- 怎样写 Echo、怎样填 Message、怎样测 client/server。
- Echo Usage 正式三事 bundled。那是不变量 492。
- Echo a string to test implementation not Flush flush queue。那是不变量 492 item 1 余量 / 674。
- Response Message the input string not already test done。那是不变量 492 item 3 余量 / 676。
- Echo 请求 Message 就已经是 Flush bundled。那是不变量 394。
- Flush 要把客户端排队的消息冲到服务端 bundled。那是不变量 374。
- Flush Usage 正式三事 bundled。那是不变量 493。
- Commit 空请求 bundled。那是不变量 399。
