# 反模式：看见 Prepare 没有确定性要求就当成已经必须确定 / 看见两边 raw 一样就当成已经是同一份提案 / 看见 ExtendVote 没有确定性要求就当成已经是同一份扩展

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements，Req 11–12 之后。  
**例**：[Prepare 没有确定性要求 ≠ 已经必须确定](../../tracks/implementation/worked-example-prepare-nondet-vs-process.md)。

## 塌法

1. 看见 `PrepareProposal` 没有确定性要求 / 看见可以依赖其它值或操作，就当成已经必须确定，或当成已经和 Process / Finalize 同一把尺。
2. 看见两边 raw 提案一样 / 看见 *v_p = v_q*，就当成已经是同一份 prepared 提案，或当成已经必须同一份。
3. 看见 `ExtendVote` 没有确定性要求 / 看见同一块，就当成已经是同一份扩展，或当成已经必须同一份。

## 为什么会出事

官方写：Prepare 和 ExtendVote 都没有与确定性相关的要求。Prepare 可以依赖其它值或操作。同一份 raw 不蕴涵同一份 prepared。同一块不蕴涵同一份扩展。

## 和相邻反模式

- [checktx-sold-as-prepared](checktx-sold-as-prepared.md) 是四门已经结算，不是本页这种没有确定性要求 ≠ 已经必须确定。
- [preparetimeout-sold-as-liveness](preparetimeout-sold-as-liveness.md) 是立刻整块执行 ≠ 已经离开关键路径，不是本页这种两边 raw 一样 ≠ 已经是同一份提案。
- [vote-extension-sold-as-block](vote-extension-sold-as-block.md) 是验签拒收整张预提交，不是本页这种同一块 ≠ 已经是同一份扩展。
