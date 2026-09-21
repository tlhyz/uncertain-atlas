# 反模式：把填了两个不是已经启用 PBTS not already pbts-enabled / not already switched / not already cannot-off 正式三事（336 余量）说成已经启用 PBTS / 已经切到 PBTS / 已经不能关

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[填了两个 not already pbts-enabled ≠ bundled（336）](../../tracks/implementation/worked-example-precision-notpbts-vs-bundled.md)。

## 卖法

把填了两个 / Precision 和 MessageDelay 都填了 / 两把尺都在 写成已经启用 PBTS interchangeable / 已经 pbts-enabled interchangeable / 已经到了 PbtsEnableHeight 交差 interchangeable / 336 precision bundled interchangeable / 40 block-time interchangeable / precision-sold-as-msgdelay interchangeable；把这两个参数用于 PBTS / 写了用于 PBTS / 参数写给 PBTS 写成已经切到 PBTS interchangeable / 已经 switched interchangeable；把参数在 / 同步参数还在 / 两把尺还在表里 写成已经不能关 interchangeable / 已经 cannot-off interchangeable，或已经和 336 precision bundled / precision-sold-as-msgdelay interchangeable / 762 precision-notpbts interchangeable。

## 为什么错

官方把填了两个单句、already pbts-enabled、already switched、already cannot-off 写成三件独立的实现事。把它们卖成 already pbts-enabled interchangeable / already switched interchangeable / already cannot-off interchangeable，会把 not already pbts-enabled、not already switched、not already cannot-off 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看填了两个不是已经启用 PBTS not already pbts-enabled / not already switched / not already cannot-off 正式三事（336 余量），必须分开 not already pbts-enabled、not already switched、not already cannot-off 三件事，不要和 336 / 40 / 330 / 761 / 763 糊成一句。

## 和相邻反模式

- [precision-noteternal-sold-as-bundled](precision-noteternal-sold-as-bundled.md) 是用于 PBTS ≠ 已经是永恒常数（336 item 3），不是本页填了两个 item 2 单句边界。
- [precision-sold-as-msgdelay](precision-sold-as-msgdelay.md) 是 Precision bundled 全段，不是本页填了两个 item 2 单句边界。
- [precision-notmsgdelay-sold-as-bundled](precision-notmsgdelay-sold-as-bundled.md) 是填了 Precision ≠ 已经是 MessageDelay（336 item 1），不是本页填了两个 ≠ 已经启用 PBTS 边界。
- [veheight-sold-as-prepared](veheight-sold-as-prepared.md) 是到了 H ≠ 已经 Prepare 带了扩展（330），不是本页写了用于 PBTS 边界。
- [pbts-sold-as-mtp](pbts-sold-as-mtp.md) 是块时间必须点名算法（40），不是本页参数在 ≠ 已经不能关 边界。
