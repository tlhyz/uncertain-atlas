# 例：看见回了空 / 没回参数 / 能设初始参数 is not already already no params interchangeable / already deleted genesis params interchangeable / already app empty params interchangeable

**层次**：实现 / InitChain 空参数不是已经没有参数 not already no params / not already deleted genesis params / not already app empty params 正式三事（319 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Updating Consensus Parameters。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「InitChain 空参数不是已经没有参数 not already no params / not already deleted genesis params / not already app empty params 正式三事（319 余量）/ not 716 consensusparams-notempty interchangeable / not 319 consensusparams bundled interchangeable」，不是 ConsensusParams vs update bundled（319），也不是 Finalize 没回不是已经清掉（717 item 2 余量）或只改一个字段不是已经只改这一项（718 item 3 余量）。不要另写怎样编 `ConsensusParams` 或怎样选上限。

## 官方三件事

规范把 Requirements 里 `InitChainResponse` 带一份 `ConsensusParams`、若是 `nil` 则 CometBFT **用创世文件里的参数**、若不空则用回包这份 和「已经是回了空就已经没有参数 interchangeable / 已经是没回就已经删掉创世参数 interchangeable / 已经是能设初始参数就已经用了应用自己的空参数 interchangeable / 已经是 ConsensusParams vs update bundled interchangeable」分开写成三件独立的实现事，不是「看见 InitChain 回了空 ConsensusParams 就已经没有参数 interchangeable / 就已经删掉创世参数 interchangeable / 就已经和 InitChain 空验证者名单同一句 interchangeable」一件事：

1. **看见回了空 / 看见 InitChain 回了空 ConsensusParams / 看见参数空 is not already 已经没有参数 interchangeable / 已经 no params interchangeable / 已经空参数交差 interchangeable / 319 consensusparams bundled interchangeable / 33 four gates interchangeable / consensusparams-sold-as-updated interchangeable，也不是已经 ConsensusParams vs update bundled（319） interchangeable / 716 consensusparams-notempty interchangeable / 319 consensusparams item 1 interchangeable，也不是已经 InitChain 空参数不是已经没有参数 not already no params / not already deleted genesis params / not already app empty params 正式三事 bundled（319 item 1 余量） interchangeable / 319 consensusparams item 1 interchangeable，也不是已经 Finalize 没回不是已经清掉（717） interchangeable / 718 consensusparams-notpartial interchangeable / 318 validatorupdate interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：若是 `nil`，CometBFT **用创世文件里的参数**。看见回了空，不是已经没有参数 interchangeable——319 钉 bundled 三事，本页从 item 1 侧钉 not already no params 单句。看见 InitChain 回了空 ConsensusParams，不是已经 ConsensusParams vs update bundled（319） interchangeable——319 钉 bundled，本页钉 item 1 第一件事。看见参数空，不是已经 Finalize 没回不是已经清掉（717） interchangeable——717 另钉 item 2，本页钉 item 1 第一件事。319 consensusparams vs update bundled unbundling 在本页 item 1 启动。

2. **看见没回参数 / 看见没回 ConsensusParams / 看见 InitChain 没回参数 is not already 已经删掉创世参数 interchangeable / 已经 deleted genesis params interchangeable / 已经清掉创世参数 interchangeable / 319 consensusparams bundled interchangeable / 303 genesis validators interchangeable，也不是已经 ConsensusParams vs update bundled（319） interchangeable / 716 consensusparams-notempty interchangeable / 319 consensusparams item 2 Finalize interchangeable / 319 consensusparams item 3 partial interchangeable，也不是已经 InitChain 空参数不是已经没有参数 not already no params / not already deleted genesis params / not already app empty params 正式三事 bundled（319 item 1 余量） interchangeable / 319 consensusparams item 1 interchangeable，也不是已经没有参数（本页第一件事） interchangeable。**  
   官方把回空改用创世参数和已经删掉创世参数路径分开——没回参数，不等于已经删掉创世参数。看见没回参数，不是已经删掉创世参数 interchangeable——本页钉 not already deleted genesis params 单句。看见没回 ConsensusParams，不是已经只改一个字段不是已经只改这一项（718） interchangeable——718 另钉 item 3，本页钉 item 1 第二件事。看见 InitChain 没回参数，不是已经 InitChain 空名单不是已经没有集合（318 / 713） interchangeable——318 另钉验证者侧，本页钉 item 1 第二件事。319 consensusparams vs update bundled unbundling 在本页 item 1 启动。

3. **看见能设初始参数 / 看见 InitChain 能设参数 / 看见应用可设参数 is not already 已经用了应用自己的空参数 interchangeable / 已经 app empty params interchangeable / 已经和 InitChain 空验证者名单同一句 interchangeable / 319 consensusparams bundled interchangeable / 318 validatorupdate interchangeable / 713 validatorupdate-notempty interchangeable，也不是已经 ConsensusParams vs update bundled（319） interchangeable / 716 consensusparams-notempty interchangeable / 319 consensusparams item 2 / 319 consensusparams item 3，也不是已经 InitChain 空参数不是已经没有参数 not already no params / not already deleted genesis params / not already app empty params 正式三事 bundled（319 item 1 余量） interchangeable / 319 consensusparams item 1 interchangeable，也不是已经没有参数（本页第一件事） interchangeable / 已经删掉创世参数（本页第二件事） interchangeable。**  
   官方把能设初始参数和已经用了应用自己的空参数 / 已经和 InitChain 空验证者名单同一句路径分开——能设，不等于已经空参数交差。看见能设初始参数，不是已经 app empty params interchangeable——本页钉 not already app empty params 单句。看见 InitChain 能设参数，不是已经没有参数（本页第一件事） interchangeable——三件事分开钉。看见应用可设参数，不是已经 InitChain 空名单不是已经没有集合（713） interchangeable——713 另钉验证者空名单。319 consensusparams vs update bundled unbundling 在本页 item 1 完成。

怎样编 `ConsensusParams`、怎样选 MaxBytes / MaxGas、公钥类型表是规范里的取值或做法，本页不抄。ConsensusParams vs update bundled（319）、Finalize 没回不是已经清掉（319 item 2 余量 / 717）、只改一个字段不是已经只改这一项（319 item 3 余量 / 718）、InitChain 空验证者名单（318 / 713）、H 更新生效（35）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **回了空 not already no params ≠ 319 / 33 interchangeable：** 官方把改用创世参数单句和已经没有参数路径分开。
- **没回参数 not already deleted genesis params ≠ 已经删掉创世参数 interchangeable：** 官方把回空改用创世单句和已经删掉创世路径分开。
- **能设初始参数 not already app empty params ≠ 已经和 InitChain 空验证者名单同一句 interchangeable：** 官方把可设参数单句和已经空参数交差路径分开；319 consensusparams vs update bundled unbundling 在本页 item 1 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 回了空 | 不是 already no params | 不是 Finalize 没回 alone（717） |
| 没回参数 | 不是 already deleted genesis params | 不是只改一项 alone（718） |
| 能设初始参数 | 不是 already app empty params | 不是 InitChain 空名单 alone（318 / 713） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain 空参数不是已经没有参数 not already no params / not already deleted genesis params / not already app empty params 正式三事（319 余量），必须分开回了空 是不是 already no params interchangeable / 319 consensusparams bundled interchangeable / consensusparams-sold-as-updated interchangeable、没回参数 是不是 already deleted genesis params interchangeable、能设初始参数 是不是 already app empty params interchangeable。可以跳过「看见回了空就已经没有参数 interchangeable / 就已经删掉创世参数 interchangeable / 就已经和 InitChain 空验证者名单同一句 interchangeable」。不要另写怎样编参数。319 consensusparams vs update bundled unbundling 在本页 item 1 完成；续 [`worked-example-consensusparams-notclear-vs-bundled.md`](worked-example-consensusparams-notclear-vs-bundled.md)（不变量 717 item 2，待写）。

## 本页不抄

- 怎样编 `ConsensusParams`、怎样选 MaxBytes / MaxGas、公钥类型表。
- ConsensusParams vs update bundled。那是不变量 319。
- Finalize 没回不是已经清掉。那是不变量 319 item 2 余量 / 717。
- 只改一个字段不是已经只改这一项。那是不变量 319 item 3 余量 / 718。
- InitChain 空名单不是已经没有集合。那是不变量 318 / 713。
- H+1 生效。那是不变量 35。
- 四门已经结算。那是不变量 33。
