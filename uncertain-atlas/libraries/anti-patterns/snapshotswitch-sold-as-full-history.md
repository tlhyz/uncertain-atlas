# 反模式：看见快照装完就当成已经有了 ChainID / 看见 Info 的 AppHash 对上就当成已经版本也对上 / 看见切进共识就当成已经有从创世的完整历史

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Transition to Consensus。  
**例**：[装完 ≠ 已经有了 ChainID](../../tracks/implementation/worked-example-snapshot-switch-vs-history.md)。

## 塌法

1. 看见快照已经装完 / 看见状态机已经恢复，就当成已经有了 ChainID、参数、集合和头，或当成已经能出块。
2. 看见 Info 的 AppHash 对上了 / 看见对上下一高度，就当成已经是版本也对上，或当成已经是本头 AppHash。
3. 看见切进共识 / 看见能出块，就当成已经有从创世的完整历史，或当成已经没有截断。

## 为什么会出事

官方写：装完之后还要从创世文件和轻客户端 RPC 再凑引导信息。Info 要分开核对下一高度的 AppHash 和当前头的版本。切过去之后块历史在快照高度被截断。

## 和相邻反模式

- [snapshotrestore-sold-as-offered](snapshotrestore-sold-as-offered.md) 是 Offer 收下 ≠ 已经装完，不是本页这种装完还没切。
- [snapshotdiscover-sold-as-listed](snapshotdiscover-sold-as-listed.md) 是 ListSnapshots 回了 ≠ 已经齐，不是本页。
