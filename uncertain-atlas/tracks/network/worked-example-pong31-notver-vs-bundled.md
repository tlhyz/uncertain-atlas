# 例：看见协议版本够了不是已经会带 nonce 的 ping；看见协议版本够了不是对端已经会回 pong；看见协议版本够了不是本页已经并进后来的功能协商

**层次**：网络 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-31](https://github.com/bitcoin/bips/blob/master/bip-0031.mediawiki)（Deployed, Peer Services）。  
**对应课文**：[L3.4](../../courses/level-03-bitcoin/L03-M04-network-and-eclipse.md)、[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：Ethereum 行、L5.1、05b、M5.4、L5.4、03 共识。本页是「BIP-31 version-enough not already nonce-ping / not already will-pong / not already merged-feature 正式三事（262 余量）/ not 1268 pong31-notver interchangeable / not 262 pong-vs-live bundled interchangeable」，不是 pong bundled（262），也不是已经 feature-enabled（259），也不是已经 sendheaders-have（247）。不要另写 怎样叠许多 ping、怎样靠假 pong 认人、怎样用往返选人做日蚀。

## 官方三件事

1. **看见协议版本够了 / 看见协议版本够了 这份对象 is not already 已经会带 nonce 的 ping interchangeable，也不是已经 pong bundled（262） interchangeable / 1268 pong31-notver interchangeable / 1269 pong31-notmatch interchangeable，也不是已经 BIP-31 version-enough not already nonce-ping / not already will-pong / not already merged-feature 正式三事 bundled（262 item 1 余量） interchangeable / 262 pong item 1 interchangeable。**  
   官方写：谈妥的协议版本够高时，ping 必须带一个 nonce。必须自己抬版本才能加入本页。旧版本的客户端不被指望在 ping 里放 nonce，也不会被送来 pong。看见协议版本够了，不是已经发了带 nonce 的 ping，也不是对端已经会回 pong，也不是本页已经并进后来的功能协商。

2. **看见协议版本够了 / 看见协议版本够了 / 这份对象 is not already 对端已经会回 pong interchangeable，也不是已经 pong bundled（262） interchangeable / 1268 pong31-notver interchangeable / 1270 pong31-notlive interchangeable，也不是已经 feature-enabled interchangeable / 259 feature-enabled interchangeable。**  
   官方把协议版本够了和对端已经会回 pong 写成两件。看见协议版本够了，不是对端已经会回 pong。

3. **看见协议版本够了 / 看见协议版本够了 / 这份对象 is not already 本页已经并进后来的功能协商 interchangeable，也不是已经 pong bundled（262） interchangeable / 1268 pong31-notver interchangeable / 1269 pong31-notmatch interchangeable，也不是已经 sendheaders-have interchangeable / 247 sendheaders-have interchangeable。**  
   官方把协议版本够了和本页已经并进后来的功能协商写成两件。看见协议版本够了，不是本页已经并进后来的功能协商。

协议版本门槛、nonce 宽度是规范里的取值，本页不抄。不要另写 怎样叠许多 ping、怎样靠假 pong 认人、怎样用往返选人做日蚀。

## 官方为什么这样拆

- **版本号 不是已经本页：官方把加入写成必须自己抬版本；旧客户端不会被送来 pong。**
- **版本够了 不是对端已经会回 pong：官方写旧版本的客户端也不会被送来 pong。**
- **版本够了 不是已经并进功能协商：官方只把本页钉在版本门槛，不是已经并进 434。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经会带 nonce 的 ping | 不是已经会带 nonce 的 ping | 不是已经feature-enabled（259） |
| 对端已经会回 pong | 不是对端已经会回 pong | 不是已经sendheaders-have（247） |
| 本页已经并进后来的功能协商 | 不是本页已经并进后来的功能协商 | 不是已经1269 pong31-notmatch |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-31 version-enough not already nonce-ping / not already will-pong / not already merged-feature 正式三事（262 余量），必须分开是不是已经会带 nonce 的 ping、是不是对端已经会回 pong、是不是本页已经并进后来的功能协商。可以跳过「看见回了 ping 就已经还活着」。不要另写 怎样叠许多 ping、怎样靠假 pong 认人、怎样用往返选人做日蚀。262 pong vs live bundled unbundling 在本页 item 1 启动；续 [`worked-example-pong31-notmatch-vs-bundled.md`](worked-example-pong31-notmatch-vs-bundled.md)（不变量 1269 item 2）。

## 本页不抄

- 协议版本门槛数字、nonce 整数宽度、消息字段布局。
- 怎样叠许多 ping、怎样靠假 pong 认人、怎样用往返选人做日蚀。
