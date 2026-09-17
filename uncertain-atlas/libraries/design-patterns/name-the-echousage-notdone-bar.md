# 模式：把 Echo Response Message the input string not Echo Usage test already done / not Request Message string to echo back / not Flush sync response 正式三事（492 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Echo Response / Usage。  
**例**：[Echo Response Message the input string not Echo Usage test already done ≠ bundled（492）](../../tracks/implementation/worked-example-echousage-notdone-vs-bundled.md)。

## 三个名字

1. **Response Message the input string 不是 Echo Usage test already done：** 看见 Echo 回包 Message 是入参那串，不是已经 Echo 用来测实现就已经刷完 interchangeable，不是 674 echousage-notflush interchangeable / 399 commit-empty-echo item 3 interchangeable / 676 echousage-notdone interchangeable。

2. **Echo 回包 Message 是入参那串 不是 Request Message string to echo back：** 看见 Response Message the input string，不是已经 Request Message 是要回显的字符串 interchangeable，不是 675 echousage-notreqresp interchangeable / 492 echousage item 2 Request Message interchangeable / 399 commit-empty-echo item 2 interchangeable。

3. **the input string / 回了 Message 不是 Flush sync response：** 看见 Echo 回包 Message 是入参那串，不是已经 Flush 回包回来就算这次同步 interchangeable，不是 673 flushusage-notimmediatesync interchangeable / 374 flush-vs-sent interchangeable / 493 flushusage item 3 immediately sync interchangeable。

官方把 Echo Response 回包栏、Echo Usage 测实现交差、Flush 同步回包（673）写成三个名字。把它们叫成一个「看见 Response Message the input string 就已经 Echo Usage test already done interchangeable / 就已经 Request Message interchangeable / 就已经 Flush sync response interchangeable」，会把 not Echo Usage test already done、not Request Message string to echo back、not Flush sync response 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Echo Response Message the input string not Echo Usage test already done / not Request Message string to echo back / not Flush sync response 正式三事（492 余量），先数清问的是 Response Message the input string 是不是 Echo Usage test already done / 674 / 399 item 3，是不是 Echo 回包 Message 是不是 Request Message string to echo back / 675 / 399 item 2，还是 the input string 是不是 Flush sync response / 673 / 374 / 493 item 3，再决定要不要同一次发布。492 echousage vs flush bundled unbundling 在本页 item 3 完成。
