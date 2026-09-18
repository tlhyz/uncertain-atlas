# 例：看见对上不是已经在集合里；看见会多下块不是已经相关；看见对上不是假阳性已经消失

**层次**：轻客户端 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-158](https://github.com/bitcoin/bips/blob/master/bip-0158.mediawiki)（Deployed, Peer Services；依赖 157）。  
**对应课文**：[L3.5](../../courses/level-03-bitcoin/L03-M05-full-node-and-spv.md)、[L9.6](../../courses/level-09-systems/L09-M06-light-clients.md)。  
**不要写进**：`index/03` 共识行、Ethereum 行、M5.4、L5.1、L5.4、05b。本页是「BIP-158 match not already in-set / not already relevant / not already no-false-positive 正式三事（244 余量）/ not 1281 bf158-notrel interchangeable / not 244 basic-filter-vs-relevant bundled interchangeable」，不是 basic filter vs relevant bundled（244），也不是已经 cfilter-have（243），也不是已经 must-name-trust（22）。不要另写 怎样造对得上的假项、怎样调假阳性、怎样按编码复刻。

## 官方三件事

1. **看见对上 / 看见对上 这份对象 is not already 已经在集合里 interchangeable，也不是已经 basic filter vs relevant bundled（244） interchangeable / 1281 bf158-notrel interchangeable / 1280 bf158-nottx interchangeable，也不是已经 BIP-158 match not already in-set / not already relevant / not already no-false-positive 正式三事 bundled（244 item 2 余量） interchangeable / 244 basic item 2 interchangeable。**  
   官方把对上和已经在集合里写成两件。看见对上，不是已经在集合里。

2. **看见会多下块 / 看见对上 / 这份对象 is not already 已经相关 interchangeable，也不是已经 basic filter vs relevant bundled（244） interchangeable / 1281 bf158-notrel interchangeable / 1282 bf158-notcomm interchangeable，也不是已经 cfilter-have interchangeable / 243 cfilter-have interchangeable。**  
   官方把会多下块和已经相关写成两件。看见会多下块，不是已经相关。

3. **看见对上 / 看见会多下块 / 这份对象 is not already 假阳性已经消失 interchangeable，也不是已经 basic filter vs relevant bundled（244） interchangeable / 1281 bf158-notrel interchangeable / 1280 bf158-nottx interchangeable，也不是已经 must-name-trust interchangeable / 22 must-name-trust interchangeable。**  
   官方把对上和假阳性已经消失写成两件。看见对上，不是假阳性已经消失。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样造对得上的假项、怎样调假阳性、怎样按编码复刻。

## 官方为什么这样拆

- **对上 不是已经在集合里：官方写集合外的项也可能对上。**
- **会多下块 不是已经相关：官方把假阳性会多下多少块写成选参数时要看的事。**
- **集合里必中 不是假阳性已经消失：官方把两句写成同一句话。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经在集合里 | 不是已经在集合里 | 不是已经cfilter-have（243） |
| 已经相关 | 不是已经相关 | 不是已经must-name-trust（22） |
| 假阳性已经消失 | 不是假阳性已经消失 | 不是已经1280 bf158-nottx |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-158 match not already in-set / not already relevant / not already no-false-positive 正式三事（244 余量），必须分开是不是已经在集合里、是不是已经相关、是不是假阳性已经消失。可以跳过「看见基本过滤器对上就已经是我的付款」。不要另写 怎样造对得上的假项、怎样调假阳性、怎样按编码复刻。244 basic filter vs relevant bundled unbundling 在本页 item 2 续；续 [`worked-example-bf158-notcomm-vs-bundled.md`](worked-example-bf158-notcomm-vs-bundled.md)（不变量 1282 item 3）。

## 本页不抄

- 假阳性参数、编码步骤、哈希参数、类型号、服务位取值、测试向量。
- 怎样造对得上的假项、怎样调假阳性、怎样按编码复刻。
