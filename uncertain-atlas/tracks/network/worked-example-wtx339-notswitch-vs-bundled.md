# 例：看见发了 wtxidrelay 不是已经改口；看见协议版本够了不是已经谈妥；看见发了 wtxidrelay 不是已经在用

**层次**：网络 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-339](https://github.com/bitcoin/bips/blob/master/bip-0339.mediawiki)（Deployed, Peer Services）。  
**对应课文**：[L3.4](../../courses/level-03-bitcoin/L03-M04-network-and-eclipse.md)、[L3.7](../../courses/level-03-bitcoin/L03-M07-segwit-soft-fork.md)、[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：index/03 共识行、Ethereum 行、M5.4、L5.1、L5.4、05b。本页是「BIP-339 wtxidrelay not already switched / not already negotiated / not already using 正式三事（248 余量）/ not 1248 wtx339-notswitch interchangeable / not 248 wtxidrelay-vs-have bundled interchangeable」，不是 wtxidrelay bundled（248），也不是 txid 就已经等于 wtxid（247），也不是发了 sendheaders 就已经有块（259）。不要另写 怎样改见证挡住转发、怎样用旧类型重放、怎样在应答之后补发信号。

## 官方三件事

1. **看见发了 wtxidrelay / 看见协议版本够了 这份对象 is not already 已经改口 interchangeable，也不是已经 wtxidrelay bundled（248） interchangeable / 1248 wtx339-notswitch interchangeable / 1247 wtx339-nothave interchangeable，也不是已经 BIP-339 wtxidrelay not already switched / not already negotiated / not already using 正式三事 bundled（248 item 2 余量） interchangeable / 248 wtxidrelay item 2 interchangeable。**  
   官方写：新增一条空消息。必须在对等节点协议版本够了之后、回完握手应答之前发出。握手应答之后才收到的，必须忽略或当非法。看见发了 wtxidrelay，不是已经按 wtxid 通告。看见协议版本够了，不是已经谈妥，也不是已经在用。

2. **看见协议版本够了 / 看见发了 wtxidrelay / 这份对象 is not already 已经谈妥 interchangeable，也不是已经 wtxidrelay bundled（248） interchangeable / 1248 wtx339-notswitch interchangeable / 1249 wtx339-notold interchangeable，也不是已经 sendheaders-have interchangeable / 247 sendheaders-have interchangeable。**  
   官方把协议版本够了和已经谈妥写成两件。看见协议版本够了，不是已经谈妥。

3. **看见发了 wtxidrelay / 看见发了 wtxidrelay / 这份对象 is not already 已经在用 interchangeable，也不是已经 wtxidrelay bundled（248） interchangeable / 1248 wtx339-notswitch interchangeable / 1247 wtx339-nothave interchangeable，也不是已经 feature-enabled interchangeable / 259 feature-enabled interchangeable。**  
   官方把发了空消息和已经在用写成两件。看见发了 wtxidrelay，不是已经在用。

协议版本号、库存类型取值、空消息编码是规范里的数字，本页不抄。不要另写 怎样改见证挡住转发、怎样用旧类型重放、怎样在应答之后补发信号。

## 官方为什么这样拆

- **握手信号 不是已经改口：官方把「能懂」钉在应答之前。看见发了空消息，不是已经按新类型通告。**
- **协议版本够了 不是已经谈妥：官方写必须在版本够了之后、回完握手应答之前发出。**
- **发了 wtxidrelay 不是已经在用：官方写握手应答之后才收到的必须忽略或当非法。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经改口 | 不是已经改口 | 不是已经sendheaders-have（247） |
| 已经谈妥 | 不是已经谈妥 | 不是已经feature-enabled（259） |
| 已经在用 | 不是已经在用 | 不是已经1247 wtx339-nothave |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-339 wtxidrelay not already switched / not already negotiated / not already using 正式三事（248 余量），必须分开是不是已经改口、是不是已经谈妥、是不是已经在用。可以跳过「看见按 wtxid 通告就已经有那笔交易」。不要另写 怎样改见证挡住转发、怎样用旧类型重放、怎样在应答之后补发信号。248 wtxidrelay vs have bundled unbundling 在本页 item 2 续；续 [`worked-example-wtx339-notold-vs-bundled.md`](worked-example-wtx339-notold-vs-bundled.md)（不变量 1249 item 3）。

## 本页不抄

- 协议版本号、库存类型取值、空消息字段、见证序列化步骤。
- 怎样改见证挡住转发、怎样用旧类型重放、怎样在应答之后补发信号。
