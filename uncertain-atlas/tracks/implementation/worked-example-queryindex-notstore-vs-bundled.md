# 例：看见 Query 回包 index 是树里这个键的下标 is not already key lookup interchangeable / not already AppHash matched interchangeable / not already settled interchangeable

**层次**：实现 / Query 回包 index not already key lookup / not already AppHash matched / not already settled 正式三事（380 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Response。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Query 回包 index not already key lookup / not already AppHash matched / not already settled 正式三事（380 余量）/ not 788 queryindex-notstore interchangeable / not 380 queryindex-vs-store bundled interchangeable」，不是 Query 回包 bundled（380），也不是 path /store 就必须按键查就已经是引擎在用（377），也不是 Query 回包 info 就已经是按键查（384/778），也不是 Query 回包 proof_ops 就已经是按键查（383/780）。不要另写怎样写 Query 回包。

## 官方三件事

1. **看见 Query 回包 `index` 是树里这个键的下标 / 看见有下标 / Query 这份回包下标 is not already 已经按 `/store` 按键查 interchangeable / 377 querystore interchangeable，也不是已经 Query 回包 bundled（380） interchangeable / 788 queryindex-notstore interchangeable / 789 queryindex-notheight interchangeable / 380 queryindex item 2 key interchangeable，也不是已经 index not already key lookup / not already AppHash matched / not already settled 正式三事 bundled（380 item 1 余量） interchangeable / 380 queryindex item 1 interchangeable。**  
   官方写：`index` 是树里这个键的下标。看见有下标，不是已经按 `/store` 按键查 interchangeable——本页从 380 item 1 侧钉 not already key lookup 单句。380 queryindex vs store bundled unbundling 在本页 item 1 启动。

2. **看见有下标 / 看见填了下标 / Query 这份回包下标 is not already 已经对上 AppHash interchangeable / 377 querystore interchangeable，也不是已经 Query 回包 bundled（380） interchangeable / 788 queryindex-notstore interchangeable / 380 queryindex item 3 value interchangeable / 790 queryindex-notapphash interchangeable，也不是已经 Query 回包 info 就已经是按键查 interchangeable / 384 querycode / 778 querycode-notkey interchangeable，也不是已经 Query 回包 proof_ops 就已经是按键查 interchangeable / 383 queryprove / 780 queryprove-notstore interchangeable。**  
   官方把填了下标和已经对上 AppHash 分开——380 bundled 第一件事常与 377 / 384 / 383 混成「看见有下标就已经是按键查或已经对上 AppHash interchangeable」，本页钉 not already AppHash matched 单句。

3. **看见有下标 / 看见有数 / Query 这份回包下标 is not already 已经交差 interchangeable，也不是已经 Query 回包 bundled（380） interchangeable / 788 queryindex-notstore interchangeable / 789 queryindex-notheight interchangeable。**  
   官方把有数和已经交差分开。看见有数，不是已经交差 interchangeable。380 queryindex vs store bundled unbundling 在本页 item 1 启动。

怎样写 Query 回包、怎样填下标、怎样对键值是规范里的做法，本页不抄。

## 官方为什么这样拆

- **index not already key lookup ≠ 377 interchangeable：** 官方把回包下标和请求必须按键查分开。
- **index not already AppHash matched ≠ 已经对上 AppHash interchangeable：** 官方把填了下标和已经对上 AppHash 分开。
- **index not already settled ≠ 已经交差 interchangeable：** 官方把有数和已经交差分开；380 queryindex vs store bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Query 回包 index 是树里这个键的下标 | 不是已经是按键查（377） | 不是 Query 回包 key（789/380 item 2） |
| 看见有下标 | 不是已经对上 AppHash | 不是 Query 回包 bundled（380） |
| 看见有数 | 不是已经交差 | 不是 Query 回包 info（384/778） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 回包 index not already key lookup / not already AppHash matched / not already settled 正式三事（380 余量），必须分开 index 是不是已经是按键查 interchangeable / 377、是不是已经对上 AppHash、是不是已经交差。可以跳过「看见有下标就已经是按键查」。不要另写怎样写 Query 回包。380 queryindex vs store bundled unbundling 在本页 item 1 启动；续 [`worked-example-queryindex-notheight-vs-bundled.md`](worked-example-queryindex-notheight-vs-bundled.md)（不变量 789 item 2）。

## 本页不抄

- 怎样写 Query 回包、怎样填下标、怎样对键值。
- Query 回包 bundled。那是不变量 380。
- Query 回包 key。那是不变量 380 item 2 余量 / 789。
- Query 回包 value。那是不变量 380 item 3 余量 / 790。
- path /store 就必须按键查就已经是引擎在用。那是不变量 377。
- Query 回包 info 就已经是按键查。那是不变量 384 / 778。
- Query 回包 proof_ops 就已经是按键查。那是不变量 383 / 780。
