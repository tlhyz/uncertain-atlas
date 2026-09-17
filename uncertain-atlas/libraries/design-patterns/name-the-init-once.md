# 模式：把 InitChain Usage 余量三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Usage。  
**例**：[InitChain 创世时只调一次 ≠ 已经是崩溃后再调](../../tracks/implementation/worked-example-initonce-vs-crash.md)。

## 三个名字

1. **InitChain 创世时只调一次不是已经是崩溃后再调：** 看见调了一次 不是已经交差。
2. **应用可以决定接受创世验证者集合或用创世应用信息算出另一套不是已经没有集合：** 看见能决定 不是已经改了集合。
3. **Request 和 Response 的 Validators 都是 ValidatorUpdate、技术上是从空集合更新不是已经改了集合：** 看见两边都是 ValidatorUpdate 不是已经带了公钥。

## 为什么要分开叫

官方把创世时只调一次、应用可以决定接受创世验证者集合或用创世应用信息算出另一套、Request 和 Response 的 Validators 都是 ValidatorUpdate、技术上是从空集合更新写成三件事。把它们叫成一个「看见填了 InitChain Usage 余量就已经是崩溃后再调」，会把已经是崩溃后再调、已经没有集合和已经改了集合一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 InitChain Usage 余量就已经是崩溃后再调」，先数清问的是 InitChain 创世时只调一次不是已经是崩溃后再调、应用可以决定接受创世验证者集合或用创世应用信息算出另一套不是已经没有集合，还是 Request 和 Response 的 Validators 都是 ValidatorUpdate、技术上是从空集合更新不是已经改了集合，再决定要不要同一次发布。
