# 反模式：把 Echo Usage 正式三事卖成 Flush / 入参字段 interchangeable / 已经刷完

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Echo a string to test implementation ≠ 已经 Flush](../../tracks/implementation/worked-example-echousage-vs-flush.md)。

## 卖法

- 「看见 Echo a string to test an ABCI client/server implementation / Echo 用来测实现 就已经 Flush 那种把排队冲到服务端 / 已经送到 / Commit 空请求 bundled interchangeable。」
- 「看见 Request Message string to echo back / Echo 请求 Message 是要回显的字符串 就已经 Response Message the input string interchangeable / 已经是 Flush / 已经填了 Message 就代表已经回显。」
- 「看见 Response Message the input string / Echo 回包 Message 是入参那串 就已经 Echo 用来测实现就已经刷完 / 已经 Request Message 字段 interchangeable / Flush 回包回来就算同步。」

## 为什么错

官方把 Echo Usage、Echo Request Message、Echo Response Message 写成三件独立的实现事。把它们卖成 Flush / 入参字段 interchangeable / 已经刷完，会把测实现、请求栏、回包栏三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Echo Usage，必须分开 Echo a string to test implementation、Request Message string to echo back、Response Message the input string 三个名字，不要把它们卖成 Flush / 入参字段 interchangeable / 已经刷完。

## 和相邻反模式

- [flushusage-sold-as-echo](flushusage-sold-as-echo.md) 是 Flush Usage 正式三事就等于 Echo 测 implementation，不是本页 Echo 测实现专用边界。
- [commitnoparam-sold-as-persist](commitnoparam-sold-as-persist.md) 是 Commit 空请求 bundled Echo 全段，不是本页 Echo Usage 专用三事。
- [flush-sold-as-sent](flush-sold-as-sent.md) 是 Flush 就等于已经送到，不是本页 Echo 测实现专用边界。
