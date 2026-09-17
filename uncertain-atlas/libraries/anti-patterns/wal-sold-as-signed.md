# 反模式：看见写下每条消息就当成已经 fsync / 看见回放时又要签就当成已经双签 / 看见 LastSignBytes 对上就当成已经换了高度

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[CometBFT WAL](https://github.com/cometbft/cometbft/blob/main/spec/consensus/wal.md)。  
**例**：[写下 ≠ 已经 fsync](../../tracks/implementation/worked-example-wal-vs-signed.md)。

## 塌法

1. 看见共识模块写下每条消息 / 看见 WAL 里有消息，就当成已经对本节点签过的消息做了 fsync，或当成已经防了双签。
2. 看见崩溃后回放上一高度 / 看见私钥签名器在回放时又要签，就当成已经双签，或当成已经发出新的一票。
3. 看见 LastSignBytes 对上 / 看见回放走到 precommit，就当成已经换了高度。
4. 看见这次签名失败，就当成回放已经坏了。
5. 看见有预写日志，就当成应用半写已经对齐。

## 为什么会出事

官方写：每条消息都写进 WAL，但 fsync 是为本节点签过的消息防双签。回放时签名器并不知道正在回放，再想签 prevote 失败是正常的。`LastSignBytes` 对上是为了继续回放旧的 precommit，不是新高度。

## 和相邻反模式

- [half-written-state](half-written-state.md) 是应用半写 ≠ 已经对齐高度，不是本页这种预写日志。
- [p2sh-address-sold-as-16](p2sh-address-sold-as-16.md) 是付给脚本哈希地址 ≠ 已经是 16，不是本页。
