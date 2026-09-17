# 例：看见本高 Finalize 回了 ConsensusParams is not already effective at H interchangeable / not already this-height Prepare interchangeable / not already settled interchangeable

**层次**：实现 / 本高回了 ConsensusParams not already effective at H / not already this-height Prepare / not already settled 正式三事（333 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Updating Consensus Parameters / `FinalizeBlock`, `PrepareProposal`/`ProcessProposal`。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「本高回了 ConsensusParams not already effective at H / not already this-height Prepare / not already settled 正式三事（333 余量）/ not 911 params-delay-noteffective interchangeable / not 333 params-delay-vs-set bundled interchangeable」，不是 ConsensusParams 生效延迟 bundled（333），也不是 InitChain 空参数就已经没有参数（319/908），也不是 Finalize 回了 consensus_param_updates 就已经在块 H 生效（471/710）。不要另写怎样编 ConsensusParams 或怎样选启用高度。

## 官方三件事

1. **看见本高 `FinalizeBlock` 回了 `ConsensusParams` / 看见本高已经交差 这份回包 is not already 已经在本高生效 interchangeable，也不是已经 ConsensusParams 生效延迟 bundled（333） interchangeable / 911 params-delay-noteffective interchangeable / 912 params-delay-notvalset interchangeable / 333 params-delay item 2 H+1 interchangeable，也不是已经本高回了 ConsensusParams not already effective at H / not already this-height Prepare / not already settled 正式三事 bundled（333 item 1 余量） interchangeable / 333 params-delay item 1 interchangeable。**  
   官方写：块 H 回的更新，立刻对块 H+1 生效。看见本高回了参数，不是已经在本高用上 interchangeable——本页从 333 item 1 侧钉 not already effective at H 单句。333 params-delay vs set bundled unbundling 在本页 item 1 启动。

2. **看见本高 Finalize 绿了 / 看见能更新 / 这份回包 is not already 已经本高 Prepare / Process 按新参数 interchangeable，也不是已经 ConsensusParams 生效延迟 bundled（333） interchangeable / 911 params-delay-noteffective interchangeable / 333 params-delay item 3 启用高度 interchangeable / 913 params-delay-notve interchangeable，也不是已经 Finalize 回了 consensus_param_updates 就已经在块 H 生效 interchangeable / 471 / 710 fincparam-nothatH interchangeable。**  
   官方把本高 Finalize 绿了和本高提议已经按新上限分开——333 bundled 第一件事常与 471 混成「看见本高回了就已经在本高生效或已经是回包 H→H+1 那句 interchangeable」，本页钉 not already this-height Prepare 单句。

3. **看见能更新 / 看见本高回了 / 这份回包 is not already 已经交差 interchangeable，也不是已经 ConsensusParams 生效延迟 bundled（333） interchangeable / 911 params-delay-noteffective interchangeable / 912 params-delay-notvalset interchangeable，也不是已经 InitChain 空参数就已经没有参数 interchangeable / 319 / 908 consensusparams-notnoparams interchangeable。**  
   官方把能更新和已经和本高交差同一句分开。看见能更新，不是已经交差 interchangeable。333 params-delay vs set bundled unbundling 在本页 item 1 启动。

怎样编 `ConsensusParams`、默认 MaxBytes / MaxGas、怎样选启用高度是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **本高回了 ConsensusParams not already effective at H ≠ 已经在本高生效 interchangeable：** 官方把 H 回参数和 H+1 才用分开。
- **看见本高 Finalize 绿了 not already this-height Prepare ≠ 已经本高提议按新上限 interchangeable：** 官方把本高 Finalize 绿了和本高 Prepare / Process 已经按新参数分开。
- **看见能更新 not already settled ≠ 已经交差 interchangeable：** 官方把能更新和已经交差分开；333 params-delay vs set bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 本高 Finalize 回了 ConsensusParams | 不是已经在本高生效 | 不是 Finalize 回了 consensus_param_updates 就已经在块 H 生效（471/710） |
| 看见本高 Finalize 绿了 | 不是已经本高提议按新上限 | 不是 InitChain 空参数已经没有参数（319/908） |
| 看见能更新 | 不是已经交差 | 不是 H+1 立刻用了就已经是集合 H+2（912） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看本高回了 ConsensusParams not already effective at H / not already this-height Prepare / not already settled 正式三事（333 余量），必须分开是不是已经在本高生效、是不是已经本高提议按新上限、是不是已经交差。可以跳过「看见本高回了就已经在本高生效」。不要把仓库默认 MaxBytes / MaxGas 当不确定默认。不要另写怎样编 ConsensusParams 或怎样选启用高度。333 params-delay vs set bundled unbundling 在本页 item 1 启动；续 [`worked-example-params-delay-notvalset-vs-bundled.md`](worked-example-params-delay-notvalset-vs-bundled.md)（不变量 912 item 2）。

## 本页不抄

- 怎样编 `ConsensusParams`、默认 MaxBytes / MaxGas、怎样选启用高度。
- ConsensusParams 生效延迟 bundled。那是不变量 333。
- H+1 立刻用了就已经是集合 H+2。那是不变量 333 item 2 余量 / 912。
- Finalize 回了 consensus_param_updates 就已经在块 H 生效。那是不变量 471 / 710。
- InitChain 空参数已经没有参数。那是不变量 319 / 908。
