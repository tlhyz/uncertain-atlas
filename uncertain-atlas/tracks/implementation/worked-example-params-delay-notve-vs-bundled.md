# 例：看见参数更新写了 H+1 is not already VE enable-height switch interchangeable / not already only that field interchangeable / not already settled interchangeable

**层次**：实现 / 参数更新写了 H+1 not already VE enable-height switch / not already only that field / not already settled 正式三事（333 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Updating Consensus Parameters / `FinalizeBlock`, `PrepareProposal`/`ProcessProposal`。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「参数更新写了 H+1 not already VE enable-height switch / not already only that field / not already settled 正式三事（333 余量）/ not 913 params-delay-notve interchangeable / not 333 params-delay-vs-set bundled interchangeable」，不是 ConsensusParams 生效延迟 bundled（333），也不是到了 H 已经 Prepare 带了扩展（330），也不是只填一项就已经只改这一项（319/910）。不要另写怎样编 ConsensusParams 或怎样选启用高度。

## 官方三件事

1. **看见参数更新写了 H+1 / 看见 H+1 已经按新参数 这份 H+1 is not already 已经是扩展启用高度那种 H / H+1 Prepare 切换 interchangeable，也不是已经 ConsensusParams 生效延迟 bundled（333） interchangeable / 913 params-delay-notve interchangeable / 911 params-delay-noteffective interchangeable / 333 params-delay item 1 本高 interchangeable，也不是已经参数更新写了 H+1 not already VE enable-height switch / not already only that field / not already settled 正式三事 bundled（333 item 3 余量） interchangeable / 333 params-delay item 3 interchangeable。**  
   官方把参数生效写成 H 回了就对 H+1 立刻生效。这不是到了 H 才开始叫 ExtendVote、到 H+1 才 Prepare 带扩展。看见写了 H+1，不是已经切到 ABCI 2.0 interchangeable——本页从 333 item 3 侧钉 not already VE enable-height switch 单句。333 params-delay vs set bundled unbundling 在本页 item 3 完成。

2. **看见立刻生效 / 看见写了 H+1 / 这份 H+1 is not already 已经只改填的那一项 interchangeable，也不是已经 ConsensusParams 生效延迟 bundled（333） interchangeable / 913 params-delay-notve interchangeable / 333 params-delay item 2 集合 interchangeable / 912 params-delay-notvalset interchangeable，也不是已经只填一项就已经只改这一项 interchangeable / 319 / 910 consensusparams-notpartial interchangeable。**  
   官方把立刻生效和已经保持没填的字段 / 已经只改填的那一项分开——333 bundled 第三件事常与 319 混成「看见写了 H+1 就已经切扩展或已经只改一项 interchangeable」，本页钉 not already only that field 单句。

3. **看见写了 H+1 / 看见立刻生效 / 这份 H+1 is not already 已经交差 interchangeable，也不是已经 ConsensusParams 生效延迟 bundled（333） interchangeable / 913 params-delay-notve interchangeable / 911 params-delay-noteffective interchangeable，也不是已经到了 H 已经 Prepare 带了扩展 interchangeable / 330 ve-height interchangeable。**  
   官方把写了 H+1 和已经交差 / 已经切到 ABCI 2.0 分开。看见写了 H+1，不是已经交差 interchangeable。333 params-delay vs set bundled unbundling 在本页 item 3 完成。

怎样编 `ConsensusParams`、默认 MaxBytes / MaxGas、怎样选启用高度是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **参数更新写了 H+1 not already VE enable-height switch ≠ 已经是扩展启用高度那种切换 interchangeable：** 官方把参数生效和扩展启用高度分开。
- **看见立刻生效 not already only that field ≠ 已经只改填的那一项 interchangeable：** 官方把立刻生效和只填一项 / 空 / 没回分开。
- **看见写了 H+1 not already settled ≠ 已经交差 interchangeable：** 官方把写了 H+1 和已经交差分开；333 params-delay vs set bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 参数更新写了 H+1 | 不是已经是扩展启用高度那种切换 | 不是到了 H 已经 Prepare 带了扩展（330） |
| 看见立刻生效 | 不是已经只改填的那一项 | 不是只填一项就已经只改这一项（319/910） |
| 看见写了 H+1 | 不是已经交差 | 不是本高回了就已经在本高生效（911） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看参数更新写了 H+1 not already VE enable-height switch / not already only that field / not already settled 正式三事（333 余量），必须分开是不是已经是扩展启用高度那种切换、是不是已经只改填的那一项、是不是已经交差。可以跳过「看见写了 H+1 就已经切到扩展启用高度」。不要另写怎样编 ConsensusParams 或怎样选启用高度。333 params-delay vs set bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样编 `ConsensusParams`、默认 MaxBytes / MaxGas、怎样选启用高度。
- ConsensusParams 生效延迟 bundled。那是不变量 333。
- 本高回了就已经在本高生效。那是不变量 333 item 1 余量 / 911。
- 到了 H 已经 Prepare 带了扩展。那是不变量 330。
- 只填一项就已经只改这一项。那是不变量 319 / 910。
