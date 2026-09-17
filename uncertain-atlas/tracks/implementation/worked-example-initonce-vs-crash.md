# 例：看见 InitChain 创世时只调一次不是已经是崩溃后再调；看见应用可以决定接受创世验证者集合或用创世应用信息算出另一套不是已经没有集合；看见 Request 和 Response 的 Validators 都是 ValidatorUpdate、技术上是从空集合更新不是已经改了集合

**层次**：实现 / InitChain Usage 余量。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「InitChain 创世时只调一次不是已经是崩溃后再调 / 应用可以决定接受创世验证者集合或用创世应用信息算出另一套不是已经没有集合 / Request 和 Response 的 Validators 都是 ValidatorUpdate、技术上是从空集合更新不是已经改了集合」，不是 InitChain 回了空名单就已经没有集合，也不是崩溃后第一块 Commit 之前再调 InitChain 就已经交差。不要另写怎样写 InitChain Usage 余量。

## 官方三件事

规范把 InitChain 创世时只调一次、应用可以决定接受创世验证者集合或用创世应用信息算出另一套、Request 和 Response 的 Validators 都是 ValidatorUpdate、技术上是从空集合更新写成三件独立的实现事，不是「看见填了 InitChain Usage 余量就已经是崩溃后再调、已经没有集合、已经改了集合」一件事：

1. **看见 InitChain 创世时只调一次 / 看见调了一次 不是已经是崩溃后再调，也不是已经交差。**  
   官方写：Called once upon genesis。看见创世时只调一次，不是已经第一块 Commit 之前崩了、`InitChain` 会再叫一次那种已经交差。看见调了一次，不是已经能跳步。看见有创世调用，不是已经过了 genesis_time。
2. **看见应用可以决定接受创世验证者集合或用创世应用信息算出另一套 / 看见能决定 不是已经没有集合，也不是已经改了集合。**  
   官方写：The application can decide to accept the initial validator set or use a different one, potentially computed based on the initial application state. 看见能决定，不是已经 `InitChain` 回了空名单那种已经没有集合。看见能算另一套，不是已经用了创世文件里的验证者。看见有创世应用信息，不是已经验过应用状态。
3. **看见 Request 和 Response 的 Validators 都是 ValidatorUpdate、技术上是从空集合更新 / 看见两边都是 ValidatorUpdate 不是已经改了集合，也不是已经带了公钥。**  
   官方写：Both the Request and Response include a type Validators, which is a list of ValidatorUpdate types. Technically, this is updating the validator set from the empty set. 看见两边都是 ValidatorUpdate，不是已经 `ValidatorUpdate` 用公钥认人那种已经改了集合。看见技术上是从空集合更新，不是已经没有集合。看见有更新结构，不是已经交差。

怎样写 InitChain Usage 余量、怎样决定接受创世集合、怎样从空集合更新是规范里的做法，本页不抄。InitChain 回了空名单就已经没有集合是不变量 318，本页不抄。

## 官方为什么这样拆

- **InitChain 创世时只调一次 ≠ 已经是崩溃后再调：** 官方把创世时只调一次和崩溃后第一块 Commit 之前再调分开。
- **应用可以决定接受创世验证者集合或用创世应用信息算出另一套 ≠ 已经没有集合：** 官方把应用自己决定用哪一套和回了空名单就已经没有集合分开。
- **Request 和 Response 的 Validators 都是 ValidatorUpdate、技术上是从空集合更新 ≠ 已经改了集合：** 官方把两边都是 ValidatorUpdate、技术上从空集合更新和已经改了集合分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| InitChain 创世时只调一次 | 不是已经是崩溃后再调 | 不是崩溃后第一块 Commit 之前再调 InitChain 就已经交差（320） |
| 应用可以决定接受创世验证者集合或用创世应用信息算出另一套 | 不是已经没有集合 | 不是 InitChain 回了空名单就已经没有集合（318） |
| Request 和 Response 的 Validators 都是 ValidatorUpdate、技术上是从空集合更新 | 不是已经改了集合 | 不是 ValidatorUpdate 用公钥认人就已经改了集合（364） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 InitChain Usage 余量就已经是崩溃后再调、已经没有集合、已经改了集合」，必须分开 InitChain 创世时只调一次是不是已经是崩溃后再调、应用可以决定接受创世验证者集合或用创世应用信息算出另一套是不是已经没有集合、Request 和 Response 的 Validators 都是 ValidatorUpdate、技术上是从空集合更新是不是已经改了集合。可以跳过「看见填了 InitChain Usage 余量就已经是崩溃后再调」。不要另写怎样写 InitChain Usage 余量。

## 本页不抄

- 怎样写 InitChain Usage 余量、怎样决定接受创世集合、怎样从空集合更新。
- 崩溃后第一块 Commit 之前再调 InitChain 就已经交差。那是不变量 320。
- InitChain 回了空名单就已经没有集合。那是不变量 318。
- ValidatorUpdate 用公钥认人就已经改了集合。那是不变量 364。
