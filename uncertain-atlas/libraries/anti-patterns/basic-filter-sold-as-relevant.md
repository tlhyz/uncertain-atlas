# 反模式：看见基本过滤器对上就当成已经相关 / 已经有那笔交易 / 已经写进共识

**层次**：轻客户端 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[BIP-158](https://github.com/bitcoin/bips/blob/master/bip-0158.mediawiki)。  
**例**：[基本过滤 ≠ 已经相关](../../tracks/light-clients/worked-example-basic-filter-vs-relevant.md)。

## 塌法

1. 看见过滤器对上，就当成已经在集合里，或当成已经相关。
2. 看见装了花费脚本和收款脚本，就当成已经有那笔交易，或当成已经有附言。
3. 看见排除了 `OP_RETURN`，就当成已经写进共识。
4. 看见服务位，就当成已经在答所有过滤器类型，或当成已经写了 157 头链。
5. 看见本页，就当成已经写了「对上再下整块」，或当成已经是布隆。

## 为什么会出事

官方写：集合里必中，集合外也可能中。基本类型只装脚本，不装整笔交易。排除附言是为了以后还能承诺，不是承诺已经上链。

## 和相邻反模式

- [cfilter-sold-as-have](cfilter-sold-as-have.md) 是对上再下整块 ≠ 已经有块，不是本页。
- [header-equals-settlement](header-equals-settlement.md) 是只看头就放货，不是本页。
- [rpc-as-verification](rpc-as-verification.md) 是浏览器 / RPC，不是本页。
