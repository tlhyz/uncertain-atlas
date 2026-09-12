# 反模式：看见客户端侧过滤器对上就当成已经有块 / 已经写进共识 / 已经验完脚本

**层次**：轻客户端 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[BIP-157](https://github.com/bitcoin/bips/blob/master/bip-0157.mediawiki)。  
**例**：[客户端侧过滤 ≠ 已经有块](../../tracks/light-clients/worked-example-cfilter-vs-have.md)。

## 塌法

1. 看见过滤器对上，就当成已经有块，或当成已经有那笔交易。
2. 看见过滤器头链对上，就当成已经写进共识，或当成块已经合法。
3. 看见「至少一个诚实对等节点」，就当成已经不需要诚实对等节点。
4. 看见支持客户端侧过滤，就当成已经是全节点，或当成脚本已经验完，或当成 BIP-37 已经退役。
5. 看见比布隆更难瞒漏，就当成隐私已经匿名，或当成已经是另一份过滤器编码。
6. 看见本页，就当成已经写了「只看头就放货」，或当成已经点名信任对象。

## 为什么会出事

官方写：对上了再下整块。过滤器头链是点对点层，不是共识承诺。客户端仍不验所有块。本页是 BIP-37 的替代路，不是布隆已经关掉。

## 和相邻反模式

- [header-equals-settlement](header-equals-settlement.md) 是只看头就放货，不是本页。
- [rpc-as-verification](rpc-as-verification.md) 是浏览器 / RPC，不是本页。
- [v2-sold-as-private](v2-sold-as-private.md) 是传输加密 ≠ 已经私人，不是本页。
