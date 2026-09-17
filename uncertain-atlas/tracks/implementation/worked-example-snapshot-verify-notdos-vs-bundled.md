# 例：看见封禁邻居 is not already no snapshot DoS interchangeable / not already accepted-this-peer interchangeable / not already settled interchangeable

**层次**：实现 / 封禁邻居 not already no snapshot DoS / not already accepted-this-peer / not already settled 正式三事（332 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Verification。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「封禁邻居 not already no snapshot DoS / not already accepted-this-peer / not already settled 正式三事（332 余量）/ not 937 snapshot-verify-notdos interchangeable / not 332 snapshot-verify-vs-early bundled interchangeable」，不是快照验完 bundled（332），也不是发了 addr 过滤查询已经收下这个人（326），也不是应用选择不实现就已经没有 state sync（334/934）。不要另写怎样做增量默克尔证明或怎样配受信邻居。

## 官方三件事

1. **看见让引擎封禁邻居 / 看见配了受信邻居名单 这份挡法 is not already 已经没有快照 DoS interchangeable，也不是已经快照验完 bundled（332） interchangeable / 937 snapshot-verify-notdos interchangeable / 935 snapshot-verify-notearly interchangeable / 332 snapshot-verify item 1 装完又对上 interchangeable，也不是已经封禁邻居 not already no snapshot DoS / not already accepted-this-peer / not already settled 正式三事 bundled（332 item 3 余量） interchangeable / 332 snapshot-verify item 3 interchangeable。**  
   官方写：对手可以给无效或有害快照，拦节点进网。应用可以让 CometBFT 封禁邻居。最后一招，运维可以把 P2P 配成只信一份能给有效快照的邻居。看见封禁了，不是已经没有这种 DoS interchangeable——本页从 332 item 3 侧钉 not already no snapshot DoS 单句。332 snapshot-verify vs early bundled unbundling 在本页 item 3 完成。

2. **看见配了受信名单 / 看见能挡一家 / 这份挡法 is not already 已经收下这个人 interchangeable，也不是已经快照验完 bundled（332） interchangeable / 937 snapshot-verify-notdos interchangeable / 332 snapshot-verify item 2 增量验 interchangeable / 936 snapshot-verify-notanchor interchangeable，也不是已经发了 addr 过滤查询已经收下这个人 interchangeable / 326 peerfilter interchangeable。**  
   官方把配了受信名单和已经是过滤已经收下分开——332 bundled 第三件事常与 326 混成「看见封禁就已经没有快照 DoS 或已经收下 interchangeable」，本页钉 not already accepted-this-peer 单句。

3. **看见能挡一家 / 看见封禁了 / 这份挡法 is not already 已经交差 interchangeable，也不是已经快照验完 bundled（332） interchangeable / 937 snapshot-verify-notdos interchangeable / 935 snapshot-verify-notearly interchangeable，也不是已经应用选择不实现就已经没有 state sync interchangeable / 334/934 snapshot-conn-notgone interchangeable。**  
   官方把能挡一家和已经能挡所有有害快照 / 已经交差分开。看见能挡一家，不是已经交差 interchangeable。332 snapshot-verify vs early bundled unbundling 在本页 item 3 完成。

怎样做增量默克尔证明、怎样配 checksum、怎样写受信邻居名单是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **封禁邻居 not already no snapshot DoS ≠ 已经没有快照 DoS interchangeable：** 官方把封禁 / 受信名单和已经没有有害快照分开。
- **看见配了受信名单 not already accepted-this-peer ≠ 已经收下这个人 interchangeable：** 官方把配了受信名单和已经是过滤已经收下分开。
- **看见能挡一家 not already settled ≠ 已经交差 interchangeable：** 官方把能挡一家和已经能挡所有有害快照分开；332 snapshot-verify vs early bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 封禁邻居 / 受信名单 | 不是已经没有快照 DoS | 不是发了 addr 过滤查询已经收下这个人（326） |
| 看见配了受信名单 | 不是已经收下这个人 | 不是应用选择不实现就已经没有 state sync（334/934） |
| 看见能挡一家 | 不是已经交差 | 不是装完又对上就已经早验过（935） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看封禁邻居 not already no snapshot DoS / not already accepted-this-peer / not already settled 正式三事（332 余量），必须分开是不是已经没有快照 DoS、是不是已经收下这个人、是不是已经交差。可以跳过「看见封禁就已经没有有害快照」。不要另写怎样做增量默克尔证明或怎样配受信邻居。332 snapshot-verify vs early bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样做增量默克尔证明、怎样配 checksum、怎样写受信邻居名单。
- 快照验完 bundled。那是不变量 332。
- 装完又对上就已经早验过。那是不变量 332 item 1 余量 / 935。
- 发了 addr 过滤查询已经收下这个人。那是不变量 326。
- 应用选择不实现就已经没有 state sync。那是不变量 334/934。
