# 反模式：把 Echo Response Message the input string not Echo Usage test already done / not Request Message string to echo back / not Flush sync response 正式三事（492 余量）说成已经 Echo Usage test already done / 已经 Request Message / 已经 Flush sync response

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Echo Response Message the input string not Echo Usage test already done ≠ bundled（492）](../../tracks/implementation/worked-example-echousage-notdone-vs-bundled.md)。

## 卖法

把 Response `Message (string)`: The input string / Echo 回包 Message 是入参那串 写成已经 Echo 用来测实现就已经刷完 interchangeable / 674 echousage-notflush interchangeable / 399 commit-empty-echo item 3 interchangeable / 399 commit-empty-echo bundled interchangeable / 335 finpersist interchangeable / 已经测实现就已经交差 interchangeable；把 Response Message the input string 写成已经 Request Message string to echo back interchangeable / 675 echousage-notreqresp interchangeable / 492 echousage item 2 Request Message interchangeable / 399 commit-empty-echo item 2 interchangeable / 已经 Echo 请求 Message 是要回显的字符串 interchangeable；把 the input string / 回了 Message 写成已经 Flush 回包回来就算这次同步 interchangeable / 673 flushusage-notimmediatesync interchangeable / 374 flush-vs-sent interchangeable / 493 flushusage item 3 immediately sync interchangeable / 已经送到 interchangeable，或已经和 492 echousage-vs-flush bundled / echousage-sold-as-flush interchangeable / 676 echousage-notdone interchangeable。

## 为什么错

官方把 Echo Response 回包栏、Echo Usage 测实现交差、Request Message string to echo back、Flush 同步回包（673）写成三件独立的实现事。把它们卖成 Echo Usage test already done interchangeable / Request Message interchangeable / Flush sync response interchangeable，会把 not Echo Usage test already done、not Request Message string to echo back、not Flush sync response 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Echo Response Message the input string not Echo Usage test already done / not Request Message string to echo back / not Flush sync response 正式三事（492 余量），必须分开 not Echo Usage test already done、not Request Message string to echo back、not Flush sync response 三件事，不要和 492 / 674 / 675 / 399 / 673 / 374 / 493 / 671 / 672 / 394 糊成一句。

## 和相邻反模式

- [echousage-notreqresp-sold-as-bundled](echousage-notreqresp-sold-as-bundled.md) 是 Echo Request Message string to echo back 单句边界（675 item 2），不是本页 Response Message 回包栏边界。
- [echousage-notflush-sold-as-bundled](echousage-notflush-sold-as-bundled.md) 是 Echo Usage Echo a string to test implementation 单句边界（674 item 1），不是本页 Response the input string vs Usage test already done 边界。
- [flushusage-notimmediatesync-sold-as-bundled](flushusage-notimmediatesync-sold-as-bundled.md) 是 Flush Usage immediately sync Flush response 单句边界（673），不是本页 Echo Response Message 回包栏边界。
