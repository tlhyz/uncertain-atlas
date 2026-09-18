# 例：看见发了 sendheaders 不是已经改用头通告；看见发了偏好不是已经有那块；看见发了 sendheaders 不是头先同步已经做完

**层次**：网络 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-130](https://github.com/bitcoin/bips/blob/master/bip-0130.mediawiki)（Deployed, Peer Services）。  
**对应课文**：[L3.4](../../courses/level-03-bitcoin/L03-M04-network-and-eclipse.md)、[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：index/03 共识行、Ethereum 行、M5.4、L5.1、L5.4、05b。本页是「BIP-130 sendheaders not already switched / not already have-block / not already headers-first 正式三事（247 余量）/ not 1235 hdr130-notswitch interchangeable / not 247 sendheaders-vs-have bundled interchangeable」，不是 sendheaders bundled（247），也不是宣布就已经收到（36），也不是后继地址偏好就已经只收后继格式（246）。不要另写 怎样扣头、怎样用假头围住对等节点、怎样只通告哈希卡住中间块。

## 官方三件事

1. **看见发了 sendheaders / 看见发了偏好 这份对象 is not already 已经改用头通告 interchangeable，也不是已经 sendheaders bundled（247） interchangeable / 1235 hdr130-notswitch interchangeable / 1236 hdr130-notmust interchangeable，也不是已经 BIP-130 sendheaders not already switched / not already have-block / not already headers-first 正式三事 bundled（247 item 1 余量） interchangeable / 247 sendheaders item 1 interchangeable。**  
   官方写：新增一条空消息，表示这个节点更想用头消息收新块通告，而不是库存通告。官方还写：头先同步之后，块必须能接到一条合法头链才会被处理；于是通告常常先发库存哈希，对等节点再回头要头、再要块。看见发了 sendheaders，不是已经改用头通告，也不是已经有那块，也不是头先同步已经做完。

2. **看见发了偏好 / 看见发了 sendheaders / 这份对象 is not already 已经有那块 interchangeable，也不是已经 sendheaders bundled（247） interchangeable / 1235 hdr130-notswitch interchangeable / 1237 hdr130-nothave interchangeable，也不是已经 announce-received interchangeable / 36 announce-received interchangeable。**  
   官方把接收方表态和已经有那块写成两件。看见发了偏好，不是已经有那块。

3. **看见发了 sendheaders / 看见发了 sendheaders / 这份对象 is not already 头先同步已经做完 interchangeable，也不是已经 sendheaders bundled（247） interchangeable / 1235 hdr130-notswitch interchangeable / 1236 hdr130-notmust interchangeable，也不是已经 addrv2-pref interchangeable / 246 addrv2-pref interchangeable。**  
   官方把头先同步当作通告常常先发库存哈希的背景，不是 sendheaders 已经做完头先同步。看见发了 sendheaders，不是头先同步已经做完。

协议版本号、空消息编码、头定位器做法是规范与实现里的数字和算法，本页不抄。不要另写 怎样扣头、怎样用假头围住对等节点、怎样只通告哈希卡住中间块。

## 官方为什么这样拆

- **更想收头 不是已经改通告：官方只让接收方表态。看见发了信号，不是发送方已经改口。**
- **发了偏好 不是已经有那块：官方把偏好信号和已经收到块写成两件。**
- **发了 sendheaders 不是头先同步已经做完：官方把头先同步写成背景，不是本页信号已经做完那一步。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经改用头通告 | 不是已经改用头通告 | 不是已经announce-received（36） |
| 已经有那块 | 不是已经有那块 | 不是已经addrv2-pref（246） |
| 头先同步已经做完 | 不是头先同步已经做完 | 不是已经1236 hdr130-notmust |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-130 sendheaders not already switched / not already have-block / not already headers-first 正式三事（247 余量），必须分开是不是已经改用头通告、是不是已经有那块、是不是头先同步已经做完。可以跳过「看见发了 sendheaders 就已经有新块」。不要另写 怎样扣头、怎样用假头围住对等节点、怎样只通告哈希卡住中间块。247 sendheaders vs have bundled unbundling 在本页 item 1 启动；续 [`worked-example-hdr130-notmust-vs-bundled.md`](worked-example-hdr130-notmust-vs-bundled.md)（不变量 1236 item 2）。

## 本页不抄

- 协议版本号、空消息字段、头定位器做法、一次带头个数。
- 怎样扣头、怎样用假头围住对等节点、怎样只通告哈希卡住中间块。
