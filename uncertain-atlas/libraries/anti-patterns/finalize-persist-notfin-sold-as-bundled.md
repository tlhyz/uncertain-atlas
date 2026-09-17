# 反模式：把 必须在 Commit 落盘 not already persisted in Finalize / not already unlocked / not already settled 正式三事（335 余量） 卖成 已经在 Finalize 落了 / 已经解锁 / 已经交差

**层次**：实现 / FinalizeBlock 落盘禁令。  
**分类**：建议（产品）。  
**对应例**：[worked-example-finalize-persist-notfin-vs-bundled.md](../../tracks/implementation/worked-example-finalize-persist-notfin-vs-bundled.md)。

官方把 Finalize 改了状态 / 必须在 Commit 落盘 / 记住上次成功 Commit 高度 三条核心句写成三件独立的实现事。把它们卖成已经在 Finalize 落了 / 已经解锁 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看必须在 Commit 落盘 正式三事（335 余量），必须分开 not already persisted in Finalize、not already unlocked、not already settled 三件事，不要和 335 / 310 / 632 / 902 / 904 糊成一句。

## 和相邻反模式

- [finalize-persist-notdisk-sold-as-bundled](finalize-persist-notdisk-sold-as-bundled.md) 是 Finalize 改了状态单句边界（902 item 1），不是本页 Commit 唯一落盘点边界。
- 默认锁已经 RPC 安全是不变量 310，不是本页必须在 Commit 落盘边界。
