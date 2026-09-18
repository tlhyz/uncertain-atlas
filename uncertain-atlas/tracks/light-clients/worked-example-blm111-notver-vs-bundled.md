# 例：看见协议版本够了不是已经在遵守这一位；看见开了布隆位不是已经能服完整历史；看见开了布隆位不是已经是归档节点

**层次**：轻客户端 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-111](https://github.com/bitcoin/bips/blob/master/bip-0111.mediawiki)（Deployed, Peer Services）。  
**对应课文**：[L3.5](../../courses/level-03-bitcoin/L03-M05-full-node-and-spv.md)、[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)、[L9.6](../../courses/level-09-systems/L09-M06-light-clients.md)。  
**不要写进**：index/03 共识行、Ethereum 行、M5.4、L5.1、L5.4、05b。本页是「BIP-111 version-enough not already obeying / not already full-history / not already archive 正式三事（252 余量）/ not 1261 blm111-notver interchangeable / not 252 bloom-bit-vs-retired bundled interchangeable」，不是 bloom bundled（252），也不是已经 limited-archive（250），也不是已经 cfilter-have（243）。不要另写 怎样用布隆做拒绝服务、怎样做交集分析、怎样按服务位认出节点。

## 官方三件事

1. **看见协议版本够了 / 看见开了布隆位 这份对象 is not already 已经在遵守这一位 interchangeable，也不是已经 bloom bundled（252） interchangeable / 1261 blm111-notver interchangeable / 1259 blm111-notpriv interchangeable，也不是已经 BIP-111 version-enough not already obeying / not already full-history / not already archive 正式三事 bundled（252 item 3 余量） interchangeable / 252 bloom item 3 interchangeable。**  
   官方写：提高协议版本是为了兼容。最初实现里，还不认识这一位、协议版本也较旧的节点，仍可能向没开这一位的节点发过滤器消息。官方还写：这一位和「能服完整历史」那一位不是同一位；只开布隆、不开完整历史，规范上合法。看见协议版本够了，不是已经在遵守这一位。看见开了布隆位，不是已经能服完整历史，也不是已经是归档节点。

2. **看见开了布隆位 / 看见协议版本够了 / 这份对象 is not already 已经能服完整历史 interchangeable，也不是已经 bloom bundled（252） interchangeable / 1261 blm111-notver interchangeable / 1260 blm111-notoff interchangeable，也不是已经 limited-archive interchangeable / 250 limited-archive interchangeable。**  
   官方把开了布隆位和已经能服完整历史写成两件。看见开了布隆位，不是已经能服完整历史。

3. **看见开了布隆位 / 看见协议版本够了 / 这份对象 is not already 已经是归档节点 interchangeable，也不是已经 bloom bundled（252） interchangeable / 1261 blm111-notver interchangeable / 1259 blm111-notpriv interchangeable，也不是已经 cfilter-have interchangeable / 243 cfilter-have interchangeable。**  
   官方把开了布隆位和已经是归档节点写成两件。看见开了布隆位，不是已经是归档节点。

位编号、协议版本号是规范里的数字，本页不抄。不要另写 怎样用布隆做拒绝服务、怎样做交集分析、怎样按服务位认出节点。

## 官方为什么这样拆

- **版本够了 不是已经遵守：官方写旧版本仍可能继续服。看见版本号，不是服务位已经生效。**
- **开了布隆位 不是已经能服完整历史：官方写这一位和完整历史位不是同一位。**
- **开了布隆位 不是已经是归档：官方只开布隆、不开完整历史，规范上合法。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经在遵守这一位 | 不是已经在遵守这一位 | 不是已经limited-archive（250） |
| 已经能服完整历史 | 不是已经能服完整历史 | 不是已经cfilter-have（243） |
| 已经是归档节点 | 不是已经是归档节点 | 不是已经1259 blm111-notpriv |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-111 version-enough not already obeying / not already full-history / not already archive 正式三事（252 余量），必须分开是不是已经在遵守这一位、是不是已经能服完整历史、是不是已经是归档节点。可以跳过「看见没开布隆服务位就已经退役布隆」。不要另写 怎样用布隆做拒绝服务、怎样做交集分析、怎样按服务位认出节点。252 bloom vs retired bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 位编号、协议版本号、过滤器命令字段、布隆构造参数。
- 怎样用布隆做拒绝服务、怎样做交集分析、怎样按服务位认出节点。
