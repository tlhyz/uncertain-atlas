# 例：看见 Application executes block _v_ / 应用回了 AppHash 和各笔输出 is not already +2/3 precommit decided / ResultHash / not FinalizeBlock When Application executes block v bundled（466） interchangeable / not +2/3 precommit same id(v) already will Finalize bundled（362） interchangeable

**层次**：实现 / FinalizeBlock When Application executes block v not +2/3 precommit decided / ResultHash 正式三事（466 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When / Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「FinalizeBlock When Application executes block v not +2/3 precommit decided / ResultHash / not FinalizeBlock When Application executes block v bundled（466） interchangeable / not +2/3 precommit same id(v) already will Finalize bundled（362） interchangeable」，不是 FinalizeBlock When Application executes block v bundled（466），也不是 FinalizeBlock When Application executes block v not apply candidate / Process already ran 正式三事（574 余量）。不要另写怎样写 Finalize、怎样算 ResultHash。

## 官方三件事

规范把 FinalizeBlock When 第 3 步 Application executes block _v_ / 应用回了 AppHash 和各笔输出 / 引擎把输出哈希进 ResultHash 和「已经 +2/3 precommit decided interchangeable / 已经 ResultHash interchangeable / 已经印进本头 interchangeable」分开写成三件独立的实现事，不是「看见 Application executes block _v_ 就已经 +2/3 precommit decided interchangeable、已经 ResultHash interchangeable、已经 466 finexecbv bundled interchangeable」一件事：

1. **看见 Application executes block _v_ / 应用回了 AppHash 和各笔输出 is not already +2/3 precommit decided / ResultHash / 看见执行了 is not already FinalizeBlock When Application executes block v bundled（466） interchangeable / 已经 +2/3 precommit decided interchangeable / 已经 ResultHash interchangeable / 已经印进本头 interchangeable，也不是已经 FinalizeBlock When Application executes block v not persist decision bundled（573 余量） interchangeable / 573 not persist interchangeable / 572 not execbv interchangeable / 584 apply candidate interchangeable，也不是已经 FinalizeBlock When Application executes block v not apply candidate bundled（574 余量） interchangeable / 574 not cand interchangeable / 351 Process also on proposer interchangeable，也不是已经 Finalize 时的 Process 保证 bundled（360） interchangeable / 已经 persist decision interchangeable / 已经至少一名非拜占庭验证者跑过 Process interchangeable。**  
   官方 When 写：Application executes block _v_；应用算出并回 AppHash，以及各笔执行输出；CometBFT 把这些输出哈希进 ResultHash。看见 Application executes block _v_，不是已经 +2/3 precommit decided / ResultHash interchangeable——466 item 3 常被写成「看见 Application executes block _v_ 就已经 ResultHash interchangeable」，本页钉 executes block v not +2/3 precommit decided / ResultHash 单句。看见 executes block _v_，不是已经 FinalizeBlock When Application executes block v（466） interchangeable——466 另钉 not persist decision / not apply candidate 三事，本页钉 item 3 边界。看见回了 AppHash，不是已经 Finalize 时的 Process 保证 bundled（360） interchangeable——360 另钉 at least one / apply candidate bundled，本页钉 finexecbv notprecommit 单句。
2. **看见 Application executes block _v_ is not already +2/3 precommit same id(v) already will Finalize bundled（362 余量） interchangeable / 看见应用回了 AppHash 和各笔输出 is not already +2/3 precommit 同一 id(v) 才决定再调 Finalize interchangeable / 已经 When 里收到带上头的 Proposal 会先验块头 interchangeable / 已经会调 Finalize interchangeable / 已经决定了 interchangeable，也不是已经 FinalizeBlock When Application executes block v bundled（466） interchangeable / 575 not precommit interchangeable / 466 executes block v interchangeable / 573 not persist interchangeable，也不是已经 +2/3 precommit 同一 id(v) 才决定再调 Finalize 三事（362） interchangeable / 362 +2/3 precommit interchangeable / 335 finpersist interchangeable / 361 ExtendVote when interchangeable，也不是已经 FinalizeBlock When calling ProcessProposal guarantee bundled（472） interchangeable / 472 finwhen interchangeable / 570 not every validator interchangeable。**  
   官方 When 把 +2/3 precommit 决定再调 Finalize 和 Application executes block _v_ / ResultHash 分开——466 item 3 常与 362 混成「看见 Application executes block _v_ 就已经是 +2/3 precommit decided interchangeable」，本页钉 not +2/3 precommit decided not 362 bundled 单句。看见 executes block _v_，不是已经 +2/3 precommit 同一 id(v) 才决定再调 Finalize（362 余量） interchangeable——362 另钉 When 流程 precommit 路径三事，本页钉 466 item 3 单句。看见回了 AppHash，不是已经先把 v 落成这一高的决定再同步调 Finalize（362 item 2） interchangeable——362 钉 persist decision 边界，本页钉 finexecbv notprecommit 单句。
3. **看见 Application executes block _v_ is not already FinalizeBlock persist decision not committed bundled（335 余量） interchangeable / 看见应用回了 AppHash 和各笔输出 is not already committed / settled interchangeable / 已经 Finalize 改了就已经落盘 interchangeable / 335 finpersist interchangeable / 576 fincand committed interchangeable，也不是已经 FinalizeBlock When Application executes block v bundled（466） interchangeable / 575 not precommit interchangeable / 466 executes block v interchangeable / 574 not cand interchangeable，也不是已经 +2/3 precommit same id(v) already will Finalize bundled（362 余量） interchangeable / 362 +2/3 precommit interchangeable / 147 apphash vs this block interchangeable，也不是已经 Finalize 含刚决定那块的字段 bundled（407 余量） interchangeable / 407 finfields interchangeable / 473 finfill interchangeable / 568 not passed means ran Process interchangeable。**  
   官方把 Application executes block _v_ / ResultHash 和 already committed / settled 分开——466 item 3 第三件事「看见 Application executes block _v_ 就已经印进本头 interchangeable」常与 335 / 147 混成一件事，本页钉 not +2/3 precommit decided not finpersist / apphash vs this block 单句。看见回了 AppHash，不是已经本头 AppHash 就已经是本高度交差（147 余量） interchangeable——147 钉 AppHash 边界，本页钉 466 item 3 第三件事。看见 ResultHash，不是已经 Finalize 含刚决定那块的字段（407 余量） interchangeable——407 钉 newly decided block fields 边界，本页钉 finexecbv notprecommit 单句。

怎样写 Finalize、怎样落决定、怎样算 ResultHash 是规范里的做法，本页不抄。FinalizeBlock When Application executes block v bundled（466）、+2/3 precommit 同一 id(v) 才决定再调 Finalize（362）、FinalizeBlock When Application executes block v not persist decision 正式三事（573 余量）是另外那套，本页不抄。

## 官方为什么这样拆

- **executes block v not +2/3 precommit decided / ResultHash ≠ FinalizeBlock When Application executes block v bundled interchangeable：** 官方把 Application executes block _v_ / ResultHash 和 466 bundled 三事分开。
- **executes block v not +2/3 precommit decided / ResultHash ≠ +2/3 precommit same id(v) already will Finalize bundled interchangeable：** 官方把 Application executes block _v_ 和 When 流程 precommit 决定分开。
- **executes block v not +2/3 precommit decided / ResultHash ≠ finpersist / apphash vs this block interchangeable：** 官方把 ResultHash 和 already committed / 本头 AppHash 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Application executes block v | 不是 already +2/3 precommit decided / ResultHash | 不是 FinalizeBlock When Application executes block v bundled（466） |
| Application executes block v | 不是 already +2/3 precommit same id(v) decided | 不是 +2/3 precommit 同一 id(v) 才决定再调 Finalize（362） |
| Application executes block v / ResultHash | 不是 already committed / 本头 AppHash | 不是 Finalize 改了就已经落盘（335） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When Application executes block v not +2/3 precommit decided / ResultHash 正式三事（466 余量），必须分开 executes block v 是不是 already +2/3 precommit decided / ResultHash interchangeable / 466 finexecbv interchangeable / 573 not persist interchangeable / 574 not cand interchangeable、executes block v 是不是 already +2/3 precommit same id(v) decided interchangeable / 362 +2/3 precommit interchangeable / 335 finpersist interchangeable / 361 ExtendVote when interchangeable、executes block v / ResultHash 是不是 already committed / 本头 AppHash interchangeable / 147 apphash vs this block interchangeable / 407 finfields interchangeable / 473 finfill interchangeable。可以跳过「看见 Application executes block _v_ 就已经 ResultHash interchangeable」。不要另写怎样算 ResultHash。

## 本页不抄

- 怎样写 Finalize、怎样落决定、怎样算 ResultHash。
- Application executes block v not persist decision / When calling guarantee。那是不变量 573（466 item 1 余量）。
- Application executes block v not apply candidate / Process already ran。那是不变量 574（466 item 2 余量）。
- FinalizeBlock When Application executes block v bundled 三事。那是不变量 466。
- +2/3 precommit 同一 id(v) 才决定再调 Finalize 三事。那是不变量 362。
