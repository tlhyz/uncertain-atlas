# 例：看见 Query 回了 is not already replicated interchangeable / not already consensus interchangeable / not already settled interchangeable

**层次**：实现 / Query 回了 not already replicated / not already consensus / not already settled 正式三事（329 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Query。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「Query 回了 not already replicated / not already consensus / not already settled 正式三事（329 余量）/ not 938 query-notrepl interchangeable / not 329 query-vs-replicated bundled interchangeable」，不是 Query bundled（329），也不是 QueryState 已经是 ExecuteTxState（314），也不是 Query 回了 Proof 已经对上 AppHash（325）。不要另写怎样写 Query 或怎样配 RPC。

## 官方三件事

1. **看见 Query 回了 / 看见 RPC 能查 这份回包 is not already 已经复制到各节点 interchangeable，也不是已经 Query bundled（329） interchangeable / 938 query-notrepl interchangeable / 939 query-notfresh interchangeable / 329 query item 2 查到了 interchangeable，也不是已经 Query 回了 not already replicated / not already consensus / not already settled 正式三事 bundled（329 item 1 余量） interchangeable / 329 query item 1 interchangeable。**  
   官方写：Query 是通用方法，给应用状态上各种查询留空。CometBFT 用它按 ID 和 IP 过滤新邻居，也把 Query 经 RPC 暴露给用户。对 Query 的调用不会在各节点之间复制，查的是本节点本地状态。看见回了，不是已经全网同一份 interchangeable——本页从 329 item 1 侧钉 not already replicated 单句。329 query vs replicated bundled unbundling 在本页 item 1 启动。

2. **看见 RPC 绿了 / 看见回了 / 这份回包 is not already 已经过了共识 interchangeable，也不是已经 Query bundled（329） interchangeable / 938 query-notrepl interchangeable / 329 query item 3 实现了 interchangeable / 940 query-notmust interchangeable，也不是已经 QueryState 已经是 ExecuteTxState interchangeable / 314 querystate interchangeable。**  
   官方把 RPC 绿了和已经过了共识分开——329 bundled 第一件事常与 314 混成「看见 Query 回了就已经复制或已经是 ExecuteTxState interchangeable」，本页钉 not already consensus 单句。

3. **看见 RPC 绿了 / 看见回了 / 这份回包 is not already 已经交差 interchangeable，也不是已经 Query bundled（329） interchangeable / 938 query-notrepl interchangeable / 939 query-notfresh interchangeable，也不是已经 Query 回了 Proof 已经对上 AppHash interchangeable / 325 query-proof interchangeable。**  
   官方把 RPC 绿了和已经交差分开。看见 RPC 绿了，不是已经交差 interchangeable。329 query vs replicated bundled unbundling 在本页 item 1 启动。

怎样写 Query 处理、怎样配 RPC、怎样做默克尔证明是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **Query 回了 not already replicated ≠ 已经复制到各节点 interchangeable：** 官方把本地查询和复制执行分开。
- **看见 RPC 绿了 not already consensus ≠ 已经过了共识 interchangeable：** 官方把 RPC 绿了和已经过了共识分开。
- **看见 RPC 绿了 not already settled ≠ 已经交差 interchangeable：** 官方把 RPC 绿了和已经交差分开；329 query vs replicated bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Query 回了 | 不是已经复制到各节点 | 不是 QueryState 已经是 ExecuteTxState（314） |
| 看见 RPC 绿了 | 不是已经过了共识 | 不是 Query 回了 Proof 已经对上 AppHash（325） |
| 看见回了 | 不是已经交差 | 不是查到了就已经新鲜（939） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 回了 not already replicated / not already consensus / not already settled 正式三事（329 余量），必须分开是不是已经复制到各节点、是不是已经过了共识、是不是已经交差。可以跳过「看见查到了就已经共识」。不要另写怎样写 Query 或怎样配 RPC。329 query vs replicated bundled unbundling 在本页 item 1 启动；续 [`worked-example-query-notfresh-vs-bundled.md`](worked-example-query-notfresh-vs-bundled.md)（不变量 939 item 2）。

## 本页不抄

- 怎样写 Query 处理、怎样配 RPC、怎样做默克尔证明。
- Query bundled。那是不变量 329。
- 查到了就已经新鲜。那是不变量 329 item 2 余量 / 939。
- QueryState 已经是 ExecuteTxState。那是不变量 314。
