# 例：看见只改了一个字段 is not already only that field interchangeable / not already rest kept interchangeable / not already settled interchangeable

**层次**：实现 / 只改一个字段 not already only that field / not already rest kept / not already settled 正式三事（319 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Updating Consensus Parameters。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、mempool。本页是「只改一个字段 not already only that field / not already rest kept / not already settled 正式三事（319 余量）/ not 910 consensusparams-notpartial interchangeable / not 319 consensusparams-vs-update bundled interchangeable」，不是 ConsensusParams bundled（319），也不是 MaxGas 已经在执行（315），也不是 Finalize 回了 gas/size 就已经只改一项（471/711）。不要另写怎样编参数或怎样选上限。

## 官方三件事

1. **看见只改了其中一个字段 / 看见 Block 只填了 MaxBytes 这份只填 is not already 已经只改这一项 interchangeable，也不是已经 ConsensusParams bundled（319） interchangeable / 910 consensusparams-notpartial interchangeable / 908 consensusparams-notnoparams interchangeable / 319 consensusparams item 1 InitChain interchangeable，也不是已经只改一个字段 not already only that field / not already rest kept / not already settled 正式三事 bundled（319 item 3 余量） interchangeable / 319 consensusparams item 3 interchangeable。**  
   官方写：空的 ConsensusParams 会被忽略。每一个不空的字段会整份套上。例如要改 Block.MaxBytes，应用必须把其余 Block 字段（如 Block.MaxGas）也写上，哪怕没变；否则那些字段会被更新成默认。看见只填了一项，不是已经只改这一项 interchangeable——本页从 319 item 3 侧钉 not already only that field 单句。319 consensusparams vs update bundled unbundling 在本页 item 3 完成。

2. **看见没写的字段 / 看见只填了一项 / 这份只填 is not already 已经保持其余不变 interchangeable，也不是已经 ConsensusParams bundled（319） interchangeable / 910 consensusparams-notpartial interchangeable / 319 consensusparams item 2 Finalize interchangeable / 909 consensusparams-notcleared interchangeable，也不是已经 MaxGas 已经在执行 interchangeable / 315 maxgas interchangeable。**  
   官方把没写的字段和已经保持原值分开——319 bundled 第三件事常与 471 混成「看见只填一项就已经只改这一项或已经是 gas/size Deterministic Yes 那句 interchangeable」，本页钉 not already rest kept 单句。

3. **看见只填了一项 / 看见没写的字段 / 这份只填 is not already 已经交差 interchangeable，也不是已经 ConsensusParams bundled（319） interchangeable / 910 consensusparams-notpartial interchangeable / 908 consensusparams-notnoparams interchangeable，也不是已经 MaxBytes 写成 -1 已经没有上限 interchangeable / 299 maxbytes-cap interchangeable，也不是已经 Finalize 回了 gas/size 就已经只改一项 interchangeable / 471 / 711 fincparam-notpartial interchangeable。**  
   官方把只填了一项和已经交差分开。看见只填了一项，不是已经交差 interchangeable。319 consensusparams vs update bundled unbundling 在本页 item 3 完成。

怎样编 `ConsensusParams`、怎样选 MaxBytes / MaxGas、公钥类型表是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **只改一个字段 not already only that field ≠ 已经只改这一项 interchangeable：** 官方把不空字段整份套上和其余被写成默认分开。
- **看见没写的字段 not already rest kept ≠ 已经保持其余不变 interchangeable：** 官方把没写的字段和已经保持原值分开。
- **看见只填了一项 not already settled ≠ 已经交差 interchangeable：** 官方把只填了一项和已经交差分开；319 consensusparams vs update bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 只填一个 Block 字段 | 不是已经只改这一项 | 不是 MaxGas 已经在执行（315） |
| 看见没写的字段 | 不是已经保持其余不变 | 不是 Finalize 回了 gas/size 就已经只改一项（471/711） |
| 看见只填了一项 | 不是已经交差 | 不是 MaxBytes 写成 -1 已经没有上限（299） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看只改一个字段 not already only that field / not already rest kept / not already settled 正式三事（319 余量），必须分开是不是已经只改这一项、是不是已经保持其余不变、是不是已经交差。可以跳过「看见只填一项就已经只改这一项」。不要把仓库默认 MaxBytes / MaxGas 当不确定默认。不要另写怎样编参数或怎样选上限。319 consensusparams vs update bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样编 `ConsensusParams`、怎样选 MaxBytes / MaxGas、公钥类型表。
- ConsensusParams bundled。那是不变量 319。
- InitChain 空参数就已经没有参数。那是不变量 319 item 1 余量 / 908。
- MaxGas 已经在执行。那是不变量 315。
- MaxBytes 写成 -1 已经没有上限。那是不变量 299。
- Finalize 回了 gas/size 就已经只改一项。那是不变量 471 / 711。
