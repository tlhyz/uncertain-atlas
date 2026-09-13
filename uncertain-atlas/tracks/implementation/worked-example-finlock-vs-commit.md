# 例：看见 CometBFT locks the mempool / no CheckTx on new transactions 不是已经是 Commit 锁；看见 CometBFT calls Commit to persist application state 不是已经引擎 persist tx outputs / AppHash / ResultsHash；看见 optionally recheck mempool / unlock / start h+1 round 0 不是已经是 Recheck

**层次**：实现 / FinalizeBlock When lock mempool Commit recheck 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When steps 7–11。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。mempool 只在 CheckTx 弱过滤器 / RECHECK 那页已有边界时对照，本页不另写 mempool 正文。本页是「locks mempool / no CheckTx on new transactions 不是已经是 Commit 锁 / calls Commit to persist application state 不是已经引擎 persist 这三份 / optionally recheck / unlock / start h+1 round 0 不是已经是 Recheck」，不是 Finalize 之后 bundled 三事，也不是 CometBFT persists tx outputs / AppHash / ResultsHash bundled 三事，也不是 Commit 不带参数 bundled 三事。不要另写怎样写 Finalize When 流程、怎样再验池里剩下的。

## 官方三件事

规范把 When 第 7 步 locks the mempool — no CheckTx on new transactions、第 8 步 calls Commit to persist application state、第 9–11 步 optionally recheck / unlock / start h+1 round 0 写成三件独立的实现事，不是「看见 Finalize 之后就已经锁池、已经 Commit 落盘、已经 Recheck、已经交差」一件事：

1. **看见 CometBFT locks the mempool — no calls to `CheckTx` on new transactions / 看见锁了内存池、新交易不进 CheckTx 不是已经是 Commit 锁，也不是已经 RPC 安全默认锁。**  
   官方 When 第 7 步写：CometBFT locks the mempool — no calls to `CheckTx` on new transactions。看见 locks the mempool，不是已经默认全局锁那种 Commit 前上锁、Commit 里等广播会停死（310）。看见 no CheckTx on new transactions，不是已经 CheckTx 技术上可选、不参与处理块（373）就已经是同一句 interchangeable。看见 When 第 7 步，不是已经 CometBFT persists tx outputs / AppHash / ResultsHash（467）那种已经交差 interchangeable。
2. **看见 CometBFT calls `Commit` to instruct the Application to persist its state / 看见叫 Commit 让应用落盘应用状态 不是已经引擎 persist tx outputs / AppHash / ResultsHash，也不是已经 Finalize 改了就已经落盘。**  
   官方 When 第 8 步写：CometBFT calls `Commit` to instruct the Application to persist its state。看见 calls Commit，不是已经引擎 persist 这三份（467）那种已经落盘 interchangeable。看见 instruct the Application to persist its state，不是已经 Finalize 改了状态就已经落盘（335）。看见 Commit 不带参数（399）只是门名，不是已经应用在 Finalize 里落盘 interchangeable。
3. **看见 optionally re-checks outstanding mempool txs / unlocks mempool / starts consensus for height h+1, round 0 / 看见可选再验、再解锁、再开下一高 round 0 不是已经是 Recheck，也不是已经能往下走 / 已经交差。**  
   官方 When 第 9–11 步写：optionally, re-checks all outstanding transactions in the mempool against the newly persisted Application state；unlocks the mempool — newly received transactions can now be checked；starts consensus for height h+1, round 0。看见 optionally recheck，不是已经 `CheckTx` 的 `Type` 标明 `RECHECK`（312）就已经是同一句 interchangeable。看见 unlocks mempool，不是已经 Commit 前上锁就已经解锁（310）。看见 starts h+1 round 0，不是已经交差。

怎样写 Finalize When 流程、怎样再验池里剩下的、怎样 Commit 是规范里的做法，本页不抄。Finalize 之后 bundled（403）是 persist 三份 / 锁池 / 再验那套另一切片，FinalizeBlock When AppHash tx outputs ResultHash persist（467）是 Application returns AppHash / ResultHash / persist 三份那套另一切片，Commit 不带参数（399）是 Commit 门那套另一切片，本页不抄。

## 官方为什么这样拆

- **locks mempool / no CheckTx on new tx ≠ 已经是 Commit 锁 / 已经 RPC 安全默认锁：** 官方把 When 第 7 步和 Commit 前那把锁分开。
- **calls Commit to persist application state ≠ 已经引擎 persist 这三份 / 已经 Finalize 改了就已经落盘：** 官方把应用 Commit 落盘和引擎 persist tx outputs / AppHash / ResultsHash 分开。
- **optionally recheck / unlock / start h+1 round 0 ≠ 已经是 Recheck / 已经能往下走：** 官方把可选再验和 RECHECK 类型 / 已经交差分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| locks mempool / no CheckTx on new tx | 不是已经是 Commit 锁 | 不是 Commit 前上锁就已经解锁（310） |
| calls Commit to persist application state | 不是已经引擎 persist 这三份 | 不是 FinalizeBlock When persist 三份（467） |
| optionally recheck / unlock / start h+1 round 0 | 不是已经是 Recheck | 不是 RECHECK 就已经是新交易（312） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Finalize 之后就已经锁池、已经 Commit 落盘、已经 Recheck」，必须分开 locks mempool 是不是已经是 Commit 锁、calls Commit 是不是已经引擎 persist 这三份、optionally recheck / unlock / start h+1 是不是已经是 Recheck。可以跳过「看见 Finalize 之后就已经交差」。不要另写怎样写 Finalize When 流程。

## 本页不抄

- 怎样写 Finalize When 流程、怎样再验池里剩下的、怎样 Commit。
- Finalize 之后 bundled 三事。那是不变量 403。
- FinalizeBlock When AppHash tx outputs ResultHash persist。那是不变量 467。
- Commit 不带参数。那是不变量 399。
- Commit 前上锁就已经解锁。那是不变量 310。
- RECHECK 就已经是新交易。那是不变量 312。
- Finalize 改了就已经落盘。那是不变量 335。
