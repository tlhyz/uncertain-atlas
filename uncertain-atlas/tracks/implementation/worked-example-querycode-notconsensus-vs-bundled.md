# 例：看见 Query 回包 code 是回包码 is not already past consensus interchangeable / not already CheckTx reject-broadcast interchangeable / not already settled interchangeable

**层次**：实现 / Query 回包 code not already past consensus / not already CheckTx reject-broadcast / not already settled 正式三事（384 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Response。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Query 回包 code not already past consensus / not already CheckTx reject-broadcast / not already settled 正式三事（384 余量）/ not 776 querycode-notconsensus interchangeable / not 384 querycode-vs-consensus bundled interchangeable」，不是 Query 回包码 bundled（384），也不是引擎对回包码不再赋予别的含义就已经被引擎用了 Data（373）。不要另写怎样写 Query 回包码。

## 官方三件事

1. **看见 Query 回包 `code` 是回包码 / 看见回了码 / Query 这份回包码 is not already 已经过了共识 interchangeable，也不是已经 Query 回包码 bundled（384） interchangeable / 776 querycode-notconsensus interchangeable / 777 querycode-notfresh interchangeable / 384 querycode item 2 log interchangeable，也不是已经 code not already past consensus / not already CheckTx reject-broadcast / not already settled 正式三事 bundled（384 item 1 余量） interchangeable / 384 querycode item 1 interchangeable。**  
   官方写：`code` 是回包码。看见回了码，不是已经过了共识 interchangeable——本页从 384 item 1 侧钉 not already past consensus 单句。384 querycode vs consensus bundled unbundling 在本页 item 1 启动。

2. **看见回了码 / 看见有码 / Query 这份回包码 is not already 已经是 CheckTx 那种拒广播 interchangeable / 373 chktxcode interchangeable，也不是已经 Query 回包码 bundled（384） interchangeable / 776 querycode-notconsensus interchangeable / 384 querycode item 3 info interchangeable / 778 querycode-notkey interchangeable。**  
   官方把 Query 回包码和已经是 CheckTx 那种拒广播分开——384 bundled 第一件事常与 373 混成「看见回了码就已经过了共识或已经是 CheckTx 那种拒广播 interchangeable」，本页钉 not already CheckTx reject-broadcast 单句。

3. **看见回了码 / 看见能回 / Query 这份回包码 is not already 已经交差 interchangeable，也不是已经 Query 回包码 bundled（384） interchangeable / 776 querycode-notconsensus interchangeable / 777 querycode-notfresh interchangeable。**  
   官方把能回 Query code 和已经交差分开。看见能回，不是已经交差 interchangeable。384 querycode vs consensus bundled unbundling 在本页 item 1 启动。

怎样写 Query 回包码、怎样填日志、怎样填附加信息是规范里的做法，本页不抄。

## 官方为什么这样拆

- **code not already past consensus ≠ 已经过了共识 interchangeable：** 官方把 Query 回包码和已经过了共识分开。
- **code not already CheckTx reject-broadcast ≠ 373 interchangeable：** 官方把有码和已经是 CheckTx 那种拒广播分开。
- **code not already settled ≠ 已经交差 interchangeable：** 官方把能回 code 和已经交差分开；384 querycode vs consensus bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Query 回包 code 是回包码 | 不是已经过了共识 | 不是 Query 回包 log（777/384 item 2） |
| 看见回了码 | 不是已经是 CheckTx 那种拒广播（373） | 不是 Query 回包码 bundled（384） |
| 看见能回 | 不是已经交差 | 不是引擎对回包码不再赋予别的含义就已经被引擎用了 Data（373） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 回包 code not already past consensus / not already CheckTx reject-broadcast / not already settled 正式三事（384 余量），必须分开 code 是不是已经过了共识、是不是已经是 CheckTx 那种拒广播 interchangeable / 373、是不是已经交差。可以跳过「看见回了码就已经过了共识」。不要另写怎样写 Query 回包码。384 querycode vs consensus bundled unbundling 在本页 item 1 启动；续 [`worked-example-querycode-notfresh-vs-bundled.md`](worked-example-querycode-notfresh-vs-bundled.md)（不变量 777 item 2）。

## 本页不抄

- 怎样写 Query 回包码、怎样填日志、怎样填附加信息。
- Query 回包码 bundled。那是不变量 384。
- Query 回包 log。那是不变量 384 item 2 余量 / 777。
- Query 回包 info。那是不变量 384 item 3 余量 / 778。
- 引擎对回包码不再赋予别的含义就已经被引擎用了 Data。那是不变量 373。
