# 例：看见回了一串库存不是已经有那些交易；看见回了一串库存不是已经收下；看见回了空库存不是这个节点已经没有未确认池

**层次**：内存池 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-35](https://github.com/bitcoin/bips/blob/master/bip-0035.mediawiki)（Deployed, Peer Services）。  
**对应课文**：[L3.2](../../courses/level-03-bitcoin/L03-M02-fees-and-standardness.md)、[L9.2](../../courses/level-09-systems/L09-M02-mempool.md)。  
**不要写进**：index/03 共识行、Ethereum 行、M5.4、L5.1、L5.4、05b。本页是「BIP-35 dump-inv not already have / not already accepted / not already empty-pool 正式三事（253 余量）/ not 1262 dump35-nothave interchangeable / not 253 mempool-dump-vs-have bundled interchangeable」，不是 dump bundled（253），也不是已经 feefilter-reject（245），也不是已经 wtxidrelay-have（248）。不要另写 怎样把别人的内存池整包拉走、怎样按内存池认人、怎样用过大库存打人。

## 官方三件事

1. **看见回了一串库存 / 看见回了一串库存 这份对象 is not already 已经有那些交易 interchangeable，也不是已经 dump bundled（253） interchangeable / 1262 dump35-nothave interchangeable / 1263 dump35-notget interchangeable，也不是已经 BIP-35 dump-inv not already have / not already accepted / not already empty-pool 正式三事 bundled（253 item 1 余量） interchangeable / 253 dump item 1 interchangeable。**  
   官方写：本页新增一条空的内存池查询消息。收到之后，节点用库存通告回自己交易内存池里所有交易的哈希；若池是空的，也可以不回。看见回了一串库存，不是已经有那些交易，也不是已经收下，也不是已经验完，也不是已经写进共识。看见回了空库存，不是这个节点已经没有未确认池，也不是链已经空。

2. **看见回了一串库存 / 看见回了一串库存 / 这份对象 is not already 已经收下 interchangeable，也不是已经 dump bundled（253） interchangeable / 1262 dump35-nothave interchangeable / 1264 dump35-notver interchangeable，也不是已经 feefilter-reject interchangeable / 245 feefilter-reject interchangeable。**  
   官方把回了一串库存和已经收下写成两件。看见回了一串库存，不是已经收下。

3. **看见回了空库存 / 看见回了一串库存 / 这份对象 is not already 这个节点已经没有未确认池 interchangeable，也不是已经 dump bundled（253） interchangeable / 1262 dump35-nothave interchangeable / 1263 dump35-notget interchangeable，也不是已经 wtxidrelay-have interchangeable / 248 wtxidrelay-have interchangeable。**  
   官方把回了空库存和这个节点已经没有未确认池写成两件。看见回了空库存，不是这个节点已经没有未确认池。

协议版本号、库存条数上限、库存类型取值是规范里的数字，本页不抄。不要另写 怎样把别人的内存池整包拉走、怎样按内存池认人、怎样用过大库存打人。

## 官方为什么这样拆

- **库存通告 不是已经有交易：官方只让节点列出此刻池里的哈希。看见名单，不是体已经在请求方手里。**
- **回了一串库存 不是已经收下：官方把列出哈希和收下、验完写成两件。**
- **回了空库存 不是已经没有未确认池：官方写池是空的也可以不回，不是这个节点已经没有池。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经有那些交易 | 不是已经有那些交易 | 不是已经feefilter-reject（245） |
| 已经收下 | 不是已经收下 | 不是已经wtxidrelay-have（248） |
| 这个节点已经没有未确认池 | 不是这个节点已经没有未确认池 | 不是已经1263 dump35-notget |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-35 dump-inv not already have / not already accepted / not already empty-pool 正式三事（253 余量），必须分开是不是已经有那些交易、是不是已经收下、是不是这个节点已经没有未确认池。可以跳过「看见内存池查询回了一串库存就已经有那些交易」。不要另写 怎样把别人的内存池整包拉走、怎样按内存池认人、怎样用过大库存打人。253 mempool vs have bundled unbundling 在本页 item 1 启动；续 [`worked-example-dump35-notget-vs-bundled.md`](worked-example-dump35-notget-vs-bundled.md)（不变量 1263 item 2）。

## 本页不抄

- 协议版本号、库存条数上限、库存类型取值。
- 怎样把别人的内存池整包拉走、怎样按内存池认人、怎样用过大库存打人。
