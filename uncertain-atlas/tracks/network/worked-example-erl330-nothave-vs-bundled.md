# 例：看见一次对账不是已经有那些交易；看见对账还在用库存通告不是库存通告已经退役；看见只向一小撮邻居发洪水不是全网已经齐

**层次**：网络 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-330](https://github.com/bitcoin/bips/blob/master/bip-0330.mediawiki)（Draft, Peer Services）。  
**对应课文**：[L3.4](../../courses/level-03-bitcoin/L03-M04-network-and-eclipse.md)、[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)、[L9.2](../../courses/level-09-systems/L09-M02-mempool.md)。  
**不要写进**：index/03 共识行、Ethereum 行、M5.4、L5.1、L5.4、05b。本页是「BIP-330 recon not already have / not already flood-retired / not already net-wide 正式三事（249 余量）/ not 1250 erl330-nothave interchangeable / not 249 erlay-vs-have bundled interchangeable」，不是 erlay bundled（249），也不是已经 wtxidrelay-have（248），也不是已经 feefilter-reject（245）。不要另写 怎样造碰撞短标识、怎样拖住对账、怎样用失败旗标灌库存通告。

## 官方三件事

1. **看见一次对账 / 看见对账还在用库存通告 这份对象 is not already 已经有那些交易 interchangeable，也不是已经 erlay bundled（249） interchangeable / 1250 erl330-nothave interchangeable / 1251 erl330-notsig interchangeable，也不是已经 BIP-330 recon not already have / not already flood-retired / not already net-wide 正式三事 bundled（249 item 1 余量） interchangeable / 249 erlay item 1 interchangeable。**  
   官方写：本页规定的是两个节点之间对齐交易通告的协议扩展，是更省带宽的转发协议（例如 Erlay）的一块积木。今天每对邻居至少有一个方向要通告 32 字节交易标识。对账可以比按库存通告灌水更省。Erlay 同时用洪水和对账。洪水贵，所以只在必须尽快传到一小撮连接时用。对账是把没靠洪水收到的交易补上，并确认其余连接两边已经对齐。看见一次对账，不是已经有那些交易，也不是库存通告已经退役，也不是已经向每个邻居都通告过。看见只向一小撮邻居发洪水，不是全网已经齐。

2. **看见对账还在用库存通告 / 看见一次对账 / 这份对象 is not already 库存通告已经退役 interchangeable，也不是已经 erlay bundled（249） interchangeable / 1250 erl330-nothave interchangeable / 1252 erl330-notflood interchangeable，也不是已经 wtxidrelay-have interchangeable / 248 wtxidrelay-have interchangeable。**  
   官方把对账还在用库存通告和库存通告已经退役写成两件。看见对账还在用库存通告，不是库存通告已经退役。

3. **看见只向一小撮邻居发洪水 / 看见一次对账 / 这份对象 is not already 全网已经齐 interchangeable，也不是已经 erlay bundled（249） interchangeable / 1250 erl330-nothave interchangeable / 1251 erl330-notsig interchangeable，也不是已经 feefilter-reject interchangeable / 245 feefilter-reject interchangeable。**  
   官方把只向一小撮邻居发洪水和全网已经齐写成两件。看见只向一小撮邻居发洪水，不是全网已经齐。

短标识怎么算、素描有限域、容量公式是规范里的数字，本页不抄。不要另写 怎样造碰撞短标识、怎样拖住对账、怎样用失败旗标灌库存通告。

## 官方为什么这样拆

- **对账 不是已经有交易：官方只把对账写成积木。看见对账消息，不是交易已经在手里。**
- **对账还在用库存通告 不是库存通告已经退役：官方写 Erlay 仍向一小撮连接发库存通告。**
- **只向一小撮邻居发洪水 不是全网已经齐：官方写洪水只在必须尽快传到一小撮连接时用。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经有那些交易 | 不是已经有那些交易 | 不是已经wtxidrelay-have（248） |
| 库存通告已经退役 | 不是库存通告已经退役 | 不是已经feefilter-reject（245） |
| 全网已经齐 | 不是全网已经齐 | 不是已经1251 erl330-notsig |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-330 recon not already have / not already flood-retired / not already net-wide 正式三事（249 余量），必须分开是不是已经有那些交易、是不是库存通告已经退役、是不是全网已经齐。可以跳过「看见对账素描就已经有那些交易」。不要另写 怎样造碰撞短标识、怎样拖住对账、怎样用失败旗标灌库存通告。249 erlay vs have bundled unbundling 在本页 item 1 启动；续 [`worked-example-erl330-notsig-vs-bundled.md`](worked-example-erl330-notsig-vs-bundled.md)（不变量 1251 item 2）。

## 本页不抄

- 短标识盐和哈希步骤、素描有限域、容量与 q 公式、字段宽度、版本号取值。
- 怎样造碰撞短标识、怎样拖住对账、怎样用失败旗标灌库存通告。
