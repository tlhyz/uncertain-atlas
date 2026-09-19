# 例：看见拍了这个高度不是已经交差之后拍的；看见没停链不是已经一致；看见只留最近两份不是已经有了全部历史快照

**层次**：实现 / Taking Snapshots。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Taking Snapshots。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「拍了这个高度不是已经交差之后拍的 / 没停链不是已经一致 / 只留最近两份不是已经有了全部历史快照」，不是只有 AppHash 可信任，也不是 Offer 收下已经装完。不要另写怎样拍快照或怎样切块。324 snapshottake vs commit bundled unbundling 续（728 + 729）；精读 [`worked-example-snapshottake-notcommitted-vs-bundled.md`](worked-example-snapshottake-notcommitted-vs-bundled.md)（不变量 728 item 1）；[`worked-example-snapshottake-notconsistent-vs-bundled.md`](worked-example-snapshottake-notconsistent-vs-bundled.md)（不变量 729 item 2）。

## 官方三件事

规范把应用自己拍快照写成三件独立的实现事，不是「看见拍了就已经交差之后拍、已经一致、已经有了全部历史快照」一件事：

1. **看见标了这个高度 / 看见拍了快照 不是已经在交差之后拍的，也不是已经没有更高高度的数据。**  
   官方写：快照有 `Height`。必须在**该高度已经 Commit 之后**拍，而且**不得含任何更高高度的数据**。看见标了高度，不是已经交差之后拍。看见拍了，不是已经没有后面高度。看见字段在，不是已经隔离在这一高度。
2. **看见在后台拍 / 看见没停链 不是已经隔离在单一高度，也不是已经各节点字节相同。**  
   官方写：应用必须同时给三件保证。**Consistent：** 必须拍在单一隔离高度，不受并发写影响。**Asynchronous：** 拍可以很慢，但不得停链。**Deterministic：** 同一高度、同一 `Format`，各节点必须字节相同，含全部元数据。看见没停链，不是已经隔离。看见在后台拍，不是已经各节点相同。看见同一高度，不是已经同一格式。
3. **看见只留最近两份 / 看见 Hash 对上了 不是已经有了全部历史快照，也不是已经是同一份。**  
   官方写：旧快照过一段时间应删掉；一般只留**最近两份**，免得最后一份正在被别人装回时被删。一份快照要被当成同一份，**Height / Format / Chunks / Hash / Metadata 五个字段都要相同**。`Hash` 只是任意哈希，用来在拉 chunk 时比对是不是同一份。看见只留两份，不是已经有了全部历史。看见 Hash 对上，不是五个字段都对上。看见 Hash，不是已经是轻验 AppHash。

怎样用 RocksDB / MVCC 拍、怎样切成 10 MB、把最近两份当产品常数是规范里的取值或做法，本页不抄。只有 AppHash 可信任是不变量 38，本页不抄。

## 官方为什么这样拆

- **拍了这个高度 ≠ 已经交差之后拍的：** 官方把标高度和必须先 Commit、不得含更高高度分开。
- **没停链 ≠ 已经一致：** 官方把后台拍、隔离高度、各节点字节相同写成三件保证，不是一件。
- **只留最近两份 ≠ 已经有了全部历史快照：** 官方把生产者只留两份和发现端每节点 10 份分开；Hash 对上不是五个字段都相同。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 拍了这个高度 | 不是已经交差之后拍的 | 不是只有 AppHash 可信任（38） |
| 没停链 / 三件保证 | 不是已经一致 | 不是 Offer 收下已经装完（321），也不是切进共识已经有完整历史（323） |
| 只留最近两份 / Hash 对上 | 不是已经有了全部历史快照 | 不是 ListSnapshots 已经齐（322） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「已经在拍快照」，必须分开拍了这个高度是不是已经交差之后拍的、没停链是不是已经一致、只留最近两份是不是已经有了全部历史快照。可以跳过「看见拍了就已经交差之后拍」。不要另写怎样拍快照或怎样切块。不要把最近两份当不确定默认。 324 snapshottake vs commit bundled unbundling 续（728 + 729 item 2）。

## 本页不抄

- 怎样用 RocksDB / MVCC 拍、怎样切块、把最近两份或 10 MB 当产品常数。
- 只有 AppHash 可信任。那是不变量 38。
- Offer 收下已经装完。那是不变量 321。
- ListSnapshots 已经齐。那是不变量 322。
- 切进共识已经有完整历史。那是不变量 323。
