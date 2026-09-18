# 例：看见协议版本够了不是已经在答内存池查询；看见开了能服数据不是已经在答；看见过大的库存被丢掉不是已经共识非法

**层次**：内存池 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-35](https://github.com/bitcoin/bips/blob/master/bip-0035.mediawiki)（Deployed, Peer Services）。  
**对应课文**：[L3.2](../../courses/level-03-bitcoin/L03-M02-fees-and-standardness.md)、[L9.2](../../courses/level-09-systems/L09-M02-mempool.md)。  
**不要写进**：index/03 共识行、Ethereum 行、M5.4、L5.1、L5.4、05b。本页是「BIP-35 dump-disc not already answering / not already serving / not already illegal 正式三事（253 余量）/ not 1264 dump35-notver interchangeable / not 253 mempool-dump-vs-have bundled interchangeable」，不是 dump bundled（253），也不是已经 policy-consensus（144），也不是已经 bloom-retired（252）。不要另写 怎样把别人的内存池整包拉走、怎样按内存池认人、怎样用过大库存打人。

## 官方三件事

1. **看见协议版本够了 / 看见开了能服数据 这份对象 is not already 已经在答内存池查询 interchangeable，也不是已经 dump bundled（253） interchangeable / 1264 dump35-notver interchangeable / 1262 dump35-nothave interchangeable，也不是已经 BIP-35 dump-disc not already answering / not already serving / not already illegal 正式三事 bundled（253 item 3 余量） interchangeable / 253 dump item 3 interchangeable。**  
   官方写：功能发现要同时看协议版本够不够，以及服务位里有没有「能服数据」那一位。旧客户端改完之后仍百分之百兼容、仍能互操作。官方还写：既有实现会丢掉条数过大的库存通告。看见协议版本够了，不是已经在答内存池查询。看见开了「能服数据」，不是已经在答。看见过大的库存被丢掉，不是那些交易已经共识非法，也不是剩下的已经在手里。

2. **看见开了能服数据 / 看见协议版本够了 / 这份对象 is not already 已经在答 interchangeable，也不是已经 dump bundled（253） interchangeable / 1264 dump35-notver interchangeable / 1263 dump35-notget interchangeable，也不是已经 policy-consensus interchangeable / 144 policy-consensus interchangeable。**  
   官方把开了能服数据和已经在答写成两件。看见开了能服数据，不是已经在答。

3. **看见过大的库存被丢掉 / 看见协议版本够了 / 这份对象 is not already 已经共识非法 interchangeable，也不是已经 dump bundled（253） interchangeable / 1264 dump35-notver interchangeable / 1262 dump35-nothave interchangeable，也不是已经 bloom-retired interchangeable / 252 bloom-retired interchangeable。**  
   官方把过大的库存被丢掉和已经共识非法写成两件。看见过大的库存被丢掉，不是已经共识非法。

协议版本号、库存条数上限、库存类型取值是规范里的数字，本页不抄。不要另写 怎样把别人的内存池整包拉走、怎样按内存池认人、怎样用过大库存打人。

## 官方为什么这样拆

- **版本够了 不是已经在答：官方把发现写成版本加服务位。看见数字，不是已经打开整池查询。**
- **开了能服数据 不是已经在答：官方要同时看版本和服务位。**
- **过大库存被丢掉 不是已经共识非法：官方只写既有实现会丢掉条数过大的库存通告。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经在答内存池查询 | 不是已经在答内存池查询 | 不是已经policy-consensus（144） |
| 已经在答 | 不是已经在答 | 不是已经bloom-retired（252） |
| 已经共识非法 | 不是已经共识非法 | 不是已经1262 dump35-nothave |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-35 dump-disc not already answering / not already serving / not already illegal 正式三事（253 余量），必须分开是不是已经在答内存池查询、是不是已经在答、是不是已经共识非法。可以跳过「看见内存池查询回了一串库存就已经有那些交易」。不要另写 怎样把别人的内存池整包拉走、怎样按内存池认人、怎样用过大库存打人。253 mempool vs have bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 协议版本号、库存条数上限、库存类型取值。
- 怎样把别人的内存池整包拉走、怎样按内存池认人、怎样用过大库存打人。
