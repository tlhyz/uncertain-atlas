# 例：看见 validator_updates 空着 / 看见 CometBFT will keep the current values 不是已经 validator_updates 空则没有集合 / empty means no validator set；不是已经 changed validator set / H+1 换人 / validator_updates 非空 interchangeable；不是已经 FinalizeBlock 空更新 keep current bundled（458） interchangeable / 已经 finempty bundled interchangeable

**层次**：实现 / FinalizeBlock empty keep current not changed set / H+1 effective 正式三事（458 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「empty validator_updates keep current set not no set / not changed set / H+1 effective / not finempty bundled（458） interchangeable」，不是 FinalizeBlock empty keep current not no must provide obligation 正式三事（597 / 458 item 1 余量），也不是 must provide values not already changed set / settled 正式三事（594 / 477 item 1 余量）。不要另写怎样编回包四列。

## 官方三件事

规范把 FinalizeBlock Usage 里 validator_updates may be empty … CometBFT will keep the current values 和「已经 validator_updates 空则没有集合 interchangeable / 已经 changed validator set / H+1 换人 interchangeable / 已经是 finempty bundled interchangeable」分开写成三件独立的实现事，不是「看见 validator_updates 空着 就已经没有集合、已经 keep current 就已经改了集合 interchangeable、已经 finempty bundled interchangeable」一件事：

1. **看见 validator_updates 空着 / 看见 may be empty / 看见 CometBFT will keep the current values is not already empty means no validator set interchangeable / 已经 validator_updates 空则保持当前集合就已经没有集合 interchangeable / 已经 empty means no validator set interchangeable，也不是已经 FinalizeBlock 空更新 keep current bundled（458） interchangeable / 598 notnoset interchangeable / 597 notmustprovide interchangeable / 458 finempty interchangeable，也不是已经 must provide values not already changed set / settled bundled（594 余量） interchangeable / 594 not settled interchangeable / 477 finasresult interchangeable / 363 finresp interchangeable，也不是已经 FinalizeBlockResponse validator_updates H→H+1 bundled（471 余量） interchangeable / 471 fincparam interchangeable / 459 validator_updates H+1/H+2/H+3 interchangeable / 35 集合 vs 参数延迟 interchangeable。**  
   官方 Usage 写 may be empty … CometBFT will keep the current values——空更新是保留当前集合，不是没有 validator set。458 item 2 常与「看见空着就没有集合 interchangeable」混成一句，本页钉 empty keep current set not no set 单句。看见 validator_updates 空，不是已经 must provide not changed set（594 余量） interchangeable——594 从 must provide 侧钉 not changed set，本页从 empty keep current 侧钉 not no set。看见 keep the current values，不是已经 finempty bundled（458） interchangeable——458 另钉 must provide + 空更新 bundled 三事，本页只钉 item 2 边界。
2. **看见 empty keep current / 看见 validator_updates 空着 is not already changed validator set / H+1 换人 interchangeable / 已经 validator_updates 非空 interchangeable / 已经 H+1 生效 interchangeable / 已经改了集合 interchangeable，也不是已经 FinalizeBlock 空更新 keep current bundled（458） interchangeable / 598 notnoset interchangeable / 597 notmustprovide interchangeable / 458 finempty interchangeable，也不是已经 FinalizeBlockResponse validator_updates H→H+1 bundled（471 余量） interchangeable / 471 fincparam interchangeable / 459 validator_updates H+1/H+2/H+3 interchangeable / 35 集合 vs 参数延迟 interchangeable，也不是已经 must provide values not already changed set / settled bundled（594 余量） interchangeable / 594 not settled interchangeable / 477 item 1 interchangeable / 596 notempty interchangeable，也不是已经 provided values not empty keep current bundled（596 余量） interchangeable / 477 item 3 interchangeable / 339 CheckTx 弱过滤器 interchangeable。**  
   官方把 empty keep current 和 validator_updates 非空 / H+1 生效延迟分开——458 item 2 常与 459 / 471 混成「看见空着就已经 keep current interchangeable 就等于已经改了集合 / 已经在 H+1 换人 interchangeable」，本页钉 not changed set not H+1 effective 单句。看见 may be empty，不是已经 validator_updates 非空那种已经改了集合 interchangeable——459 钉 H+1/H+2/H+3 生效延迟，本页钉 empty keep current 单句。看见 keep current values，不是已经 must provide not settled（594 余量） interchangeable——594 钉 must provide 四列 not settled，本页钉 458 item 2 单句。
3. **看见 empty keep current / 看见 validator_updates 空着 is not already finempty bundled（458） interchangeable / 已经 must provide + validator_updates 空 + consensus_param_updates 空 bundled interchangeable / 597 notmustprovide interchangeable / 596 notempty interchangeable / 477 finasresult interchangeable，也不是已经 empty keep current not no must provide obligation bundled（597 余量） interchangeable / 597 notmustprovide interchangeable / 319 nil means do nothing interchangeable / 432 回包末栏 bundled interchangeable，也不是已经 empty consensus_param_updates keep current not H+1 effective bundled（458 item 3 余量） interchangeable / 471 fincparam keep current interchangeable / 333 ConsensusParams 生效延迟 interchangeable，也不是已经 must provide values as a result of executing not candidate bundled（595 余量） interchangeable / 595 notcand interchangeable / 460 fincand interchangeable / 466 executes block v interchangeable。**  
   官方把 empty validator_updates keep current、empty consensus_param_updates keep current 和 finempty bundled 分开——458 item 2 常与 458 bundled / 597 item 1 混成「看见 validator_updates 空着 就已经 finempty bundled interchangeable」，本页钉 not finempty bundled not changed set 单句。看见 may be empty，不是已经 597 notmustprovide（458 item 1 余量） interchangeable——597 钉 not no must provide obligation，本页钉 item 2 单句。看见 keep current set，不是已经 458 item 3 consensus_param_updates keep current interchangeable——458 item 3 另钉参数 H→H+1，本页钉 validator_updates 空 keep current set 单句。

怎样编回包四列、怎样写空更新、怎样选 H+1/H+2/H+3 生效高度是规范里的做法，本页不抄。FinalizeBlock 空更新 keep current bundled（458）、empty keep current not no must provide（597）、must provide not changed set / settled（594）、validator_updates H→H+1（471/459）是另外那套，本页不抄。

## 官方为什么这样拆

- **empty keep current set not no set ≠ finempty bundled / 597 notmustprovide interchangeable：** 官方把 keep current values 和 no validator set / no must provide 分开。
- **empty keep current not changed set / H+1 effective ≠ 459 / 471 / 594 not settled interchangeable：** 官方把 empty keep current 和 validator_updates 非空 / H+1 生效延迟分开。
- **empty validator_updates keep current not finempty bundled ≠ 458 item 3 / 596 / 477 finasresult interchangeable：** 官方把 458 item 2 和 finempty bundled / item 1 / item 3 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| validator_updates empty | 不是 already no validator set | 不是 finempty bundled（458） |
| empty keep current | 不是 already changed set / H+1 | 不是 must provide not settled（594） |
| validator_updates empty | 不是 already finempty bundled | 不是 not no must provide（597） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock empty keep current not changed set / H+1 effective 正式三事（458 余量），必须分开 empty keep current set 是不是 already no validator set interchangeable / 597 notmustprovide interchangeable / 458 finempty interchangeable、empty keep current 是不是 already changed validator set / H+1 effective interchangeable / 459 validator_updates interchangeable / 471 fincparam interchangeable / 594 not settled interchangeable、empty keep current 是不是 already finempty bundled interchangeable / 596 notempty interchangeable / 458 item 3 consensus_param_updates interchangeable。可以跳过「看见 validator_updates 空着 就已经没有集合 interchangeable」。不要另写怎样编回包四列。

## 本页不抄

- 怎样编回包四列、怎样写空更新、怎样选 H+1/H+2/H+3 生效高度。
- FinalizeBlock 空更新 keep current bundled 三事。那是不变量 458。
- empty keep current not no must provide obligation。那是不变量 597（458 item 1 余量）。
- empty consensus_param_updates keep current not H+1 effective。那是不变量 458 item 3 余量。
- must provide values not already changed set / settled。那是不变量 594（477 item 1 余量）。
- validator_updates H+1/H+2/H+3。那是不变量 459。
