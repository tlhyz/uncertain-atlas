# 反模式：看见 Query 请求 prove 是能回就回默克尔证明就当成已经对上 AppHash / 看见 Query 回包 proof_ops 是按请求回的、要对这一高 AppHash 验的序列化证明就当成已经是按键查 / 看见 Query 回包 height 是数据来自哪一高就当成已经是请求高度

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Request / Query Response。  
**例**：[Query 请求 prove 是能回就回默克尔证明 ≠ 已经对上 AppHash](../../tracks/implementation/worked-example-queryprove-vs-proof.md)。

## 塌法

1. 看见 Query 请求 `prove` 是能回就回默克尔证明 / 看见勾了 prove，就当成已经对上 AppHash，或当成已经是一层树。
2. 看见 Query 回包 `proof_ops` 是按请求回的、要对这一高 AppHash 验的序列化证明 / 看见回了证明，就当成已经是按键查，或当成已经对上 AppHash。
3. 看见 Query 回包 `height` 是数据来自哪一高 / 看见回了高度，就当成已经是请求高度，或当成已经新鲜。

## 为什么会出事

官方写：`prove` 是能回就随回包带回默克尔证明。`proof_ops` 是按请求回的、用来对这一高 `app_hash` 验这份值的序列化证明。回包 `height` 是这份数据来自哪一高。

## 和相邻反模式

- [queryprove-notmatched-sold-as-bundled](queryprove-notmatched-sold-as-bundled.md) 是 Query 请求 prove 是能回就回默克尔证明不是已经对上 AppHash not already matched / not already tree / not already settled 正式三事（383 item 1），不是本页 bundled 全段 alone。
- [queryproof-sold-as-apphash](queryproof-sold-as-apphash.md) 是 Query 回了 Proof 就已经对上 AppHash，不是本页这种 Query 请求 prove 是能回就回默克尔证明不是已经对上 AppHash。
- [queryindex-sold-as-store](queryindex-sold-as-store.md) 是 Query 回包 value 就已经对上 AppHash，不是本页这种 Query 回包 proof_ops 是按请求回的、要对这一高 AppHash 验的序列化证明不是已经是按键查。
- [queryheight-sold-as-committed](queryheight-sold-as-committed.md) 是 Query 可以对当前或过去高度查就已经是 QueryState，不是本页这种 Query 回包 height 是数据来自哪一高不是已经是请求高度。
