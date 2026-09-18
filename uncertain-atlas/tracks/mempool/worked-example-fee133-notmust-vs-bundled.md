# 例：看见你发了费率过滤器不是对等节点已经照做；看见协议版本够了不是已经在发；看见许可不是已经必须滤

**层次**：内存池 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-133](https://github.com/bitcoin/bips/blob/master/bip-0133.mediawiki)（Deployed, Peer Services）。  
**对应课文**：[L3.2](../../courses/level-03-bitcoin/L03-M02-fees-and-standardness.md)、[L9.2](../../courses/level-09-systems/L09-M02-mempool.md)。  
**不要写进**：index/03 共识行、Ethereum 行、M5.4、L5.1、L5.4、05b。本页是「BIP-133 permission not already must / not already sending / not already obeying 正式三事（245 余量）/ not 1239 fee133-notmust interchangeable / not 245 feefilter-vs-rejected bundled interchangeable」，不是 feefilter bundled（245），也不是策略就已经是共识（247），也不是选择加入替换就已经换掉（144）。不要另写 怎样按费率认出节点、怎样绕过过滤器、怎样伪造库存通告。

## 官方三件事

1. **看见你发了费率过滤器 / 看见协议版本够了 这份对象 is not already 对等节点已经照做 interchangeable，也不是已经 feefilter bundled（245） interchangeable / 1239 fee133-notmust interchangeable / 1238 fee133-notpool interchangeable，也不是已经 BIP-133 permission not already must / not already sending / not already obeying 正式三事 bundled（245 item 2 余量） interchangeable / 245 feefilter item 2 interchangeable。**  
   官方写：收到这条消息之后，节点被许可、但不是被要求，按里面的费率过滤交易库存通告。实现这条规范的客户端也可以选择一条都不发。旧客户端仍然兼容。能不能用这条消息，靠协议版本发现。看见你发了费率过滤器，不是对等节点已经照做。看见协议版本够了，不是已经在发、也不是已经在遵守。

2. **看见协议版本够了 / 看见你发了费率过滤器 / 这份对象 is not already 已经在发 interchangeable，也不是已经 feefilter bundled（245） interchangeable / 1239 fee133-notmust interchangeable / 1240 fee133-notbloom interchangeable，也不是已经 sendheaders-perm interchangeable / 247 sendheaders-perm interchangeable。**  
   官方把协议版本够了和已经在发写成两件。看见协议版本够了，不是已经在发。

3. **看见许可 / 看见你发了费率过滤器 / 这份对象 is not already 已经必须滤 interchangeable，也不是已经 feefilter bundled（245） interchangeable / 1239 fee133-notmust interchangeable / 1238 fee133-notpool interchangeable，也不是已经 policy-consensus interchangeable / 144 policy-consensus interchangeable。**  
   官方把「可以滤」和「必须滤」写成两件。看见许可，不是已经必须滤。

消息宽度、协议版本号、量化与随机化做法是规范与实现里的数字和算法，本页不抄。不要另写 怎样按费率认出节点、怎样绕过过滤器、怎样伪造库存通告。

## 官方为什么这样拆

- **许可 不是已经照做：官方把「可以滤」和「必须滤」写成两件事。看见发了消息，不是对等节点已经滤。**
- **协议版本够了 不是已经在发：能不能用靠协议版本发现，不是已经在发、已经在遵守。**
- **许可 不是已经必须滤：实现这条规范的客户端也可以选择一条都不发。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 对等节点已经照做 | 不是对等节点已经照做 | 不是已经sendheaders-perm（247） |
| 已经在发 | 不是已经在发 | 不是已经policy-consensus（144） |
| 已经必须滤 | 不是已经必须滤 | 不是已经1238 fee133-notpool |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-133 permission not already must / not already sending / not already obeying 正式三事（245 余量），必须分开是不是对等节点已经照做、是不是已经在发、是不是已经必须滤。可以跳过「看见跳过库存通告就已经被链拒绝」。不要另写 怎样按费率认出节点、怎样绕过过滤器、怎样伪造库存通告。245 feefilter vs rejected bundled unbundling 在本页 item 2 续；续 [`worked-example-fee133-notbloom-vs-bundled.md`](worked-example-fee133-notbloom-vs-bundled.md)（不变量 1240 item 3）。

## 本页不抄

- 协议版本号、费率单位取值、消息字段宽度、量化与随机化做法。
- 怎样按费率认出节点、怎样绕过过滤器、怎样伪造库存通告。
