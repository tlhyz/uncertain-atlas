# 例：看见 FinalizeBlockResponse.events 是给索引用的类型键值事件不是已经印进本头；看见 FinalizeBlockResponse.tx_results 是执行这块各笔交易得到的结果列表不是已经是 CheckTx 回包；看见 FinalizeBlockResponse.validator_updates 是对验证者集合的改动不是已经在 H+1 换人

**层次**：实现 / Finalize 回包栏。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Response / Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「FinalizeBlockResponse.events 是给索引用的类型键值事件不是已经印进本头 / FinalizeBlockResponse.tx_results 是执行这块各笔交易得到的结果列表不是已经是 CheckTx 回包 / FinalizeBlockResponse.validator_updates 是对验证者集合的改动不是已经在 H+1 换人」，不是 Prepare 里产出了事件就已经交给引擎，也不是 Code / Data 就已经印进本头，也不是 ValidatorUpdate 用公钥认人就已经改了集合。不要另写怎样写 Finalize 回包栏。

## 官方三件事

规范把 FinalizeBlock Response 表上 `events` 是给索引用的类型键值事件、`tx_results` 是执行这块各笔交易得到的结果列表、`validator_updates` 是对验证者集合的改动写成三件独立的实现事，不是「看见回了 Finalize 回包栏就已经印进本头、已经是 CheckTx 回包、已经在 H+1 换人」一件事：

1. **看见 `FinalizeBlockResponse.events` 是给索引用的类型键值事件 / 看见回了 events 不是已经印进本头，也不是已经像 Code/Data 那样必须确定。**  
   官方写：`events` 是 Type & Key-Value events for indexing。Deterministic 列是 No。看见回了 events，不是已经 Prepare 里产出了块事件或交易事件那种已经交给引擎。看见能指索引，不是已经 Code / Data 编进下一高度块头的 `LastResultsHash` 那种已经印进本头。看见标成非确定，不是已经 Finalize 算出的状态必须只依赖上一份状态和决定块那种必须确定。
2. **看见 `FinalizeBlockResponse.tx_results` 是执行这块各笔交易得到的结果列表 / 看见回了 tx_results 不是已经是 CheckTx 回包，也不是已经同一顺序就是已经印进 LastResultsHash。**  
   官方写：`tx_results` 是 List of structures containing the data resulting from executing the transactions。Deterministic 列是 Yes。Usage 也写：应用必须提供 `tx_results` 作为执行这块的结果。看见回了列表，不是已经 CheckTx 回包 `Code` / `Data` / `Priority` 那种已经是 CheckTx 回包。看见有执行结果，不是已经结果列表和送来的交易同一顺序那种已经印进 LastResultsHash。看见 Deterministic 是 Yes，不是已经 `Info` / `Log` 标成非确定那种只是记日志。
3. **看见 `FinalizeBlockResponse.validator_updates` 是对验证者集合的改动 / 看见回了 validator_updates 不是已经在 H+1 换人，也不是已经是 ValidatorUpdate 用公钥认人就已经改了集合。**  
   官方写：`validator_updates` 是 Changes to validator set (set voting power to 0 to remove)。Deterministic 列是 Yes。Usage 也写：块 H 触发的 `validator_updates` 影响 H+1、H+2、H+3 的验证。看见回了更新，不是已经高度 H 的更新已经在 H+1 计票那种已经在 H+1 换人。看见有 ValidatorUpdate，不是已经 `Validator` 用 address 认人那种已经改了集合。看见能指下一份集合，不是已经必须回四列那种已经交差。

怎样写 Finalize 回包栏、怎样编 events、怎样编 ValidatorUpdate 是规范里的做法，本页不抄。Prepare 里产出了事件就已经交给引擎是不变量 357，本页不抄。

## 官方为什么这样拆

- **FinalizeBlockResponse.events 是给索引用的类型键值事件 ≠ 已经印进本头：** 官方把索引事件和 Code/Data 进 LastResultsHash、Prepare 先跑事件分开。
- **FinalizeBlockResponse.tx_results 是执行这块各笔交易得到的结果列表 ≠ 已经是 CheckTx 回包：** 官方把 Finalize 执行结果列表和 CheckTx 回包、只谈顺序就印进头分开。
- **FinalizeBlockResponse.validator_updates 是对验证者集合的改动 ≠ 已经在 H+1 换人：** 官方把 H→H+1/H+2/H+3 的延迟和 Validator 类型、必须回四列分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| FinalizeBlockResponse.events 是给索引用的类型键值事件 | 不是已经印进本头 | 不是 Prepare 里产出了事件就已经交给引擎（357） |
| FinalizeBlockResponse.tx_results 是执行这块各笔交易得到的结果列表 | 不是已经是 CheckTx 回包 | 不是 Code / Data 就已经印进本头（316） |
| FinalizeBlockResponse.validator_updates 是对验证者集合的改动 | 不是已经在 H+1 换人 | 不是高度 H 的 validator_updates 已经在 H+1 计票（35） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见回了 Finalize 回包栏就已经印进本头、已经是 CheckTx 回包、已经在 H+1 换人」，必须分开 FinalizeBlockResponse.events 是给索引用的类型键值事件是不是已经印进本头、FinalizeBlockResponse.tx_results 是执行这块各笔交易得到的结果列表是不是已经是 CheckTx 回包、FinalizeBlockResponse.validator_updates 是对验证者集合的改动是不是已经在 H+1 换人。可以跳过「看见回了 Finalize 回包栏就已经印进本头」。不要另写怎样写 Finalize 回包栏。431 finrespbar vs header bundled unbundling 完成（1070 item 1 / 1071 item 2 / 1072 item 3）；精读 [`worked-example-finbar-notheader-vs-bundled.md`](worked-example-finbar-notheader-vs-bundled.md)（不变量 1070 item 1）。

## 本页不抄

- 怎样写 Finalize 回包栏、怎样编 events、怎样编 ValidatorUpdate。
- Prepare 里产出了事件就已经交给引擎。那是不变量 357。
- Code / Data 就已经印进本头。那是不变量 316。
- 高度 H 的 validator_updates 已经在 H+1 计票。那是不变量 35。
