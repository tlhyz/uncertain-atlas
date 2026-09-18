# 例：看见拒收不是已经共识非法；看见拒收不是全网已经知道；看见没拒收不是已经是当前最好链

**层次**：网络 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-61](https://github.com/bitcoin/bips/blob/master/bip-0061.mediawiki)（Deployed, Peer Services）。  
**对应课文**：[L3.2](../../courses/level-03-bitcoin/L03-M02-fees-and-standardness.md)、[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)、[L9.2](../../courses/level-09-systems/L09-M02-mempool.md)。  
**不要写进**：index/03 共识行、Ethereum 行、M5.4、L5.1、L5.4、05b。本页是「BIP-61 reject not already illegal / not already net-wide / not already best-chain 正式三事（254 余量）/ not 1265 rej61-notill interchangeable / not 254 reject-vs-consensus bundled interchangeable」，不是 reject bundled（254），也不是已经 policy-consensus（144），也不是已经 feefilter-reject（245）。不要另写 怎样对合法对象乱发拒收、怎样骚扰用户、怎样把日志盘写满。

## 官方三件事

1. **看见拒收 / 看见拒收 这份对象 is not already 已经共识非法 interchangeable，也不是已经 reject bundled（254） interchangeable / 1265 rej61-notill interchangeable / 1266 rej61-notuser interchangeable，也不是已经 BIP-61 reject not already illegal / not already net-wide / not already best-chain 正式三事 bundled（254 item 1 余量） interchangeable / 254 reject item 1 interchangeable。**  
   官方写：本页新增一种消息，直接回给对等节点，用来回答版本、交易或块。动机是互操作：让对方知道为什么块或交易被拒，或为什么因没按协议走被踢。官方还写：否则合法、只是还不是这个节点心里当前最好链的块，不应当触发拒收。看见拒收，不是已经共识非法，也不是全网已经知道，也不是已经封禁。看见没拒收，不是已经收下，也不是已经是当前最好链。

2. **看见拒收 / 看见拒收 / 这份对象 is not already 全网已经知道 interchangeable，也不是已经 reject bundled（254） interchangeable / 1265 rej61-notill interchangeable / 1267 rej61-notpol interchangeable，也不是已经 policy-consensus interchangeable / 144 policy-consensus interchangeable。**  
   官方把拒收和全网已经知道写成两件。看见拒收，不是全网已经知道。

3. **看见没拒收 / 看见拒收 / 这份对象 is not already 已经是当前最好链 interchangeable，也不是已经 reject bundled（254） interchangeable / 1265 rej61-notill interchangeable / 1266 rej61-notuser interchangeable，也不是已经 feefilter-reject interchangeable / 245 feefilter-reject interchangeable。**  
   官方把没拒收和已经是当前最好链写成两件。看见没拒收，不是已经是当前最好链。

拒收码取值、协议版本号、字段宽度是规范里的数字，本页不抄。不要另写 怎样对合法对象乱发拒收、怎样骚扰用户、怎样把日志盘写满。

## 官方为什么这样拆

- **这个节点拒 不是已经共识非法：官方只让这个对等节点回一句。看见拒，不是链已经判死刑。**
- **拒收 不是全网已经知道：官方只写直接回给这个对等节点。**
- **没拒收 不是已经是当前最好链：官方写还不是最好链的合法块不应当触发拒收。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经共识非法 | 不是已经共识非法 | 不是已经policy-consensus（144） |
| 全网已经知道 | 不是全网已经知道 | 不是已经feefilter-reject（245） |
| 已经是当前最好链 | 不是已经是当前最好链 | 不是已经1266 rej61-notuser |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-61 reject not already illegal / not already net-wide / not already best-chain 正式三事（254 余量），必须分开是不是已经共识非法、是不是全网已经知道、是不是已经是当前最好链。可以跳过「看见拒收消息就已经共识非法」。不要另写 怎样对合法对象乱发拒收、怎样骚扰用户、怎样把日志盘写满。254 reject vs consensus bundled unbundling 在本页 item 1 启动；续 [`worked-example-rej61-notuser-vs-bundled.md`](worked-example-rej61-notuser-vs-bundled.md)（不变量 1266 item 2）。

## 本页不抄

- 拒收码取值、协议版本号、字段宽度、哈希宽度。
- 怎样对合法对象乱发拒收、怎样骚扰用户、怎样把日志盘写满。
