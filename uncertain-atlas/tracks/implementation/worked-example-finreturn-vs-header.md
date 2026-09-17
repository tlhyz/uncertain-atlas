# 例：看见 Application calculates and returns AppHash along with tx outputs 不是已经印进本头；看见 CometBFT hashes transaction outputs into ResultHash 不是已经 Code / Data 印进本头 LastResultsHash；看见 CometBFT persists tx outputs / AppHash / ResultsHash 不是已经交差 / 已经 Commit 落盘应用状态

**层次**：实现 / FinalizeBlock When AppHash tx outputs ResultHash persist 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When steps 4–6。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。mempool 只在 CheckTx 弱过滤器那页已有边界时对照，本页不另写 mempool 正文。本页是「Application calculates and returns AppHash along with tx outputs 不是已经印进本头 / CometBFT hashes transaction outputs into ResultHash 不是已经 Code Data 印进本头 / CometBFT persists tx outputs AppHash ResultsHash 不是已经交差 / 已经 Commit 落盘应用状态」，不是 Finalize 何时调用 bundled 三事，也不是 Finalize 之后 bundled 三事，也不是 Finalize 回包 app_hash 可以空或硬编码 bundled 三事。不要另写怎样算 AppHash、怎样算 ResultHash、怎样落盘这三份。

## 官方三件事

规范把 When 第 4 步 Application calculates and returns AppHash along with tx outputs、第 5 步 CometBFT hashes transaction outputs into ResultHash、第 6 步 CometBFT persists tx outputs / AppHash / ResultsHash 写成三件独立的实现事，不是「看见回了 AppHash 和各笔输出就已经印进本头、已经交差、已经 Commit 落盘应用状态」一件事：

1. **看见 Application calculates and returns the AppHash, along with a list containing the outputs of each of the transactions executed / 看见应用回 AppHash 和各笔 tx outputs 不是已经印进本头，也不是已经是本头 AppHash。**  
   官方 When 第 4 步写：Application calculates and returns the _AppHash_, along with a list containing the outputs of each of the transactions executed。看见 calculates and returns，不是已经 executes block _v_ 那种已经执行完（466）。看见回了 AppHash 和各笔输出，不是已经印进本头。Usage 写：`FinalizeBlockResponse.app_hash` is included as the `Header.AppHash` in the **next** block。看见回了 app_hash，不是已经是**本**头 AppHash（147）。看见 tx outputs 列表，不是已经 Finalize 回包 app_hash 可以空或硬编码（404）就已经是同一句 interchangeable。
2. **看见 CometBFT hashes all the transaction outputs and stores it in ResultHash / 看见引擎把各笔输出哈希进 ResultHash 不是已经 Code / Data 印进本头 LastResultsHash，也不是已经印进本头。**  
   官方 When 第 5 步写：CometBFT hashes all the transaction outputs and stores it in _ResultHash_。看见 hashes into ResultHash，不是已经 Application returns tx outputs 那种已经交差 interchangeable。Req 写：`Code` / `Data` 必须确定，编进结构再哈希进下一高度块头的 `LastResultsHash`。看见 ResultHash，不是已经 Code / Data 印进本头（316）就已经是同一句 interchangeable。看见引擎哈希了，不是已经印进本头。
3. **看见 CometBFT persists the transaction outputs, AppHash, and ResultsHash / 看见引擎落盘 tx outputs / AppHash / ResultsHash 不是已经交差，也不是已经 Commit 落盘应用状态。**  
   官方 When 第 6 步写：CometBFT persists the transaction outputs, _AppHash_, and _ResultsHash_。看见 persists 这三份，不是已经 Finalize 改了就已经落盘（335）那种应用在 Finalize 里落盘 interchangeable。看见引擎落了这三份，不是已经应用在 `Commit` 里落盘应用状态。看见 When 第 6 步，不是已经 Finalize 之后 bundled（403）那种落完就锁内存池 / 已经交差 interchangeable。

怎样算 AppHash、怎样算 ResultHash、怎样落盘这三份、怎样 Commit 是规范里的做法，本页不抄。Finalize 何时调用 bundled（362）是 +2/3 precommit / persist decision / 应用回了 AppHash 引擎哈希进 ResultHash 那套另一切片，Finalize 之后（403）是落完锁内存池 / Commit / Recheck 那套另一切片，Finalize 回包 app_hash 可以空或硬编码（404）是 next block Header.AppHash / Query 证明锚那套另一切片，ExecTxResult 回执 bundled（316）是 Code 非零仍可能在块里 / Code Data 印进本头那套另一切片，本页不抄。

## 官方为什么这样拆

- **Application returns AppHash + tx outputs ≠ 已经印进本头 / 已经是本头 AppHash：** 官方把 calculates and returns 和 next block Header.AppHash 分开。
- **CometBFT hashes tx outputs into ResultHash ≠ 已经 Code / Data 印进本头 LastResultsHash：** 官方把 ResultHash 和 tx_results Code / Data 编进 LastResultsHash 分开。
- **CometBFT persists tx outputs / AppHash / ResultsHash ≠ 已经交差 / 已经 Commit 落盘应用状态：** 官方把引擎 persist 这三份和应用 Commit 落盘分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Application returns AppHash + tx outputs | 不是已经印进本头 | 不是本头 AppHash 就已经是本高度交差（147） |
| CometBFT hashes tx outputs into ResultHash | 不是已经 Code / Data 印进本头 | 不是 ExecTxResult 回执 bundled（316） |
| CometBFT persists tx outputs / AppHash / ResultsHash | 不是已经 Commit 落盘应用状态 | 不是 Finalize 之后 bundled（403） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见回了 AppHash 和各笔输出就已经印进本头、已经交差、已经 Commit 落盘应用状态」，必须分开 Application returns AppHash + tx outputs 是不是已经印进本头、CometBFT hashes into ResultHash 是不是已经 Code / Data 印进本头、CometBFT persists 这三份是不是已经 Commit 落盘应用状态。可以跳过「看见回了 AppHash 就已经印进本头」。不要另写怎样算 AppHash。

## 本页不抄

- 怎样算 AppHash、怎样算 ResultHash、怎样落盘这三份、怎样 Commit。
- Finalize 何时调用 bundled 三事。那是不变量 362。
- Finalize 之后。那是不变量 403。
- Finalize 回包 app_hash 可以空或硬编码。那是不变量 404。
- ExecTxResult 回执 bundled。那是不变量 316。
- Finalize 改了就已经落盘。那是不变量 335。
- Application executes block v。那是不变量 466。
