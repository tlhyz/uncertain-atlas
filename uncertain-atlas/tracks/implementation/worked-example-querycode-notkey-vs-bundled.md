# 例：看见 Query 回包 info 是附加信息 is not already key lookup interchangeable / not already AppHash matched interchangeable / not already settled interchangeable

**层次**：实现 / Query 回包 info not already key lookup / not already AppHash matched / not already settled 正式三事（384 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Response。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Query 回包 info not already key lookup / not already AppHash matched / not already settled 正式三事（384 余量）/ not 778 querycode-notkey interchangeable / not 384 querycode-vs-consensus bundled interchangeable」，不是 Query 回包码 bundled（384），也不是 Query 回包 value 就已经对上 AppHash（380），也不是 CheckTx 回包 info 就已经是 Query 附加信息（391/754），也不是 ExecTxResult.info 就已经是 Query 附加信息（414/759）。不要另写怎样写 Query 回包码。

## 官方三件事

1. **看见 Query 回包 `info` 是附加信息 / 看见回了信息 / Query 这份附加信息 is not already 已经按 `/store` 按键查 interchangeable，也不是已经 Query 回包码 bundled（384） interchangeable / 778 querycode-notkey interchangeable / 776 querycode-notconsensus interchangeable / 384 querycode item 1 code interchangeable，也不是已经 info not already key lookup / not already AppHash matched / not already settled 正式三事 bundled（384 item 3 余量） interchangeable / 384 querycode item 3 interchangeable。**  
   官方写：`info` 是附加信息。看见回了信息，不是已经按 `/store` 按键查 interchangeable——本页从 384 item 3 侧钉 not already key lookup 单句。384 querycode vs consensus bundled unbundling 在本页 item 3 完成。

2. **看见回了信息 / 看见有附加字段 / Query 这份附加信息 is not already 已经对上 AppHash interchangeable / 380 queryval interchangeable，也不是已经 Query 回包码 bundled（384） interchangeable / 778 querycode-notkey interchangeable / 384 querycode item 2 log interchangeable / 777 querycode-notfresh interchangeable，也不是已经 CheckTx 回包 info 就已经是 Query 附加信息 interchangeable / 391 checktxtx / 754 checktxtx-notqueryinfo interchangeable，也不是已经 ExecTxResult.info 就已经是 Query 附加信息 interchangeable / 414 exectxlog / 759 exectxlog-notchecktxinfo interchangeable。**  
   官方把附加信息和已经对上 AppHash 分开——384 bundled 第三件事常与 380 / 391 / 414 混成「看见回了信息就已经是按键查或已经对上 AppHash interchangeable」，本页钉 not already AppHash matched 单句。

3. **看见回了信息 / 看见能回 / Query 这份附加信息 is not already 已经交差 interchangeable，也不是已经 Query 回包码 bundled（384） interchangeable / 778 querycode-notkey interchangeable / 776 querycode-notconsensus interchangeable。**  
   官方把能回 Query info 和已经交差分开。看见能回，不是已经交差 interchangeable。384 querycode vs consensus bundled unbundling 在本页 item 3 完成。

怎样写 Query 回包码、怎样填日志、怎样填附加信息是规范里的做法，本页不抄。

## 官方为什么这样拆

- **info not already key lookup ≠ 已经是按键查 interchangeable：** 官方把附加信息和回包键值分开。
- **info not already AppHash matched ≠ 380 interchangeable：** 官方把有附加字段和已经对上 AppHash 分开。
- **info not already settled ≠ 已经交差 interchangeable：** 官方把能回 info 和已经交差分开；384 querycode vs consensus bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Query 回包 info 是附加信息 | 不是已经是按键查 | 不是 Query 回包 code（776/384 item 1） |
| 看见回了信息 | 不是已经对上 AppHash（380） | 不是 CheckTx 回包 info（391/754） |
| 看见能回 | 不是已经交差 | 不是 ExecTxResult.info（414/759） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 回包 info not already key lookup / not already AppHash matched / not already settled 正式三事（384 余量），必须分开 info 是不是已经是按键查、是不是已经对上 AppHash interchangeable / 380、是不是已经交差。可以跳过「看见回了信息就已经是按键查」。不要另写怎样写 Query 回包码。384 querycode vs consensus bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 Query 回包码、怎样填日志、怎样填附加信息。
- Query 回包码 bundled。那是不变量 384。
- Query 回包 code。那是不变量 384 item 1 余量 / 776。
- Query 回包 log。那是不变量 384 item 2 余量 / 777。
- Query 回包 value 就已经对上 AppHash。那是不变量 380。
- CheckTx 回包 info 就已经是 Query 附加信息。那是不变量 391 / 754。
- ExecTxResult.info 就已经是 Query 附加信息。那是不变量 414 / 759。
