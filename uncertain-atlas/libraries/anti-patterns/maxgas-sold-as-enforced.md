# 反模式：看见 MaxGas 就当成已经在执行 / 看见 GasUsed 就当成已经算进共识 / 看见已提交块就当成已经按气限验过

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Gas。  
**例**：[MaxGas ≠ 已经在执行](../../tracks/implementation/worked-example-maxgas-vs-enforced.md)。

## 塌法

1. 看见 MaxGas / 看见回包里有气字段 / 看见官方说学了以太坊，就当成已经在执行，或当成气已经有意义。
2. 看见 GasWanted / 看见 GasUsed，就当成已经由 CometBFT 按实用气验过，或当成已经算进共识。
3. 看见已提交块 / 看见旧版只在内存池管气，就当成已经保证这块守了气限，或当成已经由共识层验过。

## 为什么会出事

官方写：气只用得可选且弱；默认 MaxGas 是 -1，表示不执行或没有意义。GasUsed 被 CometBFT 忽略。v0.34.x 及更早在共识里不强制任何气规则，不保证已提交块守上限；要从 v0.37 的 Prepare / Process 起，应用才能卡住被决定的块。

## 和相邻反模式

- [evidence-sold-as-full-block](evidence-sold-as-full-block.md) 是 MaxBytes 写成 -1 ≠ 已经没有上限，不是本页这种 MaxGas。
- [checktx-sold-as-prepared](checktx-sold-as-prepared.md) 是 CheckTx ≠ 已经进提案，不是本页。
