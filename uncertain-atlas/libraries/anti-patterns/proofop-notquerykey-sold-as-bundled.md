# 反模式：把 ProofOp.key not Query response key / not ProofOp type / not already settled 正式三事（390 余量） 说成已经是 Query 回包键 / 已经是 ProofOp 类型 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[ProofOp.key ≠ bundled（390）](../../tracks/implementation/worked-example-proofop-notquerykey-vs-bundled.md)。

## 卖法

把 ProofOp 键这句写成已经已经是 Query 回包键 / 已经是 ProofOp 类型 / 已经交差 interchangeable，或已经和 390 proofop-vs-key bundled / proofop-notquerykey-sold-as-bundled interchangeable。

## 为什么错

官方把 ProofOp.key / ProofOp.data / CheckTx 回包 log 三条核心句写成三件独立的实现事。把它们卖成已经是 Query 回包键 / 已经是 ProofOp 类型 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProofOp.key 正式三事（390 余量），必须分开 not Query response key、not ProofOp type、not already settled 三件事，不要和 390 / 380 / 744 / 745 糊成一句。

## 和相邻反模式

- [proofop-sold-as-key](proofop-sold-as-key.md) 是 ProofOp 键 bundled（390），不是本页 item 1 单句边界。
- [proofop-notproofops-sold-as-bundled](proofop-notproofops-sold-as-bundled.md) 是 data 单句边界（744 item 2），不是本页 key 边界。
