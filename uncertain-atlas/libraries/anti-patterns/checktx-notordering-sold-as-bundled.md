# 反模式：把不该验排序相关有效性不是已经该在 CheckTx 里验 not already in-checktx / not already exec-state / not already settled 正式三事（339 余量）说成已经该在 CheckTx 里验 / 已经按执行态验过 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[不该验所有 not already in-checktx ≠ bundled（339）](../../tracks/implementation/worked-example-checktx-notordering-vs-bundled.md)。

## 卖法

把 CheckTx 不该验所有有效性 / 不该把影响有效性的每件事都验完 / 不该验排序相关 写成已经该在 CheckTx 里验排序 interchangeable / 已经 in-checktx interchangeable / 已经该写进 CheckTx 交差 interchangeable / 339 checktxweak bundled interchangeable / 312 checktxstate interchangeable / checktxweak-sold-as-consensus interchangeable；把有效性依赖排序 / 排序会改有效性 / 有效性可能依赖交易排序 写成已经按将要执行的那份验过 interchangeable / 已经 exec-state interchangeable；把过了 CheckTx / CheckTx 绿了 / 弱过滤器放过了 写成已经交差 interchangeable / 已经 settled interchangeable，或已经和 339 checktxweak bundled / checktxweak-sold-as-consensus interchangeable / 770 checktx-notordering interchangeable。

## 为什么错

官方把不该验所有单句、already in-checktx、already exec-state、already settled 写成三件独立的实现事。把它们卖成 already in-checktx interchangeable / already exec-state interchangeable / already settled interchangeable，会把 not already in-checktx、not already exec-state、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看不该验排序相关有效性不是已经该在 CheckTx 里验 not already in-checktx / not already exec-state / not already settled 正式三事（339 余量），必须分开 not already in-checktx、not already exec-state、not already settled 三件事，不要和 339 / 312 / 33 / 313 / 771 / 772 糊成一句。

## 和相邻反模式

- [checktxweak-sold-as-consensus](checktxweak-sold-as-consensus.md) 是 CheckTx 弱过滤器 bundled 全段，不是本页不该验所有 item 1 单句边界。
- [checktxstate-sold-as-execute](checktxstate-sold-as-execute.md) 是 CheckTxState ≠ 已经是 ExecuteTxState（312），不是本页不该验排序 ≠ 已经该在 CheckTx 里验 边界。
- [checktx-sold-as-prepared](checktx-sold-as-prepared.md) 是四门已经结算（33），不是本页过了 CheckTx ≠ 已经交差 边界。
- [indexer-sold-as-replay](indexer-sold-as-replay.md) 是索引器 ≠ 已经保证不重放（313），不是本页排序会改有效性边界。
