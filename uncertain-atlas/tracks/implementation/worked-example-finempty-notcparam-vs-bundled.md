# 例：看见 consensus_param_updates 空着 / 看见 CometBFT will keep the current values 不是已经清掉参数 / empty means no ConsensusParams；不是已经块 H 回的用于 H+1 就已经在块 H 生效 / 已经改了 gas/size interchangeable；不是已经 FinalizeBlock 空更新 keep current bundled（458） interchangeable / 已经 finempty bundled interchangeable

**层次**：实现 / FinalizeBlock empty consensus_param_updates keep current not H+1 effective 正式三事（458 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「empty consensus_param_updates keep current not clear params / not H+1 effective already changed / not finempty bundled（458） interchangeable」，不是 FinalizeBlock empty keep current not no must provide obligation 正式三事（597 / 458 item 1 余量），也不是 empty keep current not changed set / H+1 effective 正式三事（598 / 458 item 2 余量），也不是 FinalizeBlockResponse consensus_param_updates H→H+1 正式三事（471）。不要另写怎样编 ConsensusParams。

## 官方三件事

规范把 FinalizeBlock Usage 里 consensus_param_updates may be empty … CometBFT will keep the current values 和「已经清掉参数 interchangeable / 已经在块 H 生效 interchangeable / 已经是 finempty bundled interchangeable」分开写成三件独立的实现事，不是「看见 consensus_param_updates 空着 就已经清掉参数、已经 keep current 就已经在 H+1 生效 interchangeable、已经 finempty bundled interchangeable」一件事：

1. **看见 consensus_param_updates 空着 / 看见 may be empty / 看见 CometBFT will keep the current values is not already empty means clear ConsensusParams interchangeable / 已经清掉参数 interchangeable / 已经 InitChain 空参数 interchangeable / 已经没有 ConsensusParams interchangeable，也不是已经 FinalizeBlock 空更新 keep current bundled（458） interchangeable / 599 notcparam interchangeable / 597 notmustprovide interchangeable / 598 notnoset interchangeable / 458 finempty interchangeable，也不是已经 Finalize 没回 / nil 就什么也不做 interchangeable / 319 partial update interchangeable / 432 回包末栏 bundled interchangeable / 335 finpersist interchangeable，也不是已经 must provide values not already changed set / settled bundled（594 余量） interchangeable / 594 not settled interchangeable / 477 finasresult interchangeable / 363 finresp interchangeable。**  
   官方 Usage 写 may be empty … CometBFT will keep the current values——空更新是保留当前 ConsensusParams，不是清掉参数。458 item 3 常与 319 混成「看见空着就已经 nil 就什么也不做 interchangeable」，本页钉 empty consensus_param_updates keep current not clear params 单句。看见 may be empty，不是已经 Finalize 没回 ConsensusParams（319） interchangeable——319 钉 nil / partial update 语义，本页钉 keep current values 单句。看见 keep the current values，不是已经 finempty bundled（458） interchangeable——458 另钉 must provide + 空更新 bundled 三事，本页只钉 item 3 边界。
2. **看见 empty consensus_param_updates keep current / 看见 may be empty is not already returned for block H apply to H+1 already effective at H interchangeable / 已经块 H 回的用于 H+1 就已经在块 H 生效 interchangeable / 已经改了 gas / size / 其它共识相关参数 interchangeable / 已经 H 的参数更新已经在 H+1 生效 interchangeable，也不是已经 FinalizeBlockResponse consensus_param_updates H→H+1 bundled（471 余量） interchangeable / 471 fincparam interchangeable / 333 ConsensusParams 生效延迟 interchangeable / 35 集合 vs 参数延迟 interchangeable / 432 回包末栏 bundled interchangeable，也不是已经 FinalizeBlock 空更新 keep current bundled（458） interchangeable / 599 notcparam interchangeable / 598 notnoset interchangeable / 459 validator_updates H+1/H+2/H+3 interchangeable，也不是已经 empty validator_updates keep current not changed set bundled（598 余量） interchangeable / 598 notnoset interchangeable / 594 not settled interchangeable / 596 notempty interchangeable。**  
   官方把 empty keep current 和 consensus_param_updates 非空 / H→H+1 生效分开——458 item 3 常与 471 混成「看见空着就已经 keep current interchangeable 就等于已经在 H+1 生效 interchangeable」，本页钉 empty keep current not H+1 effective already changed 单句。看见 may be empty，不是已经 471 fincparam（非空 H→H+1） interchangeable——471 钉 returned for block H apply to H+1，本页钉 empty keep current 单句。看见 keep current values，不是已经 333 ConsensusParams 生效延迟 interchangeable——333 来自 app requirements，本页钉 Usage may be empty 单句。
3. **看见 empty consensus_param_updates keep current / 看见 may be empty is not already finempty bundled（458） interchangeable / 已经 must provide + validator_updates 空 + consensus_param_updates 空 bundled interchangeable / 597 notmustprovide interchangeable / 598 notnoset interchangeable / 596 notempty interchangeable / 477 finasresult interchangeable，也不是已经 empty keep current not no must provide obligation bundled（597 余量） interchangeable / 597 notmustprovide interchangeable / 319 nil means do nothing interchangeable，也不是已经 empty validator_updates keep current not changed set bundled（598 余量） interchangeable / 598 notnoset interchangeable / 459 validator_updates interchangeable，也不是已经 Changes to gas, size / Deterministic = Yes bundled（471 item 2 余量） interchangeable / 432 finrespend bundled interchangeable / 469 next_block_delay nondet interchangeable。**  
   官方把 empty consensus_param_updates keep current、empty validator_updates keep current 和 finempty bundled 分开——458 item 3 常与 458 bundled / 597 / 598 混成「看见 consensus_param_updates 空着 就已经 finempty bundled interchangeable」，本页钉 not finempty bundled not clear params not H+1 effective 单句。看见 may be empty，不是已经 597 notmustprovide（458 item 1 余量） interchangeable——597 钉 not no must provide，本页钉 item 3 单句。看见 keep current params，不是已经 598 notnoset（458 item 2 余量） interchangeable——598 钉 validator_updates 空 keep current set，本页钉 consensus_param_updates 空 keep current 单句。

怎样编 ConsensusParams、默认 MaxBytes / MaxGas、怎样选启用高度是规范里的做法，本页不抄。FinalizeBlock 空更新 keep current bundled（458）、empty keep current not no must provide（597）、empty keep current not changed set（598）、consensus_param_updates H→H+1（471）、Finalize 没回 partial update（319）是另外那套，本页不抄。

## 官方为什么这样拆

- **empty consensus_param_updates keep current not clear params ≠ nil / 319 partial update interchangeable：** 官方把 keep current values 和 nil / 没回 分开。
- **empty keep current not H+1 effective already changed ≠ 471 fincparam / 333 effective delay interchangeable：** 官方把 empty keep current 和 returned for block H apply to H+1 分开。
- **empty consensus_param_updates keep current not finempty bundled ≠ 597 / 598 / 596 / 477 finasresult interchangeable：** 官方把 458 item 3 和 finempty bundled / item 1 / item 2 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| consensus_param_updates empty | 不是 already clear params | 不是 Finalize 没回（319） |
| empty keep current | 不是 already H+1 effective at H | 不是 consensus_param_updates H→H+1（471） |
| consensus_param_updates empty | 不是 already finempty bundled | 不是 not no must provide（597） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock empty consensus_param_updates keep current not H+1 effective 正式三事（458 余量），必须分开 empty consensus_param_updates keep current 是不是 already clear params interchangeable / 319 nil interchangeable / 432 回包末栏 interchangeable、empty keep current 是不是 already H+1 effective at H interchangeable / 471 fincparam interchangeable / 333 effective delay interchangeable、empty keep current 是不是 already finempty bundled interchangeable / 597 notmustprovide interchangeable / 598 notnoset interchangeable / 596 notempty interchangeable。可以跳过「看见 consensus_param_updates 空着 就已经清掉参数 interchangeable」。不要另写怎样编 ConsensusParams。

## 本页不抄

- 怎样编 ConsensusParams、默认 MaxBytes / MaxGas、怎样选启用高度。
- FinalizeBlock 空更新 keep current bundled 三事。那是不变量 458。
- empty keep current not no must provide obligation。那是不变量 597（458 item 1 余量）。
- empty validator_updates keep current not changed set。那是不变量 598（458 item 2 余量）。
- consensus_param_updates H→H+1。那是不变量 471。
- Finalize 没回 / partial update。那是不变量 319。
