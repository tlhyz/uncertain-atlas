# 例：看见 ExecTxResult.gas_wanted 是这笔要的气不是已经是 CheckTx 的 GasWanted；看见 ExecTxResult.gas_used 是这笔用掉的气不是已经算进共识；看见 ExecTxResult.codespace 是码的命名空间不是已经是 CheckTx 码空间

**层次**：实现 / ExecTxResult 气。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExecTxResult。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「ExecTxResult.gas_wanted 是这笔要的气不是已经是 CheckTx 的 GasWanted / ExecTxResult.gas_used 是这笔用掉的气不是已经算进共识 / ExecTxResult.codespace 是码的命名空间不是已经是 CheckTx 码空间」，不是 MaxGas 就已经在执行，也不是 Code / Data 就已经印进本头。不要另写怎样写 ExecTxResult 气。

## 官方三件事

规范把 ExecTxResult `gas_wanted` 是这笔要的气、`gas_used` 是这笔用掉的气、`codespace` 是码的命名空间写成三件独立的实现事，不是「看见填了 ExecTxResult 气就已经是 CheckTx 的 GasWanted、已经算进共识、已经是 CheckTx 码空间」一件事：

1. **看见 ExecTxResult `gas_wanted` 是这笔要的气 / 看见填了 gas_wanted 不是已经是 CheckTx 的 GasWanted，也不是已经在执行。**  
   官方写：`gas_wanted` 是这笔交易要的气。看见填了 gas_wanted，不是已经是 CheckTx 回包那份 GasWanted。看见有要的气，不是已经是 MaxGas 那种已经在执行。看见能填，不是已经交差。
2. **看见 ExecTxResult `gas_used` 是这笔用掉的气 / 看见填了 gas_used 不是已经算进共识，也不是已经印进本头。**  
   官方写：`gas_used` 是这笔交易用掉的气。看见填了 gas_used，不是已经是 CheckTx 那份 GasUsed 已经被引擎算进共识。看见有用掉的气，不是已经是 Code / Data 印进本头。看见能回，不是已经交差。
3. **看见 ExecTxResult `codespace` 是码的命名空间 / 看见写了空间 不是已经是 CheckTx 码空间，也不是已经是回包码。**  
   官方写：`codespace` 是这个 `code` 的命名空间。看见写了空间，不是已经是 CheckTx 回包那份码空间。看见有命名空间，不是已经是回包码本身。看见能回，不是已经交差。

怎样写 ExecTxResult 气、怎样填要的气、怎样填用掉的气是规范里的做法，本页不抄。MaxGas 就已经在执行是不变量 315，本页不抄。

## 官方为什么这样拆

- **ExecTxResult.gas_wanted 是这笔要的气 ≠ 已经是 CheckTx 的 GasWanted：** 官方把 Finalize 回执里要的气和 CheckTx 那份 GasWanted 分开。
- **ExecTxResult.gas_used 是这笔用掉的气 ≠ 已经算进共识：** 官方把 Finalize 回执里用掉的气和引擎已经按气验过分开。
- **ExecTxResult.codespace 是码的命名空间 ≠ 已经是 CheckTx 码空间：** 官方把 Finalize 这份码空间和 CheckTx 那份码空间分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ExecTxResult.gas_wanted 是这笔要的气 | 不是已经是 CheckTx 的 GasWanted | 不是 MaxGas 就已经在执行（315） |
| ExecTxResult.gas_used 是这笔用掉的气 | 不是已经算进共识 | 不是 Code / Data 就已经印进本头（316） |
| ExecTxResult.codespace 是码的命名空间 | 不是已经是 CheckTx 码空间 | 不是 CheckTx 回包 codespace 就已经是回包码（381） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 ExecTxResult 气就已经是 CheckTx 的 GasWanted、已经算进共识、已经是 CheckTx 码空间」，必须分开 ExecTxResult.gas_wanted 是这笔要的气是不是已经是 CheckTx 的 GasWanted、ExecTxResult.gas_used 是这笔用掉的气是不是已经算进共识、ExecTxResult.codespace 是码的命名空间是不是已经是 CheckTx 码空间。可以跳过「看见填了 ExecTxResult 气就已经是 CheckTx 的 GasWanted」。不要另写怎样写 ExecTxResult 气。

## 本页不抄

- 怎样写 ExecTxResult 气、怎样填要的气、怎样填用掉的气。
- MaxGas 就已经在执行。那是不变量 315。
- Code / Data 就已经印进本头。那是不变量 316。
- CheckTx 回包 codespace 就已经是回包码。那是不变量 381。
