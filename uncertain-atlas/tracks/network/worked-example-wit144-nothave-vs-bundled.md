# 例：看见带见证的线上序列化不是已经有见证；看见带见证的线上序列化不是已经收下；看见仍用旧序列化不是已经没有见证能力

**层次**：网络 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-144](https://github.com/bitcoin/bips/blob/master/bip-0144.mediawiki)（Deployed, Peer Services）。  
**对应课文**：[L3.4](../../courses/level-03-bitcoin/L03-M04-network-and-eclipse.md)、[L3.7](../../courses/level-03-bitcoin/L03-M07-segwit-soft-fork.md)、[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：index/03 共识行、Ethereum 行、M5.4、L5.1、L5.4、05b。本页是「BIP-144 witness-ser not already have / not already accepted / not already no-capability 正式三事（251 余量）/ not 1256 wit144-nothave interchangeable / not 251 witness-wire-vs-have bundled interchangeable」，不是 witness bundled（251），也不是已经 txid-wtxid（152），也不是已经 wtxidrelay-have（248）。不要另写 怎样拼能骗过旧解析器的字节、怎样用索取类型重放、怎样按服务位认出节点。

## 官方三件事

1. **看见带见证的线上序列化 / 看见带见证的线上序列化 这份对象 is not already 已经有见证 interchangeable，也不是已经 witness bundled（251） interchangeable / 1256 wit144-nothave interchangeable / 1257 wit144-notsend interchangeable，也不是已经 BIP-144 witness-ser not already have / not already accepted / not already no-capability 正式三事 bundled（251 item 1 余量） interchangeable / 251 witness item 1 interchangeable。**  
   官方写：为了传播承诺了隔离见证结构的交易和块，必须新增消息和序列化，好让对等节点能宣布自己支持、能转发见证、能向别人要，并且不把旧节点弄坏。新序列化带标记和旗标，让不支持本页的解析器永远不会把它当成一笔合法旧交易。若见证是空的，必须用旧序列化。看见带见证的线上序列化，不是已经有见证，也不是已经收下，也不是已经验完。看见仍用旧序列化，不是已经没有见证能力，也不是这笔已经没有见证结构。

2. **看见带见证的线上序列化 / 看见带见证的线上序列化 / 这份对象 is not already 已经收下 interchangeable，也不是已经 witness bundled（251） interchangeable / 1256 wit144-nothave interchangeable / 1258 wit144-notold interchangeable，也不是已经 txid-wtxid interchangeable / 152 txid-wtxid interchangeable。**  
   官方把带见证的线上序列化和已经收下写成两件。看见带见证的线上序列化，不是已经收下。

3. **看见仍用旧序列化 / 看见带见证的线上序列化 / 这份对象 is not already 已经没有见证能力 interchangeable，也不是已经 witness bundled（251） interchangeable / 1256 wit144-nothave interchangeable / 1257 wit144-notsend interchangeable，也不是已经 wtxidrelay-have interchangeable / 248 wtxidrelay-have interchangeable。**  
   官方把仍用旧序列化和已经没有见证能力写成两件。看见仍用旧序列化，不是已经没有见证能力。

标记、旗标、位编号、库存类型取值是规范里的数字，本页不抄。不要另写 怎样拼能骗过旧解析器的字节、怎样用索取类型重放、怎样按服务位认出节点。

## 官方为什么这样拆

- **线上序列化 不是已经有见证：官方只换消息怎么装。看见新格式到了，不是见证已经验完。**
- **线上序列化 不是已经收下：官方把装格式和收下、验完写成两件。**
- **仍用旧序列化 不是已经没有见证能力：官方写见证空的必须仍走旧格式。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经有见证 | 不是已经有见证 | 不是已经txid-wtxid（152） |
| 已经收下 | 不是已经收下 | 不是已经wtxidrelay-have（248） |
| 已经没有见证能力 | 不是已经没有见证能力 | 不是已经1257 wit144-notsend |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-144 witness-ser not already have / not already accepted / not already no-capability 正式三事（251 余量），必须分开是不是已经有见证、是不是已经收下、是不是已经没有见证能力。可以跳过「看见带见证的线上序列化就已经有见证」。不要另写 怎样拼能骗过旧解析器的字节、怎样用索取类型重放、怎样按服务位认出节点。251 witness vs have bundled unbundling 在本页 item 1 启动；续 [`worked-example-wit144-notsend-vs-bundled.md`](worked-example-wit144-notsend-vs-bundled.md)（不变量 1257 item 2）。

## 本页不抄

- 标记 / 旗标取值、字段宽度、服务位编号、库存类型取值、空见证编码步骤。
- 怎样拼能骗过旧解析器的字节、怎样用索取类型重放、怎样按服务位认出节点。
