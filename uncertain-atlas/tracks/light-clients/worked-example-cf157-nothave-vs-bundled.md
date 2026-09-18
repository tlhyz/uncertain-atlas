# 例：看见过滤器对上不是已经有块；看见确定性不是已经有那笔交易；看见过滤器对上不是已经是 BIP-37

**层次**：轻客户端 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-157](https://github.com/bitcoin/bips/blob/master/bip-0157.mediawiki)（Deployed, Peer Services；依赖 158）。  
**对应课文**：[L3.5](../../courses/level-03-bitcoin/L03-M05-full-node-and-spv.md)、[L9.6](../../courses/level-09-systems/L09-M06-light-clients.md)。  
**不要写进**：`index/03` 共识行、Ethereum 行、M5.4、L5.1、L5.4、05b。本页是「BIP-157 match not already have-block / not already have-tx / not already bip37 正式三事（243 余量）/ not 1277 cf157-nothave interchangeable / not 243 cfilter-vs-have bundled interchangeable」，不是 cfilter vs have bundled（243），也不是已经 bloom-retired（252），也不是已经 basic-filter（244）。不要另写 怎样造假过滤器、怎样用布隆做拒绝服务、怎样做交集分析、怎样匿名取块。

## 官方三件事

1. **看见过滤器对上 / 看见过滤器对上 这份对象 is not already 已经有块 interchangeable，也不是已经 cfilter vs have bundled（243） interchangeable / 1277 cf157-nothave interchangeable / 1278 cf157-notcons interchangeable，也不是已经 BIP-157 match not already have-block / not already have-tx / not already bip37 正式三事 bundled（243 item 1 余量） interchangeable / 243 cfilter item 1 interchangeable。**  
   官方把过滤器对上和已经有块写成两件。看见过滤器对上，不是已经有块。

2. **看见确定性 / 看见过滤器对上 / 这份对象 is not already 已经有那笔交易 interchangeable，也不是已经 cfilter vs have bundled（243） interchangeable / 1277 cf157-nothave interchangeable / 1279 cf157-notfull interchangeable，也不是已经 bloom-retired interchangeable / 252 bloom-retired interchangeable。**  
   官方把确定性和已经有那笔交易写成两件。看见确定性，不是已经有那笔交易。

3. **看见过滤器对上 / 看见确定性 / 这份对象 is not already 已经是 BIP-37 interchangeable，也不是已经 cfilter vs have bundled（243） interchangeable / 1277 cf157-nothave interchangeable / 1278 cf157-notcons interchangeable，也不是已经 basic-filter interchangeable / 244 basic-filter interchangeable。**  
   官方把过滤器对上和已经是 BIP-37写成两件。看见过滤器对上，不是已经是 BIP-37。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样造假过滤器、怎样用布隆做拒绝服务、怎样做交集分析、怎样匿名取块。

## 官方为什么这样拆

- **对上 不是已经有块：官方把看过滤器和下整块写成两步。**
- **确定性 不是已经是 BIP-37：官方写这是 BIP-37 的反面。**
- **对上了一个脚本 不是已经有那笔交易：官方写对上了再去下整块。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经有块 | 不是已经有块 | 不是已经bloom-retired（252） |
| 已经有那笔交易 | 不是已经有那笔交易 | 不是已经basic-filter（244） |
| 已经是 BIP-37 | 不是已经是 BIP-37 | 不是已经1278 cf157-notcons |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-157 match not already have-block / not already have-tx / not already bip37 正式三事（243 余量），必须分开是不是已经有块、是不是已经有那笔交易、是不是已经是 BIP-37。可以跳过「看见客户端侧过滤器对上就已经看见付款」。不要另写 怎样造假过滤器、怎样用布隆做拒绝服务、怎样做交集分析、怎样匿名取块。243 cfilter vs have bundled unbundling 在本页 item 1 启动；续 [`worked-example-cf157-notcons-vs-bundled.md`](worked-example-cf157-notcons-vs-bundled.md)（不变量 1278 item 2）。

## 本页不抄

- 过滤器构造、编码、检查点间隔、一次索取上限、服务位取值。
- 怎样造假过滤器、怎样用布隆做拒绝服务、怎样做交集分析、怎样匿名取块。
