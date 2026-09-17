# 反模式：把 height / time / proposer_address 对上拟议头 not already header hash / not already ExecuteTxState / not already settled 正式三事（359 余量） 卖成 已经知道本头哈希 / 已经是 ExecuteTxState / 已经交差

**层次**：实现 / Prepare 请求字段。  
**分类**：建议（产品）。  
**对应例**：[worked-example-prepare-fields-nothash-vs-bundled.md](../../tracks/implementation/worked-example-prepare-fields-nothash-vs-bundled.md)。

官方把 Prepare 和 Process / Finalize 同一套字段 / local_last_commit 是上一高度的预提交带扩展 / height / time / proposer_address 对上拟议头三条核心句写成三件独立的实现事。把它们卖成已经知道本头哈希 / 已经是 ExecuteTxState / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 height / time / proposer_address 对上拟议头 正式三事（359 余量），必须分开 not already header hash、not already ExecuteTxState、not already settled 三件事，不要和 359 / 311 / 147 / 462 / 845 / 846 糊成一句。

## 和相邻反模式

- [prepare-fields-notlocal-sold-as-bundled](prepare-fields-notlocal-sold-as-bundled.md) 是 local_last_commit 单句边界（846 item 2），不是本页对上拟议头边界。
- 候选已经是 ExecuteTxState 是不变量 311，不是本页对上拟议头边界。
