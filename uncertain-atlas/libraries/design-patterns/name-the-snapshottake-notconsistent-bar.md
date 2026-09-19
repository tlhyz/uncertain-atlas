# 模式：把没停链不是已经一致 not already consistent / not already async-safe / not already deterministic-bytes 正式三事（324 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Taking Snapshots。  
**例**：[没停链 not already consistent ≠ bundled（324）](../../tracks/implementation/worked-example-snapshottake-notconsistent-vs-bundled.md)。

## 三个名字

1. **没停链 不是 already consistent：** 看见没停链 / 可以继续出块 / 链还在跑，不是已经隔离在单一高度 interchangeable / 已经不受并发写影响交差 interchangeable，不是 324 snapshottake bundled interchangeable / 33 four gates interchangeable / snapshottake-sold-as-committed interchangeable。

2. **后台拍 不是 already async-safe：** 看见在后台拍 / 拍可以很慢 / 异步在拍，不是已经 Asynchronous 交差 interchangeable / 已经慢而不停链交差 interchangeable，不是 310 commitlock interchangeable / 324 snapshottake item 1 interchangeable。

3. **同一高度 不是 already deterministic-bytes：** 看见同一高度 / 同一 Format / 标了同一份，不是已经各节点字节相同 interchangeable / 已经含全部元数据交差 interchangeable，不是 322 snapshotdiscover interchangeable / 324 snapshottake item 3 interchangeable。

官方把没停链单句、already consistent、already async-safe、already deterministic-bytes 写成三个名字。把它们叫成一个「看见没停链就已经一致 interchangeable / 就已经 Asynchronous 交差 interchangeable / 就已经各节点字节相同 interchangeable」，会把 not already consistent、not already async-safe、not already deterministic-bytes 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看没停链不是已经一致 not already consistent / not already async-safe / not already deterministic-bytes 正式三事（324 余量），先数清问的是没停链 是不是 already consistent / 324 / snapshottake-sold-as-committed，是不是后台拍 是不是 already async-safe，还是同一高度 是不是 already deterministic-bytes，再决定要不要同一次发布。324 snapshottake vs commit bundled unbundling 在本页 item 2 续。
