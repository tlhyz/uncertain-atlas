# 反模式：把 Finalize 没回 not already cleared / not already changed / not already settled 正式三事（319 余量） 卖成 已经清掉 / 已经改了 / 已经交差

**层次**：实现 / ConsensusParams。  
**分类**：建议（产品）。  
**对应例**：[worked-example-consensusparams-notcleared-vs-bundled.md](../../tracks/implementation/worked-example-consensusparams-notcleared-vs-bundled.md)。

官方把 InitChain 空参数 / Finalize 没回 / 只改一个字段 三条核心句写成三件独立的实现事。把它们卖成已经清掉 / 已经改了 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 没回 正式三事（319 余量），必须分开 not already cleared、not already changed、not already settled 三件事，不要和 319 / 333 / 471 / 908 / 910 糊成一句。

## 和相邻反模式

- [consensusparams-notnoparams-sold-as-bundled](consensusparams-notnoparams-sold-as-bundled.md) 是 InitChain 空参数单句边界（908 item 1），不是本页 Finalize 回空什么也不做边界。
- Finalize 回了 consensus_param_updates 就已经清掉是不变量 471 / 712，不是本页 Finalize 没回边界。
