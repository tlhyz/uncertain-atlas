# 例：看见跳过了库存通告不是已经拒进池；看见跳过通告不是已经共识非法；看见发了这条消息不是全网低费率已经被滤掉

**层次**：内存池 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-133](https://github.com/bitcoin/bips/blob/master/bip-0133.mediawiki)（Deployed, Peer Services）。  
**对应课文**：[L3.2](../../courses/level-03-bitcoin/L03-M02-fees-and-standardness.md)、[L9.2](../../courses/level-09-systems/L09-M02-mempool.md)。  
**不要写进**：index/03 共识行、Ethereum 行、M5.4、L5.1、L5.4、05b。本页是「BIP-133 skip-inv not already rejected / not already illegal / not already filtered-net 正式三事（245 余量）/ not 1238 fee133-notpool interchangeable / not 245 feefilter-vs-rejected bundled interchangeable」，不是 feefilter bundled（245），也不是策略就已经是共识（144），也不是选择加入替换就已经换掉（166）。不要另写 怎样按费率认出节点、怎样绕过过滤器、怎样伪造库存通告。

## 官方三件事

1. **看见跳过了库存通告 / 看见跳过通告 这份对象 is not already 已经拒进池 interchangeable，也不是已经 feefilter bundled（245） interchangeable / 1238 fee133-notpool interchangeable / 1239 fee133-notmust interchangeable，也不是已经 BIP-133 skip-inv not already rejected / not already illegal / not already filtered-net 正式三事 bundled（245 item 1 余量） interchangeable / 245 feefilter item 1 interchangeable。**  
   官方写：这条消息用来告诉对等节点，不要再把低于指定费率的交易库存通告过来。收到之后，发送方可以在发出库存通告之前就知道，这笔对那个对等节点来说太便宜，于是跳过通告。看见跳过了库存通告，不是已经拒进池，也不是已经共识非法，也不是已经进不了块。看见发了这条消息，不是全网低费率交易已经被滤掉。

2. **看见跳过通告 / 看见跳过了库存通告 / 这份对象 is not already 已经共识非法 interchangeable，也不是已经 feefilter bundled（245） interchangeable / 1238 fee133-notpool interchangeable / 1240 fee133-notbloom interchangeable，也不是已经 policy-consensus interchangeable / 144 policy-consensus interchangeable。**  
   官方把少发一次库存通告和已经共识非法写成两件。看见跳过通告，不是已经共识非法。

3. **看见发了这条消息 / 看见跳过了库存通告 / 这份对象 is not already 全网低费率交易已经被滤掉 interchangeable，也不是已经 feefilter bundled（245） interchangeable / 1238 fee133-notpool interchangeable / 1239 fee133-notmust interchangeable，也不是已经 rbf-signal interchangeable / 166 rbf-signal interchangeable。**  
   官方把发给一个对等节点的指令和全网低费率已经被滤掉写成两件。看见发了这条消息，不是全网低费率交易已经被滤掉。

消息宽度、协议版本号、量化与随机化做法是规范与实现里的数字和算法，本页不抄。不要另写 怎样按费率认出节点、怎样绕过过滤器、怎样伪造库存通告。

## 官方为什么这样拆

- **跳过通告 不是已经拒进池：官方只让发送方少发一次库存通告。看见没通告过来，不是邻居已经按策略拒了。**
- **跳过通告 不是已经共识非法：官方把没通告和链已经判死刑写成两件。**
- **发了这条消息 不是全网已经被滤掉：官方写的是对那个对等节点太便宜。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经拒进池 | 不是已经拒进池 | 不是已经policy-consensus（144） |
| 已经共识非法 | 不是已经共识非法 | 不是已经rbf-signal（166） |
| 全网低费率交易已经被滤掉 | 不是全网低费率交易已经被滤掉 | 不是已经1239 fee133-notmust |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-133 skip-inv not already rejected / not already illegal / not already filtered-net 正式三事（245 余量），必须分开是不是已经拒进池、是不是已经共识非法、是不是全网低费率交易已经被滤掉。可以跳过「看见跳过库存通告就已经被链拒绝」。不要另写 怎样按费率认出节点、怎样绕过过滤器、怎样伪造库存通告。245 feefilter vs rejected bundled unbundling 在本页 item 1 启动；续 [`worked-example-fee133-notmust-vs-bundled.md`](worked-example-fee133-notmust-vs-bundled.md)（不变量 1239 item 2）。

## 本页不抄

- 协议版本号、费率单位取值、消息字段宽度、量化与随机化做法。
- 怎样按费率认出节点、怎样绕过过滤器、怎样伪造库存通告。
