# 例：看见协议版本够了不是已经支持某项功能；看见协议版本够了不是已经发了本页；看见版本够了不是旧绑版本功能已经并进本页

**层次**：网络 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-434](https://github.com/bitcoin/bips/blob/master/bip-0434.md)（Complete, Peer Services）。  
**对应课文**：[L3.4](../../courses/level-03-bitcoin/L03-M04-network-and-eclipse.md)、[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：Ethereum 行、L5.1、05b、M5.4、L5.4、03 共识。本页是「BIP-434 version-enough not already support / not already sent-page / not already merged-old 正式三事（259 余量）/ not 1244 feat434-notver interchangeable / not 259 feature-vs-enabled bundled interchangeable」，不是 feature bundled（259），也不是发了 sendheaders 就已经有块（247），也不是停交易转发就已经终身只传块（256）。不要另写 怎样按功能标识认人、怎样靠多开功能通告做日蚀、怎样在 verack 之后强插协商。

## 官方三件事

1. **看见协议版本够了 / 看见协议版本够了 这份对象 is not already 已经支持某项功能 interchangeable，也不是已经 feature bundled（259） interchangeable / 1244 feat434-notver interchangeable / 1245 feat434-noton interchangeable，也不是已经 BIP-434 version-enough not already support / not already sent-page / not already merged-old 正式三事 bundled（259 item 1 余量） interchangeable / 259 feature item 1 interchangeable。**  
   官方写：历史上新的对等改动绑在抬协议版本上，好让节点只跟会这项功能的人谈。跨实现协调版本号是不必要的负担。本页新增一种可复用的功能协商消息，以后的升级可以在交换 verack 之前谈妥，不必再协调改协议版本。实现本页的节点必须通告够高的协议版本，也不得向版本不够的对等节点发本页。看见协议版本够了，不是已经发了本页，也不是已经支持某一项具体功能，也不是以前那些各自绑版本的功能已经并进本页。

2. **看见协议版本够了 / 看见协议版本够了 / 这份对象 is not already 已经发了本页 interchangeable，也不是已经 feature bundled（259） interchangeable / 1244 feat434-notver interchangeable / 1246 feat434-notlate interchangeable，也不是已经 sendheaders-have interchangeable / 247 sendheaders-have interchangeable。**  
   官方把协议版本够了和已经发了本页写成两件。看见协议版本够了，不是已经发了本页。

3. **看见版本够了 / 看见协议版本够了 / 这份对象 is not already 以前那些各自绑版本的功能已经并进本页 interchangeable，也不是已经 feature bundled（259） interchangeable / 1244 feat434-notver interchangeable / 1245 feat434-noton interchangeable，也不是已经 disabletx-life interchangeable / 256 disabletx-life interchangeable。**  
   官方把本页写成以后升级不必再协调改协议版本，不是旧绑版本功能已经并进本页。看见版本够了，不是以前那些各自绑版本的功能已经并进本页。

协议版本号、一字节类型、长度上下限是规范里的取值，本页不抄。不要另写 怎样按功能标识认人、怎样靠多开功能通告做日蚀、怎样在 verack 之后强插协商。

## 官方为什么这样拆

- **版本号 不是已经支持：官方把「不必再协调改协议版本」写成动机。看见版本够了，不是已经会这项功能。**
- **协议版本够了 不是已经发了本页：官方写实现本页的节点必须通告够高的协议版本，也不得向版本不够的人发本页。**
- **版本够了 不是旧绑版本功能已经并进本页：官方写本页是以后升级用的可复用协商，不是已经把旧功能并进来。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经支持某项功能 | 不是已经支持某项功能 | 不是已经sendheaders-have（247） |
| 已经发了本页 | 不是已经发了本页 | 不是已经disabletx-life（256） |
| 以前那些各自绑版本的功能已经并进本页 | 不是以前那些各自绑版本的功能已经并进本页 | 不是已经1245 feat434-noton |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-434 version-enough not already support / not already sent-page / not already merged-old 正式三事（259 余量），必须分开是不是已经支持某项功能、是不是已经发了本页、是不是以前那些各自绑版本的功能已经并进本页。可以跳过「看见版本号够了就已经会这项功能」。不要另写 怎样按功能标识认人、怎样靠多开功能通告做日蚀、怎样在 verack 之后强插协商。259 feature vs enabled bundled unbundling 在本页 item 1 启动；续 [`worked-example-feat434-noton-vs-bundled.md`](worked-example-feat434-noton-vs-bundled.md)（不变量 1245 item 2）。

## 本页不抄

- 协议版本号、一字节消息类型、标识长度上下限、载荷字节上限。
- 怎样按功能标识认人、怎样靠多开功能通告做日蚀、怎样在 verack 之后强插协商。
