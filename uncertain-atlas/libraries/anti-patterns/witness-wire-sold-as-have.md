# 反模式：看见带见证的线上序列化就当成已经有见证 / 已经在传 / 通告已经改口

**层次**：网络 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[BIP-144](https://github.com/bitcoin/bips/blob/master/bip-0144.mediawiki)。  
**例**：[带见证的线上序列化 ≠ 已经有见证](../../tracks/network/worked-example-witness-wire-vs-have.md)。

## 塌法

1. 看见带见证的线上序列化，就当成已经有见证，或当成已经收下，或当成已经验完。
2. 看见开了能提供见证的服务位，就当成已经在传，或当成旧序列化已经退役。
3. 看见库存通告仍用旧类型，就当成线上已经没有见证，或当成谈妥失败。
4. 看见按带见证类型去索取，就当成已经按 wtxid 通告。
5. 看见本页，就当成已经写了 txid ≠ wtxid，或当成已经是按 wtxid 转发。

## 为什么会出事

官方写：新序列化是为了在网上装见证，并且不把旧节点弄坏。空见证必须走旧格式。通告仍用旧库存类型；带见证类型只用于索取。本页不是链上两个哈希已经是一回事，也不是已经按 wtxid 通告。

## 和相邻反模式

- [txid-sold-as-wtxid](txid-sold-as-wtxid.md) 是链上身份，不是本页。
- [wtxidrelay-sold-as-have](wtxidrelay-sold-as-have.md) 是按 wtxid 通告 ≠ 已经有交易，不是本页。
- [sendheaders-sold-as-have](sendheaders-sold-as-have.md) 是头通告偏好 ≠ 已经有块，不是本页。
