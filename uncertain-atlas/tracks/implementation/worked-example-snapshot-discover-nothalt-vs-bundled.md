# 例：看见 Offer 被拒 is not already empty interchangeable / not already halted interchangeable / not already settled interchangeable

**层次**：实现 / Offer 被拒 not already empty / not already halted / not already settled 正式三事（322 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Discovery。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「Offer 被拒 not already empty / not already halted / not already settled 正式三事（322 余量）/ not 958 snapshot-discover-nothalt interchangeable / not 322 snapshot-discover-vs-offer bundled interchangeable」，不是发现 bundled（322），也不是启动对齐已经是快照重放（314），也不是 Offer 收下已经装完（321）。不要另写怎样列快照或怎样挑。

## 官方三件事

1. **看见 Offer 被拒 / 看见拒了格式或邻居 这份回法 is not already 已经没有快照 interchangeable，也不是已经发现 bundled（322） interchangeable / 958 snapshot-discover-nothalt interchangeable / 956 snapshot-discover-notfull interchangeable / 957 snapshot-discover-nottake interchangeable / 322 snapshot-discover item 1 ListSnapshots 回了 interchangeable，也不是已经 Offer 被拒 not already empty / not already halted / not already settled 正式三事 bundled（322 item 3 余量） interchangeable / 322 snapshot-discover item 3 interchangeable。**  
   官方写：应用可以收下、拒掉、拒这种格式、拒这个邻居，以及别的回法。CometBFT 会继续发现并继续 Offer，直到有一份被收下，或应用中止。看见被拒，不是已经没有快照 interchangeable——本页从 322 item 3 侧钉 not already empty 单句。322 snapshot-discover vs offer bundled unbundling 在本页 item 3 完成。

2. **看见拒了邻居 / 看见被拒 / 这份回法 is not already 已经停 interchangeable，也不是已经发现 bundled（322） interchangeable / 958 snapshot-discover-nothalt interchangeable / 322 snapshot-discover item 2 挑了最高 interchangeable / 957 snapshot-discover-nottake interchangeable，也不是已经启动对齐已经是快照重放 interchangeable / 314 querystate interchangeable。**  
   官方把继续发现和应用中止分开。看见拒了邻居，不是已经停 interchangeable。本页钉 not already halted 单句。

3. **看见能中止 / 看见被拒 / 这份回法 is not already 已经交差 interchangeable，也不是已经发现 bundled（322） interchangeable / 958 snapshot-discover-nothalt interchangeable / 956 snapshot-discover-notfull interchangeable，也不是已经 Offer 收下已经装完 interchangeable / 321 snapshot-restore interchangeable。**  
   官方把能中止和已经发现完分开。看见能中止，不是已经交差 interchangeable。322 snapshot-discover vs offer bundled unbundling 在本页 item 3 完成。

怎样实现 ListSnapshots、怎样挑、把 10 当产品常数是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **Offer 被拒 not already empty ≠ 已经没有快照 interchangeable：** 官方把被拒和继续发现分开。
- **看见拒了邻居 not already halted ≠ 已经停 interchangeable：** 官方把拒了邻居和应用中止分开。
- **看见能中止 not already settled ≠ 已经交差 interchangeable：** 官方把能中止和已经发现完分开；322 snapshot-discover vs offer bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Offer 被拒 | 不是已经停 | 不是启动对齐已经是快照重放（314） |
| 看见拒了邻居 | 不是已经停 | 不是 Offer 收下已经装完（321） |
| 看见能中止 | 不是已经交差 | 不是 ListSnapshots 回了就已经齐（956） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Offer 被拒 not already empty / not already halted / not already settled 正式三事（322 余量），必须分开是不是已经没有快照、是不是已经停、是不是已经交差。可以跳过「看见问了就已经齐」。不要另写怎样列快照或怎样挑。不要把每节点 10 份当不确定默认。322 snapshot-discover vs offer bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样实现 ListSnapshots、怎样挑、把 10 当产品常数。
- 发现 bundled。那是不变量 322。
- 启动对齐已经是快照重放。那是不变量 314。
- Offer 收下已经装完。那是不变量 321。
