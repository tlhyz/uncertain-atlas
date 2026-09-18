# 例：看见策略拒收不是已经共识非法；看见语义非法码不是已经全网非法；看见一条拒收不是已经该弹窗或已经该写满日志

**层次**：网络 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-61](https://github.com/bitcoin/bips/blob/master/bip-0061.mediawiki)（Deployed, Peer Services）。  
**对应课文**：[L3.2](../../courses/level-03-bitcoin/L03-M02-fees-and-standardness.md)、[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)、[L9.2](../../courses/level-09-systems/L09-M02-mempool.md)。  
**不要写进**：index/03 共识行、Ethereum 行、M5.4、L5.1、L5.4、05b。本页是「BIP-61 policy-code not already illegal / not already net-illegal / not already notify 正式三事（254 余量）/ not 1267 rej61-notpol interchangeable / not 254 reject-vs-consensus bundled interchangeable」，不是 reject bundled（254），也不是已经 policy-consensus（144），也不是已经 mempool-dump（253）。不要另写 怎样对合法对象乱发拒收、怎样骚扰用户、怎样把日志盘写满。

## 官方三件事

1. **看见策略拒收 / 看见语义非法码 这份对象 is not already 已经共识非法 interchangeable，也不是已经 reject bundled（254） interchangeable / 1267 rej61-notpol interchangeable / 1265 rej61-notill interchangeable，也不是已经 BIP-61 policy-code not already illegal / not already net-illegal / not already notify 正式三事 bundled（254 item 3 余量） interchangeable / 254 reject item 3 interchangeable。**  
   官方写：码分成协议句法错误、协议语义错误、本节点策略规则三类。官方还写：实现必须考虑对手对合法交易或块发拒收、或乱发拒收；把每条拒收都通知用户，会变成骚扰；把每条都写进调试日志，会把盘写满。看见策略拒收，不是已经共识非法。看见语义非法码，不是已经全网非法。看见一条拒收，不是已经该弹窗或已经该写满日志。

2. **看见语义非法码 / 看见策略拒收 / 这份对象 is not already 已经全网非法 interchangeable，也不是已经 reject bundled（254） interchangeable / 1267 rej61-notpol interchangeable / 1266 rej61-notuser interchangeable，也不是已经 policy-consensus interchangeable / 144 policy-consensus interchangeable。**  
   官方把语义非法码和已经全网非法写成两件。看见语义非法码，不是已经全网非法。

3. **看见一条拒收 / 看见策略拒收 / 这份对象 is not already 已经该弹窗或已经该写满日志 interchangeable，也不是已经 reject bundled（254） interchangeable / 1267 rej61-notpol interchangeable / 1265 rej61-notill interchangeable，也不是已经 mempool-dump interchangeable / 253 mempool-dump interchangeable。**  
   官方把一条拒收和已经该弹窗或已经该写满日志写成两件。看见一条拒收，不是已经该弹窗或已经该写满日志。

拒收码取值、协议版本号、字段宽度是规范里的数字，本页不抄。不要另写 怎样对合法对象乱发拒收、怎样骚扰用户、怎样把日志盘写满。

## 官方为什么这样拆

- **策略码 不是已经共识码：官方把策略单独一类。看见策略拒，不是已经非法。**
- **语义非法码 不是已经全网非法：官方只写这个节点回的码类。**
- **一条拒收 不是已经该弹窗或写满日志：官方写把每条都通知用户会变成骚扰，把每条都写日志会把盘写满。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经共识非法 | 不是已经共识非法 | 不是已经policy-consensus（144） |
| 已经全网非法 | 不是已经全网非法 | 不是已经mempool-dump（253） |
| 已经该弹窗或已经该写满日志 | 不是已经该弹窗或已经该写满日志 | 不是已经1265 rej61-notill |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-61 policy-code not already illegal / not already net-illegal / not already notify 正式三事（254 余量），必须分开是不是已经共识非法、是不是已经全网非法、是不是已经该弹窗或已经该写满日志。可以跳过「看见拒收消息就已经共识非法」。不要另写 怎样对合法对象乱发拒收、怎样骚扰用户、怎样把日志盘写满。254 reject vs consensus bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 拒收码取值、协议版本号、字段宽度、哈希宽度。
- 怎样对合法对象乱发拒收、怎样骚扰用户、怎样把日志盘写满。
