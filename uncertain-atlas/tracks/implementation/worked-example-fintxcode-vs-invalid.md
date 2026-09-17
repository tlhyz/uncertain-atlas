# 例：看见 FinalizeBlockResponse.tx_results[i].Code == 0 只表示第 i 笔完全合法不是已经 CheckTx 过了；看见 Code == 0 only if fully valid 不是已经 Code != 0 那种没进块；看见回了 tx_results 不是已经 Finalize 改了就已经交差，也不是已经 Code / Data 印进本头

**层次**：实现 / FinalizeBlock tx_results Code==0 完全合法正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage；[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Transaction Results。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。mempool 只在 CheckTx 弱过滤器那页已有边界时对照，本页不另写 mempool 正文。本页是「tx_results[i].Code == 0 只表示第 i 笔完全合法不是已经 CheckTx 过了 / Code == 0 only if fully valid 不是已经 Code != 0 那种没进块 / 回了 tx_results 不是已经 Finalize 改了就已经交差」，不是 Finalize 回包余量 bundled 三事，也不是 ExecTxResult 回执 bundled 三事，也不是 Finalize 落盘禁令那套。不要另写怎样编回执、怎样建索引。

## 官方三件事

规范把 `tx_results[i].Code == 0` only if fully valid、Code 非零仍可能在块里、Finalize 回包 tx_results 和交差 / 印进本头分开写成三件独立的实现事，不是「看见 Finalize 回了 tx_results 就已经 CheckTx 过了、已经没进块、已经交差」一件事：

1. **看见 `FinalizeBlockResponse.tx_results[i].Code == 0` only if the i-th transaction is fully valid / 看见回了 0 不是已经 CheckTx 过了，也不是已经 Process 回了 Accept。**  
   官方写：`FinalizeBlockResponse.tx_results[i].Code == 0` only if the _i_-th transaction is fully valid。看见 only if fully valid，不是已经 CheckTx 弱过滤器（339）那种过了池门就已经验完。看见回了 0，不是已经 Process 回了 Accept（347）就已经是同一句 interchangeable。看见这笔合法，不是已经四门已经结算（33）。
2. **看见 Code == 0 only if fully valid / 看见这笔完全合法 不是已经 Code ≠ 0 那种没进块，也不是已经无效就不建索引那种已经不在块里。**  
   官方 Usage 写 only if fully valid。Req 写：若 `Code ≠ 0`，这笔会被标成无效，但仍在块里。无效交易不建索引。看见 Code 非零，不是已经没进块（316）。看见 fully valid，不是已经 Code ≠ 0 就已经不在块里 interchangeable。看见 0，不是已经没索引就等于没进块。
3. **看见回了 `tx_results` / 看见有 Code 不是已经 Finalize 改了就已经交差，也不是已经 Code / Data 印进本头 LastResultsHash。**  
   官方写：`Code == 0` 只表示这笔完全合法。Req 另写：`Code` / `Data` 必须确定，编进结构再哈希进下一高度块头的 `LastResultsHash`。看见回了合法，不是已经 Finalize 改了就已经落盘（335）。看见有 Code，不是已经 Code / Data 印进本头就等于已经交差 interchangeable。看见 tx_results，不是已经 Finalize 回包 app_hash 可以空或硬编码（404）就已经是同一句 interchangeable。

怎样编回执、怎样建索引、怎样算 LastResultsHash 是规范里的做法，本页不抄。Finalize 回包余量 bundled（404）是 app_hash 可以空或硬编码 / Query 证明锚 / Code==0 那套另一切片，ExecTxResult 回执 bundled（316）是列表顺序 / Code 非零仍可能在块里 / Code Data 印进本头那套另一切片，Finalize 落盘禁令（335）是 Finalize 改了不是已经落盘那套另一切片，本页不抄。

## 官方为什么这样拆

- **Code == 0 only if fully valid ≠ 已经 CheckTx 过了 / 已经 Process Accept：** 官方把 Finalize 这笔完全合法和池门 / Process Accept 分开。
- **Code == 0 only if fully valid ≠ 已经 Code != 0 那种没进块：** 官方把 fully valid 语义和 Code 非零仍可能在块里分开。
- **回了 tx_results ≠ 已经 Finalize 改了就已经交差 / 已经 Code Data 印进本头：** 官方把这笔合法和落盘 / 印进本头分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Code == 0 only if fully valid | 不是已经 CheckTx 过了 | 不是 CheckTx 弱过滤器（339） |
| Code == 0 only if fully valid | 不是已经 Code != 0 那种没进块 | 不是 ExecTxResult 回执 bundled（316） |
| 回了 tx_results | 不是已经 Finalize 改了就已经交差 | 不是 Finalize 落盘禁令（335） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Finalize 回了 tx_results 就已经 CheckTx 过了、已经没进块、已经交差」，必须分开 Code == 0 only if fully valid 是不是已经 CheckTx 过了、是不是已经 Code != 0 那种没进块、回了 tx_results 是不是已经 Finalize 改了就已经交差。可以跳过「看见回了 0 就已经没进块」。不要另写怎样编回执。

## 本页不抄

- 怎样编回执、怎样建索引、怎样算 LastResultsHash。
- Finalize 回包余量 bundled 三事。那是不变量 404。
- ExecTxResult 回执 bundled 三事。那是不变量 316。
- Finalize 落盘禁令。那是不变量 335。
- CheckTx 弱过滤器。那是不变量 339。
- 本头 AppHash 就已经是本高度交差。那是不变量 147。
