# 反模式：把 Query Usage Merkle proof self-describing type not ProofOp 按键查 / not CheckTx 守卫余量 / not Snapshot 高度余量 正式三事（487 余量）说成已经 ProofOp 按键查 / 已经 CheckTx 守卫余量 / 已经 Snapshot 高度余量

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Merkle proof self-describing type not ProofOp ≠ bundled（487）](../../tracks/implementation/worked-example-queryusage-notprooftype-vs-bundled.md)。

## 卖法

把 Merkle proof includes self-describing `type` field / 证明带自描述 type、好支持多种默克尔树和编码 写成已经是 `ProofOp.type` 那种按键查 interchangeable / 325 proofop interchangeable / 已经 Query 回了 Proof 就对上 AppHash interchangeable；把证明带自描述 type 写成已经 CheckTx 守卫余量 bundled 第三句 interchangeable / 405 checktxguard interchangeable / checktxguard-sold-as-optional interchangeable；把看见 type 字段写成已经 Snapshot 高度余量 bundled 第三句 interchangeable / 406 snapheight interchangeable / 已经 Query 可以可选回默克尔证明就已经对上 AppHash interchangeable，或已经和 487 queryusage-vs-querystate bundled / queryusage-notprooftype-sold-as-bundled interchangeable / 679 queryusage-notprooftype interchangeable。

## 为什么错

官方把 Query Usage proof type、ProofOp.type 按键查、CheckTx 守卫余量 bundled 第三句、Snapshot 高度余量 bundled 第三句写成三件独立的实现事。把它们卖成 ProofOp 按键查 interchangeable / CheckTx 守卫余量 interchangeable / Snapshot 高度余量 interchangeable，会把 not ProofOp、not CheckTx 守卫余量、not Snapshot 高度余量 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query Usage Merkle proof self-describing type not ProofOp 按键查 / not CheckTx 守卫余量 / not Snapshot 高度余量 正式三事（487 余量），必须分开 not ProofOp 按键查、not CheckTx 守卫余量、not Snapshot 高度余量 三件事，不要和 487 / 325 / 405 / 406 / 677 / 678 糊成一句。

## 和相邻反模式

- [queryusage-sold-as-querystate](queryusage-sold-as-querystate.md) 是 Query Usage 正式三事 bundled（487），不是本页 item 3 单句边界。
- [queryusage-notproof-sold-as-bundled](queryusage-notproof-sold-as-bundled.md) 是 Optionally return Merkle proof 单句边界（678 item 2），不是本页 proof type 边界。
- [checktxguard-sold-as-optional](checktxguard-sold-as-optional.md) 是 CheckTx 守卫余量 bundled 第三句，不是本页 Query Usage proof type。
