# 例：看见 FinalizeBlockResponse.consensus_param_updates is not already h-effective interchangeable / not already h1-rotate interchangeable / not already one-field interchangeable

**层次**：实现 / FinalizeBlockResponse.consensus_param_updates not already h-effective / not already h1-rotate / not already one-field 正式三事（432 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Response / Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「FinalizeBlockResponse.consensus_param_updates not already h-effective / not already h1-rotate / not already one-field 正式三事（432 余量）/ not 1073 fend-notheffect interchangeable / not 432 finrespend-vs-params bundled interchangeable」，不是 Finalize 回包末栏 bundled（432），也不是只改一个字段就只改这一项（319），也不是高度 H 的 validator_updates 已经在 H+1 计票（35）。不要另写怎样写 Finalize 回包末栏。

## 官方三件事

1. **看见 FinalizeBlockResponse.consensus_param_updates 是对 gas、大小和其它共识相关参数的改动 / 看见回了 consensus_param_updates 这份栏 is not already 已经在块 H 生效 interchangeable，也不是已经 Finalize 回包末栏 bundled（432） interchangeable / 1073 fend-notheffect interchangeable / 1074 fend-notapphash interchangeable / 432 finrespend item 2 app_hash interchangeable，也不是已经 FinalizeBlockResponse.consensus_param_updates not already h-effective / not already h1-rotate / not already one-field 正式三事 bundled（432 item 1 余量） interchangeable / 432 finrespend item 1 interchangeable。**  
   官方写：consensus_param_updates 是 Changes to gas, size, and other consensus-related parameters。Deterministic 列是 Yes。Usage 也写：块 H 返回的 consensus_param_updates 用于块 H+1 的共识参数。看见回了改动，不是已经在块 H 就用新 MaxBytes / MaxGas 验这块 interchangeable——本页从 432 item 1 侧钉 not already h-effective 单句。432 finrespend vs params bundled unbundling 在本页 item 1 启动。

2. **看见能指 H+1 / 看见回了 consensus_param_updates / 这份栏 is not already 已经在 H+1 换人 interchangeable，也不是已经 Finalize 回包末栏 bundled（432） interchangeable / 1073 fend-notheffect interchangeable / 432 finrespend item 3 delay interchangeable / 1075 fend-nottimeout interchangeable，也不是已经高度 H 的 validator_updates 已经在 H+1 计票 interchangeable / 35 validatorupdate interchangeable。**  
   官方把能指 H+1 和已经在 H+1 换人分开。看见能指 H+1，不是已经在 H+1 换人 interchangeable。本页钉 not already h1-rotate 单句。

3. **看见有 ConsensusParams / 看见回了 consensus_param_updates / 这份栏 is not already 已经只改这一项 interchangeable，也不是已经 Finalize 回包末栏 bundled（432） interchangeable / 1073 fend-notheffect interchangeable / 1074 fend-notapphash interchangeable，也不是已经只改一个字段就只改这一项 interchangeable / 319 consensusparams interchangeable。**  
   官方把有 ConsensusParams 和已经只改这一项分开。看见有 ConsensusParams，不是已经只改这一项 interchangeable。432 finrespend vs params bundled unbundling 在本页 item 1 启动。

怎样写 Finalize 回包末栏、怎样编 ConsensusParams、怎样填 next_block_delay 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **FinalizeBlockResponse.consensus_param_updates not already h-effective ≠ 已经在块 H 生效 interchangeable：** 官方把 H→H+1 的参数线和块 H 的执行分开。
- **看见能指 H+1 not already h1-rotate ≠ 已经在 H+1 换人 interchangeable：** 官方把能指 H+1 和已经在 H+1 换人分开。
- **看见有 ConsensusParams not already one-field ≠ 已经只改这一项 interchangeable：** 官方把有 ConsensusParams 和已经只改这一项分开；432 finrespend vs params bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| FinalizeBlockResponse.consensus_param_updates 是对 gas、大小和其它共识相关参数的改动 | 不是已经在块 H 生效 | 不是只改一个字段就只改这一项（319） |
| 看见能指 H+1 | 不是已经在 H+1 换人 | 不是高度 H 的 validator_updates 已经在 H+1 计票（35） |
| 看见有 ConsensusParams | 不是已经只改这一项 | 不是 app_hash 就已经写进下一块头（1074） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse.consensus_param_updates not already h-effective / not already h1-rotate / not already one-field 正式三事（432 余量），必须分开是不是已经在块 H 生效、是不是已经在 H+1 换人、是不是已经只改这一项。可以跳过「看见回了 Finalize 回包末栏就已经在块 H 生效」。不要另写怎样写 Finalize 回包末栏。432 finrespend vs params bundled unbundling 在本页 item 1 启动；续 [`worked-example-fend-notapphash-vs-bundled.md`](worked-example-fend-notapphash-vs-bundled.md)（不变量 1074 item 2）。

## 本页不抄

- 怎样写 Finalize 回包末栏、怎样编 ConsensusParams、怎样填 next_block_delay。
- Finalize 回包末栏 bundled。那是不变量 432。
- 只改一个字段就只改这一项。那是不变量 319。
- 高度 H 的 validator_updates 已经在 H+1 计票。那是不变量 35。
