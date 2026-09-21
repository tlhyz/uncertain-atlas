# 反模式：把参数更新写了 H+1 不是已经是扩展启用高度那种切换 not already ve-height-switch / not already only-filled-field / not already abci20 正式三事（333 余量）说成已经是扩展启用高度切换 / 已经只改填的那一项 / 已经切到 ABCI 2.0

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[参数更新写了 H+1 not already ve-height-switch ≠ bundled（333）](../../tracks/implementation/worked-example-paramsdelay-notveheight-vs-bundled.md)。

## 卖法

把参数更新写了 H+1 / H+1 已经按新参数 / 参数生效写成 H+1 写成已经是扩展启用高度那种 H / H+1 Prepare 切换 interchangeable / 已经 ve-height-switch interchangeable / 已经扩展启用切换交差 interchangeable / 333 paramsdelay bundled interchangeable / 33 four gates interchangeable / paramsdelay-sold-as-validatordelay interchangeable；把立刻生效 / 不是 Finalize 没回就清掉 / 不是只填一个字段就只改这一项 写成已经只改填的那一项 interchangeable / 已经 only-filled-field interchangeable；把写了 H+1 就当成切换 / 切到 ABCI 2.0 的联想 / 扩展启用那种切换口 写成已经切到 ABCI 2.0 interchangeable / 已经 abci20 interchangeable，或已经和 333 paramsdelay bundled / paramsdelay-sold-as-validatordelay interchangeable / 757 paramsdelay-notveheight interchangeable。

## 为什么错

官方把参数更新写了 H+1 单句、already ve-height-switch、already only-filled-field、already abci20 写成三件独立的实现事。把它们卖成 already ve-height-switch interchangeable / already only-filled-field interchangeable / already abci20 interchangeable，会把 not already ve-height-switch、not already only-filled-field、not already abci20 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看参数更新写了 H+1 不是已经是扩展启用高度那种切换 not already ve-height-switch / not already only-filled-field / not already abci20 正式三事（333 余量），必须分开 not already ve-height-switch、not already only-filled-field、not already abci20 三件事，不要和 333 / 33 / 319 / 330 / 755 / 756 糊成一句。

## 和相邻反模式

- [paramsdelay-sold-as-validatordelay](paramsdelay-sold-as-validatordelay.md) 是 ConsensusParams 生效延迟 bundled 全段，不是本页参数更新写了 H+1 item 3 单句边界。
- [paramsdelay-noth-sold-as-bundled](paramsdelay-noth-sold-as-bundled.md) 是本高回了 item 1，不是本页扩展启用高度边界。
- [paramsdelay-notvalidatorh2-sold-as-bundled](paramsdelay-notvalidatorh2-sold-as-bundled.md) 是验证人 H+2 item 2，不是本页扩展启用高度边界。
- [veheight-sold-as-prepared](veheight-sold-as-prepared.md) 是到了 H 已经 Prepare 带了扩展（330），不是本页参数写了 H+1 单句边界。
- [consensusparams-sold-as-updated](consensusparams-sold-as-updated.md) 是空/没回/只填一项（319），不是本页立刻生效单句边界。
