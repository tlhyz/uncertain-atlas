# 例：看见装完又对上 LastBlockAppHash is not already incrementally verified interchangeable / not already in-network interchangeable / not already settled interchangeable

**层次**：实现 / 装完又对上 LastBlockAppHash not already incrementally verified / not already in-network / not already settled 正式三事（332 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Verification。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「装完又对上 LastBlockAppHash not already incrementally verified / not already in-network / not already settled 正式三事（332 余量）/ not 935 snapshot-verify-notearly interchangeable / not 332 snapshot-verify-vs-early bundled interchangeable」，不是快照验完 bundled（332），也不是 Offer 收下已经装完（321），也不是 AppHash 对上已经版本也对上（323）。不要另写怎样做增量默克尔证明或怎样配受信邻居。

## 官方三件事

1. **看见装完又叫了 Info / 看见 LastBlockAppHash 对上轻客户端那份 这份核对 is not already 已经在装回当中增量验过 interchangeable，也不是已经快照验完 bundled（332） interchangeable / 935 snapshot-verify-notearly interchangeable / 936 snapshot-verify-notanchor interchangeable / 332 snapshot-verify item 2 增量验 interchangeable，也不是已经装完又对上 LastBlockAppHash not already incrementally verified / not already in-network / not already settled 正式三事 bundled（332 item 1 余量） interchangeable / 332 snapshot-verify item 1 interchangeable。**  
   官方写：chunk 都收下之后，CometBFT 才叫 Info，取 LastBlockAppHash，跟轻客户端从链上取来、验过的那份 AppHash 对。还要看 LastBlockHeight 是不是这份快照的高度。这次核对是为了在进网之前确认应用有效。看见对上了，不是已经在装的时候验过 interchangeable——本页从 332 item 1 侧钉 not already incrementally verified 单句。332 snapshot-verify vs early bundled unbundling 在本页 item 1 启动。

2. **看见高度对上 / 看见 Info 绿了 / 这份核对 is not already 已经进了网 interchangeable，也不是已经快照验完 bundled（332） interchangeable / 935 snapshot-verify-notearly interchangeable / 332 snapshot-verify item 3 封禁 interchangeable / 937 snapshot-verify-notdos interchangeable，也不是已经 Offer 收下已经装完 interchangeable / 321 offersnap interchangeable。**  
   官方把高度对上和已经切进共识分开——332 bundled 第一件事常与 321 / 323 混成「看见装完又对上就已经在装回当中验过或已经交差 interchangeable」，本页钉 not already in-network 单句。

3. **看见 Info 绿了 / 看见对上了 / 这份核对 is not already 已经交差 interchangeable，也不是已经快照验完 bundled（332） interchangeable / 935 snapshot-verify-notearly interchangeable / 936 snapshot-verify-notanchor interchangeable，也不是已经 AppHash 对上已经版本也对上 interchangeable / 323 apphash-version interchangeable。**  
   官方把 Info 绿了和已经进了网 / 已经交差分开。看见 Info 绿了，不是已经交差 interchangeable。332 snapshot-verify vs early bundled unbundling 在本页 item 1 启动。

怎样做增量默克尔证明、怎样配 checksum、怎样写受信邻居名单是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **装完又对上 LastBlockAppHash not already incrementally verified ≠ 已经在装回当中验过 interchangeable：** 官方把进网前最后一次 Info 和装回当中的增量验分开。
- **看见高度对上 not already in-network ≠ 已经进了网 interchangeable：** 官方把高度对上和已经切进共识分开。
- **看见 Info 绿了 not already settled ≠ 已经交差 interchangeable：** 官方把 Info 绿了和已经交差分开；332 snapshot-verify vs early bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 装完又对上 LastBlockAppHash | 不是已经在装回当中验过 | 不是 Offer 收下已经装完（321） |
| 看见高度对上 | 不是已经进了网 | 不是 AppHash 对上已经版本也对上（323） |
| 看见 Info 绿了 | 不是已经交差 | 不是增量验就已经是唯一可信锚（936） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看装完又对上 LastBlockAppHash not already incrementally verified / not already in-network / not already settled 正式三事（332 余量），必须分开是不是已经在装回当中验过、是不是已经进了网、是不是已经交差。可以跳过「看见对上就已经早验过」。不要另写怎样做增量默克尔证明或怎样配受信邻居。332 snapshot-verify vs early bundled unbundling 在本页 item 1 启动；续 [`worked-example-snapshot-verify-notanchor-vs-bundled.md`](worked-example-snapshot-verify-notanchor-vs-bundled.md)（不变量 936 item 2）。

## 本页不抄

- 怎样做增量默克尔证明、怎样配 checksum、怎样写受信邻居名单。
- 快照验完 bundled。那是不变量 332。
- 增量验就已经是唯一可信锚。那是不变量 332 item 2 余量 / 936。
- Offer 收下已经装完。那是不变量 321。
