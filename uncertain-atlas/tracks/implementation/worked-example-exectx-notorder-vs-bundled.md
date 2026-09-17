# 例：看见结果列表 is not already same-order interchangeable / not already same-count interchangeable / not already engine-sorted interchangeable

**层次**：实现 / 结果列表 not already same-order / not already same-count / not already engine-sorted 正式三事（316 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Transaction Results / ExecTxResult。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「结果列表 not already same-order / not already same-count / not already engine-sorted 正式三事（316 余量）/ not 1013 exectx-notorder interchangeable / not 316 exectxresult-vs-consensus bundled interchangeable」，不是 ExecTxResult bundled（316），也不是四门已经结算（33），也不是 HasChannel 就已经入队（309/1010）。不要另写怎样编回执或怎样建索引。

## 官方三件事

1. **看见结果列表 / 看见 FinalizeBlockResponse 这份回执 is not already 已经和送来的交易同一顺序 interchangeable，也不是已经 ExecTxResult bundled（316） interchangeable / 1013 exectx-notorder interchangeable / 1014 exectx-notout interchangeable / 316 exectx item 2 Code 非零 interchangeable，也不是已经结果列表 not already same-order / not already same-count / not already engine-sorted 正式三事 bundled（316 item 1 余量） interchangeable / 316 exectx item 1 interchangeable。**  
   官方写：应用应回一份 ExecTxResult 列表。这份列表必须和 FinalizeBlockRequest 送来的交易列表同一顺序。看见回了列表，不是已经对上 interchangeable——本页从 316 item 1 侧钉 not already same-order 单句。316 exectxresult vs consensus bundled unbundling 在本页 item 1 启动。

2. **看见条数一样 / 看见回了列表 / 这份回执 is not already 已经按送来的顺序 interchangeable，也不是已经 ExecTxResult bundled（316） interchangeable / 1013 exectx-notorder interchangeable / 316 exectx item 3 Code Data interchangeable / 1015 exectx-notheader interchangeable，也不是已经四门已经结算 interchangeable / 33 four-gates interchangeable。**  
   官方把条数一样和已经按送来的顺序分开。看见条数一样，不是已经按送来的顺序 interchangeable。本页钉 not already same-count 单句。

3. **看见 Finalize 回了 / 看见回了列表 / 这份回执 is not already 引擎已经替你排好 interchangeable，也不是已经 ExecTxResult bundled（316） interchangeable / 1013 exectx-notorder interchangeable / 1014 exectx-notout interchangeable，也不是已经 HasChannel 就已经入队 interchangeable / 309/1010 sendq-notqueued interchangeable。**  
   官方把 Finalize 回了和引擎已经替你排好分开。看见 Finalize 回了，不是引擎已经替你排好 interchangeable。316 exectxresult vs consensus bundled unbundling 在本页 item 1 启动。

怎样编回执、怎样建索引、怎样算 LastResultsHash 是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **结果列表 not already same-order ≠ 已经和送来的交易同一顺序 interchangeable：** 官方把必须同一顺序写成应用义务，不是引擎已经排好。
- **看见条数一样 not already same-count ≠ 已经按送来的顺序 interchangeable：** 官方把条数一样和已经按送来的顺序分开。
- **看见 Finalize 回了 not already engine-sorted ≠ 引擎已经替你排好 interchangeable：** 官方把 Finalize 回了和引擎已经替你排好分开；316 exectxresult vs consensus bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 结果列表顺序 | 不是已经和送来的交易同一顺序 | 不是四门已经结算（33） |
| 看见条数一样 | 不是已经按送来的顺序 | 不是 HasChannel 就已经入队（309/1010） |
| 看见 Finalize 回了 | 不是引擎已经替你排好 | 不是 Code 非零就已经没进块（1014） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看结果列表 not already same-order / not already same-count / not already engine-sorted 正式三事（316 余量），必须分开是不是已经同一顺序、是不是已经按送来的顺序、是不是引擎已经替你排好。可以跳过「看见回了就已经对上顺序」。不要另写怎样编回执或怎样建索引。316 exectxresult vs consensus bundled unbundling 在本页 item 1 启动；续 [`worked-example-exectx-notout-vs-bundled.md`](worked-example-exectx-notout-vs-bundled.md)（不变量 1014 item 2）。

## 本页不抄

- 怎样编回执、怎样建索引、怎样算 LastResultsHash。
- ExecTxResult bundled。那是不变量 316。
- 四门已经结算。那是不变量 33。
- HasChannel 就已经入队。那是不变量 309/1010。
