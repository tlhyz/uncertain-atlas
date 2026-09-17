# 例：看见 ListSnapshots 回了 is not already all-snapshots interchangeable / not already unbounded interchangeable / not already settled interchangeable

**层次**：实现 / ListSnapshots 回了 not already all-snapshots / not already unbounded / not already settled 正式三事（322 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Discovery。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「ListSnapshots 回了 not already all-snapshots / not already unbounded / not already settled 正式三事（322 余量）/ not 956 snapshot-discover-notfull interchangeable / not 322 snapshot-discover-vs-offer bundled interchangeable」，不是发现 bundled（322），也不是 Offer 收下已经装完（321），也不是切进共识已经有完整历史（323/955）。不要另写怎样列快照或怎样挑。

## 官方三件事

1. **看见问了邻居 / 看见 ListSnapshots 回了 这份列表 is not already 已经有了全部快照 interchangeable，也不是已经发现 bundled（322） interchangeable / 956 snapshot-discover-notfull interchangeable / 957 snapshot-discover-nottake interchangeable / 322 snapshot-discover item 2 挑了最高 interchangeable，也不是已经 ListSnapshots 回了 not already all-snapshots / not already unbounded / not already settled 正式三事 bundled（322 item 1 余量） interchangeable / 322 snapshot-discover item 1 interchangeable。**  
   官方写：空节点进网之后，会问所有邻居用 ListSnapshots 报快照，每个节点限 10 份。看见问了，不是已经齐 interchangeable——本页从 322 item 1 侧钉 not already all-snapshots 单句。322 snapshot-discover vs offer bundled unbundling 在本页 item 1 启动。

2. **看见回了 / 看见问了 / 这份列表 is not already 已经没有上限 interchangeable，也不是已经发现 bundled（322） interchangeable / 956 snapshot-discover-notfull interchangeable / 322 snapshot-discover item 3 Offer 被拒 interchangeable / 958 snapshot-discover-nothalt interchangeable，也不是已经 Offer 收下已经装完 interchangeable / 321 snapshot-restore interchangeable。**  
   官方把回了和每个节点限 10 份分开——322 bundled 第一件事常与 321 混成「看见问了就已经齐或已经装完 interchangeable」，本页钉 not already unbounded 单句。

3. **看见 10 / 看见回了 / 这份列表 is not already 已经交差 interchangeable，也不是已经发现 bundled（322） interchangeable / 956 snapshot-discover-notfull interchangeable / 957 snapshot-discover-nottake interchangeable，也不是已经切进共识已经有完整历史 interchangeable / 323/955 snapshot-switch-nothist interchangeable。**  
   官方把 10 和已经是不确定默认分开。看见 10，不是已经交差 interchangeable。322 snapshot-discover vs offer bundled unbundling 在本页 item 1 启动。

怎样实现 ListSnapshots、怎样挑、把 10 当产品常数是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **ListSnapshots 回了 not already all-snapshots ≠ 已经有了全部快照 interchangeable：** 官方把每节点 10 份上限和已经齐分开。
- **看见回了 not already unbounded ≠ 已经没有上限 interchangeable：** 官方把回了和每个节点限 10 份分开。
- **看见 10 not already settled ≠ 已经交差 interchangeable：** 官方把 10 和已经是不确定默认分开；322 snapshot-discover vs offer bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ListSnapshots 回了 | 不是已经有了全部快照 | 不是 Offer 收下已经装完（321） |
| 看见回了 | 不是已经没有上限 | 不是切进共识已经有完整历史（323/955） |
| 看见 10 | 不是已经交差 | 不是挑了最高就已经收下（957） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ListSnapshots 回了 not already all-snapshots / not already unbounded / not already settled 正式三事（322 余量），必须分开是不是已经齐、是不是已经没有上限、是不是已经交差。可以跳过「看见问了就已经齐」。不要另写怎样列快照或怎样挑。不要把每节点 10 份当不确定默认。322 snapshot-discover vs offer bundled unbundling 在本页 item 1 启动；续 [`worked-example-snapshot-discover-nottake-vs-bundled.md`](worked-example-snapshot-discover-nottake-vs-bundled.md)（不变量 957 item 2）。

## 本页不抄

- 怎样实现 ListSnapshots、怎样挑、把 10 当产品常数。
- 发现 bundled。那是不变量 322。
- Offer 收下已经装完。那是不变量 321。
- 切进共识已经有完整历史。那是不变量 323/955。
