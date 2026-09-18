# 例：看见通告了 feature 不是已经启用；看见一条 feature 通告不是已经理解；看见不认识的 featureid 不是已经非法

**层次**：网络 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-434](https://github.com/bitcoin/bips/blob/master/bip-0434.md)（Complete, Peer Services）。  
**对应课文**：[L3.4](../../courses/level-03-bitcoin/L03-M04-network-and-eclipse.md)、[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：Ethereum 行、L5.1、05b、M5.4、L5.4、03 共识。本页是「BIP-434 feature-adv not already enabled / not already understood / not already illegal 正式三事（259 余量）/ not 1245 feat434-noton interchangeable / not 259 feature-vs-enabled bundled interchangeable」，不是 feature bundled（259），也不是发了 sendheaders 就已经有块（248），也不是停交易转发就已经终身只传块（246）。不要另写 怎样按功能标识认人、怎样靠多开功能通告做日蚀、怎样在 verack 之后强插协商。

## 官方三件事

1. **看见通告了 feature / 看见一条 feature 通告 这份对象 is not already 已经启用 interchangeable，也不是已经 feature bundled（259） interchangeable / 1245 feat434-noton interchangeable / 1244 feat434-notver interchangeable，也不是已经 BIP-434 feature-adv not already enabled / not already understood / not already illegal 正式三事 bundled（259 item 2 余量） interchangeable / 259 feature item 2 interchangeable。**  
   官方写：实现本页的节点必须忽略自己不支持的 featureid，只要载荷符合本页要求。基于本页的功能规范必须禁止：对等节点没通过本页表示支持，就在 verack 之后发该功能引入的消息。看见一条 feature 通告，不是已经启用，也不是已经理解，也不是已经可以发该功能的消息。看见不认识的 featureid，不是已经非法，也不是已经必须断开。

2. **看见一条 feature 通告 / 看见通告了 feature / 这份对象 is not already 已经理解 interchangeable，也不是已经 feature bundled（259） interchangeable / 1245 feat434-noton interchangeable / 1246 feat434-notlate interchangeable，也不是已经 wtxidrelay-have interchangeable / 248 wtxidrelay-have interchangeable。**  
   官方把通告和已经理解写成两件。看见一条 feature 通告，不是已经理解。

3. **看见不认识的 featureid / 看见通告了 feature / 这份对象 is not already 已经非法 interchangeable，也不是已经 feature bundled（259） interchangeable / 1245 feat434-noton interchangeable / 1244 feat434-notver interchangeable，也不是已经 addrv2-reachable interchangeable / 246 addrv2-reachable interchangeable。**  
   官方把不认识的 featureid 和已经非法、已经必须断开写成两件。看见不认识的 featureid，不是已经非法。

协议版本号、一字节类型、长度上下限是规范里的取值，本页不抄。不要另写 怎样按功能标识认人、怎样靠多开功能通告做日蚀、怎样在 verack 之后强插协商。

## 官方为什么这样拆

- **通告 不是已经启用：官方要求忽略不支持的标识，并禁止没通告就发该功能的消息。**
- **一条 feature 通告 不是已经理解：官方把必须忽略不支持的标识写成独立要求。**
- **不认识的 featureid 不是已经非法：官方写只要载荷符合本页要求就必须忽略，不是已经必须断开。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经启用 | 不是已经启用 | 不是已经wtxidrelay-have（248） |
| 已经理解 | 不是已经理解 | 不是已经addrv2-reachable（246） |
| 已经非法 | 不是已经非法 | 不是已经1244 feat434-notver |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-434 feature-adv not already enabled / not already understood / not already illegal 正式三事（259 余量），必须分开是不是已经启用、是不是已经理解、是不是已经非法。可以跳过「看见版本号够了就已经会这项功能」。不要另写 怎样按功能标识认人、怎样靠多开功能通告做日蚀、怎样在 verack 之后强插协商。259 feature vs enabled bundled unbundling 在本页 item 2 续；续 [`worked-example-feat434-notlate-vs-bundled.md`](worked-example-feat434-notlate-vs-bundled.md)（不变量 1246 item 3）。

## 本页不抄

- 协议版本号、一字节消息类型、标识长度上下限、载荷字节上限。
- 怎样按功能标识认人、怎样靠多开功能通告做日蚀、怎样在 verack 之后强插协商。
