# 例：看见 H+1 立刻用了新参数 is not already validator H+2 interchangeable / not already last_commit H+3 interchangeable / not already settled interchangeable

**层次**：实现 / H+1 立刻用了新参数 not already validator H+2 / not already last_commit H+3 / not already settled 正式三事（333 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Updating Consensus Parameters / `FinalizeBlock`, `PrepareProposal`/`ProcessProposal`。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「H+1 立刻用了新参数 not already validator H+2 / not already last_commit H+3 / not already settled 正式三事（333 余量）/ not 912 params-delay-notvalset interchangeable / not 333 params-delay-vs-set bundled interchangeable」，不是 ConsensusParams 生效延迟 bundled（333），也不是验证人集合 H+1 / H+2 / H+3（35），也不是 Finalize 回了 validator_updates 就已经 H+2 计票（459）。不要另写怎样编 ConsensusParams 或怎样选启用高度。

## 官方三件事

1. **看见 H+1 立刻用了新参数 / 看见参数走 H→H+1 这份立刻 is not already 已经是验证人集合那种 H+2 才计票 interchangeable，也不是已经 ConsensusParams 生效延迟 bundled（333） interchangeable / 912 params-delay-notvalset interchangeable / 911 params-delay-noteffective interchangeable / 333 params-delay item 1 本高 interchangeable，也不是已经 H+1 立刻用了新参数 not already validator H+2 / not already last_commit H+3 / not already settled 正式三事 bundled（333 item 2 余量） interchangeable / 333 params-delay item 2 interchangeable。**  
   官方把集合更新写成处理 H 之后只在 H+2 生效；参数更新写成 H 回了就对 H+1 立刻生效。看见参数已经在 H+1 用上，不是新人已经在 H+1 计票 interchangeable——本页从 333 item 2 侧钉 not already validator H+2 单句。333 params-delay vs set bundled unbundling 在本页 item 2 续。

2. **看见「立刻」 / 看见参数延迟 / 这份立刻 is not already 已经是 H+3 才带 last_commit interchangeable，也不是已经 ConsensusParams 生效延迟 bundled（333） interchangeable / 912 params-delay-notvalset interchangeable / 333 params-delay item 3 启用高度 interchangeable / 913 params-delay-notve interchangeable，也不是已经验证人集合 H+1 / H+2 / H+3 interchangeable / 35 height-effect interchangeable。**  
   官方把「立刻」和已经和 NextValidatorsHash / ValidatorsHash / last_commit 同一张表分开——333 bundled 第二件事常与 35 混成「看见参数 H+1 就已经是换人那种延迟 interchangeable」，本页钉 not already last_commit H+3 单句。

3. **看见参数延迟 / 看见立刻 / 这份立刻 is not already 已经交差 interchangeable，也不是已经 ConsensusParams 生效延迟 bundled（333） interchangeable / 912 params-delay-notvalset interchangeable / 911 params-delay-noteffective interchangeable，也不是已经 Finalize 回了 validator_updates 就已经 H+2 计票 interchangeable / 459 valupdate-delay interchangeable。**  
   官方把参数延迟和已经是不变量 35 那三条高度 / 已经交差分开。看见参数延迟，不是已经交差 interchangeable。333 params-delay vs set bundled unbundling 在本页 item 2 续。

怎样编 `ConsensusParams`、默认 MaxBytes / MaxGas、怎样选启用高度是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **H+1 立刻用了新参数 not already validator H+2 ≠ 已经是验证人集合那种 H+2 才计票 interchangeable：** 官方把参数延迟和集合延迟分开。
- **看见「立刻」 not already last_commit H+3 ≠ 已经是 H+3 才带 last_commit interchangeable：** 官方把立刻和 last_commit 那张表分开。
- **看见参数延迟 not already settled ≠ 已经交差 interchangeable：** 官方把参数延迟和已经交差分开；333 params-delay vs set bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| H+1 立刻用了新参数 | 不是已经是验证人集合那种 H+2 才计票 | 不是验证人集合 H+1 / H+2 / H+3（35） |
| 看见「立刻」 | 不是已经是 H+3 才带 last_commit | 不是 Finalize 回了 validator_updates 就已经 H+2（459） |
| 看见参数延迟 | 不是已经交差 | 不是本高回了就已经在本高生效（911） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 H+1 立刻用了新参数 not already validator H+2 / not already last_commit H+3 / not already settled 正式三事（333 余量），必须分开是不是已经是验证人集合那种 H+2 才计票、是不是已经是 H+3 才带 last_commit、是不是已经交差。可以跳过「看见参数 H+1 就已经是换人那种延迟」。不要另写怎样编 ConsensusParams 或怎样选启用高度。333 params-delay vs set bundled unbundling 在本页 item 2 续；续 [`worked-example-params-delay-notve-vs-bundled.md`](worked-example-params-delay-notve-vs-bundled.md)（不变量 913 item 3）。

## 本页不抄

- 怎样编 `ConsensusParams`、默认 MaxBytes / MaxGas、怎样选启用高度。
- ConsensusParams 生效延迟 bundled。那是不变量 333。
- 本高回了就已经在本高生效。那是不变量 333 item 1 余量 / 911。
- 验证人集合 H+1 / H+2 / H+3。那是不变量 35。
