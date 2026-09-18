# 例：看见建议关掉地址不是已经禁止传地址；看见发了本页不是已经断开；看见这条连接上还在传地址不是已经共识非法

**层次**：网络 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-338](https://github.com/bitcoin/bips/blob/master/bip-0338.mediawiki)（Closed, Peer Services）。  
**对应课文**：[L3.4](../../courses/level-03-bitcoin/L03-M04-network-and-eclipse.md)、[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：index/03 共识行、Ethereum 行、M5.4、L5.1、L5.4、05b。本页是「BIP-338 addr-suggest not already forbidden / not already disconnected / not already illegal 正式三事（256 余量）/ not 1243 dis338-notaddr interchangeable / not 256 disabletx-vs-lifetime bundled interchangeable」，不是 disabletx bundled（256），也不是费率过滤器就已经拒进池（246），也不是内存池查询就已经有那些交易（252）。不要另写 怎样按只传块连接认人、怎样靠多开只传块入口做日蚀、怎样用本页探测别人会不会断开。

## 官方三件事

1. **看见建议关掉地址 / 看见发了本页 这份对象 is not already 已经禁止传地址 interchangeable，也不是已经 disabletx bundled（256） interchangeable / 1243 dis338-notaddr interchangeable / 1241 dis338-notlife interchangeable，也不是已经 BIP-338 addr-suggest not already forbidden / not already disconnected / not already illegal 正式三事 bundled（256 item 3 余量） interchangeable / 256 disabletx item 3 interchangeable。**  
   官方写：发过或收过本页之后，建议不要再发地址、要地址、后继地址。关掉地址只是建议，不是必须，好留给以后单独谈地址。官方还写：节点可以决定不跟发了本页的人继续连，例如自己正要找会传交易的邻居。看见发了本页，不是已经没有地址，也不是已经断开。看见这条连接上还在传地址，不是已经共识非法，也不是已经不是只传块。

2. **看见发了本页 / 看见建议关掉地址 / 这份对象 is not already 已经断开 interchangeable，也不是已经 disabletx bundled（256） interchangeable / 1243 dis338-notaddr interchangeable / 1242 dis338-notcmpct interchangeable，也不是已经 addrv2-reachable interchangeable / 246 addrv2-reachable interchangeable。**  
   官方把可以因此断开和已经断开写成两件。看见发了本页，不是已经断开。

3. **看见这条连接上还在传地址 / 看见建议关掉地址 / 这份对象 is not already 已经共识非法 interchangeable，也不是已经 disabletx bundled（256） interchangeable / 1243 dis338-notaddr interchangeable / 1241 dis338-notlife interchangeable，也不是已经 bloom-retired interchangeable / 252 bloom-retired interchangeable。**  
   官方把还在传地址和已经共识非法写成两件。看见还在传地址，不是已经共识非法。

协议版本号、消息类型字面量是规范里的取值，本页不抄。不要另写 怎样按只传块连接认人、怎样靠多开只传块入口做日蚀、怎样用本页探测别人会不会断开。

## 官方为什么这样拆

- **建议关掉地址 不是已经禁止：官方把地址写成建议，好留给以后单独谈。**
- **发了本页 不是已经断开：官方写节点可以决定不继续连，不是已经断。**
- **还在传地址 不是已经共识非法：官方写关掉地址只是建议，不是必须。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经禁止传地址 | 不是已经禁止传地址 | 不是已经addrv2-reachable（246） |
| 已经断开 | 不是已经断开 | 不是已经bloom-retired（252） |
| 已经共识非法 | 不是已经共识非法 | 不是已经1241 dis338-notlife |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-338 addr-suggest not already forbidden / not already disconnected / not already illegal 正式三事（256 余量），必须分开是不是已经禁止传地址、是不是已经断开、是不是已经共识非法。可以跳过「看见版本里关掉转发就已经是终身只传块」。不要另写 怎样按只传块连接认人、怎样靠多开只传块入口做日蚀、怎样用本页探测别人会不会断开。256 disabletx vs lifetime bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 协议版本号、消息类型字面量、参考实现何时用版本字段冒充只传块。
- 怎样按只传块连接认人、怎样靠多开只传块入口做日蚀、怎样用本页探测别人会不会断开。
