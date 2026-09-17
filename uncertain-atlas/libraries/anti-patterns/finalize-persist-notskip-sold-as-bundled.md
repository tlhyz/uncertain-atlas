# 反模式：把 记住上次成功 Commit 高度 not already app ahead / not already can skip / not already settled 正式三事（335 余量） 卖成 已经能单独比引擎高 / 已经能跳步 / 已经交差

**层次**：实现 / FinalizeBlock 落盘禁令。  
**分类**：建议（产品）。  
**对应例**：[worked-example-finalize-persist-notskip-vs-bundled.md](../../tracks/implementation/worked-example-finalize-persist-notskip-vs-bundled.md)。

官方把 Finalize 改了状态 / 必须在 Commit 落盘 / 记住上次成功 Commit 高度 三条核心句写成三件独立的实现事。把它们卖成已经能单独比引擎高 / 已经能跳步 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看记住上次成功 Commit 高度 正式三事（335 余量），必须分开 not already app ahead、not already can skip、not already settled 三件事，不要和 335 / 320 / 5 / 902 / 903 糊成一句。

## 和相邻反模式

- [finalize-persist-notfin-sold-as-bundled](finalize-persist-notfin-sold-as-bundled.md) 是 Commit 唯一落盘点单句边界（903 item 2），不是本页记住高度边界。
- 崩溃恢复三步已经交差是不变量 320，不是本页记住高度不许跳步边界。
