# 模式：把 Echo Request Message string to echo back not Response Message / not Echo request Message is Flush / not filled Message means echoed 正式三事（492 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Echo Request / Response。  
**例**：[Echo Request Message string to echo back not Response Message ≠ bundled（492）](../../tracks/implementation/worked-example-echousage-notreqresp-vs-bundled.md)。

## 三个名字

1. **Request Message string to echo back 不是 Response Message：** 看见 Echo 请求 Message 是要回显的字符串，不是已经 Response Message 是入参那串 interchangeable，不是 492 echousage item 3 Response Message interchangeable / 399 commit-empty-echo bundled interchangeable / 675 echousage-notreqresp interchangeable。

2. **Echo 请求 Message 是要回显的字符串 不是 Echo request Message is Flush：** 看见 Request Message string to echo back，不是已经 Echo 请求 Message 就已经是 Flush interchangeable，不是 394 echo-message-is-flush interchangeable / 374 flush bundled interchangeable / 671 flushusage-notechoqueued interchangeable。

3. **string to echo back / 填了 Message 不是 filled Message means echoed：** 看见 Echo 请求 Message 是要回显的字符串，不是已经填了 Message 就代表已经回显 interchangeable，不是 676 echousage-notdone interchangeable / 492 echousage item 3 Response Message interchangeable / 673 flushusage-notimmediatesync interchangeable。

官方把 Echo Request 请求栏、Echo Response 回包栏、Echo 请求 Message 就已经是 Flush（394）写成三个名字。把它们叫成一个「看见 Request Message string to echo back 就已经 Response Message interchangeable / 就已经 Echo Message 是 Flush interchangeable / 就已经填了 Message 就代表已经回显 interchangeable」，会把 not Response Message、not Echo request Message is Flush、not filled Message means echoed 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Echo Request Message string to echo back not Response Message / not Echo request Message is Flush / not filled Message means echoed 正式三事（492 余量），先数清问的是 Request Message string to echo back 是不是 Response Message / 492 item 3 / 399，是不是 Echo 请求 Message 是不是 Echo request Message is Flush / 394 / 374 / 671，还是 string to echo back / 填了 Message 是不是 filled Message means echoed / 676 / 673，再决定要不要同一次发布。492 echousage vs flush bundled unbundling 在本页 item 2 完成。
