# 例：看见 Finalize 回包 events 标成非确定 is not already must be deterministic interchangeable / not already settled interchangeable / not already same order as results interchangeable

**层次**：实现 / Finalize 回包 events not already must be deterministic / not already settled / not already same order as results 正式三事（382 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Finalize 回包 events not already must be deterministic / not already settled / not already same order as results 正式三事（382 余量）/ not 784 syncingheight-notdet interchangeable / not 382 syncingheight-vs-history bundled interchangeable」，不是 Finalize 请求回包 bundled（382），也不是 Finalize 算出的状态就必须只依赖上一份状态和决定块（342）。不要另写怎样写 Finalize 请求回包。

## 官方三件事

1. **看见 Finalize 回包 `events` 标成非确定 / 看见回了事件 / Finalize 这份非确定事件 is not already 已经必须像状态那样只依赖上一份状态和决定块 interchangeable / 342 findet interchangeable，也不是已经 Finalize 请求回包 bundled（382） interchangeable / 784 syncingheight-notdet interchangeable / 782 syncingheight-nothistory interchangeable / 382 syncingheight item 1 syncing_to_height interchangeable，也不是已经 events not already must be deterministic / not already settled / not already same order as results 正式三事 bundled（382 item 3 余量） interchangeable / 382 syncingheight item 3 interchangeable。**  
   官方写：`events` 的 Deterministic 列是 No。看见回了事件，不是已经必须像状态那样只依赖上一份状态和决定块 interchangeable——本页从 382 item 3 侧钉 not already must be deterministic 单句。382 syncingheight vs history bundled unbundling 在本页 item 3 完成。

2. **看见回了事件 / 看见标成非确定 / Finalize 这份非确定事件 is not already 已经交差 interchangeable / 342 findet interchangeable，也不是已经 Finalize 请求回包 bundled（382） interchangeable / 784 syncingheight-notdet interchangeable / 382 syncingheight item 2 validator_updates interchangeable / 783 syncingheight-notnoset interchangeable。**  
   官方把标成非确定和已经交差分开——382 bundled 第三件事常与 342 混成「看见回了事件就已经必须确定或已经交差 interchangeable」，本页钉 not already settled 单句。

3. **看见回了事件 / 看见能按类型键值索引 / Finalize 这份非确定事件 is not already 已经是结果列表同一顺序 interchangeable，也不是已经 Finalize 请求回包 bundled（382） interchangeable / 784 syncingheight-notdet interchangeable / 782 syncingheight-nothistory interchangeable。**  
   官方把能按类型键值索引和已经是结果列表同一顺序分开。看见能按类型键值索引，不是已经是结果列表同一顺序 interchangeable。382 syncingheight vs history bundled unbundling 在本页 item 3 完成。

怎样写 Finalize 请求、怎样空着更新、怎样编事件是规范里的做法，本页不抄。

## 官方为什么这样拆

- **events not already must be deterministic ≠ 342 interchangeable：** 官方把事件非确定和状态必须确定分开。
- **events not already settled ≠ 已经交差 interchangeable：** 官方把标成非确定和已经交差分开。
- **events not already same order as results ≠ 已经是结果列表同一顺序 interchangeable：** 官方把能按类型键值索引和已经是结果列表同一顺序分开；382 syncingheight vs history bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Finalize 回包 events 标成非确定 | 不是已经必须确定（342） | 不是 syncing_to_height（782/382 item 1） |
| 看见回了事件 | 不是已经交差 | 不是 Finalize 请求回包 bundled（382） |
| 看见能按类型键值索引 | 不是已经是结果列表同一顺序 | 不是 Finalize 算出的状态就必须只依赖上一份状态和决定块（342） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 回包 events not already must be deterministic / not already settled / not already same order as results 正式三事（382 余量），必须分开 events 是不是已经必须确定 interchangeable / 342、是不是已经交差、是不是已经是结果列表同一顺序。可以跳过「看见回了事件就已经必须确定」。不要另写怎样写 Finalize 请求回包。382 syncingheight vs history bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 Finalize 请求、怎样空着更新、怎样编事件。
- Finalize 请求回包 bundled。那是不变量 382。
- syncing_to_height。那是不变量 382 item 1 余量 / 782。
- validator_updates 空。那是不变量 382 item 2 余量 / 783。
- Finalize 算出的状态就必须只依赖上一份状态和决定块。那是不变量 342。
