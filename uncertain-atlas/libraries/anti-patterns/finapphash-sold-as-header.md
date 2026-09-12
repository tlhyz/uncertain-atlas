# 反模式：看见 Finalize 回包 app_hash 可以空或硬编码、但必须确定就当成已经印进本头 / 看见以后 Query 可以拿这份根当锚回证明就当成已经对上 AppHash / 看见 tx_results[i].Code == 0 只表示第 i 笔完全合法就当成已经没进块

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[Finalize 回包 app_hash 可以空或硬编码、但必须确定 ≠ 已经印进本头](../../tracks/implementation/worked-example-finapphash-vs-header.md)。

## 塌法

1. 看见 Finalize 回包 `app_hash` 可以空或硬编码、但必须确定 / 看见回了 app_hash，就当成已经印进本头，或当成已经交差。
2. 看见以后 Query 可以拿这份根当锚回证明 / 看见能回证明，就当成已经对上 AppHash，或当成已经是按键查。
3. 看见 `tx_results[i].Code == 0` 只表示第 i 笔完全合法 / 看见回了 0，就当成已经没进块，或当成已经印进本头。

## 为什么会出事

官方写：`FinalizeBlockResponse.app_hash` 可以空，也可以硬编码，但必须确定。以后叫 `Query`，可以回以这份默克尔根为锚的应用状态证明。`tx_results[i].Code == 0` 只表示第 i 笔完全合法。

## 和相邻反模式

- [apphash-sold-as-this-block](apphash-sold-as-this-block.md) 是本头 AppHash 就已经是本高度交差，不是本页这种 Finalize 回包 app_hash 可以空或硬编码、但必须确定不是已经印进本头。
- [proofop-sold-as-key](proofop-sold-as-key.md) 是 ProofOp.type 就已经是按键查，不是本页这种以后 Query 可以拿这份根当锚回证明不是已经对上 AppHash。
- [exectxresult-sold-as-consensus](exectxresult-sold-as-consensus.md) 是 Code 非零就已经没进块，不是本页这种 tx_results[i].Code == 0 只表示第 i 笔完全合法不是已经没进块。
