# 反模式：把 Flush Usage Called periodically ensure async requests actually sent not Echo test / not one connection four gates / not Flush bundled item 2 正式三事（493 余量）说成已经 Echo 测 implementation / 已经四门 / 已经 Flush bundled 第二件事

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Flush Usage Called periodically ensure async requests actually sent not Echo test ≠ bundled（493）](../../tracks/implementation/worked-example-flushusage-notperiodicasync-vs-bundled.md)。

## 卖法

把 Called periodically to ensure async requests are actually sent 写成已经 Echo a string to test an ABCI client/server implementation interchangeable / 492 echousage-vs-flush interchangeable / 已经 Echo 用来测 client/server implementation interchangeable / 已经 Echo 测实现 interchangeable；把 periodically / async requests actually sent / 定期 Flush 让异步请求真发出去 写成已经一条连接就已经是四门 interchangeable / 307 abci-conn-vs-gates interchangeable / 已经同进程四门 interchangeable / 已经 ABCI 连接就是四门 interchangeable；把 ensure async requests are actually sent 写成已经 Flush 要把客户端排队的消息冲到服务端 bundled 第二件事 interchangeable / 374 flush bundled interchangeable / 374 flush-vs-sent interchangeable / 已经送到 interchangeable / 已经交差 interchangeable，或已经和 493 flushusage-vs-echo bundled / flushusage-sold-as-echo interchangeable / 672 flushusage-notperiodicasync interchangeable。

## 为什么错

官方把 Flush Usage periodically ensure async requests 单句、Echo Usage 测实现（492）、一条连接四门（307）、Flush bundled 第二件事（374）写成三件独立的实现事。把它们卖成 Echo 测 implementation interchangeable / 四门 interchangeable / Flush bundled 第二件事 interchangeable，会把 not Echo test、not one connection four gates、not Flush bundled item 2 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Flush Usage Called periodically ensure async requests actually sent not Echo test / not one connection four gates / not Flush bundled item 2 正式三事（493 余量），必须分开 not Echo test、not one connection four gates、not Flush bundled item 2 三件事，不要和 493 / 492 / 307 / 374 / 671 / 673 / 309 / 310 糊成一句。

## 和相邻反模式

- [flushusage-sold-as-echo](flushusage-sold-as-echo.md) 是 Flush Usage 正式三事 bundled 全段，不是本页 item 2 periodically async 单句边界。
- [flushusage-notechoqueued-sold-as-bundled](flushusage-notechoqueued-sold-as-bundled.md) 是 493 item 1 Signals messages queued 单句边界，不是本页 item 2 periodically async 单句边界。
- [flush-sold-as-sent](flush-sold-as-sent.md) 是 Flush bundled 就等于已经送到，不是本页 periodically async vs Flush bundled item 2 单句边界。
