# 模式：把 FinalizeBlock When Application executes block v 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When。  
**例**：[Application executes block v ≠ 已经把 v 落成这一高的决定](../../tracks/implementation/worked-example-finexec-vs-decided.md)。

## 三个名字

1. **Application executes block v 不是已经把 v 落成这一高的决定：** 看见 executes block v 不是已经 persist decision / 已经交差。
2. **Application executes block v 不是已经每个验证者都跑过 Process：** 看见 executes block v 不是已经是 ExecuteTxState。
3. **Application executes block v 不是已经套用 candidate 就不需要再在 Finalize 执行：** 看见 executes block v 不是已经 Process 跑过就不执行。

## 为什么要分开叫

官方把 When 第 3 步 Application executes block _v_、persist decision / 同步调 Finalize、以及 Process 保证 / apply candidate 写成三个名字。把它们叫成一个「看见调了 Finalize 就已经执行完」，会把落决定、Process 保证和 Finalize 执行义务三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 persist decision 就已经执行完」，先数清问的是 executes block v 是不是已经把 v 落成这一高的决定、是不是已经每个验证者都跑过 Process，还是是不是已经套用 candidate 就不需要再在 Finalize 执行，再决定要不要同一次发布。
