# 模式：把 H+1 立刻用了新参数不是已经是验证人集合那种 H+2 才计票 not already validator-h2 / not already last-commit-h3 / not already same-as-35 正式三事（333 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Updating Consensus Parameters。  
**例**：[H+1 立刻用了新参数 not already validator-h2 ≠ bundled（333）](../../tracks/implementation/worked-example-paramsdelay-notvalidatorh2-vs-bundled.md)。

## 三个名字

1. **H+1 立刻用了新参数 不是 already validator-h2：** 看见 H+1 立刻用了新参数 / 参数已经在 H+1 用上 / 参数走 H→H+1，不是已经是验证人集合那种 H+2 才计票 interchangeable / 已经新人 H+2 计票交差 interchangeable，不是 333 paramsdelay bundled interchangeable / 33 four gates interchangeable / paramsdelay-sold-as-validatordelay interchangeable。

2. **「立刻」 不是 already last-commit-h3：** 看见「立刻」 / 立刻生效 / 参数立刻对 H+1，不是已经是 H+3 才带 last_commit interchangeable / 已经和 NextValidatorsHash / ValidatorsHash / last_commit 同一张表交差 interchangeable，不是 35 validator-delay interchangeable / 333 paramsdelay item 1 interchangeable。

3. **参数延迟 不是 already same-as-35：** 看见参数延迟 / 参数那种延迟 / 参数 H→H+1 延迟，不是已经是不变量 35 那三条高度 interchangeable / 已经验证人三条高度交差 interchangeable，不是 35 validator-delay interchangeable / 333 paramsdelay item 3 interchangeable。

官方把 H+1 立刻用了新参数单句、already validator-h2、already last-commit-h3、already same-as-35 写成三个名字。把它们叫成一个「看见 H+1 立刻用了新参数就已经是验证人 H+2 interchangeable / 就已经是 H+3 last_commit interchangeable / 就已经是不变量 35 interchangeable」，会把 not already validator-h2、not already last-commit-h3、not already same-as-35 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 H+1 立刻用了新参数不是已经是验证人集合那种 H+2 才计票 not already validator-h2 / not already last-commit-h3 / not already same-as-35 正式三事（333 余量），先数清问的是 H+1 立刻用了新参数 是不是 already validator-h2 / 333 / paramsdelay-sold-as-validatordelay，是不是「立刻」 是不是 already last-commit-h3，还是参数延迟 是不是 already same-as-35，再决定要不要同一次发布。333 paramsdelay vs set bundled unbundling 在本页 item 2 续。
