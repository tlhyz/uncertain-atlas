# 反模式：把 FinalizeBlockResponse consensus_param_updates H→H+1 not effective at H / not validator_updates H+2 / not app-requirements delay 正式三事（471 余量） 说成已经在块 H 生效 / 已经换人 / 已经 app requirements 延迟交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[H→H+1 ≠ bundled（471）](../../tracks/implementation/worked-example-fincparam-nothatH-vs-bundled.md)。

## 卖法

把 FinalizeBlockResponse consensus_param_updates 这句写成已经已经在块 H 生效 / 已经换人 / 已经 app requirements 延迟交差 interchangeable，或已经和 471 fincparam-vs-heffective bundled / fincparam-nothatH-sold-as-bundled interchangeable。

## 为什么错

官方把 FinalizeBlockResponse consensus_param_updates 三条核心句写成三件独立的实现事。把它们卖成已经在块 H 生效 / 已经换人 / 已经 app requirements 延迟交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse consensus_param_updates H→H+1 正式三事（471 余量），必须分开 not effective at H、not validator_updates H+2、not app-requirements delay 三件事，不要和 471 / 459 / 333 / 711 / 712 糊成一句。

## 和相邻反模式

- [fincparam-sold-as-heffective](fincparam-sold-as-heffective.md) 是 consensus_param_updates bundled（471），不是本页 item 1 单句边界。
- [fincparam-notpartial-sold-as-bundled](fincparam-notpartial-sold-as-bundled.md) 是 gas/size 单句边界（711 item 2），不是本页 H→H+1 边界。
