# 例：看见实现了 Query is not already required for normal operation interchangeable / not already peer-filter interchangeable / not already settled interchangeable

**层次**：实现 / 实现了 Query not already required for normal operation / not already peer-filter / not already settled 正式三事（329 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Query。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「实现了 Query not already required for normal operation / not already peer-filter / not already settled 正式三事（329 余量）/ not 940 query-notmust interchangeable / not 329 query-vs-replicated bundled interchangeable」，不是 Query bundled（329），也不是发了 addr 过滤查询已经收下这个人（326），也不是应用选择不实现就已经没有 state sync（334/934）。不要另写怎样写 Query 或怎样配 RPC。

## 官方三件事

1. **看见实现了 Query / 看见规范写了 Query 这份方法 is not already 已经是正常运转必须有 interchangeable，也不是已经 Query bundled（329） interchangeable / 940 query-notmust interchangeable / 938 query-notrepl interchangeable / 329 query item 1 回了 interchangeable，也不是已经实现了 Query not already required for normal operation / not already peer-filter / not already settled 正式三事 bundled（329 item 3 余量） interchangeable / 329 query item 3 interchangeable。**  
   官方写：CometBFT 技术上对正常运转没有来自 Query 消息的要求。应用开发者可以不实现 Query。看见规范写了，不是已经必须有 interchangeable——本页从 329 item 3 侧钉 not already required for normal operation 单句。329 query vs replicated bundled unbundling 在本页 item 3 完成。

2. **看见实现了 / 看见规范写了 / 这份方法 is not already 已经是邻居过滤 interchangeable，也不是已经 Query bundled（329） interchangeable / 940 query-notmust interchangeable / 329 query item 2 查到了 interchangeable / 939 query-notfresh interchangeable，也不是已经发了 addr 过滤查询已经收下这个人 interchangeable / 326 peerfilter interchangeable。**  
   官方把实现了和已经是邻居过滤 / 已经是默克尔证明分开——329 bundled 第三件事常与 326 混成「看见实现了就已经必须有或已经是过滤 interchangeable」，本页钉 not already peer-filter 单句。

3. **看见实现了 / 看见规范写了 / 这份方法 is not already 已经交差 interchangeable，也不是已经 Query bundled（329） interchangeable / 940 query-notmust interchangeable / 938 query-notrepl interchangeable，也不是已经应用选择不实现就已经没有 state sync interchangeable / 334/934 snapshot-conn-notgone interchangeable。**  
   官方把实现了和已经交差分开。看见实现了，不是已经交差 interchangeable。329 query vs replicated bundled unbundling 在本页 item 3 完成。

怎样写 Query 处理、怎样配 RPC、怎样做默克尔证明是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **实现了 Query not already required for normal operation ≠ 已经是正常运转必须有 interchangeable：** 官方把可以有的 Query 和正常运转必须有的消息分开。
- **看见实现了 not already peer-filter ≠ 已经是邻居过滤 interchangeable：** 官方把实现了和已经是邻居过滤 / 已经是默克尔证明分开。
- **看见实现了 not already settled ≠ 已经交差 interchangeable：** 官方把实现了和已经交差分开；329 query vs replicated bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 实现了 Query | 不是已经是正常运转必须有 | 不是发了 addr 过滤查询已经收下这个人（326） |
| 看见规范写了 Query | 不是已经是邻居过滤 | 不是应用选择不实现就已经没有 state sync（334/934） |
| 看见实现了 | 不是已经交差 | 不是 Query 回了就已经复制（938） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看实现了 Query not already required for normal operation / not already peer-filter / not already settled 正式三事（329 余量），必须分开是不是已经是正常运转必须有、是不是已经是邻居过滤、是不是已经交差。可以跳过「看见规范写了就已经必须实现」。不要另写怎样写 Query 或怎样配 RPC。329 query vs replicated bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 Query 处理、怎样配 RPC、怎样做默克尔证明。
- Query bundled。那是不变量 329。
- Query 回了就已经复制。那是不变量 329 item 1 余量 / 938。
- 发了 addr 过滤查询已经收下这个人。那是不变量 326。
- 应用选择不实现就已经没有 state sync。那是不变量 334/934。
