# 例：看见 Query 回了 / 看见 RPC 能查 / 看见查的是本节点本地 is not already already replicated interchangeable / already consensus-passed interchangeable / already network-same interchangeable

**层次**：实现 / Query 回了不是已经复制到各节点 not already replicated / not already consensus-passed / not already network-same 正式三事（329 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Query。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Query 回了不是已经复制到各节点 not already replicated / not already consensus-passed / not already network-same 正式三事（329 余量）/ not 743 query-notreplicated interchangeable / not 329 query bundled interchangeable」，不是 Query bundled（329），也不是查到了不是已经新鲜（744 item 2 余量）或实现了 Query 不是已经是正常运转必须有（745 item 3 余量）。不要另写怎样写 Query 或怎样配 RPC。

## 官方三件事

规范把 Requirements 里对 `Query` 的调用不会在各节点之间复制、查的是本节点本地状态 和「已经是 Query 回了就已经复制到各节点 interchangeable / 已经是 RPC 能查就已经过了共识 interchangeable / 已经是本地查就已经全网同一份 interchangeable / 已经是 Query bundled interchangeable」分开写成三件独立的实现事，不是「看见 Query 回了就已经复制到各节点 interchangeable / 就已经过了共识 interchangeable / 就已经全网同一份 interchangeable」一件事：

1. **看见 Query 回了 / 看见查有回包 / 看见通用查询回了 is not already 已经复制到各节点 interchangeable / 已经 replicated interchangeable / 已经复制交差 interchangeable / 329 query bundled interchangeable / 33 four gates interchangeable / query-sold-as-replicated interchangeable，也不是已经 Query bundled（329） interchangeable / 743 query-notreplicated interchangeable / 329 query item 1 interchangeable，也不是已经 Query 回了不是已经复制到各节点 not already replicated / not already consensus-passed / not already network-same 正式三事 bundled（329 item 1 余量） interchangeable / 329 query item 1 interchangeable，也不是已经查到了不是已经新鲜（744） interchangeable / 745 query-notrequired interchangeable / 314 querystate interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：对 `Query` 的调用**不会在各节点之间复制**。看见 Query 回了，不是已经 replicated interchangeable——329 钉 bundled 三事，本页从 item 1 侧钉 not already replicated 单句。看见查有回包，不是已经 Query bundled（329） interchangeable——329 钉 bundled，本页钉 item 1 第一件事。看见通用查询回了，不是已经 QueryState 已经是 ExecuteTxState（314） interchangeable——314 另钉 QueryState。329 query vs replicated bundled unbundling 在本页 item 1 启动。

2. **看见 RPC 能查 / 看见 RPC 绿了 / 看见经 RPC 暴露给用户 is not already 已经过了共识 interchangeable / 已经 consensus-passed interchangeable / 已经共识读交差 interchangeable / 329 query bundled interchangeable / 325 queryproof interchangeable，也不是已经 Query bundled（329） interchangeable / 743 query-notreplicated interchangeable / 329 query item 2 新鲜 interchangeable / 329 query item 3 必须有 interchangeable，也不是已经 Query 回了不是已经复制到各节点 not already replicated / not already consensus-passed / not already network-same 正式三事 bundled（329 item 1 余量） interchangeable / 329 query item 1 interchangeable，也不是已经复制到各节点（本页第一件事） interchangeable。**  
   官方写：CometBFT 也把 `Query` 经 RPC 暴露给用户；看见 RPC 绿了，不是已经过了共识。看见 RPC 能查，不是已经 consensus-passed interchangeable——本页钉 not already consensus-passed 单句。看见经 RPC 暴露给用户，不是已经 Query 回了 Proof 已经对上 AppHash（325） interchangeable——325 另钉证明。看见 RPC 绿了，不是已经复制到各节点（本页第一件事） interchangeable——三件事分开钉。329 query vs replicated bundled unbundling 在本页 item 1 启动。

3. **看见查的是本节点本地 / 看见本地状态 / 看见本机查询 is not already 已经全网同一份 interchangeable / 已经 network-same interchangeable / 已经全网同一份交差 interchangeable / 329 query bundled interchangeable / 314 querystate interchangeable，也不是已经 Query bundled（329） interchangeable / 743 query-notreplicated interchangeable / 329 query item 2 / 329 query item 3，也不是已经 Query 回了不是已经复制到各节点 not already replicated / not already consensus-passed / not already network-same 正式三事 bundled（329 item 1 余量） interchangeable / 329 query item 1 interchangeable，也不是已经复制到各节点（本页第一件事） interchangeable / 已经过了共识（本页第二件事） interchangeable。**  
   官方写：查的是**本节点本地**状态。看见查的是本节点本地，不是已经 network-same interchangeable——本页钉 not already network-same 单句。看见本地状态，不是已经 QueryState 已经是 ExecuteTxState（314） interchangeable——314 另钉。看见本机查询，不是已经过了共识（本页第二件事） interchangeable——三件事分开钉。329 query vs replicated bundled unbundling 在本页 item 1 完成。

怎样写 Query 处理、怎样配 RPC、怎样做默克尔证明是规范里的取值或做法，本页不抄。Query bundled（329）、查到了不是已经新鲜（329 item 2 余量 / 744）、实现了 Query 不是已经是正常运转必须有（329 item 3 余量 / 745）、QueryState 已经是 ExecuteTxState（314）、Query 回了 Proof 已经对上 AppHash（325）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **Query 回了 not already replicated ≠ 329 / 33 interchangeable：** 官方把本地查询和复制执行分开。
- **RPC 能查 not already consensus-passed ≠ 已经过了共识 interchangeable：** 官方把 RPC 暴露和已经过了共识分开。
- **查的是本节点本地 not already network-same ≠ 已经全网同一份 interchangeable：** 官方把本机查询和全网同一份分开；329 query vs replicated bundled unbundling 在本页 item 1 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Query 回了 | 不是 already replicated | 不是 QueryState alone（314） |
| RPC 能查 | 不是 already consensus-passed | 不是 Query Proof alone（325） |
| 查的是本节点本地 | 不是 already network-same | 不是四门 alone（33） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 回了不是已经复制到各节点 not already replicated / not already consensus-passed / not already network-same 正式三事（329 余量），必须分开 Query 回了 是不是 already replicated interchangeable / 329 query bundled interchangeable / query-sold-as-replicated interchangeable、RPC 能查 是不是 already consensus-passed interchangeable、查的是本节点本地 是不是 already network-same interchangeable。可以跳过「看见 Query 回了就已经复制到各节点 interchangeable / 就已经过了共识 interchangeable / 就已经全网同一份 interchangeable」。不要另写怎样写 Query。329 query vs replicated bundled unbundling 在本页 item 1 启动；续 [`worked-example-query-notfresh-vs-bundled.md`](worked-example-query-notfresh-vs-bundled.md)（不变量 744 item 2）。

## 本页不抄

- 怎样写 Query 处理、怎样配 RPC、怎样做默克尔证明。
- Query bundled。那是不变量 329。
- 查到了不是已经新鲜。那是不变量 329 item 2 余量 / 744。
- 实现了 Query 不是已经是正常运转必须有。那是不变量 329 item 3 余量 / 745。
- QueryState 已经是 ExecuteTxState。那是不变量 314。
- Query 回了 Proof 已经对上 AppHash。那是不变量 325。
- 四门已经结算。那是不变量 33。
