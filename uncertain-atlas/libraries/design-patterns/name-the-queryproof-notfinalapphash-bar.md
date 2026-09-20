# 模式：把一层 ProofOp 的根不是已经对上最终 AppHash not already next-layer / not already final-apphash / not already blockhash-compared 正式三事（325 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Query Proofs。  
**例**：[一层对上 not already next-layer ≠ bundled（325）](../../tracks/implementation/worked-example-queryproof-notfinalapphash-vs-bundled.md)。

## 三个名字

1. **一层对上 不是 already next-layer：** 看见一层对上 / 这一条 ProofOp 的根对了 / 一层根绿了，不是已经交给下一层 interchangeable / 已经是下一条要验的值交差 interchangeable，不是 325 queryproof bundled interchangeable / 33 four gates interchangeable / queryproof-sold-as-apphash interchangeable。

2. **中间根对了 不是 already final-apphash：** 看见中间根对了 / 对上了 / 某层根绿了，不是已经对上最终 AppHash interchangeable / 已经最后一条对 AppHash 交差 interchangeable，不是 38 apphash interchangeable / 325 queryproof item 1 interchangeable。

3. **能证缺席 不是 already blockhash-compared：** 看见能证缺席 / 缺席证明绿了 / 能证这把键不在，不是已经比对着块哈希 interchangeable / 已经对着块哈希交差 interchangeable，不是 147 apphash-this-block interchangeable / 325 queryproof item 2 interchangeable。

官方把一层对上单句、already next-layer、already final-apphash、already blockhash-compared 写成三个名字。把它们叫成一个「看见一层 ProofOp 的根对上了就已经走完多层 interchangeable / 就已经对上最终 AppHash interchangeable / 就已经比对着块哈希 interchangeable」，会把 not already next-layer、not already final-apphash、not already blockhash-compared 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看一层 ProofOp 的根不是已经对上最终 AppHash not already next-layer / not already final-apphash / not already blockhash-compared 正式三事（325 余量），先数清问的是一层对上 是不是 already next-layer / 325 / queryproof-sold-as-apphash，是不是中间根对了 是不是 already final-apphash，还是能证缺席 是不是 already blockhash-compared，再决定要不要同一次发布。325 queryproof vs apphash bundled unbundling 在本页 item 3 完成。
