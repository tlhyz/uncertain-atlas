# 反模式：把 FinalizeBlockResponse consensus_param_updates gas/size/Deterministic Yes not only one field / not finrespend bundled / not next_block_delay nondet means whole gate 正式三事（471 余量） 说成已经只改一项 / 已经回包末栏交差 / 已经整门非确定

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[gas/size/Deterministic ≠ bundled（471）](../../tracks/implementation/worked-example-fincparam-notpartial-vs-bundled.md)。

## 卖法

把 FinalizeBlockResponse consensus_param_updates 这句写成已经已经只改一项 / 已经回包末栏交差 / 已经整门非确定 interchangeable，或已经和 471 fincparam-vs-heffective bundled / fincparam-notpartial-sold-as-bundled interchangeable。

## 为什么错

官方把 FinalizeBlockResponse consensus_param_updates 三条核心句写成三件独立的实现事。把它们卖成已经只改一项 / 已经回包末栏交差 / 已经整门非确定，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse consensus_param_updates gas/size 正式三事（471 余量），必须分开 not only one field、not finrespend bundled、not next_block_delay nondet means whole gate 三件事，不要和 471 / 319 / 432 / 469 / 710 / 712 糊成一句。

## 和相邻反模式

- [fincparam-sold-as-heffective](fincparam-sold-as-heffective.md) 是 consensus_param_updates bundled（471），不是本页 item 2 单句边界。
- [fincparam-nothatH-sold-as-bundled](fincparam-nothatH-sold-as-bundled.md) 是 H→H+1 单句边界（710 item 1），不是本页 gas/size 边界。
