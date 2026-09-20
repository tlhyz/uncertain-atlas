# 例：看见 Query 回了不是已经复制到各节点；看见查到了不是已经新鲜；看见实现了 Query 不是已经是正常运转必须有

**层次**：实现 / Query。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Query。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「Query 回了不是已经复制到各节点 / 查到了不是已经新鲜 / 实现了 Query 不是已经是正常运转必须有」，不是 QueryState 已经是 ExecuteTxState，也不是 Query 回了 Proof 已经对上 AppHash。不要另写怎样写 Query 或怎样配 RPC。 329 query vs replicated bundled unbundling 启动（743）；精读 [`worked-example-query-notreplicated-vs-bundled.md`](worked-example-query-notreplicated-vs-bundled.md)。

## 官方三件事

规范把 Query 写成三件独立的实现事，不是「看见查到了就已经共识、已经新鲜、已经必须实现」一件事：

1. **看见 Query 回了 / 看见 RPC 能查 不是已经复制到各节点，也不是已经过了共识。**  
   官方写：`Query` 是通用方法，给应用状态上各种查询留空。CometBFT 用它按 ID 和 IP 过滤新邻居，也把 `Query` 经 RPC 暴露给用户。**对 `Query` 的调用不会在各节点之间复制**，查的是**本节点本地**状态。看见回了，不是已经全网同一份。看见 RPC 绿了，不是已经过了共识。
2. **看见查到了 / 看见本地有这份 不是已经新鲜，也不是已经是当前尖。**  
   官方写：因此它们**可能读到旧的**。需要共识的读，必须走交易。看见查到了，不是已经跟上尖。看见本地有这份，不是已经是决定块之后的那份。
3. **看见实现了 Query / 看见规范写了 Query 不是已经是正常运转必须有，也不是已经是过滤或证明。**  
   官方写：CometBFT **技术上对正常运转没有**来自 `Query` 消息的要求。应用开发者**可以不实现** Query。看见规范写了，不是已经必须有。看见实现了，不是已经是邻居过滤，也不是已经是默克尔证明。

怎样写 Query 处理、怎样配 RPC、怎样做默克尔证明是规范里的取值或做法，本页不抄。QueryState 不是 ExecuteTxState 是不变量 314，本页不抄。

## 官方为什么这样拆

- **Query 回了 ≠ 已经复制到各节点：** 官方把本地查询和复制执行分开。
- **查到了 ≠ 已经新鲜：** 官方把可能读到旧的和必须走交易的共识读分开。
- **实现了 Query ≠ 已经是正常运转必须有：** 官方把可以有的 Query 和正常运转必须有的消息分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Query 回了 | 不是已经复制到各节点 | 不是 QueryState 已经是 ExecuteTxState（314） |
| 查到了 | 不是已经新鲜 | 不是 Query 回了 Proof 已经对上 AppHash（325） |
| 实现了 Query | 不是已经是正常运转必须有 | 不是发了 addr 过滤查询已经收下这个人（326） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「查到了就已经共识、已经新鲜、已经必须实现」，必须分开 Query 回了是不是已经复制到各节点、查到了是不是已经新鲜、实现了 Query 是不是已经是正常运转必须有。可以跳过「看见查到了就已经共识」。不要另写怎样写 Query 或怎样配 RPC。 329 query vs replicated bundled unbundling 启动（743 item 1）。

## 本页不抄

- 怎样写 Query 处理、怎样配 RPC、怎样做默克尔证明。
- QueryState 已经是 ExecuteTxState。那是不变量 314。
- Query 回了 Proof 已经对上 AppHash。那是不变量 325。
- 发了 addr 过滤查询已经收下这个人。那是不变量 326。
