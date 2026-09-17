# 例：看见 Finalize 没回 ConsensusParams is not already cleared interchangeable / not already changed interchangeable / not already settled interchangeable

**层次**：实现 / Finalize 没回 not already cleared / not already changed / not already settled 正式三事（319 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Updating Consensus Parameters。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、mempool。本页是「Finalize 没回 not already cleared / not already changed / not already settled 正式三事（319 余量）/ not 909 consensusparams-notcleared interchangeable / not 319 consensusparams-vs-update bundled interchangeable」，不是 ConsensusParams bundled（319），也不是 H 的参数更新已经在 H+1 生效（333），也不是 Finalize 回了 consensus_param_updates 就已经清掉（471/712）。不要另写怎样编参数或怎样选上限。

## 官方三件事

1. **看见 FinalizeBlock 回了空 / 看见没回 ConsensusParams 这份空回 is not already 已经清掉 interchangeable，也不是已经 ConsensusParams bundled（319） interchangeable / 909 consensusparams-notcleared interchangeable / 908 consensusparams-notnoparams interchangeable / 319 consensusparams item 1 InitChain interchangeable，也不是已经 Finalize 没回 not already cleared / not already changed / not already settled 正式三事 bundled（319 item 2 余量） interchangeable / 319 consensusparams item 2 interchangeable。**  
   官方写：`FinalizeBlockResponse` 也收一份 `ConsensusParams`。若是 nil，CometBFT 什么也不做。看见没回，不是已经清成默认 interchangeable——本页从 319 item 2 侧钉 not already cleared 单句。319 consensusparams vs update bundled unbundling 在本页 item 2 续。

2. **看见空着 / 看见没回 / 这份空回 is not already 已经改了 interchangeable，也不是已经 ConsensusParams bundled（319） interchangeable / 909 consensusparams-notcleared interchangeable / 319 consensusparams item 3 只改一项 interchangeable / 910 consensusparams-notpartial interchangeable，也不是已经 H 的参数更新已经在 H+1 生效 interchangeable / 333 params-delay interchangeable。**  
   官方把空着和已经改过分开——319 bundled 第二件事常与 471 混成「看见 Finalize 没回就已经清掉或已经是回包 H→H+1 那句 interchangeable」，本页钉 not already changed 单句。

3. **看见能更新 / 看见没回 / 这份空回 is not already 已经交差 interchangeable，也不是已经 ConsensusParams bundled（319） interchangeable / 909 consensusparams-notcleared interchangeable / 908 consensusparams-notnoparams interchangeable，也不是已经 Finalize 回了 consensus_param_updates 就已经清掉 interchangeable / 471 / 712 fincparam-notcleared interchangeable。**  
   官方把能更新和已经和 InitChain 空回包同一句 / 已经交差分开。看见能更新，不是已经交差 interchangeable。319 consensusparams vs update bundled unbundling 在本页 item 2 续。

怎样编 `ConsensusParams`、怎样选 MaxBytes / MaxGas、公钥类型表是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **Finalize 没回 not already cleared ≠ 已经清掉 interchangeable：** 官方把回空什么也不做和真的改参数分开。
- **看见空着 not already changed ≠ 已经改了 interchangeable：** 官方把空着和已经改过分开。
- **看见能更新 not already settled ≠ 已经交差 interchangeable：** 官方把能更新和已经交差分开；319 consensusparams vs update bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Finalize 没回 | 不是已经清掉 | 不是 H 的参数更新已经在 H+1 生效（333） |
| 看见空着 | 不是已经改了 | 不是 Finalize 回了 consensus_param_updates 就已经清掉（471/712） |
| 看见能更新 | 不是已经交差 | 不是 InitChain 空参数就已经没有参数（908） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 没回 not already cleared / not already changed / not already settled 正式三事（319 余量），必须分开是不是已经清掉、是不是已经改了、是不是已经交差。可以跳过「看见没回就已经清掉」。不要把仓库默认 MaxBytes / MaxGas 当不确定默认。不要另写怎样编参数或怎样选上限。319 consensusparams vs update bundled unbundling 在本页 item 2 续；续 [`worked-example-consensusparams-notpartial-vs-bundled.md`](worked-example-consensusparams-notpartial-vs-bundled.md)（不变量 910 item 3）。

## 本页不抄

- 怎样编 `ConsensusParams`、怎样选 MaxBytes / MaxGas、公钥类型表。
- ConsensusParams bundled。那是不变量 319。
- InitChain 空参数就已经没有参数。那是不变量 319 item 1 余量 / 908。
- H 的参数更新已经在 H+1 生效。那是不变量 333。
- Finalize 回了 consensus_param_updates 就已经清掉。那是不变量 471 / 712。
