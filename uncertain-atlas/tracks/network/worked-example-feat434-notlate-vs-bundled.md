# 例：看见 verack 之后才来的 feature 不是已经是本页协商；看见 verack 之后才来的 feature 不是已经启用；看见忽略了不认识的消息不是已经实现本页

**层次**：网络 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-434](https://github.com/bitcoin/bips/blob/master/bip-0434.md)（Complete, Peer Services）。  
**对应课文**：[L3.4](../../courses/level-03-bitcoin/L03-M04-network-and-eclipse.md)、[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：Ethereum 行、L5.1、05b、M5.4、L5.4、03 共识。本页是「BIP-434 after-verack not already this-handshake / not already enabled / not already implemented 正式三事（259 余量）/ not 1246 feat434-notlate interchangeable / not 259 feature-vs-enabled bundled interchangeable」，不是 feature bundled（259），也不是发了 sendheaders 就已经有块（242），也不是停交易转发就已经终身只传块（245）。不要另写 怎样按功能标识认人、怎样靠多开功能通告做日蚀、怎样在 verack 之后强插协商。

## 官方三件事

1. **看见verack 之后才来的 feature / 看见verack 之后才来的 feature 这份对象 is not already 已经是本页协商 interchangeable，也不是已经 feature bundled（259） interchangeable / 1246 feat434-notlate interchangeable / 1244 feat434-notver interchangeable，也不是已经 BIP-434 after-verack not already this-handshake / not already enabled / not already implemented 正式三事 bundled（259 item 3 余量） interchangeable / 259 feature item 3 interchangeable。**  
   官方写：必须接受 version 之后、verack 之前的 feature。自己发过 verack 之后，不得再发 feature。verack 之后收到的 feature 可以忽略，也可以因此断开。看见 verack 之后才来的 feature，不是已经是本页这种握手，也不是已经启用。看见忽略了不认识的消息，不是已经实现本页。

2. **看见verack 之后才来的 feature / 看见verack 之后才来的 feature / 这份对象 is not already 已经启用 interchangeable，也不是已经 feature bundled（259） interchangeable / 1246 feat434-notlate interchangeable / 1245 feat434-noton interchangeable，也不是已经 v2-private interchangeable / 242 v2-private interchangeable。**  
   官方把 verack 之后才来的 feature 和已经启用写成两件。看见 verack 之后才来的 feature，不是已经启用。

3. **看见忽略了不认识的消息 / 看见verack 之后才来的 feature / 这份对象 is not already 已经实现本页 interchangeable，也不是已经 feature bundled（259） interchangeable / 1246 feat434-notlate interchangeable / 1244 feat434-notver interchangeable，也不是已经 feefilter-reject interchangeable / 245 feefilter-reject interchangeable。**  
   官方把忽略不认识的消息和已经实现本页写成两件。看见忽略了不认识的消息，不是已经实现本页。

协议版本号、一字节类型、长度上下限是规范里的取值，本页不抄。不要另写 怎样按功能标识认人、怎样靠多开功能通告做日蚀、怎样在 verack 之后强插协商。

## 官方为什么这样拆

- **verack 之后 不是本页窗口：官方把协商窗钉在 version 与 verack 之间。**
- **verack 之后才来的 feature 不是已经启用：官方写收到可以忽略，也可以因此断开。**
- **忽略了不认识的消息 不是已经实现本页：官方把本页协商和随便忽略不认识的消息写成两件。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是本页协商 | 不是已经是本页协商 | 不是已经v2-private（242） |
| 已经启用 | 不是已经启用 | 不是已经feefilter-reject（245） |
| 已经实现本页 | 不是已经实现本页 | 不是已经1244 feat434-notver |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-434 after-verack not already this-handshake / not already enabled / not already implemented 正式三事（259 余量），必须分开是不是已经是本页协商、是不是已经启用、是不是已经实现本页。可以跳过「看见版本号够了就已经会这项功能」。不要另写 怎样按功能标识认人、怎样靠多开功能通告做日蚀、怎样在 verack 之后强插协商。259 feature vs enabled bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 协议版本号、一字节消息类型、标识长度上下限、载荷字节上限。
- 怎样按功能标识认人、怎样靠多开功能通告做日蚀、怎样在 verack 之后强插协商。
