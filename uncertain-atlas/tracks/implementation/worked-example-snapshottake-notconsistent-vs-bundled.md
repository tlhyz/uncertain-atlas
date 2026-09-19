# 例：看见没停链 / 看见在后台拍 / 看见同一高度 is not already already consistent interchangeable / already async-safe interchangeable / already deterministic-bytes interchangeable

**层次**：实现 / 没停链不是已经一致 not already consistent / not already async-safe / not already deterministic-bytes 正式三事（324 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Taking Snapshots。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「没停链不是已经一致 not already consistent / not already async-safe / not already deterministic-bytes 正式三事（324 余量）/ not 729 snapshottake-notconsistent interchangeable / not 324 snapshottake bundled interchangeable」，不是 Taking Snapshots bundled（324），也不是拍了这个高度不是已经交差之后拍的（728 item 1 余量）或只留最近两份不是已经有了全部历史快照（730 item 3 余量）。不要另写怎样拍快照或怎样切块。

## 官方三件事

规范把 Requirements 里应用必须同时给 **Consistent / Asynchronous / Deterministic** 三件保证 和「已经是没停链就已经 Consistent interchangeable / 已经是后台拍就已经 Asynchronous 交差 interchangeable / 已经是同一高度就已经各节点字节相同 interchangeable / 已经是 Taking Snapshots bundled interchangeable」分开写成三件独立的实现事，不是「看见没停链 / 看见在后台拍就已经一致 interchangeable / 就已经 Asynchronous 交差 interchangeable / 就已经各节点字节相同 interchangeable」一件事：

1. **看见没停链 / 看见可以继续出块 / 看见链还在跑 is not already 已经隔离在单一高度 interchangeable / 已经 consistent interchangeable / 已经不受并发写影响交差 interchangeable / 324 snapshottake bundled interchangeable / 33 four gates interchangeable / snapshottake-sold-as-committed interchangeable，也不是已经 Taking Snapshots bundled（324） interchangeable / 729 snapshottake-notconsistent interchangeable / 324 snapshottake item 2 interchangeable，也不是已经没停链不是已经一致 not already consistent / not already async-safe / not already deterministic-bytes 正式三事 bundled（324 item 2 余量） interchangeable / 324 snapshottake item 2 interchangeable，也不是已经拍了这个高度不是已经交差之后拍的（728） interchangeable / 730 snapshottake-notretained interchangeable / 323 snapshotswitch interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：**Consistent** 必须拍在单一隔离高度，不受并发写影响。看见没停链，不是已经 Consistent / 已经隔离 interchangeable——324 钉 bundled 三事，本页从 item 2 侧钉 not already consistent 单句。看见可以继续出块，不是已经 Taking Snapshots bundled（324） interchangeable——324 钉 bundled，本页钉 item 2 第一件事。看见链还在跑，不是已经拍了这个高度不是已经交差之后拍的（728） interchangeable——728 另钉 item 1，本页钉三件保证。324 snapshottake vs commit bundled unbundling 在本页 item 2 续。

2. **看见在后台拍 / 看见拍可以很慢 / 看见异步在拍 is not already 已经 Asynchronous 交差 interchangeable / 已经 async-safe interchangeable / 已经慢而不停链交差 interchangeable / 324 snapshottake bundled interchangeable / 310 commitlock interchangeable，也不是已经 Taking Snapshots bundled（324） interchangeable / 729 snapshottake-notconsistent interchangeable / 324 snapshottake item 1 拍高度 interchangeable / 324 snapshottake item 3 只留两份 interchangeable，也不是已经没停链不是已经一致 not already consistent / not already async-safe / not already deterministic-bytes 正式三事 bundled（324 item 2 余量） interchangeable / 324 snapshottake item 2 interchangeable，也不是已经 Consistent（本页第一件事） interchangeable。**  
   官方写：**Asynchronous** 拍可以很慢，但不得停链。看见在后台拍，不是已经 async-safe interchangeable——后台拍不等于 Asynchronous 三件保证已经交差。看见拍可以很慢，不是已经 Consistent（本页第一件事） interchangeable——三件事分开钉。看见异步在拍，不是已经 Commit 锁已经 RPC 安全（310） interchangeable——310 另钉锁，本页钉拍快照 Asynchronous。324 snapshottake vs commit bundled unbundling 在本页 item 2 续。

3. **看见同一高度 / 看见同一 Format / 看见标了同一份 is not already 已经各节点字节相同 interchangeable / 已经 deterministic-bytes interchangeable / 已经含全部元数据交差 interchangeable / 324 snapshottake bundled interchangeable / 322 snapshotdiscover interchangeable，也不是已经 Taking Snapshots bundled（324） interchangeable / 729 snapshottake-notconsistent interchangeable / 324 snapshottake item 1 / 324 snapshottake item 3，也不是已经没停链不是已经一致 not already consistent / not already async-safe / not already deterministic-bytes 正式三事 bundled（324 item 2 余量） interchangeable / 324 snapshottake item 2 interchangeable，也不是已经 Consistent（本页第一件事） interchangeable / 已经 async-safe（本页第二件事） interchangeable。**  
   官方写：**Deterministic** 同一高度、同一 `Format`，各节点必须字节相同，含全部元数据。看见同一高度，不是已经 deterministic-bytes interchangeable——本页钉 not already deterministic-bytes 单句。看见同一 Format，不是已经 Consistent（本页第一件事） interchangeable——三件事分开钉。看见标了同一份，不是已经 ListSnapshots 已经齐（322） interchangeable——322 另钉发现端。324 snapshottake vs commit bundled unbundling 在本页 item 2 完成。

怎样用 RocksDB / MVCC 拍、怎样切成 10 MB、把最近两份当产品常数是规范里的取值或做法，本页不抄。Taking Snapshots bundled（324）、拍了这个高度不是已经交差之后拍的（324 item 1 余量 / 728）、只留最近两份不是已经有了全部历史快照（324 item 3 余量 / 730）、只有 AppHash 可信任（38）、Offer 收下已经装完（321）、切进共识已经有完整历史（323）是另外那套，本页不抄。

## 官方为什么这样拆

- **没停链 not already consistent ≠ 324 / 33 interchangeable：** 官方把没停链和 Consistent 隔离高度分开。
- **后台拍 not already async-safe ≠ 已经 Asynchronous 交差 interchangeable：** 官方把后台拍和 Asynchronous 慢而不停链交差分开。
- **同一高度 not already deterministic-bytes ≠ 已经各节点字节相同 interchangeable：** 官方把同一高度 / Format 和各节点字节相同分开；324 snapshottake vs commit bundled unbundling 在本页 item 2 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 没停链 | 不是 already consistent | 不是拍高度 post-commit alone（728） |
| 后台拍 | 不是 already async-safe | 不是 Commit 锁 alone（310） |
| 同一高度 | 不是 already deterministic-bytes | 不是 ListSnapshots alone（322） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看没停链不是已经一致 not already consistent / not already async-safe / not already deterministic-bytes 正式三事（324 余量），必须分开没停链 是不是 already consistent interchangeable / 324 snapshottake bundled interchangeable / snapshottake-sold-as-committed interchangeable、后台拍 是不是 already async-safe interchangeable、同一高度 是不是 already deterministic-bytes interchangeable。可以跳过「看见没停链就已经一致 interchangeable / 就已经 Asynchronous 交差 interchangeable / 就已经各节点字节相同 interchangeable」。不要另写怎样拍快照。324 snapshottake vs commit bundled unbundling 在本页 item 2 续（728 + 729）；续 [`worked-example-snapshottake-notretained-vs-bundled.md`](worked-example-snapshottake-notretained-vs-bundled.md)（不变量 730 item 3）。

## 本页不抄

- 怎样用 RocksDB / MVCC 拍、怎样切块、把最近两份或 10 MB 当产品常数。
- Taking Snapshots bundled。那是不变量 324。
- 拍了这个高度不是已经交差之后拍的。那是不变量 324 item 1 余量 / 728。
- 只留最近两份不是已经有了全部历史快照。那是不变量 324 item 3 余量 / 730。
- 只有 AppHash 可信任。那是不变量 38。
- Offer 收下已经装完。那是不变量 321。
- 切进共识已经有完整历史。那是不变量 323。
