# 例：看见 must provide values for app_hash / tx_results / validator_updates / consensus_param_updates 不是已经改了集合 / H+1 换人；不是已经 Finalize + Commit 交差；不是已经 FinalizeBlock must provide values bundled（477） interchangeable / 已经 finresp bundled（363） interchangeable / 已经 empty keep current（458） interchangeable

**层次**：实现 / FinalizeBlock must provide values not already changed set / settled 正式三事（477 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「must provide 四列 not already changed set / settled / not finasresult bundled（477） interchangeable / not finresp bundled（363） interchangeable / not empty keep current（458） interchangeable」，不是 FinalizeBlock must provide values as a result of executing the block bundled（477），也不是 as a result of executing the block not candidate 正式三事（477 item 2 余量）。不要另写怎样编回包四列。

## 官方三件事

规范把 FinalizeBlock Usage 里 The Application must provide values for `FinalizeBlockResponse.app_hash`, `FinalizeBlockResponse.tx_results`, `FinalizeBlockResponse.validator_updates`, and `FinalizeBlockResponse.consensus_param_updates` 和「已经改了集合 interchangeable / 已经 Finalize + Commit 交差 interchangeable / 已经是 finasresult bundled interchangeable」分开写成三件独立的实现事，不是「看见 must provide 就已经改了集合、已经交差、已经 finasresult bundled interchangeable」一件事：

1. **看见 must provide values for app_hash / tx_results / validator_updates / consensus_param_updates / 看见必须回四列 is not already changed validator set / H+1 换人 interchangeable / 已经 validator_updates 非空 interchangeable / 已经 H+1 生效 interchangeable，也不是已经 FinalizeBlock must provide values as a result of executing the block bundled（477） interchangeable / 已经 must provide 四列 interchangeable / 已经 as a result of executing interchangeable，也不是已经 FinalizeBlockResponse validator_updates H→H+1 bundled（471 余量） interchangeable / 471 fincparam interchangeable / 459 validator_updates H+1/H+2/H+3 interchangeable，也不是已经 FinalizeBlock 空更新 keep current bundled（458 余量） interchangeable / 458 finempty interchangeable / 已经空着就没有 must provide 义务 interchangeable。**  
   官方 Usage 写：must provide values for … validator_updates … consensus_param_updates as a result of executing the block；另句写 validator_updates triggered by block H affect validation at H+1/H+2/H+3。看见 must provide，不是已经 validator_updates 非空那种已经改了集合 interchangeable——471 / 459 各钉 H→H+1 生效延迟，本页钉 477 item 1 边界。看见必须回四列，不是已经 finasresult bundled（477） interchangeable——477 另钉 as a result of executing / 提供了值 三事，本页只钉 item 1 单句。看见 must provide validator_updates，不是已经 empty keep current（458 余量） interchangeable——458 钉空更新 keep current，本页钉 not changed set 单句。
2. **看见 must provide values / 看见必须回四列 is not already Finalize + Commit 那种已经交差 / 已经四门已经结算 interchangeable / 已经 persist decision interchangeable / 已经 Application executes block _v_ interchangeable，也不是已经 FinalizeBlock must provide values bundled（477） interchangeable / 594 not settled interchangeable / 477 finasresult interchangeable / 363 finresp interchangeable，也不是已经 FinalizeBlock When persist decision bundled（478 余量） interchangeable / 478 finpersist interchangeable / 466 executes block v interchangeable，也不是已经 Finalize 回包义务 bundled（363 余量） interchangeable / 363 finresp interchangeable / 586 finequiv interchangeable / 已经 must provide 四列 interchangeable。**  
   官方把 must provide 义务和 Finalize + Commit 交差分开——477 item 1 常与 33 / 478 混成「看见 must provide 就已经交差 interchangeable」，本页钉 must provide not settled 单句。看见 must provide，不是已经 persist decision（478 第 1 步） interchangeable——478 钉 When 第 1 步，本页钉 Usage must provide 单句。看见必须回四列，不是已经 finresp bundled（363） interchangeable——363 把 must provide 四列和 can use decided_last_commit 定奖惩 bundled，本页钉 477 item 1 边界。
3. **看见 must provide values / 看见提供了值 is not already finasresult bundled（477） interchangeable / 已经 must provide 四列 interchangeable / 已经 as a result of executing interchangeable / 已经提供了 tx_results interchangeable，也不是已经 finresp bundled（363） interchangeable / 363 finresp interchangeable / 586 finequiv interchangeable / 471 fincparam interchangeable，也不是已经 empty keep current means no must provide obligation bundled（458 余量） interchangeable / 458 finempty interchangeable / 477 item 3 interchangeable，也不是已经 as a result of executing not candidate bundled（477 item 2 余量） interchangeable / 460 fincand interchangeable / 466 executes block v interchangeable。**  
   官方把 must provide 四列、must provide as a result of executing、provided values 和 empty keep current 分开——477 item 1 常与 477 bundled / 458 混成「看见 must provide 就已经 finasresult bundled interchangeable」，本页钉 not changed set not finasresult bundled 单句。看见 must provide，不是已经 finresp bundled（363） interchangeable——363 另钉 必须回四列 / 等价 ABCI 1.0 bundled，本页钉 477 item 1 第三件事。看见必须回四列，不是已经 as a result of executing not candidate（477 item 2 余量） interchangeable——477 item 2 另钉 Process / Prepare candidate，本页钉 item 1 单句。

怎样编回包四列、怎样写空更新、怎样在 Finalize 套用 candidate 是规范里的做法，本页不抄。FinalizeBlock must provide values bundled（477）、Finalize 回包义务 bundled（363）、FinalizeBlock 空更新 keep current（458）、validator_updates H→H+1（471）、FinalizeBlock When persist decision（478）是另外那套，本页不抄。

## 官方为什么这样拆

- **must provide 四列 not changed set / H+1 effective ≠ finasresult bundled interchangeable：** 官方把 must provide 义务和 validator_updates 已经改了集合 / H+1 生效分开。
- **must provide not settled / four gates ≠ finresp bundled interchangeable：** 官方把 must provide 四列和 Finalize + Commit 交差 / persist decision 分开。
- **must provide not finasresult bundled ≠ empty keep current / as a result of executing not candidate：** 官方把 477 item 1 和 477 bundled / 458 / 477 item 2 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| must provide 四列 | 不是 already changed set / H+1 | 不是 finasresult bundled（477） |
| must provide 四列 | 不是 already settled / persist decision | 不是 finresp bundled（363） |
| must provide 四列 | 不是 already finasresult bundled | 不是 empty keep current（458） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock must provide values not already changed set / settled 正式三事（477 余量），必须分开 must provide 四列是不是 already changed validator set / H+1 effective interchangeable / 471 fincparam interchangeable / 459 validator_updates interchangeable、must provide 是不是 already Finalize + Commit 交差 / persist decision interchangeable / 478 finpersist interchangeable / 363 finresp interchangeable、must provide 是不是 already finasresult bundled interchangeable / 458 finempty interchangeable / 477 item 2 not candidate interchangeable。可以跳过「看见 must provide 就已经改了集合 interchangeable」。不要另写怎样编回包四列。

## 本页不抄

- 怎样编回包四列、怎样写空更新、怎样在 Finalize 套用 candidate。
- FinalizeBlock must provide values bundled。那是不变量 477。
- as a result of executing not candidate。那是不变量 477 item 2 余量。
- Finalize 回包义务 bundled。那是不变量 363。
- FinalizeBlock 空更新 keep current。那是不变量 458。
- FinalizeBlockResponse validator_updates H→H+1。那是不变量 471。
