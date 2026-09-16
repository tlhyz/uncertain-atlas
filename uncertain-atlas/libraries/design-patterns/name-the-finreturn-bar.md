# 模式：把 FinalizeBlock When AppHash tx outputs ResultHash persist 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When steps 4–6。  
**例**：[Application returns AppHash + tx outputs ≠ 已经印进本头](../../tracks/implementation/worked-example-finreturn-vs-header.md)。

## 三个名字

1. **Application returns AppHash + tx outputs 不是已经印进本头：** 看见 calculates and returns 不是已经是本头 AppHash。
2. **CometBFT hashes tx outputs into ResultHash 不是已经 Code / Data 印进本头：** 看见 ResultHash 不是已经 LastResultsHash interchangeable。
3. **CometBFT persists tx outputs / AppHash / ResultsHash 不是已经 Commit 落盘应用状态：** 看见 persists 这三份不是已经交差。

## 为什么要分开叫

官方把 When 第 4 步 Application returns AppHash + tx outputs、第 5 步 hashes into ResultHash、第 6 步 persists 这三份写成三个名字。把它们叫成一个「看见回了 AppHash 和各笔输出就已经印进本头」，会把 next block Header.AppHash、ResultHash 和引擎 persist 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见回了 AppHash 就已经印进本头」，先数清问的是 Application returns AppHash + tx outputs 是不是已经印进本头、CometBFT hashes into ResultHash 是不是已经 Code / Data 印进本头，还是 CometBFT persists 这三份是不是已经 Commit 落盘应用状态，再决定要不要同一次发布。
