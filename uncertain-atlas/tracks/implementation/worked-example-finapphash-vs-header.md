# 例：看见 Finalize 回包 app_hash 可以空或硬编码、但必须确定不是已经印进本头；看见以后 Query 可以拿这份根当锚回证明不是已经对上 AppHash；看见 tx_results[i].Code == 0 只表示第 i 笔完全合法不是已经没进块

**层次**：实现 / Finalize 回包余量。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「Finalize 回包 app_hash 可以空或硬编码、但必须确定不是已经印进本头 / 以后 Query 可以拿这份根当锚回证明不是已经对上 AppHash / tx_results[i].Code == 0 只表示第 i 笔完全合法不是已经没进块」，不是本头 AppHash 就已经是本高度交差，也不是 Code 非零就已经没进块。不要另写怎样写 Finalize 回包余量。

## 官方三件事

规范把 Finalize 回包 `app_hash` 可以空或硬编码、但必须确定、以后 Query 可以拿这份根当锚回证明、`tx_results[i].Code == 0` 只表示第 i 笔完全合法写成三件独立的实现事，不是「看见回了 Finalize 回包余量就已经印进本头、已经对上 AppHash、已经没进块」一件事：

1. **看见 Finalize 回包 `app_hash` 可以空或硬编码、但必须确定 / 看见回了 app_hash 不是已经印进本头，也不是已经交差。**  
   官方写：`FinalizeBlockResponse.app_hash` 可以空，也可以硬编码，但必须确定——不得依赖这次请求和上一份已提交状态以外的东西。看见回了空根，不是已经印进本头。看见硬编码，不是已经是本头 AppHash。看见必须确定，不是已经交差。
2. **看见以后 Query 可以拿这份根当锚回证明 / 看见能回证明 不是已经对上 AppHash，也不是已经是按键查。**  
   官方写：以后叫 `Query`，可以回以这份默克尔根为锚的应用状态证明。看见能回证明，不是已经对上这一高 AppHash。看见有锚，不是已经是 `ProofOp` 那份按键查。看见能查，不是已经交差。
3. **看见 `tx_results[i].Code == 0` 只表示第 i 笔完全合法 / 看见回了 0 不是已经没进块，也不是已经印进本头。**  
   官方写：`FinalizeBlockResponse.tx_results[i].Code == 0` 只表示第 i 笔完全合法。看见回了 0，不是已经 Code 非零那种没进块。看见这笔合法，不是已经 Code / Data 印进本头。看见能回，不是已经交差。

怎样写 Finalize 回包余量、怎样挑空根、怎样回证明是规范里的做法，本页不抄。本头 AppHash 就已经是本高度交差是不变量 147，本页不抄。

## 官方为什么这样拆

- **Finalize 回包 app_hash 可以空或硬编码、但必须确定 ≠ 已经印进本头：** 官方把可以空或硬编码和已经印进本头分开。
- **以后 Query 可以拿这份根当锚回证明 ≠ 已经对上 AppHash：** 官方把能回证明和已经对上分开。
- **tx_results[i].Code == 0 只表示第 i 笔完全合法 ≠ 已经没进块：** 官方把这笔完全合法和 Code 非零就已经没进块分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Finalize 回包 app_hash 可以空或硬编码、但必须确定 | 不是已经印进本头 | 不是本头 AppHash 就已经是本高度交差（147） |
| 以后 Query 可以拿这份根当锚回证明 | 不是已经对上 AppHash | 不是 ProofOp.type 就已经是按键查（325） |
| tx_results[i].Code == 0 只表示第 i 笔完全合法 | 不是已经没进块 | 不是 Code 非零就已经没进块（316） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见回了 Finalize 回包余量就已经印进本头、已经对上 AppHash、已经没进块」，必须分开 Finalize 回包 app_hash 可以空或硬编码、但必须确定是不是已经印进本头、以后 Query 可以拿这份根当锚回证明是不是已经对上 AppHash、tx_results[i].Code == 0 只表示第 i 笔完全合法是不是已经没进块。可以跳过「看见回了 Finalize 回包余量就已经印进本头」。不要另写怎样写 Finalize 回包余量。

## 本页不抄

- 怎样写 Finalize 回包余量、怎样挑空根、怎样回证明。
- 本头 AppHash 就已经是本高度交差。那是不变量 147。
- ProofOp.type 就已经是按键查。那是不变量 325。
- Code 非零就已经没进块。那是不变量 316。
