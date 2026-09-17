# 例：看见 Query 回包 value 是对上的那份数据的值 is not already AppHash matched interchangeable / not already replicated interchangeable / not already settled interchangeable

**层次**：实现 / Query 回包 value not already AppHash matched / not already replicated / not already settled 正式三事（380 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Response。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Query 回包 value not already AppHash matched / not already replicated / not already settled 正式三事（380 余量）/ not 790 queryindex-notapphash interchangeable / not 380 queryindex-vs-store bundled interchangeable」，不是 Query 回包 bundled（380），也不是 Query 回了 Proof 就已经对上 AppHash（325），也不是 Query 回了就已经复制到各节点（329）。不要另写怎样写 Query 回包。

## 官方三件事

1. **看见 Query 回包 `value` 是对上的那份数据的值 / 看见回了值 / Query 这份回包值 is not already 已经对上 AppHash interchangeable / 325 queryproof interchangeable，也不是已经 Query 回包 bundled（380） interchangeable / 790 queryindex-notapphash interchangeable / 788 queryindex-notstore interchangeable / 380 queryindex item 1 index interchangeable，也不是已经 value not already AppHash matched / not already replicated / not already settled 正式三事 bundled（380 item 3 余量） interchangeable / 380 queryindex item 3 interchangeable。**  
   官方写：`value` 是对上的那份数据的值。看见回了值，不是已经对上 AppHash interchangeable——本页从 380 item 3 侧钉 not already AppHash matched 单句。380 queryindex vs store bundled unbundling 在本页 item 3 完成。

2. **看见回了值 / 看见有字节 / Query 这份回包值 is not already 已经复制到各节点 interchangeable / 329 queryrep interchangeable，也不是已经 Query 回包 bundled（380） interchangeable / 790 queryindex-notapphash interchangeable / 380 queryindex item 2 key interchangeable / 789 queryindex-notheight interchangeable，也不是已经 Query 回了 Proof 就已经对上 AppHash interchangeable / 325 queryproof interchangeable。**  
   官方把有字节和已经复制到各节点分开——380 bundled 第三件事常与 325 / 329 混成「看见回了值就已经对上 AppHash 或已经复制到各节点 interchangeable」，本页钉 not already replicated 单句。

3. **看见回了值 / 看见能读 / Query 这份回包值 is not already 已经交差 interchangeable，也不是已经 Query 回包 bundled（380） interchangeable / 790 queryindex-notapphash interchangeable / 788 queryindex-notstore interchangeable。**  
   官方把能读 value 和已经交差分开。看见能读，不是已经交差 interchangeable。380 queryindex vs store bundled unbundling 在本页 item 3 完成。

怎样写 Query 回包、怎样填下标、怎样对键值是规范里的做法，本页不抄。

## 官方为什么这样拆

- **value not already AppHash matched ≠ 325 interchangeable：** 官方把回包值和证明对上 AppHash 分开。
- **value not already replicated ≠ 329 interchangeable：** 官方把有字节和已经复制到各节点分开。
- **value not already settled ≠ 已经交差 interchangeable：** 官方把能读 value 和已经交差分开；380 queryindex vs store bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Query 回包 value 是对上的那份数据的值 | 不是已经对上 AppHash（325） | 不是 Query 回包 index（788/380 item 1） |
| 看见回了值 | 不是已经复制到各节点（329） | 不是 Query 回了 Proof 就已经对上 AppHash（325） |
| 看见能读 | 不是已经交差 | 不是 Query 回包 bundled（380） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 回包 value not already AppHash matched / not already replicated / not already settled 正式三事（380 余量），必须分开 value 是不是已经对上 AppHash interchangeable / 325、是不是已经复制到各节点 interchangeable / 329、是不是已经交差。可以跳过「看见回了值就已经对上 AppHash」。不要另写怎样写 Query 回包。380 queryindex vs store bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 Query 回包、怎样填下标、怎样对键值。
- Query 回包 bundled。那是不变量 380。
- Query 回包 index。那是不变量 380 item 1 余量 / 788。
- Query 回包 key。那是不变量 380 item 2 余量 / 789。
- Query 回了 Proof 就已经对上 AppHash。那是不变量 325。
- Query 回了就已经复制到各节点。那是不变量 329。
