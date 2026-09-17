# 反模式：把 Echo Request Message string to echo back not Response Message / not Echo request Message is Flush / not filled Message means echoed 正式三事（492 余量）说成已经 Response Message / 已经 Echo Message 是 Flush / 已经填了 Message 就代表已经回显

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Echo Request Message string to echo back not Response Message ≠ bundled（492）](../../tracks/implementation/worked-example-echousage-notreqresp-vs-bundled.md)。

## 卖法

把 Request `Message (string)`: A string to echo back / Echo 请求 Message 是要回显的字符串 写成已经 Response Message the input string interchangeable / 492 echousage item 3 Response Message interchangeable / 399 commit-empty-echo bundled interchangeable / 已经 Echo 回包 Message 是入参那串 interchangeable；把 Request Message string to echo back 写成已经 Echo 请求 Message 就已经是 Flush interchangeable / 394 echo-message-is-flush interchangeable / 374 flush bundled interchangeable / 493 flushusage-vs-echo interchangeable / 671 flushusage-notechoqueued interchangeable / 已经 Echo Message 是 Flush interchangeable；把 string to echo back / 填了 Message 写成已经填了 Message 就代表已经回显 interchangeable / 已经 Response 侧 the input string 就代表请求已经交差 interchangeable / 676 echousage-notdone interchangeable / 673 flushusage-notimmediatesync interchangeable，或已经和 492 echousage-vs-flush bundled / echousage-sold-as-flush interchangeable / 675 echousage-notreqresp interchangeable。

## 为什么错

官方把 Echo Request 请求栏、Echo Response 回包栏、Echo 请求 Message 就已经是 Flush（394）写成三件独立的实现事。把它们卖成 Response Message interchangeable / Echo request Message is Flush interchangeable / filled Message means echoed interchangeable，会把 not Response Message、not Echo request Message is Flush、not filled Message means echoed 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Echo Request Message string to echo back not Response Message / not Echo request Message is Flush / not filled Message means echoed 正式三事（492 余量），必须分开 not Response Message、not Echo request Message is Flush、not filled Message means echoed 三件事，不要和 492 / 674 / 676 / 394 / 374 / 399 / 493 / 671 / 672 / 673 糊成一句。

## 和相邻反模式

- [echousage-notflush-sold-as-bundled](echousage-notflush-sold-as-bundled.md) 是 Echo Usage Echo a string to test implementation 单句边界（674 item 1），不是本页 Request Message 请求栏边界。
- [echousage-sold-as-flush](echousage-sold-as-flush.md) 是 Echo Usage 正式三事 bundled 全段，不是本页 item 2 Request vs Response 单句边界。
- [flushusage-sold-as-echo](flushusage-sold-as-echo.md) 是 Flush Usage 正式三事 bundled 全段，不是本页 Echo Request Message vs Flush 边界。
