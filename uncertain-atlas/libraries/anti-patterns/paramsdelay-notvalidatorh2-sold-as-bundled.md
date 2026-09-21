# 反模式：把 H+1 立刻用了新参数不是已经是验证人集合那种 H+2 才计票 not already validator-h2 / not already last-commit-h3 / not already same-as-35 正式三事（333 余量）说成已经是验证人 H+2 / 已经是 H+3 last_commit / 已经是不变量 35

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[H+1 立刻用了新参数 not already validator-h2 ≠ bundled（333）](../../tracks/implementation/worked-example-paramsdelay-notvalidatorh2-vs-bundled.md)。

## 卖法

把 H+1 立刻用了新参数 / 参数已经在 H+1 用上 / 参数走 H→H+1 写成已经是验证人集合那种 H+2 才计票 interchangeable / 已经 validator-h2 interchangeable / 已经新人 H+2 计票交差 interchangeable / 333 paramsdelay bundled interchangeable / 33 four gates interchangeable / paramsdelay-sold-as-validatordelay interchangeable；把「立刻」 / 立刻生效 / 参数立刻对 H+1 写成已经是 H+3 才带 last_commit interchangeable / 已经 last-commit-h3 interchangeable；把参数延迟 / 参数那种延迟 / 参数 H→H+1 延迟 写成已经是不变量 35 那三条高度 interchangeable / 已经 same-as-35 interchangeable，或已经和 333 paramsdelay bundled / paramsdelay-sold-as-validatordelay interchangeable / 756 paramsdelay-notvalidatorh2 interchangeable。

## 为什么错

官方把 H+1 立刻用了新参数单句、already validator-h2、already last-commit-h3、already same-as-35 写成三件独立的实现事。把它们卖成 already validator-h2 interchangeable / already last-commit-h3 interchangeable / already same-as-35 interchangeable，会把 not already validator-h2、not already last-commit-h3、not already same-as-35 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 H+1 立刻用了新参数不是已经是验证人集合那种 H+2 才计票 not already validator-h2 / not already last-commit-h3 / not already same-as-35 正式三事（333 余量），必须分开 not already validator-h2、not already last-commit-h3、not already same-as-35 三件事，不要和 333 / 33 / 35 / 755 / 757 糊成一句。

## 和相邻反模式

- [paramsdelay-sold-as-validatordelay](paramsdelay-sold-as-validatordelay.md) 是 ConsensusParams 生效延迟 bundled 全段，不是本页 H+1 立刻用了新参数 item 2 单句边界。
- [paramsdelay-noth-sold-as-bundled](paramsdelay-noth-sold-as-bundled.md) 是本高回了 item 1，不是本页参数与集合延迟边界。
- [paramsdelay-notveheight-sold-as-bundled](paramsdelay-notveheight-sold-as-bundled.md) 是扩展启用高度（333 item 3），不是本页验证人 H+2 item 2 单句边界。
- [validator-update-sold-as-immediate](validator-update-sold-as-immediate.md) 是验证人集合延迟（35），不是本页参数 H→H+1 单句边界。
