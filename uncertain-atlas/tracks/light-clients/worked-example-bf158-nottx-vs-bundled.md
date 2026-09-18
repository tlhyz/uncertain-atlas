# 例：看见装了花费脚本和收款脚本不是已经有那笔交易；看见对上了一个脚本不是已经有附言数据；看见装了花费脚本和收款脚本不是已经花掉

**层次**：轻客户端 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-158](https://github.com/bitcoin/bips/blob/master/bip-0158.mediawiki)（Deployed, Peer Services；依赖 157）。  
**对应课文**：[L3.5](../../courses/level-03-bitcoin/L03-M05-full-node-and-spv.md)、[L9.6](../../courses/level-09-systems/L09-M06-light-clients.md)。  
**不要写进**：`index/03` 共识行、Ethereum 行、M5.4、L5.1、L5.4、05b。本页是「BIP-158 scripts not already have-tx / not already have-opreturn / not already spent 正式三事（244 余量）/ not 1280 bf158-nottx interchangeable / not 244 basic-filter-vs-relevant bundled interchangeable」，不是 basic filter vs relevant bundled（244），也不是已经 cfilter-have（243），也不是已经 bloom-retired（252）。不要另写 怎样造对得上的假项、怎样调假阳性、怎样按编码复刻。

## 官方三件事

1. **看见装了花费脚本和收款脚本 / 看见装了花费脚本和收款脚本 这份对象 is not already 已经有那笔交易 interchangeable，也不是已经 basic filter vs relevant bundled（244） interchangeable / 1280 bf158-nottx interchangeable / 1281 bf158-notrel interchangeable，也不是已经 BIP-158 scripts not already have-tx / not already have-opreturn / not already spent 正式三事 bundled（244 item 1 余量） interchangeable / 244 basic item 1 interchangeable。**  
   官方把装了花费脚本和收款脚本和已经有那笔交易写成两件。看见装了花费脚本和收款脚本，不是已经有那笔交易。

2. **看见对上了一个脚本 / 看见装了花费脚本和收款脚本 / 这份对象 is not already 已经有附言数据 interchangeable，也不是已经 basic filter vs relevant bundled（244） interchangeable / 1280 bf158-nottx interchangeable / 1282 bf158-notcomm interchangeable，也不是已经 cfilter-have interchangeable / 243 cfilter-have interchangeable。**  
   官方把对上了一个脚本和已经有附言数据写成两件。看见对上了一个脚本，不是已经有附言数据。

3. **看见装了花费脚本和收款脚本 / 看见对上了一个脚本 / 这份对象 is not already 已经花掉 interchangeable，也不是已经 basic filter vs relevant bundled（244） interchangeable / 1280 bf158-nottx interchangeable / 1281 bf158-notrel interchangeable，也不是已经 bloom-retired interchangeable / 252 bloom-retired interchangeable。**  
   官方把装了花费脚本和收款脚本和已经花掉写成两件。看见装了花费脚本和收款脚本，不是已经花掉。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样造对得上的假项、怎样调假阳性、怎样按编码复刻。

## 官方为什么这样拆

- **脚本 不是已经有交易：官方只点名上一份输出脚本和本笔收款脚本。**
- **装了花费脚本和收款脚本 不是已经有附言：官方写所有以 OP_RETURN 开头的输出不要。**
- **对上了一个脚本 不是已经花掉：官方不把匹配写成已经能花。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经有那笔交易 | 不是已经有那笔交易 | 不是已经cfilter-have（243） |
| 已经有附言数据 | 不是已经有附言数据 | 不是已经bloom-retired（252） |
| 已经花掉 | 不是已经花掉 | 不是已经1281 bf158-notrel |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-158 scripts not already have-tx / not already have-opreturn / not already spent 正式三事（244 余量），必须分开是不是已经有那笔交易、是不是已经有附言数据、是不是已经花掉。可以跳过「看见基本过滤器对上就已经是我的付款」。不要另写 怎样造对得上的假项、怎样调假阳性、怎样按编码复刻。244 basic filter vs relevant bundled unbundling 在本页 item 1 启动；续 [`worked-example-bf158-notrel-vs-bundled.md`](worked-example-bf158-notrel-vs-bundled.md)（不变量 1281 item 2）。

## 本页不抄

- 假阳性参数、编码步骤、哈希参数、类型号、服务位取值、测试向量。
- 怎样造对得上的假项、怎样调假阳性、怎样按编码复刻。
