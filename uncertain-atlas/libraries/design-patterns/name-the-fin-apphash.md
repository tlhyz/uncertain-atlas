# 模式：把 Finalize 回包余量三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[Finalize 回包 app_hash 可以空或硬编码、但必须确定 ≠ 已经印进本头](../../tracks/implementation/worked-example-finapphash-vs-header.md)。

## 三个名字

1. **Finalize 回包 app_hash 可以空或硬编码、但必须确定不是已经印进本头：** 看见回了 app_hash 不是已经交差。
2. **以后 Query 可以拿这份根当锚回证明不是已经对上 AppHash：** 看见能回证明不是已经是按键查。
3. **tx_results[i].Code == 0 只表示第 i 笔完全合法不是已经没进块：** 看见回了 0 不是已经印进本头。

## 为什么要分开叫

官方把 Finalize 回包 `app_hash` 可以空或硬编码、但必须确定、以后 Query 可以拿这份根当锚回证明、`tx_results[i].Code == 0` 只表示第 i 笔完全合法写成三件事。把它们叫成一个「看见回了 Finalize 回包余量就已经印进本头」，会把本头 AppHash、按键查和 Code 非零就已经没进块一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见回了 Finalize 回包余量就已经印进本头」，先数清问的是 Finalize 回包 app_hash 可以空或硬编码、但必须确定不是已经印进本头、以后 Query 可以拿这份根当锚回证明不是已经对上 AppHash，还是 tx_results[i].Code == 0 只表示第 i 笔完全合法不是已经没进块，再决定要不要同一次发布。
