# 例：看见装完又叫了 Info / 看见 Info 绿了 / 看见高度对上 is not already already incremental-verified interchangeable / already in-network interchangeable / already consensus-entered interchangeable

**层次**：实现 / 装完又对上不是已经在装回当中验过 not already incremental-verified / not already in-network / not already consensus-entered 正式三事（332 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Verification。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「装完又对上不是已经在装回当中验过 not already incremental-verified / not already in-network / not already consensus-entered 正式三事（332 余量）/ not 752 snapshotverify-notduringrestore interchangeable / not 332 snapshotverify bundled interchangeable」，不是 Snapshot Verification bundled（332），也不是增量验了 chunk 不是已经是唯一可信的 AppHash（753 item 2 余量）或封禁邻居不是已经没有快照 DoS（754 item 3 余量）。不要另写怎样做增量默克尔证明或怎样配受信邻居。

## 官方三件事

规范把 Requirements 里 chunk 都收下之后才叫 Info、对 LastBlockAppHash 和快照高度、是为了进网之前确认应用有效 和「已经是装完又对上就已经在装回当中增量验过 interchangeable / 已经是 Info 绿了就已经进了网 interchangeable / 已经是高度对上就已经切进共识 interchangeable / 已经是 snapshotverify bundled interchangeable」分开写成三件独立的实现事，不是「看见装完又对上就已经在装回当中验过 interchangeable / 就已经进了网 interchangeable / 就已经切进共识 interchangeable」一件事：

1. **看见装完又叫了 Info / 看见 LastBlockAppHash 对上轻客户端那份 / 看见装完又对上 is not already 已经在装回当中增量验过 interchangeable / 已经 incremental-verified interchangeable / 已经装回当中验过交差 interchangeable / 332 snapshotverify bundled interchangeable / 33 four gates interchangeable / snapshotverify-sold-as-early interchangeable，也不是已经 Snapshot Verification bundled（332） interchangeable / 752 snapshotverify-notduringrestore interchangeable / 332 snapshotverify item 1 interchangeable，也不是已经装完又对上不是已经在装回当中验过 not already incremental-verified / not already in-network / not already consensus-entered 正式三事 bundled（332 item 1 余量） interchangeable / 332 snapshotverify item 1 interchangeable，也不是已经增量验了 chunk 不是已经是唯一可信的 AppHash（753） interchangeable / 754 snapshotverify-notnodod interchangeable / 321 snapshotrestore interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：chunk **都收下之后**，CometBFT 才叫 `Info`，取 `LastBlockAppHash`，跟轻客户端从链上取来、验过的那份 AppHash 对。看见装完又对上，不是已经 incremental-verified interchangeable——332 钉 bundled 三事，本页从 item 1 侧钉 not already incremental-verified 单句。看见装完又叫了 Info，不是已经 Snapshot Verification bundled（332） interchangeable——332 钉 bundled，本页钉 item 1 第一件事。看见 LastBlockAppHash 对上轻客户端那份，不是已经 Offer 收下已经装完（321） interchangeable——321 另钉。332 snapshotverify vs early bundled unbundling 在本页 item 1 启动。

2. **看见 Info 绿了 / 看见进网前核对绿了 / 看见应用有效确认 is not already 已经进了网 interchangeable / 已经 in-network interchangeable / 已经进网交差 interchangeable / 332 snapshotverify bundled interchangeable / 323 snapshotswitch interchangeable，也不是已经 Snapshot Verification bundled（332） interchangeable / 752 snapshotverify-notduringrestore interchangeable / 332 snapshotverify item 2 唯一可信 interchangeable / 332 snapshotverify item 3 封禁 interchangeable，也不是已经装完又对上不是已经在装回当中验过 not already incremental-verified / not already in-network / not already consensus-entered 正式三事 bundled（332 item 1 余量） interchangeable / 332 snapshotverify item 1 interchangeable，也不是已经在装回当中增量验过（本页第一件事） interchangeable。**  
   官方写：这次核对是为了在**进网之前**确认应用有效。看见 Info 绿了，不是已经进了网。看见进网前核对绿了，不是已经 in-network interchangeable——本页钉 not already in-network 单句。看见应用有效确认，不是已经切进共识已经有完整历史（323） interchangeable——323 另钉。看见进网前核对绿了，不是已经在装回当中增量验过（本页第一件事） interchangeable——三件事分开钉。332 snapshotverify vs early bundled unbundling 在本页 item 1 启动。

3. **看见高度对上 / 看见 LastBlockHeight 对上 / 看见快照高度对上 is not already 已经切进共识 interchangeable / 已经 consensus-entered interchangeable / 已经切进共识交差 interchangeable / 332 snapshotverify bundled interchangeable / 323 snapshotswitch interchangeable，也不是已经 Snapshot Verification bundled（332） interchangeable / 752 snapshotverify-notduringrestore interchangeable / 332 snapshotverify item 2 / 332 snapshotverify item 3，也不是已经装完又对上不是已经在装回当中验过 not already incremental-verified / not already in-network / not already consensus-entered 正式三事 bundled（332 item 1 余量） interchangeable / 332 snapshotverify item 1 interchangeable，也不是已经在装回当中增量验过（本页第一件事） interchangeable / 已经进了网（本页第二件事） interchangeable。**  
   官方写：还要看 `LastBlockHeight` 是不是这份快照的高度。看见高度对上，不是已经 consensus-entered interchangeable——本页钉 not already consensus-entered 单句。看见 LastBlockHeight 对上，不是已经 AppHash 对上已经版本也对上（323） interchangeable——323 另钉。看见快照高度对上，不是已经进了网（本页第二件事） interchangeable——三件事分开钉。332 snapshotverify vs early bundled unbundling 在本页 item 1 启动。

怎样做增量默克尔证明、怎样配 checksum、怎样写受信邻居名单是规范里的取值或做法，本页不抄。Snapshot Verification bundled（332）、增量验了 chunk 不是已经是唯一可信的 AppHash（332 item 2 余量 / 753）、封禁邻居不是已经没有快照 DoS（332 item 3 余量 / 754）、Offer 收下已经装完（321）、切进共识已经有完整历史（323）、只有 AppHash 可信任（38）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **装完又对上 not already incremental-verified ≠ 332 / 33 interchangeable：** 官方把进网前最后一次 Info 和装回当中的增量验分开。
- **Info 绿了 not already in-network ≠ 已经进了网 interchangeable：** 官方把进网前确认和应用有效和已经进了网分开。
- **高度对上 not already consensus-entered ≠ 已经切进共识 interchangeable：** 官方把快照高度对上和已经切进共识分开；332 snapshotverify vs early bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 装完又对上 | 不是 already incremental-verified | 不是 Offer 收下 alone（321） |
| Info 绿了 | 不是 already in-network | 不是切进共识有完整历史 alone（323） |
| 高度对上 | 不是 already consensus-entered | 不是版本也对上 alone（323） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看装完又对上不是已经在装回当中验过 not already incremental-verified / not already in-network / not already consensus-entered 正式三事（332 余量），必须分开装完又对上 是不是 already incremental-verified interchangeable / 332 snapshotverify bundled interchangeable / snapshotverify-sold-as-early interchangeable、Info 绿了 是不是 already in-network interchangeable、高度对上 是不是 already consensus-entered interchangeable。可以跳过「看见装完又对上就已经在装回当中验过 interchangeable / 就已经进了网 interchangeable / 就已经切进共识 interchangeable」。不要另写怎样做增量默克尔证明。332 snapshotverify vs early bundled unbundling 在本页 item 1 启动；续 [`worked-example-snapshotverify-notuniqueapphash-vs-bundled.md`](worked-example-snapshotverify-notuniqueapphash-vs-bundled.md)（不变量 753 item 2）。

## 本页不抄

- 怎样做增量默克尔证明、怎样配 checksum、怎样写受信邻居名单。
- Snapshot Verification bundled。那是不变量 332。
- 增量验了 chunk 不是已经是唯一可信的 AppHash。那是不变量 332 item 2 余量 / 753。
- 封禁邻居不是已经没有快照 DoS。那是不变量 332 item 3 余量 / 754。
- Offer 收下已经装完。那是不变量 321。
- 切进共识已经有完整历史、AppHash 对上已经版本也对上。那是不变量 323。
- 只有 AppHash 可信任。那是不变量 38。
- 四门已经结算。那是不变量 33。
