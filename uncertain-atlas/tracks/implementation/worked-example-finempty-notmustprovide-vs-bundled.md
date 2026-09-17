# 例：看见 validator_updates / consensus_param_updates 空着 / 看见 CometBFT will keep the current values 不是已经空着就没有 must provide 义务；不是已经 FinalizeBlock 空更新 keep current bundled（458） interchangeable / 已经 finempty bundled interchangeable；不是已经 Finalize 没回 / nil 就什么也不做

**层次**：实现 / FinalizeBlock empty keep current not no must provide obligation 正式三事（458 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「empty keep current not no must provide obligation / not finempty bundled（458） interchangeable / not nil means do nothing（319） interchangeable」，不是 FinalizeBlock must provide values as a result of executing the block bundled（477），也不是 provided values not empty keep current 正式三事（596 / 477 item 3 余量）。不要另写怎样编回包四列。

## 官方三件事

规范把 FinalizeBlock Usage 里 The values for `validator_updates` or `consensus_param_updates` may be empty. In this case, CometBFT will keep the current values 和「已经空着就没有 must provide 义务 interchangeable / 已经是 finempty bundled interchangeable / 已经 nil 就什么也不做 interchangeable」分开写成三件独立的实现事，不是「看见空着 就已经没有 must provide 义务、已经 keep current 就已经是同一句 bundled interchangeable、已经 nil 就已经 keep current interchangeable」一件事：

1. **看见 validator_updates / consensus_param_updates 空着 / 看见 may be empty / 看见 CometBFT will keep the current values is not already empty means no must provide obligation interchangeable / 已经空着就没有 must provide 义务 interchangeable / 已经 keep current values 就不需要回四列 interchangeable，也不是已经 FinalizeBlock must provide values as a result of executing the block bundled（477） interchangeable / 477 finasresult interchangeable / 596 notempty interchangeable / 477 item 3 interchangeable，也不是已经 must provide values not already changed set / settled bundled（594 余量） interchangeable / 594 not settled interchangeable / 471 fincparam interchangeable / 459 validator_updates H+1/H+2/H+3 interchangeable，也不是已经 Finalize 回包义务 bundled（363 余量） interchangeable / 363 finresp interchangeable / 586 finequiv interchangeable / 404 回包余量 interchangeable。**  
   官方 Usage 写 must provide values for … as a result of executing the block，另句写 may be empty … CometBFT will keep the current values——空更新是 keep current values 语义，不是没有 must provide 义务。458 item 1 常与 477 item 3 / 596 混成「看见空着就没有 must provide interchangeable」，本页从 458 侧钉 empty keep current not no must provide 单句。看见 may be empty，不是已经 finasresult bundled（477） interchangeable——477 另钉 must provide 四列 / as a result of executing / provided values 三事，本页只钉 458 item 1 边界。看见 keep the current values，不是已经 must provide not changed set（594 余量） interchangeable——594 钉 changed set / settled，本页钉 not no must provide 单句。
2. **看见 empty keep current / 看见 may be empty is not already FinalizeBlock 空更新 keep current bundled（458） interchangeable / 597 notmustprovide interchangeable / 458 finempty interchangeable / 已经 validator_updates 空 + consensus_param_updates 空 bundled interchangeable，也不是已经 provided values not empty keep current bundled（596 余量） interchangeable / 596 notempty interchangeable / 477 item 3 interchangeable / 339 CheckTx 弱过滤器 interchangeable，也不是已经 FinalizeBlockResponse validator_updates H→H+1 bundled（471 余量） interchangeable / 471 fincparam interchangeable / 459 validator_updates interchangeable / 333 ConsensusParams 生效延迟 interchangeable，也不是已经 must provide values as a result of executing not candidate bundled（595 余量） interchangeable / 595 notcand interchangeable / 460 fincand interchangeable / 466 executes block v interchangeable。**  
   官方把 empty keep current 和 finempty bundled / 596 notempty / 471 fincparam / 459 validator_updates 分开——458 item 1 常与 471 混成「看见空着就已经 keep current interchangeable 就等于没有 must provide」，本页钉 not finempty bundled not no must provide 单句。看见 may be empty，不是已经 596 notempty（477 item 3 余量） interchangeable——596 从 provided values 侧钉 not empty means no must provide，本页从 empty keep current 侧钉 not no must provide obligation。看见 keep current values，不是已经 as a result of executing not candidate（595 余量） interchangeable——595 钉 Process / apply candidate，本页钉 458 item 1 单句。
3. **看见 empty keep current / 看见 may be empty is not already Finalize 没回 / nil 就什么也不做 interchangeable / 已经 Finalize 没回 ConsensusParams 那种 nil 语义 interchangeable / 319 partial update interchangeable / 432 回包末栏 bundled interchangeable，也不是已经 FinalizeBlock 空更新 keep current bundled（458） interchangeable / 597 notmustprovide interchangeable / 458 finempty interchangeable / 471 fincparam keep current interchangeable，也不是已经 must provide tx_results 就不需要回 interchangeable / 464 fintxcode interchangeable / 585 tx_results Code==0 interchangeable / 316 ExecTxResult 回执 interchangeable，也不是已经 Finalize 改了就已经交差 interchangeable / 335 finpersist interchangeable / 478 finpersist interchangeable / 33 four gates interchangeable。**  
   官方把 empty keep current 和 nil / partial update / 没回 分开——458 item 1 常与 319 混成「看见空着就已经 nil 就什么也不做 interchangeable」，本页钉 empty keep current not nil means do nothing 单句。看见 may be empty，不是已经 432 回包末栏 bundled interchangeable——432 钉 consensus_param_updates / app_hash / next_block_delay 三栏，本页钉 458 item 1 第三件事。看见 keep the current values，不是已经 Finalize 落盘禁令（335） interchangeable——335 钉 persist decision，本页钉 must provide + empty keep current 单句。

怎样编回包四列、怎样写空更新、怎样选启用高度是规范里的做法，本页不抄。FinalizeBlock 空更新 keep current bundled（458）、FinalizeBlock must provide values bundled（477）、provided values not empty keep current（596）、Finalize 没回 / partial update（319）是另外那套，本页不抄。

## 官方为什么这样拆

- **empty keep current not no must provide ≠ finasresult bundled / 596 notempty interchangeable：** 官方把 must provide 义务和 empty keep current 语义分开。
- **empty keep current not finempty bundled ≠ fincparam / validator_updates H+1 effective interchangeable：** 官方把 458 item 1 和 471 / 459 / 333 分开。
- **empty keep current not nil means do nothing ≠ 319 partial update / 335 persist interchangeable：** 官方把 keep current values 和 nil / 没回 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| empty keep current | 不是 already no must provide obligation | 不是 finasresult bundled（477） |
| may be empty | 不是 already finempty bundled | 不是 596 notempty（477 item 3） |
| keep current values | 不是 already nil / do nothing | 不是 Finalize 没回（319） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock empty keep current not no must provide obligation 正式三事（458 余量），必须分开 empty keep current 是不是 already no must provide obligation interchangeable / 477 finasresult interchangeable / 596 notempty interchangeable、empty keep current 是不是 already finempty bundled interchangeable / 471 fincparam interchangeable / 459 validator_updates interchangeable、empty keep current 是不是 already nil means do nothing interchangeable / 319 partial update interchangeable / 432 回包末栏 interchangeable。可以跳过「看见空着 就已经没有 must provide 义务 interchangeable」。不要另写怎样编回包四列。

## 本页不抄

- 怎样编回包四列、怎样写空更新、怎样选启用高度。
- FinalizeBlock 空更新 keep current bundled 三事。那是不变量 458。
- empty validator_updates keep current set not changed set。那是不变量 458 item 2 余量。
- empty consensus_param_updates keep current not H+1 effective。那是不变量 458 item 3 余量。
- provided values not empty keep current。那是不变量 596（477 item 3 余量）。
- FinalizeBlock must provide values bundled。那是不变量 477。
