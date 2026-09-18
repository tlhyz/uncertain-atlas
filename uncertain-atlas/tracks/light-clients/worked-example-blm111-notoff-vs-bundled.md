# 例：看见没开布隆服务位不是全网布隆已经退役；看见没开这一位不是已经改用客户端侧过滤；看见因过滤器命令被断开不是已经共识非法

**层次**：轻客户端 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-111](https://github.com/bitcoin/bips/blob/master/bip-0111.mediawiki)（Deployed, Peer Services）。  
**对应课文**：[L3.5](../../courses/level-03-bitcoin/L03-M05-full-node-and-spv.md)、[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)、[L9.6](../../courses/level-09-systems/L09-M06-light-clients.md)。  
**不要写进**：index/03 共识行、Ethereum 行、M5.4、L5.1、L5.4、05b。本页是「BIP-111 bloom-off not already retired / not already cfilter / not already consensus-illegal 正式三事（252 余量）/ not 1260 blm111-notoff interchangeable / not 252 bloom-bit-vs-retired bundled interchangeable」，不是 bloom bundled（252），也不是已经 cfilter-have（243），也不是已经 feefilter-reject（245）。不要另写 怎样用布隆做拒绝服务、怎样做交集分析、怎样按服务位认出节点。

## 官方三件事

1. **看见没开布隆服务位 / 看见没开这一位 这份对象 is not already 全网布隆已经退役 interchangeable，也不是已经 bloom bundled（252） interchangeable / 1260 blm111-notoff interchangeable / 1259 blm111-notpriv interchangeable，也不是已经 BIP-111 bloom-off not already retired / not already cfilter / not already consensus-illegal 正式三事 bundled（252 item 2 余量） interchangeable / 252 bloom item 2 interchangeable。**  
   官方写：支持布隆的节点应当打开这一位，否则应当保持关闭。不支持布隆的节点若收到装过滤器、加条件或清过滤器的消息，应当立刻断开这个对等节点。为了兼容，最初实现也可以只对已经升到新协议版本、还来发过滤器命令的节点断开。看见没开这一位，不是全网布隆已经退役，也不是已经改用客户端侧过滤，也不是已经安全。看见因过滤器命令被断开，不是那些交易已经共识非法。

2. **看见没开这一位 / 看见没开布隆服务位 / 这份对象 is not already 已经改用客户端侧过滤 interchangeable，也不是已经 bloom bundled（252） interchangeable / 1260 blm111-notoff interchangeable / 1261 blm111-notver interchangeable，也不是已经 cfilter-have interchangeable / 243 cfilter-have interchangeable。**  
   官方把没开这一位和已经改用客户端侧过滤写成两件。看见没开这一位，不是已经改用客户端侧过滤。

3. **看见因过滤器命令被断开 / 看见没开布隆服务位 / 这份对象 is not already 已经共识非法 interchangeable，也不是已经 bloom bundled（252） interchangeable / 1260 blm111-notoff interchangeable / 1259 blm111-notpriv interchangeable，也不是已经 feefilter-reject interchangeable / 245 feefilter-reject interchangeable。**  
   官方把因过滤器命令被断开和已经共识非法写成两件。看见因过滤器命令被断开，不是已经共识非法。

位编号、协议版本号是规范里的数字，本页不抄。不要另写 怎样用布隆做拒绝服务、怎样做交集分析、怎样按服务位认出节点。

## 官方为什么这样拆

- **能关掉 不是已经退役：官方只让这个节点拒。看见没开，不是全网已经关掉布隆。**
- **没开这一位 不是已经改用客户端侧过滤：官方只写这个节点可以拒，不是已经换成 158。**
- **因过滤器命令被断开 不是已经共识非法：官方断开是连接策略，不是那些交易已经非法。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 全网布隆已经退役 | 不是全网布隆已经退役 | 不是已经cfilter-have（243） |
| 已经改用客户端侧过滤 | 不是已经改用客户端侧过滤 | 不是已经feefilter-reject（245） |
| 已经共识非法 | 不是已经共识非法 | 不是已经1259 blm111-notpriv |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-111 bloom-off not already retired / not already cfilter / not already consensus-illegal 正式三事（252 余量），必须分开是不是全网布隆已经退役、是不是已经改用客户端侧过滤、是不是已经共识非法。可以跳过「看见没开布隆服务位就已经退役布隆」。不要另写 怎样用布隆做拒绝服务、怎样做交集分析、怎样按服务位认出节点。252 bloom vs retired bundled unbundling 在本页 item 2 续；续 [`worked-example-blm111-notver-vs-bundled.md`](worked-example-blm111-notver-vs-bundled.md)（不变量 1261 item 3）。

## 本页不抄

- 位编号、协议版本号、过滤器命令字段、布隆构造参数。
- 怎样用布隆做拒绝服务、怎样做交集分析、怎样按服务位认出节点。
