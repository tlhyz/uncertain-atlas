# 反模式：把 InitChain 空参数 not already no params / not already app empty params / not already settled 正式三事（319 余量） 卖成 已经没有参数 / 已经用了应用自己的空参数 / 已经交差

**层次**：实现 / ConsensusParams。  
**分类**：建议（产品）。  
**对应例**：[worked-example-consensusparams-notnoparams-vs-bundled.md](../../tracks/implementation/worked-example-consensusparams-notnoparams-vs-bundled.md)。

官方把 InitChain 空参数 / Finalize 没回 / 只改一个字段 三条核心句写成三件独立的实现事。把它们卖成已经没有参数 / 已经用了应用自己的空参数 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain 空参数 正式三事（319 余量），必须分开 not already no params、not already app empty params、not already settled 三件事，不要和 319 / 318 / 388 / 909 / 910 糊成一句。

## 和相邻反模式

- [validatorupdate-notempty-sold-as-bundled](validatorupdate-notempty-sold-as-bundled.md) 是 InitChain 空验证者名单（318/905），不是本页 InitChain 空参数边界。
- InitChain 请求 consensus_params 就已经没有参数是不变量 388 / 764，不是本页 InitChain 回空参数边界。
