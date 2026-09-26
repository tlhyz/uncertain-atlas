# 例：看见回了事件 / 看见标成非确定 / 看见能按类型键值索引 is not already already mustdet interchangeable / already settled interchangeable / already ordered interchangeable

**层次**：实现 / Finalize 回包 events 标成非确定不是已经必须确定 not already mustdet / not already settled / not already ordered 正式三事（382 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Finalize 回包 events 标成非确定不是已经必须确定 not already mustdet / not already settled / not already ordered 正式三事（382 余量）/ not 895 syncingheight-notmustdet interchangeable / not 382 syncingheight bundled interchangeable」，不是 syncingheight bundled（382），也不是 syncing_to_height 同步或重放时是目标高、否则等于本高不是已经有完整历史（382 item 1 / 893）或 validator_updates 空则引擎保持当前集合不是已经没有集合（382 item 2 / 894）。不要另写怎样写 Finalize 请求回包。

## 官方三件事

规范把 Methods 里 Finalize 回包 events 标成非确定 和「已经是回了事件就已经必须确定 interchangeable / 已经是标成非确定就已经交差 interchangeable / 已经是能按类型键值索引就已经是结果列表同一顺序 interchangeable / 已经是 syncingheight bundled interchangeable」分开写成三件独立的实现事，不是「看见回了事件就已经必须确定 interchangeable / 就已经交差 interchangeable / 就已经是结果列表同一顺序 interchangeable」一件事：

1. **看见回了事件 / 看见 Finalize 回包 events 标成非确定 / 看见 events 的 Deterministic 列是 No is not already 已经必须确定 interchangeable / 已经 mustdet interchangeable / 已经必须像状态那样只依赖上一份状态和决定块交差 interchangeable / 382 syncingheight bundled interchangeable / 342 finalizedet interchangeable / syncingheight-sold-as-history interchangeable，也不是已经 syncingheight bundled（382） interchangeable / 895 syncingheight-notmustdet interchangeable / 382 syncingheight item 3 interchangeable，也不是已经 Finalize 回包 events 标成非确定不是已经必须确定 not already mustdet / not already settled / not already ordered 正式三事 bundled（382 item 3 余量） interchangeable / 382 syncingheight item 3 interchangeable，也不是已经填了目标就已经有完整历史（382 item 1 / 893） interchangeable / 空着就已经没有集合（382 item 2 / 894） interchangeable / 342 finalizedet interchangeable，也不是已经 Finalize 算出的状态就必须只依赖上一份状态和决定块（342） interchangeable。**  
   官方写：`events` 的 Deterministic 列是 No。看见回了事件，不是已经必须像状态那样只依赖上一份状态和决定块。看见回了事件，不是已经 mustdet interchangeable——382 钉 bundled 三事，本页从 item 3 侧钉 not already mustdet 单句。看见 Finalize 回包 events 标成非确定，不是已经 syncingheight bundled（382） interchangeable——382 钉 bundled，本页钉 item 3 第一件事。看见 Deterministic 列是 No，不是已经 Finalize 算出的状态就必须只依赖上一份状态和决定块（342） interchangeable——342 另钉。382 syncingheight-vs-history bundled unbundling 在本页 item 3 完成。

2. **看见标成非确定 / 看见 Deterministic 是 No / 看见事件不必像状态那样确定 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 382 syncingheight bundled interchangeable / 316 txresults interchangeable，也不是已经 syncingheight bundled（382） interchangeable / 895 syncingheight-notmustdet interchangeable / 382 syncingheight item 1 填了目标 interchangeable / 382 syncingheight item 2 空着 interchangeable，也不是已经 Finalize 回包 events 标成非确定不是已经必须确定 not already mustdet / not already settled / not already ordered 正式三事 bundled（382 item 3 余量） interchangeable / 382 syncingheight item 3 interchangeable，也不是已经必须确定（本页第一件事） interchangeable。**  
   官方写：看见标成非确定，不是已经交差。看见 Deterministic 是 No，不是已经 settled interchangeable——本页钉 not already settled 单句。看见事件不必像状态那样确定，不是已经必须确定（本页第一件事） interchangeable——三件事分开钉。382 syncingheight-vs-history bundled unbundling 在本页 item 3 完成。

3. **看见能按类型键值索引 / 看见有 events 类型键值 / 看见能按账户建索引 is not already 已经是结果列表同一顺序 interchangeable / 已经 ordered interchangeable / 已经是共识顺序交差 interchangeable / 382 syncingheight bundled interchangeable / 316 txresults interchangeable，也不是已经 syncingheight bundled（382） interchangeable / 895 syncingheight-notmustdet interchangeable / 382 syncingheight item 1 / 382 syncingheight item 2，也不是已经 Finalize 回包 events 标成非确定不是已经必须确定 not already mustdet / not already settled / not already ordered 正式三事 bundled（382 item 3 余量） interchangeable / 382 syncingheight item 3 interchangeable，也不是已经必须确定（本页第一件事） interchangeable / 已经交差（本页第二件事） interchangeable。**  
   官方写：看见能按类型键值索引，不是已经是结果列表同一顺序。看见有 events 类型键值，不是已经 ordered interchangeable——本页钉 not already ordered 单句。看见能按账户建索引，不是已经交差（本页第二件事） interchangeable——三件事分开钉。382 syncingheight-vs-history bundled unbundling 在本页 item 3 完成。

怎样写 Finalize 请求、怎样空着更新、怎样编事件是规范里的做法，本页不抄。syncingheight bundled（382）、syncing_to_height 同步或重放时是目标高、否则等于本高不是已经有完整历史（382 item 1 / 893）、validator_updates 空则引擎保持当前集合不是已经没有集合（382 item 2 / 894）、Finalize 算出的状态就必须只依赖上一份状态和决定块（342）、结果列表就已经同一顺序（316）、切进共识就已经有从创世的完整历史（323）是另外那套，本页不抄。

## 官方为什么这样拆

- **回了事件 not already mustdet ≠ 382 / 342 interchangeable：** 官方把事件非确定和状态必须确定分开。
- **标成非确定 not already settled ≠ 已经交差 interchangeable：** 官方把标成非确定和已经交差分开。
- **能按类型键值索引 not already ordered ≠ 已经是结果列表同一顺序 interchangeable：** 官方把事件索引和结果列表顺序分开；382 syncingheight-vs-history bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 回了事件 | 不是 already mustdet | 不是 Finalize 算出的状态就必须只依赖上一份状态和决定块 alone（342） |
| 标成非确定 | 不是 already settled | 不是空着 already empty alone（894） |
| 能按类型键值索引 | 不是 already ordered | 不是结果列表就已经同一顺序 alone（316） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 回包 events 标成非确定不是已经必须确定 not already mustdet / not already settled / not already ordered 正式三事（382 余量），必须分开回了事件 是不是 already mustdet interchangeable / 382 syncingheight bundled interchangeable / syncingheight-sold-as-history interchangeable、标成非确定 是不是 already settled interchangeable、能按类型键值索引 是不是 already ordered interchangeable。可以跳过「看见回了事件就已经必须确定 interchangeable / 就已经交差 interchangeable / 就已经是结果列表同一顺序 interchangeable」。不要另写怎样写 Finalize 请求回包。382 syncingheight-vs-history bundled unbundling 在本页 item 3 完成（895）。

## 本页不抄

- 怎样写 Finalize 请求、怎样空着更新、怎样编事件。
- syncingheight bundled。那是不变量 382。
- syncing_to_height 同步或重放时是目标高、否则等于本高不是已经有完整历史。那是不变量 382 item 1 / 893。
- validator_updates 空则引擎保持当前集合不是已经没有集合。那是不变量 382 item 2 / 894。
- Finalize 算出的状态就必须只依赖上一份状态和决定块。那是不变量 342。
- 结果列表就已经同一顺序。那是不变量 316。
- 切进共识就已经有从创世的完整历史。那是不变量 323。
