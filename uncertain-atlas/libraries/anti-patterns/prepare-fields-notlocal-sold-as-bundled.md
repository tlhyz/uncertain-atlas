# 反模式：把 local_last_commit 是上一高度的预提交带扩展 not already this-height extension / not already H Prepare has extensions / not already settled 正式三事（359 余量） 卖成 已经是本高度刚签的扩展 / 已经到了 H 就已经 Prepare 带了扩展 / 已经交差

**层次**：实现 / Prepare 请求字段。  
**分类**：建议（产品）。  
**对应例**：[worked-example-prepare-fields-notlocal-vs-bundled.md](../../tracks/implementation/worked-example-prepare-fields-notlocal-vs-bundled.md)。

官方把 Prepare 和 Process / Finalize 同一套字段 / local_last_commit 是上一高度的预提交带扩展 / height / time / proposer_address 对上拟议头三条核心句写成三件独立的实现事。把它们卖成已经是本高度刚签的扩展 / 已经到了 H 就已经 Prepare 带了扩展 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 local_last_commit 是上一高度的预提交带扩展 正式三事（359 余量），必须分开 not already this-height extension、not already H Prepare has extensions、not already settled 三件事，不要和 359 / 330 / 422 / 365 / 845 / 847 糊成一句。

## 和相邻反模式

- [prepare-fields-notrun-sold-as-bundled](prepare-fields-notrun-sold-as-bundled.md) 是同一套字段单句边界（845 item 1），不是本页 local_last_commit 边界。
- 到了 H 就已经 Prepare 带了扩展是不变量 330，不是本页上一高预提交边界。
