# 模式：把 FinalizeBlockResponse consensus_param_updates H→H+1 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Response / Usage。  
**例**：[consensus_param_updates H→H+1 ≠ 已经在块 H 生效](../../tracks/implementation/worked-example-fincparam-vs-heffective.md)。

## 三个名字

1. **returned for block H apply to H+1 不是已经在块 H 生效：** 看见块 H 回的用于 H+1 不是已经 validator_updates 那种 H+2 才计票 interchangeable。
2. **Changes to gas, size, consensus-related / Deterministic = Yes 不是已经只填一个字段就只改这一项：** 看见改了 gas、大小和其它共识相关参数不是已经 finrespend bundled 里那句 interchangeable。
3. **may be empty / keep current values 不是已经清掉参数：** 看见空着则保持当前值不是已经 InitChain 空参数 / Finalize 没回 nil 那种 interchangeable。

## 为什么要分开叫

官方把 returned for block H apply to H+1、Changes to gas, size, and other consensus-related parameters / Deterministic = Yes、may be empty / keep current values 写成三个名字。把它们叫成一个「看见 Finalize 回了 consensus_param_updates 就已经在块 H 生效、已经只改一项、已经清掉参数」，会把 H→H+1 生效、partial update 规则和 keep current 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Finalize 回了 consensus_param_updates」，先数清问的是 returned for block H apply to H+1 是不是已经在块 H 生效、Changes to gas, size / Deterministic = Yes 是不是已经只填一个字段就只改这一项，还是 may be empty / keep current values 是不是已经清掉参数，再决定要不要同一次发布。
