# 例：看见服了最近一块不是已经暴露了剪到哪；看见连上了有限服务位不是初始同步已经能靠它从创世拉完；看见地址表里有这一位不是轻客户端已经核过服务位

**层次**：网络 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-159](https://github.com/bitcoin/bips/blob/master/bip-0159.mediawiki)（Deployed, Peer Services）。  
**对应课文**：[L3.5](../../courses/level-03-bitcoin/L03-M05-full-node-and-spv.md)、[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)、[L9.3](../../courses/level-09-systems/L09-M03-storage.md)。  
**不要写进**：index/03 共识行、Ethereum 行、M5.4、L5.1、L5.4、05b。本页是「BIP-159 served-recent not already leaked / not already ibd-done / not already light-checked 正式三事（250 余量）/ not 1255 lim159-notcut interchangeable / not 250 limited-service-vs-archive bundled interchangeable」，不是 limited bundled（250），也不是已经 cfilter-have（243），也不是已经 skip-script（25）。不要另写 怎样按索取旧块摸剪点、怎样把轻客户端骗到有限对等节点上下旧块。

## 官方三件事

1. **看见服了最近一块 / 看见连上了有限服务位 这份对象 is not already 已经暴露了剪到哪 interchangeable，也不是已经 limited bundled（250） interchangeable / 1255 lim159-notcut interchangeable / 1253 lim159-notarch interchangeable，也不是已经 BIP-159 served-recent not already leaked / not already ibd-done / not already light-checked 正式三事 bundled（250 item 3 余量） interchangeable / 250 limited item 3 interchangeable。**  
   官方写：各节点剪到哪可能不同，靠索取旧块能摸出深度，这是指纹。剪枝节点因此不该泄露深度，不应当去服比它对外宣布的窗口更深的块。连上宣布有限服务的对等节点时，应当给重组留一段缓冲。看见它服了最近一块，不是已经知道它剪到哪。看见连上了有限服务位，不是初始同步已经能靠它从创世拉完。看见地址表里有这一位，不是轻客户端已经核过服务位。

2. **看见连上了有限服务位 / 看见服了最近一块 / 这份对象 is not already 初始同步已经能靠它从创世拉完 interchangeable，也不是已经 limited bundled（250） interchangeable / 1255 lim159-notcut interchangeable / 1254 lim159-notprune interchangeable，也不是已经 cfilter-have interchangeable / 243 cfilter-have interchangeable。**  
   官方把连上了有限服务位和初始同步已经能靠它从创世拉完写成两件。看见连上了有限服务位，不是初始同步已经能靠它从创世拉完。

3. **看见地址表里有这一位 / 看见服了最近一块 / 这份对象 is not already 轻客户端已经核过服务位 interchangeable，也不是已经 limited bundled（250） interchangeable / 1255 lim159-notcut interchangeable / 1253 lim159-notarch interchangeable，也不是已经 skip-script interchangeable / 25 skip-script interchangeable。**  
   官方把地址表里有这一位和轻客户端已经核过服务位写成两件。看见地址表里有这一位，不是轻客户端已经核过服务位。

窗口长度、位编号、缓冲块数是规范里的数字，本页不抄。不要另写 怎样按索取旧块摸剪点、怎样把轻客户端骗到有限对等节点上下旧块。

## 官方为什么这样拆

- **服了最近一块 不是已经暴露剪点：官方要求不要服得比宣布窗口更深。看见最近一块到了，不是深度已经测出来。**
- **连上有限位 不是已经能从创世拉完：官方写初始同步不该靠有限对等节点从创世拉完。**
- **地址表里有这一位 不是轻客户端已经核过：官方只把这一位写成对等服务宣布，不是核完服务。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经暴露了剪到哪 | 不是已经暴露了剪到哪 | 不是已经cfilter-have（243） |
| 初始同步已经能靠它从创世拉完 | 不是初始同步已经能靠它从创世拉完 | 不是已经skip-script（25） |
| 轻客户端已经核过服务位 | 不是轻客户端已经核过服务位 | 不是已经1253 lim159-notarch |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-159 served-recent not already leaked / not already ibd-done / not already light-checked 正式三事（250 余量），必须分开是不是已经暴露了剪到哪、是不是初始同步已经能靠它从创世拉完、是不是轻客户端已经核过服务位。可以跳过「看见有限服务位就已经是剪枝」。不要另写 怎样按索取旧块摸剪点、怎样把轻客户端骗到有限对等节点上下旧块。250 limited vs archive bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 位编号、窗口块数、缓冲块数、大约天数、参考实现拉取号。
- 怎样按索取旧块摸剪点、怎样把轻客户端骗到有限对等节点上下旧块。
