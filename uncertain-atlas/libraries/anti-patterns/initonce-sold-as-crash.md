# 反模式：看见 InitChain 创世时只调一次就当成已经是崩溃后再调 / 看见应用可以决定接受创世验证者集合或用创世应用信息算出另一套就当成已经没有集合 / 看见 Request 和 Response 的 Validators 都是 ValidatorUpdate、技术上是从空集合更新就当成已经改了集合

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Usage。  
**例**：[InitChain 创世时只调一次 ≠ 已经是崩溃后再调](../../tracks/implementation/worked-example-initonce-vs-crash.md)。

## 塌法

1. 看见 InitChain 创世时只调一次 / 看见调了一次，就当成已经是崩溃后再调，或当成已经交差。
2. 看见应用可以决定接受创世验证者集合或用创世应用信息算出另一套 / 看见能决定，就当成已经没有集合，或当成已经改了集合。
3. 看见 Request 和 Response 的 Validators 都是 ValidatorUpdate、技术上是从空集合更新 / 看见两边都是 ValidatorUpdate，就当成已经改了集合，或当成已经带了公钥。

## 为什么会出事

官方写：Called once upon genesis。The application can decide to accept the initial validator set or use a different one, potentially computed based on the initial application state. Both the Request and Response include a type Validators, which is a list of ValidatorUpdate types. Technically, this is updating the validator set from the empty set. 看见填了栏，不是已经是崩溃后再调，也不是已经没有集合，也不是已经改了集合。

## 和相邻反模式

- [initchainusage-sold-as-bundled](initchainusage-sold-as-bundled.md) 是 InitChain Usage 正式三事就等于崩溃后再调 / 空名单 / bundled，不是本页 InitChain Usage 余量 bundled 三事。
- [crashsteps-sold-as-committed](crashsteps-sold-as-committed.md) 是崩溃后第一块 Commit 之前再调 InitChain 就已经交差，不是本页这种 InitChain 创世时只调一次不是已经是崩溃后再调。
- [validatorupdate-sold-as-set](validatorupdate-sold-as-set.md) 是 InitChain 回了空名单就已经没有集合，不是本页这种应用可以决定接受创世验证者集合或用创世应用信息算出另一套不是已经没有集合。
- [validator-sold-as-update](validator-sold-as-update.md) 是 ValidatorUpdate 用公钥认人就已经改了集合，不是本页这种 Request 和 Response 的 Validators 都是 ValidatorUpdate、技术上是从空集合更新不是已经改了集合。
