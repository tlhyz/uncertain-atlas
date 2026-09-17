# 例：看见 Finalize 等价于 ABCI 1.0 的 BeginBlock / DeliverTx / EndBlock / 看见收成一门 不是已经四门已经结算 / 已经交差；不是已经 Finalize 回包义务 bundled（363） interchangeable / 已经 finresp bundled interchangeable；不是已经可以用 decided_last_commit 定奖惩 / 已经必须回四列 interchangeable

**层次**：实现 / Finalize 回包义务 not four gates settled 正式三事（363 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Finalize equiv ABCI 1.0 not four gates settled / not finresp bundled（363） interchangeable / not decided_last_commit rewards bundled（463） interchangeable」，不是 FinalizeBlock 等价于 ABCI 1.0 BeginBlock/DeliverTx/EndBlock 正式三事（586），也不是 Finalize 回包义务 bundled 三事（363）。不要另写怎样写 Finalize 回包。

## 官方三件事

规范把 FinalizeBlock Usage 里 This method is equivalent to the call sequence BeginBlock, DeliverTx, and EndBlock in ABCI 1.0 和「已经四门已经结算 interchangeable / 已经是 finresp bundled interchangeable / 已经可以用 decided_last_commit 定奖惩 interchangeable」分开写成三件独立的实现事，不是「看见收成一门 就已经四门已经结算、已经 finresp bundled interchangeable、已经定奖惩 interchangeable」一件事：

1. **看见 Finalize 等价于 ABCI 1.0 的 `BeginBlock` / `DeliverTx` / `EndBlock` / 看见收成一门 is not already four gates settled interchangeable / 已经 CheckTx / Prepare / Process / Finalize + Commit 四门齐了 interchangeable / 已经交差 interchangeable / 已经 persist decision interchangeable，也不是已经 Finalize 回包义务 bundled（363） interchangeable / 600 notgates interchangeable / 363 finresp interchangeable / 586 finequiv interchangeable / 33 four gates interchangeable，也不是已经 FinalizeBlock 等价于 ABCI 1.0 BeginBlock/DeliverTx/EndBlock 正式三事（586） interchangeable / 586 finequiv interchangeable / 465 equiv bundled interchangeable，也不是已经 FinalizeBlock When persist decision bundled（478 余量） interchangeable / 478 finpersist interchangeable / 466 executes block v interchangeable / 335 finpersist interchangeable。**  
   官方写：This method is equivalent to the call sequence BeginBlock, DeliverTx, and EndBlock in ABCI 1.0。看见收成一门，不是已经四门已经结算（33） interchangeable——363 bundled 第一件事常被写成「看见等价于旧三步 就已经四门已经结算」，本页从 363 侧钉 equiv not four gates settled 单句。看见等价，不是已经 persist decision（478） interchangeable——478 钉 When 第 1 步，本页钉 Usage equiv 单句。看见 BeginBlock/DeliverTx/EndBlock，不是已经 586 finequiv bundled interchangeable——586 另钉 equiv 三事，本页钉 363 item 1 边界。
2. **看见 equiv ABCI 1.0 / 看见收成一门 is not already finresp bundled（363） interchangeable / 已经 must provide 四列 interchangeable / 已经可以用 decided_last_commit 和 misbehavior 定奖惩 interchangeable / 已经必须回四列 interchangeable，也不是已经 FinalizeBlock decided_last_commit + misbehavior 定奖惩 bundled（463 余量） interchangeable / 463 finreward interchangeable / 567 not slashed interchangeable / 568 not proposed interchangeable / 569 not voteinfo interchangeable，也不是已经 must provide values not already changed set / settled bundled（594 余量） interchangeable / 594 not settled interchangeable / 477 finasresult interchangeable / 363 item 3 interchangeable，也不是已经 CometBFT fill up all fields even if Prepare/Process passed bundled（363 余量 / 473 finfill） interchangeable / 473 finfill interchangeable / 562 not need Finalize interchangeable。**  
   官方把 equiv 收成一门 和 finresp bundled 三事分开——363 item 1 常与 363 bundled 混成「看见收成一门 就已经 finresp bundled interchangeable」，本页钉 not finresp bundled not four gates 单句。看见等价，不是已经 463 finreward（363 item 2 余量） interchangeable——463 钉 can use decided_last_commit + misbehavior，本页钉 item 1 单句。看见收成一门，不是已经 must provide 四列（363 item 3 余量） interchangeable——363 item 3 另钉必须回四列 not changed set，本页钉 item 1 单句。
3. **看见 equiv ABCI 1.0 / 看见收成一门 is not already no Prepare/Process interchangeable / 已经 ABCI++ 只剩 Finalize 一门 interchangeable / 已经 CheckTx 技术上可选 interchangeable / 已经 Process 跑过就不用在 Finalize 再执行 interchangeable，也不是已经 FinalizeBlock 等价于 ABCI 1.0 BeginBlock/DeliverTx/EndBlock 正式三事（586） interchangeable / 586 finequiv item 2 interchangeable / 351 Process also on proposer interchangeable / 373 CheckTx optional interchangeable，也不是已经 Finalize 含刚决定那块字段 bundled（461 余量） interchangeable / 474 finnewdec interchangeable / 460 fincand interchangeable，也不是已经 FinalizeBlock When Application executes block v bundled（466 余量） interchangeable / 466 executes block v interchangeable / 595 notcand interchangeable / 584 apply candidate interchangeable。**  
   官方把 equiv 收成一门 和 ABCI++ 仍保留 Prepare/Process 分开——363 item 1 常与 586 item 2 混成「看见收成一门 就已经没有 Prepare/Process interchangeable」，本页从 363 侧钉 not no Prepare/Process 单句边界。看见等价，不是已经 586 finequiv item 2 interchangeable——586 钉 not no Prepare/Process，本页钉 363 item 1 第三件事。看见收成一门，不是已经 Process 跑过就不执行（595 / 460） interchangeable——460 / 595 另钉 apply candidate / as a result of executing，本页钉 equiv not four gates 单句。

怎样写 Finalize 回包、怎样映射 BeginBlock/DeliverTx/EndBlock 是规范里的做法，本页不抄。Finalize 回包义务 bundled（363）、FinalizeBlock 等价于 ABCI 1.0 BeginBlock/DeliverTx/EndBlock（586）、FinalizeBlock decided_last_commit + misbehavior 定奖惩（463）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **equiv not four gates settled ≠ finresp bundled interchangeable：** 官方把收成一门和四门已经结算 / finresp bundled 分开。
- **equiv not finresp bundled ≠ 463 finreward / 594 not settled interchangeable：** 官方把 363 item 1 和 item 2 / item 3 分开。
- **equiv not no Prepare/Process ≠ 586 finequiv item 2 / 460 fincand interchangeable：** 官方把 363 item 1 和 equiv 三事 item 2 / apply candidate 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| equiv ABCI 1.0 | 不是 already four gates settled | 不是 four gates（33） |
| equiv ABCI 1.0 | 不是 already finresp bundled | 不是 decided_last_commit rewards（463） |
| equiv ABCI 1.0 | 不是 already no Prepare/Process | 不是 finequiv item 2（586） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 回包义务 not four gates settled 正式三事（363 余量），必须分开 equiv 是不是 already four gates settled interchangeable / 33 / 478 finpersist interchangeable、equiv 是不是 already finresp bundled interchangeable / 463 finreward interchangeable / 594 not settled interchangeable、equiv 是不是 already no Prepare/Process interchangeable / 586 finequiv interchangeable / 460 fincand interchangeable。可以跳过「看见收成一门 就已经四门已经结算 interchangeable」。不要另写怎样写 Finalize 回包。

## 本页不抄

- 怎样写 Finalize 回包、怎样映射 BeginBlock/DeliverTx/EndBlock。
- Finalize 回包义务 bundled 三事。那是不变量 363。
- can use decided_last_commit + misbehavior not slashed。那是不变量 463（363 item 2 余量）。
- must provide 四列 not changed set / settled。那是不变量 363 item 3 余量 / 594（477 item 1 余量）。
- FinalizeBlock 等价于 ABCI 1.0 BeginBlock/DeliverTx/EndBlock 三事。那是不变量 586。
- 四门已经结算。那是不变量 33。
