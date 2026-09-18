# 例：看见库存通告仍用旧类型不是线上已经没有见证；看见按带见证类型去索取不是已经按 wtxid 通告；看见回了交易消息不是已经验完

**层次**：网络 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-144](https://github.com/bitcoin/bips/blob/master/bip-0144.mediawiki)（Deployed, Peer Services）。  
**对应课文**：[L3.4](../../courses/level-03-bitcoin/L03-M04-network-and-eclipse.md)、[L3.7](../../courses/level-03-bitcoin/L03-M07-segwit-soft-fork.md)、[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：index/03 共识行、Ethereum 行、M5.4、L5.1、L5.4、05b。本页是「BIP-144 old-inv not already no-wit / not already wtxid-ann / not already verified 正式三事（251 余量）/ not 1258 wit144-notold interchangeable / not 251 witness-wire-vs-have bundled interchangeable」，不是 witness bundled（251），也不是已经 wtxidrelay-have（248），也不是已经 sendheaders-have（247）。不要另写 怎样拼能骗过旧解析器的字节、怎样用索取类型重放、怎样按服务位认出节点。

## 官方三件事

1. **看见库存通告仍用旧类型 / 看见按带见证类型去索取 这份对象 is not already 线上已经没有见证 interchangeable，也不是已经 witness bundled（251） interchangeable / 1258 wit144-notold interchangeable / 1256 wit144-nothave interchangeable，也不是已经 BIP-144 old-inv not already no-wit / not already wtxid-ann / not already verified 正式三事 bundled（251 item 3 余量） interchangeable / 251 witness item 3 interchangeable。**  
   官方写：新增的带见证库存类型只用于索取。库存通告本身仍只用旧的交易类型和块类型。理由：现在并不总是用库存通告（还有头通告偏好），而且默认每笔交易、每个块都有见证，旧的只是空的。按带见证类型去索取交易时，应当用不带见证的那个哈希。对等节点回交易消息；见证非空时才改用新序列化。看见库存通告仍用旧类型，不是线上已经没有见证。看见按带见证类型去索取，不是已经按 wtxid 通告，也不是已经有见证。看见回了交易消息，不是已经验完。

2. **看见按带见证类型去索取 / 看见库存通告仍用旧类型 / 这份对象 is not already 已经按 wtxid 通告 interchangeable，也不是已经 witness bundled（251） interchangeable / 1258 wit144-notold interchangeable / 1257 wit144-notsend interchangeable，也不是已经 wtxidrelay-have interchangeable / 248 wtxidrelay-have interchangeable。**  
   官方把按带见证类型去索取和已经按 wtxid 通告写成两件。看见按带见证类型去索取，不是已经按 wtxid 通告。

3. **看见回了交易消息 / 看见库存通告仍用旧类型 / 这份对象 is not already 已经验完 interchangeable，也不是已经 witness bundled（251） interchangeable / 1258 wit144-notold interchangeable / 1256 wit144-nothave interchangeable，也不是已经 sendheaders-have interchangeable / 247 sendheaders-have interchangeable。**  
   官方把回了交易消息和已经验完写成两件。看见回了交易消息，不是已经验完。

标记、旗标、位编号、库存类型取值是规范里的数字，本页不抄。不要另写 怎样拼能骗过旧解析器的字节、怎样用索取类型重放、怎样按服务位认出节点。

## 官方为什么这样拆

- **通告仍用旧类型 不是线上已经没有见证：官方通告仍走旧类型。看见旧库存通告，不是见证已经从网上消失。**
- **按带见证类型去索取 不是已经按 wtxid 通告：官方索取用的是不带见证的那个哈希。**
- **回了交易消息 不是已经验完：官方只规定回消息，不是已经验完脚本。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 线上已经没有见证 | 不是线上已经没有见证 | 不是已经wtxidrelay-have（248） |
| 已经按 wtxid 通告 | 不是已经按 wtxid 通告 | 不是已经sendheaders-have（247） |
| 已经验完 | 不是已经验完 | 不是已经1256 wit144-nothave |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-144 old-inv not already no-wit / not already wtxid-ann / not already verified 正式三事（251 余量），必须分开是不是线上已经没有见证、是不是已经按 wtxid 通告、是不是已经验完。可以跳过「看见带见证的线上序列化就已经有见证」。不要另写 怎样拼能骗过旧解析器的字节、怎样用索取类型重放、怎样按服务位认出节点。251 witness vs have bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 标记 / 旗标取值、字段宽度、服务位编号、库存类型取值、空见证编码步骤。
- 怎样拼能骗过旧解析器的字节、怎样用索取类型重放、怎样按服务位认出节点。
