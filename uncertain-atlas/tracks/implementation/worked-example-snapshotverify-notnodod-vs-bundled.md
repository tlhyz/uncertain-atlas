# 例：看见封禁了邻居 / 看见配了受信名单 / 看见能挡一家 is not already already no-snapshot-dos interchangeable / already trusted-list-is-accept interchangeable / already blocks-all-bad interchangeable

**层次**：实现 / 封禁邻居不是已经没有快照 DoS not already no-snapshot-dos / not already trusted-list-is-accept / not already blocks-all-bad 正式三事（332 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Verification。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「封禁邻居不是已经没有快照 DoS not already no-snapshot-dos / not already trusted-list-is-accept / not already blocks-all-bad 正式三事（332 余量）/ not 754 snapshotverify-notnodod interchangeable / not 332 snapshotverify bundled interchangeable」，不是 Snapshot Verification bundled（332），也不是装完又对上不是已经在装回当中验过（752 item 1 余量）或增量验了 chunk 不是已经是唯一可信的 AppHash（753 item 2 余量）。不要另写怎样写受信邻居名单或怎样封禁。

## 官方三件事

规范把 Requirements 里对手可给无效或有害快照、应用可让引擎封禁邻居、运维可配受信名单 和「已经是封禁了就已经没有快照 DoS interchangeable / 已经是配了受信名单就已经是过滤已经收下 interchangeable / 已经是能挡一家就已经能挡所有有害快照 interchangeable / 已经是 snapshotverify bundled interchangeable」分开写成三件独立的实现事，不是「看见封禁邻居就已经没有快照 DoS interchangeable / 就已经是过滤已经收下 interchangeable / 就已经能挡所有有害快照 interchangeable」一件事：

1. **看见让引擎封禁邻居 / 看见封禁了 / 看见应用让 CometBFT 封禁 is not already 已经没有快照 DoS interchangeable / 已经 no-snapshot-dos interchangeable / 已经没有有害快照交差 interchangeable / 332 snapshotverify bundled interchangeable / 33 four gates interchangeable / snapshotverify-sold-as-early interchangeable，也不是已经 Snapshot Verification bundled（332） interchangeable / 754 snapshotverify-notnodod interchangeable / 332 snapshotverify item 3 interchangeable，也不是已经封禁邻居不是已经没有快照 DoS not already no-snapshot-dos / not already trusted-list-is-accept / not already blocks-all-bad 正式三事 bundled（332 item 3 余量） interchangeable / 332 snapshotverify item 3 interchangeable，也不是已经装完又对上不是已经在装回当中验过（752） interchangeable / 753 snapshotverify-notuniqueapphash interchangeable / 326 peerfilter interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：对手可以给无效或有害快照，拦节点进网。应用可以让 CometBFT 封禁邻居。看见封禁了，不是已经 no-snapshot-dos interchangeable——332 钉 bundled 三事，本页从 item 3 侧钉 not already no-snapshot-dos 单句。看见让引擎封禁邻居，不是已经 Snapshot Verification bundled（332） interchangeable——332 钉 bundled，本页钉 item 3 第一件事。看见应用让 CometBFT 封禁，不是已经发了 addr 过滤查询已经收下这个人（326） interchangeable——326 另钉。332 snapshotverify vs early bundled unbundling 在本页 item 3 完成。

2. **看见配了受信邻居名单 / 看见 P2P 只信一份 / 看见受信名单 is not already 已经是过滤已经收下 interchangeable / 已经 trusted-list-is-accept interchangeable / 已经收下交差 interchangeable / 332 snapshotverify bundled interchangeable / 326 peerfilter interchangeable，也不是已经 Snapshot Verification bundled（332） interchangeable / 754 snapshotverify-notnodod interchangeable / 332 snapshotverify item 1 装完又对上 interchangeable / 332 snapshotverify item 2 唯一可信 interchangeable，也不是已经封禁邻居不是已经没有快照 DoS not already no-snapshot-dos / not already trusted-list-is-accept / not already blocks-all-bad 正式三事 bundled（332 item 3 余量） interchangeable / 332 snapshotverify item 3 interchangeable，也不是已经没有快照 DoS（本页第一件事） interchangeable。**  
   官方写：最后一招，运维可以把 P2P 配成只信一份能给有效快照的邻居。看见配了受信名单，不是已经是过滤已经收下。看见 P2P 只信一份，不是已经 trusted-list-is-accept interchangeable——本页钉 not already trusted-list-is-accept 单句。看见受信名单，不是已经发了 addr 过滤查询已经收下这个人（326） interchangeable——326 另钉。看见配了受信名单，不是已经没有快照 DoS（本页第一件事） interchangeable——三件事分开钉。332 snapshotverify vs early bundled unbundling 在本页 item 3 完成。

3. **看见能挡一家 / 看见封禁了一家 / 看见挡住这份有害快照 is not already 已经能挡所有有害快照 interchangeable / 已经 blocks-all-bad interchangeable / 已经挡全交差 interchangeable / 332 snapshotverify bundled interchangeable / 326 peerfilter interchangeable，也不是已经 Snapshot Verification bundled（332） interchangeable / 754 snapshotverify-notnodod interchangeable / 332 snapshotverify item 1 / 332 snapshotverify item 2，也不是已经封禁邻居不是已经没有快照 DoS not already no-snapshot-dos / not already trusted-list-is-accept / not already blocks-all-bad 正式三事 bundled（332 item 3 余量） interchangeable / 332 snapshotverify item 3 interchangeable，也不是已经没有快照 DoS（本页第一件事） interchangeable / 已经是过滤已经收下（本页第二件事） interchangeable。**  
   官方写：看见能挡一家，不是已经能挡所有有害快照。看见封禁了一家，不是已经 blocks-all-bad interchangeable——本页钉 not already blocks-all-bad 单句。看见挡住这份有害快照，不是已经没有快照 DoS（本页第一件事） interchangeable——三件事分开钉。332 snapshotverify vs early bundled unbundling 在本页 item 3 完成。

怎样写受信邻居名单、怎样封禁、怎样配 P2P 是规范里的取值或做法，本页不抄。Snapshot Verification bundled（332）、装完又对上不是已经在装回当中验过（332 item 1 余量 / 752）、增量验了 chunk 不是已经是唯一可信的 AppHash（332 item 2 余量 / 753）、发了 addr 过滤查询已经收下这个人（326）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **封禁了 not already no-snapshot-dos ≠ 332 / 33 interchangeable：** 官方把封禁对策和已经没有有害快照分开。
- **配了受信名单 not already trusted-list-is-accept ≠ 已经是过滤已经收下 interchangeable：** 官方把受信名单和已经收下这个人分开。
- **能挡一家 not already blocks-all-bad ≠ 已经能挡所有有害快照 interchangeable：** 官方把挡住一家和已经挡全分开；332 snapshotverify vs early bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 封禁了 | 不是 already no-snapshot-dos | 不是 addr 过滤已经收下 alone（326） |
| 配了受信名单 | 不是 already trusted-list-is-accept | 不是装完又对上 alone（752） |
| 能挡一家 | 不是 already blocks-all-bad | 不是唯一可信 AppHash alone（753） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看封禁邻居不是已经没有快照 DoS not already no-snapshot-dos / not already trusted-list-is-accept / not already blocks-all-bad 正式三事（332 余量），必须分开封禁了 是不是 already no-snapshot-dos interchangeable / 332 snapshotverify bundled interchangeable / snapshotverify-sold-as-early interchangeable、配了受信名单 是不是 already trusted-list-is-accept interchangeable、能挡一家 是不是 already blocks-all-bad interchangeable。可以跳过「看见封禁邻居就已经没有快照 DoS interchangeable / 就已经是过滤已经收下 interchangeable / 就已经能挡所有有害快照 interchangeable」。不要另写怎样写受信邻居名单。332 snapshotverify vs early bundled unbundling 在本页 item 3 完成（752 + 753 + 754）。

## 本页不抄

- 怎样写受信邻居名单、怎样封禁、怎样配 P2P。
- Snapshot Verification bundled。那是不变量 332。
- 装完又对上不是已经在装回当中验过。那是不变量 332 item 1 余量 / 752。
- 增量验了 chunk 不是已经是唯一可信的 AppHash。那是不变量 332 item 2 余量 / 753。
- 发了 addr 过滤查询已经收下这个人。那是不变量 326。
- 四门已经结算。那是不变量 33。
