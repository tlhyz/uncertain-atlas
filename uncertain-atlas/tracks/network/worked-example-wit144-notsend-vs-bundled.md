# 例：看见开了能提供见证那一位不是已经在传；看见开了这一位不是见证已经在请求方手里；看见开了这一位不是旧序列化已经退役

**层次**：网络 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-144](https://github.com/bitcoin/bips/blob/master/bip-0144.mediawiki)（Deployed, Peer Services）。  
**对应课文**：[L3.4](../../courses/level-03-bitcoin/L03-M04-network-and-eclipse.md)、[L3.7](../../courses/level-03-bitcoin/L03-M07-segwit-soft-fork.md)、[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：index/03 共识行、Ethereum 行、M5.4、L5.1、L5.4、05b。本页是「BIP-144 service-bit not already sending / not already have / not already old-retired 正式三事（251 余量）/ not 1257 wit144-notsend interchangeable / not 251 witness-wire-vs-have bundled interchangeable」，不是 witness bundled（251），也不是已经 limited-archive（250），也不是已经 wtxidrelay-have（248）。不要另写 怎样拼能骗过旧解析器的字节、怎样用索取类型重放、怎样按服务位认出节点。

## 官方三件事

1. **看见开了能提供见证那一位 / 看见开了这一位 这份对象 is not already 已经在传 interchangeable，也不是已经 witness bundled（251） interchangeable / 1257 wit144-notsend interchangeable / 1256 wit144-nothave interchangeable，也不是已经 BIP-144 service-bit not already sending / not already have / not already old-retired 正式三事 bundled（251 item 2 余量） interchangeable / 251 witness item 2 interchangeable。**  
   官方写：节点用一位服务位表示自己能提供见证。看见开了这一位，不是已经在传见证，也不是见证已经在请求方手里，也不是旧序列化已经退役。

2. **看见开了这一位 / 看见开了能提供见证那一位 / 这份对象 is not already 见证已经在请求方手里 interchangeable，也不是已经 witness bundled（251） interchangeable / 1257 wit144-notsend interchangeable / 1258 wit144-notold interchangeable，也不是已经 limited-archive interchangeable / 250 limited-archive interchangeable。**  
   官方把开了这一位和见证已经在请求方手里写成两件。看见开了这一位，不是见证已经在请求方手里。

3. **看见开了这一位 / 看见开了能提供见证那一位 / 这份对象 is not already 旧序列化已经退役 interchangeable，也不是已经 witness bundled（251） interchangeable / 1257 wit144-notsend interchangeable / 1256 wit144-nothave interchangeable，也不是已经 wtxidrelay-have interchangeable / 248 wtxidrelay-have interchangeable。**  
   官方把开了这一位和旧序列化已经退役写成两件。看见开了这一位，不是旧序列化已经退役。

标记、旗标、位编号、库存类型取值是规范里的数字，本页不抄。不要另写 怎样拼能骗过旧解析器的字节、怎样用索取类型重放、怎样按服务位认出节点。

## 官方为什么这样拆

- **能提供 不是已经在传：官方把「能提供」钉在服务位。看见开了位，不是已经在传。**
- **开了这一位 不是见证已经在请求方手里：官方只宣布能力，不是已经下完。**
- **开了这一位 不是旧序列化已经退役：官方空见证仍必须走旧格式。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经在传 | 不是已经在传 | 不是已经limited-archive（250） |
| 见证已经在请求方手里 | 不是见证已经在请求方手里 | 不是已经wtxidrelay-have（248） |
| 旧序列化已经退役 | 不是旧序列化已经退役 | 不是已经1256 wit144-nothave |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-144 service-bit not already sending / not already have / not already old-retired 正式三事（251 余量），必须分开是不是已经在传、是不是见证已经在请求方手里、是不是旧序列化已经退役。可以跳过「看见带见证的线上序列化就已经有见证」。不要另写 怎样拼能骗过旧解析器的字节、怎样用索取类型重放、怎样按服务位认出节点。251 witness vs have bundled unbundling 在本页 item 2 续；续 [`worked-example-wit144-notold-vs-bundled.md`](worked-example-wit144-notold-vs-bundled.md)（不变量 1258 item 3）。

## 本页不抄

- 标记 / 旗标取值、字段宽度、服务位编号、库存类型取值、空见证编码步骤。
- 怎样拼能骗过旧解析器的字节、怎样用索取类型重放、怎样按服务位认出节点。
