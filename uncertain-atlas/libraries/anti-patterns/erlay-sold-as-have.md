# 反模式：看见对账素描就当成已经有交易 / 已经在对账 / 库存通告已经退役

**层次**：网络 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[BIP-330](https://github.com/bitcoin/bips/blob/master/bip-0330.mediawiki)。  
**例**：[对账素描 ≠ 已经有交易](../../tracks/network/worked-example-erlay-vs-have.md)。

## 塌法

1. 看见一次对账，就当成已经有那些交易，或当成库存通告已经退役，或当成已经向每个邻居都通告过。
2. 看见发了 sendtxrcncl，就当成已经在对账，或当成发了 wtxidrelay 就已经打开对账。
3. 看见一份素描或解码成功，就当成已经下完，或当成已经验完。
4. 看见解码失败退回洪水，就当成对账已经没用，或当成那些交易已经共识非法。
5. 看见本页，就当成已经写了按 wtxid 通告，或当成已经是宣布≠收到。

## 为什么会出事

官方写：对账是两个节点对齐通告集合的积木。Erlay 仍然会向一小撮连接发库存通告。握手必须在应答之前，并且必须带着 wtxidrelay。解完仍要再发库存通告；解不开还得退回洪水。本页不是交易已经在手里。

## 和相邻反模式

- [wtxidrelay-sold-as-have](wtxidrelay-sold-as-have.md) 是按 wtxid 通告 ≠ 已经有交易，不是本页。
- [feefilter-sold-as-rejected](feefilter-sold-as-rejected.md) 是费率过滤器 ≠ 已经拒进池，不是本页。
- [sendheaders-sold-as-have](sendheaders-sold-as-have.md) 是头通告偏好 ≠ 已经有块，不是本页。
