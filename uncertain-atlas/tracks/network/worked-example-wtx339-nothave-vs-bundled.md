# 例：看见按 wtxid 通告不是已经有那笔交易；看见按 wtxid 通告不是已经收下；看见拒过一份见证不是这个 txid 已经永远不该下

**层次**：网络 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-339](https://github.com/bitcoin/bips/blob/master/bip-0339.mediawiki)（Deployed, Peer Services）。  
**对应课文**：[L3.4](../../courses/level-03-bitcoin/L03-M04-network-and-eclipse.md)、[L3.7](../../courses/level-03-bitcoin/L03-M07-segwit-soft-fork.md)、[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：index/03 共识行、Ethereum 行、M5.4、L5.1、L5.4、05b。本页是「BIP-339 wtxid-ann not already have / not already accepted / not already never-again 正式三事（248 余量）/ not 1247 wtx339-nothave interchangeable / not 248 wtxidrelay-vs-have bundled interchangeable」，不是 wtxidrelay bundled（248），也不是 txid 就已经等于 wtxid（152），也不是发了 sendheaders 就已经有块（247）。不要另写 怎样改见证挡住转发、怎样用旧类型重放、怎样在应答之后补发信号。

## 官方三件事

1. **看见按 wtxid 通告 / 看见按 wtxid 通告 这份对象 is not already 已经有那笔交易 interchangeable，也不是已经 wtxidrelay bundled（248） interchangeable / 1247 wtx339-nothave interchangeable / 1248 wtx339-notswitch interchangeable，也不是已经 BIP-339 wtxid-ann not already have / not already accepted / not already never-again 正式三事 bundled（248 item 1 余量） interchangeable / 248 wtxidrelay item 1 interchangeable。**  
   官方写：历史上库存通告按 txid，即使隔离见证已经上线也是这样。txid 不承诺见证。见证可以被改而不改 txid，于是节点拒过一份带见证的交易之后，别的对等节点再用同一个 txid 通告，一般还得再下一次。反过来，若拒过这个 txid 就再也不下，第三者只要改见证、通告一份非法交易，就能挡住合法那份。看见按 wtxid 通告，不是已经有那笔交易，也不是已经收下，也不是已经验完。看见拒过一份见证，不是这个 txid 已经永远不该下。

2. **看见按 wtxid 通告 / 看见按 wtxid 通告 / 这份对象 is not already 已经收下 interchangeable，也不是已经 wtxidrelay bundled（248） interchangeable / 1247 wtx339-nothave interchangeable / 1249 wtx339-notold interchangeable，也不是已经 txid-wtxid interchangeable / 152 txid-wtxid interchangeable。**  
   官方把按 wtxid 通告和已经收下写成两件。看见按 wtxid 通告，不是已经收下。

3. **看见拒过一份见证 / 看见按 wtxid 通告 / 这份对象 is not already 这个 txid 已经永远不该下 interchangeable，也不是已经 wtxidrelay bundled（248） interchangeable / 1247 wtx339-nothave interchangeable / 1248 wtx339-notswitch interchangeable，也不是已经 sendheaders-have interchangeable / 247 sendheaders-have interchangeable。**  
   官方把拒过一份见证和这个 txid 已经永远不该下写成两件。看见拒过一份见证，不是这个 txid 已经永远不该下。

协议版本号、库存类型取值、空消息编码是规范里的数字，本页不抄。不要另写 怎样改见证挡住转发、怎样用旧类型重放、怎样在应答之后补发信号。

## 官方为什么这样拆

- **按 wtxid 通告 不是已经有交易：官方只换通告用的哈希。看见哈希到了，不是交易已经在手里。**
- **按 wtxid 通告 不是已经收下：官方把通告和收下、验完写成两件。**
- **拒过一份见证 不是这个 txid 已经永远不该下：官方写若拒过这个 txid 就再也不下，第三者改见证就能挡住合法那份。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经有那笔交易 | 不是已经有那笔交易 | 不是已经txid-wtxid（152） |
| 已经收下 | 不是已经收下 | 不是已经sendheaders-have（247） |
| 这个 txid 已经永远不该下 | 不是这个 txid 已经永远不该下 | 不是已经1248 wtx339-notswitch |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-339 wtxid-ann not already have / not already accepted / not already never-again 正式三事（248 余量），必须分开是不是已经有那笔交易、是不是已经收下、是不是这个 txid 已经永远不该下。可以跳过「看见按 wtxid 通告就已经有那笔交易」。不要另写 怎样改见证挡住转发、怎样用旧类型重放、怎样在应答之后补发信号。248 wtxidrelay vs have bundled unbundling 在本页 item 1 启动；续 [`worked-example-wtx339-notswitch-vs-bundled.md`](worked-example-wtx339-notswitch-vs-bundled.md)（不变量 1248 item 2）。

## 本页不抄

- 协议版本号、库存类型取值、空消息字段、见证序列化步骤。
- 怎样改见证挡住转发、怎样用旧类型重放、怎样在应答之后补发信号。
