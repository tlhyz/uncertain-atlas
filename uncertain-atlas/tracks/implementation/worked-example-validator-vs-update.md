# 例：看见 Validator 用 address 认人不是已经带了公钥；看见不带 PubKey 是为了不在 ABCI 上传大后量子公钥不是已经选型；看见 ValidatorUpdate 用 pub_key_type 和 pub_key_bytes 认人不是已经改了集合

**层次**：实现 / Validator 类型。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Validator / ValidatorUpdate。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「Validator 用 address 认人不是已经带了公钥 / 不带 PubKey 不是已经选型 / ValidatorUpdate 用公钥认人不是已经改了集合」，不是 H 的更新已经在 H+1 计票，也不是 InitChain 空名单就已经没有集合。不要另写怎样写 Validator 类型。

## 官方三件事

规范把 `Validator` 用 address 认人、不带 PubKey 以免在 ABCI 上传大后量子公钥、`ValidatorUpdate` 用公钥认人写成三件独立的实现事，不是「看见 VoteInfo 里有验证者就已经带了公钥、已经选型、已经改了集合」一件事：

1. **看见 Validator 用 address 认人 / 看见只有 address 和 power 不是已经带了公钥，也不是已经能验签。**  
   官方写：`Validator` 用 address 认人。字段只有 `address` 和 `power`。看见 VoteInfo / CommitInfo / ExtendedCommitInfo 里有这份结构，不是已经带了公钥。看见有 address，不是已经能验签。看见有 power，不是已经是 `ValidatorUpdate`。
2. **看见不带 PubKey 是为了不在 ABCI 上传大后量子公钥 / 看见省了字段 不是已经选型，也不是已经没有后量子钥。**  
   官方写：不带 PubKey，是为了避免在 ABCI 上传送可能很大的后量子公钥。看见省了字段，不是已经选定算法。看见提到后量子公钥，不是已经没有后量子钥。看见 ABCI 不传公钥，不是已经交差。
3. **看见 ValidatorUpdate 用 `pub_key_type` 和 `pub_key_bytes` 认人 / 看见更新集合 不是已经是 VoteInfo 里那份 Validator，也不是已经改了集合。**  
   官方写：`ValidatorUpdate` 用 PubKeyType 和 PubKeyBytes 认人，用来告诉 CometBFT 更新验证者集合。看见有公钥字段，不是已经是 `CommitInfo` 里那份 `Validator`。看见回了更新，不是已经改了集合。看见有 `pub_key_type`，不是已经选型。

怎样编 `Validator`、怎样编 `ValidatorUpdate`、怎样在 ABCI 上传钥是规范里的做法，本页不抄。H 的更新已经在 H+1 计票是不变量 35，本页不抄。

## 官方为什么这样拆

- **Validator 用 address 认人 ≠ 已经带了公钥：** 官方把票里认人和更新里认人分开。
- **不带 PubKey ≠ 已经选型：** 官方把省字段和已经选定算法分开。
- **ValidatorUpdate 用公钥认人 ≠ 已经改了集合：** 官方把更新结构和已经改完分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Validator 用 address 认人 | 不是已经带了公钥 | 不是 H 的更新已经在 H+1 计票（35） |
| 不带 PubKey | 不是已经选型 | 不是 InitChain 空名单就已经没有集合（318） |
| ValidatorUpdate 用公钥认人 | 不是已经改了集合 | 不是必须回四列就已经改了集合（363） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 VoteInfo 里有验证者就已经带了公钥、已经选型、已经改了集合」，必须分开 Validator 用 address 认人是不是已经带了公钥、不带 PubKey 是不是已经选型、ValidatorUpdate 用公钥认人是不是已经改了集合。可以跳过「看见 VoteInfo 里有验证者就已经带了公钥」。不要另写怎样写 Validator 类型。

## 本页不抄

- 怎样编 `Validator`、怎样编 `ValidatorUpdate`、怎样在 ABCI 上传钥。
- H 的更新已经在 H+1 计票。那是不变量 35。
- InitChain 空名单就已经没有集合。那是不变量 318。
- 必须回四列就已经改了集合。那是不变量 363。
