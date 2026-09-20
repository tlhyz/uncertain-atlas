# 例：看见查到了 / 看见本地有这份 / 看见决定块之后那份 is not already already fresh interchangeable / already tip interchangeable / already decided-state interchangeable

**层次**：实现 / 查到了不是已经新鲜 not already fresh / not already tip / not already decided-state 正式三事（329 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Query。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「查到了不是已经新鲜 not already fresh / not already tip / not already decided-state 正式三事（329 余量）/ not 744 query-notfresh interchangeable / not 329 query bundled interchangeable」，不是 Query bundled（329），也不是 Query 回了不是已经复制到各节点（743 item 1 余量）或实现了 Query 不是已经是正常运转必须有（745 item 3 余量）。不要另写怎样写 Query 或怎样配 RPC。

## 官方三件事

规范把 Requirements 里 Query 可能读到旧的、需要共识的读必须走交易 和「已经是查到了就已经新鲜 interchangeable / 已经是本地有这份就已经是当前尖 interchangeable / 已经是决定块之后那份就已经是决定后状态 interchangeable / 已经是 Query bundled interchangeable」分开写成三件独立的实现事，不是「看见查到了就已经新鲜 interchangeable / 就已经是当前尖 interchangeable / 就已经是决定块之后那份 interchangeable」一件事：

1. **看见查到了 / 看见本地有这份 / 看见查有结果 is not already 已经新鲜 interchangeable / 已经 fresh interchangeable / 已经新鲜交差 interchangeable / 329 query bundled interchangeable / 33 four gates interchangeable / query-sold-as-replicated interchangeable，也不是已经 Query bundled（329） interchangeable / 744 query-notfresh interchangeable / 329 query item 2 interchangeable，也不是已经查到了不是已经新鲜 not already fresh / not already tip / not already decided-state 正式三事 bundled（329 item 2 余量） interchangeable / 329 query item 2 interchangeable，也不是已经 Query 回了不是已经复制到各节点（743） interchangeable / 745 query-notrequired interchangeable / 314 querystate interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：因此它们**可能读到旧的**。看见查到了，不是已经 fresh interchangeable——329 钉 bundled 三事，本页从 item 2 侧钉 not already fresh 单句。看见本地有这份，不是已经 Query bundled（329） interchangeable——329 钉 bundled，本页钉 item 2 第一件事。看见查有结果，不是已经 Query 回了不是已经复制到各节点（743） interchangeable——743 另钉 item 1。329 query vs replicated bundled unbundling 在本页 item 2 续。

2. **看见跟上了尖 / 看见当前尖 / 看见尖上这份 is not already 已经是当前尖 interchangeable / 已经 tip interchangeable / 已经尖交差 interchangeable / 329 query bundled interchangeable / 325 queryproof interchangeable，也不是已经 Query bundled（329） interchangeable / 744 query-notfresh interchangeable / 329 query item 1 复制 interchangeable / 329 query item 3 必须有 interchangeable，也不是已经查到了不是已经新鲜 not already fresh / not already tip / not already decided-state 正式三事 bundled（329 item 2 余量） interchangeable / 329 query item 2 interchangeable，也不是已经新鲜（本页第一件事） interchangeable。**  
   官方写：需要共识的读，必须走交易；看见查到了，不是已经跟上尖。看见跟上了尖，不是已经 tip interchangeable——本页钉 not already tip 单句。看见当前尖，不是已经 Query 回了 Proof 已经对上 AppHash（325） interchangeable——325 另钉证明。看见尖上这份，不是已经新鲜（本页第一件事） interchangeable——三件事分开钉。329 query vs replicated bundled unbundling 在本页 item 2 续。

3. **看见决定块之后那份 / 看见决定后状态 / 看见已决定状态 is not already 已经是决定块之后那份 interchangeable / 已经 decided-state interchangeable / 已经决定后交差 interchangeable / 329 query bundled interchangeable / 314 querystate interchangeable，也不是已经 Query bundled（329） interchangeable / 744 query-notfresh interchangeable / 329 query item 1 / 329 query item 3，也不是已经查到了不是已经新鲜 not already fresh / not already tip / not already decided-state 正式三事 bundled（329 item 2 余量） interchangeable / 329 query item 2 interchangeable，也不是已经新鲜（本页第一件事） interchangeable / 已经是当前尖（本页第二件事） interchangeable。**  
   官方写：看见本地有这份，不是已经是决定块之后的那份。看见决定块之后那份，不是已经 decided-state interchangeable——本页钉 not already decided-state 单句。看见决定后状态，不是已经 QueryState 已经是 ExecuteTxState（314） interchangeable——314 另钉。看见已决定状态，不是已经是当前尖（本页第二件事） interchangeable——三件事分开钉。329 query vs replicated bundled unbundling 在本页 item 2 完成。

怎样写 Query 处理、怎样配 RPC、怎样做默克尔证明是规范里的取值或做法，本页不抄。Query bundled（329）、Query 回了不是已经复制到各节点（329 item 1 余量 / 743）、实现了 Query 不是已经是正常运转必须有（329 item 3 余量 / 745）、QueryState 已经是 ExecuteTxState（314）、Query 回了 Proof 已经对上 AppHash（325）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **查到了 not already fresh ≠ 329 / 33 interchangeable：** 官方把可能读到旧的和已经新鲜分开。
- **跟上了尖 not already tip ≠ 已经是当前尖 interchangeable：** 官方把本地查到和已经跟上尖分开。
- **决定块之后那份 not already decided-state ≠ 已经是决定后状态 interchangeable：** 官方把本地有这份和已经是决定块之后那份分开；329 query vs replicated bundled unbundling 在本页 item 2 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 查到了 | 不是 already fresh | 不是复制 alone（743） |
| 跟上了尖 | 不是 already tip | 不是 Query Proof alone（325） |
| 决定块之后那份 | 不是 already decided-state | 不是 QueryState alone（314） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看查到了不是已经新鲜 not already fresh / not already tip / not already decided-state 正式三事（329 余量），必须分开查到了 是不是 already fresh interchangeable / 329 query bundled interchangeable / query-sold-as-replicated interchangeable、跟上了尖 是不是 already tip interchangeable、决定块之后那份 是不是 already decided-state interchangeable。可以跳过「看见查到了就已经新鲜 interchangeable / 就已经是当前尖 interchangeable / 就已经是决定块之后那份 interchangeable」。不要另写怎样写 Query。329 query vs replicated bundled unbundling 在本页 item 2 续（743 + 744）；续 [`worked-example-query-notrequired-vs-bundled.md`](worked-example-query-notrequired-vs-bundled.md)（不变量 745 item 3）。

## 本页不抄

- 怎样写 Query 处理、怎样配 RPC、怎样做默克尔证明。
- Query bundled。那是不变量 329。
- Query 回了不是已经复制到各节点。那是不变量 329 item 1 余量 / 743。
- 实现了 Query 不是已经是正常运转必须有。那是不变量 329 item 3 余量 / 745。
- QueryState 已经是 ExecuteTxState。那是不变量 314。
- Query 回了 Proof 已经对上 AppHash。那是不变量 325。
- 四门已经结算。那是不变量 33。
