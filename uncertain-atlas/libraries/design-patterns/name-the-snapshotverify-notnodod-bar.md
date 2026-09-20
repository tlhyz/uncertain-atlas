# 模式：把封禁邻居不是已经没有快照 DoS not already no-snapshot-dos / not already trusted-list-is-accept / not already blocks-all-bad 正式三事（332 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Verification。  
**例**：[封禁邻居 not already no-snapshot-dos ≠ bundled（332）](../../tracks/implementation/worked-example-snapshotverify-notnodod-vs-bundled.md)。

## 三个名字

1. **封禁了 不是 already no-snapshot-dos：** 看见让引擎封禁邻居 / 封禁了 / 应用让 CometBFT 封禁，不是已经没有快照 DoS interchangeable / 已经没有有害快照交差 interchangeable，不是 332 snapshotverify bundled interchangeable / 33 four gates interchangeable / snapshotverify-sold-as-early interchangeable。

2. **配了受信名单 不是 already trusted-list-is-accept：** 看见配了受信邻居名单 / P2P 只信一份 / 受信名单，不是已经是过滤已经收下 interchangeable / 已经收下交差 interchangeable，不是 326 peerfilter interchangeable / 332 snapshotverify item 1 interchangeable。

3. **能挡一家 不是 already blocks-all-bad：** 看见能挡一家 / 封禁了一家 / 挡住这份有害快照，不是已经能挡所有有害快照 interchangeable / 已经挡全交差 interchangeable，不是 326 peerfilter interchangeable / 332 snapshotverify item 2 interchangeable。

官方把封禁邻居单句、already no-snapshot-dos、already trusted-list-is-accept、already blocks-all-bad 写成三个名字。把它们叫成一个「看见封禁邻居就已经没有快照 DoS interchangeable / 就已经是过滤已经收下 interchangeable / 就已经能挡所有有害快照 interchangeable」，会把 not already no-snapshot-dos、not already trusted-list-is-accept、not already blocks-all-bad 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看封禁邻居不是已经没有快照 DoS not already no-snapshot-dos / not already trusted-list-is-accept / not already blocks-all-bad 正式三事（332 余量），先数清问的是封禁了 是不是 already no-snapshot-dos / 332 / snapshotverify-sold-as-early，是不是配了受信名单 是不是 already trusted-list-is-accept，还是能挡一家 是不是 already blocks-all-bad，再决定要不要同一次发布。332 snapshotverify vs early bundled unbundling 在本页 item 3 完成。
