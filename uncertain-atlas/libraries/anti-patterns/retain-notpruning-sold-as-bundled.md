# 反模式：把 retain_height 默认 0 not already pruning / not already settled / not already no history 正式三事（366 余量） 卖成 已经在剪 / 已经交差 / 已经没有历史

**层次**：实现 / Commit 保留高度。  
**分类**：建议（产品）。  
**对应例**：[worked-example-retain-notpruning-vs-bundled.md](../../tracks/implementation/worked-example-retain-notpruning-vs-bundled.md)。

官方把 retain_height 默认 0 / 低于这个高度可删 / 全网都删会永久丢三条核心句写成三件独立的实现事。把它们卖成已经在剪 / 已经交差 / 已经没有历史，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 retain_height 默认 0 正式三事（366 余量），必须分开 not already pruning、not already settled、not already no history 三件事，不要和 366 / 320 / 491 / 692 / 370 / 817 / 828 / 829 糊成一句。

## 和相邻反模式

- [commitretaincaution-notdefault-sold-as-bundled](commitretaincaution-notdefault-sold-as-bundled.md) 是 Commit Usage retain_height caution 默认就已经在剪（491/692），不是本页默认 0 边界。
- 崩溃三步就已经 Commit 是不变量 320，不是本页默认 0 边界。
