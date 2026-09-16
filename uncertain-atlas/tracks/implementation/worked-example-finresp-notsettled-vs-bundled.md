# 例：看见必须回 app_hash / tx_results / validator_updates / consensus_param_updates / 看见 must provide 四列 is not already changed validator set / H+1 换人；不是已经 Finalize + Commit 交差；不是已经 Finalize 回包义务 bundled（363） interchangeable / 已经 finresp bundled interchangeable

**层次**：实现 / Finalize 回包义务 must provide 四列 not already changed set / settled 正式三事（363 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Finalize 回包义务 must provide 四列 not already changed set / settled / not finresp bundled（363） interchangeable / not finasresult bundled（477） interchangeable / not 594 not settled interchangeable」，不是 Finalize 回包义务 bundled（363），也不是 FinalizeBlock must provide values not already changed set / settled 正式三事（477 余量 / 594）。不要另写怎样编回包四列。

## 官方三件事

规范把 FinalizeBlock Usage 里执行完这块应用必须给 `FinalizeBlockResponse.app_hash`、`tx_results`、`validator_updates`、`consensus_param_updates` 提供值 和「已经改了集合 interchangeable / 已经 Finalize + Commit 交差 interchangeable / 已经是 finresp bundled interchangeable」分开写成三件独立的实现事，不是「看见 must provide 四列 就已经改了集合、已经交差、已经 finresp bundled interchangeable」一件事：

1. **看见必须回 `app_hash` / `tx_results` / `validator_updates` / `consensus_param_updates` / 看见 must provide 四列 is not already changed validator set / H+1 换人 interchangeable / 已经 validator_updates 非空 interchangeable / 已经 H+1 生效 interchangeable，也不是已经 Finalize 回包义务 bundled（363） interchangeable / 601 notsettled interchangeable / 363 finresp interchangeable / 594 not settled interchangeable / 477 finasresult interchangeable，也不是已经 FinalizeBlockResponse validator_updates H→H+1 bundled（471 余量） interchangeable / 471 fincparam interchangeable / 459 validator_updates H+1/H+2/H+3 interchangeable，也不是已经 FinalizeBlock 空更新 keep current bundled（458 余量） interchangeable / 458 finempty interchangeable / 597 notmustprovide interchangeable / 598 notnoset interchangeable，也不是已经 InitChain 空名单就已经没有集合 interchangeable / 318 ValidatorUpdate interchangeable / 335 finpersist interchangeable。**  
   官方写：执行完这块，应用必须给 `FinalizeBlockResponse.app_hash`、`tx_results`、`validator_updates`、`consensus_param_updates` 提供值；另句写 validator_updates triggered by block H affect validation at H+1/H+2/H+3。看见 must provide 四列，不是已经改了集合——363 bundled 第三件事常被写成「看见回了四列 就已经改了集合」，本页从 363 侧钉 must provide not changed set 单句。看见必须回 validator_updates，不是已经 471 fincparam / 459 validator_updates interchangeable——471 / 459 各钉 H→H+1 生效延迟，本页钉 363 item 3 边界。看见 must provide，不是已经 empty keep current（458 余量） interchangeable——458 钉空更新 keep current，本页钉 363 item 3 单句。
2. **看见 must provide 四列 / 看见必须回四列 is not already Finalize + Commit 那种已经交差 / 已经 persist decision interchangeable / 已经四门已经结算 interchangeable / 已经 Application executes block _v_ interchangeable，也不是已经 Finalize 回包义务 bundled（363） interchangeable / 601 notsettled interchangeable / 363 finresp interchangeable / 600 notgates interchangeable / 586 finequiv interchangeable，也不是已经 FinalizeBlock When persist decision bundled（478 余量） interchangeable / 478 finpersist interchangeable / 466 executes block v interchangeable / 335 finpersist interchangeable，也不是已经 FinalizeBlock must provide values not already changed set / settled bundled（594 余量 / 477 item 1） interchangeable / 594 not settled interchangeable / 477 finasresult interchangeable，也不是已经 Finalize 等价于 ABCI 1.0 BeginBlock/DeliverTx/EndBlock 正式三事（586） interchangeable / 465 equiv bundled interchangeable / 33 four gates interchangeable。**  
   官方把 must provide 四列 和 Finalize + Commit 已经交差分开——363 item 3 常与 33 / 478 混成「看见 must provide 四列 就已经交差 interchangeable」，本页钉 must provide not settled 单句。看见必须回四列，不是已经 persist decision（478 第 1 步） interchangeable——478 钉 When 第 1 步，本页钉 363 item 3 第二件事。看见 must provide，不是已经 finasresult not settled（594 余量 / 477 item 1） interchangeable——594 从 477 侧钉同一 Usage 句，本页从 363 finresp bundled 侧钉 not settled 单句。
3. **看见 must provide 四列 / 看见必须回四列 is not already finresp bundled（363） interchangeable / 已经 must provide 四列 interchangeable / 已经可以用 decided_last_commit 和 misbehavior 定奖惩 interchangeable / 已经收成一门 interchangeable，也不是已经 FinalizeBlock must provide values as a result of executing the block bundled（477） interchangeable / 477 finasresult interchangeable / 595 notcand interchangeable / 596 notempty interchangeable，也不是已经 FinalizeBlock decided_last_commit + misbehavior 定奖惩 bundled（463 余量） interchangeable / 463 finreward interchangeable / 567 not slashed interchangeable / 600 notgates interchangeable，也不是已经 empty keep current means no must provide obligation bundled（458 余量） interchangeable / 597 notmustprovide interchangeable / 477 item 3 interchangeable，也不是已经 as a result of executing not candidate bundled（477 item 2 余量） interchangeable / 460 fincand interchangeable / 584 apply candidate interchangeable。**  
   官方把 363 finresp bundled 三事里的 must provide 四列 和 can use decided_last_commit 定奖惩 / equiv 收成一门 分开——363 bundled 常与 463 / 600 混成「看见 must provide 四列 就已经 finresp bundled interchangeable」，本页钉 363 item 3 第三件事。看见 must provide，不是已经 finasresult bundled（477） interchangeable——477 另钉 as a result of executing / 提供了值 三事，本页钉 finresp not finasresult bundled 单句。看见必须回四列，不是已经 as a result of executing not candidate（477 item 2 余量） interchangeable——477 item 2 另钉 Process / Prepare candidate，本页钉 363 item 3 单句。

怎样编回包四列、怎样写空更新、怎样在 Finalize 套用 candidate 是规范里的做法，本页不抄。Finalize 回包义务 bundled（363）、FinalizeBlock must provide values not already changed set / settled（594 / 477 item 1）、FinalizeBlock 空更新 keep current（458）、validator_updates H→H+1（471）、Finalize 回包义务 not four gates settled（600 / 363 item 1）是另外那套，本页不抄。

## 官方为什么这样拆

- **must provide 四列 not changed set / H+1 ≠ finresp bundled interchangeable：** 官方把 must provide 四列 和 validator_updates 已经改了集合 / H+1 生效分开。
- **must provide not settled / four gates ≠ finresp bundled interchangeable：** 官方把 must provide 四列 和 Finalize + Commit 交差 / persist decision 分开。
- **must provide not finresp bundled ≠ finasresult bundled / 463 finreward / 600 notgates interchangeable：** 官方把 363 item 3 和 363 bundled 整包 / 477 bundled / 463 item 2 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| must provide 四列 | 不是 already changed set / H+1 | 不是 finresp bundled（363） |
| must provide 四列 | 不是 already settled / 交差 | 不是 finasresult not settled（594 / 477） |
| must provide 四列 | 不是 already finresp bundled | 不是 decided_last_commit rewards（463） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 回包义务 must provide 四列 not already changed set / settled 正式三事（363 余量），必须分开 must provide 四列是不是 already changed validator set / H+1 effective interchangeable / 471 fincparam interchangeable / 458 finempty interchangeable、must provide 是不是 already Finalize + Commit 交差 / persist decision interchangeable / 478 finpersist interchangeable / 600 notgates interchangeable、must provide 是不是 already finresp bundled interchangeable / 594 not settled interchangeable / 477 finasresult interchangeable / 463 finreward interchangeable。可以跳过「看见 must provide 四列 就已经改了集合 interchangeable」。不要另写怎样编回包四列。

## 本页不抄

- 怎样编回包四列、怎样写空更新、怎样在 Finalize 套用 candidate。
- Finalize 回包义务 bundled 三事。那是不变量 363。
- FinalizeBlock must provide values not already changed set / settled。那是不变量 594（477 item 1 余量）。
- Finalize 回包义务 not four gates settled。那是不变量 600（363 item 1 余量）。
- can use decided_last_commit + misbehavior 定奖惩。那是不变量 463（363 item 2 余量）。
- FinalizeBlock 空更新 keep current。那是不变量 458。
