# 例：看见用于 PBTS is not already eternal constant interchangeable / not already BFT Time median interchangeable / not already settled interchangeable

**层次**：实现 / 用于 PBTS not already eternal constant / not already BFT Time median / not already settled 正式三事（336 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / SynchronyParams.Precision / SynchronyParams.MessageDelay。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「用于 PBTS not already eternal constant / not already BFT Time median / not already settled 正式三事（336 余量）/ not 925 precision-notconst interchangeable / not 336 precision-vs-msgdelay bundled interchangeable」，不是同步参数 bundled（336），也不是块时间必须点名算法 / 不得把 PRECISION / MSGDELAY 写成永恒共识（40），也不是 PBTS 启用高度已经切了（343）。不要另写怎样设 PRECISION / MSGDELAY 或怎样选启用高度。

## 官方三件事

1. **看见用于 PBTS / 看见能出合法提案 这份尺 is not already 已经是永恒常数 interchangeable，也不是已经同步参数 bundled（336） interchangeable / 925 precision-notconst interchangeable / 923 precision-notmsg interchangeable / 336 precision item 1 Precision interchangeable，也不是已经用于 PBTS not already eternal constant / not already BFT Time median / not already settled 正式三事 bundled（336 item 3 余量） interchangeable / 336 precision item 3 interchangeable。**  
   官方把它们写成 PBTS 用的两把尺，不是未标注版本的永恒共识常数，也不是上一高度 LastCommit 的加权中位。看见用于 PBTS，不是已经抄成产品常数 interchangeable——本页从 336 item 3 侧钉 not already eternal constant 单句。336 precision vs msgdelay bundled unbundling 在本页 item 3 完成。

2. **看见能出合法提案 / 看见用于 PBTS / 这份尺 is not already 已经是 BFT Time 中位数 interchangeable，也不是已经同步参数 bundled（336） interchangeable / 925 precision-notconst interchangeable / 336 precision item 2 填了两个 interchangeable / 924 precision-noton interchangeable，也不是已经块时间必须点名算法 interchangeable / 40 block-time interchangeable。**  
   官方把能出合法提案和已经是 MTP / 已经是调整钟分开——336 bundled 第三件事常与 40 混成「看见用于 PBTS 就已经是永恒常数或已经是 BFT Time interchangeable」，本页钉 not already BFT Time median 单句。

3. **看见能出合法提案 / 看见用于 PBTS / 这份尺 is not already 已经交差 interchangeable，也不是已经同步参数 bundled（336） interchangeable / 925 precision-notconst interchangeable / 923 precision-notmsg interchangeable，也不是已经 PBTS 启用高度已经切了 interchangeable / 343 pbts-height interchangeable。**  
   官方把能出合法提案和已经交差分开。看见能出合法提案，不是已经交差 interchangeable。336 precision vs msgdelay bundled unbundling 在本页 item 3 完成。

怎样设 PRECISION / MSGDELAY、默认毫秒、怎样选 PbtsEnableHeight 是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **用于 PBTS not already eternal constant ≠ 已经是永恒常数 interchangeable：** 官方把这两把尺和永恒常数、BFT Time 中位数分开。
- **看见能出合法提案 not already BFT Time median ≠ 已经是 BFT Time 中位数 interchangeable：** 官方把能出合法提案和已经是 MTP / 已经是调整钟分开。
- **看见用于 PBTS not already settled ≠ 已经交差 interchangeable：** 官方把用于 PBTS 和已经交差分开；336 precision vs msgdelay bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 用于 PBTS | 不是已经是永恒常数 | 不是块时间必须点名算法 / 不得把 PRECISION / MSGDELAY 写成永恒共识（40） |
| 看见能出合法提案 | 不是已经是 BFT Time 中位数 | 不是 PBTS 启用高度已经切了（343） |
| 看见用于 PBTS | 不是已经交差 | 不是 Precision 就已经是 MessageDelay（923） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看用于 PBTS not already eternal constant / not already BFT Time median / not already settled 正式三事（336 余量），必须分开是不是已经是永恒常数、是不是已经是 BFT Time 中位数、是不是已经交差。可以跳过「看见用于 PBTS 就已经是产品常数」。不要另写怎样设 PRECISION / MSGDELAY 或怎样选启用高度。336 precision vs msgdelay bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样设 PRECISION / MSGDELAY、默认毫秒、怎样选 PbtsEnableHeight。
- 同步参数 bundled。那是不变量 336。
- Precision 就已经是 MessageDelay。那是不变量 336 item 1 余量 / 923。
- 块时间必须点名算法。那是不变量 40。
- PBTS 启用高度已经切了。那是不变量 343。
