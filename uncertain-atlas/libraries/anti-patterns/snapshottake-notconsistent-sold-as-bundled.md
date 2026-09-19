# 反模式：把没停链不是已经一致 not already consistent / not already async-safe / not already deterministic-bytes 正式三事（324 余量）说成已经一致 / 已经 Asynchronous 交差 / 已经各节点字节相同

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[没停链 not already consistent ≠ bundled（324）](../../tracks/implementation/worked-example-snapshottake-notconsistent-vs-bundled.md)。

## 卖法

把没停链 / 可以继续出块 / 链还在跑 写成已经隔离在单一高度 interchangeable / 已经 consistent interchangeable / 已经不受并发写影响交差 interchangeable / 324 snapshottake bundled interchangeable / 33 four gates interchangeable / snapshottake-sold-as-committed interchangeable；把在后台拍 / 拍可以很慢 / 异步在拍 写成已经 Asynchronous 交差 interchangeable / 已经 async-safe interchangeable；把同一高度 / 同一 Format / 标了同一份 写成已经各节点字节相同 interchangeable / 已经 deterministic-bytes interchangeable，或已经和 324 snapshottake bundled / snapshottake-sold-as-committed interchangeable / 729 snapshottake-notconsistent interchangeable。

## 为什么错

官方把没停链单句、already consistent、already async-safe、already deterministic-bytes 写成三件独立的实现事。把它们卖成 already consistent interchangeable / already async-safe interchangeable / already deterministic-bytes interchangeable，会把 not already consistent、not already async-safe、not already deterministic-bytes 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看没停链不是已经一致 not already consistent / not already async-safe / not already deterministic-bytes 正式三事（324 余量），必须分开 not already consistent、not already async-safe、not already deterministic-bytes 三件事，不要和 324 / 33 / 728 / 730 / 310 / 322 / 323 糊成一句。

## 和相邻反模式

- [snapshottake-sold-as-committed](snapshottake-sold-as-committed.md) 是 Taking Snapshots bundled 全段，不是本页三件保证 item 2 单句边界。
- [snapshottake-notcommitted-sold-as-bundled](snapshottake-notcommitted-sold-as-bundled.md) 是拍高度 item 1，不是本页 Consistent / Asynchronous / Deterministic 边界。
- [snapshotdiscover-sold-as-listed](snapshotdiscover-sold-as-listed.md) 是 ListSnapshots 已经齐（322），不是本页 Deterministic 字节边界。
