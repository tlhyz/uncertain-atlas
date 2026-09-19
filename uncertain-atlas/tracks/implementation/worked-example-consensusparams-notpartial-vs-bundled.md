# 例：看见只填一项 / 看见没写字段 / 看见能整份套上 is not already already only-that interchangeable / already rest-unchanged interchangeable / already field-merge interchangeable

**层次**：实现 / 只改一个字段不是已经只改这一项 not already only-that / not already rest-unchanged / not already field-merge 正式三事（319 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Updating Consensus Parameters。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「只改一个字段不是已经只改这一项 not already only-that / not already rest-unchanged / not already field-merge 正式三事（319 余量）/ not 718 consensusparams-notpartial interchangeable / not 319 consensusparams bundled interchangeable」，不是 ConsensusParams vs update bundled（319），也不是 InitChain 空参数不是已经没有参数（716 item 1 余量）或 Finalize 没回不是已经清掉（717 item 2 余量）。不要另写怎样编 `ConsensusParams` 或怎样选上限。

## 官方三件事

规范把 Requirements 里空的 `ConsensusParams` 会被忽略、每一个**不空**的字段会**整份套上**、例如要改 `Block.MaxBytes` 必须把其余 `Block` 字段（如 `Block.MaxGas`）也写上哪怕没变否则那些字段会被更新成默认 和「已经是只填一项就已经只改这一项 interchangeable / 已经是没写字段就已经保持原值 interchangeable / 已经是能整份套上就已经是按字段合并 interchangeable / 已经是 ConsensusParams vs update bundled interchangeable」分开写成三件独立的实现事，不是「看见只改了其中一个字段就已经只改这一项 interchangeable / 就已经保持其余不变 interchangeable / 就已经是 field-wise merge interchangeable」一件事：

1. **看见只填一项 / 看见 Block 只填了 MaxBytes / 看见只改了其中一个字段 is not already 已经只改这一项 interchangeable / 已经 only-that interchangeable / 已经只改这一项交差 interchangeable / 319 consensusparams bundled interchangeable / 33 four gates interchangeable / consensusparams-sold-as-updated interchangeable，也不是已经 ConsensusParams vs update bundled（319） interchangeable / 718 consensusparams-notpartial interchangeable / 319 consensusparams item 3 interchangeable，也不是已经只改一个字段不是已经只改这一项 not already only-that / not already rest-unchanged / not already field-merge 正式三事 bundled（319 item 3 余量） interchangeable / 319 consensusparams item 3 interchangeable，也不是已经 InitChain 空参数不是已经没有参数（716） interchangeable / 717 consensusparams-notclear interchangeable / 315 maxgas interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：每一个**不空**的字段会**整份套上**。看见只填一项，不是已经只改这一项 interchangeable——319 钉 bundled 三事，本页从 item 3 侧钉 not already only-that 单句。看见 Block 只填了 MaxBytes，不是已经 ConsensusParams vs update bundled（319） interchangeable——319 钉 bundled，本页钉 item 3 第一件事。看见只改了其中一个字段，不是已经 MaxGas 已经在执行（315） interchangeable——315 另钉，本页钉 item 3 第一件事。319 consensusparams vs update bundled unbundling 在本页 item 3 启动。

2. **看见没写字段 / 看见没写的 Block 字段 / 看见其余字段空着 is not already 已经保持原值 interchangeable / 已经 rest-unchanged interchangeable / 已经保持其余不变 interchangeable / 319 consensusparams bundled interchangeable / 299 maxbytes interchangeable，也不是已经 ConsensusParams vs update bundled（319） interchangeable / 718 consensusparams-notpartial interchangeable / 319 consensusparams item 1 InitChain interchangeable / 319 consensusparams item 2 Finalize interchangeable，也不是已经只改一个字段不是已经只改这一项 not already only-that / not already rest-unchanged / not already field-merge 正式三事 bundled（319 item 3 余量） interchangeable / 319 consensusparams item 3 interchangeable，也不是已经只改这一项（本页第一件事） interchangeable。**  
   官方写：否则那些字段会被更新成默认。看见没写字段，不是已经保持原值 interchangeable——本页钉 not already rest-unchanged 单句。看见没写的 Block 字段，不是已经 Finalize 没回不是已经清掉（717） interchangeable——717 另钉 item 2，本页钉 item 3 第二件事。看见其余字段空着，不是已经 MaxBytes 写成 -1 已经没有上限（299） interchangeable——299 另钉，本页钉 item 3 第二件事。319 consensusparams vs update bundled unbundling 在本页 item 3 启动。

3. **看见能整份套上 / 看见不空字段会套上 / 看见空的 ConsensusParams 会被忽略 is not already 已经是按字段合并 interchangeable / 已经 field-merge interchangeable / 已经 field-wise merge interchangeable / 319 consensusparams bundled interchangeable / 717 consensusparams-notclear interchangeable，也不是已经 ConsensusParams vs update bundled（319） interchangeable / 718 consensusparams-notpartial interchangeable / 319 consensusparams item 1 / 319 consensusparams item 2，也不是已经只改一个字段不是已经只改这一项 not already only-that / not already rest-unchanged / not already field-merge 正式三事 bundled（319 item 3 余量） interchangeable / 319 consensusparams item 3 interchangeable，也不是已经只改这一项（本页第一件事） interchangeable / 已经保持原值（本页第二件事） interchangeable。**  
   官方把不空字段整份套上和已经是按字段合并 / 已经和 Finalize nil 什么也不做同一句路径分开——能整份套上，不等于已经 field-merge。看见能整份套上，不是已经 field-merge interchangeable——本页钉 not already field-merge 单句。看见不空字段会套上，不是已经只改这一项（本页第一件事） interchangeable——三件事分开钉。看见空的 ConsensusParams 会被忽略，不是已经 Finalize 没回 not already clear（717） interchangeable——717 另钉 Finalize nil 侧。319 consensusparams vs update bundled unbundling 在本页 item 3 完成。

怎样编 `ConsensusParams`、怎样选 MaxBytes / MaxGas、公钥类型表是规范里的取值或做法，本页不抄。ConsensusParams vs update bundled（319）、InitChain 空参数不是已经没有参数（319 item 1 余量 / 716）、Finalize 没回不是已经清掉（319 item 2 余量 / 717）、H 更新生效（35）、MaxGas（315）、MaxBytes -1（299）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **只填一项 not already only-that ≠ 319 / 33 interchangeable：** 官方把整份套上单句和已经只改这一项路径分开。
- **没写字段 not already rest-unchanged ≠ 已经保持原值 interchangeable：** 官方把未写字段更新成默认单句和已经保持其余不变路径分开。
- **能整份套上 not already field-merge ≠ 已经是按字段合并 interchangeable：** 官方把不空字段整份套上与 field-wise merge / Finalize nil 路径分开；319 consensusparams vs update bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 只填一项 | 不是 already only-that | 不是 MaxGas alone（315） |
| 没写字段 | 不是 already rest-unchanged | 不是 Finalize 没回 alone（717） |
| 能整份套上 | 不是 already field-merge | 不是 Finalize nil 什么也不做 alone（717） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看只改一个字段不是已经只改这一项 not already only-that / not already rest-unchanged / not already field-merge 正式三事（319 余量），必须分开只填一项 是不是 already only-that interchangeable / 319 consensusparams bundled interchangeable / consensusparams-sold-as-updated interchangeable、没写字段 是不是 already rest-unchanged interchangeable、能整份套上 是不是 already field-merge interchangeable。可以跳过「看见只改了其中一个字段就已经只改这一项 interchangeable / 就已经保持其余不变 interchangeable / 就已经是 field-wise merge interchangeable」。不要另写怎样编参数。不要把仓库默认 MaxBytes / MaxGas 当不确定默认。319 consensusparams vs update bundled unbundling 在本页 item 3 完成（716 + 717 + 718）。

## 本页不抄

- 怎样编 `ConsensusParams`、怎样选 MaxBytes / MaxGas、公钥类型表。
- ConsensusParams vs update bundled。那是不变量 319。
- InitChain 空参数不是已经没有参数。那是不变量 319 item 1 余量 / 716。
- Finalize 没回不是已经清掉。那是不变量 319 item 2 余量 / 717。
- H+1 生效。那是不变量 35。
- MaxGas 已经在执行。那是不变量 315。
- MaxBytes 写成 -1。那是不变量 299。
- 四门已经结算。那是不变量 33。
