# 例：看见有限服务位不是已经剪枝；看见两位都开不是已经同一种服务；看见没开完整链位不是已经不可用

**层次**：网络 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-159](https://github.com/bitcoin/bips/blob/master/bip-0159.mediawiki)（Deployed, Peer Services）。  
**对应课文**：[L3.5](../../courses/level-03-bitcoin/L03-M05-full-node-and-spv.md)、[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)、[L9.3](../../courses/level-09-systems/L09-M03-storage.md)。  
**不要写进**：index/03 共识行、Ethereum 行、M5.4、L5.1、L5.4、05b。本页是「BIP-159 limited-bit not already pruned / not already same-service / not already unusable 正式三事（250 余量）/ not 1254 lim159-notprune interchangeable / not 250 limited-service-vs-archive bundled interchangeable」，不是 limited bundled（250），也不是已经 history-window（207），也不是已经 skip-script（25）。不要另写 怎样按索取旧块摸剪点、怎样把轻客户端骗到有限对等节点上下旧块。

## 官方三件事

1. **看见有限服务位 / 看见两位都开 这份对象 is not already 已经剪枝 interchangeable，也不是已经 limited bundled（250） interchangeable / 1254 lim159-notprune interchangeable / 1253 lim159-notarch interchangeable，也不是已经 BIP-159 limited-bit not already pruned / not already same-service / not already unusable 正式三事 bundled（250 item 2 余量） interchangeable / 250 limited item 2 interchangeable。**  
   官方写：剪枝或有限对等节点不得再打开宣称能服完整链的那一位。理由：能服完整链的节点也可以同时打开有限位。看见有限服务位，不是已经剪枝。看见两位都开，不是已经同一种服务，也不是已经剪过。看见没开「完整链」那一位，不是已经不可用。

2. **看见两位都开 / 看见有限服务位 / 这份对象 is not already 已经同一种服务 interchangeable，也不是已经 limited bundled（250） interchangeable / 1254 lim159-notprune interchangeable / 1255 lim159-notcut interchangeable，也不是已经 history-window interchangeable / 207 history-window interchangeable。**  
   官方把两位都开和已经同一种服务写成两件。看见两位都开，不是已经同一种服务。

3. **看见没开完整链位 / 看见有限服务位 / 这份对象 is not already 已经不可用 interchangeable，也不是已经 limited bundled（250） interchangeable / 1254 lim159-notprune interchangeable / 1253 lim159-notarch interchangeable，也不是已经 skip-script interchangeable / 25 skip-script interchangeable。**  
   官方把没开完整链位和已经不可用写成两件。看见没开完整链位，不是已经不可用。

窗口长度、位编号、缓冲块数是规范里的数字，本页不抄。不要另写 怎样按索取旧块摸剪点、怎样把轻客户端骗到有限对等节点上下旧块。

## 官方为什么这样拆

- **有限位 不是已经剪枝：官方允许完整链节点同时打开这一位。看见有限位，不是对方已经撕了旧体。**
- **两位都开 不是已经同一种服务：官方写完整链节点也可以同时打开有限位。**
- **没开完整链位 不是已经不可用：官方只禁止剪枝节点再宣称完整链，不是这一位已经没邻居。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经剪枝 | 不是已经剪枝 | 不是已经history-window（207） |
| 已经同一种服务 | 不是已经同一种服务 | 不是已经skip-script（25） |
| 已经不可用 | 不是已经不可用 | 不是已经1253 lim159-notarch |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-159 limited-bit not already pruned / not already same-service / not already unusable 正式三事（250 余量），必须分开是不是已经剪枝、是不是已经同一种服务、是不是已经不可用。可以跳过「看见有限服务位就已经是剪枝」。不要另写 怎样按索取旧块摸剪点、怎样把轻客户端骗到有限对等节点上下旧块。250 limited vs archive bundled unbundling 在本页 item 2 续；续 [`worked-example-lim159-notcut-vs-bundled.md`](worked-example-lim159-notcut-vs-bundled.md)（不变量 1255 item 3）。

## 本页不抄

- 位编号、窗口块数、缓冲块数、大约天数、参考实现拉取号。
- 怎样按索取旧块摸剪点、怎样把轻客户端骗到有限对等节点上下旧块。
