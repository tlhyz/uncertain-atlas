# 例：看见 InitChain 回了空 ConsensusParams is not already no params interchangeable / not already app empty params interchangeable / not already settled interchangeable

**层次**：实现 / InitChain 空参数 not already no params / not already app empty params / not already settled 正式三事（319 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Updating Consensus Parameters。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、mempool。本页是「InitChain 空参数 not already no params / not already app empty params / not already settled 正式三事（319 余量）/ not 908 consensusparams-notnoparams interchangeable / not 319 consensusparams-vs-update bundled interchangeable」，不是 ConsensusParams bundled（319），也不是 InitChain 空名单就已经没有集合（318/905），也不是 InitChain 请求 consensus_params 就已经没有参数（388/764）。不要另写怎样编参数或怎样选上限。

## 官方三件事

1. **看见 InitChain 回了空 ConsensusParams / 看见没回参数 这份空参数 is not already 已经没有参数 interchangeable，也不是已经 ConsensusParams bundled（319） interchangeable / 908 consensusparams-notnoparams interchangeable / 909 consensusparams-notcleared interchangeable / 319 consensusparams item 2 Finalize interchangeable，也不是已经 InitChain 空参数 not already no params / not already app empty params / not already settled 正式三事 bundled（319 item 1 余量） interchangeable / 319 consensusparams item 1 interchangeable。**  
   官方写：`InitChainResponse` 带一份 `ConsensusParams`。若是 nil，CometBFT 用创世文件里的参数。看见回了空，不是已经没有参数 interchangeable——本页从 319 item 1 侧钉 not already no params 单句。319 consensusparams vs update bundled unbundling 在本页 item 1 启动。

2. **看见没回 / 看见能设初始参数 / 这份空参数 is not already 已经用了应用自己的空参数 interchangeable，也不是已经 ConsensusParams bundled（319） interchangeable / 908 consensusparams-notnoparams interchangeable / 319 consensusparams item 3 只改一项 interchangeable / 910 consensusparams-notpartial interchangeable，也不是已经 InitChain 空名单就已经没有集合 interchangeable / 318 / 905 validatorupdate-notempty interchangeable。**  
   官方把没回和已经删掉创世参数分开——319 bundled 第一件事常与 318 混成「看见回了空就已经没有参数或已经和空验证者名单同一句 interchangeable」，本页钉 not already app empty params 单句。

3. **看见能设初始参数 / 看见回了空 / 这份空参数 is not already 已经交差 interchangeable，也不是已经 ConsensusParams bundled（319） interchangeable / 908 consensusparams-notnoparams interchangeable / 909 consensusparams-notcleared interchangeable，也不是已经 InitChain 请求 consensus_params 就已经没有参数 interchangeable / 388 / 764 initparams-notnoparams interchangeable。**  
   官方把能设初始参数和已经和 InitChain 空验证者名单同一句 / 已经交差分开。看见能设初始参数，不是已经交差 interchangeable。319 consensusparams vs update bundled unbundling 在本页 item 1 启动。

怎样编 `ConsensusParams`、怎样选 MaxBytes / MaxGas、公钥类型表是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **InitChain 空参数 not already no params ≠ 已经没有参数 interchangeable：** 官方把回空和改用创世参数分开。
- **看见没回 not already app empty params ≠ 已经用了应用自己的空参数 interchangeable：** 官方把没回和已经删掉创世参数分开。
- **看见能设初始参数 not already settled ≠ 已经交差 interchangeable：** 官方把能设初始参数和已经交差分开；319 consensusparams vs update bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| InitChain 回空参数 | 不是已经没有参数 | 不是 InitChain 空验证者名单已经没有集合（318/905） |
| 看见没回 | 不是已经用了应用自己的空参数 | 不是 InitChain 请求 consensus_params 就已经没有参数（388/764） |
| 看见能设初始参数 | 不是已经交差 | 不是 Finalize 没回就已经清掉（909） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain 空参数 not already no params / not already app empty params / not already settled 正式三事（319 余量），必须分开是不是已经没有参数、是不是已经用了应用自己的空参数、是不是已经交差。可以跳过「看见回了就已经改完」。不要把仓库默认 MaxBytes / MaxGas 当不确定默认。不要另写怎样编参数或怎样选上限。319 consensusparams vs update bundled unbundling 在本页 item 1 启动；续 [`worked-example-consensusparams-notcleared-vs-bundled.md`](worked-example-consensusparams-notcleared-vs-bundled.md)（不变量 909 item 2）。

## 本页不抄

- 怎样编 `ConsensusParams`、怎样选 MaxBytes / MaxGas、公钥类型表。
- ConsensusParams bundled。那是不变量 319。
- Finalize 没回就已经清掉。那是不变量 319 item 2 余量 / 909。
- InitChain 空验证者名单已经没有集合。那是不变量 318 / 905。
- InitChain 请求 consensus_params 就已经没有参数。那是不变量 388 / 764。
