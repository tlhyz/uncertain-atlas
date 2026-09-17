# 例：看见切进共识 is not already full-history interchangeable / not already any-old interchangeable / not already settled interchangeable

**层次**：实现 / 切进共识 not already full-history / not already any-old / not already settled 正式三事（323 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Transition to Consensus。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「切进共识 not already full-history / not already any-old / not already settled 正式三事（323 余量）/ not 955 snapshot-switch-nothist interchangeable / not 323 snapshot-switch-vs-history bundled interchangeable」，不是切进 bundled（323），也不是 ListSnapshots 已经齐（322），也不是 Offer 收下已经装完（321）。不要另写怎样切到共识或怎样配扩展。

## 官方三件事

1. **看见切进共识 / 看见能出块 这份切换 is not already 已经有从创世的完整历史 interchangeable，也不是已经切进 bundled（323） interchangeable / 955 snapshot-switch-nothist interchangeable / 953 snapshot-switch-notchain interchangeable / 954 snapshot-switch-notver interchangeable / 323 snapshot-switch item 1 装完 interchangeable，也不是已经切进共识 not already full-history / not already any-old / not already settled 正式三事 bundled（323 item 3 余量） interchangeable / 323 snapshot-switch item 3 interchangeable。**  
   官方写：切过去之后，这个节点和其他节点一样跑，只是块历史在恢复快照的那个高度被截断。看见能出块，不是已经有从创世的完整历史 interchangeable——本页从 323 item 3 侧钉 not already full-history 单句。323 snapshot-switch vs history bundled unbundling 在本页 item 3 完成。

2. **看见能出块 / 看见切进共识 / 这份切换 is not already 已经能给任意旧高度 interchangeable，也不是已经切进 bundled（323） interchangeable / 955 snapshot-switch-nothist interchangeable / 323 snapshot-switch item 2 AppHash 对上 interchangeable / 954 snapshot-switch-notver interchangeable，也不是已经 ListSnapshots 已经齐 interchangeable / 322 snapshot-discover interchangeable。**  
   官方把能出块和历史被截断分开。看见能出块，不是已经能给任意旧高度 interchangeable。本页钉 not already any-old 单句。

3. **看见和其他节点一样跑 / 看见透明 / 这份切换 is not already 已经交差 interchangeable，也不是已经切进 bundled（323） interchangeable / 955 snapshot-switch-nothist interchangeable / 953 snapshot-switch-notchain interchangeable，也不是已经 Offer 收下已经装完 interchangeable / 321 snapshot-restore interchangeable。**  
   官方把透明和已经不用管扩展高度分开。看见和其他节点一样跑，不是已经交差 interchangeable。323 snapshot-switch vs history bundled unbundling 在本页 item 3 完成。

怎样切到共识、怎样配 RFC-100、怎样写扩展高度是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **切进共识 not already full-history ≠ 已经有从创世的完整历史 interchangeable：** 官方把能出块和历史被截断分开。
- **看见能出块 not already any-old ≠ 已经能给任意旧高度 interchangeable：** 官方把能出块和已经能给任意旧高度分开。
- **看见和其他节点一样跑 not already settled ≠ 已经交差 interchangeable：** 官方把透明和已经不用管扩展高度分开；323 snapshot-switch vs history bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 切进共识 | 不是已经有完整历史 | 不是 ListSnapshots 已经齐（322） |
| 看见能出块 | 不是已经能给任意旧高度 | 不是 Offer 收下已经装完（321） |
| 看见和其他节点一样跑 | 不是已经交差 | 不是装完就已经有了 ChainID（953） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看切进共识 not already full-history / not already any-old / not already settled 正式三事（323 余量），必须分开是不是已经有完整历史、是不是已经能给任意旧高度、是不是已经交差。可以跳过「看见装完就已经是全节点」。不要另写怎样切到共识或怎样配扩展。323 snapshot-switch vs history bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样切到共识、怎样配 RFC-100、怎样写扩展高度。
- 切进 bundled。那是不变量 323。
- ListSnapshots 已经齐。那是不变量 322。
- Offer 收下已经装完。那是不变量 321。
