# 例：看见版本里关掉了转发不是已经终身只传块；看见协议版本够了不是已经实现本页；看见本页状态是关闭不是网上已经默认这样谈

**层次**：网络 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-338](https://github.com/bitcoin/bips/blob/master/bip-0338.mediawiki)（Closed, Peer Services）。  
**对应课文**：[L3.4](../../courses/level-03-bitcoin/L03-M04-network-and-eclipse.md)、[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：index/03 共识行、Ethereum 行、M5.4、L5.1、L5.4、05b。本页是「BIP-338 version-flag not already lifetime / not already implemented / not already default-on 正式三事（256 余量）/ not 1241 dis338-notlife interchangeable / not 256 disabletx-vs-lifetime bundled interchangeable」，不是 disabletx bundled（256），也不是费率过滤器就已经拒进池（245），也不是内存池查询就已经有那些交易（253）。不要另写 怎样按只传块连接认人、怎样靠多开只传块入口做日蚀、怎样用本页探测别人会不会断开。

## 官方三件事

1. **看见版本里关掉了转发 / 看见协议版本够了 这份对象 is not already 已经终身只传块 interchangeable，也不是已经 disabletx bundled（256） interchangeable / 1241 dis338-notlife interchangeable / 1242 dis338-notcmpct interchangeable，也不是已经 BIP-338 version-flag not already lifetime / not already implemented / not already default-on 正式三事 bundled（256 item 1 余量） interchangeable / 256 disabletx item 1 interchangeable。**  
   官方写：版本消息里的交易转发字段不是这条连接一辈子的设定。收进站的一方因此分不清对方以后还会不会再打开转发，也分不清对方会不会丢掉地址。本页新增一种可选的空消息，在应答版本之后、应答完成之前发出，用来标明这条连接终身不拿来传交易。官方还写：版本里若省略了该字段、或把它打开，就不得再发本页这条消息。看见版本里关掉了转发，不是已经发了本页，也不是已经终身只传块。看见协议版本够了，不是已经实现本页。看见本页状态是关闭，不是网上已经默认这样谈。

2. **看见协议版本够了 / 看见版本里关掉了转发 / 这份对象 is not already 已经实现本页 interchangeable，也不是已经 disabletx bundled（256） interchangeable / 1241 dis338-notlife interchangeable / 1243 dis338-notaddr interchangeable，也不是已经 feefilter-reject interchangeable / 245 feefilter-reject interchangeable。**  
   官方把协议版本够了和已经实现本页写成两件。看见协议版本够了，不是已经实现本页。

3. **看见本页状态是关闭 / 看见版本里关掉了转发 / 这份对象 is not already 网上已经默认这样谈 interchangeable，也不是已经 disabletx bundled（256） interchangeable / 1241 dis338-notlife interchangeable / 1242 dis338-notcmpct interchangeable，也不是已经 mempool-dump interchangeable / 253 mempool-dump interchangeable。**  
   官方把本页状态是关闭和网上已经默认这样谈写成两件。看见关闭，不是已经在主网默认打开。

协议版本号、消息类型字面量是规范里的取值，本页不抄。不要另写 怎样按只传块连接认人、怎样靠多开只传块入口做日蚀、怎样用本页探测别人会不会断开。

## 官方为什么这样拆

- **关掉转发 不是已经终身：官方把版本字段写成可以再改。看见关掉，不是已经谈妥终身只传块。**
- **协议版本够了 不是已经实现本页：官方写本页是可选空消息。**
- **关闭状态 不是网上已经默认这样谈：官方写看见关闭不是已经默认打开。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经终身只传块 | 不是已经终身只传块 | 不是已经feefilter-reject（245） |
| 已经实现本页 | 不是已经实现本页 | 不是已经mempool-dump（253） |
| 网上已经默认这样谈 | 不是网上已经默认这样谈 | 不是已经1242 dis338-notcmpct |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-338 version-flag not already lifetime / not already implemented / not already default-on 正式三事（256 余量），必须分开是不是已经终身只传块、是不是已经实现本页、是不是网上已经默认这样谈。可以跳过「看见版本里关掉转发就已经是终身只传块」。不要另写 怎样按只传块连接认人、怎样靠多开只传块入口做日蚀、怎样用本页探测别人会不会断开。256 disabletx vs lifetime bundled unbundling 在本页 item 1 启动；续 [`worked-example-dis338-notcmpct-vs-bundled.md`](worked-example-dis338-notcmpct-vs-bundled.md)（不变量 1242 item 2）。

## 本页不抄

- 协议版本号、消息类型字面量、参考实现何时用版本字段冒充只传块。
- 怎样按只传块连接认人、怎样靠多开只传块入口做日蚀、怎样用本页探测别人会不会断开。
