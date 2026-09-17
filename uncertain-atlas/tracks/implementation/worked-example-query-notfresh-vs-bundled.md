# 例：看见查到了 is not already fresh interchangeable / not already tip interchangeable / not already settled interchangeable

**层次**：实现 / 查到了 not already fresh / not already tip / not already settled 正式三事（329 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Query。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「查到了 not already fresh / not already tip / not already settled 正式三事（329 余量）/ not 939 query-notfresh interchangeable / not 329 query-vs-replicated bundled interchangeable」，不是 Query bundled（329），也不是 Query 回了 Proof 已经对上 AppHash（325），也不是发了 addr 过滤查询已经收下这个人（326）。不要另写怎样写 Query 或怎样配 RPC。

## 官方三件事

1. **看见查到了 / 看见本地有这份 这份读 is not already 已经新鲜 interchangeable，也不是已经 Query bundled（329） interchangeable / 939 query-notfresh interchangeable / 938 query-notrepl interchangeable / 329 query item 1 回了 interchangeable，也不是已经查到了 not already fresh / not already tip / not already settled 正式三事 bundled（329 item 2 余量） interchangeable / 329 query item 2 interchangeable。**  
   官方写：因此它们可能读到旧的。需要共识的读，必须走交易。看见查到了，不是已经跟上尖 interchangeable——本页从 329 item 2 侧钉 not already fresh 单句。329 query vs replicated bundled unbundling 在本页 item 2 续。

2. **看见本地有这份 / 看见查到了 / 这份读 is not already 已经是当前尖 interchangeable，也不是已经 Query bundled（329） interchangeable / 939 query-notfresh interchangeable / 329 query item 3 实现了 interchangeable / 940 query-notmust interchangeable，也不是已经 Query 回了 Proof 已经对上 AppHash interchangeable / 325 query-proof interchangeable。**  
   官方把本地有这份和已经是决定块之后的那份分开——329 bundled 第二件事常与 325 混成「看见查到了就已经新鲜或已经对上 AppHash interchangeable」，本页钉 not already tip 单句。

3. **看见本地有这份 / 看见查到了 / 这份读 is not already 已经交差 interchangeable，也不是已经 Query bundled（329） interchangeable / 939 query-notfresh interchangeable / 938 query-notrepl interchangeable，也不是已经发了 addr 过滤查询已经收下这个人 interchangeable / 326 peerfilter interchangeable。**  
   官方把本地有这份和已经交差分开。看见本地有这份，不是已经交差 interchangeable。329 query vs replicated bundled unbundling 在本页 item 2 续。

怎样写 Query 处理、怎样配 RPC、怎样做默克尔证明是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **查到了 not already fresh ≠ 已经新鲜 interchangeable：** 官方把可能读到旧的和必须走交易的共识读分开。
- **看见本地有这份 not already tip ≠ 已经是当前尖 interchangeable：** 官方把本地有这份和已经是决定块之后的那份分开。
- **看见本地有这份 not already settled ≠ 已经交差 interchangeable：** 官方把本地有这份和已经交差分开；329 query vs replicated bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 查到了 | 不是已经新鲜 | 不是 Query 回了 Proof 已经对上 AppHash（325） |
| 看见本地有这份 | 不是已经是当前尖 | 不是发了 addr 过滤查询已经收下这个人（326） |
| 看见查到了 | 不是已经交差 | 不是 Query 回了就已经复制（938） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看查到了 not already fresh / not already tip / not already settled 正式三事（329 余量），必须分开是不是已经新鲜、是不是已经是当前尖、是不是已经交差。可以跳过「看见查到了就已经新鲜」。不要另写怎样写 Query 或怎样配 RPC。329 query vs replicated bundled unbundling 在本页 item 2 续；续 [`worked-example-query-notmust-vs-bundled.md`](worked-example-query-notmust-vs-bundled.md)（不变量 940 item 3）。

## 本页不抄

- 怎样写 Query 处理、怎样配 RPC、怎样做默克尔证明。
- Query bundled。那是不变量 329。
- Query 回了就已经复制。那是不变量 329 item 1 余量 / 938。
- Query 回了 Proof 已经对上 AppHash。那是不变量 325。
- 发了 addr 过滤查询已经收下这个人。那是不变量 326。
