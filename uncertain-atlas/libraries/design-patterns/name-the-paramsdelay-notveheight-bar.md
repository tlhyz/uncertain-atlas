# 模式：把参数更新写了 H+1 不是已经是扩展启用高度那种切换 not already ve-height-switch / not already only-filled-field / not already abci20 正式三事（333 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Updating Consensus Parameters。  
**例**：[参数更新写了 H+1 not already ve-height-switch ≠ bundled（333）](../../tracks/implementation/worked-example-paramsdelay-notveheight-vs-bundled.md)。

## 三个名字

1. **参数更新写了 H+1 不是 already ve-height-switch：** 看见参数更新写了 H+1 / H+1 已经按新参数 / 参数生效写成 H+1，不是已经是扩展启用高度那种 H / H+1 Prepare 切换 interchangeable / 已经扩展启用切换交差 interchangeable，不是 333 paramsdelay bundled interchangeable / 33 four gates interchangeable / paramsdelay-sold-as-validatordelay interchangeable。

2. **立刻生效 不是 already only-filled-field：** 看见立刻生效 / 不是 Finalize 没回就清掉 / 不是只填一个字段就只改这一项，不是已经只改填的那一项 interchangeable / 已经保持没填的字段交差 interchangeable，不是 319 consensusparams interchangeable / 333 paramsdelay item 1 interchangeable。

3. **写了 H+1 就当成切换 不是 already abci20：** 看见写了 H+1 就当成切换 / 切到 ABCI 2.0 的联想 / 扩展启用那种切换口，不是已经切到 ABCI 2.0 interchangeable / 已经 ABCI 2.0 切换交差 interchangeable，不是 330 veheight interchangeable / 333 paramsdelay item 2 interchangeable。

官方把参数更新写了 H+1 单句、already ve-height-switch、already only-filled-field、already abci20 写成三个名字。把它们叫成一个「看见参数更新写了 H+1 就已经是扩展启用高度切换 interchangeable / 就已经只改填的那一项 interchangeable / 就已经切到 ABCI 2.0 interchangeable」，会把 not already ve-height-switch、not already only-filled-field、not already abci20 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看参数更新写了 H+1 不是已经是扩展启用高度那种切换 not already ve-height-switch / not already only-filled-field / not already abci20 正式三事（333 余量），先数清问的是参数更新写了 H+1 是不是 already ve-height-switch / 333 / paramsdelay-sold-as-validatordelay，是不是立刻生效 是不是 already only-filled-field，还是写了 H+1 就当成切换 是不是 already abci20，再决定要不要同一次发布。333 paramsdelay vs set bundled unbundling 在本页 item 3 完成。
