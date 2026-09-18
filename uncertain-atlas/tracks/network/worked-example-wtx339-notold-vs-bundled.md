# 例：看见仍用旧类型要父交易不是旧库存已经退役；看见通告类型改了不是已经有见证；看见两端都支持不是全网已经不再按 txid 通告

**层次**：网络 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-339](https://github.com/bitcoin/bips/blob/master/bip-0339.mediawiki)（Deployed, Peer Services）。  
**对应课文**：[L3.4](../../courses/level-03-bitcoin/L03-M04-network-and-eclipse.md)、[L3.7](../../courses/level-03-bitcoin/L03-M07-segwit-soft-fork.md)、[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：index/03 共识行、Ethereum 行、M5.4、L5.1、L5.4、05b。本页是「BIP-339 old-getdata not already retired / not already have-wit / not already net-wide 正式三事（248 余量）/ not 1249 wtx339-notold interchangeable / not 248 wtxidrelay-vs-have bundled interchangeable」，不是 wtxidrelay bundled（248），也不是 txid 就已经等于 wtxid（152），也不是发了 sendheaders 就已经有块（245）。不要另写 怎样改见证挡住转发、怎样用旧类型重放、怎样在应答之后补发信号。

## 官方三件事

1. **看见仍用旧类型要父交易 / 看见通告类型改了 这份对象 is not already 旧库存已经退役 interchangeable，也不是已经 wtxidrelay bundled（248） interchangeable / 1249 wtx339-notold interchangeable / 1247 wtx339-nothave interchangeable，也不是已经 BIP-339 old-getdata not already retired / not already have-wit / not already net-wide 正式三事 bundled（248 item 3 余量） interchangeable / 248 wtxidrelay item 3 interchangeable。**  
   官方写：收到对等节点的这条信号之后，向它通告交易必须改用 wtxid 那种库存类型。向它索取应当也用这种类型。仍可用旧类型去要它最近没通告过的交易，例如刚通告那笔的父交易。官方还写：只有两端都支持才打开，旧客户端仍然兼容。看见通告类型改了，不是已经有见证，也不是已经验完。看见仍用旧类型要父交易，不是旧库存已经退役。看见两端都支持，不是全网已经不再按 txid 通告。

2. **看见通告类型改了 / 看见仍用旧类型要父交易 / 这份对象 is not already 已经有见证 interchangeable，也不是已经 wtxidrelay bundled（248） interchangeable / 1249 wtx339-notold interchangeable / 1248 wtx339-notswitch interchangeable，也不是已经 txid-wtxid interchangeable / 152 txid-wtxid interchangeable。**  
   官方把通告类型改了和已经有见证写成两件。看见通告类型改了，不是已经有见证。

3. **看见两端都支持 / 看见仍用旧类型要父交易 / 这份对象 is not already 全网已经不再按 txid 通告 interchangeable，也不是已经 wtxidrelay bundled（248） interchangeable / 1249 wtx339-notold interchangeable / 1247 wtx339-nothave interchangeable，也不是已经 feefilter-reject interchangeable / 245 feefilter-reject interchangeable。**  
   官方把两端都支持和全网已经不再按 txid 通告写成两件。看见两端都支持，不是全网已经不再按 txid 通告。

协议版本号、库存类型取值、空消息编码是规范里的数字，本页不抄。不要另写 怎样改见证挡住转发、怎样用旧类型重放、怎样在应答之后补发信号。

## 官方为什么这样拆

- **必须改通告 不是已经退役旧索取：官方允许父交易仍走旧类型。看见谈妥了，不是 txid 库存已经消失。**
- **通告类型改了 不是已经有见证：官方只换库存类型，不是已经验完见证。**
- **两端都支持 不是全网已经不再按 txid 通告：官方写只有两端都支持才打开，旧客户端仍然兼容。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 旧库存已经退役 | 不是旧库存已经退役 | 不是已经txid-wtxid（152） |
| 已经有见证 | 不是已经有见证 | 不是已经feefilter-reject（245） |
| 全网已经不再按 txid 通告 | 不是全网已经不再按 txid 通告 | 不是已经1247 wtx339-nothave |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-339 old-getdata not already retired / not already have-wit / not already net-wide 正式三事（248 余量），必须分开是不是旧库存已经退役、是不是已经有见证、是不是全网已经不再按 txid 通告。可以跳过「看见按 wtxid 通告就已经有那笔交易」。不要另写 怎样改见证挡住转发、怎样用旧类型重放、怎样在应答之后补发信号。248 wtxidrelay vs have bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 协议版本号、库存类型取值、空消息字段、见证序列化步骤。
- 怎样改见证挡住转发、怎样用旧类型重放、怎样在应答之后补发信号。
