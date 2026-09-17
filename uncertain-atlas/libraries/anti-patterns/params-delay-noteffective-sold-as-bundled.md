# 反模式：把 本高回了 ConsensusParams not already effective at H / not already this-height Prepare / not already settled 正式三事（333 余量） 卖成 已经在本高生效 / 已经本高提议按新上限 / 已经交差

**层次**：实现 / ConsensusParams 生效延迟。  
**分类**：建议（产品）。  
**对应例**：[worked-example-params-delay-noteffective-vs-bundled.md](../../tracks/implementation/worked-example-params-delay-noteffective-vs-bundled.md)。

官方把本高回了 ConsensusParams / H+1 立刻用了新参数 / 参数更新写了 H+1 三条核心句写成三件独立的实现事。把它们卖成已经在本高生效 / 已经本高提议按新上限 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看本高回了 ConsensusParams 正式三事（333 余量），必须分开 not already effective at H、not already this-height Prepare、not already settled 三件事，不要和 333 / 471 / 319 / 912 / 913 糊成一句。

## 和相邻反模式

- [fincparam-nothatH-sold-as-bundled](fincparam-nothatH-sold-as-bundled.md) 是 FinalizeBlockResponse consensus_param_updates H→H+1（471/710），不是本页 Formal Requirements 本高回了参数延迟边界。
- InitChain 空参数已经没有参数是不变量 319 / 908，不是本页本高回了何时生效边界。
