# 例：看见 OfferSnapshot Result REJECT_FORMAT 是拒掉这种 format、换一份不是已经是拒掉这份；看见 OfferSnapshot Result REJECT_SENDER 是拒掉送来这份的所有人、换一份不是已经拒了人；看见 OfferSnapshot Result ABORT 是中止装回、不再试别份不是已经换一份

**层次**：实现 / OfferSnapshot 结果枚举。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) OfferSnapshot Result。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「OfferSnapshot Result REJECT_FORMAT 是拒掉这种 format、换一份不是已经是拒掉这份 / OfferSnapshot Result REJECT_SENDER 是拒掉送来这份的所有人、换一份不是已经拒了人 / OfferSnapshot Result ABORT 是中止装回、不再试别份不是已经换一份」，不是 ApplySnapshotChunk Result REJECT_SNAPSHOT 就已经是拒掉这份，也不是 Offer 收下就已经装完。不要另写怎样写 OfferSnapshot 结果枚举。

## 官方三件事

规范把 OfferSnapshot Result `REJECT_FORMAT` 是拒掉这种 format、换一份、`REJECT_SENDER` 是拒掉送来这份的所有人、换一份、`ABORT` 是中止装回、不再试别份写成三件独立的实现事，不是「看见回了 OfferSnapshot 结果枚举就已经是拒掉这份、已经拒了人、已经换一份」一件事：

1. **看见 OfferSnapshot Result `REJECT_FORMAT` 是拒掉这种 format、换一份 / 看见回了 REJECT_FORMAT 不是已经是拒掉这份，也不是已经齐。**  
   官方写：`REJECT_FORMAT` 是拒掉这种 `format`，换一份。看见回了 REJECT_FORMAT，不是已经是 ApplySnapshotChunk Result `REJECT_SNAPSHOT` 那种拒掉这份、换一份。看见能换一份，不是已经齐。看见能回，不是已经交差。
2. **看见 OfferSnapshot Result `REJECT_SENDER` 是拒掉送来这份的所有人、换一份 / 看见回了 REJECT_SENDER 不是已经拒了人，也不是已经能接着装。**  
   官方写：`REJECT_SENDER` 是拒掉送来这份的所有人，换一份。看见回了 REJECT_SENDER，不是已经 `reject_senders` 不论 Result 都拒这些人。看见能换一份，不是已经能接着装。看见能回，不是已经交差。
3. **看见 OfferSnapshot Result `ABORT` 是中止装回、不再试别份 / 看见回了 ABORT 不是已经换一份，也不是已经装完。**  
   官方写：`ABORT` 是中止装回，不再试别份。看见回了 ABORT，不是已经拉失败换一份就已经能接着装。看见能中止，不是已经装完。看见能回，不是已经交差。

怎样写 OfferSnapshot 结果枚举、怎样挑 REJECT_FORMAT、怎样挑 REJECT_SENDER 是规范里的做法，本页不抄。ApplySnapshotChunk Result REJECT_SNAPSHOT 就已经是拒掉这份是不变量 398，本页不抄。

## 官方为什么这样拆

- **OfferSnapshot Result REJECT_FORMAT 是拒掉这种 format、换一份 ≠ 已经是拒掉这份：** 官方把拒掉这种 format 和拒掉这份分开。
- **OfferSnapshot Result REJECT_SENDER 是拒掉送来这份的所有人、换一份 ≠ 已经拒了人：** 官方把拒掉送来这份的所有人和不论 Result 都拒这些人分开。
- **OfferSnapshot Result ABORT 是中止装回、不再试别份 ≠ 已经换一份：** 官方把中止装回和拉失败换一份分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| OfferSnapshot Result REJECT_FORMAT 是拒掉这种 format、换一份 | 不是已经是拒掉这份 | 不是 ApplySnapshotChunk Result REJECT_SNAPSHOT 就已经是拒掉这份（398） |
| OfferSnapshot Result REJECT_SENDER 是拒掉送来这份的所有人、换一份 | 不是已经拒了人 | 不是 reject_senders 不论 Result 都拒这些人就已经能接着装（378） |
| OfferSnapshot Result ABORT 是中止装回、不再试别份 | 不是已经换一份 | 不是拉失败换一份就已经能接着装（321） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见回了 OfferSnapshot 结果枚举就已经是拒掉这份、已经拒了人、已经换一份」，必须分开 OfferSnapshot Result REJECT_FORMAT 是拒掉这种 format、换一份是不是已经是拒掉这份、OfferSnapshot Result REJECT_SENDER 是拒掉送来这份的所有人、换一份是不是已经拒了人、OfferSnapshot Result ABORT 是中止装回、不再试别份是不是已经换一份。可以跳过「看见回了 OfferSnapshot 结果枚举就已经是拒掉这份」。不要另写怎样写 OfferSnapshot 结果枚举。

## 本页不抄

- 怎样写 OfferSnapshot 结果枚举、怎样挑 REJECT_FORMAT、怎样挑 REJECT_SENDER。
- ApplySnapshotChunk Result REJECT_SNAPSHOT 就已经是拒掉这份。那是不变量 398。
- reject_senders 不论 Result 都拒这些人就已经能接着装。那是不变量 378。
- 拉失败换一份就已经能接着装。那是不变量 321。
