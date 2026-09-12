# 反模式：看见头上有 AppHash 就当成已经是交易默克尔 / 看见 Query 回了 Proof 就当成已经对上 AppHash / 看见一层 ProofOp 的根就当成已经对上最终 AppHash

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Query Proofs。  
**例**：[头上有 AppHash ≠ 已经是交易默克尔](../../tracks/implementation/worked-example-query-proof-vs-apphash.md)。

## 塌法

1. 看见头上有 AppHash / 看见和 ValidatorsHash、DataHash 并列，就当成已经是交易默克尔，或当成已经是验证者集合。
2. 看见 Query 回了 Proof / 看见 QueryResponse.Proof，就当成已经对上 AppHash，或当成已经是一层树。
3. 看见一层 ProofOp 的根 / 看见对上了，就当成已经是下一层要验的值，或当成已经对上最终 AppHash。

## 为什么会出事

官方写：AppHash 是应用自己的锚，不是 DataHash，也不是 ValidatorsHash。QueryResponse.Proof 是一串 ProofOp，每一条只覆盖一棵树的一把键。验整份时这一条的根是下一条的值，最后一条才对 AppHash。

## 和相邻反模式

- [apphash-sold-as-this-block](apphash-sold-as-this-block.md) 是本头 AppHash ≠ 本高度已经交差，不是本页这种查询证明。
- [querystate-sold-as-execute](querystate-sold-as-execute.md) 是 QueryState ≠ 已经是 ExecuteTxState，不是本页。
- [snapshottake-sold-as-committed](snapshottake-sold-as-committed.md) 是拍了这个高度 ≠ 已经交差之后拍的，不是本页。
