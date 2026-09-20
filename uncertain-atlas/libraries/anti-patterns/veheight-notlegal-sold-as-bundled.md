# 反模式：把 h < H 带了扩展不是已经合法 not already legal / not already enabled / not already abci20 正式三事（330 余量）说成已经合法 / 已经启用 / 已经切到 ABCI 2.0

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[h < H 带了扩展 not already legal ≠ bundled（330）](../../tracks/implementation/worked-example-veheight-notlegal-vs-bundled.md)。

## 卖法

把 h < H 带了扩展 / 启用前带了扩展 / 带扩展的预提交 写成已经合法 interchangeable / 已经 legal interchangeable / 已经合法交差 interchangeable / 330 veheight bundled interchangeable / 33 four gates interchangeable / veheight-sold-as-prepared interchangeable；把已经启用 / 字段在 / H 之后不能关 写成已经启用交差 interchangeable / 已经 enabled interchangeable；把切到 ABCI 2.0 / 已经是 ABCI 2.0 / 切换完成 写成已经切到 ABCI 2.0 interchangeable / 已经 abci20 interchangeable，或已经和 330 veheight bundled / veheight-sold-as-prepared interchangeable / 748 veheight-notlegal interchangeable。

## 为什么错

官方把 h < H 带了扩展单句、already legal、already enabled、already abci20 写成三件独立的实现事。把它们卖成 already legal interchangeable / already enabled interchangeable / already abci20 interchangeable，会把 not already legal、not already enabled、not already abci20 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 h < H 带了扩展不是已经合法 not already legal / not already enabled / not already abci20 正式三事（330 余量），必须分开 not already legal、not already enabled、not already abci20 三件事，不要和 330 / 33 / 34 / 58 / 346 / 746 / 747 糊成一句。

## 和相邻反模式

- [veheight-sold-as-prepared](veheight-sold-as-prepared.md) 是 VoteExtensionsEnableHeight bundled 全段，不是本页合法 item 3 单句边界。
- [veheight-notprepare-sold-as-bundled](veheight-notprepare-sold-as-bundled.md) 是到了 H item 1，不是本页合法边界。
- [veheight-notthissigned-sold-as-bundled](veheight-notthissigned-sold-as-bundled.md) 是本高度刚签 item 2，不是本页合法边界。
- [enable-height-sold-as-safe](enable-height-sold-as-safe.md) 是治理改 enable-height 会 panic（58），不是本页启用单句边界。
