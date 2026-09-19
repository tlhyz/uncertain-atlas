# 例：看见没回 / 看见空着 / 看见能更新 is not already already clear interchangeable / already changed interchangeable / already InitChain-empty-same interchangeable

**层次**：实现 / Finalize 没回不是已经清掉 not already clear / not already changed / not already InitChain-empty-same 正式三事（319 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Updating Consensus Parameters。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Finalize 没回不是已经清掉 not already clear / not already changed / not already InitChain-empty-same 正式三事（319 余量）/ not 717 consensusparams-notclear interchangeable / not 319 consensusparams bundled interchangeable」，不是 ConsensusParams vs update bundled（319），也不是 InitChain 空参数不是已经没有参数（716 item 1 余量）或只改一个字段不是已经只改这一项（718 item 3 余量）。不要另写怎样编 `ConsensusParams` 或怎样选上限。

## 官方三件事

规范把 Requirements 里 `FinalizeBlockResponse` 也收一份 `ConsensusParams`、若是 `nil` 则 CometBFT **什么也不做**、若不空则用回包这份 和「已经是没回就已经清成默认 interchangeable / 已经是空着就已经改过 interchangeable / 已经是能更新就已经和 InitChain 空回包同一句 interchangeable / 已经是 ConsensusParams vs update bundled interchangeable」分开写成三件独立的实现事，不是「看见 FinalizeBlock 回了空 就已经清掉 interchangeable / 就已经改了 interchangeable / 就已经和 InitChain 空回包同一句 interchangeable」一件事：

1. **看见没回 / 看见 Finalize 没回 ConsensusParams / 看见 FinalizeBlock 回了空 is not already 已经清成默认 interchangeable / 已经 clear interchangeable / 已经清掉 interchangeable / 319 consensusparams bundled interchangeable / 33 four gates interchangeable / consensusparams-sold-as-updated interchangeable，也不是已经 ConsensusParams vs update bundled（319） interchangeable / 717 consensusparams-notclear interchangeable / 319 consensusparams item 2 interchangeable，也不是已经 Finalize 没回不是已经清掉 not already clear / not already changed / not already InitChain-empty-same 正式三事 bundled（319 item 2 余量） interchangeable / 319 consensusparams item 2 interchangeable，也不是已经 InitChain 空参数不是已经没有参数（716） interchangeable / 718 consensusparams-notpartial interchangeable / 35 params delay interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：若是 `nil`，CometBFT **什么也不做**。看见没回，不是已经清成默认 interchangeable——319 钉 bundled 三事，本页从 item 2 侧钉 not already clear 单句。看见 Finalize 没回 ConsensusParams，不是已经 ConsensusParams vs update bundled（319） interchangeable——319 钉 bundled，本页钉 item 2 第一件事。看见 FinalizeBlock 回了空，不是已经 InitChain 空参数不是已经没有参数（716） interchangeable——716 另钉 item 1，本页钉 item 2 第一件事。319 consensusparams vs update bundled unbundling 在本页 item 2 续。

2. **看见空着 / 看见 Finalize 空着 / 看见回包空 is not already 已经改过 interchangeable / 已经 changed interchangeable / 已经改了参数 interchangeable / 319 consensusparams bundled interchangeable / 35 params delay interchangeable，也不是已经 ConsensusParams vs update bundled（319） interchangeable / 717 consensusparams-notclear interchangeable / 319 consensusparams item 1 InitChain interchangeable / 319 consensusparams item 3 partial interchangeable，也不是已经 Finalize 没回不是已经清掉 not already clear / not already changed / not already InitChain-empty-same 正式三事 bundled（319 item 2 余量） interchangeable / 319 consensusparams item 2 interchangeable，也不是已经清成默认（本页第一件事） interchangeable。**  
   官方把什么也不做和已经改过路径分开——空着，不等于已经改过。看见空着，不是已经改过 interchangeable——本页钉 not already changed 单句。看见 Finalize 空着，不是已经只改一个字段不是已经只改这一项（718） interchangeable——718 另钉 item 3，本页钉 item 2 第二件事。看见回包空，不是已经 H 的参数更新已经在 H+1 生效（35） interchangeable——35 另钉，本页钉 item 2 第二件事。319 consensusparams vs update bundled unbundling 在本页 item 2 续。

3. **看见能更新 / 看见 Finalize 能更新参数 / 看见能回 ConsensusParams is not already 已经和 InitChain 空回包同一句 interchangeable / 已经 InitChain-empty-same interchangeable / 已经和 InitChain nil 同一路径 interchangeable / 319 consensusparams bundled interchangeable / 716 consensusparams-notempty interchangeable，也不是已经 ConsensusParams vs update bundled（319） interchangeable / 717 consensusparams-notclear interchangeable / 319 consensusparams item 1 / 319 consensusparams item 3，也不是已经 Finalize 没回不是已经清掉 not already clear / not already changed / not already InitChain-empty-same 正式三事 bundled（319 item 2 余量） interchangeable / 319 consensusparams item 2 interchangeable，也不是已经清成默认（本页第一件事） interchangeable / 已经改过（本页第二件事） interchangeable。**  
   官方把 Finalize nil 什么也不做和 InitChain nil 改用创世参数路径分开——能更新，不等于已经和 InitChain 空回包同一句。看见能更新，不是已经 InitChain-empty-same interchangeable——本页钉 not already InitChain-empty-same 单句。看见 Finalize 能更新参数，不是已经清成默认（本页第一件事） interchangeable——三件事分开钉。看见能回 ConsensusParams，不是已经 InitChain 空参数 not already no params（716） interchangeable——716 另钉 InitChain 侧。319 consensusparams vs update bundled unbundling 在本页 item 2 完成。

怎样编 `ConsensusParams`、怎样选 MaxBytes / MaxGas、公钥类型表是规范里的取值或做法，本页不抄。ConsensusParams vs update bundled（319）、InitChain 空参数不是已经没有参数（319 item 1 余量 / 716）、只改一个字段不是已经只改这一项（319 item 3 余量 / 718）、H 更新生效（35）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **没回 not already clear ≠ 319 / 33 interchangeable：** 官方把什么也不做单句和已经清成默认路径分开。
- **空着 not already changed ≠ 已经改过 interchangeable：** 官方把 nil 什么也不做单句和已经改过路径分开。
- **能更新 not already InitChain-empty-same ≠ 已经和 InitChain 空回包同一句 interchangeable：** 官方把 Finalize nil 与 InitChain nil 路径分开；319 consensusparams vs update bundled unbundling 在本页 item 2 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 没回 | 不是 already clear | 不是 InitChain 空参数 alone（716） |
| 空着 | 不是 already changed | 不是只改一项 alone（718） |
| 能更新 | 不是 already InitChain-empty-same | 不是 InitChain 改用创世 alone（716） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 没回不是已经清掉 not already clear / not already changed / not already InitChain-empty-same 正式三事（319 余量），必须分开没回 是不是 already clear interchangeable / 319 consensusparams bundled interchangeable / consensusparams-sold-as-updated interchangeable、空着 是不是 already changed interchangeable、能更新 是不是 already InitChain-empty-same interchangeable。可以跳过「看见没回就已经清成默认 interchangeable / 就已经改过 interchangeable / 就已经和 InitChain 空回包同一句 interchangeable」。不要另写怎样编参数。319 consensusparams vs update bundled unbundling 在本页 item 2 完成；续 [`worked-example-consensusparams-notpartial-vs-bundled.md`](worked-example-consensusparams-notpartial-vs-bundled.md)（不变量 718 item 3）。319 consensusparams vs update bundled unbundling 在 716 + 717 + 718 完成。

## 本页不抄

- 怎样编 `ConsensusParams`、怎样选 MaxBytes / MaxGas、公钥类型表。
- ConsensusParams vs update bundled。那是不变量 319。
- InitChain 空参数不是已经没有参数。那是不变量 319 item 1 余量 / 716。
- 只改一个字段不是已经只改这一项。那是不变量 319 item 3 余量 / 718。
- H+1 生效。那是不变量 35。
- 四门已经结算。那是不变量 33。
