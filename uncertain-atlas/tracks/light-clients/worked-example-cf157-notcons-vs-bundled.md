# 例：看见过滤器头链对上不是已经写进共识；看见至少一个诚实对等节点不是块已经合法；看见过滤器头链对上不是已经不需要诚实对等节点

**层次**：轻客户端 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-157](https://github.com/bitcoin/bips/blob/master/bip-0157.mediawiki)（Deployed, Peer Services；依赖 158）。  
**对应课文**：[L3.5](../../courses/level-03-bitcoin/L03-M05-full-node-and-spv.md)、[L9.6](../../courses/level-09-systems/L09-M06-light-clients.md)。  
**不要写进**：`index/03` 共识行、Ethereum 行、M5.4、L5.1、L5.4、05b。本页是「BIP-157 header-chain not already consensus / not already valid-block / not already no-honest-peer 正式三事（243 余量）/ not 1278 cf157-notcons interchangeable / not 243 cfilter-vs-have bundled interchangeable」，不是 cfilter vs have bundled（243），也不是已经 must-name-trust（22），也不是已经 v2-private（242）。不要另写 怎样造假过滤器、怎样用布隆做拒绝服务、怎样做交集分析、怎样匿名取块。

## 官方三件事

1. **看见过滤器头链对上 / 看见过滤器头链对上 这份对象 is not already 已经写进共识 interchangeable，也不是已经 cfilter vs have bundled（243） interchangeable / 1278 cf157-notcons interchangeable / 1277 cf157-nothave interchangeable，也不是已经 BIP-157 header-chain not already consensus / not already valid-block / not already no-honest-peer 正式三事 bundled（243 item 2 余量） interchangeable / 243 cfilter item 2 interchangeable。**  
   官方把过滤器头链对上和已经写进共识写成两件。看见过滤器头链对上，不是已经写进共识。

2. **看见至少一个诚实对等节点 / 看见过滤器头链对上 / 这份对象 is not already 块已经合法 interchangeable，也不是已经 cfilter vs have bundled（243） interchangeable / 1278 cf157-notcons interchangeable / 1279 cf157-notfull interchangeable，也不是已经 must-name-trust interchangeable / 22 must-name-trust interchangeable。**  
   官方把至少一个诚实对等节点和块已经合法写成两件。看见至少一个诚实对等节点，不是块已经合法。

3. **看见过滤器头链对上 / 看见至少一个诚实对等节点 / 这份对象 is not already 已经不需要诚实对等节点 interchangeable，也不是已经 cfilter vs have bundled（243） interchangeable / 1278 cf157-notcons interchangeable / 1277 cf157-nothave interchangeable，也不是已经 v2-private interchangeable / 242 v2-private interchangeable。**  
   官方把过滤器头链对上和已经不需要诚实对等节点写成两件。看见过滤器头链对上，不是已经不需要诚实对等节点。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样造假过滤器、怎样用布隆做拒绝服务、怎样做交集分析、怎样匿名取块。

## 官方为什么这样拆

- **头链对上 不是已经写进共识：官方明确不改共识规则。**
- **至少一个诚实对等节点 不是已经不需要诚实对等节点：官方把保证钉在至少一个诚实对等节点。**
- **头链一致 不是块已经合法：官方写这是纯点对点层方案。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经写进共识 | 不是已经写进共识 | 不是已经must-name-trust（22） |
| 块已经合法 | 不是块已经合法 | 不是已经v2-private（242） |
| 已经不需要诚实对等节点 | 不是已经不需要诚实对等节点 | 不是已经1277 cf157-nothave |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-157 header-chain not already consensus / not already valid-block / not already no-honest-peer 正式三事（243 余量），必须分开是不是已经写进共识、是不是块已经合法、是不是已经不需要诚实对等节点。可以跳过「看见客户端侧过滤器对上就已经看见付款」。不要另写 怎样造假过滤器、怎样用布隆做拒绝服务、怎样做交集分析、怎样匿名取块。243 cfilter vs have bundled unbundling 在本页 item 2 续；续 [`worked-example-cf157-notfull-vs-bundled.md`](worked-example-cf157-notfull-vs-bundled.md)（不变量 1279 item 3）。

## 本页不抄

- 过滤器构造、编码、检查点间隔、一次索取上限、服务位取值。
- 怎样造假过滤器、怎样用布隆做拒绝服务、怎样做交集分析、怎样匿名取块。
