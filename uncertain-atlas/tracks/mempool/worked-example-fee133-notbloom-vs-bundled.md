# 例：看见布隆过了不是已经过了费率门；看见费率过滤器不是已经是精确最低费率；看见强制转发例外不是已经关掉全部策略

**层次**：内存池 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-133](https://github.com/bitcoin/bips/blob/master/bip-0133.mediawiki)（Deployed, Peer Services）。  
**对应课文**：[L3.2](../../courses/level-03-bitcoin/L03-M02-fees-and-standardness.md)、[L9.2](../../courses/level-09-systems/L09-M02-mempool.md)。  
**不要写进**：index/03 共识行、Ethereum 行、M5.4、L5.1、L5.4、05b。本页是「BIP-133 bloom-and not already fee-pass / not already exact-min / not already policy-off 正式三事（245 余量）/ not 1240 fee133-notbloom interchangeable / not 245 feefilter-vs-rejected bundled interchangeable」，不是 feefilter bundled（245），也不是策略就已经是共识（44），也不是选择加入替换就已经换掉（166）。不要另写 怎样按费率认出节点、怎样绕过过滤器、怎样伪造库存通告。

## 官方三件事

1. **看见布隆过了 / 看见费率过滤器 这份对象 is not already 已经过了费率门 interchangeable，也不是已经 feefilter bundled（245） interchangeable / 1240 fee133-notbloom interchangeable / 1238 fee133-notpool interchangeable，也不是已经 BIP-133 bloom-and not already fee-pass / not already exact-min / not already policy-off 正式三事 bundled（245 item 3 余量） interchangeable / 245 feefilter item 3 interchangeable。**  
   官方写：费率过滤和布隆过滤是相加的；轻客户端若两边都开，交易必须两道都过才转发。由内存池查询产生的库存通告，若已经有费率过滤器，也要受它管。官方还写：把本节点内存池最低费率广播出去，会留下可用来认人的信息。对打算强制转发的白名单对等节点，可以不发这条消息；那时交易即使没进池也打算转发。看见布隆过了，不是已经过了费率门。看见费率过滤器，不是已经是本节点精确的最低费率。看见强制转发例外，不是已经关掉全部策略。

2. **看见费率过滤器 / 看见布隆过了 / 这份对象 is not already 已经是本节点精确的最低费率 interchangeable，也不是已经 feefilter bundled（245） interchangeable / 1240 fee133-notbloom interchangeable / 1239 fee133-notmust interchangeable，也不是已经 reject-cost interchangeable / 44 reject-cost interchangeable。**  
   官方把广播最低费率和已经是本节点精确最低费率写成两件。看见费率过滤器，不是已经是精确最低费率，也不是已经匿名。

3. **看见强制转发例外 / 看见布隆过了 / 这份对象 is not already 已经关掉全部策略 interchangeable，也不是已经 feefilter bundled（245） interchangeable / 1240 fee133-notbloom interchangeable / 1238 fee133-notpool interchangeable，也不是已经 rbf-signal interchangeable / 166 rbf-signal interchangeable。**  
   官方把强制转发例外和已经关掉全部策略写成两件。看见强制转发例外，不是已经关掉全部策略。

消息宽度、协议版本号、量化与随机化做法是规范与实现里的数字和算法，本页不抄。不要另写 怎样按费率认出节点、怎样绕过过滤器、怎样伪造库存通告。

## 官方为什么这样拆

- **相加 不是已经只剩一道门：官方把布隆、费率、内存池查询写成要一起过。看见一道过了，不是两道都过。**
- **费率过滤器 不是已经是精确最低费率：官方写广播最低费率会留下可用来认人的信息。**
- **强制转发例外 不是已经关掉全部策略：官方写对白名单可以不发这条消息，那时交易即使没进池也打算转发。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经过了费率门 | 不是已经过了费率门 | 不是已经reject-cost（44） |
| 已经是本节点精确的最低费率 | 不是已经是本节点精确的最低费率 | 不是已经rbf-signal（166） |
| 已经关掉全部策略 | 不是已经关掉全部策略 | 不是已经1238 fee133-notpool |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-133 bloom-and not already fee-pass / not already exact-min / not already policy-off 正式三事（245 余量），必须分开是不是已经过了费率门、是不是已经是本节点精确的最低费率、是不是已经关掉全部策略。可以跳过「看见跳过库存通告就已经被链拒绝」。不要另写 怎样按费率认出节点、怎样绕过过滤器、怎样伪造库存通告。245 feefilter vs rejected bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 协议版本号、费率单位取值、消息字段宽度、量化与随机化做法。
- 怎样按费率认出节点、怎样绕过过滤器、怎样伪造库存通告。
