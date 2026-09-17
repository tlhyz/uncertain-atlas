# 反模式：把 ExecTxResult.gas_wanted not CheckTx GasWanted / not already executing / not already settled 正式三事（393 余量） 说成已经是 CheckTx 的 GasWanted / 已经在执行 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[ExecTxResult.gas_wanted ≠ bundled（393）](../../tracks/implementation/worked-example-exectxgas-notwanted-vs-bundled.md)。

## 卖法

把 ExecTxResult 气这句写成已经已经是 CheckTx 的 GasWanted / 已经在执行 / 已经交差 interchangeable，或已经和 393 exectxgas-vs-checktx bundled / exectxgas-notwanted-sold-as-bundled interchangeable。

## 为什么错

官方把 ExecTxResult.gas_wanted / gas_used / codespace 三条核心句写成三件独立的实现事。把它们卖成已经是 CheckTx 的 GasWanted / 已经在执行 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExecTxResult.gas_wanted 正式三事（393 余量），必须分开 not CheckTx GasWanted、not already executing、not already settled 三件事，不要和 393 / 315 / 747 / 748 糊成一句。

## 和相邻反模式

- [exectxgas-sold-as-checktx](exectxgas-sold-as-checktx.md) 是 ExecTxResult 气 bundled（393），不是本页 item 1 单句边界。
- [exectxgas-notused-sold-as-bundled](exectxgas-notused-sold-as-bundled.md) 是 gas_used 单句边界（747 item 2），不是本页 gas_wanted 边界。
