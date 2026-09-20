# 例：看见本高回了 ConsensusParams / 看见本高 Finalize 绿了 / 看见能更新 is not already already in-effect-at-h interchangeable / already prepare-new-at-h interchangeable / already tied-to-finalize interchangeable

**层次**：实现 / 本高回了 ConsensusParams 不是已经在本高生效 not already in-effect-at-h / not already prepare-new-at-h / not already tied-to-finalize 正式三事（333 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Updating Consensus Parameters / `FinalizeBlock`, `PrepareProposal`/`ProcessProposal`。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「本高回了 ConsensusParams 不是已经在本高生效 not already in-effect-at-h / not already prepare-new-at-h / not already tied-to-finalize 正式三事（333 余量）/ not 755 paramsdelay-noth interchangeable / not 333 paramsdelay bundled interchangeable」，不是 ConsensusParams 生效延迟 bundled（333），也不是 H+1 立刻用了新参数不是已经是验证人集合那种 H+2 才计票（756 item 2 余量）或参数更新写了 H+1 不是已经是扩展启用高度那种切换（757 item 3 余量）。不要另写怎样编 `ConsensusParams` 或怎样选启用高度。

## 官方三件事

规范把 Requirements 里块 H 回的更新立刻对块 H+1 生效 和「已经是本高回了就已经在本高生效 interchangeable / 已经是本高 Finalize 绿了就已经本高提议按新参数 interchangeable / 已经是能更新就已经和本高交差同一句 interchangeable / 已经是 paramsdelay bundled interchangeable」分开写成三件独立的实现事，不是「看见本高回了 ConsensusParams 就已经在本高生效 interchangeable / 就已经本高提议按新参数 interchangeable / 就已经和本高交差同一句 interchangeable」一件事：

1. **看见本高 FinalizeBlock 回了 ConsensusParams / 看见本高回了参数 / 看见回了 ConsensusParams is not already 已经在本高生效 interchangeable / 已经 in-effect-at-h interchangeable / 已经本高用上交差 interchangeable / 333 paramsdelay bundled interchangeable / 33 four gates interchangeable / paramsdelay-sold-as-validatordelay interchangeable，也不是已经 ConsensusParams 生效延迟 bundled（333） interchangeable / 755 paramsdelay-noth interchangeable / 333 paramsdelay item 1 interchangeable，也不是已经本高回了 ConsensusParams 不是已经在本高生效 not already in-effect-at-h / not already prepare-new-at-h / not already tied-to-finalize 正式三事 bundled（333 item 1 余量） interchangeable / 333 paramsdelay item 1 interchangeable，也不是已经 H+1 立刻用了新参数不是已经是验证人集合那种 H+2（756） interchangeable / 757 paramsdelay-notveheight interchangeable / 319 consensusparams interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：块 **H** 回的更新，**立刻**对块 **H+1** 生效。看见本高回了参数，不是已经 in-effect-at-h interchangeable——333 钉 bundled 三事，本页从 item 1 侧钉 not already in-effect-at-h 单句。看见本高 FinalizeBlock 回了 ConsensusParams，不是已经 ConsensusParams 生效延迟 bundled（333） interchangeable——333 钉 bundled，本页钉 item 1 第一件事。看见回了 ConsensusParams，不是已经 InitChain 空 / Finalize 没回 / 只填一项（319） interchangeable——319 另钉。333 paramsdelay vs set bundled unbundling 在本页 item 1 启动。

2. **看见本高 Finalize 绿了 / 看见本高已经交差 / 看见本高 Finalize 过了 is not already 已经本高提议按新参数 interchangeable / 已经 prepare-new-at-h interchangeable / 已经本高 Prepare 按新上限交差 interchangeable / 333 paramsdelay bundled interchangeable / 319 consensusparams interchangeable，也不是已经 ConsensusParams 生效延迟 bundled（333） interchangeable / 755 paramsdelay-noth interchangeable / 333 paramsdelay item 2 验证人 H+2 interchangeable / 333 paramsdelay item 3 扩展启用 interchangeable，也不是已经本高回了 ConsensusParams 不是已经在本高生效 not already in-effect-at-h / not already prepare-new-at-h / not already tied-to-finalize 正式三事 bundled（333 item 1 余量） interchangeable / 333 paramsdelay item 1 interchangeable，也不是已经在本高生效（本页第一件事） interchangeable。**  
   官方写：看见本高 Finalize 绿了，不是本高 `PrepareProposal` / `ProcessProposal` 已经按新参数。看见本高已经交差，不是已经 prepare-new-at-h interchangeable——本页钉 not already prepare-new-at-h 单句。看见本高 Finalize 过了，不是已经在本高生效（本页第一件事） interchangeable——三件事分开钉。333 paramsdelay vs set bundled unbundling 在本页 item 1 启动。

3. **看见能更新 / 看见本高能回参数 / 看见参数更新口开了 is not already 已经和本高交差同一句 interchangeable / 已经 tied-to-finalize interchangeable / 已经本高交差同一句交差 interchangeable / 333 paramsdelay bundled interchangeable / 33 four gates interchangeable，也不是已经 ConsensusParams 生效延迟 bundled（333） interchangeable / 755 paramsdelay-noth interchangeable / 333 paramsdelay item 2 / 333 paramsdelay item 3，也不是已经本高回了 ConsensusParams 不是已经在本高生效 not already in-effect-at-h / not already prepare-new-at-h / not already tied-to-finalize 正式三事 bundled（333 item 1 余量） interchangeable / 333 paramsdelay item 1 interchangeable，也不是已经在本高生效（本页第一件事） interchangeable / 已经本高提议按新参数（本页第二件事） interchangeable。**  
   官方写：看见能更新，不是已经和本高交差同一句。看见本高能回参数，不是已经 tied-to-finalize interchangeable——本页钉 not already tied-to-finalize 单句。看见参数更新口开了，不是已经四门已经结算（33） interchangeable——33 另钉。看见能更新，不是已经本高提议按新参数（本页第二件事） interchangeable——三件事分开钉。333 paramsdelay vs set bundled unbundling 在本页 item 1 启动。

怎样编 `ConsensusParams`、默认 MaxBytes / MaxGas、怎样选启用高度是规范里的取值或做法，本页不抄。ConsensusParams 生效延迟 bundled（333）、H+1 立刻用了新参数不是已经是验证人集合那种 H+2 才计票（333 item 2 余量 / 756）、参数更新写了 H+1 不是已经是扩展启用高度那种切换（333 item 3 余量 / 757）、InitChain 空 / Finalize 没回 / 只填一项（319）、验证人集合 H+1 / H+2 / H+3（35）、到了 H 已经 Prepare 带了扩展（330）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **本高回了 not already in-effect-at-h ≠ 333 / 33 interchangeable：** 官方把 H 回参数和 H+1 才用分开。
- **本高 Finalize 绿了 not already prepare-new-at-h ≠ 已经本高提议按新参数 interchangeable：** 官方把本高交差和本高提议已经按新上限分开。
- **能更新 not already tied-to-finalize ≠ 已经和本高交差同一句 interchangeable：** 官方把能更新和已经与本高交差同一句分开；333 paramsdelay vs set bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 本高回了参数 | 不是 already in-effect-at-h | 不是 InitChain 空 / 没回 / 只填一项 alone（319） |
| 本高 Finalize 绿了 | 不是 already prepare-new-at-h | 不是验证人 H+2 alone（35） |
| 能更新 | 不是 already tied-to-finalize | 不是四门已经结算 alone（33） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看本高回了 ConsensusParams 不是已经在本高生效 not already in-effect-at-h / not already prepare-new-at-h / not already tied-to-finalize 正式三事（333 余量），必须分开本高回了参数 是不是 already in-effect-at-h interchangeable / 333 paramsdelay bundled interchangeable / paramsdelay-sold-as-validatordelay interchangeable、本高 Finalize 绿了 是不是 already prepare-new-at-h interchangeable、能更新 是不是 already tied-to-finalize interchangeable。可以跳过「看见本高回了就已经在本高生效 interchangeable / 就已经本高提议按新参数 interchangeable / 就已经和本高交差同一句 interchangeable」。不要另写怎样编 `ConsensusParams`。333 paramsdelay vs set bundled unbundling 在本页 item 1 启动；续 [`worked-example-paramsdelay-notvalidatorh2-vs-bundled.md`](worked-example-paramsdelay-notvalidatorh2-vs-bundled.md)（不变量 756 item 2）。

## 本页不抄

- 怎样编 `ConsensusParams`、默认 MaxBytes / MaxGas、怎样选启用高度。
- ConsensusParams 生效延迟 bundled。那是不变量 333。
- H+1 立刻用了新参数不是已经是验证人集合那种 H+2 才计票。那是不变量 333 item 2 余量 / 756。
- 参数更新写了 H+1 不是已经是扩展启用高度那种切换。那是不变量 333 item 3 余量 / 757。
- InitChain 空参数已经没有参数、Finalize 没回已经清掉、只填一项已经只改这一项。那是不变量 319。
- 验证人集合 H+1 / H+2 / H+3。那是不变量 35。
- 到了 H 已经 Prepare 带了扩展。那是不变量 330。
- 四门已经结算。那是不变量 33。
