# 反模式：把用于 PBTS 不是已经是永恒常数 not already eternal-constant / not already bft-median / not already clock-adjust 正式三事（336 余量）说成已经是永恒常数 / 已经是 BFT Time 中位数 / 已经是调整钟

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[用于 PBTS not already eternal-constant ≠ bundled（336）](../../tracks/implementation/worked-example-precision-noteternal-vs-bundled.md)。

## 卖法

把用于 PBTS / 两把尺给 PBTS 用 / 写了 PBTS 用 写成已经是永恒常数 interchangeable / 已经 eternal-constant interchangeable / 已经抄成产品常数交差 interchangeable / 336 precision bundled interchangeable / 40 block-time interchangeable / precision-sold-as-msgdelay interchangeable；把能出合法提案 / 仍能出合法提案 / 提案还能过 写成已经是 BFT Time 中位数 interchangeable / 已经 bft-median interchangeable；把两把尺 / Precision 和 MessageDelay / 同步参数两栏 写成已经是调整钟 interchangeable / 已经 clock-adjust interchangeable，或已经和 336 precision bundled / precision-sold-as-msgdelay interchangeable / 763 precision-noteternal interchangeable。

## 为什么错

官方把用于 PBTS 单句、already eternal-constant、already bft-median、already clock-adjust 写成三件独立的实现事。把它们卖成 already eternal-constant interchangeable / already bft-median interchangeable / already clock-adjust interchangeable，会把 not already eternal-constant、not already bft-median、not already clock-adjust 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看用于 PBTS 不是已经是永恒常数 not already eternal-constant / not already bft-median / not already clock-adjust 正式三事（336 余量），必须分开 not already eternal-constant、not already bft-median、not already clock-adjust 三件事，不要和 336 / 40 / 330 / 761 / 762 糊成一句。

## 和相邻反模式

- [precision-sold-as-msgdelay](precision-sold-as-msgdelay.md) 是 Precision bundled 全段，不是本页用于 PBTS item 3 单句边界。
- [precision-notmsgdelay-sold-as-bundled](precision-notmsgdelay-sold-as-bundled.md) 是填了 Precision ≠ 已经是 MessageDelay（336 item 1），不是本页用于 PBTS ≠ 已经是永恒常数 边界。
- [precision-notpbts-sold-as-bundled](precision-notpbts-sold-as-bundled.md) 是填了两个 ≠ 已经启用 PBTS（336 item 2），不是本页用于 PBTS item 3 单句边界。
- [pbts-sold-as-mtp](pbts-sold-as-mtp.md) 是块时间必须点名算法（40），不是本页能出合法提案 ≠ 已经是中位数 边界。
