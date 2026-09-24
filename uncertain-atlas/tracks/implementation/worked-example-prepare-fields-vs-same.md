# 例：看见 Prepare 和 Process / Finalize 同一套字段不是已经跑过 Process；看见 local_last_commit 是上一高度的预提交带扩展不是已经是本高度刚签的扩展；看见 height / time / proposer_address 对上拟议头不是已经知道本头哈希

**层次**：实现 / Prepare 请求字段。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「Prepare 和 Process / Finalize 同一套字段不是已经跑过 Process / local_last_commit 是上一高度的预提交带扩展不是已经是本高度刚签的扩展 / height / time / proposer_address 对上拟议头不是已经知道本头哈希」，不是 Process 也会在提议者那边叫，也不是到了 H 就已经 Prepare 带了扩展。不要另写怎样填 Prepare 请求字段。359 prepare-fields vs same bundled unbundling 启动（830）；精读 [`worked-example-prepfields-notprocess-vs-bundled.md`](worked-example-prepfields-notprocess-vs-bundled.md)（不变量 830 item 1）。

## 官方三件事

规范把 Prepare 请求里那几列和 Process / Finalize 同一套、`local_last_commit` 是上一高度预提交带扩展、`height` / `time` / `proposer_address` 对上拟议头写成三件独立的实现事，不是「看见字段名对得上就已经跑过 Process、已经是本高度刚签的扩展、已经知道本头哈希」一件事：

1. **看见 `txs` / `misbehavior` / `height` / `time` / `next_validators_hash` / `proposer_address` 和 Process / Finalize 同一套 / 看见字段名对得上 不是已经跑过 Process，也不是已经 Finalize。**  
   官方写：`PrepareProposalRequest` 的 `txs`、`misbehavior`、`height`、`time`、`next_validators_hash`、`proposer_address` 和 `ProcessProposalRequest`、`FinalizeBlockRequest` 是同一套。看见字段名对得上，不是已经叫过 Process。看见同一套，不是已经 Finalize。看见请求在，不是已经交差。
2. **看见 `local_last_commit` 是上一高度的预提交带扩展 / 看见有上一高的票 不是已经是本高度刚签的扩展，也不是已经到了 H 就已经 Prepare 带了扩展。**  
   官方写：`local_last_commit` 是上一高度的预提交，包括促成上一块决定的那些，以及对应的投票扩展。看见有上一高的票，不是已经是本高度刚签的 *e*。看见带了扩展，不是已经到了 H 就已经 Prepare 带了扩展。看见能用上一高，不是已经交差。
3. **看见 `height` / `time` / `proposer_address` 对上拟议头 / 看见对得上 不是已经知道本头哈希，也不是已经是候选已经是 ExecuteTxState。**  
   官方写：这三列对上拟议块头里的值。看见对得上，不是已经有本头哈希。看见头上有这些，不是已经是 ExecuteTxState。看见拟议头，不是已经交差。

怎样填 Prepare 请求字段、怎样读 `local_last_commit`、怎样对头是规范里的做法，本页不抄。Process 也会在提议者那边叫是不变量 351，本页不抄。

## 官方为什么这样拆

- **Prepare 和 Process / Finalize 同一套字段 ≠ 已经跑过 Process：** 官方把同一套字段和已经叫过分开。
- **local_last_commit 是上一高度的预提交带扩展 ≠ 已经是本高度刚签的扩展：** 官方把上一高和本高分开。
- **height / time / proposer_address 对上拟议头 ≠ 已经知道本头哈希：** 官方把这三列和对上本头哈希分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Prepare 和 Process / Finalize 同一套字段 | 不是已经跑过 Process | 不是 Process 也会在提议者那边叫就已经不用再 Process（351） |
| local_last_commit 是上一高度的预提交带扩展 | 不是已经是本高度刚签的扩展 | 不是到了 H 就已经 Prepare 带了扩展（330） |
| height / time / proposer_address 对上拟议头 | 不是已经知道本头哈希 | 不是候选已经是 ExecuteTxState（311） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见字段名对得上就已经跑过 Process、已经是本高度刚签的扩展、已经知道本头哈希」，必须分开 Prepare 和 Process / Finalize 同一套字段是不是已经跑过 Process、local_last_commit 是上一高度的预提交带扩展是不是已经是本高度刚签的扩展、height / time / proposer_address 对上拟议头是不是已经知道本头哈希。可以跳过「看见字段名对得上就已经跑过 Process」。不要另写怎样填 Prepare 请求字段。359 prepare-fields vs same bundled unbundling 启动（830）。

## 本页不抄

- 怎样填 Prepare 请求字段、怎样读 `local_last_commit`、怎样对头。
- Process 也会在提议者那边叫就已经不用再 Process。那是不变量 351。
- 到了 H 就已经 Prepare 带了扩展。那是不变量 330。
- 候选已经是 ExecuteTxState。那是不变量 311。
