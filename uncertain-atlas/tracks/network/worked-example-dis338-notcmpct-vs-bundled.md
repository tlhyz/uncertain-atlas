# 例：看见发了本页不是已经没有紧凑块；看见发了本页不是交易消息已经共识非法；看见本页不是已经没有块

**层次**：网络 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-338](https://github.com/bitcoin/bips/blob/master/bip-0338.mediawiki)（Closed, Peer Services）。  
**对应课文**：[L3.4](../../courses/level-03-bitcoin/L03-M04-network-and-eclipse.md)、[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：index/03 共识行、Ethereum 行、M5.4、L5.1、L5.4、05b。本页是「BIP-338 disabletx not already no-compact / not already tx-illegal / not already no-block 正式三事（256 余量）/ not 1242 dis338-notcmpct interchangeable / not 256 disabletx-vs-lifetime bundled interchangeable」，不是 disabletx bundled（256），也不是费率过滤器就已经拒进池（36），也不是内存池查询就已经有那些交易（245）。不要另写 怎样按只传块连接认人、怎样靠多开只传块入口做日蚀、怎样用本页探测别人会不会断开。

## 官方三件事

1. **看见发了本页 / 看见发了本页 这份对象 is not already 已经没有紧凑块 interchangeable，也不是已经 disabletx bundled（256） interchangeable / 1242 dis338-notcmpct interchangeable / 1241 dis338-notlife interchangeable，也不是已经 BIP-338 disabletx not already no-compact / not already tx-illegal / not already no-block 正式三事 bundled（256 item 2 余量） interchangeable / 256 disabletx item 2 interchangeable。**  
   官方写：一旦自己发过或对方发过本页，就不得再向对方发交易库存、交易未找到、交易索取、布隆块索取、布隆过滤命令、费率过滤器、内存池查询、交易消息。官方还写：紧凑块那一套消息，包括要块交易和回块交易，在谈妥紧凑块的前提下仍允许。看见发了本页，不是那些交易消息已经共识非法，也不是费率过滤器 / 内存池查询 / 布隆已经退役。看见本页，不是已经没有块，也不是已经没有紧凑块。

2. **看见发了本页 / 看见发了本页 / 这份对象 is not already 那些交易消息已经共识非法 interchangeable，也不是已经 disabletx bundled（256） interchangeable / 1242 dis338-notcmpct interchangeable / 1243 dis338-notaddr interchangeable，也不是已经 compact-announce interchangeable / 36 compact-announce interchangeable。**  
   官方把不得再发交易类消息和那些消息已经共识非法写成两件。看见发了本页，不是那些交易消息已经共识非法。

3. **看见本页 / 看见发了本页 / 这份对象 is not already 已经没有块 interchangeable，也不是已经 disabletx bundled（256） interchangeable / 1242 dis338-notcmpct interchangeable / 1241 dis338-notlife interchangeable，也不是已经 feefilter-reject interchangeable / 245 feefilter-reject interchangeable。**  
   官方把停交易和已经没有块写成两件。看见本页，不是已经没有块。

协议版本号、消息类型字面量是规范里的取值，本页不抄。不要另写 怎样按只传块连接认人、怎样靠多开只传块入口做日蚀、怎样用本页探测别人会不会断开。

## 官方为什么这样拆

- **停交易 不是已经停块：官方把交易类消息写成不得再发，同时又写紧凑块仍允许。**
- **发了本页 不是交易消息已经共识非法：官方写的是这条连接上不得再发，不是那些 BIP 已经退役。**
- **本页 不是已经没有块：官方写紧凑块那一套在谈妥前提下仍允许。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经没有紧凑块 | 不是已经没有紧凑块 | 不是已经compact-announce（36） |
| 那些交易消息已经共识非法 | 不是那些交易消息已经共识非法 | 不是已经feefilter-reject（245） |
| 已经没有块 | 不是已经没有块 | 不是已经1241 dis338-notlife |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-338 disabletx not already no-compact / not already tx-illegal / not already no-block 正式三事（256 余量），必须分开是不是已经没有紧凑块、是不是那些交易消息已经共识非法、是不是已经没有块。可以跳过「看见版本里关掉转发就已经是终身只传块」。不要另写 怎样按只传块连接认人、怎样靠多开只传块入口做日蚀、怎样用本页探测别人会不会断开。256 disabletx vs lifetime bundled unbundling 在本页 item 2 续；续 [`worked-example-dis338-notaddr-vs-bundled.md`](worked-example-dis338-notaddr-vs-bundled.md)（不变量 1243 item 3）。

## 本页不抄

- 协议版本号、消息类型字面量、参考实现何时用版本字段冒充只传块。
- 怎样按只传块连接认人、怎样靠多开只传块入口做日蚀、怎样用本页探测别人会不会断开。
