# 反模式：把 retain_height 默认 0 不是已经在剪 not already pruning / not already settled / not already no-history 正式三事（366 余量）说成已经在剪 / 已经交差 / 已经没有历史

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[默认 0 全留 not already pruning ≠ bundled（366）](../../tracks/implementation/worked-example-retain-notpruning-vs-bundled.md)。

## 卖法

把默认 0 全留 / `retain_height` 默认是 `0`、表示全留 / 字段在 写成已经在剪 interchangeable / 已经 pruning interchangeable / 已经在剪交差 interchangeable / 366 retain bundled interchangeable / retain-sold-as-kept interchangeable；把没填 / 没填 retain_height / 字段在没回非零 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable；把 Commit 回了 / Commit 回了高度 / 回了字段 写成已经没有历史 interchangeable / 已经 no-history interchangeable / 已经没有历史交差 interchangeable，或已经和 366 retain bundled / retain-sold-as-kept interchangeable / 845 retain-notpruning interchangeable。

## 为什么错

官方把默认 0 全留、不是已经交差、不是已经没有历史写成三件独立的实现事。把它们卖成 already pruning interchangeable / already settled interchangeable / already no-history interchangeable，会把 not already pruning、not already settled、not already no-history 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 retain_height 默认 0 不是已经在剪 not already pruning / not already settled / not already no-history 正式三事（366 余量），必须分开 not already pruning、not already settled、not already no-history 三件事，不要和 366 / 320 / 846 / 847 糊成一句。

## 和相邻反模式

- [retain-sold-as-kept](retain-sold-as-kept.md) 是 retain bundled 全段，不是本页默认 0 全留 item 1 单句边界。
- [crashsteps-sold-as-committed](crashsteps-sold-as-committed.md) 是崩溃三步就已经 Commit（320），不是本页 not already pruning 边界。
- [commitretaincaution-notdefaultzero-sold-as-bundled](commitretaincaution-notdefaultzero-sold-as-bundled.md) 是 Use retain_height with caution vs defaults to 0（677），不是本页 not already settled 单句。
