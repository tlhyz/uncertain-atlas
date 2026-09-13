# 例：看见 Misbehavior.total_voting_power 是 height 那一高验证者集合的总投票权不是已经 VoteInfo.validator.power / Misbehavior.validator.power 那种单个验证者权；看见 Misbehavior.total_voting_power 不是已经按到场定奖惩；看见 Misbehavior.total_voting_power 不是已经定了奖惩

**层次**：实现 / Misbehavior total_voting_power 栏正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Misbehavior Fields。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「Misbehavior.total_voting_power 是 height 那一高验证者集合的总投票权不是已经 VoteInfo.validator.power / Misbehavior.validator.power 那种单个验证者权 / Misbehavior.total_voting_power 不是已经按到场定奖惩 / Misbehavior.total_voting_power 不是已经定了奖惩」，不是 Misbehavior 结构栏 type/height/time/total_voting_power 那套已经罚没，也不是 misbehavior 列表就已经定奖惩。不要另写怎样填 Misbehavior total_voting_power 栏。

## 官方三件事

规范把 Misbehavior 里 `total_voting_power` 栏写成三件独立的实现事，不是「看见 Misbehavior 里填了 total_voting_power 就已经按到场定奖惩、已经是单个验证者权、已经定了奖惩」一件事：

1. **看见 Misbehavior.total_voting_power 是 height 那一高验证者集合的总投票权 / 看见填了 total_voting_power 不是已经 VoteInfo.validator.power / Misbehavior.validator.power 那种单个验证者权，也不是已经 CommitInfo.votes 里按投票权降序排过那种已经奖罚完。**  
   官方写：`total_voting_power` is Total voting power of the validator set at height `height`。看见能指那一高整个集合的总权，不是已经 VoteInfo / ExtendedVoteInfo 里某个 `Validator.power` 那种单个验证者权 interchangeable。看见有总权数字，不是已经 Misbehavior.validator 里 address+power 那种 offending validator 的 power 就等于集合总权。
2. **看见 Misbehavior.total_voting_power 是 offense height 那一高的集合总权 / 看见填了 total_voting_power 不是已经按到场定奖惩，也不是已经 block_id_flag 那种 VoteInfo / ExtendedVoteInfo Usage 里 allowing for rewards based on validator availability 就已经奖罚完。**  
   官方把 total_voting_power 和 height 配成「过错发生在哪一高、那一高验证者集合的总权」。看见有集合总权，不是已经 CommitInfo / ExtendedCommitInfo 里 votes 按到场定奖惩那种已经交差。看见填了总权，不是已经 Finalize 可以用 `decided_last_commit` 和 `misbehavior` 定奖惩那种已经奖罚完。
3. **看见 Misbehavior.total_voting_power / 看见有总权 不是已经定了奖惩，也不是已经 slashed，也不是已经改了集合。**  
   官方把集合总权字段和已经罚没分开。看见有 total_voting_power，不是已经证据上链就罚没那种已经交差。看见填了总权，不是已经 ValidatorUpdate 那种已经改了集合。

怎样填 Misbehavior.total_voting_power、怎样从 evidence 算那一高集合总权、怎样和 VoteInfo 对齐是规范里的做法，本页不抄。Misbehavior 结构栏 type/height/time/total_voting_power 是不变量 372 的另一切片，Misbehavior.validator 是不变量 448，Misbehavior height/time 是不变量 449，Prepare/Process/Finalize 请求 misbehavior 列表是不变量 413/420/428，本页不抄。

## 官方为什么这样拆

- **Misbehavior.total_voting_power 是 height 那一高验证者集合的总投票权 ≠ 已经是 VoteInfo.validator.power / Misbehavior.validator.power 那种单个验证者权：** 官方把集合总权和单个验证者 power 分开。
- **Misbehavior.total_voting_power 是 offense height 那一高的集合总权 ≠ 已经按到场定奖惩：** 官方把那一高总权和 VoteInfo / ExtendedVoteInfo 按到场定奖惩分开。
- **Misbehavior.total_voting_power ≠ 已经定了奖惩 / 已经 slashed / 已经改了集合：** 官方把集合总权字段和已经罚没分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Misbehavior.total_voting_power 是集合总权 | 不是已经 VoteInfo.validator.power / Misbehavior.validator.power 那种单个验证者权 | 不是 Misbehavior 结构栏就已经罚没（372） |
| Misbehavior.total_voting_power | 不是已经按到场定奖惩 | 不是 VoteInfo 能按到场定奖惩就已经罚没（365） |
| Misbehavior.total_voting_power | 不是已经定了奖惩 | 不是 misbehavior 列表就已经定奖惩（413） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Misbehavior 里填了 total_voting_power 就已经按到场定奖惩、已经是单个验证者权、已经定了奖惩」，必须分开 Misbehavior.total_voting_power 是不是已经 VoteInfo.validator.power / Misbehavior.validator.power 那种单个验证者权、Misbehavior.total_voting_power 是不是已经按到场定奖惩、Misbehavior.total_voting_power 是不是已经定了奖惩。可以跳过「看见 Misbehavior 里填了 total_voting_power 就已经奖罚完」。不要另写怎样填 Misbehavior total_voting_power 栏。

## 本页不抄

- 怎样填 Misbehavior.total_voting_power、怎样从 evidence 算那一高集合总权、怎样和 VoteInfo 对齐。
- Misbehavior.type / height / time。那是不变量 372 / 449 的 Misbehavior 结构其它栏。
- Misbehavior.validator。那是不变量 448。
- misbehavior 列表就已经定奖惩。那是不变量 413 / 420 / 428 的请求栏。
- VoteInfo 能按到场定奖惩就已经罚没。那是不变量 365。
