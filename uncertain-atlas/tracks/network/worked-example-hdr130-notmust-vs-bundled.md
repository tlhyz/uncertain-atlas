# 例：看见你发了 sendheaders 不是对等节点已经改用头通告；看见协议版本够了不是已经在发；看见许可不是已经照做

**层次**：网络 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-130](https://github.com/bitcoin/bips/blob/master/bip-0130.mediawiki)（Deployed, Peer Services）。  
**对应课文**：[L3.4](../../courses/level-03-bitcoin/L03-M04-network-and-eclipse.md)、[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：index/03 共识行、Ethereum 行、M5.4、L5.1、L5.4、05b。本页是「BIP-130 permission not already must / not already sending / not already forever 正式三事（247 余量）/ not 1236 hdr130-notmust interchangeable / not 247 sendheaders-vs-have bundled interchangeable」，不是 sendheaders bundled（247），也不是宣布就已经收到（246），也不是后继地址偏好就已经只收后继格式（36）。不要另写 怎样扣头、怎样用假头围住对等节点、怎样只通告哈希卡住中间块。

## 官方三件事

1. **看见你发了 sendheaders / 看见协议版本够了 这份对象 is not already 对等节点已经改用头通告 interchangeable，也不是已经 sendheaders bundled（247） interchangeable / 1236 hdr130-notmust interchangeable / 1235 hdr130-notswitch interchangeable，也不是已经 BIP-130 permission not already must / not already sending / not already forever 正式三事 bundled（247 item 2 余量） interchangeable / 247 sendheaders item 2 interchangeable。**  
   官方写：收到这条消息之后，节点被许可、但不是被要求，用新块的头（以及它认为对等节点还缺的、好让这块接得上的头）来通告。支持本页是可选的；实现还可以另加约束，例如只在刚连上后不久才理会这条消息。能不能用这条消息，靠协议版本发现。看见你发了 sendheaders，不是对等节点已经改用头通告。看见协议版本够了，不是已经在发、也不是已经在遵守。

2. **看见协议版本够了 / 看见你发了 sendheaders / 这份对象 is not already 已经在发 interchangeable，也不是已经 sendheaders bundled（247） interchangeable / 1236 hdr130-notmust interchangeable / 1237 hdr130-nothave interchangeable，也不是已经 addrv2-pref interchangeable / 246 addrv2-pref interchangeable。**  
   官方把协议版本够了和已经在发写成两件。看见协议版本够了，不是已经在发。

3. **看见许可 / 看见你发了 sendheaders / 这份对象 is not already 已经照做 interchangeable，也不是已经 sendheaders bundled（247） interchangeable / 1236 hdr130-notmust interchangeable / 1235 hdr130-notswitch interchangeable，也不是已经 announce-received interchangeable / 36 announce-received interchangeable。**  
   官方把许可和必须改、刚连上才理会和已经永远理会写成两件。看见许可，不是已经照做。

协议版本号、空消息编码、头定位器做法是规范与实现里的数字和算法，本页不抄。不要另写 怎样扣头、怎样用假头围住对等节点、怎样只通告哈希卡住中间块。

## 官方为什么这样拆

- **许可 不是已经照做：官方把「可以改用头通告」和「必须改」写成两件事。**
- **协议版本够了 不是已经在发：能不能用靠协议版本发现，不是已经在发、已经在遵守。**
- **刚连上才理会 不是已经永远理会：实现还可以另加约束。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 对等节点已经改用头通告 | 不是对等节点已经改用头通告 | 不是已经addrv2-pref（246） |
| 已经在发 | 不是已经在发 | 不是已经announce-received（36） |
| 已经照做 | 不是已经照做 | 不是已经1235 hdr130-notswitch |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-130 permission not already must / not already sending / not already forever 正式三事（247 余量），必须分开是不是对等节点已经改用头通告、是不是已经在发、是不是已经照做。可以跳过「看见发了 sendheaders 就已经有新块」。不要另写 怎样扣头、怎样用假头围住对等节点、怎样只通告哈希卡住中间块。247 sendheaders vs have bundled unbundling 在本页 item 2 续；续 [`worked-example-hdr130-nothave-vs-bundled.md`](worked-example-hdr130-nothave-vs-bundled.md)（不变量 1237 item 3）。

## 本页不抄

- 协议版本号、空消息字段、头定位器做法、一次带头个数。
- 怎样扣头、怎样用假头围住对等节点、怎样只通告哈希卡住中间块。
