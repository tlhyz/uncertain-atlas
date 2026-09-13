# 例：看见 Misbehavior.height 是过错发生的高度不是已经 Prepare/Process 请求 height；看见 Misbehavior.time 是那一高已提交块的时间戳不是已经验过票上 Timestamp；看见 height 和 time 一起不是已经定了奖惩

**层次**：实现 / Misbehavior height/time 栏正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Misbehavior Fields。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「Misbehavior.height 是过错发生的高度不是已经 Prepare/Process 请求 height / Misbehavior.time 是那一高已提交块的时间戳不是已经验过票上 Timestamp / height 和 time 一起不是已经定了奖惩」，不是 Misbehavior 结构栏 type/height/time/total_voting_power 那套已经罚没，也不是请求 misbehavior 列表就已经定奖惩。不要另写怎样填 Misbehavior height/time 栏。

## 官方三件事

规范把 Misbehavior 里 `height` 和 `time` 栏写成三件独立的实现事，不是「看见 Misbehavior 里填了 height/time 就已经验过时间、已经对拟议头、已经定了奖惩」一件事：

1. **看见 Misbehavior.height 是过错发生的高度 / 看见填了 height 不是已经 PrepareProposalRequest.height / ProcessProposalRequest.height 那种将要提议或拟议块高度，也不是已经验过块头。**  
   官方写：`height` is Height when the offense occurred。看见能指过错发生在哪一高，不是已经 Prepare / Process / Finalize 请求里 `height` 对上拟议头那种已经知道本头。看见有高度数字，不是已经 VerifyVoteExtensionRequest.height 那种用来对一下的块高度 interchangeable。
2. **看见 Misbehavior.time 是 height 那一高已提交块的时间戳 / 看见填了 time 不是已经验过票上 Timestamp，也不是已经是 PrepareProposalRequest.time / ProcessProposalRequest.time 那种拟议块时间戳 interchangeable。**  
   官方写：`time` is Timestamp of the block that was committed at height `height`。看见能指那一高已提交块的时间，不是已经票上 Timestamp 验过。看见有时间戳，不是已经 ExtendVoteRequest.time 那种扩展要指的拟议块时间 interchangeable。
3. **看见 Misbehavior.height 和 time 一起 / 看见对上了 height 和 time 不是已经定了奖惩，也不是已经 slashed。**  
   官方把 height 和 time 配成「过错发生在哪一高、那一高已提交块的时间」。看见两个字段都在，不是已经 Finalize 可以用 `decided_last_commit` 和 `misbehavior` 定奖惩那种已经交差。看见对上了，不是已经证据上链就罚没。

怎样填 Misbehavior.height/time、怎样从 evidence 编过错高度和时间、怎样和请求栏对齐是规范里的做法，本页不抄。Misbehavior 结构栏 type/height/time/total_voting_power 是不变量 372 的另一切片，Misbehavior.validator 是不变量 448，Prepare/Process/Finalize 请求 misbehavior 列表是不变量 413/420/428，本页不抄。

## 官方为什么这样拆

- **Misbehavior.height 是过错发生的高度 ≠ 已经是 Prepare/Process 请求 height：** 官方把 offense height 和将要提议/拟议块高度分开。
- **Misbehavior.time 是那一高已提交块的时间戳 ≠ 已经验过票上 Timestamp：** 官方把 committed-at-height 时间和票上时间分开。
- **height + time 一起 ≠ 已经定了奖惩 / 已经 slashed：** 官方把过错时空信息和已经罚没分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Misbehavior.height | 不是已经 Prepare/Process 请求 height | 不是 Misbehavior 结构栏就已经罚没（372） |
| Misbehavior.time | 不是已经验过票上 Timestamp | 不是票上 Timestamp 就已经验过（304） |
| height + time 一起 | 不是已经定了奖惩 | 不是 misbehavior 列表就已经定奖惩（413） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Misbehavior 里填了 height/time 就已经验过时间、已经对拟议头、已经定了奖惩」，必须分开 Misbehavior.height 是不是已经 Prepare/Process 请求 height、Misbehavior.time 是不是已经验过票上 Timestamp、height 和 time 一起是不是已经定了奖惩。可以跳过「看见 Misbehavior 里填了 height/time 就已经验过时间」。不要另写怎样填 Misbehavior height/time 栏。

## 本页不抄

- 怎样填 Misbehavior.height/time、怎样从 evidence 编过错高度和时间、怎样和请求栏对齐。
- Misbehavior.type / total_voting_power。那是不变量 372 的 Misbehavior 结构其它栏。
- Misbehavior.validator。那是不变量 448。
- misbehavior 列表就已经定奖惩。那是不变量 413 / 420 / 428 的请求栏。
- 票上 Timestamp 就已经验过。那是不变量 304。
