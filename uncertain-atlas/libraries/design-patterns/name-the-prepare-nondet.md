# 模式：把 Prepare / ExtendVote 没有确定性要求三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements，Req 11–12 之后。  
**例**：[Prepare 没有确定性要求 ≠ 已经必须确定](../../tracks/implementation/worked-example-prepare-nondet-vs-process.md)。

## 三个名字

1. **Prepare 没有确定性要求不是已经必须确定：** 看见可以依赖其它值不是已经和 Process / Finalize 同一把尺。
2. **两边 raw 一样不是已经是同一份提案：** 看见 *v_p = v_q* 不是已经是同一份 prepared。
3. **ExtendVote 没有确定性要求不是已经是同一份扩展：** 看见同一块不是已经是同一份 *e*。

## 为什么要分开叫

官方把 Prepare 没有确定性要求、同一份 raw 不蕴涵同一份 prepared、同一块不蕴涵同一份扩展写成三件事。把它们叫成一个「看见可以不确定就必须确定」，会把四门、提议超时和验签扩展一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见可以不确定就必须确定」，先数清问的是 Prepare 没有确定性要求不是已经必须确定、两边 raw 一样不是已经是同一份提案，还是 ExtendVote 没有确定性要求不是已经是同一份扩展，再决定要不要同一次发布。
