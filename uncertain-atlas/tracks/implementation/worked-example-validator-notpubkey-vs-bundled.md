# 例：看见 Validator 用 address 认人 is not already has pubkey interchangeable / not already can verify sig interchangeable / not already ValidatorUpdate interchangeable

**层次**：实现 / Validator 用 address 认人 not already has pubkey / not already can verify sig / not already ValidatorUpdate 正式三事（364 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Validator / ValidatorUpdate。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Validator 用 address 认人 not already has pubkey / not already can verify sig / not already ValidatorUpdate 正式三事（364 余量）/ not 833 validator-notpubkey interchangeable / not 364 validator-vs-update bundled interchangeable」，不是 Validator 类型 bundled（364），也不是从块抽出就已经带了公钥（365/831），也不是 H 的更新已经在 H+1 计票（35），也不是 ConsensusParams.validator 就已经带了公钥（385/774）。不要另写怎样写 Validator 类型。

## 官方三件事

1. **看见 Validator 用 address 认人 / 看见只有 address 和 power / 这份认人 is not already 已经带了公钥 interchangeable / 365 voteinfo interchangeable，也不是已经 Validator 类型 bundled（364） interchangeable / 833 validator-notpubkey interchangeable / 834 validator-notselected interchangeable / 364 validator item 2 不带 PubKey interchangeable，也不是已经 Validator 用 address 认人 not already has pubkey / not already can verify sig / not already ValidatorUpdate 正式三事 bundled（364 item 1 余量） interchangeable / 364 validator item 1 interchangeable。**  
   官方写：`Validator` 用 address 认人。字段只有 `address` 和 `power`。看见 VoteInfo 里有这份结构，不是已经带了公钥 interchangeable——本页从 364 item 1 侧钉 not already has pubkey 单句。364 validator vs update bundled unbundling 在本页 item 1 启动。

2. **看见只有 address 和 power / 看见有 address / 这份认人 is not already 已经能验签 interchangeable / 365 voteinfo interchangeable，也不是已经 Validator 类型 bundled（364） interchangeable / 833 validator-notpubkey interchangeable / 364 validator item 3 ValidatorUpdate interchangeable / 835 validator-notchanged interchangeable，也不是已经从块抽出就已经带了公钥 interchangeable / 365 voteinfo / 831 voteinfo-notpubkey interchangeable，也不是已经 H 的更新已经在 H+1 计票 interchangeable / 35 nextset interchangeable。**  
   官方把有 address 和已经能验签分开——364 bundled 第一件事常与 365 / 35 混成「看见 VoteInfo 里有验证者就已经带了公钥或已经能验签 interchangeable」，本页钉 not already can verify sig 单句。

3. **看见只有 address 和 power / 看见有 power / 这份认人 is not already 已经是 ValidatorUpdate interchangeable，也不是已经 Validator 类型 bundled（364） interchangeable / 833 validator-notpubkey interchangeable / 834 validator-notselected interchangeable，也不是已经 ConsensusParams.validator 就已经带了公钥 interchangeable / 385 paramsblock / 774 paramsblock-notpubkey interchangeable。**  
   官方把有 power 和已经是 ValidatorUpdate 分开。看见有 power，不是已经是 ValidatorUpdate interchangeable。364 validator vs update bundled unbundling 在本页 item 1 启动。

怎样编 Validator、怎样编 ValidatorUpdate、怎样在 ABCI 上传钥是规范里的做法，本页不抄。

## 官方为什么这样拆

- **Validator 用 address 认人 not already has pubkey ≠ 365 interchangeable：** 官方把票里认人和更新里认人分开。
- **看见有 address not already can verify sig ≠ 已经能验签 interchangeable：** 官方把有 address 和已经能验签分开。
- **看见有 power not already ValidatorUpdate ≠ 已经是 ValidatorUpdate interchangeable：** 官方把有 power 和已经是 ValidatorUpdate 分开；364 validator vs update bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Validator 用 address 认人 | 不是已经带了公钥 | 不是不带 PubKey（834/364 item 2） |
| 看见有 address | 不是已经能验签 | 不是从块抽出就已经带了公钥（365/831） |
| 看见有 power | 不是已经是 ValidatorUpdate | 不是 H+1 计票（35） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Validator 用 address 认人 not already has pubkey / not already can verify sig / not already ValidatorUpdate 正式三事（364 余量），必须分开是不是已经带了公钥、是不是已经能验签、是不是已经是 ValidatorUpdate。可以跳过「看见只有 address 和 power 就已经带了公钥」。不要另写怎样写 Validator 类型。364 validator vs update bundled unbundling 在本页 item 1 启动；续 [`worked-example-validator-notselected-vs-bundled.md`](worked-example-validator-notselected-vs-bundled.md)（不变量 834 item 2）。

## 本页不抄

- 怎样编 Validator、怎样编 ValidatorUpdate、怎样在 ABCI 上传钥。
- Validator 类型 bundled。那是不变量 364。
- 不带 PubKey。那是不变量 364 item 2 余量 / 834。
- 从块抽出就已经带了公钥。那是不变量 365 / 831。
- H 的更新已经在 H+1 计票。那是不变量 35。
