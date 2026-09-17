# 反模式：把 FinalizeBlock must provide values as a result of executing the block 正式三事卖成已经 Process 跑过就不用再执行

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[must provide 四列 ≠ 已经改了集合](../../tracks/implementation/worked-example-finasresult-vs-candidate.md)。

## 卖法

- 「看见 must provide 四列就已经改了集合 / 已经交差。」
- 「看见 Process 跑过 candidate，as a result of executing the block 就已经满足，不用再在 Finalize 执行。」
- 「看见 validator_updates / consensus_param_updates 空着，就没有 must provide 义务。」

## 为什么错

官方把 must provide values、as a result of executing the block、provided values 和 may be empty … keep the current values 写成三件独立的实现事。把它们卖成已经改了集合、已经 candidate 就不需要执行、空着就没有义务，会把 must provide 义务、执行来源和 empty keep current 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize must provide as a result of executing the block，必须分开 must provide 四列、as a result of executing the block、提供了值 三个名字，不要把它们卖成已经 Process 跑过就不用再执行。

## 和相邻反模式

- [finempty-sold-as-noset](finempty-sold-as-noset.md) 是 validator_updates 空则保持当前集合就已经没有集合，不是本页这种 must provide 四列不是已经改了集合。
- [fincand-sold-as-commit](fincand-sold-as-commit.md) 是 apply candidate 就已经交差，不是本页这种 as a result of executing 不是已经 candidate 就不需要执行。
- [fintxcode-sold-as-absent](fintxcode-sold-as-absent.md) 是 Code==0 就已经没进块，不是本页这种 must provide tx_results 不是已经 CheckTx 过了。
