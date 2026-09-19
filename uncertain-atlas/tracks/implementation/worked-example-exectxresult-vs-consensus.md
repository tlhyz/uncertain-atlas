# 例：看见结果列表不是已经和送来的交易同一顺序；看见 Code 非零不是已经没进块；看见 Code / Data 不是已经印进本头

**层次**：实现 / ExecTxResult。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Transaction Results / Specifics of `ExecTxResult`。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「结果列表不是已经同一顺序 / Code 非零不是已经没进块 / Code Data 不是已经印进本头」，不是四门已经结算，也不是本头 AppHash 已经是本高度交差。不要另写怎样编回执或怎样建索引。

## 官方三件事

规范把 `FinalizeBlock` 回的 `ExecTxResult` 写成三件独立的实现事，不是「看见回了结果就已经对上顺序、已经没进块、已经印进本头」一件事：

1. **看见结果列表 / 看见 FinalizeBlockResponse 不是已经和送来的交易同一顺序。**  
   官方写：应用应回一份 `ExecTxResult` 列表。这份列表**必须**和 `FinalizeBlockRequest` 送来的交易列表同一顺序。看见回了列表，不是已经对上。看见条数一样，不是已经按送来的顺序。看见 Finalize 回了，不是引擎已经替你排好。
2. **看见 Code ≠ 0 / 看见标成无效 不是已经没进块，也不是已经建了索引。**  
   官方写：`FinalizeBlock` 把已决定块连同全部交易同步交给应用。正确节点上这块（因而交易顺序）由共识的 Agreement 保证同一份。若 `Code ≠ 0`，这笔会被标成无效，**但仍在块里**。无效交易**不建索引**，官方把它类比成没过 `CheckTx` 的那些。看见标成无效，不是已经没进块。看见没索引，不是已经没进共识。看见类比 CheckTx，不是已经和池门同一把尺。
3. **看见 Code / Data / 看见 Events 不是已经印进本头 LastResultsHash，也不是已经是共识字段。**  
   官方写：`Data` 必须确定，可装任意字节；`Code` 也必须确定。`Code` 和 `Data` 会编进一份结构，再哈希进**下一高度**块头的 `LastResultsHash`。`Events` 只供 CometBFT 按执行里发生的事建索引、以后按事件查询。`Info` 和 `Log` 是非确定的调试字段，CometBFT 会记日志，**此外忽略**。看见 Code / Data，不是已经印进本头。看见 Events，不是已经进了那份哈希。看见 Info / Log，不是已经是共识。

怎样编回执、怎样建索引、怎样算 LastResultsHash 是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **回了列表 ≠ 已经同一顺序：** 官方把必须同一顺序写成应用义务，不是引擎已经排好。
- **Code 非零 ≠ 已经没进块：** 官方把标无效、仍在块里、不建索引分开。
- **Code / Data ≠ 已经印进本头：** 官方把下一高度的 LastResultsHash 和 Events / Info / Log 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 结果列表顺序 | 不是已经和送来的交易同一顺序 | 不是四门已经结算（33） |
| Code ≠ 0 仍在块里 | 不是已经没进块，也不是已经建了索引 | 不是 MaxGas 已经在执行（315） |
| Code / Data 进下一头 | 不是已经印进本头 | 不是本头 AppHash 已经是本高度交差（147） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「Finalize 已经回了结果」，必须分开列表是不是已经同一顺序、Code 非零是不是已经没进块、Code / Data 是不是已经印进本头。可以跳过「看见回了就已经对上顺序」。不要另写怎样编回执或怎样建索引。316 exectxresult vs consensus bundled unbundling 续（707 + 708）；精读 [`worked-example-exectxresult-notorder-vs-bundled.md`](worked-example-exectxresult-notorder-vs-bundled.md)（不变量 707 item 1）；[`worked-example-exectxresult-notexcluded-vs-bundled.md`](worked-example-exectxresult-notexcluded-vs-bundled.md)（不变量 708 item 2）。

## 本页不抄

- 怎样编回执、怎样建索引、怎样算 LastResultsHash。
- 怎样写四门。那是不变量 33。
- CheckTxResponse 的 Data / Priority。那是另一对象。
