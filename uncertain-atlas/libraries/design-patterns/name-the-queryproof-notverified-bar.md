# 模式：把 Query 回了 Proof 不是已经对上 AppHash not already verified / not already same-tree / not already prove-absence 正式三事（325 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Query Proofs。  
**例**：[回了 Proof not already verified ≠ bundled（325）](../../tracks/implementation/worked-example-queryproof-notverified-vs-bundled.md)。

## 三个名字

1. **回了 Proof 不是 already verified：** 看见回了 Proof / QueryResponse.Proof / 回了证明，不是已经验过对上 AppHash interchangeable / 已经用对应块 AppHash 验过交差 interchangeable，不是 325 queryproof bundled interchangeable / 33 four gates interchangeable / queryproof-sold-as-apphash interchangeable。

2. **有 type 不是 already same-tree：** 看见有 type / ProofOp 有 type / 指定了树类型，不是已经是同一棵树 interchangeable / 已经一层树交差 interchangeable，不是 314 querystate interchangeable / 325 queryproof item 1 interchangeable。

3. **能证存在 不是 already prove-absence：** 看见能证存在 / 存在证明绿了 / 能证这把键在，不是已经能证不存在 interchangeable / 已经缺席证明交差 interchangeable，不是 38 apphash interchangeable / 325 queryproof item 3 interchangeable。

官方把回了 Proof 单句、already verified、already same-tree、already prove-absence 写成三个名字。把它们叫成一个「看见 Query 回了 Proof 就已经对上 AppHash interchangeable / 就已经是一层树 interchangeable / 就已经能证不存在 interchangeable」，会把 not already verified、not already same-tree、not already prove-absence 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 回了 Proof 不是已经对上 AppHash not already verified / not already same-tree / not already prove-absence 正式三事（325 余量），先数清问的是回了 Proof 是不是 already verified / 325 / queryproof-sold-as-apphash，是不是有 type 是不是 already same-tree，还是能证存在 是不是 already prove-absence，再决定要不要同一次发布。325 queryproof vs apphash bundled unbundling 在本页 item 2 续。
