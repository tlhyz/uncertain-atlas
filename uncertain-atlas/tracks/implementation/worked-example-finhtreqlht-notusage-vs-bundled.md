# 例：看见 `FinalizeBlockRequest.height` 是已决块的高度 / `FinalizeBlockRequest.time` 是已决块的时间戳 / 看见填了 height / time is not already Usage match the values from the header / 看见 Request height / time 栏 is not already FinalizeBlock height/time 对上拟议块头 bundled interchangeable / 已经 Usage 那种 match the values from the header interchangeable / 已经 Request height / time 栏 interchangeable

**层次**：实现 / FinalizeBlock Request height/time 栏 not Usage match 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage / Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Request height / time 栏 not Usage match 不是 FinalizeBlock height/time 对上拟议块头 bundled interchangeable / 不是已经 Usage 那种 match the values from the header interchangeable / 不是已经 Request height / time 栏 interchangeable」，不是 FinalizeBlock height/time 对上拟议块头 bundled（462），也不是 Finalize height/time match header not already verified（553），也不是 Finalize 请求栏单栏定义（422）。不要另写怎样对 height / time。

## 官方三件事

规范把 FinalizeBlock Request 表上 height / time 栏描述、Usage 里 height and time values match the values from the header、Finalize 和 Process 各自的 Request height / time 栏分开写成三件独立的实现事，不是「看见 Finalize 填了 height/time 就已经 Usage 那种对上了 interchangeable、已经验过票上时间 interchangeable、已经 ProcessProposalRequest.height / time interchangeable」一件事：

1. **看见 `FinalizeBlockRequest.height` 是已决块的高度 / `FinalizeBlockRequest.time` 是已决块的时间戳 / 看见填了 height / time is not already Usage match the values from the header / 看见 Request height / time 栏 is not already FinalizeBlock height/time 对上拟议块头 bundled（462） interchangeable / 已经 Usage 那种 match the values from the header interchangeable / 已经 Request height / time 栏 interchangeable，也不是已经 FinalizeBlockRequest.height 是已决块的高度 Request栏（422 余量） interchangeable / 已经 FinalizeBlockRequest.time 是已决块的时间戳 Request栏（422 余量） interchangeable / 已经 FinalizeBlockRequest.height 是已决块的高度就已经对上了拟议块头 interchangeable，也不是已经 FinalizeBlock height/time match header not already verified bundled（553 余量） interchangeable / 已经验过块头 interchangeable / 已经 When 里先验块头 interchangeable，也不是已经 Finalize 请求余栏 / 请求末栏 bundled（422 / 428 余量） interchangeable / 已经 hash height time interchangeable / 已经 decided_last_commit interchangeable，也不是已经 FinalizeBlock height/time 对上拟议块头 bundled（462 第三件事 / 555 余量） interchangeable / 已经 ProcessProposal height/time match interchangeable / 已经 ProcessProposalRequest.height / time interchangeable。**  
   官方 Request 表写：`height` 是已决块的高度；`time` 是已决块的时间戳。看见填了 height / time，不是已经 Usage 里 height and time values match the values from the header 那种已经对上了——462 bundled 第二件事常被写成「看见 Request 栏就已经 Usage match」，本页钉 Request height / time 栏 not Usage match 单句。看见有高度和时间戳栏，不是已经 FinalizeBlockRequest.height 是已决块的高度（422 余量） interchangeable——422 钉单栏 height 定义，本页钉 Request 栏 vs Usage match 边界。看见 Request height / time 栏，不是已经 Finalize height/time match header not already verified（553 余量） interchangeable——553 钉 Usage match not verified，本页钉 Request 栏描述 vs Usage match 单句。
2. **看见 Request height / time 栏 is not already verified vote timestamp / 看见填了 time 不是已经 ExtendVoteRequest.time 那种已经验过票上 Timestamp 不是已经 FinalizeBlock height/time 对上拟议块头 bundled（462） interchangeable / 已经验过票上时间 interchangeable / 已经 ExtendVoteRequest.time interchangeable，也不是已经票上 Timestamp 就已经验过 bundled（304 余量） interchangeable / 已经 Timestamp 验过 interchangeable / 已经冲突提案 interchangeable，也不是已经 Misbehavior.time 是 height 那一高已提交块的时间戳 bundled（372 余量） interchangeable / 已经验过这个时间 interchangeable / 已经定了奖惩 interchangeable，也不是已经 PrepareProposalRequest.time 是将要提议那块的时间戳 Request栏（426 余量） interchangeable / 已经对上了拟议块头 interchangeable / 已经 ProcessProposalRequest.time 是拟议块的时间戳 interchangeable，也不是已经 FinalizeBlock height/time match header not already verified bundled（553 余量） interchangeable / 已经 When 里先验块头 interchangeable / 已经 Usage match interchangeable，也不是已经 FinalizeBlockRequest.height 是已决块的高度 Request栏（422 余量） interchangeable / 已经对上了拟议块头 interchangeable。**  
   官方把 Request 表 time 栏描述和 ExtendVoteRequest.time / 票上 Timestamp 验过分开——462 bundled 常与 304 混成「填了 time 就已经验过票上时间」，本页钉 Request height / time 栏 not verified vote timestamp 单句。看见填了 time，不是已经票上 Timestamp 就已经验过（304 余量） interchangeable——304 钉 Timestamp 验过边界，本页钉 Finalize Request time 栏 单句。看见 Request time 栏，不是已经 Misbehavior.time 是 height 那一高已提交块的时间戳（372 余量） interchangeable——372 钉 Misbehavior time 栏，本页钉 Request height / time 栏 not verified 边界。
3. **看见 Request height / time 栏 is not already ProcessProposalRequest.height / time interchangeable / 看见有高度和时间戳栏不是已经 ProcessProposalRequest.height 是拟议块的高度 / ProcessProposalRequest.time 是拟议块的时间戳 interchangeable 不是已经 FinalizeBlock height/time 对上拟议块头 bundled（462） interchangeable / 已经 ProcessProposal height/time match interchangeable / 已经 ProcessProposalRequest.height / time interchangeable，也不是已经 ProcessProposal height/time 对上拟议块头 bundled（454 余量） interchangeable / 已经 Process height/time match header interchangeable / 已经头字段对上余量 bundled interchangeable，也不是已经 ProcessProposal Request height/time 栏 not Usage match bundled（551 余量） interchangeable / 已经 Usage 那种 match the values from the header interchangeable / 已经 419 / 420 单栏 interchangeable，也不是已经头字段对上余量 bundled（417 余量） interchangeable / 已经 Prepare 没有头哈希 interchangeable / 已经 Finalize height/time match interchangeable，也不是已经 FinalizeBlockRequest.height 是已决块的高度 Request栏（422 余量） interchangeable / 已经 FinalizeBlockRequest.time 是已决块的时间戳 Request栏 interchangeable / 已经 hash height time interchangeable，也不是已经 FinalizeBlock height/time 对上拟议块头 bundled（462 第三件事 / 555 余量） interchangeable / 已经 Finalize match header interchangeable / 已经 ProcessProposal height/time 对上拟议块头 interchangeable。**  
   官方把 Finalize Request 表 height / time 栏描述和 ProcessProposalRequest.height / time 栏描述、Usage 里 Finalize / Process match 分开——462 bundled 常与 454 混成「看见 Finalize Request 栏就已经 ProcessProposalRequest.height / time interchangeable」，本页钉 Request height / time 栏 not ProcessProposalRequest height/time interchangeable 单句。看见有 height / time 栏，不是已经 ProcessProposal height/time 对上拟议块头 bundled（454 余量） interchangeable——454 钉 Process Usage match，本页钉 Finalize Request 栏 vs Process Request 栏 边界。看见 Request height / time 栏，不是已经 ProcessProposal Request height/time 栏 not Usage match（551 余量） interchangeable——550 钉 Process Request 栏 vs Usage match，本页钉 Finalize Request 栏 not ProcessProposal interchangeable 单句。

怎样对 height、怎样对 time、怎样和 Process 请求栏对齐 是规范里的做法，本页不抄。FinalizeBlock height/time 对上拟议块头 bundled（462）、Finalize height/time match header not already verified（553）、Finalize 请求栏单栏定义（422）是另外那套，本页不抄。

## 官方为什么这样拆

- **Request height/time 栏 not Usage match ≠ FinalizeBlock height/time 对上拟议块头 bundled interchangeable：** 官方把 Request 表字段描述（已决块高度/时间戳）和 Usage match 语句分开。
- **Request height/time 栏 not verified vote timestamp ≠ 304 Timestamp verified interchangeable：** 官方把 Finalize Request time 栏和票上 Timestamp 验过分开。
- **Request height/time 栏 not ProcessProposalRequest height/time interchangeable ≠ 454 Process match interchangeable：** 官方把 Finalize 和 Process 的 Request height / time 栏描述分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Request height / time 栏 | 不是 already Usage match | 不是 Finalize height/time match header not verified（553） |
| Request time 栏 | 不是 already verified vote timestamp | 不是票上 Timestamp 就已经验过（304） |
| Request height / time 栏 | 不是 ProcessProposalRequest height/time interchangeable | 不是 ProcessProposal height/time 对上拟议块头（454） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock Request height/time 栏 not Usage match 正式三事，必须分开 Request height / time 栏 是不是 already Usage match interchangeable / 422 height 单栏 interchangeable、Request height / time 栏 是不是 already verified vote timestamp interchangeable / 304 Timestamp verified interchangeable、Request height / time 栏 是不是 already ProcessProposalRequest.height / time interchangeable / 454 Process match interchangeable。可以跳过「看见填了 height/time 就已经 Usage 那种对上了 interchangeable」。不要另写怎样对 height / time。

## 本页不抄

- 怎样对 height、怎样对 time、怎样和 Process 请求栏对齐。
- Finalize match header ≠ ProcessProposal height/time match interchangeable。那是不变量 555（462 item 3 余量）。
- Finalize height/time match header not already verified。那是不变量 553。
- Finalize 请求栏 / 请求余栏单栏定义。那是不变量 422 / 428。
