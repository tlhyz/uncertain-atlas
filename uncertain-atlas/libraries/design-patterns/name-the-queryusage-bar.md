# 模式：把 Query Usage 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Usage。  
**例**：[Query for data at current or past height ≠ QueryState](../../tracks/implementation/worked-example-queryusage-vs-querystate.md)。

## 三个名字

1. **Query for data at current or past height 不是已经是 QueryState：** 看见 Methods Usage 侧查当前或过去高度，不是 Query Request height 栏 bundled 或 QueryState 那份只读副本 interchangeable。
2. **Optionally return Merkle proof 不是已经对上 AppHash：** 看见 Usage optional proof，不是 Request prove 栏 / 验 AppHash bundled interchangeable。
3. **Merkle proof self-describing type 不是 ProofOp 按键查：** 看见 Usage proof type 支持多种树和编码，不是 ProofOp.type 按键查或 CheckTx 守卫余量 bundled interchangeable。

## 为什么要分开叫

官方把 Query Usage 里 Query for data at current or past height、Optionally return Merkle proof、Merkle proof self-describing type，和 Query Request height（371）、Query 证明回包（383）、ProofOp.type（325）写成三个名字。把它们叫成一个「看见能 Query 就已经是 QueryState、已经对上 AppHash、已经是 ProofOp 按键查」，会把查哪一高度、optional proof、proof type 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query Usage 正式三事，先数清问的是 Query for data at current or past height 是不是已经是 QueryState、Optionally return Merkle proof 是不是已经对上 AppHash、Merkle proof self-describing type 是不是 ProofOp 按键查，再决定要不要同一次发布。
