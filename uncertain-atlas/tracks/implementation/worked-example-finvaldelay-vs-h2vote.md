# 例：看见块 H 触发的 validator_updates 在 H+1 只更新 NextValidatorsHash 不是已经在 H+1 按新集合计票；看见 H+2 集合变更才生效 / ValidatorsHash 才更新 不是已经在 H+1 换人；看见 H+3 *_last_commit 才带变更后的集合 不是已经在 H+1/H+2 的 proposed_last_commit / decided_last_commit 就已经是新集合

**层次**：实现 / FinalizeBlock validator_updates H+1/H+2/H+3 生效正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)、[L4.5](../../courses/level-04-bft/L04-M05-validator-set.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5 以外的集合课正文、mempool。本页是「H+1 只更新 Next ≠ 已经在 H+1 计票 / H+2 ValidatorsHash 才生效 ≠ 已经在 H+1 换人 / H+3 last_commit 才带新集合 ≠ 已经 proposed/decided_last_commit 就是新集合」，不是集合更新必须写出哪一高度改哪一个哈希那条总则，也不是 Finalize 回包栏里 validator_updates 已经在 H+1 换人，也不是 consensus_param_updates H→H+1 立刻生效。不要另写怎样编 ValidatorUpdate 或解绑天数。

## 官方三件事

规范把块 H 触发的 `validator_updates` 在 H+1、H+2、H+3 各改哪个对象写成三件独立的实现事，不是「看见 Finalize 回了 validator_updates 就已经在 H+1 换人、Next 更新了就已经计票、last_commit 立刻带新集合」一件事：

1. **看见块 H 触发的 `FinalizeBlockResponse.validator_updates` 在高度 H+1 只让 `NextValidatorsHash` 纳入这份更新 / 看见 H+1 更新了 Next 不是已经在 H+1 按新集合计票，也不是已经 `ValidatorsHash` 已经更新。**  
   官方写：`FinalizeBlockResponse.validator_updates`, triggered by block `H`, affect validation for blocks `H+1`, `H+2`, and `H+3`。Height `H+1`: `NextValidatorsHash` includes the new `validator_updates` value。看见 H+1 只改 Next，不是已经在 H+1 用新 `ValidatorsHash` 计票。看见 Next 纳入更新，不是已经 H+2 才生效那种已经换人。看见 H+1 头字段变了，不是已经 Finalize 当下换人（35 总则）就已经是同一句 interchangeable。
2. **看见高度 H+2 验证者集合变更才生效 / `ValidatorsHash` 才更新 / 看见 H+2 开始按新集合投票 不是已经在 H+1 换人，也不是已经 NextValidatorsHash 更新了就已经计票。**  
   官方写：Height `H+2`: The validator set change takes effect and `ValidatorsHash` is updated。看见 H+2 才生效，不是已经在 H+1 按新集合计票。看见 ValidatorsHash 更新，不是已经 NextValidatorsHash 那种只是头里承诺下一集合。看见新集合开始投票，不是已经 H 的 Finalize 回了 `validator_updates` 就已经改了集合（458 必须回四列）就已经是同一句 interchangeable。
3. **看见高度 H+3 的 `PrepareProposal` / `ProcessProposal` / `FinalizeBlock` 的 `*_last_commit` 才带上变更后的验证者集合 / 看见 H+3 last_commit 带新集合 不是已经在 H+1/H+2 的 `proposed_last_commit` / `decided_last_commit` 就已经是新集合，也不是已经 Process/Finalize 里 CommitInfo 立刻带新人。**  
   官方写：Height `H+3`: `*_last_commit` fields in `PrepareProposal`, `ProcessProposal`, and `FinalizeBlock` now include the altered validator set。看见 H+3 才带新 last_commit，不是已经 H+1 的 `ProcessProposalRequest.proposed_last_commit` 就是新集合。看见 altered validator set 进 last_commit，不是已经 H+2 的 `FinalizeBlockRequest.decided_last_commit` 就已经带新人 interchangeable。看见三门 last_commit 同步变，不是已经本头 LastCommit 就已经是本高 +2/3（363）。

怎样编 `ValidatorUpdate`、怎样从 store 装 CommitInfo、怎样算 NextValidatorsHash 是规范里的做法，本页不抄。集合更新必须写出哪一高度改哪一个哈希（35）是总则另一切片，Finalize 回包栏 validator_updates 已经在 H+1 换人（431）是 Response 栏另一切片，ConsensusParams H→H+1 立刻生效（333）是参数延迟另一切片，共识专题 [`worked-example-validator-delay.md`](../consensus/worked-example-validator-delay.md) 是四门外的总表，本页钉 FinalizeBlock Usage 这三句正式三事。

## 官方为什么这样拆

- **H+1 只更新 NextValidatorsHash ≠ 已经在 H+1 计票：** 官方把头里承诺下一集合和 ValidatorsHash 开始计票分开。
- **H+2 ValidatorsHash 才更新 ≠ 已经在 H+1 换人：** 官方把 Next 和生效计票分开。
- **H+3 last_commit 才带新集合 ≠ 已经 proposed/decided_last_commit 就是新集合：** 官方把三门 last_commit 延迟和 Process/Finalize 请求栏里的 commit 信息分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| H+1 NextValidatorsHash | 不是已经在 H+1 计票 | 不是集合更新 H+1/H+2/H+3 总则（35） |
| H+2 ValidatorsHash 才更新 | 不是已经在 H+1 换人 | 不是 Finalize 回包栏已经在 H+1 换人（431） |
| H+3 last_commit 带新集合 | 不是已经 proposed/decided_last_commit 就是新集合 | 不是 consensus_param_updates H→H+1 立刻生效（333） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Finalize 回了 validator_updates 就已经在 H+1 换人、Next 更新了就已经计票、last_commit 立刻带新集合」，必须分开 H+1 只更新 Next 是不是已经在 H+1 计票、H+2 ValidatorsHash 才生效是不是已经在 H+1 换人、H+3 last_commit 才带新集合是不是已经 proposed/decided_last_commit 就是新集合。可以跳过「看见 Next 更新了就已经计票」。不要另写怎样编 ValidatorUpdate 或解绑天数。

## 本页不抄

- 怎样编 `ValidatorUpdate`、怎样从 store 装 CommitInfo、怎样算 NextValidatorsHash。
- 集合更新必须写出哪一高度改哪一个哈希。那是不变量 35。
- Finalize 回包栏 validator_updates 已经在 H+1 换人。那是不变量 431。
- ConsensusParams H→H+1 立刻生效。那是不变量 333。
- FinalizeBlock 空更新保持当前值。那是不变量 458。
