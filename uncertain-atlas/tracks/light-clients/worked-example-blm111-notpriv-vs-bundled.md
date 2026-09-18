# 例：看见开了布隆服务位不是已经私人；看见开了这一位不是拒绝服务面已经没了；看见没写服务位的旧协议不是已经保证人人都服

**层次**：轻客户端 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-111](https://github.com/bitcoin/bips/blob/master/bip-0111.mediawiki)（Deployed, Peer Services）。  
**对应课文**：[L3.5](../../courses/level-03-bitcoin/L03-M05-full-node-and-spv.md)、[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)、[L9.6](../../courses/level-09-systems/L09-M06-light-clients.md)。  
**不要写进**：index/03 共识行、Ethereum 行、M5.4、L5.1、L5.4、05b。本页是「BIP-111 bloom-bit not already private / not already no-dos / not already everyone-serves 正式三事（252 余量）/ not 1259 blm111-notpriv interchangeable / not 252 bloom-bit-vs-retired bundled interchangeable」，不是 bloom bundled（252），也不是已经 cfilter-have（243），也不是已经 basic-filter（244）。不要另写 怎样用布隆做拒绝服务、怎样做交集分析、怎样按服务位认出节点。

## 官方三件事

1. **看见开了布隆服务位 / 看见开了这一位 这份对象 is not already 已经私人 interchangeable，也不是已经 bloom bundled（252） interchangeable / 1259 blm111-notpriv interchangeable / 1260 blm111-notoff interchangeable，也不是已经 BIP-111 bloom-bit not already private / not already no-dos / not already everyone-serves 正式三事 bundled（252 item 1 余量） interchangeable / 252 bloom item 1 interchangeable。**  
   官方写：本页给 BIP-37 补一位服务位，让对等节点能明确宣布自己支持连接上的布隆过滤。BIP-37 没写这一位，等于默认凡是给人数据的节点都服。官方还写：后来发现这套连接过滤几乎不提供隐私，也对部分节点构成很大的拒绝服务面，所以运营者必须能关掉。看见开了这一位，不是已经私人，也不是拒绝服务面已经没了，也不是过滤器已经有用。看见没写服务位的旧协议，不是已经保证人人都服。

2. **看见开了这一位 / 看见开了布隆服务位 / 这份对象 is not already 拒绝服务面已经没了 interchangeable，也不是已经 bloom bundled（252） interchangeable / 1259 blm111-notpriv interchangeable / 1261 blm111-notver interchangeable，也不是已经 cfilter-have interchangeable / 243 cfilter-have interchangeable。**  
   官方把开了这一位和拒绝服务面已经没了写成两件。看见开了这一位，不是拒绝服务面已经没了。

3. **看见没写服务位的旧协议 / 看见开了布隆服务位 / 这份对象 is not already 已经保证人人都服 interchangeable，也不是已经 bloom bundled（252） interchangeable / 1259 blm111-notpriv interchangeable / 1260 blm111-notoff interchangeable，也不是已经 basic-filter interchangeable / 244 basic-filter interchangeable。**  
   官方把没写服务位的旧协议和已经保证人人都服写成两件。看见没写服务位的旧协议，不是已经保证人人都服。

位编号、协议版本号是规范里的数字，本页不抄。不要另写 怎样用布隆做拒绝服务、怎样做交集分析、怎样按服务位认出节点。

## 官方为什么这样拆

- **显式宣布 不是已经私人：官方补这一位，是因为后来发现几乎不提供隐私。看见开了位，不是隐私已经修好。**
- **开了这一位 不是拒绝服务面已经没了：官方写这套连接过滤也对部分节点构成很大的拒绝服务面。**
- **旧协议没写这一位 不是已经保证人人都服：官方只把旧默认写成历史，不是已经人人都服。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经私人 | 不是已经私人 | 不是已经cfilter-have（243） |
| 拒绝服务面已经没了 | 不是拒绝服务面已经没了 | 不是已经basic-filter（244） |
| 已经保证人人都服 | 不是已经保证人人都服 | 不是已经1260 blm111-notoff |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-111 bloom-bit not already private / not already no-dos / not already everyone-serves 正式三事（252 余量），必须分开是不是已经私人、是不是拒绝服务面已经没了、是不是已经保证人人都服。可以跳过「看见没开布隆服务位就已经退役布隆」。不要另写 怎样用布隆做拒绝服务、怎样做交集分析、怎样按服务位认出节点。252 bloom vs retired bundled unbundling 在本页 item 1 启动；续 [`worked-example-blm111-notoff-vs-bundled.md`](worked-example-blm111-notoff-vs-bundled.md)（不变量 1260 item 2）。

## 本页不抄

- 位编号、协议版本号、过滤器命令字段、布隆构造参数。
- 怎样用布隆做拒绝服务、怎样做交集分析、怎样按服务位认出节点。
