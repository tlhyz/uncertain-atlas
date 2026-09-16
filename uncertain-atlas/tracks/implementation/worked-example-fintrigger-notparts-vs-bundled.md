# 例：看见 the Proposal message with block _v_ for a round _r_, along with all its block parts, from _q_ / 看见提议者 _q_ 的提案 _v_ 和全部块片 is not already only `FinalizeBlockRequest.hash` interchangeable / 已经只有 hash interchangeable；不是已经 FinalizeBlock When trigger Proposal block parts 2f+1 precommit 正式三事 bundled（479） interchangeable / 已经 fintrigger bundled interchangeable

**层次**：实现 / FinalizeBlock When trigger Proposal + all block parts not only hash / Process ran 正式三事（479 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When preamble。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「FinalizeBlock When trigger Proposal + all block parts not only hash / not Process ran / not fintrigger bundled（479） interchangeable / not 608 notparts interchangeable / not 428 finhash interchangeable / not 472 Process guarantee interchangeable」，不是 FinalizeBlock When trigger Proposal block parts 2f+1 precommit 正式三事 bundled（479），也不是 Finalize 请求 hash 栏（428），也不是 Process guarantee bundled（472）。不要另写怎样收块片、怎样数 2f+1。

## 官方三件事

规范把 FinalizeBlock When preamble 里 _p_ receives the Proposal message with block _v_ … along with all its block parts, from _q_ 和「已经是 only `FinalizeBlockRequest.hash` interchangeable / 已经是 Process 跑过 interchangeable / 已经是 fintrigger bundled interchangeable」分开写成三件独立的实现事，不是「看见 Proposal + all block parts 就已经 only hash、已经 Process 跑过、已经 fintrigger bundled interchangeable」一件事：

1. **看见 the Proposal message with block _v_ for a round _r_, along with all its block parts, from _q_ / 看见提议者 _q_ 的提案 _v_ 和全部块片 is not already only `FinalizeBlockRequest.hash` interchangeable / 已经 hash 栏对上 interchangeable / 已经收到部分块片就可以决定 interchangeable / 428 finhash interchangeable，也不是已经 FinalizeBlock When trigger Proposal block parts 2f+1 precommit 正式三事 bundled（479） interchangeable / 608 notparts interchangeable / 479 fintrigger interchangeable / 428 finhash interchangeable / 611 finwhenparts interchangeable，也不是已经 FinalizeBlockRequest.hash 不是已经 only hash bundled（428 余量） interchangeable / 428 finhash interchangeable / 473 finfill interchangeable / 407 finfields interchangeable，也不是已经 partial block / gossip partial block interchangeable / 已经任意节点流言 partial block interchangeable / 已经填了 hash 就代表收齐 interchangeable。**  
   官方 When 写：_p_ receives the Proposal message with block _v_ for a round _r_, along with all its block parts, from _q_, which is the proposer of round _r_, height _h_。看见 all its block parts，不是已经 only hash 栏对上——479 bundled 第一件事常被写成「看见 Proposal 就已经 only hash interchangeable」，本页从 479 item 1 侧钉 not only hash 单句。看见 from proposer _q_，不是已经任意节点流言 partial block interchangeable——本页钉 Proposal + parts 第一件事。看见 Proposal + parts，不是已经 partial block 就够决定 interchangeable——本页钉 608 item 1 单句。
2. **看见 Proposal + all block parts / 看见提议者 _q_ 的提案 _v_ 和全部块片 is not already ProcessProposal 跑过 interchangeable / 已经 at least one non-byzantine has run Process interchangeable / 472 Process guarantee interchangeable / 472 When calling interchangeable / 351 Process also on proposer interchangeable，也不是已经 FinalizeBlock When trigger Proposal block parts 2f+1 precommit 正式三事 bundled（479） interchangeable / 608 notparts interchangeable / 479 fintrigger interchangeable / 472 finwhen interchangeable / 570 not every validator interchangeable / 563 not passed means ran Process interchangeable，也不是已经 ProcessProposal 候选执行 bundled（452 余量） interchangeable / 452 candidate interchangeable / 311 candidate interchangeable / 460 fincand interchangeable / 584 apply candidate interchangeable，也不是已经 ProcessProposal 同步 bundled（354 余量） interchangeable / 354 processwhen synchronous interchangeable / 347 Process Accept interchangeable / 339 CheckTx weak filter interchangeable。**  
   官方把 Proposal + all block parts 和 ProcessProposal 跑过分开——479 item 1 常与 472 混成「看见 Proposal + parts 就已经 Process 跑过 interchangeable」，本页钉 not Process ran 单句。看见 Proposal + parts，不是已经 Process guarantee（472） interchangeable——472 钉 When calling at least one non-byzantine has run Process，本页钉 479 item 1 第二件事。看见 all block parts，不是已经 Process 回了 Accept 就代表已经收齐 interchangeable——347 钉 Process Accept，本页钉 not Process ran 单句。
3. **看见 Proposal + all block parts / 看见提议者 _q_ 的提案 _v_ 和全部块片 is not already fintrigger bundled（479） interchangeable / 已经 2f+1 precommit same id(v) interchangeable / 已经 +2/3 prevote ExtendVote interchangeable / 已经 decides block v interchangeable，也不是已经 FinalizeBlock When trigger Proposal block parts 2f+1 precommit 正式三事 bundled（479） interchangeable / 608 notparts interchangeable / 479 fintrigger item 2 interchangeable / 479 fintrigger item 3 interchangeable / 362 +2/3 precommit interchangeable / 361 prevote ExtendVote interchangeable，也不是已经 Finalize 何时调用 bundled（362 余量） interchangeable / 362 finwhen interchangeable / 478 finpersist interchangeable / 605 notpersist interchangeable / 606 notoutputs interchangeable / 607 notsync interchangeable，也不是已经 +2/3 prevote ExtendVote bundled（361 余量） interchangeable / 361 extendwhen interchangeable / 513 extwhen broadcast interchangeable / 511 extwhen canonicalvote interchangeable。**  
   官方把 479 fintrigger bundled 三事里的 Proposal + all block parts 和 2f+1 precommit / decides block v 分开——479 bundled 常与 item 2 / item 3 混成「看见 Proposal + parts 就已经 fintrigger bundled interchangeable」，本页钉 479 item 1 第三件事。看见 Proposal + parts，不是已经 2f+1 precommit same id(v)（479 item 2 余量） interchangeable——479 item 2 另钉 not +2/3 prevote ExtendVote / not precommit without all block parts，本页钉 item 1 单句。看见 all block parts，不是已经 then decides block _v_（479 item 3 余量 / 362） interchangeable——362 钉何时决定，本页钉 not fintrigger bundled 单句。

怎样收块片、怎样数 2f+1、怎样落决定是规范里的做法，本页不抄。FinalizeBlock When trigger Proposal block parts 2f+1 precommit 正式三事 bundled（479）、2f+1 precommit not +2/3 prevote ExtendVote（479 item 2 余量）、decides block v not at height h will Finalize（479 item 3 余量）、Finalize 请求 hash 栏（428）、Process guarantee bundled（472）、Finalize 何时调用 bundled（362）是另外那套，本页不抄。

## 官方为什么这样拆

- **Proposal + all block parts not only hash ≠ 428 finhash / partial block interchangeable：** 官方把收齐 Proposal 和全部块片与 only hash、部分块片分开。
- **Proposal + all block parts not Process ran ≠ 472 Process guarantee / 452 candidate interchangeable：** 官方把 Proposal + parts 和 ProcessProposal 跑过分开。
- **Proposal + all block parts not fintrigger bundled ≠ 2f+1 precommit / decides block v interchangeable：** 官方把 479 item 1 和 item 2 / item 3 / 362 finwhen 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Proposal + all block parts | 不是 already only hash | 不是 finhash（428） |
| Proposal + all block parts | 不是 already Process 跑过 | 不是 Process guarantee（472） |
| Proposal + all block parts | 不是 already fintrigger bundled | 不是 2f+1 precommit（479 item 2） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When trigger Proposal + all block parts not only hash / Process ran 正式三事（479 余量），必须分开 Proposal + all block parts 是不是 already only hash interchangeable / 428 finhash interchangeable / partial block interchangeable、Proposal + all block parts 是不是 already Process 跑过 interchangeable / 472 Process guarantee interchangeable / 452 candidate interchangeable / 354 processwhen synchronous interchangeable、Proposal + all block parts 是不是 already fintrigger bundled interchangeable / 479 item 2 2f+1 precommit interchangeable / 479 item 3 decides block v interchangeable / 362 finwhen interchangeable / 361 prevote ExtendVote interchangeable。可以跳过「看见 Proposal + parts 就已经 only hash interchangeable」。不要另写怎样收块片。

## 本页不抄

- 怎样收块片、怎样数 2f+1、怎样落决定。
- FinalizeBlock When trigger Proposal block parts 2f+1 precommit 正式三事 bundled。那是不变量 479。
- 2f+1 precommit not +2/3 prevote ExtendVote。那是不变量 479 item 2 余量。
- decides block v not at height h will Finalize。那是不变量 479 item 3 余量。
- Finalize 请求 hash 栏。那是不变量 428。
- Process guarantee bundled。那是不变量 472。
- Finalize 何时调用 bundled。那是不变量 362。
