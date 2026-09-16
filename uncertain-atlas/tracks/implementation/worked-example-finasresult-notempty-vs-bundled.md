# 例：看见提供了值 / 看见 tx_results 等来自执行结果 不是已经空更新就没有 must provide 义务；不是已经 CheckTx 过了就不需要 Finalize 再回 tx_results；不是已经 FinalizeBlock must provide values as a result of executing the block bundled（477） interchangeable / 已经 finasresult bundled interchangeable / 已经 empty keep current（458） interchangeable

**层次**：实现 / FinalizeBlock must provide values provided values not empty keep current / not CheckTx 正式三事（477 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「provided values not empty keep current / not CheckTx passed / not finasresult bundled（477） interchangeable / not finempty bundled（458 余量） interchangeable / not Code==0 fully valid（464） interchangeable」，不是 FinalizeBlock must provide values as a result of executing the block bundled（477），也不是 must provide values not already changed set / settled 正式三事（594 余量），也不是 as a result of executing the block not candidate 正式三事（595 余量）。不要另写怎样编回包四列。

## 官方三件事

规范把 FinalizeBlock Usage 里 The Application must provide values for … as a result of executing the block 和「已经空更新就没有 must provide 义务 interchangeable / 已经 CheckTx 过了就不需要 Finalize 再回 tx_results interchangeable / 已经是 finasresult bundled interchangeable」分开写成三件独立的实现事，不是「看见提供了值 就已经空着就没有义务、已经 CheckTx 过了就不用再回 tx_results、已经 477 finasresult bundled interchangeable」一件事：

1. **看见提供了值 / 看见 tx_results 等来自执行结果 / 看见 must provide values is not already empty validator_updates / consensus_param_updates means no must provide obligation interchangeable / 已经空着就没有 must provide 义务 interchangeable / 已经 keep current values interchangeable / 已经 empty keep current（458 余量） interchangeable，也不是已经 FinalizeBlock must provide values as a result of executing the block bundled（477） interchangeable / 596 notempty interchangeable / 477 finasresult interchangeable / 594 not settled interchangeable，也不是已经 FinalizeBlock 空更新 keep current bundled（458 余量） interchangeable / 458 finempty interchangeable / 471 fincparam interchangeable / 459 validator_updates H+1/H+2/H+3 interchangeable，也不是已经 must provide values not already changed set / settled bundled（594 余量） interchangeable / 594 not settled interchangeable / 363 finresp interchangeable。**  
   官方 Usage 写：must provide values … as a result of executing the block。另句写：The values for `validator_updates` or `consensus_param_updates` may be empty … CometBFT will keep the current values——空更新是 keep current values，不是没有 must provide 义务。477 item 3 常与 458 混成「看见空着就没有 must provide interchangeable」，本页钉 provided values not empty keep current 单句。看见提供了值，不是已经 finasresult bundled（477） interchangeable——477 另钉 must provide 四列 / as a result of executing 三事，本页只钉 item 3 边界。看见 must provide validator_updates，不是已经 must provide not changed set（594 余量） interchangeable——594 钉 item 1 单句，本页钉 item 3 单句。
2. **看见提供了值 / 看见 tx_results 等来自执行结果 / 看见 must provide tx_results is not already CheckTx 过了就不需要 Finalize 再回 tx_results interchangeable / 已经 CheckTx 弱过滤器（339） interchangeable / 已经 Process 回了 Accept（347） interchangeable / 已经过了池门就已经验完 interchangeable，也不是已经 FinalizeBlock must provide values as a result of executing the block bundled（477） interchangeable / 596 notempty interchangeable / 595 notcand interchangeable / 477 finasresult interchangeable，也不是已经 FinalizeBlock tx_results Code==0 完全合法 bundled（464 余量） interchangeable / 464 fintxcode interchangeable / 585 tx_results Code==0 interchangeable / 316 ExecTxResult 回执 interchangeable，也不是已经 CheckTx 过了就永远有效（301） interchangeable / 312 RECHECK interchangeable / 373 CheckTx 技术上可选 interchangeable。**  
   官方把 must provide tx_results 和 CheckTx 弱过滤器分开——477 item 3 常与 339 混成「看见 CheckTx 过了就不需要 Finalize 再回 tx_results interchangeable」，本页钉 not CheckTx passed 单句。看见 must provide tx_results，不是已经 Code == 0 only if fully valid（464 余量） interchangeable——464 钉 Code 语义，本页钉 must provide 义务边界。看见提供了 tx_results，不是已经 as a result of executing not candidate（595 余量） interchangeable——595 钉 Process / apply candidate，本页钉 item 3 单句。
3. **看见提供了值 / 看见 must provide values / 看见 tx_results 等来自执行结果 is not already finasresult bundled（477） interchangeable / 已经 must provide 四列 interchangeable / 已经 as a result of executing interchangeable / 已经 finresp bundled（363） interchangeable，也不是已经 FinalizeBlock must provide values not already changed set / settled bundled（594 余量） interchangeable / 594 not settled interchangeable / 595 notcand interchangeable / 458 finempty interchangeable，也不是已经 Finalize 回包义务 bundled（363 余量） interchangeable / 363 finresp interchangeable / 586 finequiv interchangeable / 404 回包余量 interchangeable，也不是已经 FinalizeBlock tx_results Code==0 完全合法 bundled（464 余量） interchangeable / 464 fintxcode interchangeable / 335 Finalize 落盘禁令 interchangeable。**  
   官方把 provided values、must provide 义务、empty keep current 和 CheckTx 过了 分开——477 item 3 常与 477 bundled / 363 混成「看见提供了值 就已经 finasresult bundled interchangeable」，本页钉 not finasresult bundled not empty keep current not CheckTx 单句。看见提供了值，不是已经 must provide not settled（594 余量） interchangeable——594 另钉 changed set / settled，本页钉 item 3 第三件事。看见 must provide tx_results，不是已经 Finalize 改了就已经交差（335） interchangeable——335 钉落盘禁令，本页钉 must provide 单句。

怎样编回包四列、怎样写空更新、怎样编 tx_results 是规范里的做法，本页不抄。FinalizeBlock must provide values bundled（477）、FinalizeBlock 空更新 keep current bundled（458 余量）、FinalizeBlock must provide values not already changed set / settled（594 余量）、FinalizeBlock must provide values as a result of executing not candidate（595 余量）是另外那套，本页不抄。

## 官方为什么这样拆

- **provided values not empty keep current ≠ finasresult bundled interchangeable：** 官方把 must provide 义务和 empty keep current 分开。
- **provided values not CheckTx passed ≠ CheckTx weak filter / Code==0 fully valid：** 官方把 must provide tx_results 和 CheckTx 过了 / Code 语义分开。
- **provided values not finasresult bundled ≠ not settled / not candidate / finresp bundled：** 官方把 477 item 3 和 594 / 595 / 363 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| provided values | 不是 already empty means no must provide | 不是 finasresult bundled（477） |
| must provide tx_results | 不是 already CheckTx passed | 不是 Code==0 fully valid（464） |
| provided values | 不是 already finasresult bundled | 不是 empty keep current bundled（458） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock must provide values provided values not empty keep current / not CheckTx 正式三事（477 余量），必须分开 provided values 是不是 already empty keep current means no must provide interchangeable / 458 finempty interchangeable / 471 fincparam interchangeable、must provide tx_results 是不是 already CheckTx passed interchangeable / 339 CheckTx 弱过滤器 interchangeable / 464 fintxcode interchangeable、provided values 是不是 already finasresult bundled interchangeable / 594 not settled interchangeable / 595 notcand interchangeable / 363 finresp interchangeable。可以跳过「看见提供了值 就已经空着就没有义务 interchangeable」。不要另写怎样编回包四列。

## 本页不抄

- 怎样编回包四列、怎样写空更新、怎样编 tx_results。
- FinalizeBlock must provide values bundled。那是不变量 477。
- FinalizeBlock 空更新 keep current bundled。那是不变量 458 余量。
- must provide values not already changed set / settled。那是不变量 594（477 item 1 余量）。
- as a result of executing not candidate。那是不变量 595（477 item 2 余量）。
- FinalizeBlock tx_results Code==0 完全合法。那是不变量 464 / 585。
