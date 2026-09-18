# 例：看见对账失败退回洪水不是库存通告已经退役；看见一份素描不是已经有那些交易；看见短标识不是已经有带见证的哈希

**层次**：网络 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-330](https://github.com/bitcoin/bips/blob/master/bip-0330.mediawiki)（Draft, Peer Services）。  
**对应课文**：[L3.4](../../courses/level-03-bitcoin/L03-M04-network-and-eclipse.md)、[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)、[L9.2](../../courses/level-09-systems/L09-M02-mempool.md)。  
**不要写进**：index/03 共识行、Ethereum 行、M5.4、L5.1、L5.4、05b。本页是「BIP-330 sketch not already have / not already illegal / not already wtxid 正式三事（249 余量）/ not 1252 erl330-notflood interchangeable / not 249 erlay-vs-have bundled interchangeable」，不是 erlay bundled（249），也不是已经 txid-wtxid（152），也不是已经 announce-received（36）。不要另写 怎样造碰撞短标识、怎样拖住对账、怎样用失败旗标灌库存通告。

## 官方三件事

1. **看见对账失败退回洪水 / 看见一份素描 这份对象 is not already 库存通告已经退役 interchangeable，也不是已经 erlay bundled（249） interchangeable / 1252 erl330-notflood interchangeable / 1250 erl330-nothave interchangeable，也不是已经 BIP-330 sketch not already have / not already illegal / not already wtxid 正式三事 bundled（249 item 3 余量） interchangeable / 249 erlay item 3 interchangeable。**  
   官方写：对账主要是按请求传一份通告集合的素描并尝试解码。解不开可以再要一份加长素描，也可以直接标失败结束。标失败时，应当把该通告集合里的交易再按库存通告一遍，当作退回洪水。标成功时，对方缺的短标识走对账差额消息，己方缺的短标识再发库存通告。看见对账失败退回洪水，不是库存通告已经退役。看见一份素描，不是已经有那些交易，也不是差额已经在手里。看见短标识，不是已经有带见证的哈希，也不是已经收下。

2. **看见一份素描 / 看见对账失败退回洪水 / 这份对象 is not already 已经有那些交易 interchangeable，也不是已经 erlay bundled（249） interchangeable / 1252 erl330-notflood interchangeable / 1251 erl330-notsig interchangeable，也不是已经 txid-wtxid interchangeable / 152 txid-wtxid interchangeable。**  
   官方把一份素描和已经有那些交易写成两件。看见一份素描，不是已经有那些交易。

3. **看见短标识 / 看见对账失败退回洪水 / 这份对象 is not already 已经有带见证的哈希 interchangeable，也不是已经 erlay bundled（249） interchangeable / 1252 erl330-notflood interchangeable / 1250 erl330-nothave interchangeable，也不是已经 announce-received interchangeable / 36 announce-received interchangeable。**  
   官方把短标识和已经有带见证的哈希写成两件。看见短标识，不是已经有带见证的哈希。

短标识怎么算、素描有限域、容量公式是规范里的数字，本页不抄。不要另写 怎样造碰撞短标识、怎样拖住对账、怎样用失败旗标灌库存通告。

## 官方为什么这样拆

- **退回洪水 不是库存通告已经退役：官方标失败时应当再按库存通告一遍。**
- **一份素描 不是已经有那些交易：官方解完仍要再发库存通告。看见素描到了，不是交易已经在手里。**
- **短标识 不是已经有带见证的哈希：官方短标识只是通告集合里的压缩记号。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 库存通告已经退役 | 不是库存通告已经退役 | 不是已经txid-wtxid（152） |
| 已经有那些交易 | 不是已经有那些交易 | 不是已经announce-received（36） |
| 已经有带见证的哈希 | 不是已经有带见证的哈希 | 不是已经1250 erl330-nothave |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-330 sketch not already have / not already illegal / not already wtxid 正式三事（249 余量），必须分开是不是库存通告已经退役、是不是已经有那些交易、是不是已经有带见证的哈希。可以跳过「看见对账素描就已经有那些交易」。不要另写 怎样造碰撞短标识、怎样拖住对账、怎样用失败旗标灌库存通告。249 erlay vs have bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 短标识盐和哈希步骤、素描有限域、容量与 q 公式、字段宽度、版本号取值。
- 怎样造碰撞短标识、怎样拖住对账、怎样用失败旗标灌库存通告。
