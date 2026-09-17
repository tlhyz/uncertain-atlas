# 反模式：看见按 wtxid 通告就当成已经有交易 / 已经改口 / 旧库存已经退役

**层次**：网络 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[BIP-339](https://github.com/bitcoin/bips/blob/master/bip-0339.mediawiki)。  
**例**：[按 wtxid 通告 ≠ 已经有交易](../../tracks/network/worked-example-wtxidrelay-vs-have.md)。

## 塌法

1. 看见按 wtxid 通告，就当成已经有那笔交易，或当成已经收下，或当成已经验完。
2. 看见发了 wtxidrelay，就当成已经改口，或当成协议版本够了就已经谈妥。
3. 看见仍用旧类型要父交易，就当成谈妥失败，或当成旧库存已经退役。
4. 看见两端都支持，就当成全网已经不再按 txid 通告。
5. 看见本页，就当成已经写了 txid ≠ wtxid，或当成已经是头通告偏好。

## 为什么会出事

官方写：历史上按 txid 通告，不承诺见证。换 wtxid 是为了让拒过一份见证的节点不必再按同一个 txid 重下。握手信号必须在应答之前。父交易仍可用旧类型要。本页不是链上两个哈希已经是一回事。

## 和相邻反模式

- [txid-sold-as-wtxid](txid-sold-as-wtxid.md) 是链上身份，不是本页。
- [sendheaders-sold-as-have](sendheaders-sold-as-have.md) 是头通告偏好 ≠ 已经有块，不是本页。
- [feefilter-sold-as-rejected](feefilter-sold-as-rejected.md) 是费率过滤器 ≠ 已经拒进池，不是本页。
