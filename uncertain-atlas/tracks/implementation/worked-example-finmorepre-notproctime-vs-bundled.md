# 例：看见 This includes the time the application and CometBFT take for processing the committed block / 看见包含应用和 CometBFT 处理已提交块的时间 is not already 本地 `timeout_commit` interchangeable / 已经 Previously timeout_commit in CometBFT config interchangeable；不是已经 FinalizeBlockResponse next_block_delay processing time / more precommits 正式三事 bundled（480） interchangeable / 已经 finmorepre bundled interchangeable

**层次**：实现 / FinalizeBlockResponse next_block_delay includes processing time not timeout_commit / wallclock 正式三事（480 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage `next_block_delay`。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「FinalizeBlockResponse next_block_delay includes processing time not timeout_commit / not wallclock 非确定（589） / not finmorepre bundled（480） interchangeable / not 611 notproctime interchangeable / not 432 finrespend interchangeable / not 52 post-commit nondet interchangeable」，不是 FinalizeBlockResponse next_block_delay processing time / more precommits 正式三事 bundled（480），也不是 next_block_delay 非确定 bundled（589），也不是 Finalize 回包末栏 bundled（432）。不要另写怎样填 next_block_delay、怎样抄规范 1s。

## 官方三件事

规范把 FinalizeBlock Usage 里 **This includes the time the application and CometBFT take for processing the committed block** 和「已经是本地 `timeout_commit` interchangeable / 已经是 depends on local wallclock / NTP 非确定 interchangeable / 已经是 finmorepre bundled interchangeable」分开写成三件独立的实现事，不是「看见 includes processing time 就已经 timeout_commit、就已经 wallclock 非确定、就已经 finmorepre bundled interchangeable」一件事：

1. **看见 This includes the time the application and CometBFT take for processing the committed block / 看见包含应用和 CometBFT 处理已提交块的时间 is not already 本地 `timeout_commit` interchangeable / 已经 Previously `timeout_commit` in CometBFT config interchangeable / 已经 replaces timeout_commit 就等于配置项 interchangeable / 47 timeout_commit interchangeable，也不是已经 FinalizeBlockResponse next_block_delay processing time / more precommits 正式三事 bundled（480） interchangeable / 611 notproctime interchangeable / 480 finmorepre interchangeable / 612 finmorepre bundled interchangeable / 432 finrespend interchangeable，也不是已经 Finalize 回包末栏 bundled（432 余量） interchangeable / 432 finrespend interchangeable / 432 item 3 next_block_delay interchangeable / 589 fndelay interchangeable / 385 ConsensusParams block interval interchangeable，也不是已经 post-commit 等待必须标非确定性 bundled（52 余量） interchangeable / 52 post-commit nondet interchangeable / 47 local timeout interchangeable / 589 item 1 Deterministic = No interchangeable。**  
   官方 Usage 写：how long CometBFT waits after committing a block, before starting the next height。**This includes the time the application and CometBFT take for processing the committed block**。看见 includes processing time，不是已经 Previously `timeout_commit` in CometBFT config 那种可以整段替换成配置项 interchangeable——480 bundled 第一件事常被写成「看见 processing time 就已经 timeout_commit interchangeable」，本页从 480 item 1 侧钉 not timeout_commit 单句。看见包含应用处理时间，不是已经 FinalizeBlockResponse.next_block_delay 是这块 Commit 后再开下一高的等待（432 item 3） interchangeable——432 钉回包末栏三栏，本页钉 480 item 1 第一件事。看见 processing committed block，不是已经 ConsensusParams.block 块间隔（385） interchangeable——385 钉 block 参数，本页钉 includes processing time 单句。
2. **看见 includes processing time / 看见包含应用和 CometBFT 处理已提交块的时间 is not already depends on local wallclock / NTP 那种非确定 interchangeable / 已经 next_block_delay Deterministic = No interchangeable / 589 fndelay interchangeable / 589 item 1 Deterministic = No interchangeable / 589 item 2 each node MAY interchangeable，也不是已经 FinalizeBlockResponse next_block_delay processing time / more precommits 正式三事 bundled（480） interchangeable / 611 notproctime interchangeable / 589 fndelay interchangeable / 476 finharddet interchangeable / 470 findet interchangeable，也不是已经 FinalizeBlockResponse next_block_delay 非确定 bundled（589 余量） interchangeable / 589 fndelay interchangeable / 589 item 2 wallclock interchangeable / 589 item 3 set to 0 interchangeable / 470 findet item 3 app_hash nondet interchangeable，也不是已经 FinalizeBlockResponse app_hash empty / hard-coded / MUST be deterministic bundled（476 余量） interchangeable / 476 finharddet interchangeable / 581 findet not replication interchangeable / 580 finddet not apphash interchangeable，也不是已经 FinalizeBlock When starts consensus for h+1 round 0 bundled（593 余量） interchangeable / 593 finh1 interchangeable / 589 next_block_delay slot interchangeable / 592 finunlock interchangeable。**  
   官方把 includes processing time 和 depends on local wallclock / NTP 非确定分开——480 item 1 常与 589 混成「看见 processing time 就已经 wallclock 非确定 interchangeable」，本页钉 not wallclock 非确定 单句。看见 includes processing time，不是已经 each node MAY provide a different value（589 item 2） interchangeable——589 钉 MAY / wallclock / NTP，本页钉 480 item 1 第二件事。看见 processing committed block，不是已经 app_hash MUST be deterministic 就代表整门非确定（470 / 476） interchangeable——470 钉 executes txs / app_hash / implementation MUST be deterministic，本页钉 not wallclock 单句。
3. **看见 includes processing time / 看见包含应用和 CometBFT 处理已提交块的时间 is not already finmorepre bundled（480） interchangeable / 已经 more precommits despite 2/3+ interchangeable / 已经 after committing before next height interchangeable / 480 finmorepre item 2 interchangeable / 480 finmorepre item 3 interchangeable，也不是已经 FinalizeBlockResponse next_block_delay processing time / more precommits 正式三事 bundled（480） interchangeable / 611 notproctime interchangeable / 480 finmorepre item 2 interchangeable / 480 finmorepre item 3 interchangeable / 362 +2/3 precommit interchangeable / 479 fintrigger interchangeable，也不是已经 In CometBFT terms, this interval gives the proposer a chance to receive some more precommits bundled（480 item 2 余量） interchangeable / 612 notmorepre interchangeable / 362 finwhen interchangeable / 479 fintrigger interchangeable / 610 notdecides interchangeable，也不是已经 how long CometBFT waits after committing before next height bundled（480 item 3 余量） interchangeable / 613 notaftercommit interchangeable / 589 set to 0 interchangeable / 385 block interval interchangeable / 593 finh1 interchangeable。**  
   官方把 480 finmorepre bundled 三事里的 includes processing time 和 more precommits / after committing before next height 分开——480 bundled 常与 item 2 / item 3 混成「看见 includes processing time 就已经 finmorepre bundled interchangeable」，本页钉 480 item 1 第三件事。看见 includes processing time，不是已经 more precommits despite 2/3+（480 item 2 余量） interchangeable——480 item 2 另钉 not decided / not 479 fintrigger，本页钉 item 1 单句。看见 processing committed block，不是已经 after committing before next height / set to 0（480 item 3 余量 / 589 item 3） interchangeable——480 item 3 另钉 not slot / not 1s constant，本页钉 not finmorepre bundled 单句。

怎样填 next_block_delay、怎样配 NTP、怎样从 timeout_commit 迁移是规范里的做法，本页不抄。FinalizeBlockResponse next_block_delay processing time / more precommits 正式三事 bundled（480）、more precommits despite 2/3+ not decided（480 item 2 余量）、after committing before next height not slot（480 item 3 余量）、next_block_delay 非确定 bundled（589）、Finalize 回包末栏 bundled（432）、post-commit 等待必须标非确定性（52）是另外那套，本页不抄。

## 官方为什么这样拆

- **includes processing time not timeout_commit ≠ 47 timeout_commit / 432 finrespend interchangeable：** 官方把 delay 包含的处理时间和配置项 timeout_commit 分开。
- **includes processing time not wallclock ≠ 589 fndelay / 470 findet interchangeable：** 官方把 480 item 1 和 depends on local wallclock / NTP 非确定分开。
- **includes processing time not finmorepre bundled ≠ more precommits / after committing interchangeable：** 官方把 480 item 1 和 item 2 / item 3 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| includes processing time | 不是 already timeout_commit | 不是 post-commit 非确定（52） |
| includes processing time | 不是 already wallclock 非确定 | 不是 next_block_delay 非确定（589） |
| includes processing time | 不是 already finmorepre bundled | 不是 more precommits（480 item 2） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse next_block_delay includes processing time not timeout_commit / wallclock 正式三事（480 余量），必须分开 includes processing time 是不是 already timeout_commit interchangeable / 47 / 432 finrespend interchangeable / 385 block interval interchangeable、includes processing time 是不是 already wallclock 非确定 interchangeable / 589 fndelay interchangeable / 470 findet interchangeable / 476 finharddet interchangeable、includes processing time 是不是 already finmorepre bundled interchangeable / 480 item 2 more precommits interchangeable / 480 item 3 after committing interchangeable / 362 +2/3 precommit interchangeable。可以跳过「看见 includes processing time 就已经 timeout_commit interchangeable」。不要另写怎样填 next_block_delay。不要把规范 1s 抄进不确定。

## 本页不抄

- 怎样填 next_block_delay、怎样配 NTP、怎样从 timeout_commit 迁移。
- FinalizeBlockResponse next_block_delay processing time / more precommits 正式三事 bundled。那是不变量 480。
- more precommits despite 2/3+ not decided。那是不变量 480 item 2 余量。
- after committing before next height not slot。那是不变量 480 item 3 余量。
- next_block_delay 非确定 bundled。那是不变量 589。
- Finalize 回包末栏 bundled。那是不变量 432。
- post-commit 等待必须标非确定性。那是不变量 52。
