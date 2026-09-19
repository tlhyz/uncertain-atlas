# 例：看见回了列表 / 条数一样 / Finalize 回了 is not already already same order interchangeable / already count-implies-order interchangeable / already engine-ordered interchangeable

**层次**：实现 / 结果列表不是已经同一顺序 not already same order / not already count-implies-order / not already engine-ordered 正式三事（316 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Transaction Results / Specifics of `ExecTxResult`。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「结果列表不是已经同一顺序 not already same order / not already count-implies-order / not already engine-ordered 正式三事（316 余量）/ not 707 exectxresult-notorder interchangeable / not 316 exectxresult bundled interchangeable」，不是 ExecTxResult vs consensus bundled（316），也不是 Code 非零不是已经没进块（708 item 2 余量）或 Code / Data 不是已经印进本头（709 item 3 余量）。不要另写怎样编回执或怎样建索引。

## 官方三件事

规范把 Requirements 里应用应回一份 `ExecTxResult` 列表、这份列表**必须**和 `FinalizeBlockRequest` 送来的交易列表同一顺序 和「已经是回了列表就已经对上顺序 interchangeable / 已经是条数一样就已经按送来的顺序 interchangeable / 已经是 Finalize 回了就已经由引擎排好 interchangeable / 已经是 ExecTxResult vs consensus bundled interchangeable」分开写成三件独立的实现事，不是「看见回了结果 就已经对上顺序 interchangeable / 就已经条数等于顺序 interchangeable / 就已经引擎排好 interchangeable」一件事：

1. **看见回了列表 / 看见结果列表 / 看见 FinalizeBlockResponse 有列表 is not already 已经和送来的交易同一顺序 interchangeable / 已经 same order interchangeable / 已经对上 interchangeable / 316 exectxresult bundled interchangeable / 33 four gates interchangeable / exectxresult-sold-as-consensus interchangeable，也不是已经 ExecTxResult vs consensus bundled（316） interchangeable / 707 exectxresult-notorder interchangeable / 316 exectxresult item 1 interchangeable，也不是已经结果列表不是已经同一顺序 not already same order / not already count-implies-order / not already engine-ordered 正式三事 bundled（316 item 1 余量） interchangeable / 316 exectxresult item 1 interchangeable，也不是已经 Code 非零不是已经没进块（708） interchangeable / 709 exectxresult-notheader interchangeable / 147 apphash interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：应用应回一份 `ExecTxResult` 列表；这份列表**必须**和送来的交易列表同一顺序。看见回了列表，不是已经对上 interchangeable——316 钉 bundled 三事，本页从 item 1 侧钉 not already same order 单句。看见结果列表，不是已经 ExecTxResult vs consensus bundled（316） interchangeable——316 钉 bundled，本页钉 item 1 第一件事。看见 FinalizeBlockResponse 有列表，不是已经 Code 非零不是已经没进块（708） interchangeable——708 另钉 item 2，本页钉 item 1 第一件事。316 exectxresult vs consensus bundled unbundling 在本页 item 1 启动。

2. **看见条数一样 / 看见结果条数等于交易条数 / 看见列表长度对上 is not already 已经按送来的顺序 interchangeable / 已经 count-implies-order interchangeable / 已经长度等于顺序 interchangeable / 316 exectxresult bundled interchangeable / 33 four gates interchangeable，也不是已经 ExecTxResult vs consensus bundled（316） interchangeable / 707 exectxresult-notorder interchangeable / 316 exectxresult item 2 Code 非零 interchangeable / 316 exectxresult item 3 Code Data interchangeable，也不是已经结果列表不是已经同一顺序 not already same order / not already count-implies-order / not already engine-ordered 正式三事 bundled（316 item 1 余量） interchangeable / 316 exectxresult item 1 interchangeable，也不是已经同一顺序（本页第一件事） interchangeable。**  
   官方把必须同一顺序和已经条数一样就等于顺序路径分开——条数一样，不等于已经按送来的顺序。看见条数一样，不是已经按送来的顺序 interchangeable——本页钉 not already count-implies-order 单句。看见结果条数等于交易条数，不是已经 Code 非零不是已经没进块（708） interchangeable——708 另钉 item 2，本页钉 item 1 第二件事。看见列表长度对上，不是已经 Code / Data 不是已经印进本头（709） interchangeable——709 另钉 item 3，本页钉 item 1 第二件事。316 exectxresult vs consensus bundled unbundling 在本页 item 1 启动。

3. **看见 Finalize 回了 / 看见 FinalizeBlock 回了结果 / 看见引擎收下了回包 is not already 已经由引擎排好 interchangeable / 已经 engine-ordered interchangeable / 已经引擎替你排好 interchangeable / 316 exectxresult bundled interchangeable / 147 apphash interchangeable，也不是已经 ExecTxResult vs consensus bundled（316） interchangeable / 707 exectxresult-notorder interchangeable / 316 exectxresult item 2 / 316 exectxresult item 3，也不是已经结果列表不是已经同一顺序 not already same order / not already count-implies-order / not already engine-ordered 正式三事 bundled（316 item 1 余量） interchangeable / 316 exectxresult item 1 interchangeable，也不是已经同一顺序（本页第一件事） interchangeable / 已经条数等于顺序（本页第二件事） interchangeable。**  
   官方把必须同一顺序写成应用义务，不是引擎已经排好——Finalize 回了，不等于引擎已经替你排好。看见 Finalize 回了，不是已经由引擎排好 interchangeable——本页钉 not already engine-ordered 单句。看见 FinalizeBlock 回了结果，不是已经同一顺序（本页第一件事） interchangeable——三件事分开钉。看见引擎收下了回包，不是已经本头 AppHash 已经是本高度交差（147） interchangeable——147 另钉。316 exectxresult vs consensus bundled unbundling 在本页 item 1 完成。

怎样编回执、怎样建索引、怎样算 LastResultsHash 是规范里的取值或做法，本页不抄。ExecTxResult vs consensus bundled（316）、Code 非零不是已经没进块（316 item 2 余量 / 708）、Code / Data 不是已经印进本头（316 item 3 余量 / 709）、四门已经结算（33）、本头 AppHash（147）是另外那套，本页不抄。

## 官方为什么这样拆

- **回了列表 not already same order ≠ 316 / 33 interchangeable：** 官方把必须同一顺序单句和已经对上路径分开。
- **条数一样 not already count-implies-order ≠ 已经按送来的顺序 interchangeable：** 官方把条数单句和已经顺序路径分开。
- **Finalize 回了 not already engine-ordered ≠ 已经由引擎排好 interchangeable：** 官方把应用义务单句和引擎已经排好路径分开；316 exectxresult vs consensus bundled unbundling 在本页 item 1 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 回了列表 | 不是 already same order | 不是 Code 非零 alone（708） |
| 条数一样 | 不是 already count-implies-order | 不是 Code/Data 印本头 alone（709） |
| Finalize 回了 | 不是 already engine-ordered | 不是四门 alone（33） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看结果列表不是已经同一顺序 not already same order / not already count-implies-order / not already engine-ordered 正式三事（316 余量），必须分开回了列表 是不是 already same order interchangeable / 316 exectxresult bundled interchangeable / exectxresult-sold-as-consensus interchangeable、条数一样 是不是 already count-implies-order interchangeable、Finalize 回了 是不是 already engine-ordered interchangeable。可以跳过「看见回了就已经对上顺序 interchangeable / 就已经条数等于顺序 interchangeable / 就已经引擎排好 interchangeable」。不要另写怎样编回执。316 exectxresult vs consensus bundled unbundling 在本页 item 1 完成；续 [`worked-example-exectxresult-notexcluded-vs-bundled.md`](worked-example-exectxresult-notexcluded-vs-bundled.md)（不变量 708 item 2）。

## 本页不抄

- 怎样编回执、怎样建索引、怎样算 LastResultsHash。
- ExecTxResult vs consensus bundled。那是不变量 316。
- Code 非零不是已经没进块。那是不变量 316 item 2 余量 / 708。
- Code / Data 不是已经印进本头。那是不变量 316 item 3 余量 / 709。
- 四门已经结算。那是不变量 33。
- 本头 AppHash 已经是本高度交差。那是不变量 147。
