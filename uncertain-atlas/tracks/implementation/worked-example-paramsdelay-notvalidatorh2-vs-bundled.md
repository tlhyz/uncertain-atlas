# 例：看见 H+1 立刻用了新参数 / 看见「立刻」 / 看见参数延迟 is not already already validator-h2 interchangeable / already last-commit-h3 interchangeable / already same-as-35 interchangeable

**层次**：实现 / H+1 立刻用了新参数不是已经是验证人集合那种 H+2 才计票 not already validator-h2 / not already last-commit-h3 / not already same-as-35 正式三事（333 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Updating Consensus Parameters / `FinalizeBlock`, `PrepareProposal`/`ProcessProposal`。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「H+1 立刻用了新参数不是已经是验证人集合那种 H+2 才计票 not already validator-h2 / not already last-commit-h3 / not already same-as-35 正式三事（333 余量）/ not 756 paramsdelay-notvalidatorh2 interchangeable / not 333 paramsdelay bundled interchangeable」，不是 ConsensusParams 生效延迟 bundled（333），也不是本高回了 ConsensusParams 不是已经在本高生效（755 item 1 余量）或参数更新写了 H+1 不是已经是扩展启用高度那种切换（757 item 3 余量）。不要另写怎样编 `ConsensusParams` 或怎样选启用高度。

## 官方三件事

规范把 Requirements 里参数更新 H 回了就对 H+1 立刻生效、集合更新处理 H 之后只在 H+2 生效 和「已经是 H+1 立刻用了新参数就已经是验证人集合那种 H+2 才计票 interchangeable / 已经是立刻就已经是 H+3 才带 last_commit interchangeable / 已经是参数延迟就已经是不变量 35 那三条高度 interchangeable / 已经是 paramsdelay bundled interchangeable」分开写成三件独立的实现事，不是「看见 H+1 立刻用了新参数就已经是验证人 H+2 interchangeable / 就已经是 H+3 last_commit interchangeable / 就已经是不变量 35 interchangeable」一件事：

1. **看见 H+1 立刻用了新参数 / 看见参数已经在 H+1 用上 / 看见参数走 H→H+1 is not already 已经是验证人集合那种 H+2 才计票 interchangeable / 已经 validator-h2 interchangeable / 已经新人 H+2 计票交差 interchangeable / 333 paramsdelay bundled interchangeable / 33 four gates interchangeable / paramsdelay-sold-as-validatordelay interchangeable，也不是已经 ConsensusParams 生效延迟 bundled（333） interchangeable / 756 paramsdelay-notvalidatorh2 interchangeable / 333 paramsdelay item 2 interchangeable，也不是已经 H+1 立刻用了新参数不是已经是验证人集合那种 H+2 才计票 not already validator-h2 / not already last-commit-h3 / not already same-as-35 正式三事 bundled（333 item 2 余量） interchangeable / 333 paramsdelay item 2 interchangeable，也不是已经本高回了不是已经在本高生效（755） interchangeable / 757 paramsdelay-notveheight interchangeable / 35 validator-delay interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方把集合更新写成处理 H 之后只在 **H+2** 生效；参数更新写成 H 回了就对 **H+1** 立刻生效。看见参数已经在 H+1 用上，不是已经 validator-h2 interchangeable——333 钉 bundled 三事，本页从 item 2 侧钉 not already validator-h2 单句。看见 H+1 立刻用了新参数，不是已经 ConsensusParams 生效延迟 bundled（333） interchangeable——333 钉 bundled，本页钉 item 2 第一件事。看见参数走 H→H+1，不是已经验证人集合 H+1 / H+2 / H+3（35） interchangeable——35 另钉。333 paramsdelay vs set bundled unbundling 在本页 item 2 续。

2. **看见「立刻」 / 看见立刻生效 / 看见参数立刻对 H+1 is not already 已经是 H+3 才带 last_commit interchangeable / 已经 last-commit-h3 interchangeable / 已经和 NextValidatorsHash / ValidatorsHash / last_commit 同一张表交差 interchangeable / 333 paramsdelay bundled interchangeable / 35 validator-delay interchangeable，也不是已经 ConsensusParams 生效延迟 bundled（333） interchangeable / 756 paramsdelay-notvalidatorh2 interchangeable / 333 paramsdelay item 1 本高回了 interchangeable / 333 paramsdelay item 3 扩展启用 interchangeable，也不是已经 H+1 立刻用了新参数不是已经是验证人集合那种 H+2 才计票 not already validator-h2 / not already last-commit-h3 / not already same-as-35 正式三事 bundled（333 item 2 余量） interchangeable / 333 paramsdelay item 2 interchangeable，也不是已经是验证人集合那种 H+2 才计票（本页第一件事） interchangeable。**  
   官方写：看见「立刻」，不是已经和 NextValidatorsHash / ValidatorsHash / last_commit 同一张表。看见立刻生效，不是已经 last-commit-h3 interchangeable——本页钉 not already last-commit-h3 单句。看见参数立刻对 H+1，不是已经是验证人集合那种 H+2 才计票（本页第一件事） interchangeable——三件事分开钉。333 paramsdelay vs set bundled unbundling 在本页 item 2 续。

3. **看见参数延迟 / 看见参数那种延迟 / 看见参数 H→H+1 延迟 is not already 已经是不变量 35 那三条高度 interchangeable / 已经 same-as-35 interchangeable / 已经验证人三条高度交差 interchangeable / 333 paramsdelay bundled interchangeable / 35 validator-delay interchangeable，也不是已经 ConsensusParams 生效延迟 bundled（333） interchangeable / 756 paramsdelay-notvalidatorh2 interchangeable / 333 paramsdelay item 1 / 333 paramsdelay item 3，也不是已经 H+1 立刻用了新参数不是已经是验证人集合那种 H+2 才计票 not already validator-h2 / not already last-commit-h3 / not already same-as-35 正式三事 bundled（333 item 2 余量） interchangeable / 333 paramsdelay item 2 interchangeable，也不是已经是验证人集合那种 H+2 才计票（本页第一件事） interchangeable / 已经是 H+3 才带 last_commit（本页第二件事） interchangeable。**  
   官方写：看见参数延迟，不是已经是不变量 35 那三条高度。看见参数那种延迟，不是已经 same-as-35 interchangeable——本页钉 not already same-as-35 单句。看见参数 H→H+1 延迟，不是已经验证人集合 H+1 / H+2 / H+3（35） interchangeable——35 另钉全段。看见参数延迟，不是已经是 H+3 才带 last_commit（本页第二件事） interchangeable——三件事分开钉。333 paramsdelay vs set bundled unbundling 在本页 item 2 续。

怎样编 `ConsensusParams`、默认 MaxBytes / MaxGas、怎样选启用高度是规范里的取值或做法，本页不抄。ConsensusParams 生效延迟 bundled（333）、本高回了 ConsensusParams 不是已经在本高生效（333 item 1 余量 / 755）、参数更新写了 H+1 不是已经是扩展启用高度那种切换（333 item 3 余量 / 757）、验证人集合 H+1 / H+2 / H+3（35）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **H+1 立刻用了新参数 not already validator-h2 ≠ 333 / 33 interchangeable：** 官方把参数延迟和集合延迟分开。
- **「立刻」 not already last-commit-h3 ≠ 已经是 H+3 才带 last_commit interchangeable：** 官方把参数立刻对 H+1 和集合 last_commit 表分开。
- **参数延迟 not already same-as-35 ≠ 已经是不变量 35 那三条高度 interchangeable：** 官方把参数延迟和验证人三条高度分开；333 paramsdelay vs set bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| H+1 立刻用了新参数 | 不是 already validator-h2 | 不是验证人三条高度 alone（35） |
| 「立刻」 | 不是 already last-commit-h3 | 不是本高回了 alone（755） |
| 参数延迟 | 不是 already same-as-35 | 不是扩展启用高度 alone（330） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 H+1 立刻用了新参数不是已经是验证人集合那种 H+2 才计票 not already validator-h2 / not already last-commit-h3 / not already same-as-35 正式三事（333 余量），必须分开 H+1 立刻用了新参数 是不是 already validator-h2 interchangeable / 333 paramsdelay bundled interchangeable / paramsdelay-sold-as-validatordelay interchangeable、「立刻」 是不是 already last-commit-h3 interchangeable、参数延迟 是不是 already same-as-35 interchangeable。可以跳过「看见 H+1 立刻用了新参数就已经是验证人 H+2 interchangeable / 就已经是 H+3 last_commit interchangeable / 就已经是不变量 35 interchangeable」。不要另写怎样编 `ConsensusParams`。333 paramsdelay vs set bundled unbundling 在本页 item 2 续（755 + 756）；续 [`worked-example-paramsdelay-notveheight-vs-bundled.md`](worked-example-paramsdelay-notveheight-vs-bundled.md)（不变量 757 item 3）。

## 本页不抄

- 怎样编 `ConsensusParams`、默认 MaxBytes / MaxGas、怎样选启用高度。
- ConsensusParams 生效延迟 bundled。那是不变量 333。
- 本高回了 ConsensusParams 不是已经在本高生效。那是不变量 333 item 1 余量 / 755。
- 参数更新写了 H+1 不是已经是扩展启用高度那种切换。那是不变量 333 item 3 余量 / 757。
- 验证人集合 H+1 / H+2 / H+3。那是不变量 35。
- 到了 H 已经 Prepare 带了扩展。那是不变量 330。
- 四门已经结算。那是不变量 33。
