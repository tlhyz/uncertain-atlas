# 例：看见 ValidatorUpdate 用公钥认人 is not already VoteInfo Validator interchangeable / not already changed set interchangeable / not already selected interchangeable

**层次**：实现 / ValidatorUpdate 用公钥认人 not already VoteInfo Validator / not already changed set / not already selected 正式三事（364 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Validator / ValidatorUpdate。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ValidatorUpdate 用公钥认人 not already VoteInfo Validator / not already changed set / not already selected 正式三事（364 余量）/ not 835 validator-notchanged interchangeable / not 364 validator-vs-update bundled interchangeable」，不是 Validator 类型 bundled（364），也不是必须回四列就已经改了集合（363），也不是 H 的更新已经在 H+1 计票（35），也不是从块抽出就已经是 ValidatorUpdate（365/831）。不要另写怎样写 Validator 类型。

## 官方三件事

1. **看见 ValidatorUpdate 用 `pub_key_type` 和 `pub_key_bytes` 认人 / 看见更新集合 / 这份更新 is not already 已经是 VoteInfo 里那份 Validator interchangeable / 365 voteinfo interchangeable，也不是已经 Validator 类型 bundled（364） interchangeable / 835 validator-notchanged interchangeable / 833 validator-notpubkey interchangeable / 364 validator item 1 address interchangeable，也不是已经 ValidatorUpdate 用公钥认人 not already VoteInfo Validator / not already changed set / not already selected 正式三事 bundled（364 item 3 余量） interchangeable / 364 validator item 3 interchangeable。**  
   官方写：`ValidatorUpdate` 用 PubKeyType 和 PubKeyBytes 认人，用来告诉 CometBFT 更新验证者集合。看见有公钥字段，不是已经是 CommitInfo 里那份 Validator interchangeable——本页从 364 item 3 侧钉 not already VoteInfo Validator 单句。364 validator vs update bundled unbundling 在本页 item 3 完成。

2. **看见更新集合 / 看见回了更新 / 这份更新 is not already 已经改了集合 interchangeable / 363 finresp interchangeable，也不是已经 Validator 类型 bundled（364） interchangeable / 835 validator-notchanged interchangeable / 364 validator item 2 不带 PubKey interchangeable / 834 validator-notselected interchangeable，也不是已经必须回四列就已经改了集合 interchangeable / 363 finresp interchangeable，也不是已经 H 的更新已经在 H+1 计票 interchangeable / 35 nextset interchangeable。**  
   官方把回了更新和已经改了集合分开——364 bundled 第三件事常与 363 / 35 混成「看见更新集合就已经改了集合或已经是 VoteInfo 里那份 interchangeable」，本页钉 not already changed set 单句。

3. **看见更新集合 / 看见有 pub_key_type / 这份更新 is not already 已经选型 interchangeable，也不是已经 Validator 类型 bundled（364） interchangeable / 835 validator-notchanged interchangeable / 833 validator-notpubkey interchangeable，也不是已经从块抽出就已经是 ValidatorUpdate interchangeable / 365 voteinfo / 831 voteinfo-notpubkey interchangeable。**  
   官方把有 pub_key_type 和已经选型分开。看见有 pub_key_type，不是已经选型 interchangeable。364 validator vs update bundled unbundling 在本页 item 3 完成。

怎样编 Validator、怎样编 ValidatorUpdate、怎样在 ABCI 上传钥是规范里的做法，本页不抄。

## 官方为什么这样拆

- **ValidatorUpdate 用公钥认人 not already VoteInfo Validator ≠ 365 interchangeable：** 官方把更新结构和票里那份 Validator 分开。
- **看见回了更新 not already changed set ≠ 363 interchangeable：** 官方把更新结构和已经改完分开。
- **看见有 pub_key_type not already selected ≠ 已经选型 interchangeable：** 官方把有 pub_key_type 和已经选型分开；364 validator vs update bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ValidatorUpdate 用公钥认人 | 不是已经是 VoteInfo 里那份 Validator | 不是 address 认人（833/364 item 1） |
| 看见回了更新 | 不是已经改了集合（363） | 不是 H+1 计票（35） |
| 看见有 pub_key_type | 不是已经选型 | 不是从块抽出就已经是 ValidatorUpdate（365/831） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ValidatorUpdate 用公钥认人 not already VoteInfo Validator / not already changed set / not already selected 正式三事（364 余量），必须分开是不是已经是 VoteInfo 里那份 Validator、是不是已经改了集合 interchangeable / 363、是不是已经选型。可以跳过「看见回了更新就已经改了集合」。不要另写怎样写 Validator 类型。364 validator vs update bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样编 Validator、怎样编 ValidatorUpdate、怎样在 ABCI 上传钥。
- Validator 类型 bundled。那是不变量 364。
- Validator 用 address 认人。那是不变量 364 item 1 余量 / 833。
- 必须回四列就已经改了集合。那是不变量 363。
- 从块抽出就已经是 ValidatorUpdate。那是不变量 365 / 831。
