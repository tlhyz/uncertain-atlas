# 模式：把 FinalizeBlock tx_results Code==0 完全合法正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[Code == 0 only if fully valid ≠ 已经 CheckTx 过了](../../tracks/implementation/worked-example-fintxcode-vs-invalid.md)。

## 三个名字

1. **Code == 0 only if fully valid 不是已经 CheckTx 过了：** 看见 only if fully valid 不是已经 Process 回了 Accept。
2. **Code == 0 only if fully valid 不是已经 Code != 0 那种没进块：** 看见 fully valid 不是已经无效就不在块里。
3. **回了 tx_results 不是已经 Finalize 改了就已经交差：** 看见有 Code 不是已经 Code / Data 印进本头就等于已经交差。

## 为什么要分开叫

官方把 `tx_results[i].Code == 0` only if fully valid、Code 非零仍可能在块里、Finalize 回包和交差 / 印进本头写成三个名字。把它们叫成一个「看见 Finalize 回了 tx_results 就已经 CheckTx 过了」，会把 fully valid 语义、在块里与否和交差三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见回了 0 就已经没进块」，先数清问的是 Code == 0 only if fully valid 是不是已经 CheckTx 过了、是不是已经 Code != 0 那种没进块，还是回了 tx_results 是不是已经 Finalize 改了就已经交差，再决定要不要同一次发布。
