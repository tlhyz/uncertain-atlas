# 反模式：把 只改一个字段 not already only that field / not already rest kept / not already settled 正式三事（319 余量） 卖成 已经只改这一项 / 已经保持其余不变 / 已经交差

**层次**：实现 / ConsensusParams。  
**分类**：建议（产品）。  
**对应例**：[worked-example-consensusparams-notpartial-vs-bundled.md](../../tracks/implementation/worked-example-consensusparams-notpartial-vs-bundled.md)。

官方把 InitChain 空参数 / Finalize 没回 / 只改一个字段 三条核心句写成三件独立的实现事。把它们卖成已经只改这一项 / 已经保持其余不变 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看只改一个字段 正式三事（319 余量），必须分开 not already only that field、not already rest kept、not already settled 三件事，不要和 319 / 315 / 299 / 471 / 908 / 909 糊成一句。

## 和相邻反模式

- [consensusparams-notcleared-sold-as-bundled](consensusparams-notcleared-sold-as-bundled.md) 是 Finalize 没回单句边界（909 item 2），不是本页不空字段整份套上边界。
- Finalize 回了 gas/size 就已经只改一项是不变量 471 / 711，不是本页只填一项边界。
