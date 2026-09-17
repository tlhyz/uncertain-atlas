# 反模式：看见结果列表就当成已经同一顺序 / 看见 Code 非零就当成已经没进块 / 看见 Code Data 就当成已经印进本头

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Transaction Results。  
**例**：[结果列表 ≠ 已经同一顺序](../../tracks/implementation/worked-example-exectxresult-vs-consensus.md)。

## 塌法

1. 看见结果列表 / 看见 FinalizeBlockResponse，就当成已经和送来的交易同一顺序。
2. 看见 Code ≠ 0 / 看见标成无效，就当成已经没进块，或当成已经建了索引。
3. 看见 Code / Data / 看见 Events，就当成已经印进本头 LastResultsHash，或当成已经是共识字段。

## 为什么会出事

官方写：结果列表必须和送来的交易同一顺序。Code ≠ 0 仍在块里，只是不建索引。Code 和 Data 哈希进下一高度的 LastResultsHash；Events 只供查询；Info / Log 会被忽略。

## 和相邻反模式

- [checktx-sold-as-prepared](checktx-sold-as-prepared.md) 是 CheckTx ≠ 已经进提案，不是本页这种 Finalize 结果。
- [maxgas-sold-as-enforced](maxgas-sold-as-enforced.md) 是 MaxGas ≠ 已经在执行，不是本页。
