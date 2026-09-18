# 例：看见发了 sendtxrcncl 不是已经在对账；看见发了 wtxidrelay 不是对账已经打开；看见协议两边都写了支持不是已经对齐过一轮

**层次**：网络 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-330](https://github.com/bitcoin/bips/blob/master/bip-0330.mediawiki)（Draft, Peer Services）。  
**对应课文**：[L3.4](../../courses/level-03-bitcoin/L03-M04-network-and-eclipse.md)、[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)、[L9.2](../../courses/level-09-systems/L09-M02-mempool.md)。  
**不要写进**：index/03 共识行、Ethereum 行、M5.4、L5.1、L5.4、05b。本页是「BIP-330 sendtxrcncl not already reconciling / not already opened / not already aligned 正式三事（249 余量）/ not 1251 erl330-notsig interchangeable / not 249 erlay-vs-have bundled interchangeable」，不是 erlay bundled（249），也不是已经 wtxidrelay-have（248），也不是已经 feature-enabled（259）。不要另写 怎样造碰撞短标识、怎样拖住对账、怎样用失败旗标灌库存通告。

## 官方三件事

1. **看见发了 sendtxrcncl / 看见发了 wtxidrelay 这份对象 is not already 已经在对账 interchangeable，也不是已经 erlay bundled（249） interchangeable / 1251 erl330-notsig interchangeable / 1250 erl330-nothave interchangeable，也不是已经 BIP-330 sendtxrcncl not already reconciling / not already opened / not already aligned 正式三事 bundled（249 item 2 余量） interchangeable / 249 erlay item 2 interchangeable。**  
   官方写：这条消息宣布支持对账。应当只发一次。应当在握手应答之前发出，并且同时带着 wtxidrelay（先后不论）。应答之后才发的，发送方应当被断开。应答之前发了、但到应答时还没收到 wtxidrelay 的，应当忽略对账信号，连接照常，只当不支持对账。看见发了 sendtxrcncl，不是已经在对账，也不是已经有通告集合。看见发了 wtxidrelay，不是对账已经打开。看见协议两边都写了支持，不是已经对齐过一轮。

2. **看见发了 wtxidrelay / 看见发了 sendtxrcncl / 这份对象 is not already 对账已经打开 interchangeable，也不是已经 erlay bundled（249） interchangeable / 1251 erl330-notsig interchangeable / 1252 erl330-notflood interchangeable，也不是已经 wtxidrelay-have interchangeable / 248 wtxidrelay-have interchangeable。**  
   官方把发了 wtxidrelay 和对账已经打开写成两件。看见发了 wtxidrelay，不是对账已经打开。

3. **看见协议两边都写了支持 / 看见发了 sendtxrcncl / 这份对象 is not already 已经对齐过一轮 interchangeable，也不是已经 erlay bundled（249） interchangeable / 1251 erl330-notsig interchangeable / 1250 erl330-nothave interchangeable，也不是已经 feature-enabled interchangeable / 259 feature-enabled interchangeable。**  
   官方把协议两边都写了支持和已经对齐过一轮写成两件。看见协议两边都写了支持，不是已经对齐过一轮。

短标识怎么算、素描有限域、容量公式是规范里的数字，本页不抄。不要另写 怎样造碰撞短标识、怎样拖住对账、怎样用失败旗标灌库存通告。

## 官方为什么这样拆

- **握手信号 不是已经在对账：官方把「能懂」钉在应答之前。看见发了信号，不是已经对齐过集合。**
- **发了 wtxidrelay 不是对账已经打开：官方写必须同时带着 wtxidrelay，缺了应当忽略对账信号。**
- **两边都写了支持 不是已经对齐过一轮：官方写两端都发了之后，发起连接的一方才发起对账请求。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经在对账 | 不是已经在对账 | 不是已经wtxidrelay-have（248） |
| 对账已经打开 | 不是对账已经打开 | 不是已经feature-enabled（259） |
| 已经对齐过一轮 | 不是已经对齐过一轮 | 不是已经1250 erl330-nothave |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-330 sendtxrcncl not already reconciling / not already opened / not already aligned 正式三事（249 余量），必须分开是不是已经在对账、是不是对账已经打开、是不是已经对齐过一轮。可以跳过「看见对账素描就已经有那些交易」。不要另写 怎样造碰撞短标识、怎样拖住对账、怎样用失败旗标灌库存通告。249 erlay vs have bundled unbundling 在本页 item 2 续；续 [`worked-example-erl330-notflood-vs-bundled.md`](worked-example-erl330-notflood-vs-bundled.md)（不变量 1252 item 3）。

## 本页不抄

- 短标识盐和哈希步骤、素描有限域、容量与 q 公式、字段宽度、版本号取值。
- 怎样造碰撞短标识、怎样拖住对账、怎样用失败旗标灌库存通告。
