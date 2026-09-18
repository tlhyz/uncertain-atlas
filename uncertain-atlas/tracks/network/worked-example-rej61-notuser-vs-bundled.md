# 例：看见一条拒收理由不是已经是官方原因；看见一条拒收理由不是已经写进共识；看见一条拒收理由不是已经该弹给用户

**层次**：网络 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-61](https://github.com/bitcoin/bips/blob/master/bip-0061.mediawiki)（Deployed, Peer Services）。  
**对应课文**：[L3.2](../../courses/level-03-bitcoin/L03-M02-fees-and-standardness.md)、[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)、[L9.2](../../courses/level-09-systems/L09-M02-mempool.md)。  
**不要写进**：index/03 共识行、Ethereum 行、M5.4、L5.1、L5.4、05b。本页是「BIP-61 reason not already official / not already consensus / not already for-users 正式三事（254 余量）/ not 1266 rej61-notuser interchangeable / not 254 reject-vs-consensus bundled interchangeable」，不是 reject bundled（254），也不是已经 reject-cost（44），也不是已经 mempool-dump（253）。不要另写 怎样对合法对象乱发拒收、怎样骚扰用户、怎样把日志盘写满。

## 官方三件事

1. **看见一条拒收理由 / 看见一条拒收理由 这份对象 is not already 已经是官方原因 interchangeable，也不是已经 reject bundled（254） interchangeable / 1266 rej61-notuser interchangeable / 1265 rej61-notill interchangeable，也不是已经 BIP-61 reason not already official / not already consensus / not already for-users 正式三事 bundled（254 item 2 余量） interchangeable / 254 reject item 2 interchangeable。**  
   官方写：人读字符串只打算用来调试。尤其是，不同实现可以用不同的句子。这条字符串不应当给用户看，也不应当拿去做互操作诊断以外的事。看见一条拒收理由，不是已经是官方原因，也不是已经写进共识，也不是已经该弹给用户。

2. **看见一条拒收理由 / 看见一条拒收理由 / 这份对象 is not already 已经写进共识 interchangeable，也不是已经 reject bundled（254） interchangeable / 1266 rej61-notuser interchangeable / 1267 rej61-notpol interchangeable，也不是已经 reject-cost interchangeable / 44 reject-cost interchangeable。**  
   官方把一条拒收理由和已经写进共识写成两件。看见一条拒收理由，不是已经写进共识。

3. **看见一条拒收理由 / 看见一条拒收理由 / 这份对象 is not already 已经该弹给用户 interchangeable，也不是已经 reject bundled（254） interchangeable / 1266 rej61-notuser interchangeable / 1265 rej61-notill interchangeable，也不是已经 mempool-dump interchangeable / 253 mempool-dump interchangeable。**  
   官方把一条拒收理由和已经该弹给用户写成两件。看见一条拒收理由，不是已经该弹给用户。

拒收码取值、协议版本号、字段宽度是规范里的数字，本页不抄。不要另写 怎样对合法对象乱发拒收、怎样骚扰用户、怎样把日志盘写满。

## 官方为什么这样拆

- **调试句 不是已经是官方原因：官方写不同实现可以用不同的句子。**
- **调试句 不是已经写进共识：官方把人读字符串写成调试专用。**
- **调试句 不是已经该给用户看：官方写这条字符串不应当给用户看。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是官方原因 | 不是已经是官方原因 | 不是已经reject-cost（44） |
| 已经写进共识 | 不是已经写进共识 | 不是已经mempool-dump（253） |
| 已经该弹给用户 | 不是已经该弹给用户 | 不是已经1265 rej61-notill |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-61 reason not already official / not already consensus / not already for-users 正式三事（254 余量），必须分开是不是已经是官方原因、是不是已经写进共识、是不是已经该弹给用户。可以跳过「看见拒收消息就已经共识非法」。不要另写 怎样对合法对象乱发拒收、怎样骚扰用户、怎样把日志盘写满。254 reject vs consensus bundled unbundling 在本页 item 2 续；续 [`worked-example-rej61-notpol-vs-bundled.md`](worked-example-rej61-notpol-vs-bundled.md)（不变量 1267 item 3）。

## 本页不抄

- 拒收码取值、协议版本号、字段宽度、哈希宽度。
- 怎样对合法对象乱发拒收、怎样骚扰用户、怎样把日志盘写满。
