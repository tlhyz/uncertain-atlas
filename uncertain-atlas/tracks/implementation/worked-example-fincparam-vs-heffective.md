# 例：看见块 H 回的 `FinalizeBlockResponse.consensus_param_updates` 用于块 H+1 的共识参数不是已经在块 H 生效；看见 Changes to gas, size, and other consensus-related parameters / Deterministic = Yes 不是已经只填一个字段就只改这一项；看见 may be empty / CometBFT keeps the current values 不是已经清掉参数

**层次**：实现 / FinalizeBlockResponse consensus_param_updates H→H+1 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Response / Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「块 H 回的 consensus_param_updates 用于 H+1 不是已经在块 H 生效 / Changes to gas, size, and other consensus-related parameters / Deterministic = Yes 不是已经只填一个字段就只改这一项 / may be empty / keep current values 不是已经清掉参数」，不是 Finalize 回包末栏 bundled 三事，也不是 app requirements 里参数哪一高度生效那套，也不是 validator_updates H+1/H+2/H+3 那套。不要另写怎样编 ConsensusParams、怎样选 MaxBytes / MaxGas。

## 官方三件事

规范把 FinalizeBlock Usage 里 `FinalizeBlockResponse.consensus_param_updates` 的 H→H+1 生效、gas/size/共识相关参数改动 / Deterministic = Yes、空则保持当前值写成三件独立的实现事，不是「看见 Finalize 回了 consensus_param_updates 就已经在块 H 生效、已经只改一项、已经清掉参数」一件事：

1. **看见 `FinalizeBlockResponse.consensus_param_updates` returned for block `H` apply to the consensus params for block `H+1` / 看见块 H 回的用于 H+1 不是已经在块 H 生效，也不是已经 validator_updates 那种 H+2 才计票 / H+1 换人。**  
   官方 Usage 写：`FinalizeBlockResponse.consensus_param_updates` returned for block `H` apply to the consensus params for block `H+1`。For more information on the consensus parameters, see the consensus parameters section in app requirements。看见 returned for block H apply to H+1，不是已经在块 H 就用新 MaxBytes / MaxGas 验这块。看见能指 H+1，不是已经高度 H 的 `validator_updates` 已经在 H+1 按新 `ValidatorsHash` 计票那种已经在 H+1 换人（459）。看见参数 H→H+1，不是已经集合更新 H+1 只改 Next / H+2 才生效 / H+3 才带 last_commit 那种已经在 H+1 换人 interchangeable（35 总则也不把参数和集合混成同一张表）。
2. **看见 Changes to gas, size, and other consensus-related parameters / Deterministic = Yes / 看见改了 gas、大小和其它共识相关参数 不是已经只填一个字段就只改这一项，也不是已经是 finrespend bundled 里那句 interchangeable。**  
   官方 Response 表写：`consensus_param_updates` 是 Changes to gas, size, and other consensus-related parameters。Deterministic 列是 Yes。看见能改 gas / size / 其它共识相关参数，不是已经只填 `Block.MaxBytes` 其它 `Block` 字段就保持原值那种只改这一项（319）。看见 Deterministic = Yes，不是已经像 `next_block_delay` 那样 Deterministic = No（469）就代表 Finalize 回包整门都可以非确定。看见是 consensus_param_updates 栏，不是已经 Finalize 回包末栏 bundled 里「consensus_param_updates / app_hash / next_block_delay 三栏」（432）就已经是同一句 interchangeable——432 另钉 bundled 三栏，本页只钉 consensus_param_updates H→H+1 正式三事。
3. **看见 may be empty / CometBFT will keep the current values / 看见空着则保持当前值 不是已经清掉参数，也不是已经 InitChain 空参数那种没有参数。**  
   官方 Usage 写：The values for `FinalizeBlockResponse.validator_updates`, or `FinalizeBlockResponse.consensus_param_updates` may be empty. In this case, CometBFT will keep the current values。看见 consensus_param_updates 空，不是已经 Finalize 没回 ConsensusParams 那种 nil 就什么也不做（319）就已经是同一句 interchangeable。看见 keep the current values，不是已经清掉参数。看见空着，不是已经 H 的参数更新已经在 H+1 生效（333）就已经改了——333 来自 app requirements 钉哪一高度生效，本页只钉 abci++_methods Usage 这句 keep current。看见 may be empty，不是已经 FinalizeBlock 空更新保持当前值 bundled（458）三事里第三句就已经是同一句 interchangeable——458 另钉必须回四列 / validator_updates 空 / consensus_param_updates 空 bundled，本页只钉 consensus_param_updates 专用切片。

怎样编 ConsensusParams、默认 MaxBytes / MaxGas、怎样选启用高度是规范里的做法，本页不抄。Finalize 回包末栏 bundled（432）是 consensus_param_updates / app_hash / next_block_delay 三栏那套另一切片，ConsensusParams 生效延迟（333）是 app requirements 里 H 回了就对 H+1 立刻生效那套另一切片，validator_updates H+1/H+2/H+3（459）是集合延迟那套另一切片，集合 vs 参数延迟总则（35）是高层对照那套另一切片，Finalize 没回 / 只填一项（319）是 nil 语义和 partial update 那套另一切片，FinalizeBlock 空更新保持当前值（458）是 must provide / validator_updates 空 / consensus_param_updates 空 bundled 那套另一切片，本页不抄。

## 官方为什么这样拆

- **returned for block H apply to H+1 ≠ 已经在块 H 生效 / 已经 validator_updates H+2 才计票：** 官方把参数 H→H+1 生效和块 H 执行、集合 H+2 才生效分开。
- **Changes to gas, size, consensus-related / Deterministic = Yes ≠ 已经只填一个字段就只改这一项 / 已经是 finrespend bundled：** 官方把 consensus_param_updates 必须确定、partial update 规则和 bundled 三栏分开。
- **may be empty / keep current values ≠ 已经清掉参数 / 已经 InitChain 空参数：** 官方把 keep current values 和 nil 什么也不做、空参数语义分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| returned for block H apply to H+1 | 不是已经在块 H 生效 | 不是 validator_updates H+1/H+2/H+3（459） |
| Changes to gas, size / Deterministic = Yes | 不是已经只填一个字段就只改这一项 | 不是 Finalize 回包末栏 bundled（432） |
| may be empty / keep current values | 不是已经清掉参数 | 不是 Finalize 没回 ConsensusParams（319） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Finalize 回了 consensus_param_updates 就已经在块 H 生效、已经只改一项、已经清掉参数」，必须分开块 H 回的用于 H+1 是不是已经在块 H 生效、Changes to gas, size / Deterministic = Yes 是不是已经只填一个字段就只改这一项、may be empty / keep current values 是不是已经清掉参数。可以跳过「看见回了 consensus_param_updates 就已经在块 H 生效」。不要另写怎样编 ConsensusParams。471 fincparam vs heffective bundled unbundling 完成（710 item 1 / 711 item 2 / 712 item 3）；精读 [`worked-example-fincparam-nothatH-vs-bundled.md`](worked-example-fincparam-nothatH-vs-bundled.md)（不变量 710 item 1）。

## 本页不抄

- 怎样编 ConsensusParams、默认 MaxBytes / MaxGas、怎样选启用高度。
- Finalize 回包末栏 bundled 三事。那是不变量 432。
- ConsensusParams 生效延迟（app requirements）。那是不变量 333。
- validator_updates H+1/H+2/H+3。那是不变量 459。
- 集合 vs 参数延迟总则。那是不变量 35。
- Finalize 没回 / 只填一项。那是不变量 319。
- FinalizeBlock 空更新保持当前值 bundled。那是不变量 458。
