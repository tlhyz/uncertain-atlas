# 反模式：看见 State 对象就当成已经进了块 / 看见头上的根就当成已经有了 State / 看见能读本地 State 就当成已经进了规范

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[State](https://github.com/cometbft/cometbft/blob/main/spec/core/state.md)。  
**例**：[State 对象 ≠ 已经进了块](../../tracks/implementation/worked-example-state-vs-gossip.md)。

## 塌法

1. 看见 State 对象 / 看见本地 State，就当成已经写进块，或当成已经流言，或当成已经有 State 哈希。
2. 看见头上的 Merkle 根 / 看见验证者根或结果根，就当成已经有了 State 对象本身。
3. 看见 State 的落盘或查询接口 / 看见能读本地 State，就当成已经进了规范。
4. 看见根对上了，就当成 State 已经流言过。
5. 看见本地 State，就当成本头 AppHash 已经交差。

## 为什么会出事

官方写：`State` 对象本身是实现细节，从不进块、不流言、不算哈希。进块的是这些对象的 Merkle 根。怎么落盘、怎么查询，不写进规范。

## 和相邻反模式

- [evidence-sold-as-full-block](evidence-sold-as-full-block.md) 是先装证据 ≠ 已经装满交易，不是本页这种 State。
- [wal-sold-as-signed](wal-sold-as-signed.md) 是写下 ≠ 已经 fsync，不是本页。
- [half-written-state](half-written-state.md) 是应用半写 ≠ 已经对齐高度，不是本页这种引擎 State。
