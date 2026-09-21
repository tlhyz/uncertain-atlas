# 例：看见参数更新写了 H+1 / 看见立刻生效 / 看见写了 H+1 就当成切换 is not already already ve-height-switch interchangeable / already only-filled-field interchangeable / already abci20 interchangeable

**层次**：实现 / 参数更新写了 H+1 不是已经是扩展启用高度那种切换 not already ve-height-switch / not already only-filled-field / not already abci20 正式三事（333 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Updating Consensus Parameters / `FinalizeBlock`, `PrepareProposal`/`ProcessProposal`。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「参数更新写了 H+1 不是已经是扩展启用高度那种切换 not already ve-height-switch / not already only-filled-field / not already abci20 正式三事（333 余量）/ not 757 paramsdelay-notveheight interchangeable / not 333 paramsdelay bundled interchangeable」，不是 ConsensusParams 生效延迟 bundled（333），也不是本高回了 ConsensusParams 不是已经在本高生效（755 item 1 余量）或 H+1 立刻用了新参数不是已经是验证人集合那种 H+2 才计票（756 item 2 余量）。不要另写怎样编 `ConsensusParams` 或怎样选启用高度。

## 官方三件事

规范把 Requirements 里参数生效写成 H 回了就对 H+1 立刻生效 和「已经是参数更新写了 H+1 就已经是扩展启用高度那种切换 interchangeable / 已经是立刻生效就已经只改填的那一项 interchangeable / 已经是写了 H+1 就已经切到 ABCI 2.0 interchangeable / 已经是 paramsdelay bundled interchangeable」分开写成三件独立的实现事，不是「看见参数更新写了 H+1 就已经是扩展启用高度切换 interchangeable / 就已经只改填的那一项 interchangeable / 就已经切到 ABCI 2.0 interchangeable」一件事：

1. **看见参数更新写了 H+1 / 看见 H+1 已经按新参数 / 看见参数生效写成 H+1 is not already 已经是扩展启用高度那种 H / H+1 Prepare 切换 interchangeable / 已经 ve-height-switch interchangeable / 已经扩展启用切换交差 interchangeable / 333 paramsdelay bundled interchangeable / 33 four gates interchangeable / paramsdelay-sold-as-validatordelay interchangeable，也不是已经 ConsensusParams 生效延迟 bundled（333） interchangeable / 757 paramsdelay-notveheight interchangeable / 333 paramsdelay item 3 interchangeable，也不是已经参数更新写了 H+1 不是已经是扩展启用高度那种切换 not already ve-height-switch / not already only-filled-field / not already abci20 正式三事 bundled（333 item 3 余量） interchangeable / 333 paramsdelay item 3 interchangeable，也不是已经本高回了不是已经在本高生效（755） interchangeable / 756 paramsdelay-notvalidatorh2 interchangeable / 330 veheight interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方把参数生效写成 H 回了就对 H+1 立刻生效。这不是到了 H 才开始叫 `ExtendVote`、到 H+1 才 Prepare 带扩展。看见参数更新写了 H+1，不是已经 ve-height-switch interchangeable——333 钉 bundled 三事，本页从 item 3 侧钉 not already ve-height-switch 单句。看见 H+1 已经按新参数，不是已经 ConsensusParams 生效延迟 bundled（333） interchangeable——333 钉 bundled，本页钉 item 3 第一件事。看见参数生效写成 H+1，不是已经到了 H 已经 Prepare 带了扩展（330） interchangeable——330 另钉。333 paramsdelay vs set bundled unbundling 在本页 item 3 完成。

2. **看见立刻生效 / 看见不是 Finalize 没回就清掉 / 看见不是只填一个字段就只改这一项 is not already 已经只改填的那一项 interchangeable / 已经 only-filled-field interchangeable / 已经保持没填的字段交差 interchangeable / 333 paramsdelay bundled interchangeable / 319 consensusparams interchangeable，也不是已经 ConsensusParams 生效延迟 bundled（333） interchangeable / 757 paramsdelay-notveheight interchangeable / 333 paramsdelay item 1 本高回了 interchangeable / 333 paramsdelay item 2 验证人 H+2 interchangeable，也不是已经参数更新写了 H+1 不是已经是扩展启用高度那种切换 not already ve-height-switch / not already only-filled-field / not already abci20 正式三事 bundled（333 item 3 余量） interchangeable / 333 paramsdelay item 3 interchangeable，也不是已经是扩展启用高度那种切换（本页第一件事） interchangeable。**  
   官方写：也不是 Finalize 没回就清掉、只填一个字段就只改这一项。看见立刻生效，不是已经 only-filled-field interchangeable——本页钉 not already only-filled-field 单句。看见不是 Finalize 没回就清掉，不是已经 InitChain 空 / Finalize 没回 / 只填一项（319） interchangeable——319 另钉。看见立刻生效，不是已经是扩展启用高度那种切换（本页第一件事） interchangeable——三件事分开钉。333 paramsdelay vs set bundled unbundling 在本页 item 3 完成。

3. **看见写了 H+1 就当成切换 / 看见切到 ABCI 2.0 的联想 / 看见扩展启用那种切换口 is not already 已经切到 ABCI 2.0 interchangeable / 已经 abci20 interchangeable / 已经 ABCI 2.0 切换交差 interchangeable / 333 paramsdelay bundled interchangeable / 330 veheight interchangeable，也不是已经 ConsensusParams 生效延迟 bundled（333） interchangeable / 757 paramsdelay-notveheight interchangeable / 333 paramsdelay item 1 / 333 paramsdelay item 2，也不是已经参数更新写了 H+1 不是已经是扩展启用高度那种切换 not already ve-height-switch / not already only-filled-field / not already abci20 正式三事 bundled（333 item 3 余量） interchangeable / 333 paramsdelay item 3 interchangeable，也不是已经是扩展启用高度那种切换（本页第一件事） interchangeable / 已经只改填的那一项（本页第二件事） interchangeable。**  
   官方写：看见写了 H+1，不是已经切到 ABCI 2.0。看见切到 ABCI 2.0 的联想，不是已经 abci20 interchangeable——本页钉 not already abci20 单句。看见扩展启用那种切换口，不是已经到了 H 已经 Prepare 带了扩展（330） interchangeable——330 另钉。看见写了 H+1 就当成切换，不是已经只改填的那一项（本页第二件事） interchangeable——三件事分开钉。333 paramsdelay vs set bundled unbundling 在本页 item 3 完成。

怎样编 `ConsensusParams`、默认 MaxBytes / MaxGas、怎样选启用高度是规范里的取值或做法，本页不抄。ConsensusParams 生效延迟 bundled（333）、本高回了 ConsensusParams 不是已经在本高生效（333 item 1 余量 / 755）、H+1 立刻用了新参数不是已经是验证人集合那种 H+2 才计票（333 item 2 余量 / 756）、InitChain 空 / Finalize 没回 / 只填一项（319）、到了 H 已经 Prepare 带了扩展（330）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **参数更新写了 H+1 not already ve-height-switch ≠ 333 / 33 interchangeable：** 官方把参数生效和扩展启用高度切换分开。
- **立刻生效 not already only-filled-field ≠ 已经只改填的那一项 interchangeable：** 官方把参数立刻对 H+1 和空/没回/只填一项分开。
- **写了 H+1 就当成切换 not already abci20 ≠ 已经切到 ABCI 2.0 interchangeable：** 官方把参数写了 H+1 和已经切到 ABCI 2.0 分开；333 paramsdelay vs set bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 参数更新写了 H+1 | 不是 already ve-height-switch | 不是到了 H 已经 Prepare 带扩展 alone（330） |
| 立刻生效 | 不是 already only-filled-field | 不是空/没回/只填一项 alone（319） |
| 写了 H+1 就当成切换 | 不是 already abci20 | 不是本高回了 alone（755） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看参数更新写了 H+1 不是已经是扩展启用高度那种切换 not already ve-height-switch / not already only-filled-field / not already abci20 正式三事（333 余量），必须分开参数更新写了 H+1 是不是 already ve-height-switch interchangeable / 333 paramsdelay bundled interchangeable / paramsdelay-sold-as-validatordelay interchangeable、立刻生效 是不是 already only-filled-field interchangeable、写了 H+1 就当成切换 是不是 already abci20 interchangeable。可以跳过「看见参数更新写了 H+1 就已经是扩展启用高度切换 interchangeable / 就已经只改填的那一项 interchangeable / 就已经切到 ABCI 2.0 interchangeable」。不要另写怎样编 `ConsensusParams`。333 paramsdelay vs set bundled unbundling 在本页 item 3 完成（755 + 756 + 757）。

## 本页不抄

- 怎样编 `ConsensusParams`、默认 MaxBytes / MaxGas、怎样选启用高度。
- ConsensusParams 生效延迟 bundled。那是不变量 333。
- 本高回了 ConsensusParams 不是已经在本高生效。那是不变量 333 item 1 余量 / 755。
- H+1 立刻用了新参数不是已经是验证人集合那种 H+2 才计票。那是不变量 333 item 2 余量 / 756。
- InitChain 空参数已经没有参数、Finalize 没回已经清掉、只填一项已经只改这一项。那是不变量 319。
- 到了 H 已经 Prepare 带了扩展、H+1 带了扩展已经是本高度刚签的。那是不变量 330。
- 四门已经结算。那是不变量 33。
