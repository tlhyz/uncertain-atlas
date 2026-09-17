# 反模式：看见内存池查询回了一串库存就当成已经有那些交易 / 已经是全网同一口池 / 已经共识

**层次**：内存池 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[BIP-35](https://github.com/bitcoin/bips/blob/master/bip-0035.mediawiki)。  
**例**：[内存池查询 ≠ 已经有那些交易](../../tracks/mempool/worked-example-mempool-dump-vs-have.md)。

## 塌法

1. 看见内存池查询回了一串库存，就当成已经有那些交易，或当成已经收下、已经验完。
2. 看见仍只肯给最近转发过的，就当成那些交易已经不在池里，或当成整池查询已经打开。
3. 看见协议版本够了，或看见开了「能服数据」，就当成已经在答内存池查询。
4. 看见过大的库存被丢掉，就当成那些交易已经共识非法。
5. 看见本页，就当成已经写了费率过滤器，或当成已经是对账素描。

## 为什么会出事

官方写：空消息只换回哈希。索取还得单独扩到内存池。版本够了仍可能不答。一节点的池不是全网队列，也不是共识。

## 和相邻反模式

- [feefilter-sold-as-rejected](feefilter-sold-as-rejected.md) 是费率过滤器 ≠ 已经拒进池，不是本页。
- [wtxidrelay-sold-as-have](wtxidrelay-sold-as-have.md) 是按 wtxid 通告 ≠ 已经有交易，不是本页。
- [erlay-sold-as-have](erlay-sold-as-have.md) 是对账素描 ≠ 已经有那些交易，不是本页。
