# 反模式：把 应用选择不实现 not already no-state-sync-object / not already genesis-only / not already settled 正式三事（334 余量） 卖成 已经没有 state sync 这条对象 / 已经从创世是唯一合法路径 / 已经交差

**层次**：实现 / Snapshot Connection。  
**分类**：建议（产品）。  
**对应例**：[worked-example-snapshot-conn-notgone-vs-bundled.md](../../tracks/implementation/worked-example-snapshot-conn-notgone-vs-bundled.md)。

官方把四门里有 Snapshot Connection / 给人快照或给自己装回 / 应用选择不实现 三条核心句写成三件独立的实现事。把它们卖成已经没有 state sync 这条对象 / 已经从创世是唯一合法路径 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看应用选择不实现 正式三事（334 余量），必须分开 not already no-state-sync-object、not already genesis-only、not already settled 三件事，不要和 334 / 38 / 329 / 932 / 933 糊成一句。

## 和相邻反模式

- [snapshot-conn-notboth-sold-as-bundled](snapshot-conn-notboth-sold-as-bundled.md) 是「和 / 或」仍可只做一头单句边界（933 item 2），不是本页可选仍留着 state sync 对象边界。
- Query 回了已经是正常运转必须有是不变量 329，不是本页可选仍不是删掉对象边界。
