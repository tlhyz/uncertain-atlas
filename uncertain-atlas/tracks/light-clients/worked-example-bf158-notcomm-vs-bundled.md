# 例：看见排除了 OP_RETURN不是已经有共识承诺；看见服务位不是已经在答别的过滤器类型；看见排除了 OP_RETURN不是已经写了 157 那套头链

**层次**：轻客户端 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-158](https://github.com/bitcoin/bips/blob/master/bip-0158.mediawiki)（Deployed, Peer Services；依赖 157）。  
**对应课文**：[L3.5](../../courses/level-03-bitcoin/L03-M05-full-node-and-spv.md)、[L9.6](../../courses/level-09-systems/L09-M06-light-clients.md)。  
**不要写进**：`index/03` 共识行、Ethereum 行、M5.4、L5.1、L5.4、05b。本页是「BIP-158 exclude-opreturn not already consensus / not already other-type / not already header-chain 正式三事（244 余量）/ not 1282 bf158-notcomm interchangeable / not 244 basic-filter-vs-relevant bundled interchangeable」，不是 basic filter vs relevant bundled（244），也不是已经 cfilter-have（243），也不是已经 must-name-trust（22）。不要另写 怎样造对得上的假项、怎样调假阳性、怎样按编码复刻。

## 官方三件事

1. **看见排除了 OP_RETURN / 看见排除了 OP_RETURN 这份对象 is not already 已经有共识承诺 interchangeable，也不是已经 basic filter vs relevant bundled（244） interchangeable / 1282 bf158-notcomm interchangeable / 1280 bf158-nottx interchangeable，也不是已经 BIP-158 exclude-opreturn not already consensus / not already other-type / not already header-chain 正式三事 bundled（244 item 3 余量） interchangeable / 244 basic item 3 interchangeable。**  
   官方把排除了 OP_RETURN和已经有共识承诺写成两件。看见排除了 OP_RETURN，不是已经有共识承诺。

2. **看见服务位 / 看见排除了 OP_RETURN / 这份对象 is not already 已经在答别的过滤器类型 interchangeable，也不是已经 basic filter vs relevant bundled（244） interchangeable / 1282 bf158-notcomm interchangeable / 1281 bf158-notrel interchangeable，也不是已经 cfilter-have interchangeable / 243 cfilter-have interchangeable。**  
   官方把服务位和已经在答别的过滤器类型写成两件。看见服务位，不是已经在答别的过滤器类型。

3. **看见排除了 OP_RETURN / 看见服务位 / 这份对象 is not already 已经写了 157 那套头链 interchangeable，也不是已经 basic filter vs relevant bundled（244） interchangeable / 1282 bf158-notcomm interchangeable / 1280 bf158-nottx interchangeable，也不是已经 must-name-trust interchangeable / 22 must-name-trust interchangeable。**  
   官方把排除了 OP_RETURN和已经写了 157 那套头链写成两件。看见排除了 OP_RETURN，不是已经写了 157 那套头链。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样造对得上的假项、怎样调假阳性、怎样按编码复刻。

## 官方为什么这样拆

- **排除了 OP_RETURN 不是已经有共识承诺：官方为了以后能承诺才排除。**
- **服务位 不是已经在答别的过滤器类型：官方把服务位只钉这一种基本类型。**
- **服务位 不是已经写了 157 那套头链：官方把构造和点对点索取写成两页。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经有共识承诺 | 不是已经有共识承诺 | 不是已经cfilter-have（243） |
| 已经在答别的过滤器类型 | 不是已经在答别的过滤器类型 | 不是已经must-name-trust（22） |
| 已经写了 157 那套头链 | 不是已经写了 157 那套头链 | 不是已经1280 bf158-nottx |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-158 exclude-opreturn not already consensus / not already other-type / not already header-chain 正式三事（244 余量），必须分开是不是已经有共识承诺、是不是已经在答别的过滤器类型、是不是已经写了 157 那套头链。可以跳过「看见基本过滤器对上就已经是我的付款」。不要另写 怎样造对得上的假项、怎样调假阳性、怎样按编码复刻。244 basic filter vs relevant bundled unbundling 在本页 item 3 完成；本页收束本批。

## 本页不抄

- 假阳性参数、编码步骤、哈希参数、类型号、服务位取值、测试向量。
- 怎样造对得上的假项、怎样调假阳性、怎样按编码复刻。
