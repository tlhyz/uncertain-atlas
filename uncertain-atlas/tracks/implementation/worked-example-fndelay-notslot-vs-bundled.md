# 例：看见 `FinalizeBlockResponse.next_block_delay` is a non-deterministic field / Response 表 Deterministic = No / 看见非确定 is not already 槽位 interchangeable / 已经 ConsensusParams.block 块间隔 interchangeable / 已经是本地 `timeout_commit` interchangeable；不是已经 FinalizeBlockResponse next_block_delay 非确定正式三事 bundled（589） interchangeable / 已经 fndelay bundled interchangeable

**层次**：实现 / FinalizeBlockResponse next_block_delay Deterministic = No not slot / not finality / not timeout_commit 正式三事（589 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Response / Usage `next_block_delay`。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「FinalizeBlockResponse next_block_delay Deterministic = No not slot / not finality / not timeout_commit 正式三事（589 余量）/ not 617 notslot interchangeable / not 385 block interval interchangeable / not 47 timeout_commit interchangeable / not 480 finmorepre interchangeable / not 618 notwallclock interchangeable / not 619 notsetzero interchangeable」，不是 FinalizeBlockResponse next_block_delay 非确定正式三事 bundled（589），也不是 processing time / more precommits / after committing bundled（480），也不是共识层 ADR 精读。不要另写怎样填 next_block_delay、怎样抄规范 1s。

## 官方三件事

规范把 `FinalizeBlockResponse.next_block_delay` Response 表 **Deterministic = No** / Usage 里 non-deterministic field 和「已经是槽位 interchangeable / 已经是 finality interchangeable / 已经是 timeout_commit interchangeable / 已经是 fndelay bundled interchangeable」分开写成三件独立的实现事，不是「看见 Deterministic = No 就已经槽位、就已经 finality、就已经 timeout_commit interchangeable」一件事：

1. **看见 `FinalizeBlockResponse.next_block_delay` is a non-deterministic field / Response 表 Deterministic = No / 看见非确定 is not already 槽位 interchangeable / 已经 ConsensusParams.block 块间隔 interchangeable / 385 block interval interchangeable / 593 finh1 slot interchangeable / 52 post-commit nondet slot interchangeable，也不是已经 FinalizeBlockResponse next_block_delay 非确定正式三事 bundled（589） interchangeable / 617 notslot interchangeable / 589 fndelay interchangeable / 480 finmorepre interchangeable / 611 notproctime interchangeable，也不是已经 FinalizeBlockResponse next_block_delay after committing before next height not slot bundled（480 item 3 余量 / 613） interchangeable / 613 notaftercommit interchangeable / 589 fndelay slot interchangeable / 385 block interval interchangeable / 593 finh1 interchangeable，也不是已经 post-commit 等待必须标非确定性 bundled（52 余量） interchangeable / 52 post-commit nondet interchangeable / 47 local timeout interchangeable / 589 next_block_delay slot interchangeable / 385 ConsensusParams block interval interchangeable，也不是已经 FinalizeBlock When starts consensus for h+1 round 0 bundled（593 余量） interchangeable / 593 finh1 interchangeable / 589 fndelay interchangeable / 592 finunlock interchangeable。**  
   官方 Response 表写：`next_block_delay` 列 **Deterministic = No**。Usage 写：`FinalizeBlockResponse.next_block_delay` is a **non-deterministic field**。看见 Deterministic = No，不是已经 `ConsensusParams.block` 块间隔（385） interchangeable——589 bundled 第一件事常被写成「看见 non-deterministic field 就已经槽位 interchangeable」，本页从 589 item 1 侧钉 not slot 单句。看见 non-deterministic field，不是已经 post-commit 等待必须标非确定性（52）那种高层产品门禁 interchangeable——52 钉高层标签，本页钉 Response / Usage 对象边界。看见 replaces Previously `timeout_commit`，不是已经 includes processing time / more precommits（480）就已经是同一句 interchangeable——480 另钉 processing time / more precommits / after committing，本页钉 589 item 1 第一件事。
2. **看见 `FinalizeBlockResponse.next_block_delay` Deterministic = No / 看见非确定 is not already 已经 finality interchangeable / 已经决定 interchangeable / 362 +2/3 precommit interchangeable / 362 finwhen interchangeable / 610 notdecides interchangeable / 33 four gates interchangeable，也不是已经 FinalizeBlockResponse next_block_delay 非确定正式三事 bundled（589） interchangeable / 617 notslot interchangeable / 589 fndelay interchangeable / 613 notaftercommit interchangeable / 612 notmorepre interchangeable，也不是已经 Set to 0 when all precommits and block processed bundled（589 item 3 余量 / 619） interchangeable / 619 notsetzero interchangeable / 589 item 3 set to 0 interchangeable / 480 finmorepre item 3 interchangeable / 613 notaftercommit interchangeable，也不是已经 FinalizeBlock When trigger decides block v not at height h will Finalize bundled（610 余量） interchangeable / 610 notdecides interchangeable / 479 fintrigger interchangeable / 362 finwhen interchangeable / 601 notsettled interchangeable，也不是已经 FinalizeBlockResponse next_block_delay more precommits despite 2/3+ not decided bundled（612 余量） interchangeable / 612 notmorepre interchangeable / 362 +2/3 precommit interchangeable / 479 fintrigger interchangeable。**  
   官方把 Deterministic = No 和已经 finality / 已经决定分开——589 item 1 常与 589 item 3 混成「看见 non-deterministic field 就已经 finality interchangeable」，本页钉 not finality 单句。看见 Deterministic = No，不是已经 +2/3 precommit 决定就已经 finality interchangeable——362 钉 When 触发，本页钉 589 item 1 第二件事。看见 non-deterministic field，不是已经 Set to 0 when all precommits and block processed（589 item 3 余量 / 619） interchangeable——619 另钉 not block interval / not decided，本页钉 not finality 单句。
3. **看见 `FinalizeBlockResponse.next_block_delay` Deterministic = No / 看见非确定 is not already fndelay bundled（589） interchangeable / 已经 each node MAY provide a different value interchangeable / 已经 wallclock / NTP 非确定 interchangeable / 589 fndelay item 2 interchangeable / 589 fndelay item 3 interchangeable / 618 notwallclock interchangeable / 619 notsetzero interchangeable，也不是已经 FinalizeBlockResponse next_block_delay 非确定正式三事 bundled（589） interchangeable / 617 notslot interchangeable / 618 notwallclock interchangeable / 619 notsetzero interchangeable / 470 findet interchangeable / 476 finharddet interchangeable，也不是已经 each node MAY provide a different value / depends on local processing bundled（589 item 2 余量 / 618） interchangeable / 618 notwallclock interchangeable / 470 findet interchangeable / 476 finharddet interchangeable / 581 findet not replication interchangeable，也不是已经 Set to 0 when all precommits and block processed bundled（589 item 3 余量 / 619） interchangeable / 619 notsetzero interchangeable / 613 notaftercommit interchangeable / 480 finmorepre item 3 interchangeable / 385 block interval interchangeable，也不是已经 FinalizeBlockResponse next_block_delay includes processing time not timeout_commit bundled（611 余量） interchangeable / 611 notproctime interchangeable / 47 timeout_commit interchangeable / 432 finrespend interchangeable / 480 finmorepre item 1 interchangeable。**  
   官方把 589 fndelay bundled 三事里的 Deterministic = No 和 each node MAY / wallclock / Set to 0 分开——589 bundled 常与 item 2 / item 3 混成「看见 Deterministic = No 就已经 fndelay bundled interchangeable」，本页钉 589 item 1 第三件事。看见 Deterministic = No，不是已经 each node MAY provide a different value（589 item 2 余量 / 618） interchangeable——618 另钉 not app_hash MUST be deterministic / not 整门非确定，本页钉 item 1 单句。看见 non-deterministic field，不是已经 Previously `timeout_commit` in CometBFT config（47 / 611） interchangeable——611 另钉 not timeout_commit / not wallclock，本页钉 not fndelay bundled 单句。

怎样填 next_block_delay、怎样从 timeout_commit 迁移、怎样配 NTP 是规范里的做法，本页不抄。FinalizeBlockResponse next_block_delay 非确定正式三事 bundled（589）、each node MAY / wallclock not app_hash MUST be deterministic（589 item 2 余量 / 618）、Set to 0 not decided / block interval（589 item 3 余量 / 619）、processing time / more precommits / after committing（480）、Finalize 回包末栏 bundled（432）、FinalizeBlock Usage determinism bundled（470）、post-commit 等待必须标非确定性（52）是另外那套，本页不抄。

## 官方为什么这样拆

- **next_block_delay Deterministic = No not slot ≠ 385 block interval / 593 finh1 / 52 post-commit nondet interchangeable：** 官方把 Response 表非确定列和块间隔 / 槽位参数分开。
- **Deterministic = No not finality ≠ 589 set to 0 / 362 finwhen / 613 notaftercommit interchangeable：** 官方把 589 item 1 和已经决定 / set to 0 分开。
- **Deterministic = No not fndelay bundled ≠ 618 notwallclock / 619 notsetzero / 611 notproctime interchangeable：** 官方把 589 item 1 和 item 2 / item 3 / 480 finmorepre 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| next_block_delay Deterministic = No | 不是 already 槽位 | 不是 block interval（385） |
| next_block_delay Deterministic = No | 不是 already finality | 不是 set to 0（589 item 3 / 619） |
| next_block_delay Deterministic = No | 不是 already fndelay bundled | 不是 MAY / wallclock（589 item 2 / 618） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse next_block_delay Deterministic = No not slot / not finality / not timeout_commit 正式三事（589 余量），必须分开 Deterministic = No 是不是 already 槽位 interchangeable / 385 block interval interchangeable / 593 finh1 interchangeable / 52 post-commit nondet interchangeable、Deterministic = No 是不是 already finality interchangeable / 362 finwhen interchangeable / 610 notdecides interchangeable / 619 notsetzero interchangeable、Deterministic = No 是不是 already fndelay bundled interchangeable / 618 notwallclock interchangeable / 619 notsetzero interchangeable / 611 notproctime interchangeable / 47 timeout_commit interchangeable。可以跳过「看见 Deterministic = No 就已经槽位 interchangeable」。不要另写怎样填 next_block_delay。不要把规范 Set to constant 1s 抄进不确定。

## 本页不抄

- 怎样填 next_block_delay、怎样从 timeout_commit 迁移、怎样配 NTP。
- FinalizeBlockResponse next_block_delay 非确定正式三事 bundled。那是不变量 589。
- each node MAY / wallclock not app_hash MUST be deterministic。那是不变量 589 item 2 余量 / 618。
- Set to 0 not decided / block interval。那是不变量 589 item 3 余量 / 619。
- processing time / more precommits / after committing。那是不变量 480。
- Finalize 回包末栏 bundled。那是不变量 432。
- FinalizeBlock Usage determinism bundled。那是不变量 470。
- post-commit 等待必须标非确定性。那是不变量 52。
- 共识层 next_block_delay 精读（ADR / 发布线）。那是 [`../consensus/worked-example-next-block-delay.md`](../consensus/worked-example-next-block-delay.md)。
