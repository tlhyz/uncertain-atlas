# 模式：把 MaxGas 三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Gas。  
**例**：[MaxGas ≠ 已经在执行](../../tracks/implementation/worked-example-maxgas-vs-enforced.md)。

## 三个名字

1. **MaxGas 不是已经在执行：** 看见默认 -1 不是已经有意义。
2. **GasUsed 不是已经算进共识：** 看见回包有字段不是已经被引擎验。
3. **已提交块不是已经按气验过：** 看见旧版只在池里管不是共识已经守了。

## 为什么要分开叫

官方把可选弱抽象、引擎忽略 GasUsed、旧版只在内存池管气写成三件事。把它们叫成一个「看见有气限就已经在卡」，会把 MaxBytes、默认体积和四门一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「已经有气限」，先数清问的是 MaxGas 不是已经在执行、GasUsed 不是已经算进共识，还是已提交块不是已经按气验过，再决定要不要同一次发布。
