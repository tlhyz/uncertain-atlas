# 例：看见 consensus_param_updates H apply to H+1 is not already effective at H interchangeable / not already validator_updates H+2 voting interchangeable / not already app-requirements delay interchangeable

**层次**：实现 / FinalizeBlockResponse consensus_param_updates H→H+1 not effective at H / not validator_updates H+2 / not app-requirements delay 正式三事（471 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Response / Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「FinalizeBlockResponse consensus_param_updates H→H+1 not effective at H / not validator_updates H+2 / not app-requirements delay 正式三事（471 余量）/ not 710 fincparam-nothatH interchangeable / not 471 fincparam-vs-heffective bundled interchangeable」，不是 FinalizeBlockResponse consensus_param_updates H→H+1 正式三事 bundled（471），也不是 validator_updates H+1/H+2/H+3（459）或 ConsensusParams 生效延迟（333）。不要另写怎样编 ConsensusParams。

## 官方三件事

1. **看见 `FinalizeBlockResponse.consensus_param_updates` returned for block `H` apply to the consensus params for block `H+1` / 看见块 H 回的用于 H+1 / H→H+1 is not already 已经在块 H 生效 interchangeable，也不是已经 FinalizeBlockResponse consensus_param_updates H→H+1 正式三事 bundled（471） interchangeable / 710 fincparam-nothatH interchangeable / 711 fincparam-notpartial interchangeable / 471 fincparam item 2 gas interchangeable，也不是已经 H apply to H+1 not effective at H / not validator_updates H+2 / not app-requirements delay 正式三事 bundled（471 item 1 余量） interchangeable / 471 fincparam item 1 interchangeable。**  
   官方 Usage 写：FinalizeBlockResponse.consensus_param_updates returned for block H apply to the consensus params for block H+1。看见 apply to H+1，不是已经在块 H 就用新 MaxBytes / MaxGas 验这块 interchangeable——本页从 471 item 1 侧钉 not effective at H 单句。471 fincparam vs heffective bundled unbundling 在本页 item 1 启动。

2. **看见能指 H+1 / 看见 Usage 这句 / H→H+1 is not already 已经 validator_updates 那种 H+2 才计票 / H+1 换人 interchangeable / 459 validatorupdate interchangeable，也不是已经 FinalizeBlockResponse consensus_param_updates H→H+1 正式三事 bundled（471） interchangeable / 710 fincparam-nothatH interchangeable / 471 fincparam item 3 empty interchangeable / 712 fincparam-notcleared interchangeable。**  
   官方把参数 H→H+1 和集合 H+2 才计票分开——471 bundled 第一件事常与 459 混成「看见 H→H+1 就已经换人 interchangeable」，本页钉 not validator_updates H+2 单句。

3. **看见参数 H→H+1 / 看见 Usage 这句 / apply to H+1 is not already 已经 app requirements 里 H 回了就对 H+1 立刻生效（333） interchangeable / 333 cparamdelay interchangeable，也不是已经 FinalizeBlockResponse consensus_param_updates H→H+1 正式三事 bundled（471） interchangeable / 710 fincparam-nothatH interchangeable / 711 fincparam-notpartial interchangeable。**  
   官方把 Methods Usage H→H+1 单句和 app requirements 生效延迟分开——333 钉 app requirements，本页钉 Methods Usage 侧 not app-requirements delay 单句。471 fincparam vs heffective bundled unbundling 在本页 item 1 启动。

怎样编 ConsensusParams、默认 MaxBytes / MaxGas、怎样选启用高度是规范里的做法，本页不抄。

## 官方为什么这样拆

- **H apply to H+1 not effective at H ≠ 已经在块 H 生效 interchangeable：** 官方把参数用于 H+1 和块 H 执行就用新参数分开。
- **H apply to H+1 not validator_updates H+2 ≠ 459 interchangeable：** 官方把参数 H→H+1 和集合 H+2 才计票分开。
- **H apply to H+1 not app-requirements delay ≠ 333 interchangeable：** 官方把 Methods Usage 和 app requirements 生效延迟分开；471 fincparam vs heffective bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| H apply to H+1 | 不是已经在块 H 生效 | 不是 gas/size/Deterministic（711/471 item 2） |
| 看见能指 H+1 | 不是 validator_updates H+2 才计票（459） | 不是 consensus_param_updates bundled（471） |
| 看见 Usage 这句 | 不是 app requirements 生效延迟（333） | 不是 may be empty（712/471 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse consensus_param_updates H→H+1 not effective at H / not validator_updates H+2 / not app-requirements delay 正式三事（471 余量），必须分开 H→H+1 是不是已经在块 H 生效、是不是集合 H+2 才计票 interchangeable / 459、是不是 app requirements 延迟 interchangeable / 333。可以跳过「看见回了 consensus_param_updates 就已经在块 H 生效」。不要另写怎样编 ConsensusParams。471 fincparam vs heffective bundled unbundling 在本页 item 1 启动；续 [`worked-example-fincparam-notpartial-vs-bundled.md`](worked-example-fincparam-notpartial-vs-bundled.md)（不变量 711 item 2）。

## 本页不抄

- 怎样编 ConsensusParams、默认 MaxBytes / MaxGas、怎样选启用高度。
- FinalizeBlockResponse consensus_param_updates H→H+1 正式三事 bundled。那是不变量 471。
- Changes to gas, size / Deterministic = Yes。那是不变量 471 item 2 余量 / 711。
- may be empty / keep current values。那是不变量 471 item 3 余量 / 712。
- validator_updates H+1/H+2/H+3。那是不变量 459。
- ConsensusParams 生效延迟。那是不变量 333。
