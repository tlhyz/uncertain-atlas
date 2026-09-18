# 例：看见有限服务位不是已经能服任意旧块；看见能转发新块不是已经能服创世以来的体；看见有限位不是已经是归档节点

**层次**：网络 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-159](https://github.com/bitcoin/bips/blob/master/bip-0159.mediawiki)（Deployed, Peer Services）。  
**对应课文**：[L3.5](../../courses/level-03-bitcoin/L03-M05-full-node-and-spv.md)、[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)、[L9.3](../../courses/level-09-systems/L09-M03-storage.md)。  
**不要写进**：index/03 共识行、Ethereum 行、M5.4、L5.1、L5.4、05b。本页是「BIP-159 limited-bit not already any-old / not already genesis-body / not already archive 正式三事（250 余量）/ not 1253 lim159-notarch interchangeable / not 250 limited-service-vs-archive bundled interchangeable」，不是 limited bundled（250），也不是已经 history-window（207），也不是已经 cfilter-have（243）。不要另写 怎样按索取旧块摸剪点、怎样把轻客户端骗到有限对等节点上下旧块。

## 官方三件事

1. **看见有限服务位 / 看见能转发新块 这份对象 is not already 已经能服任意旧块 interchangeable，也不是已经 limited bundled（250） interchangeable / 1253 lim159-notarch interchangeable / 1254 lim159-notprune interchangeable，也不是已经 BIP-159 limited-bit not already any-old / not already genesis-body / not already archive 正式三事 bundled（250 item 1 余量） interchangeable / 250 limited item 1 interchangeable。**  
   官方写：剪枝对等节点能转发块、头、交易和地址，但只保证能服最少数量的历史块。今天只有「能服全部历史」那一位。打开本页这一位的对等节点，必须至少能服最近一段窗口。看见有限服务位，不是已经能服任意旧块，也不是那些块已经在请求方手里，也不是已经是归档节点。看见能转发新块，不是已经能服创世以来的体。

2. **看见能转发新块 / 看见有限服务位 / 这份对象 is not already 已经能服创世以来的体 interchangeable，也不是已经 limited bundled（250） interchangeable / 1253 lim159-notarch interchangeable / 1255 lim159-notcut interchangeable，也不是已经 history-window interchangeable / 207 history-window interchangeable。**  
   官方把能转发新块和已经能服创世以来的体写成两件。看见能转发新块，不是已经能服创世以来的体。

3. **看见有限位 / 看见有限服务位 / 这份对象 is not already 已经是归档节点 interchangeable，也不是已经 limited bundled（250） interchangeable / 1253 lim159-notarch interchangeable / 1254 lim159-notprune interchangeable，也不是已经 cfilter-have interchangeable / 243 cfilter-have interchangeable。**  
   官方把有限位和已经是归档节点写成两件。看见有限位，不是已经是归档节点。

窗口长度、位编号、缓冲块数是规范里的数字，本页不抄。不要另写 怎样按索取旧块摸剪点、怎样把轻客户端骗到有限对等节点上下旧块。

## 官方为什么这样拆

- **有限窗口 不是已经能服任意旧块：官方只保证最近一段。看见这一位，不是完整历史已经可索取。**
- **能转发新块 不是已经能服创世以来的体：官方写剪枝节点能转发新块，但仍只保证最近窗口。**
- **有限位 不是已经是归档：官方把有限位和「能服全部历史」写成两位。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经能服任意旧块 | 不是已经能服任意旧块 | 不是已经history-window（207） |
| 已经能服创世以来的体 | 不是已经能服创世以来的体 | 不是已经cfilter-have（243） |
| 已经是归档节点 | 不是已经是归档节点 | 不是已经1254 lim159-notprune |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-159 limited-bit not already any-old / not already genesis-body / not already archive 正式三事（250 余量），必须分开是不是已经能服任意旧块、是不是已经能服创世以来的体、是不是已经是归档节点。可以跳过「看见有限服务位就已经是剪枝」。不要另写 怎样按索取旧块摸剪点、怎样把轻客户端骗到有限对等节点上下旧块。250 limited vs archive bundled unbundling 在本页 item 1 启动；续 [`worked-example-lim159-notprune-vs-bundled.md`](worked-example-lim159-notprune-vs-bundled.md)（不变量 1254 item 2）。

## 本页不抄

- 位编号、窗口块数、缓冲块数、大约天数、参考实现拉取号。
- 怎样按索取旧块摸剪点、怎样把轻客户端骗到有限对等节点上下旧块。
