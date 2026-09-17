# 反模式：看见拒收消息就当成已经共识非法 / 已经该给用户看 / 已经是全网拒绝

**层次**：网络 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[BIP-61](https://github.com/bitcoin/bips/blob/master/bip-0061.mediawiki)。  
**例**：[拒收消息 ≠ 已经共识非法](../../tracks/network/worked-example-reject-vs-consensus.md)。

## 塌法

1. 看见拒收消息，就当成已经共识非法，或当成全网已经知道，或当成已经封禁。
2. 看见调试理由，就当成已经是官方原因，或当成已经该弹给用户。
3. 看见策略拒收，就当成已经共识非法。
4. 看见没拒收，就当成已经收下，或当成已经是当前最好链。
5. 看见本页，就当成已经写了策略大类，或当成已经是费率过滤器。

## 为什么会出事

官方写：拒收只是这个对等节点的直接反馈。人读字符串只给调试，各实现可以不同。策略码单独一类。否则合法、只是还不是当前最好链的块，不应当触发拒收。对手也可以对合法对象乱发拒收。

## 和相邻反模式

- [policy-sold-as-consensus](policy-sold-as-consensus.md) 是策略拒绝 ≠ 共识非法，不是本页这条消息。
- [feefilter-sold-as-rejected](feefilter-sold-as-rejected.md) 是费率过滤器 ≠ 已经拒进池，不是本页。
- [mempool-dump-sold-as-have](mempool-dump-sold-as-have.md) 是内存池查询 ≠ 已经有那些交易，不是本页。
