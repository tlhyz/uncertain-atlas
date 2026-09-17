# 例：看见 syncing_to_height 同步或重放时是目标高、否则等于本高 is not already full history interchangeable / not already snapshot replay interchangeable / not already settled interchangeable

**层次**：实现 / syncing_to_height not already full history / not already snapshot replay / not already settled 正式三事（382 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「syncing_to_height not already full history / not already snapshot replay / not already settled 正式三事（382 余量）/ not 782 syncingheight-nothistory interchangeable / not 382 syncingheight-vs-history bundled interchangeable」，不是 Finalize 请求回包 bundled（382），也不是切进共识就已经有从创世的完整历史（323）。不要另写怎样写 Finalize 请求回包。

## 官方三件事

1. **看见 `syncing_to_height` 同步或重放时是目标高、否则等于本高 / 看见填了目标 / Finalize 这份同步目标 is not already 已经有从创世的完整历史 interchangeable / 323 snapid interchangeable，也不是已经 Finalize 请求回包 bundled（382） interchangeable / 782 syncingheight-nothistory interchangeable / 783 syncingheight-notnoset interchangeable / 382 syncingheight item 2 validator_updates interchangeable，也不是已经 syncing_to_height not already full history / not already snapshot replay / not already settled 正式三事 bundled（382 item 1 余量） interchangeable / 382 syncingheight item 1 interchangeable。**  
   官方写：节点在同步或重放块时，`syncing_to_height` 等于目标高度。否则 `syncing_to_height` 等于本高。看见填了目标，不是已经有从创世的完整历史 interchangeable——本页从 382 item 1 侧钉 not already full history 单句。382 syncingheight vs history bundled unbundling 在本页 item 1 启动。

2. **看见填了目标 / 看见在同步 / Finalize 这份同步目标 is not already 已经是快照重放 interchangeable / 323 snapid interchangeable，也不是已经 Finalize 请求回包 bundled（382） interchangeable / 782 syncingheight-nothistory interchangeable / 382 syncingheight item 3 events interchangeable / 784 syncingheight-notdet interchangeable。**  
   官方把同步目标高和已经是快照重放分开——382 bundled 第一件事常与 323 混成「看见填了目标就已经有完整历史或已经是快照重放 interchangeable」，本页钉 not already snapshot replay 单句。

3. **看见填了目标 / 看见等于本高 / Finalize 这份同步目标 is not already 已经交差 interchangeable，也不是已经 Finalize 请求回包 bundled（382） interchangeable / 782 syncingheight-nothistory interchangeable / 783 syncingheight-notnoset interchangeable。**  
   官方把等于本高和已经交差分开。看见等于本高，不是已经交差 interchangeable。382 syncingheight vs history bundled unbundling 在本页 item 1 启动。

怎样写 Finalize 请求、怎样空着更新、怎样编事件是规范里的做法，本页不抄。

## 官方为什么这样拆

- **syncing_to_height not already full history ≠ 323 interchangeable：** 官方把同步目标高和已经有完整历史分开。
- **syncing_to_height not already snapshot replay ≠ 323 interchangeable：** 官方把在同步和已经是快照重放分开。
- **syncing_to_height not already settled ≠ 已经交差 interchangeable：** 官方把等于本高和已经交差分开；382 syncingheight vs history bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| syncing_to_height 同步或重放时是目标高、否则等于本高 | 不是已经有完整历史（323） | 不是 validator_updates 空（783/382 item 2） |
| 看见填了目标 | 不是已经是快照重放 | 不是 Finalize 请求回包 bundled（382） |
| 看见等于本高 | 不是已经交差 | 不是切进共识就已经有从创世的完整历史（323） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 syncing_to_height not already full history / not already snapshot replay / not already settled 正式三事（382 余量），必须分开 syncing_to_height 是不是已经有完整历史 interchangeable / 323、是不是已经是快照重放、是不是已经交差。可以跳过「看见填了目标就已经有完整历史」。不要另写怎样写 Finalize 请求回包。382 syncingheight vs history bundled unbundling 在本页 item 1 启动；续 [`worked-example-syncingheight-notnoset-vs-bundled.md`](worked-example-syncingheight-notnoset-vs-bundled.md)（不变量 783 item 2）。

## 本页不抄

- 怎样写 Finalize 请求、怎样空着更新、怎样编事件。
- Finalize 请求回包 bundled。那是不变量 382。
- validator_updates 空。那是不变量 382 item 2 余量 / 783。
- Finalize 回包 events。那是不变量 382 item 3 余量 / 784。
- 切进共识就已经有从创世的完整历史。那是不变量 323。
