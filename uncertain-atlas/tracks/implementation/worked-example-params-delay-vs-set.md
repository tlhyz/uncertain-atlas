# 例：看见本高 Finalize 回了 ConsensusParams 不是已经在本高生效；看见 H+1 立刻用了新参数不是已经是验证人集合那种 H+2 才计票；看见参数更新写了 H+1 不是已经是扩展启用高度那种切换

**层次**：实现 / ConsensusParams 生效延迟。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Updating Consensus Parameters / `FinalizeBlock`, `PrepareProposal`/`ProcessProposal`。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「本高 Finalize 回了 ConsensusParams 不是已经在本高生效 / H+1 立刻用了新参数不是已经是验证人集合那种 H+2 才计票 / 参数更新写了 H+1 不是已经是扩展启用高度那种切换，也不是已经只改填的那一项」，不是 InitChain 空参数已经没有参数，也不是验证人集合 H+1 / H+2 / H+3。不要另写怎样编 `ConsensusParams` 或怎样选启用高度。

## 官方三件事

规范把共识参数哪一高度生效写成三件独立的实现事，不是「看见本高回了 ConsensusParams 就已经在本高生效、已经是换人那种延迟、已经是扩展启用高度那种切换」一件事：

1. **看见本高 `FinalizeBlock` 回了 `ConsensusParams` / 看见本高已经交差 不是已经在本高生效，也不是本高 `PrepareProposal` / `ProcessProposal` 已经按新参数。**  
   官方写：块 **H** 回的更新，**立刻**对块 **H+1** 生效。看见本高回了参数，不是已经在本高用上。看见本高 Finalize 绿了，不是本高提议已经按新上限。看见能更新，不是已经和本高交差同一句。
2. **看见 H+1 立刻用了新参数 / 看见参数走 H→H+1 不是已经是验证人集合那种 H+2 才计票，也不是已经是 H+3 才带 last_commit。**  
   官方把集合更新写成处理 H 之后只在 **H+2** 生效；参数更新写成 H 回了就对 **H+1** 立刻生效。看见参数已经在 H+1 用上，不是新人已经在 H+1 计票。看见「立刻」，不是已经和 NextValidatorsHash / ValidatorsHash / last_commit 同一张表。看见参数延迟，不是已经是不变量 35 那三条高度。
3. **看见参数更新写了 H+1 / 看见 H+1 已经按新参数 不是已经是扩展启用高度那种 H / H+1 Prepare 切换，也不是已经只改填的那一项。**  
   官方把参数生效写成 H 回了就对 H+1 立刻生效。这不是到了 H 才开始叫 `ExtendVote`、到 H+1 才 Prepare 带扩展。也不是 Finalize 没回就清掉、只填一个字段就只改这一项。看见写了 H+1，不是已经切到 ABCI 2.0。看见立刻生效，不是已经保持没填的字段。

怎样编 `ConsensusParams`、默认 MaxBytes / MaxGas、怎样选启用高度是规范里的取值或做法，本页不抄。InitChain 空 / Finalize 没回 / 只填一项是不变量 319，本页不抄。

## 官方为什么这样拆

- **本高回了 ≠ 已经在本高生效：** 官方把 H 回参数和 H+1 才用分开。
- **H+1 立刻用了新参数 ≠ 已经是验证人集合那种 H+2 才计票：** 官方把参数延迟和集合延迟分开。
- **参数更新写了 H+1 ≠ 已经是扩展启用高度那种切换：** 官方把参数生效和扩展启用高度、空/没回/只填一项分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 本高 Finalize 回了 ConsensusParams | 不是已经在本高生效 | 不是 InitChain 空参数已经没有参数 / Finalize 没回已经清掉 / 只填一项已经只改这一项（319） |
| H+1 立刻用了新参数 | 不是已经是验证人集合那种 H+2 才计票 | 不是验证人集合 H+1 / H+2 / H+3（35） |
| 参数更新写了 H+1 | 不是已经是扩展启用高度那种切换 | 不是到了 H 已经 Prepare 带了扩展（330） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「本高回了 ConsensusParams 就已经在本高生效、已经是换人那种延迟、已经是扩展启用高度那种切换」，必须分开本高回了是不是已经在本高生效、H+1 立刻用了新参数是不是已经是验证人集合那种 H+2 才计票、参数更新写了 H+1 是不是已经是扩展启用高度那种切换。可以跳过「看见本高回了就已经在本高生效」。不要另写怎样编 `ConsensusParams` 或怎样选启用高度。333 params-delay vs set bundled unbundling 完成（911 item 1 / 912 item 2 / 913 item 3）；精读 [`worked-example-params-delay-noteffective-vs-bundled.md`](worked-example-params-delay-noteffective-vs-bundled.md)（不变量 911 item 1）。

## 本页不抄

- 怎样编 `ConsensusParams`、默认 MaxBytes / MaxGas、怎样选启用高度。
- InitChain 空参数已经没有参数、Finalize 没回已经清掉、只填一项已经只改这一项。那是不变量 319。
- 验证人集合 H+1 / H+2 / H+3。那是不变量 35。
- 到了 H 已经 Prepare 带了扩展、H+1 带了扩展已经是本高度刚签的。那是不变量 330。
