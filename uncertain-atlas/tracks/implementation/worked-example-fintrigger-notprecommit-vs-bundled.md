# 例：看见 Precommit messages from 2f + 1 validators' voting power for round _r_, height _h_, precommitting the same block id(_v_) / 看见 2f+1 投票权对同一 id(_v_) precommit is not already +2/3 prevote 同一 id(_v_) 才 ExtendVote interchangeable / 已经 prevote 锁住 ExtendVote interchangeable；不是已经 FinalizeBlock When trigger Proposal block parts 2f+1 precommit 正式三事 bundled（479） interchangeable / 已经 fintrigger bundled interchangeable

**层次**：实现 / FinalizeBlock When trigger 2f+1 precommit not +2/3 prevote ExtendVote / not without all block parts 正式三事（479 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When preamble。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「FinalizeBlock When trigger 2f+1 precommit not +2/3 prevote ExtendVote / not without all block parts / not fintrigger bundled（479） interchangeable / not 609 notprecommit interchangeable / not 361 extendwhen interchangeable / not 608 notparts interchangeable」，不是 FinalizeBlock When trigger Proposal block parts 2f+1 precommit 正式三事 bundled（479），也不是 +2/3 prevote ExtendVote bundled（361），也不是 Proposal + all block parts not only hash（608）。不要另写怎样收块片、怎样数 2f+1。

## 官方三件事

规范把 FinalizeBlock When preamble 里 Precommit messages from 2f + 1 validators' voting power … precommitting the same block id(_v_) 和「已经是 +2/3 prevote 同一 id(_v_) 才 ExtendVote interchangeable / 已经是 +2/3 precommit 就可以没有 all block parts interchangeable / 已经是 fintrigger bundled interchangeable」分开写成三件独立的实现事，不是「看见 2f+1 precommit 就已经 prevote ExtendVote、就已经可以没有 all block parts、就已经 fintrigger bundled interchangeable」一件事：

1. **看见 Precommit messages from 2f + 1 validators' voting power for round _r_, height _h_, precommitting the same block id(_v_) / 看见 2f+1 投票权对同一 id(_v_) precommit is not already +2/3 prevote 同一 id(_v_) 才 ExtendVote interchangeable / 已经 prevote 锁住 ExtendVote interchangeable / 361 extendwhen interchangeable / 361 prevote ExtendVote bundled interchangeable，也不是已经 FinalizeBlock When trigger Proposal block parts 2f+1 precommit 正式三事 bundled（479） interchangeable / 609 notprecommit interchangeable / 479 fintrigger interchangeable / 361 extendwhen interchangeable / 513 extwhen broadcast interchangeable / 511 extwhen canonicalvote interchangeable，也不是已经 +2/3 prevote ExtendVote bundled（361 余量） interchangeable / 361 extendwhen interchangeable / 358 ExtendVote When interchangeable / 438 extwhen flow interchangeable / 520 preparewhen suggestvalidate interchangeable，也不是已经 ExtendVote When 正式流程 bundled（438 余量） interchangeable / 438 extwhen flow interchangeable / 361 item 2 CanonicalVote interchangeable / 361 item 3 Precommit broadcast interchangeable，也不是已经 PrepareProposal When +2/3 prevote 才 ExtendVote bundled（520 余量） interchangeable / 520 preparewhen suggestvalidate interchangeable / 519 preparewhen lateext interchangeable / 361 prevote ExtendVote interchangeable。**  
   官方 When 写：Precommit messages from 2f + 1 validators' voting power … precommitting the same block id(_v_)。看见 2f+1 投票权，不是已经 +2/3 prevote 锁住 ExtendVote（361）那种已经 interchangeable——479 bundled 第二件事常被写成「看见 2f+1 precommit 就已经 prevote ExtendVote interchangeable」，本页从 479 item 2 侧钉 not +2/3 prevote ExtendVote 单句。看见 precommitting the same block id(_v_)，不是已经 +2/3 prevote 同一 id(_v_) 才 ExtendVote（361） interchangeable——361 钉 prevote 锁住再 Extend，本页钉 479 item 2 第一件事。看见 Precommit 门槛，不是已经 ExtendVote When 正式流程（438） interchangeable——438 钉填进 CanonicalVoteExtension / 构造 Precommit，本页钉 609 item 2 单句。
2. **看见 2f+1 precommit same id(v) / 看见 Precommit from 2f+1 voting power is not already +2/3 precommit 就可以没有 all block parts interchangeable / 已经 partial block 就够 precommit interchangeable / 已经 Proposal + all block parts interchangeable / 608 notparts interchangeable，也不是已经 FinalizeBlock When trigger Proposal block parts 2f+1 precommit 正式三事 bundled（479） interchangeable / 609 notprecommit interchangeable / 479 fintrigger item 1 interchangeable / 608 notparts interchangeable / 428 finhash interchangeable / 472 Process guarantee interchangeable，也不是已经 FinalizeBlock When trigger Proposal + all block parts not only hash bundled（608 余量） interchangeable / 608 notparts interchangeable / 428 finhash interchangeable / 611 finwhenparts interchangeable / 473 finfill interchangeable，也不是已经 When calling FinalizeBlock Process guarantee bundled（472 余量） interchangeable / 472 finwhen interchangeable / 570 not every validator interchangeable / 563 not passed means ran Process interchangeable，也不是已经 Finalize 何时调用 bundled（362 余量） interchangeable / 362 finwhen item 1 +2/3 precommit interchangeable / 362 item 2 persist decision interchangeable / 466 executes block v interchangeable。**  
   官方把 2f+1 precommit 和 all block parts 分开——479 item 2 常与 608 混成「看见 2f+1 precommit 就已经可以没有 all block parts interchangeable」，本页钉 not without all block parts 单句。看见 Precommit 门槛，不是已经 Proposal + all block parts（608 / 479 item 1 余量） interchangeable——608 另钉 not only hash / not Process ran，本页钉 479 item 2 第二件事。看见 2f+1 precommit same id(v)，不是已经 Process guarantee（472） interchangeable——472 钉 When calling at least one non-byzantine has run Process，本页钉 not without all block parts 单句。
3. **看见 2f+1 precommit same id(v) / 看见 Precommit from 2f+1 voting power is not already fintrigger bundled（479） interchangeable / 已经 decides block v interchangeable / 已经 then decides block _v_ interchangeable / 362 +2/3 precommit interchangeable / 362 finwhen interchangeable，也不是已经 FinalizeBlock When trigger Proposal block parts 2f+1 precommit 正式三事 bundled（479） interchangeable / 609 notprecommit interchangeable / 479 fintrigger item 3 interchangeable / 478 finpersist interchangeable / 605 notpersist interchangeable / 606 notoutputs interchangeable / 607 notsync interchangeable，也不是已经 Finalize 何时调用 bundled（362 余量） interchangeable / 362 finwhen bundled interchangeable / 362 item 1 +2/3 precommit interchangeable / 362 item 2 persist decision interchangeable / 362 item 3 synchronous call interchangeable，也不是已经 FinalizeBlock When calls FinalizeBlock not persist outputs bundled（606 余量） interchangeable / 606 notoutputs interchangeable / 362 decides trigger interchangeable / 479 fintrigger interchangeable，也不是已经 FinalizeBlock When synchronous call not decides trigger bundled（607 余量） interchangeable / 607 notsync interchangeable / 362 finwhen interchangeable / 479 fintrigger interchangeable。**  
   官方把 479 fintrigger bundled 三事里的 2f+1 precommit 和 decides block v / finwhen 分开——479 bundled 常与 item 3 混成「看见 2f+1 precommit 就已经 fintrigger bundled interchangeable」，本页钉 479 item 2 第三件事。看见 Precommit 门槛，不是已经 then decides block _v_（479 item 3 余量 / 362） interchangeable——479 item 3 另钉 not at height h will Finalize / not persist outputs，本页钉 item 2 单句。看见 2f+1 precommit，不是已经 +2/3 precommit 决定再调 Finalize（362） interchangeable——362 钉 When 第 1–2 步 persist decision / calls FinalizeBlock，本页钉 not fintrigger bundled 单句。

怎样收块片、怎样数 2f+1、怎样落决定是规范里的做法，本页不抄。FinalizeBlock When trigger Proposal block parts 2f+1 precommit 正式三事 bundled（479）、Proposal + all block parts not only hash（608 / 479 item 1）、decides block v not at height h will Finalize（479 item 3 余量）、+2/3 prevote ExtendVote bundled（361）、Finalize 何时调用 bundled（362）、Process guarantee bundled（472）是另外那套，本页不抄。

## 官方为什么这样拆

- **2f+1 precommit not +2/3 prevote ExtendVote ≠ 361 extendwhen / prevote ExtendVote bundled interchangeable：** 官方把 Precommit 门槛和 Prevote/ExtendVote 锁住分开。
- **2f+1 precommit not without all block parts ≠ 608 notparts / 428 finhash interchangeable：** 官方把 479 item 2 和 Proposal + all block parts 分开。
- **2f+1 precommit not fintrigger bundled ≠ decides block v / 362 finwhen interchangeable：** 官方把 479 item 2 和 item 3 / 362 finwhen 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 2f+1 precommit same id(v) | 不是 already +2/3 prevote ExtendVote | 不是 prevote ExtendVote bundled（361） |
| 2f+1 precommit same id(v) | 不是 already without all block parts | 不是 Proposal + parts（608 / 479 item 1） |
| 2f+1 precommit same id(v) | 不是 already fintrigger bundled | 不是 decides block v（479 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When trigger 2f+1 precommit not +2/3 prevote ExtendVote / not without all block parts 正式三事（479 余量），必须分开 2f+1 precommit 是不是 already +2/3 prevote ExtendVote interchangeable / 361 extendwhen interchangeable / 438 extwhen flow interchangeable、2f+1 precommit 是不是 already without all block parts interchangeable / 608 notparts interchangeable / 428 finhash interchangeable / 472 Process guarantee interchangeable、2f+1 precommit 是不是 already fintrigger bundled interchangeable / 479 item 3 decides block v interchangeable / 362 finwhen interchangeable / 606 notoutputs interchangeable。可以跳过「看见 2f+1 precommit 就已经 prevote ExtendVote interchangeable」。不要另写怎样收块片。

## 本页不抄

- 怎样收块片、怎样数 2f+1、怎样落决定。
- FinalizeBlock When trigger Proposal block parts 2f+1 precommit 正式三事 bundled。那是不变量 479。
- Proposal + all block parts not only hash / Process ran。那是不变量 608（479 item 1 余量）。
- decides block v not at height h will Finalize。那是不变量 479 item 3 余量。
- +2/3 prevote ExtendVote bundled。那是不变量 361。
- Finalize 何时调用 bundled。那是不变量 362。
- Process guarantee bundled。那是不变量 472。
