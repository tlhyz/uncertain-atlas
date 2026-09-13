# 例：看见 Misbehavior.validator 是过错验证者不是已经 slashed；看见 Misbehavior.validator 只是 address+power 的 Validator 结构不是已经 VoteInfo.validator 那种按到场定奖惩；看见 Misbehavior.validator 不是已经 ValidatorUpdate 那种已经改了集合

**层次**：实现 / Misbehavior.validator 栏正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Misbehavior Fields。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「Misbehavior.validator 是过错验证者不是已经 slashed / Misbehavior.validator 只是 address+power 的 Validator 结构不是已经 VoteInfo.validator 那种按到场定奖惩 / Misbehavior.validator 不是已经 ValidatorUpdate 那种已经改了集合」，不是 Misbehavior.type 只是过错枚举就已经罚没，也不是 misbehavior 列表就已经定奖惩。不要另写怎样写 Misbehavior.validator 栏。

## 官方三件事

规范把 Misbehavior 里 `validator` 栏写成三件独立的实现事，不是「看见 Misbehavior 里填了 validator 就已经 slashed、已经是 CommitInfo votes 里那份、已经改了集合」一件事：

1. **看见 Misbehavior.validator 是过错验证者 / 看见填了 validator 不是已经 slashed，也不是已经罚没。**  
   官方写：`validator` is The offending validator。看见能指过错的人，不是已经 slashed。看见有 address 和 power，不是已经定了奖惩。看见 Misbehavior 结构里有 validator，不是已经证据上链就罚没那种已经交差。
2. **看见 Misbehavior.validator 只是 address+power 的 Validator 结构 / 看见填了 validator 不是已经 VoteInfo.validator 那种按到场定奖惩，也不是已经 CommitInfo.votes 里那份 interchangeable。**  
   官方写：`Validator` 字段只有 `address` 和 `power`。`Validator` 也作为 `VoteInfo` / `ExtendedVoteInfo` 的一部分出现在 `CommitInfo` / `ExtendedCommitInfo` 里，用来按到场定奖惩。Misbehavior 里的 `validator` 另指 offending validator。看见同是 Validator 类型，不是已经 VoteInfo 里那份就可以 interchange。看见有 power，不是已经 block_id_flag 那种已经奖罚完。
3. **看见 Misbehavior.validator 不是已经 ValidatorUpdate 那种已经改了集合，也不是已经带了公钥。**  
   官方写：`ValidatorUpdate` 用 PubKeyType 和 PubKeyBytes 认人，用来告诉 CometBFT 更新验证者集合。Misbehavior 里的 `Validator` 不带 PubKey。看见有 address，不是已经能验签。看见过错验证者，不是已经 FinalizeBlockResponse.validator_updates 那种已经改了集合。

怎样填 Misbehavior.validator、怎样从 evidence 编过错验证者、怎样和 VoteInfo 对齐是规范里的做法，本页不抄。Misbehavior.type/height/time/total_voting_power 是不变量 372 的另一切片，MisbehaviorType enum 三值是不变量 447，Prepare/Process/Finalize 请求 misbehavior 列表是不变量 413/420/428，本页不抄。

## 官方为什么这样拆

- **Misbehavior.validator 是过错验证者 ≠ 已经 slashed / 已经罚没：** 官方把 offending validator 字段和已经罚没分开。
- **Misbehavior.validator 只是 Validator 结构 ≠ 已经是 VoteInfo.validator 按到场定奖惩：** 官方把过错验证者和 CommitInfo/ExtendedCommitInfo 里按到场定奖惩的 Validator 分开。
- **Misbehavior.validator ≠ 已经 ValidatorUpdate / 已经改了集合：** 官方把 Misbehavior 里的 address+power 和 Finalize 回包更新集合分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Misbehavior.validator 是过错验证者 | 不是已经 slashed | 不是 Misbehavior.type 只是过错枚举就已经罚没（372） |
| Misbehavior.validator 只是 Validator 结构 | 不是已经 VoteInfo.validator 按到场定奖惩 | 不是 VoteInfo 能按到场定奖惩就已经罚没（365） |
| Misbehavior.validator | 不是已经 ValidatorUpdate | 不是 Validator 用 address 认人就已经带了公钥（364） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Misbehavior 里填了 validator 就已经 slashed、已经是 CommitInfo votes 里那份、已经改了集合」，必须分开 Misbehavior.validator 是不是已经 slashed、Misbehavior.validator 是不是已经 VoteInfo.validator 那种按到场定奖惩、Misbehavior.validator 是不是已经 ValidatorUpdate。可以跳过「看见 Misbehavior 里填了 validator 就已经罚没」。不要另写怎样写 Misbehavior.validator 栏。

## 本页不抄

- 怎样填 Misbehavior.validator、怎样从 evidence 编过错验证者、怎样和 VoteInfo 对齐。
- Misbehavior.type/height/time/total_voting_power。那是不变量 372 的 Misbehavior 结构其它栏。
- misbehavior 列表就已经定奖惩。那是不变量 413 / 420 / 428 的请求栏。
- MisbehaviorType enum 三值。那是不变量 447。
