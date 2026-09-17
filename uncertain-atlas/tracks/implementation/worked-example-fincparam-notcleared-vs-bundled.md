# 例：看见 may be empty keep current values is not already params cleared interchangeable / not already InitChain empty params interchangeable / not already empty-update bundled interchangeable

**层次**：实现 / FinalizeBlockResponse consensus_param_updates may be empty keep current not params cleared / not InitChain empty params / not empty-update bundled 正式三事（471 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Response / Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「FinalizeBlockResponse consensus_param_updates may be empty keep current not params cleared / not InitChain empty params / not empty-update bundled 正式三事（471 余量）/ not 712 fincparam-notcleared interchangeable / not 471 fincparam-vs-heffective bundled interchangeable」，不是 FinalizeBlockResponse consensus_param_updates H→H+1 正式三事 bundled（471），也不是 Finalize 没回 ConsensusParams（319）或空更新 bundled（458）。不要另写怎样编 ConsensusParams。

## 官方三件事

1. **看见 may be empty / CometBFT will keep the current values / 看见空着则保持当前值 / empty is not already 已经清掉参数 interchangeable，也不是已经 FinalizeBlockResponse consensus_param_updates H→H+1 正式三事 bundled（471） interchangeable / 712 fincparam-notcleared interchangeable / 710 fincparam-nothatH interchangeable / 471 fincparam item 1 H→H+1 interchangeable，也不是已经 may be empty keep current not params cleared / not InitChain empty params / not empty-update bundled 正式三事 bundled（471 item 3 余量） interchangeable / 471 fincparam item 3 interchangeable。**  
   官方 Usage 写：The values for FinalizeBlockResponse.validator_updates, or FinalizeBlockResponse.consensus_param_updates may be empty. In this case, CometBFT will keep the current values。看见 keep the current values，不是已经清掉参数 interchangeable——本页从 471 item 3 侧钉 not params cleared 单句。471 fincparam vs heffective bundled unbundling 在本页 item 3 完成。

2. **看见空着 / 看见 Usage 这句 / empty is not already 已经 InitChain 空参数那种没有参数 interchangeable，也不是已经 FinalizeBlockResponse consensus_param_updates H→H+1 正式三事 bundled（471） interchangeable / 712 fincparam-notcleared interchangeable / 471 fincparam item 2 gas interchangeable / 711 fincparam-notpartial interchangeable。**  
   官方把 Finalize keep current 和 InitChain 空参数分开——471 bundled 第三件事常与创世空参数混成「看见空着就已经没有参数 interchangeable」，本页钉 not InitChain empty params 单句。

3. **看见 may be empty / 看见 Usage 这句 / empty is not already 已经 FinalizeBlock 空更新保持当前值 bundled（458） interchangeable / 458 finempty interchangeable / 已经 Finalize 没回 ConsensusParams（319） interchangeable / 319 finpartial interchangeable，也不是已经 FinalizeBlockResponse consensus_param_updates H→H+1 正式三事 bundled（471） interchangeable / 712 fincparam-notcleared interchangeable / 710 fincparam-nothatH interchangeable。**  
   官方把 consensus_param_updates 专用 keep current 和 458 空更新 bundled / 319 nil 分开。看见 may be empty，不是已经 458 bundled 交差 interchangeable。471 fincparam vs heffective bundled unbundling 在本页 item 3 完成。

怎样编 ConsensusParams、默认 MaxBytes / MaxGas、怎样选启用高度是规范里的做法，本页不抄。

## 官方为什么这样拆

- **may be empty keep current not params cleared ≠ 已经清掉参数 interchangeable：** 官方把 keep current values 和清掉参数分开。
- **may be empty keep current not InitChain empty params ≠ 创世空参数 interchangeable：** 官方把 Finalize 空着保持当前值和 InitChain 空参数分开。
- **may be empty keep current not empty-update bundled ≠ 458 / 319 interchangeable：** 官方把 Usage keep current 和空更新 bundled / nil 分开；471 fincparam vs heffective bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| may be empty / keep current values | 不是已经清掉参数 | 不是 H apply to H+1（710/471 item 1） |
| 看见空着 | 不是 InitChain 空参数 | 不是 gas/size/Deterministic（711/471 item 2） |
| 看见 Usage 这句 | 不是空更新 bundled（458） / 没回（319） | 不是 consensus_param_updates bundled（471） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse consensus_param_updates may be empty keep current not params cleared / not InitChain empty params / not empty-update bundled 正式三事（471 余量），必须分开 empty 是不是已经清掉参数、是不是 InitChain 空参数、是不是空更新 bundled interchangeable / 458 / 319。可以跳过「看见空着就已经清掉参数」。不要另写怎样编 ConsensusParams。471 fincparam vs heffective bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样编 ConsensusParams、默认 MaxBytes / MaxGas、怎样选启用高度。
- FinalizeBlockResponse consensus_param_updates H→H+1 正式三事 bundled。那是不变量 471。
- H apply to H+1。那是不变量 471 item 1 余量 / 710。
- Changes to gas, size / Deterministic = Yes。那是不变量 471 item 2 余量 / 711。
- FinalizeBlock 空更新保持当前值 bundled。那是不变量 458。
- Finalize 没回 / 只填一项。那是不变量 319。
