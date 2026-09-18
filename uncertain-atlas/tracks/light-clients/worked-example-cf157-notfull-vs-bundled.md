# 例：看见支持客户端侧过滤不是已经是全节点；看见比 BIP-37 好核不是脚本已经验完；看见支持客户端侧过滤不是BIP-37 已经退役

**层次**：轻客户端 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-157](https://github.com/bitcoin/bips/blob/master/bip-0157.mediawiki)（Deployed, Peer Services；依赖 158）。  
**对应课文**：[L3.5](../../courses/level-03-bitcoin/L03-M05-full-node-and-spv.md)、[L9.6](../../courses/level-09-systems/L09-M06-light-clients.md)。  
**不要写进**：`index/03` 共识行、Ethereum 行、M5.4、L5.1、L5.4、05b。本页是「BIP-157 cfilter not already full-node / not already scripts-checked / not already bloom-retired 正式三事（243 余量）/ not 1279 cf157-notfull interchangeable / not 243 cfilter-vs-have bundled interchangeable」，不是 cfilter vs have bundled（243），也不是已经 bloom-retired（252），也不是已经 basic-filter（244）。不要另写 怎样造假过滤器、怎样用布隆做拒绝服务、怎样做交集分析、怎样匿名取块。

## 官方三件事

1. **看见支持客户端侧过滤 / 看见支持客户端侧过滤 这份对象 is not already 已经是全节点 interchangeable，也不是已经 cfilter vs have bundled（243） interchangeable / 1279 cf157-notfull interchangeable / 1277 cf157-nothave interchangeable，也不是已经 BIP-157 cfilter not already full-node / not already scripts-checked / not already bloom-retired 正式三事 bundled（243 item 3 余量） interchangeable / 243 cfilter item 3 interchangeable。**  
   官方把支持客户端侧过滤和已经是全节点写成两件。看见支持客户端侧过滤，不是已经是全节点。

2. **看见比 BIP-37 好核 / 看见支持客户端侧过滤 / 这份对象 is not already 脚本已经验完 interchangeable，也不是已经 cfilter vs have bundled（243） interchangeable / 1279 cf157-notfull interchangeable / 1278 cf157-notcons interchangeable，也不是已经 bloom-retired interchangeable / 252 bloom-retired interchangeable。**  
   官方把比 BIP-37 好核和脚本已经验完写成两件。看见比 BIP-37 好核，不是脚本已经验完。

3. **看见支持客户端侧过滤 / 看见比 BIP-37 好核 / 这份对象 is not already BIP-37 已经退役 interchangeable，也不是已经 cfilter vs have bundled（243） interchangeable / 1279 cf157-notfull interchangeable / 1277 cf157-nothave interchangeable，也不是已经 basic-filter interchangeable / 244 basic-filter interchangeable。**  
   官方把支持客户端侧过滤和BIP-37 已经退役写成两件。看见支持客户端侧过滤，不是BIP-37 已经退役。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样造假过滤器、怎样用布隆做拒绝服务、怎样做交集分析、怎样匿名取块。

## 官方为什么这样拆

- **支持本页 不是已经是全节点：官方仍写不检查所有块是否合法。**
- **比 BIP-37 好核 不是脚本已经验完：官方把安全仍靠矿工激励。**
- **采纳本页 不是 BIP-37 已经退役：官方写可能减少支持，不是已经关掉布隆。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是全节点 | 不是已经是全节点 | 不是已经bloom-retired（252） |
| 脚本已经验完 | 不是脚本已经验完 | 不是已经basic-filter（244） |
| BIP-37 已经退役 | 不是BIP-37 已经退役 | 不是已经1277 cf157-nothave |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-157 cfilter not already full-node / not already scripts-checked / not already bloom-retired 正式三事（243 余量），必须分开是不是已经是全节点、是不是脚本已经验完、是不是BIP-37 已经退役。可以跳过「看见客户端侧过滤器对上就已经看见付款」。不要另写 怎样造假过滤器、怎样用布隆做拒绝服务、怎样做交集分析、怎样匿名取块。243 cfilter vs have bundled unbundling 在本页 item 3 完成；本页收束本批。

## 本页不抄

- 过滤器构造、编码、检查点间隔、一次索取上限、服务位取值。
- 怎样造假过滤器、怎样用布隆做拒绝服务、怎样做交集分析、怎样匿名取块。
