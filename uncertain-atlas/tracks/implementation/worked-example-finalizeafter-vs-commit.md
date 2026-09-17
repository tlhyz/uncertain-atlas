# 例：看见 Finalize 之后引擎才落盘各笔输出 / AppHash / ResultsHash 不是已经交差；看见落完再锁内存池、新交易不进 CheckTx 不是已经是 Commit 锁；看见可选再验池里剩下的、再解锁、再开下一高 round 0 不是已经是 Recheck

**层次**：实现 / Finalize 之后。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「Finalize 之后引擎才落盘各笔输出 / AppHash / ResultsHash 不是已经交差 / 落完再锁内存池、新交易不进 CheckTx 不是已经是 Commit 锁 / 可选再验池里剩下的、再解锁、再开下一高 round 0 不是已经是 Recheck」，不是应用回了 AppHash 和各笔输出引擎哈希进 ResultHash 就已经印进本头，也不是 Finalize 改了就已经落盘。不要另写怎样写 Finalize 之后。

## 官方三件事

规范把 Finalize 回了之后引擎才落盘各笔输出 / AppHash / ResultsHash、落完再锁内存池、新交易不进 CheckTx、可选再验池里剩下的、再解锁、再开下一高 round 0 写成三件独立的实现事，不是「看见回了 Finalize 就已经交差、已经是 Commit 锁、已经是 Recheck」一件事：

1. **看见 Finalize 之后引擎才落盘各笔输出 / AppHash / ResultsHash / 看见回了 Finalize 不是已经交差，也不是已经落盘应用状态。**  
   官方写：应用回了 AppHash 和各笔输出之后，引擎先把这些输出哈希进 ResultHash，再落盘各笔输出、`AppHash` 和 `ResultsHash`。看见回了 Finalize，不是已经交差。看见有 ResultHash，不是已经落盘应用状态。看见引擎落了这三份，不是已经应用在 `Commit` 里落盘。
2. **看见落完再锁内存池、新交易不进 CheckTx / 看见锁了 不是已经是 Commit 锁，也不是已经交差。**  
   官方写：引擎落完这三份之后，才锁内存池；锁住期间不对新交易叫 `CheckTx`。看见锁了，不是已经默认全局锁那种 Commit 前上锁、Commit 里等广播会停死。看见新交易不进 CheckTx，不是已经技术上可选、不参与处理块。看见锁上了，不是已经交差。
3. **看见可选再验池里剩下的、再解锁、再开下一高 round 0 / 看见再验了 不是已经是 Recheck，也不是已经交差。**  
   官方写：引擎叫完 `Commit` 之后，可以对照刚落盘的应用状态再验池里剩下的交易，再解锁内存池，再开高度 `h+1`、round 0。看见再验了，不是已经 `CheckTx` 的 `Type` 标明 `RECHECK`。看见解锁了，不是已经能往下走。看见开了下一高，不是已经交差。

怎样写 Finalize 之后、怎样落盘这三份、怎样再验是规范里的做法，本页不抄。应用回了 AppHash 和各笔输出引擎哈希进 ResultHash 就已经印进本头是不变量 362，本页不抄。

## 官方为什么这样拆

- **Finalize 之后引擎才落盘各笔输出 / AppHash / ResultsHash ≠ 已经交差：** 官方把回了 Finalize 和引擎落这三份分开。
- **落完再锁内存池、新交易不进 CheckTx ≠ 已经是 Commit 锁：** 官方把这时锁住不接新 CheckTx 和 Commit 前那把锁分开。
- **可选再验池里剩下的、再解锁、再开下一高 round 0 ≠ 已经是 Recheck：** 官方把可以再验和 Recheck 类型分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Finalize 之后引擎才落盘各笔输出 / AppHash / ResultsHash | 不是已经交差 | 不是应用回了 AppHash 和各笔输出引擎哈希进 ResultHash 就已经印进本头（362） |
| 落完再锁内存池、新交易不进 CheckTx | 不是已经是 Commit 锁 | 不是 Commit 前上锁就已经解锁（310） |
| 可选再验池里剩下的、再解锁、再开下一高 round 0 | 不是已经是 Recheck | 不是 RECHECK 就已经是新交易（312） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见回了 Finalize 就已经交差、已经是 Commit 锁、已经是 Recheck」，必须分开 Finalize 之后引擎才落盘各笔输出 / AppHash / ResultsHash 是不是已经交差、落完再锁内存池、新交易不进 CheckTx 是不是已经是 Commit 锁、可选再验池里剩下的、再解锁、再开下一高 round 0 是不是已经是 Recheck。可以跳过「看见回了 Finalize 就已经交差」。不要另写怎样写 Finalize 之后。

## 本页不抄

- 怎样写 Finalize 之后、怎样落盘这三份、怎样再验。
- 应用回了 AppHash 和各笔输出引擎哈希进 ResultHash 就已经印进本头。那是不变量 362。
- Commit 前上锁就已经解锁。那是不变量 310。
- RECHECK 就已经是新交易。那是不变量 312。
