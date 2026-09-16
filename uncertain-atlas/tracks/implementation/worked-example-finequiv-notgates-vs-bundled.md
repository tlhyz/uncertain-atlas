# 例：看见 FinalizeBlock 等价于 ABCI 1.0 BeginBlock/DeliverTx/EndBlock / 看见收成一门 is not already four gates settled interchangeable / 已经交差 interchangeable；不是已经 FinalizeBlock 等价于 ABCI 1.0 BeginBlock/DeliverTx/EndBlock 正式三事 bundled（586） interchangeable / 已经 finequiv bundled interchangeable

**层次**：实现 / FinalizeBlock equiv ABCI 1.0 not four gates settled 正式三事（586 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「FinalizeBlock equiv ABCI 1.0 not four gates settled / not finequiv bundled（586） interchangeable / not finresp bundled（363） interchangeable / not 600 notgates interchangeable」，不是 FinalizeBlock 等价于 ABCI 1.0 BeginBlock/DeliverTx/EndBlock 正式三事 bundled（586），也不是 Finalize 回包义务 not four gates settled（600 / 363 item 1 余量）。不要另写怎样写 Finalize 回包、怎样映射旧三步。

## 官方三件事

规范把 FinalizeBlock Usage 里 This method is equivalent to the call sequence BeginBlock, DeliverTx, and EndBlock in ABCI 1.0 和「已经四门已经结算 interchangeable / 已经交差 interchangeable / 已经是 finequiv bundled interchangeable」分开写成三件独立的实现事，不是「看见收成一门 就已经四门已经结算、已经交差、已经 finequiv bundled interchangeable」一件事：

1. **看见 FinalizeBlock 等价于 ABCI 1.0 的 `BeginBlock` / `DeliverTx` / `EndBlock` / 看见收成一门 is not already four gates settled interchangeable / 已经 CheckTx / Prepare / Process / Finalize + Commit 四门齐了 interchangeable / 已经 persist decision interchangeable，也不是已经 FinalizeBlock 等价于 ABCI 1.0 BeginBlock/DeliverTx/EndBlock 正式三事 bundled（586） interchangeable / 602 notgates interchangeable / 586 finequiv interchangeable / 600 notgates interchangeable / 363 finresp interchangeable / 33 four gates interchangeable，也不是已经 Finalize 回包义务 not four gates settled 正式三事（363 余量 / 600） interchangeable / 600 notgates interchangeable / 465 equiv bundled interchangeable，也不是已经 FinalizeBlock When persist decision bundled（478 余量） interchangeable / 478 finpersist interchangeable / 466 executes block v interchangeable / 335 finpersist interchangeable。**  
   官方写：This method is equivalent to the call sequence BeginBlock, DeliverTx, and EndBlock in ABCI 1.0。看见收成一门，不是已经四门已经结算（33） interchangeable——586 bundled 第一件事常被写成「看见等价于旧三步 就已经四门已经结算」，本页从 586 侧钉 equiv not four gates settled 单句。看见等价，不是已经 persist decision（478） interchangeable——478 钉 When 第 1 步，本页钉 Usage equiv 单句。看见 BeginBlock/DeliverTx/EndBlock，不是已经 600 notgates（363 item 1 余量） interchangeable——600 从 363 finresp 侧钉同一 Usage 句，本页从 586 finequiv bundled 侧钉 not four gates 单句。
2. **看见 equiv ABCI 1.0 / 看见收成一门 is not already Finalize + Commit 那种已经交差 / 已经 Application executes block _v_ interchangeable / 已经 Process 回了 Accept 就已经是同一句 interchangeable，也不是已经 FinalizeBlock 等价于 ABCI 1.0 BeginBlock/DeliverTx/EndBlock 正式三事 bundled（586） interchangeable / 602 notgates interchangeable / 586 finequiv interchangeable / 601 notsettled interchangeable / 594 not settled interchangeable，也不是已经 Finalize 回包义务 bundled（363 余量） interchangeable / 363 finresp interchangeable / 586 finequiv item 2 interchangeable / 373 CheckTx optional interchangeable，也不是已经 FinalizeBlock must provide values not already changed set / settled bundled（594 余量 / 477 item 1） interchangeable / 594 not settled interchangeable / 477 finasresult interchangeable。**  
   官方把 equiv 收成一门 和 Finalize + Commit 已经交差 / Process Accept 已经 settled 分开——586 item 1 常与 478 / 601 混成「看见收成一门 就已经交差 interchangeable」，本页钉 equiv not settled 单句。看见等价，不是已经 persist decision（478 第 1 步） interchangeable——478 钉 When 第 1 步，本页钉 Usage equiv 单句。看见收成一门，不是已经 finresp notsettled（601 余量 / 363 item 3） interchangeable——601 钉 must provide 四列 not settled，本页钉 586 item 1 第二件事。
3. **看见 equiv ABCI 1.0 / 看见收成一门 is not already finequiv bundled（586） interchangeable / 已经 must provide 四列 interchangeable / 已经 no Prepare/Process interchangeable / 已经 Contains newly decided block fields interchangeable，也不是已经 Finalize 回包义务 bundled（363 余量） interchangeable / 363 finresp interchangeable / 600 notgates interchangeable / 463 finreward interchangeable / 594 not settled interchangeable，也不是已经 FinalizeBlock 等价于 ABCI 1.0 BeginBlock/DeliverTx/EndBlock 正式三事（586） interchangeable / 586 finequiv item 2 interchangeable / 586 finequiv item 3 interchangeable / 460 fincand interchangeable / 461 finnewfields interchangeable，也不是已经 FinalizeBlock decided_last_commit + misbehavior 定奖惩 bundled（463 余量） interchangeable / 567 not slashed interchangeable / 568 not proposed interchangeable。**  
   官方把 586 finequiv bundled 三事里的 equiv 收成一门 和 no Prepare/Process / Contains newly decided block fields 分开——586 bundled 常与 item 2 / item 3 混成「看见收成一门 就已经 finequiv bundled interchangeable」，本页钉 586 item 1 第三件事。看见等价，不是已经 finresp bundled（363） interchangeable——363 另钉 必须回四列 / can use decided_last_commit 定奖惩 bundled，本页钉 finequiv not finresp bundled 单句。看见收成一门，不是已经 586 finequiv item 2 / item 3 interchangeable——586 item 2 另钉 no Prepare/Process，item 3 另钉 Contains newly decided / apply candidate，本页钉 item 1 单句。

怎样写 Finalize 回包、怎样映射 BeginBlock/DeliverTx/EndBlock 是规范里的做法，本页不抄。FinalizeBlock 等价于 ABCI 1.0 BeginBlock/DeliverTx/EndBlock 正式三事 bundled（586）、Finalize 回包义务 not four gates settled（600 / 363 item 1）、Finalize 回包义务 must provide 四列 not settled（601 / 363 item 3）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **equiv not four gates settled ≠ finequiv bundled interchangeable：** 官方把收成一门和四门已经结算 / finequiv bundled 分开。
- **equiv not settled / 交差 ≠ finresp notsettled / 478 finpersist interchangeable：** 官方把 586 item 1 和 Finalize + Commit 交差 / must provide not settled 分开。
- **equiv not finequiv bundled ≠ 586 item 2 / item 3 / 363 finresp interchangeable：** 官方把 586 item 1 和 no Prepare/Process / Contains newly decided block fields / 363 finresp bundled 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| equiv ABCI 1.0 | 不是 already four gates settled | 不是 four gates（33） |
| equiv ABCI 1.0 | 不是 already settled / 交差 | 不是 finresp notsettled（601 / 363） |
| equiv ABCI 1.0 | 不是 already finequiv bundled | 不是 no Prepare/Process（586 item 2） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock equiv ABCI 1.0 not four gates settled 正式三事（586 余量），必须分开 equiv 是不是 already four gates settled interchangeable / 33 / 478 finpersist interchangeable / 600 notgates interchangeable、equiv 是不是 already settled / 交差 interchangeable / 601 notsettled interchangeable / 594 not settled interchangeable、equiv 是不是 already finequiv bundled interchangeable / 363 finresp interchangeable / 586 item 2 / 586 item 3 interchangeable。可以跳过「看见收成一门 就已经四门已经结算 interchangeable」。不要另写怎样写 Finalize 回包。

## 本页不抄

- 怎样写 Finalize 回包、怎样映射 BeginBlock/DeliverTx/EndBlock。
- FinalizeBlock 等价于 ABCI 1.0 BeginBlock/DeliverTx/EndBlock 正式三事 bundled。那是不变量 586。
- Finalize 回包义务 not four gates settled。那是不变量 600（363 item 1 余量）。
- Finalize 回包义务 must provide 四列 not settled。那是不变量 601（363 item 3 余量）。
- no Prepare/Process。那是不变量 586 item 2 余量。
- Contains newly decided block fields / apply candidate。那是不变量 586 item 3 余量 / 461 / 460。
- 四门已经结算。那是不变量 33。
