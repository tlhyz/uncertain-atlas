# 反模式：把 Finalize 改了状态 not already persisted / not already Commit / not already settled 正式三事（335 余量） 卖成 已经落盘 / 已经 Commit / 已经交差

**层次**：实现 / FinalizeBlock 落盘禁令。  
**分类**：建议（产品）。  
**对应例**：[worked-example-finalize-persist-notdisk-vs-bundled.md](../../tracks/implementation/worked-example-finalize-persist-notdisk-vs-bundled.md)。

官方把 Finalize 改了状态 / 必须在 Commit 落盘 / 记住上次成功 Commit 高度 三条核心句写成三件独立的实现事。把它们卖成已经落盘 / 已经 Commit / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 改了状态 正式三事（335 余量），必须分开 not already persisted、not already Commit、not already settled 三件事，不要和 335 / 478 / 320 / 5 / 903 / 904 糊成一句。

## 和相邻反模式

- [finpersist-notpersist-sold-as-bundled](finpersist-notpersist-sold-as-bundled.md) 是 persist decision ≠ executes block v（478/605），不是本页 Finalize MUST NOT 持久化边界。
- 崩溃恢复三步已经交差是不变量 320，不是本页 Finalize 改了状态边界。
