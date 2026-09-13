# 例：看见 CometBFT will fill up all fields in FinalizeBlockRequest 不是已经 Prepare / Process 给过就不用再 Finalize；看见 even if already passed on via PrepareProposalRequest or ProcessProposalRequest 不是已经字段名对得上就代表已经跑过 Process；看见 all fields / 又填一遍 不是已经 decided_last_commit 和 proposed_last_commit 就可以混用

**层次**：实现 / FinalizeBlock fill all fields even if Prepare/Process passed 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「CometBFT will fill up all fields in FinalizeBlockRequest 不是已经 Prepare / Process 给过就不用再 Finalize / even if already passed on via PrepareProposalRequest or ProcessProposalRequest 不是已经字段名对得上就代表已经跑过 Process / all fields / 又填一遍 不是已经 decided 和 proposed 就可以混用」，不是 Finalize 时的 Process 保证 bundled 三事，也不是 FinalizeBlock 含刚决定那块字段 bundled 三事，也不是 Prepare 请求字段同一套那套。不要另写怎样写 FinalizeBlockRequest 各栏。

## 官方三件事

规范把 FinalizeBlock Usage 里 Currently / CometBFT will fill up all fields in `FinalizeBlockRequest` / even if they were already passed on via `PrepareProposalRequest` or `ProcessProposalRequest` 写成三件独立的实现事，不是「看见 Prepare / Process 已经给过就已经不用再 Finalize、已经字段名对得上就代表已经跑过 Process、decided 和 proposed 字段 interchangeable」一件事：

1. **看见 Currently, CometBFT will fill up all fields in `FinalizeBlockRequest` / 看见引擎会把 Finalize 请求全部字段填齐 不是已经 Prepare / Process 给过就不用再 Finalize，也不是已经交差。**  
   官方 Usage 写：Currently, CometBFT will fill up all fields in `FinalizeBlockRequest`, even if they were already passed on to the Application via `PrepareProposalRequest` or `ProcessProposalRequest`。看见 will fill up all fields，不是已经 Prepare / Process 传过就意味着已经不用再叫 Finalize interchangeable。看见 fill up all fields in FinalizeBlockRequest，不是已经 Finalize + Commit 那种已经交差。看见 Currently，不是已经 Contains the fields of the newly decided block（461 bundled 第一句）就已经是同一句 interchangeable——461 另钉 newly decided block 对象边界，本页只钉 fill all fields even if passed 这句。
2. **看见 even if they were already passed on to the Application via `PrepareProposalRequest` or `ProcessProposalRequest` / 看见即使 Prepare / Process 已经传过 不是已经字段名对得上就代表已经跑过 Process，也不是已经 Prepare 和 Process / Finalize 同一套字段就已经是刚决定那块的字段。**  
   官方写 even if they were already passed on via PrepareProposalRequest or ProcessProposalRequest。看见已经传过，不是已经 `PrepareProposalRequest` 的 `txs` / `misbehavior` / `height` / `time` / `next_validators_hash` / `proposer_address` 和 Process / Finalize 同一套（359）那种字段名对得上就代表已经跑过 Process interchangeable——359 钉 Prepare 请求字段，本页钉 Finalize Usage 这句 even if passed。看见已经经 Prepare 或 Process 给过，不是已经 newly decided block 的字段和 proposed block 字段 interchangeable（461 bundled 第二句）。看见 even if passed，不是已经可以套用先前 candidate 就不需要再填 Finalize 请求（460）那种已经 previously executed interchangeable。
3. **看见 all fields / 又填一遍 不是已经 `FinalizeBlockRequest.decided_last_commit` 和 `ProcessProposalRequest.proposed_last_commit` 就可以混用，也不是已经 Prepare / Process 传过就意味着 decided 和 proposed 语义 interchangeable。**  
   官方写 fill up **all** fields in FinalizeBlockRequest。看见全部字段齐，不是已经 decided_last_commit 是从刚决定那块拿到、proposed_last_commit 是从拟议块里的信息拿到那种可以混用 interchangeable（422）。看见又填一遍，不是已经 Finalize 时的 Process 保证 bundled（360）第二件事就已经是同一句 interchangeable——360 另钉 Process guarantee / 字段再填一遍 / 套用候选 bundled，本页只钉 fill all fields even if passed 专用切片。看见 all fields，不是已经 `syncing_to_height` 等 Finalize 专有栏就可以当成和 Prepare / Process 同一套字段名对上就够那种已经验完 interchangeable——Request 表把 decided_last_commit / syncing_to_height 等和 Prepare / Process 的 proposed_last_commit / local_last_commit 分开写。

怎样写 FinalizeBlockRequest 各栏、怎样和 Process 请求栏对齐、怎样缓存 Prepare / Process 数据是规范里的做法，本页不抄。Finalize 时的 Process 保证 bundled（360）是至少一名非拜占庭跑过 Process / 字段再填一遍 / 套用先前候选那套另一切片，FinalizeBlock 含刚决定那块字段 bundled（461）是 Contains newly decided block / proposed vs decided / fill all fields 那套另一切片，Prepare 请求字段同一套（359）是字段名对得上 / local_last_commit / 对上拟议头那套另一切片，Finalize 请求栏 decided vs proposed（422）是 decided_last_commit / height / txs 单栏定义那套另一切片，Finalize 套用候选（460）是 execute txs / apply candidate / previously executed 那套另一切片，本页不抄。

## 官方为什么这样拆

- **will fill up all fields in FinalizeBlockRequest ≠ 已经 Prepare / Process 给过就不用再 Finalize / 已经交差：** 官方把引擎再填 Finalize 请求和已经传过就不叫 Finalize 分开。
- **even if already passed via Prepare / Process ≠ 已经字段名对得上就代表已经跑过 Process / 已经是刚决定那块的字段：** 官方把 even if passed 和 Prepare 同一套字段名 / newly decided vs proposed 分开。
- **all fields / 又填一遍 ≠ decided 和 proposed 就可以混用：** 官方把 all fields 填齐和 decided_last_commit vs proposed_last_commit 语义分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| will fill up all fields in FinalizeBlockRequest | 不是已经 Prepare / Process 给过就不用再 Finalize | 不是 Finalize 时的 Process 保证 bundled（360） |
| even if already passed via Prepare / Process | 不是已经字段名对得上就代表已经跑过 Process | 不是 Prepare 请求字段同一套（359） |
| all fields / 又填一遍 | 不是已经 decided 和 proposed 就可以混用 | 不是 Finalize 请求栏 decided vs proposed（422） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Prepare / Process 已经给过就已经不用再 Finalize、已经字段名对得上就代表已经跑过 Process、decided 和 proposed 字段 interchangeable」，必须分开 will fill up all fields 是不是已经 Prepare / Process 给过就不用再 Finalize、even if already passed 是不是已经字段名对得上就代表已经跑过 Process、all fields / 又填一遍 是不是已经 decided 和 proposed 就可以混用。可以跳过「看见 Prepare / Process 已经给过就已经不用再 Finalize」。不要另写怎样写 FinalizeBlockRequest 各栏。

## 本页不抄

- 怎样写 FinalizeBlockRequest 各栏、怎样和 Process 请求栏对齐、怎样缓存 Prepare / Process 数据。
- Finalize 时的 Process 保证 bundled 三事。那是不变量 360。
- FinalizeBlock 含刚决定那块字段 bundled 三事。那是不变量 461。
- Prepare 请求字段同一套。那是不变量 359。
- Finalize 请求栏 decided vs proposed 单栏定义。那是不变量 422。
- Finalize 套用候选。那是不变量 460。
