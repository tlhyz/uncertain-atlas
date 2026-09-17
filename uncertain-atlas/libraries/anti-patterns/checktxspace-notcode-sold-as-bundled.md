# 反模式：把 CheckTx 回包 codespace not already response code / not already not-in-block / not already settled 正式三事（381 余量） 说成已经是回包码 / 已经没进块 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[CheckTx ≠ bundled（381）](../../tracks/implementation/worked-example-checktxspace-notcode-vs-bundled.md)。

## 卖法

把 CheckTx 回包这句写成已经已经是回包码 / 已经没进块 / 已经交差 interchangeable，或已经和 381 checktxspace-vs-code bundled / checktxspace-notcode-sold-as-bundled interchangeable。

## 为什么错

官方把 CheckTx 回包 codespace / events / lane_id 三条核心句写成三件独立的实现事。把它们卖成已经是回包码 / 已经没进块 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx 回包 codespace 正式三事（381 余量），必须分开 not already response code、not already not-in-block、not already settled 三件事，不要和 381 / 373 / 393 / 748 / 786 / 787 糊成一句。

## 和相邻反模式

- [checktxspace-sold-as-code](checktxspace-sold-as-code.md) 是 CheckTx 回包 bundled（381），不是本页 item 1 单句边界。
- [exectxgas-notcodespace-sold-as-bundled](exectxgas-notcodespace-sold-as-bundled.md) 是 ExecTxResult.codespace 就已经是 CheckTx 码空间（393/748），不是本页 CheckTx codespace 边界。
