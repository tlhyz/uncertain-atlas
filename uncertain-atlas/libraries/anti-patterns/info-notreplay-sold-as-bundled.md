# 反模式：把 Info 握手 not already snapshot replay / not already QueryState / not already settled 正式三事（370 余量） 卖成 已经是快照重放 / 已经是 QueryState / 已经交差

**层次**：实现 / Info 握手。  
**分类**：建议（产品）。  
**对应例**：[worked-example-info-notreplay-vs-bundled.md](../../tracks/implementation/worked-example-info-notreplay-vs-bundled.md)。

官方把 Info 用来握手对齐 / app_version 进每块头 / last_block 要在 Commit 里落盘三条核心句写成三件独立的实现事。把它们卖成已经是快照重放 / 已经是 QueryState / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info 握手 正式三事（370 余量），必须分开 not already snapshot replay、not already QueryState、not already settled 三件事，不要和 370 / 314 / 494 / 669 / 389 / 761 / 379 / 793 / 816 / 817 糊成一句。

## 和相邻反模式

- [infousage-nothandshake-sold-as-bundled](infousage-nothandshake-sold-as-bundled.md) 是 Info Usage 握手就已经是 370 bundled（494/669），不是本页握手对齐边界。
- [infodata-nothandshake-sold-as-bundled](infodata-nothandshake-sold-as-bundled.md) 是 Info 回包 data 就已经是握手（389/761），不是本页握手对齐边界。
