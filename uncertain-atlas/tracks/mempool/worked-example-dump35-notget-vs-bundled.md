# 例：看见回了内存池库存不是已经下载那些交易；看见只肯给最近转发过的不是已经支持整池查询；看见仍只肯给最近转发过的不是那些交易已经不在池里

**层次**：内存池 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-35](https://github.com/bitcoin/bips/blob/master/bip-0035.mediawiki)（Deployed, Peer Services）。  
**对应课文**：[L3.2](../../courses/level-03-bitcoin/L03-M02-fees-and-standardness.md)、[L9.2](../../courses/level-09-systems/L09-M02-mempool.md)。  
**不要写进**：index/03 共识行、Ethereum 行、M5.4、L5.1、L5.4、05b。本页是「BIP-35 dump-get not already downloaded / not already full-query / not already gone 正式三事（253 余量）/ not 1263 dump35-notget interchangeable / not 253 mempool-dump-vs-have bundled interchangeable」，不是 dump bundled（253），也不是已经 erlay-have（249），也不是已经 feefilter-reject（245）。不要另写 怎样把别人的内存池整包拉走、怎样按内存池认人、怎样用过大库存打人。

## 官方三件事

1. **看见回了内存池库存 / 看见只肯给最近转发过的 这份对象 is not already 已经下载那些交易 interchangeable，也不是已经 dump bundled（253） interchangeable / 1263 dump35-notget interchangeable / 1262 dump35-nothave interchangeable，也不是已经 BIP-35 dump-get not already downloaded / not already full-query / not already gone 正式三事 bundled（253 item 2 余量） interchangeable / 253 dump item 2 interchangeable。**  
   官方写：对库存通告的通常反应是去索取。可参考实现会忽略「最近没转发过」的交易哈希索取。要支持本页，实现必须把索取扩到能问内存池。看见回了内存池库存，不是已经下载那些交易。看见仍只肯给最近转发过的，不是已经支持整池查询，也不是那些交易已经不在池里。

2. **看见只肯给最近转发过的 / 看见回了内存池库存 / 这份对象 is not already 已经支持整池查询 interchangeable，也不是已经 dump bundled（253） interchangeable / 1263 dump35-notget interchangeable / 1264 dump35-notver interchangeable，也不是已经 erlay-have interchangeable / 249 erlay-have interchangeable。**  
   官方把只肯给最近转发过的和已经支持整池查询写成两件。看见只肯给最近转发过的，不是已经支持整池查询。

3. **看见仍只肯给最近转发过的 / 看见回了内存池库存 / 这份对象 is not already 那些交易已经不在池里 interchangeable，也不是已经 dump bundled（253） interchangeable / 1263 dump35-notget interchangeable / 1262 dump35-nothave interchangeable，也不是已经 feefilter-reject interchangeable / 245 feefilter-reject interchangeable。**  
   官方把仍只肯给最近转发过的和那些交易已经不在池里写成两件。看见仍只肯给最近转发过的，不是那些交易已经不在池里。

协议版本号、库存条数上限、库存类型取值是规范里的数字，本页不抄。不要另写 怎样把别人的内存池整包拉走、怎样按内存池认人、怎样用过大库存打人。

## 官方为什么这样拆

- **能列 不是已经能索取：官方单独要求把索取扩到内存池。看见名单，不是已经能把整池拉完。**
- **只肯给最近转发过的 不是已经支持整池查询：官方写必须把索取扩到能问内存池。**
- **仍只肯给最近转发过的 不是那些交易已经不在池里：官方只写参考实现会忽略最近没转发过的索取。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经下载那些交易 | 不是已经下载那些交易 | 不是已经erlay-have（249） |
| 已经支持整池查询 | 不是已经支持整池查询 | 不是已经feefilter-reject（245） |
| 那些交易已经不在池里 | 不是那些交易已经不在池里 | 不是已经1262 dump35-nothave |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-35 dump-get not already downloaded / not already full-query / not already gone 正式三事（253 余量），必须分开是不是已经下载那些交易、是不是已经支持整池查询、是不是那些交易已经不在池里。可以跳过「看见内存池查询回了一串库存就已经有那些交易」。不要另写 怎样把别人的内存池整包拉走、怎样按内存池认人、怎样用过大库存打人。253 mempool vs have bundled unbundling 在本页 item 2 续；续 [`worked-example-dump35-notver-vs-bundled.md`](worked-example-dump35-notver-vs-bundled.md)（不变量 1264 item 3）。

## 本页不抄

- 协议版本号、库存条数上限、库存类型取值。
- 怎样把别人的内存池整包拉走、怎样按内存池认人、怎样用过大库存打人。
