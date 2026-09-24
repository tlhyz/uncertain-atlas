# 例：看见有公钥字段 / 看见回了更新 / 看见有 pub_key_type is not already already same-val interchangeable / already changed-set interchangeable / already algo interchangeable

**层次**：实现 / ValidatorUpdate 用公钥认人不是已经改了集合 not already same-val / not already changed-set / not already algo 正式三事（364 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Validator / ValidatorUpdate。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ValidatorUpdate 用公钥认人不是已经改了集合 not already same-val / not already changed-set / not already algo 正式三事（364 余量）/ not 841 valupdate-notset interchangeable / not 364 validator bundled interchangeable」，不是 Validator 类型 bundled（364），也不是 Validator 用 address 认人不是已经带了公钥（839 item 1 余量）或不带 PubKey 不是已经选型（840 item 2 余量）。不要另写怎样写 Validator 类型。

## 官方三件事

规范把 Methods 里 `ValidatorUpdate` 用 PubKeyType 和 PubKeyBytes 认人、用来告诉 CometBFT 更新验证者集合 和「已经是有公钥字段就已经是 VoteInfo 里那份 Validator interchangeable / 已经是回了更新就已经改了集合 interchangeable / 已经是有 pub_key_type 就已经选型 interchangeable / 已经是 validator bundled interchangeable」分开写成三件独立的实现事，不是「看见有公钥字段就已经是 VoteInfo 里那份 Validator interchangeable / 就已经改了集合 interchangeable / 就已经选型 interchangeable」一件事：

1. **看见有公钥字段 / 看见 ValidatorUpdate 用 `pub_key_type` 和 `pub_key_bytes` 认人 / 看见有公钥字段 is not already 已经是 VoteInfo / CommitInfo 里那份 Validator interchangeable / 已经 same-val interchangeable / 已经是那份 Validator 交差 interchangeable / 364 validator bundled interchangeable / 363 finresp interchangeable / validator-sold-as-update interchangeable，也不是已经 Validator 类型 bundled（364） interchangeable / 841 valupdate-notset interchangeable / 364 validator item 3 interchangeable，也不是已经 ValidatorUpdate 用公钥认人不是已经改了集合 not already same-val / not already changed-set / not already algo 正式三事 bundled（364 item 3 余量） interchangeable / 364 validator item 3 interchangeable，也不是已经带了公钥（839） interchangeable / 840 valnopub-notalgo interchangeable / 35 valupdate interchangeable，也不是已经必须回四列就已经改了集合（363） interchangeable。**  
   官方写：`ValidatorUpdate` 用 PubKeyType 和 PubKeyBytes 认人，用来告诉 CometBFT 更新验证者集合。看见有公钥字段，不是已经是 `CommitInfo` 里那份 `Validator`。看见有公钥字段，不是已经 same-val interchangeable——364 钉 bundled 三事，本页从 item 3 侧钉 not already same-val 单句。看见 ValidatorUpdate 用公钥认人，不是已经 Validator 类型 bundled（364） interchangeable——364 钉 bundled，本页钉 item 3 第一件事。看见有公钥字段，不是已经带了公钥（839） interchangeable——839 另钉 item 1。看见有公钥字段，不是已经不带 PubKey 选型（840） interchangeable——840 另钉 item 2。364 validator-vs-update bundled unbundling 在本页 item 3 完成。

2. **看见回了更新 / 看见用来告诉 CometBFT 更新验证者集合 / 看见回了 ValidatorUpdate is not already 已经改了集合 interchangeable / 已经 changed-set interchangeable / 已经改了集合交差 interchangeable / 364 validator bundled interchangeable / 363 finresp interchangeable，也不是已经 Validator 类型 bundled（364） interchangeable / 841 valupdate-notset interchangeable / 364 validator item 1 address interchangeable / 364 validator item 2 省字段 interchangeable，也不是已经 ValidatorUpdate 用公钥认人不是已经改了集合 not already same-val / not already changed-set / not already algo 正式三事 bundled（364 item 3 余量） interchangeable / 364 validator item 3 interchangeable，也不是已经是那份 Validator（本页第一件事） interchangeable。**  
   官方写：看见回了更新，不是已经改了集合。看见用来告诉 CometBFT 更新验证者集合，不是已经 changed-set interchangeable——本页钉 not already changed-set 单句。看见回了 ValidatorUpdate，不是已经是那份 Validator（本页第一件事） interchangeable——三件事分开钉。364 validator-vs-update bundled unbundling 在本页 item 3 完成。

3. **看见有 pub_key_type / 看见有 PubKeyType / 看见有类型字段 is not already 已经选型 interchangeable / 已经 algo interchangeable / 已经选型交差 interchangeable / 364 validator bundled interchangeable / 33 fourgates interchangeable，也不是已经 Validator 类型 bundled（364） interchangeable / 841 valupdate-notset interchangeable / 364 validator item 1 / 364 validator item 2，也不是已经 ValidatorUpdate 用公钥认人不是已经改了集合 not already same-val / not already changed-set / not already algo 正式三事 bundled（364 item 3 余量） interchangeable / 364 validator item 3 interchangeable，也不是已经是那份 Validator（本页第一件事） interchangeable / 已经改了集合（本页第二件事） interchangeable。**  
   官方写：看见有 `pub_key_type`，不是已经选型。看见有 PubKeyType，不是已经 algo interchangeable——本页钉 not already algo 单句。看见有类型字段，不是已经改了集合（本页第二件事） interchangeable——三件事分开钉。364 validator-vs-update bundled unbundling 在本页 item 3 完成。

怎样编 `Validator`、怎样编 `ValidatorUpdate`、怎样在 ABCI 上传钥是规范里的做法，本页不抄。Validator 类型 bundled（364）、Validator 用 address 认人不是已经带了公钥（364 item 1 余量 / 839）、不带 PubKey 不是已经选型（364 item 2 余量 / 840）、H 的更新已经在 H+1 计票（35）、InitChain 空名单就已经没有集合（318）、必须回四列就已经改了集合（363）是另外那套，本页不抄。

## 官方为什么这样拆

- **有公钥字段 not already same-val ≠ 364 / 363 interchangeable：** 官方把有公钥字段和已经是 VoteInfo 里那份 Validator 分开。
- **回了更新 not already changed-set ≠ 已经改了集合 interchangeable：** 官方把回了更新和已经改了集合分开。
- **有 pub_key_type not already algo ≠ 已经选型 interchangeable：** 官方把有 pub_key_type 和已经选型分开；364 validator-vs-update bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 有公钥字段 | 不是 already same-val | 不是必须回四列就已经改了集合 alone（363） |
| 回了更新 | 不是 already changed-set | 不是有结构 already pubkey alone（839） |
| 有 pub_key_type | 不是 already algo | 不是省了字段 already algo alone（840） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ValidatorUpdate 用公钥认人不是已经改了集合 not already same-val / not already changed-set / not already algo 正式三事（364 余量），必须分开有公钥字段 是不是 already same-val interchangeable / 364 validator bundled interchangeable / validator-sold-as-update interchangeable、回了更新 是不是 already changed-set interchangeable、有 pub_key_type 是不是 already algo interchangeable。可以跳过「看见有公钥字段就已经是 VoteInfo 里那份 Validator interchangeable / 就已经改了集合 interchangeable / 就已经选型 interchangeable」。不要另写怎样写 Validator 类型。364 validator-vs-update bundled unbundling 在本页 item 3 完成（839 + 840 + 841）。

## 本页不抄

- 怎样编 `Validator`、怎样编 `ValidatorUpdate`、怎样在 ABCI 上传钥。
- Validator 类型 bundled。那是不变量 364。
- Validator 用 address 认人不是已经带了公钥。那是不变量 364 item 1 余量 / 839。
- 不带 PubKey 不是已经选型。那是不变量 364 item 2 余量 / 840。
- H 的更新已经在 H+1 计票。那是不变量 35。
- InitChain 空名单就已经没有集合。那是不变量 318。
- 必须回四列就已经改了集合。那是不变量 363。
