# 例：看见 Application executes block _v_ is not already persist decision / When calling / consensus guarantees means Application executes block v / not FinalizeBlock When Application executes block v bundled（466） interchangeable / not FinalizeBlock When calling ProcessProposal guarantee bundled（472） interchangeable

**层次**：实现 / FinalizeBlock When Application executes block v not persist decision / When calling guarantee 正式三事（466 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When / Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「FinalizeBlock When Application executes block v not persist decision / When calling guarantee / not FinalizeBlock When Application executes block v bundled（466） interchangeable / not FinalizeBlock When calling ProcessProposal guarantee bundled（472） interchangeable」，不是 FinalizeBlock When Application executes block v bundled（466），也不是 apply candidate state not ExecuteTxState 正式三事（584 余量）。不要另写怎样写 Finalize、怎样缓存 candidate。

## 官方三件事

规范把 FinalizeBlock When 第 3 步 Application executes block _v_ 和「已经 persist decision interchangeable / 已经 When calling guarantee interchangeable / 已经是 FinalizeBlock When Application executes block v bundled interchangeable」分开写成三件独立的实现事，不是「看见 Application executes block _v_ 就已经 persist decision interchangeable、已经 When calling guarantee interchangeable、已经 466 finexecbv bundled interchangeable」一件事：

1. **看见 Application executes block _v_ / 看见 When 第 3 步 executes block _v_ is not already persist decision / When calling / consensus guarantees means Application executes block v / 看见执行了 is not already FinalizeBlock When Application executes block v bundled（466） interchangeable / 已经 persist decision interchangeable / 已经把块落成这一高的决定 interchangeable / 已经 When calling guarantee interchangeable，也不是已经 FinalizeBlock When calling ProcessProposal guarantee bundled（472） interchangeable / 472 finwhen interchangeable / 570 not every validator interchangeable / 571 not proposer interchangeable，也不是已经 Finalize 时的 Process 保证 bundled（360） interchangeable / 已经字段再填一遍 interchangeable / 已经至少一名非拜占庭验证者跑过 Process interchangeable，也不是已经 +2/3 precommit same id(v) already will Finalize bundled（362 余量） interchangeable / 362 +2/3 precommit interchangeable / 584 apply candidate interchangeable。**  
   官方 When 写：Application executes block _v_。Usage 把 When 第 3 步和 When calling guarantee 分开——466 item 1 常被写成「看见 Application executes block _v_ 就已经 persist decision interchangeable」，本页钉 executes block v not persist decision / When calling guarantee 单句。看见 executes block _v_，不是已经 FinalizeBlock When Application executes block v（466） interchangeable——466 另钉 not apply candidate / not +2/3 precommit 三事，本页钉 item 1 边界。看见 When 第 3 步，不是已经 Finalize 时的 Process 保证 bundled（360） interchangeable——360 另钉 fill all fields / apply candidate bundled，本页钉 finexecbv notpersist 单句。
2. **看见 Application executes block _v_ is not already FinalizeBlock When calling ProcessProposal guarantee bundled（472） interchangeable / 看见 When 第 3 步 is not already When calling / consensus guarantees means Application executes block v / persist decision interchangeable / 已经 persist decision interchangeable / 已经 When calling guarantee interchangeable / 已经 Process 跑过就不执行 interchangeable，也不是已经 FinalizeBlock When Application executes block v bundled（466） interchangeable / 573 not persist interchangeable / 466 executes block v interchangeable / 362 +2/3 precommit interchangeable，也不是已经 When calling guarantee not executes block v / persist decision bundled（572 余量） interchangeable / 572 not execbv interchangeable / 570 not every validator interchangeable / 571 not proposer interchangeable，也不是已经 apply candidate state not ExecuteTxState bundled（584 余量） interchangeable / 584 apply candidate interchangeable / 583 not refill interchangeable。**  
   官方把 When 第 3 步 executes block _v_ 和 Usage When calling guarantee 分开——466 item 1 常与 472 混成「看见 Application executes block _v_ 就已经是 When calling guarantee interchangeable」，本页钉 not persist decision not 472 bundled 单句。看见 executes block _v_，不是已经 FinalizeBlock When calling ProcessProposal guarantee（472） interchangeable——472 另钉 not every validator / not proposer 三事，本页钉 466 item 1 单句。看见 When 第 3 步，不是已经 apply candidate（584 余量） interchangeable——584 钉 360 item 3 边界，本页钉 finexecbv notpersist 单句。
3. **看见 Application executes block _v_ is not already When calling guarantee not executes block v / persist decision bundled（572 余量） interchangeable / 看见 When 第 3 步 is not already When calling / persist decision / executes block v interchangeable / 572 not execbv interchangeable / 已经 472 item 3 单句 interchangeable，也不是已经 FinalizeBlock When Application executes block v bundled（466） interchangeable / 573 not persist interchangeable / 466 executes block v interchangeable / 362 +2/3 precommit interchangeable，也不是已经 FinalizeBlock When calling ProcessProposal guarantee bundled（472） interchangeable / 472 finwhen interchangeable / 570 not every validator interchangeable / 571 not proposer interchangeable，也不是已经 Finalize 请求把字段再填一遍 not no need to provide again bundled（583 余量） interchangeable / 473 finfill interchangeable / 568 not passed means ran Process interchangeable。**  
   官方把 When 第 3 步 Application executes block _v_ 和 472 item 3 not executes block v 单句分开——466 item 1 常与 572 混成「看见 Application executes block _v_ 就已经是 When calling guarantee not executes block v interchangeable」，本页钉 not persist decision not 572 not execbv 单句。看见 executes block _v_，不是已经 +2/3 precommit same id(v)（362 余量） interchangeable——362 钉 When 流程 precommit 路径，本页钉 466 item 1 第三件事。看见 When 第 3 步，不是已经 even if already passed（568 余量） interchangeable——568 钉 473 item 2 边界，本页钉 finexecbv notpersist 单句。

怎样写 Finalize、怎样缓存 candidate、怎样测失败路径是规范里的做法，本页不抄。FinalizeBlock When Application executes block v bundled（466）、When calling guarantee not executes block v / persist decision 正式三事（572 余量）、apply candidate state not ExecuteTxState 正式三事（584 余量）是另外那套，本页不抄。

## 官方为什么这样拆

- **executes block v not persist decision / When calling guarantee ≠ FinalizeBlock When Application executes block v bundled interchangeable：** 官方把 When 第 3 步 executes block _v_ 和 persist decision / When calling guarantee 分开。
- **executes block v not persist decision / When calling guarantee ≠ FinalizeBlock When calling ProcessProposal guarantee bundled interchangeable：** 官方把 Application executes block _v_ 和 Usage When calling guarantee 分开。
- **executes block v not persist decision / When calling guarantee ≠ 572 not execbv interchangeable：** 官方把 466 item 1 和 472 item 3 not executes block v 单句分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Application executes block v | 不是 already persist decision / When calling guarantee | 不是 FinalizeBlock When Application executes block v bundled（466） |
| Application executes block v | 不是 already When calling guarantee / persist decision | 不是 FinalizeBlock When calling ProcessProposal guarantee bundled（472） |
| Application executes block v | 不是 already 572 not execbv | 不是 When calling guarantee not executes block v / persist decision 正式三事（572） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When Application executes block v not persist decision / When calling guarantee 正式三事（466 余量），必须分开 executes block v 是不是 already persist decision / When calling guarantee interchangeable / 466 finexecbv interchangeable / 584 apply candidate interchangeable / 362 +2/3 precommit interchangeable、executes block v 是不是 already When calling guarantee / persist decision interchangeable / 472 finwhen interchangeable / 570 not every validator interchangeable / 571 not proposer interchangeable、executes block v 是不是 already 572 not execbv interchangeable / 473 finfill interchangeable / 568 not passed means ran Process interchangeable。可以跳过「看见 Application executes block _v_ 就已经 persist decision interchangeable」。不要另写怎样写 Finalize。

## 本页不抄

- 怎样写 Finalize、怎样缓存 candidate、怎样测失败路径。
- Application executes block v not apply candidate / Process already ran。那是不变量 584（466 item 2 余量）。
- Application executes block v not +2/3 precommit decided / ResultHash。那是不变量 362 / 466 item 3 余量。
- FinalizeBlock When Application executes block v bundled 三事。那是不变量 466。
- When calling guarantee not executes block v / persist decision 正式三事（472 余量）。那是不变量 572。
