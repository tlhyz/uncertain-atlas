# 例：看见用头通告新尖不是已经有块；看见重组时先发了头不是中间块已经在手里；看见先发头不是重组已经处理完

**层次**：网络 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-130](https://github.com/bitcoin/bips/blob/master/bip-0130.mediawiki)（Deployed, Peer Services）。  
**对应课文**：[L3.4](../../courses/level-03-bitcoin/L03-M04-network-and-eclipse.md)、[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：index/03 共识行、Ethereum 行、M5.4、L5.1、L5.4、05b。本页是「BIP-130 tip-headers not already have-block / not already have-middle / not already reorg-done 正式三事（247 余量）/ not 1237 hdr130-nothave interchangeable / not 247 sendheaders-vs-have bundled interchangeable」，不是 sendheaders bundled（247），也不是宣布就已经收到（36），也不是后继地址偏好就已经只收后继格式（246）。不要另写 怎样扣头、怎样用假头围住对等节点、怎样只通告哈希卡住中间块。

## 官方三件事

1. **看见用头通告新尖 / 看见重组时先发了头 这份对象 is not already 已经有块 interchangeable，也不是已经 sendheaders bundled（247） interchangeable / 1237 hdr130-nothave interchangeable / 1235 hdr130-notswitch interchangeable，也不是已经 BIP-130 tip-headers not already have-block / not already have-middle / not already reorg-done 正式三事 bundled（247 item 3 余量） interchangeable / 247 sendheaders item 3 interchangeable。**  
   官方写：新块若接在当前尖上，直接通告这块的头，通常比只通告哈希更省：对等节点不必再造、再发一次回头要头。重组时若只通告新尖的库存，对等节点能立刻要新尖，但中间块要等头到了才要。从上次分叉点一直发到新尖的头，对等节点才能立刻要那些中间块。看见用头通告新尖，不是已经有块。看见重组时先发了头，不是中间块已经在手里，也不是重组已经处理完。

2. **看见重组时先发了头 / 看见用头通告新尖 / 这份对象 is not already 中间块已经在手里 interchangeable，也不是已经 sendheaders bundled（247） interchangeable / 1237 hdr130-nothave interchangeable / 1236 hdr130-notmust interchangeable，也不是已经 announce-received interchangeable / 36 announce-received interchangeable。**  
   官方把先发头和中间块已经在手里写成两件。看见重组时先发了头，不是中间块已经在手里。

3. **看见先发头 / 看见用头通告新尖 / 这份对象 is not already 重组已经处理完 interchangeable，也不是已经 sendheaders bundled（247） interchangeable / 1237 hdr130-nothave interchangeable / 1235 hdr130-notswitch interchangeable，也不是已经 addrv2-pref interchangeable / 246 addrv2-pref interchangeable。**  
   官方把先发头写成好让对等节点立刻要中间块，不是重组已经处理完。看见先发头，不是重组已经处理完。

协议版本号、空消息编码、头定位器做法是规范与实现里的数字和算法，本页不抄。不要另写 怎样扣头、怎样用假头围住对等节点、怎样只通告哈希卡住中间块。

## 官方为什么这样拆

- **先发头 不是已经有块：官方写头通告是为了少一次回头要头。看见头到了，不是块已经在手里。**
- **重组时先发了头 不是中间块已经在手里：官方写从分叉点发头，好让对等节点立刻要中间块。**
- **先发头 不是重组已经处理完：官方把能立刻要和已经处理完写成两件。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经有块 | 不是已经有块 | 不是已经announce-received（36） |
| 中间块已经在手里 | 不是中间块已经在手里 | 不是已经addrv2-pref（246） |
| 重组已经处理完 | 不是重组已经处理完 | 不是已经1235 hdr130-notswitch |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-130 tip-headers not already have-block / not already have-middle / not already reorg-done 正式三事（247 余量），必须分开是不是已经有块、是不是中间块已经在手里、是不是重组已经处理完。可以跳过「看见发了 sendheaders 就已经有新块」。不要另写 怎样扣头、怎样用假头围住对等节点、怎样只通告哈希卡住中间块。247 sendheaders vs have bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 协议版本号、空消息字段、头定位器做法、一次带头个数。
- 怎样扣头、怎样用假头围住对等节点、怎样只通告哈希卡住中间块。
