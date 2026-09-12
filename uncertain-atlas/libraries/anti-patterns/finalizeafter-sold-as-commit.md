# 反模式：看见 Finalize 之后引擎才落盘各笔输出 / AppHash / ResultsHash 就当成已经交差 / 看见落完再锁内存池、新交易不进 CheckTx 就当成已经是 Commit 锁 / 看见可选再验池里剩下的、再解锁、再开下一高 round 0 就当成已经是 Recheck

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When。  
**例**：[Finalize 之后引擎才落盘各笔输出 / AppHash / ResultsHash ≠ 已经交差](../../tracks/implementation/worked-example-finalizeafter-vs-commit.md)。

## 塌法

1. 看见 Finalize 之后引擎才落盘各笔输出 / AppHash / ResultsHash / 看见回了 Finalize，就当成已经交差，或当成已经落盘应用状态。
2. 看见落完再锁内存池、新交易不进 CheckTx / 看见锁了，就当成已经是 Commit 锁，或当成已经交差。
3. 看见可选再验池里剩下的、再解锁、再开下一高 round 0 / 看见再验了，就当成已经是 Recheck，或当成已经交差。

## 为什么会出事

官方写：应用回了 AppHash 和各笔输出之后，引擎先把这些输出哈希进 ResultHash，再落盘各笔输出、`AppHash` 和 `ResultsHash`。落完才锁内存池；锁住期间不对新交易叫 `CheckTx`。叫完 `Commit` 之后，可以对照刚落盘的应用状态再验池里剩下的交易，再解锁，再开高度 `h+1`、round 0。

## 和相邻反模式

- [finalizewhen-sold-as-decided](finalizewhen-sold-as-decided.md) 是应用回了 AppHash 和各笔输出引擎哈希进 ResultHash 就已经印进本头，不是本页这种 Finalize 之后引擎才落盘各笔输出 / AppHash / ResultsHash 不是已经交差。
- [commitlock-sold-as-rpc](commitlock-sold-as-rpc.md) 是 Commit 前上锁就已经解锁，不是本页这种落完再锁内存池、新交易不进 CheckTx 不是已经是 Commit 锁。
- [checktxstate-sold-as-execute](checktxstate-sold-as-execute.md) 是 RECHECK 就已经是新交易，不是本页这种可选再验池里剩下的、再解锁、再开下一高 round 0 不是已经是 Recheck。
