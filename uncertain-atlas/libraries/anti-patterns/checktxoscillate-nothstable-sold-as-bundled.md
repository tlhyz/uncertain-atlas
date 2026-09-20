# 反模式：把还在振荡不是已经过了 h_stable not already past-hstable / not already left-pool / not already in-block 正式三事（328 余量）说成已经过了 h_stable / 已经离池 / 已经进了块

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[还在振荡 not already past-hstable ≠ bundled（328）](../../tracks/implementation/worked-example-checktxoscillate-nothstable-vs-bundled.md)。

## 卖法

把还在振荡 / 还在成功和失败之间来回 / 此刻来回 写成已经过了 h_stable interchangeable / 已经 past-hstable interchangeable / 已经过了稳定高交差 interchangeable / 328 checktxoscillate bundled interchangeable / 33 four gates interchangeable / checktxcode-sold-as-stable interchangeable；把还在池里 / 本节点池里还在 / 待得够久之前 写成已经离池 interchangeable / 已经 left-pool interchangeable；把最终不再振荡 / 不再来回 / Requirement 13 保证最终 写成已经进了块 interchangeable / 已经 in-block interchangeable，或已经和 328 checktxoscillate bundled / checktxcode-sold-as-stable interchangeable / 741 checktxoscillate-nothstable interchangeable。

## 为什么错

官方把还在振荡单句、already past-hstable、already left-pool、already in-block 写成三件独立的实现事。把它们卖成 already past-hstable interchangeable / already left-pool interchangeable / already in-block interchangeable，会把 not already past-hstable、not already left-pool、not already in-block 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看还在振荡不是已经过了 h_stable not already past-hstable / not already left-pool / not already in-block 正式三事（328 余量），必须分开 not already past-hstable、not already left-pool、not already in-block 三件事，不要和 328 / 33 / 301 / 740 / 742 糊成一句。

## 和相邻反模式

- [checktxcode-sold-as-stable](checktxcode-sold-as-stable.md) 是 CheckTx 最终不再振荡 bundled 全段，不是本页 h_stable item 2 单句边界。
- [checktxoscillate-notcode-sold-as-bundled](checktxoscillate-notcode-sold-as-bundled.md) 是有码 item 1，不是本页还在振荡与过了 h_stable 边界。
- [proposed-sold-as-removed](proposed-sold-as-removed.md) 是提案收了已经从池里删掉（301），不是本页还在池里边界。
