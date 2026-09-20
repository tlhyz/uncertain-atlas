# 例：看见实现了 Query / 看见邻居过滤 / 看见默克尔证明 is not already already required interchangeable / already filter interchangeable / already proof interchangeable

**层次**：实现 / 实现了 Query 不是已经是正常运转必须有 not already required / not already filter / not already proof 正式三事（329 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Query。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「实现了 Query 不是已经是正常运转必须有 not already required / not already filter / not already proof 正式三事（329 余量）/ not 745 query-notrequired interchangeable / not 329 query bundled interchangeable」，不是 Query bundled（329），也不是 Query 回了不是已经复制到各节点（743 item 1 余量）或查到了不是已经新鲜（744 item 2 余量）。不要另写怎样写 Query 或怎样配 RPC。

## 官方三件事

规范把 Requirements 里正常运转技术上不要求 Query、可以不实现、实现了不等于过滤或证明 和「已经是实现了 Query 就已经是正常运转必须有 interchangeable / 已经是邻居过滤就已经是过滤交差 interchangeable / 已经是默克尔证明就已经是证明交差 interchangeable / 已经是 Query bundled interchangeable」分开写成三件独立的实现事，不是「看见实现了 Query 就已经是正常运转必须有 interchangeable / 就已经是邻居过滤 interchangeable / 就已经是默克尔证明 interchangeable」一件事：

1. **看见实现了 Query / 看见规范写了 Query / 看见有 Query is not already 已经是正常运转必须有 interchangeable / 已经 required interchangeable / 已经必须有交差 interchangeable / 329 query bundled interchangeable / 33 four gates interchangeable / query-sold-as-replicated interchangeable，也不是已经 Query bundled（329） interchangeable / 745 query-notrequired interchangeable / 329 query item 3 interchangeable，也不是已经实现了 Query 不是已经是正常运转必须有 not already required / not already filter / not already proof 正式三事 bundled（329 item 3 余量） interchangeable / 329 query item 3 interchangeable，也不是已经 Query 回了不是已经复制到各节点（743） interchangeable / 744 query-notfresh interchangeable / 326 peerfilter interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：CometBFT **技术上对正常运转没有**来自 `Query` 消息的要求；应用开发者**可以不实现** Query。看见实现了 Query，不是已经 required interchangeable——329 钉 bundled 三事，本页从 item 3 侧钉 not already required 单句。看见规范写了 Query，不是已经 Query bundled（329） interchangeable——329 钉 bundled，本页钉 item 3 第一件事。看见有 Query，不是已经查到了不是已经新鲜（744） interchangeable——744 另钉 item 2。329 query vs replicated bundled unbundling 在本页 item 3 完成。

2. **看见邻居过滤 / 看见按 ID IP 过滤 / 看见过滤查询 is not already 已经是邻居过滤交差 interchangeable / 已经 filter interchangeable / 已经过滤交差 interchangeable / 329 query bundled interchangeable / 326 peerfilter interchangeable，也不是已经 Query bundled（329） interchangeable / 745 query-notrequired interchangeable / 329 query item 1 复制 interchangeable / 329 query item 2 新鲜 interchangeable，也不是已经实现了 Query 不是已经是正常运转必须有 not already required / not already filter / not already proof 正式三事 bundled（329 item 3 余量） interchangeable / 329 query item 3 interchangeable，也不是已经是正常运转必须有（本页第一件事） interchangeable。**  
   官方写：看见实现了，不是已经是邻居过滤。看见邻居过滤，不是已经 filter interchangeable——本页钉 not already filter 单句。看见按 ID IP 过滤，不是已经发了 addr 过滤查询已经收下这个人（326） interchangeable——326 另钉 peerfilter。看见过滤查询，不是已经是正常运转必须有（本页第一件事） interchangeable——三件事分开钉。329 query vs replicated bundled unbundling 在本页 item 3 完成。

3. **看见默克尔证明 / 看见有 Proof / 看见证明回了 is not already 已经是默克尔证明交差 interchangeable / 已经 proof interchangeable / 已经证明交差 interchangeable / 329 query bundled interchangeable / 325 queryproof interchangeable，也不是已经 Query bundled（329） interchangeable / 745 query-notrequired interchangeable / 329 query item 1 / 329 query item 2，也不是已经实现了 Query 不是已经是正常运转必须有 not already required / not already filter / not already proof 正式三事 bundled（329 item 3 余量） interchangeable / 329 query item 3 interchangeable，也不是已经是正常运转必须有（本页第一件事） interchangeable / 已经是邻居过滤（本页第二件事） interchangeable。**  
   官方写：看见实现了，不是已经是默克尔证明。看见默克尔证明，不是已经 proof interchangeable——本页钉 not already proof 单句。看见有 Proof，不是已经 Query 回了 Proof 已经对上 AppHash（325） interchangeable——325 另钉证明对上。看见证明回了，不是已经是邻居过滤（本页第二件事） interchangeable——三件事分开钉。329 query vs replicated bundled unbundling 在本页 item 3 完成。

怎样写 Query 处理、怎样配 RPC、怎样做默克尔证明是规范里的取值或做法，本页不抄。Query bundled（329）、Query 回了不是已经复制到各节点（329 item 1 余量 / 743）、查到了不是已经新鲜（329 item 2 余量 / 744）、发了 addr 过滤查询已经收下这个人（326）、Query 回了 Proof 已经对上 AppHash（325）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **实现了 Query not already required ≠ 329 / 33 interchangeable：** 官方把可以有的 Query 和正常运转必须有分开。
- **邻居过滤 not already filter ≠ 已经是过滤交差 interchangeable：** 官方把实现了 Query 和已经是邻居过滤分开。
- **默克尔证明 not already proof ≠ 已经是证明交差 interchangeable：** 官方把实现了 Query 和已经是默克尔证明分开；329 query vs replicated bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 实现了 Query | 不是 already required | 不是新鲜 alone（744） |
| 邻居过滤 | 不是 already filter | 不是 peerfilter alone（326） |
| 默克尔证明 | 不是 already proof | 不是 Query Proof alone（325） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看实现了 Query 不是已经是正常运转必须有 not already required / not already filter / not already proof 正式三事（329 余量），必须分开实现了 Query 是不是 already required interchangeable / 329 query bundled interchangeable / query-sold-as-replicated interchangeable、邻居过滤 是不是 already filter interchangeable、默克尔证明 是不是 already proof interchangeable。可以跳过「看见实现了 Query 就已经是正常运转必须有 interchangeable / 就已经是邻居过滤 interchangeable / 就已经是默克尔证明 interchangeable」。不要另写怎样写 Query。329 query vs replicated bundled unbundling 在本页 item 3 完成（743 + 744 + 745）。

## 本页不抄

- 怎样写 Query 处理、怎样配 RPC、怎样做默克尔证明。
- Query bundled。那是不变量 329。
- Query 回了不是已经复制到各节点。那是不变量 329 item 1 余量 / 743。
- 查到了不是已经新鲜。那是不变量 329 item 2 余量 / 744。
- 发了 addr 过滤查询已经收下这个人。那是不变量 326。
- Query 回了 Proof 已经对上 AppHash。那是不变量 325。
- 四门已经结算。那是不变量 33。
