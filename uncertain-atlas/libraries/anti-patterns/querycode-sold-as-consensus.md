# 反模式：看见 Query 回包 code 是回包码就当成已经过了共识 / 看见 Query 回包 log 是应用日志输出就当成已经新鲜 / 看见 Query 回包 info 是附加信息就当成已经是按键查

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Response。  
**例**：[Query 回包 code 是回包码 ≠ 已经过了共识](../../tracks/implementation/worked-example-querycode-vs-consensus.md)。

## 塌法

1. 看见 Query 回包 `code` 是回包码 / 看见回了码，就当成已经过了共识，或当成已经没进块。
2. 看见 Query 回包 `log` 是应用日志输出 / 看见回了日志，就当成已经新鲜，或当成已经复制到各节点。
3. 看见 Query 回包 `info` 是附加信息 / 看见回了信息，就当成已经是按键查，或当成已经对上 AppHash。

## 为什么会出事

官方写：`code` 是回包码。`log` 是应用日志的输出。`info` 是附加信息。

## 和相邻反模式

- [checktxspace-sold-as-code](checktxspace-sold-as-code.md) 是 CheckTx 回包 codespace 就已经是回包码，不是本页这种 Query 回包 code 是回包码不是已经过了共识。
- [query-sold-as-replicated](query-sold-as-replicated.md) 是 Query 回了就已经复制到各节点，不是本页这种 Query 回包 log 是应用日志输出不是已经新鲜。
- [queryindex-sold-as-store](queryindex-sold-as-store.md) 是 Query 回包 value 就已经对上 AppHash，不是本页这种 Query 回包 info 是附加信息不是已经是按键查。
