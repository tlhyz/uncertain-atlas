# 反模式：把 last_block 落盘 not already settled / not already crash-three-step Commit / not already pruning 正式三事（370 余量） 卖成 已经交差 / 已经是崩溃三步已经 Commit / 已经在剪

**层次**：实现 / Info 握手。  
**分类**：建议（产品）。  
**对应例**：[worked-example-info-notpersist-vs-bundled.md](../../tracks/implementation/worked-example-info-notpersist-vs-bundled.md)。

官方把 Info 用来握手对齐 / app_version 进每块头 / last_block 要在 Commit 里落盘三条核心句写成三件独立的实现事。把它们卖成已经交差 / 已经是崩溃三步已经 Commit / 已经在剪，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 last_block 落盘 正式三事（370 余量），必须分开 not already settled、not already crash-three-step Commit、not already pruning 三件事，不要和 370 / 320 / 481 / 701 / 497 / 665 / 491 / 692 / 815 / 816 糊成一句。

## 和相邻反模式

- [info-notapphash-sold-as-bundled](info-notapphash-sold-as-bundled.md) 是 app_version 进头单句边界（816 item 2），不是本页 last_block 落盘边界。
- [infousage-notcommitpersist-sold-as-bundled](infousage-notcommitpersist-sold-as-bundled.md) 是 Info Usage last_block 就已经是 370 bundled（497/665），不是本页 last_block 落盘边界。
