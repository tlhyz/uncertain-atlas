# 反模式：把 syncing_to_height not already full history / not already snapshot replay / not already settled 正式三事（382 余量） 说成已经有完整历史 / 已经是快照重放 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[syncing_to_height ≠ bundled（382）](../../tracks/implementation/worked-example-syncingheight-nothistory-vs-bundled.md)。

## 卖法

把 Finalize 请求回包这句写成已经已经有完整历史 / 已经是快照重放 / 已经交差 interchangeable，或已经和 382 syncingheight-vs-history bundled / syncingheight-nothistory-sold-as-bundled interchangeable。

## 为什么错

官方把 syncing_to_height / validator_updates 空 / Finalize events 三条核心句写成三件独立的实现事。把它们卖成已经有完整历史 / 已经是快照重放 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 syncing_to_height 正式三事（382 余量），必须分开 not already full history、not already snapshot replay、not already settled 三件事，不要和 382 / 323 / 783 / 784 糊成一句。

## 和相邻反模式

- [queryprove-notreqh-sold-as-bundled](queryprove-notreqh-sold-as-bundled.md) 是 Query 回包 height 就已经是请求高度（383/781），不是本页 syncing_to_height 边界。
- [inittime-notskip-sold-as-bundled](inittime-notskip-sold-as-bundled.md) 是 InitChain initial_height 就已经能跳步（387/769），不是本页同步目标高边界。
