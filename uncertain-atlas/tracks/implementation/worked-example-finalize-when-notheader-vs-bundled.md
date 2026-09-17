# 例：看见回了 AppHash 和输出哈希进 ResultHash is not already printed in header interchangeable / not already this-height AppHash interchangeable / not already settled interchangeable

**层次**：实现 / 回了 AppHash 和输出哈希进 ResultHash not already printed in header / not already this-height AppHash / not already settled 正式三事（362 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「回了 AppHash 和输出哈希进 ResultHash not already printed in header / not already this-height AppHash / not already settled 正式三事（362 余量）/ not 841 finalize-when-notheader interchangeable / not 362 finalize-when-vs-decided bundled interchangeable」，不是 Finalize 何时调用 bundled（362），也不是本头 AppHash 就已经是本高度交差（147），也不是必须回四列就已经印进本头（363/838），也不是 Query 高度就已经含根（371）。不要另写怎样写 Finalize 何时调用。

## 官方三件事

1. **看见应用回了 AppHash 和各笔输出、引擎把输出哈希进 ResultHash / 看见回了 这份回了 is not already 已经印进本头 interchangeable，也不是已经 Finalize 何时调用 bundled（362） interchangeable / 841 finalize-when-notheader interchangeable / 839 finalize-when-notcall interchangeable / 362 finalize-when item 1 +2/3 interchangeable，也不是已经回了 AppHash 和输出哈希进 ResultHash not already printed in header / not already this-height AppHash / not already settled 正式三事 bundled（362 item 3 余量） interchangeable / 362 finalize-when item 3 interchangeable。**  
   官方写：应用算出并回 AppHash，以及各笔执行输出；CometBFT 把这些输出哈希进 ResultHash。看见回了，不是已经印进本头 interchangeable——本页从 362 item 3 侧钉 not already printed in header 单句。362 finalize-when vs decided bundled unbundling 在本页 item 3 完成。

2. **看见回了 / 看见有 ResultHash / 这份回了 is not already 已经是本头 AppHash interchangeable / 147 header AppHash interchangeable，也不是已经 Finalize 何时调用 bundled（362） interchangeable / 841 finalize-when-notheader interchangeable / 362 finalize-when item 2 先落决定 interchangeable / 840 finalize-when-notpersist interchangeable，也不是已经必须回四列就已经印进本头 interchangeable / 363 finalize-equiv / 838 finalize-equiv-notchanged interchangeable。**  
   官方把有 ResultHash 和已经是本头 AppHash 分开——362 bundled 第三件事常与 147 / 363 混成「看见回了就已经印进本头或已经是本头 AppHash interchangeable」，本页钉 not already this-height AppHash 单句。

3. **看见回了 / 看见哈希了 / 这份回了 is not already 已经交差 interchangeable，也不是已经 Finalize 何时调用 bundled（362） interchangeable / 841 finalize-when-notheader interchangeable / 839 finalize-when-notcall interchangeable，也不是已经 Query 高度就已经含根 interchangeable / 371 queryheight interchangeable。**  
   官方把哈希了和已经交差分开。看见哈希了，不是已经交差 interchangeable。362 finalize-when vs decided bundled unbundling 在本页 item 3 完成。

怎样写 Finalize 何时调用、怎样落决定、怎样算 ResultHash 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **回了 AppHash 和输出哈希进 ResultHash not already printed in header ≠ 已经印进本头 interchangeable：** 官方把回了和印进本头分开。
- **看见有 ResultHash not already this-height AppHash ≠ 147 interchangeable：** 官方把有 ResultHash 和已经是本头 AppHash 分开。
- **看见哈希了 not already settled ≠ 已经交差 interchangeable：** 官方把哈希了和已经交差分开；362 finalize-when vs decided bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 回了 AppHash 和输出哈希进 ResultHash | 不是已经印进本头 | 不是本头 AppHash 就已经是本高度交差（147） |
| 看见有 ResultHash | 不是已经是本头 AppHash | 不是必须回四列就已经印进本头（363/838） |
| 看见哈希了 | 不是已经交差 | 不是 Query 高度就已经含根（371） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看回了 AppHash 和输出哈希进 ResultHash not already printed in header / not already this-height AppHash / not already settled 正式三事（362 余量），必须分开是不是已经印进本头、是不是已经是本头 AppHash interchangeable / 147、是不是已经交差。可以跳过「看见回了就已经印进本头」。不要另写怎样写 Finalize 何时调用。362 finalize-when vs decided bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 Finalize 何时调用、怎样落决定、怎样算 ResultHash。
- Finalize 何时调用 bundled。那是不变量 362。
- +2/3 precommit 才决定再调 Finalize。那是不变量 362 item 1 余量 / 839。
- 本头 AppHash 就已经是本高度交差。那是不变量 147。
- 必须回四列就已经印进本头。那是不变量 363 / 838。
- Query 高度就已经含根。那是不变量 371。
