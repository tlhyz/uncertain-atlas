# 例：看见 Query 回包 key 是对上的那份数据的键 is not already Query height interchangeable / not already fresh interchangeable / not already settled interchangeable

**层次**：实现 / Query 回包 key not already Query height / not already fresh / not already settled 正式三事（380 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Response。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Query 回包 key not already Query height / not already fresh / not already settled 正式三事（380 余量）/ not 789 queryindex-notheight interchangeable / not 380 queryindex-vs-store bundled interchangeable」，不是 Query 回包 bundled（380），也不是 Query 可以对当前或过去高度查就已经是 QueryState（371），也不是 ProofOp.key 就已经是 Query 回包键（390/743）。不要另写怎样写 Query 回包。

## 官方三件事

1. **看见 Query 回包 `key` 是对上的那份数据的键 / 看见回了键 / Query 这份回包键 is not already 已经填了高度 interchangeable / 371 queryheight interchangeable，也不是已经 Query 回包 bundled（380） interchangeable / 789 queryindex-notheight interchangeable / 788 queryindex-notstore interchangeable / 380 queryindex item 1 index interchangeable，也不是已经 key not already Query height / not already fresh / not already settled 正式三事 bundled（380 item 2 余量） interchangeable / 380 queryindex item 2 interchangeable。**  
   官方写：`key` 是对上的那份数据的键。看见回了键，不是已经填了高度 interchangeable——本页从 380 item 2 侧钉 not already Query height 单句。380 queryindex vs store bundled unbundling 在本页 item 2 续。

2. **看见回了键 / 看见有键 / Query 这份回包键 is not already 已经新鲜 interchangeable / 371 queryheight interchangeable，也不是已经 Query 回包 bundled（380） interchangeable / 789 queryindex-notheight interchangeable / 380 queryindex item 3 value interchangeable / 790 queryindex-notapphash interchangeable，也不是已经 ProofOp.key 就已经是 Query 回包键 interchangeable / 390 proofop / 743 proofop-notquerykey interchangeable。**  
   官方把有键和已经新鲜分开——380 bundled 第二件事常与 371 / 390 混成「看见回了键就已经是 Query 高度或已经新鲜 interchangeable」，本页钉 not already fresh 单句。

3. **看见回了键 / 看见能回 / Query 这份回包键 is not already 已经交差 interchangeable，也不是已经 Query 回包 bundled（380） interchangeable / 789 queryindex-notheight interchangeable / 788 queryindex-notstore interchangeable。**  
   官方把能回 key 和已经交差分开。看见能回，不是已经交差 interchangeable。380 queryindex vs store bundled unbundling 在本页 item 2 续。

怎样写 Query 回包、怎样填下标、怎样对键值是规范里的做法，本页不抄。

## 官方为什么这样拆

- **key not already Query height ≠ 371 interchangeable：** 官方把回包键和查询高度分开。
- **key not already fresh ≠ 已经新鲜 interchangeable：** 官方把有键和已经新鲜分开。
- **key not already settled ≠ 已经交差 interchangeable：** 官方把能回 key 和已经交差分开；380 queryindex vs store bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Query 回包 key 是对上的那份数据的键 | 不是已经是 Query 高度（371） | 不是 Query 回包 index（788/380 item 1） |
| 看见回了键 | 不是已经新鲜 | 不是 ProofOp.key（390/743） |
| 看见能回 | 不是已经交差 | 不是 Query 回包 bundled（380） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 回包 key not already Query height / not already fresh / not already settled 正式三事（380 余量），必须分开 key 是不是已经是 Query 高度 interchangeable / 371、是不是已经新鲜、是不是已经交差。可以跳过「看见回了键就已经是 Query 高度」。不要另写怎样写 Query 回包。380 queryindex vs store bundled unbundling 在本页 item 2 续；完成 [`worked-example-queryindex-notapphash-vs-bundled.md`](worked-example-queryindex-notapphash-vs-bundled.md)（不变量 790 item 3）。

## 本页不抄

- 怎样写 Query 回包、怎样填下标、怎样对键值。
- Query 回包 bundled。那是不变量 380。
- Query 回包 index。那是不变量 380 item 1 余量 / 788。
- Query 回包 value。那是不变量 380 item 3 余量 / 790。
- Query 可以对当前或过去高度查就已经是 QueryState。那是不变量 371。
- ProofOp.key 就已经是 Query 回包键。那是不变量 390 / 743。
