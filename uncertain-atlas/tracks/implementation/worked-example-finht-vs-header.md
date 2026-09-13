# 例：看见 Finalize 的 height / time 对上拟议块头不是已经验过块头；看见 FinalizeBlockRequest.height / FinalizeBlockRequest.time 是已决块高度和时间戳不是已经 Usage 那种 match header；看见 Finalize height/time match header 不是已经是 ProcessProposal height/time match interchangeable

**层次**：实现 / FinalizeBlock height/time 对上拟议块头正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage / Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Finalize 的 height / time 对上拟议块头不是已经验过块头 / FinalizeBlockRequest.height / time 是已决块高度和时间戳不是已经 Usage 那种 match header / Finalize height/time match header 不是已经是 ProcessProposal height/time match interchangeable」，不是头字段对上余量 bundled 三事，也不是 Finalize 请求栏 decided vs proposed 单栏定义，也不是 ProcessProposal height/time 对上拟议块头那套。不要另写怎样对 height / time。

## 官方三件事

规范把 Finalize 的 height / time 对上拟议块头、Request 表上 height / time 栏描述、Finalize Usage 里 match header 写成三件独立的实现事，不是「看见 Finalize 填了 height/time 就已经验过块头、已经对上了、已经是 Process match interchangeable」一件事：

1. **看见 Finalize 的 `height` / `time` 对上拟议块头 / 看见对上了 不是已经验过块头，也不是已经跑过 Process。**  
   官方写：The height and time values match the values from the header of the proposed block。看见对上了，不是已经 When 里收到带上头的 Proposal 会先验块头那种已经验过。看见 Finalize 这边 match header，不是已经 Process 调用之前就已经跑过 Process。看见 Usage 这句，不是已经 Prepare 和 Process / Finalize 同一套字段那种已经知道本头哈希。
2. **看见 `FinalizeBlockRequest.height` 是已决块的高度 / `FinalizeBlockRequest.time` 是已决块的时间戳 / 看见填了 height / time 不是已经 Usage 那种 match the values from the header，也不是已经是 ProcessProposalRequest.height / time interchangeable。**  
   官方 Request 表写：`height` 是已决块的高度；`time` 是已决块的时间戳。看见填了 height，不是已经 Usage 里 height and time values match the values from the header of the proposed block 那种已经对上了。看见填了 time，不是已经 PrepareProposalRequest.time 那种已经对上了拟议块头。看见有已决块高度和时间戳栏，不是已经头字段对上余量 bundled（417）就已经是同一句 interchangeable。
3. **看见 Finalize height / time match proposed block header / 看见 match header 不是已经是 ProcessProposal height/time match interchangeable，也不是已经知道本头哈希。**  
   官方写：The height and time values match the values from the header of the proposed block。看见 Finalize 这边 match，不是已经 ProcessProposal Usage 里 Process 的 height / time 对上拟议块头（454）就已经是同一句 interchangeable。看见拟议块头字段对上，不是已经 FinalizeBlockRequest.hash 是已决块的哈希那种已经知道本头哈希。看见 match header，不是已经 Finalize 含刚决定那块的字段（461）就已经是同一句 interchangeable。

怎样对 height、怎样对 time、怎样和 Process 请求栏对齐是规范里的做法，本页不抄。头字段对上余量 bundled 三事（417）是自己是提议者会先走 Prepare / Process height/time match 那套另一切片，Finalize 请求栏 decided vs proposed（422）是 decided_last_commit / height / txs 单栏定义，ProcessProposal height/time 对上拟议块头（454）是 Process Usage match 那套另一切片，本页不抄。

## 官方为什么这样拆

- **Finalize height/time match header ≠ 已经验过块头 / 已经跑过 Process：** 官方把 Finalize Usage 里 match 和 When 里先验块头分开。
- **Request height / time 栏 ≠ 已经 Usage 那种 match header：** 官方把 Request 表字段描述（已决块高度/时间戳）和 Usage match 语句分开。
- **Finalize match header ≠ 已经是 ProcessProposal height/time match interchangeable：** 官方把 Finalize 和 Process 的 height/time match 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Finalize height/time match header | 不是已经验过块头 | 不是收到带上头的提案会先验块头就已经跑过 Process（416） |
| Request height / time 栏 | 不是已经 Usage 那种 match header | 不是 FinalizeBlockRequest.height 是已决块的高度就已经对上了拟议块头（422） |
| Finalize match header | 不是已经是 ProcessProposal match interchangeable | 不是 ProcessProposal height/time 对上拟议块头（454） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Finalize 填了 height/time 就已经验过块头、已经对上了、已经是 Process match interchangeable」，必须分开 Finalize height/time match header 是不是已经验过块头、Request height / time 栏是不是已经 Usage 那种 match header、Finalize match header 是不是已经是 ProcessProposal height/time match interchangeable。可以跳过「看见 Finalize 填了 height/time 就已经验过块头」。不要另写怎样对 height / time。

## 本页不抄

- 怎样对 height、怎样对 time、怎样和 Process 请求栏对齐。
- 头字段对上余量 bundled 三事。那是不变量 417。
- Finalize 请求栏 decided vs proposed 单栏定义。那是不变量 422。
- ProcessProposal height/time 对上拟议块头。那是不变量 454。
- Finalize 含刚决定那块的字段。那是不变量 461。
