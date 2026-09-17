# 反模式：把 Query Usage 正式三事卖成 QueryState / 已经对上 AppHash / ProofOp 按键查

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Query for data at current or past height ≠ QueryState](../../tracks/implementation/worked-example-queryusage-vs-querystate.md)。

## 卖法

- 「看见 Query for data from the application at current or past height / 查当前或过去高度 就已经是 QueryState / 已经复制到各节点 / 已经 QueryState 就是 ExecuteTxState。」
- 「看见 Optionally return Merkle proof / 可选回默克尔证明 就已经对上 AppHash / 已经勾了 prove 就齐 / 已经 Finalize Query proofs anchored 交差。」
- 「看见 Merkle proof includes self-describing type / 证明带自描述 type、好支持多种默克尔树和编码 就已经是 ProofOp.type 按键查 / 已经 Query 回了 Proof 就对上 AppHash / 已经 CheckTx 守卫余量 bundled 第三句 interchangeable。」

## 为什么错

官方把 Query for data at current or past height、Optionally return Merkle proof、Merkle proof self-describing type 写成三件独立的实现事。把它们卖成 QueryState / 已经对上 AppHash / ProofOp 按键查，会把 Methods Usage 查哪一高度、optional proof、proof type 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query Usage 正式三事，必须分开 Query for data at current or past height、Optionally return Merkle proof、Merkle proof self-describing type 三个名字，不要把它们卖成 QueryState / 已经对上 AppHash / ProofOp 按键查。

## 和相邻反模式

- [queryproof-sold-as-apphash](queryproof-sold-as-apphash.md) 是 Query 回了 Proof 就对上 AppHash，不是本页 Usage optional proof 全段。
- [checktxguard-sold-as-optional](checktxguard-sold-as-optional.md) 是 CheckTx 守卫余量 bundled 第三句，不是本页 Query Usage proof type。
- [queryheight-sold-as-committed](queryheight-sold-as-committed.md) 是 Query Request height 栏，不是本页 Usage 查当前或过去高度。
