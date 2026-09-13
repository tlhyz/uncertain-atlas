# 反模式：把 FinalizeBlockResponse consensus_param_updates H→H+1 正式三事卖成已经在块 H 生效

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[consensus_param_updates H→H+1 ≠ 已经在块 H 生效](../../tracks/implementation/worked-example-fincparam-vs-heffective.md)。

## 卖法

- 「看见 Finalize 回了 `consensus_param_updates` 就已经在块 H 用新 MaxBytes / MaxGas 验这块。」
- 「看见 Changes to gas, size 就已经只填 `Block.MaxBytes` 其它字段保持原值。」
- 「看见空着就已经清掉参数 / 没有 ConsensusParams。」

## 为什么错

官方把块 H 回的 `consensus_param_updates` 用于块 H+1 的共识参数、Changes to gas, size, and other consensus-related parameters / Deterministic = Yes、may be empty / CometBFT will keep the current values 写成三件独立的实现事。把它们卖成已经在块 H 生效、只改一项、清掉参数，会把 H→H+1 生效、partial update 规则和 keep current 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 回包参数栏，必须分开 returned for block H apply to H+1、Changes to gas, size / Deterministic = Yes、may be empty / keep current values 三个名字，不要把它们卖成已经在块 H 生效。
