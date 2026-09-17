# 模式：把 Query Usage Merkle proof self-describing type not ProofOp 按键查 / not CheckTx 守卫余量 / not Snapshot 高度余量 正式三事（487 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Usage。  
**例**：[Merkle proof self-describing type not ProofOp ≠ bundled（487）](../../tracks/implementation/worked-example-queryusage-notprooftype-vs-bundled.md)。

## 三个名字

1. **Merkle proof self-describing type 不是 ProofOp 按键查：** 看见 Usage proof type 支持多种树和编码，不是已经是 ProofOp.type 那种按键查 interchangeable，不是 325 proofop interchangeable / 679 queryusage-notprooftype interchangeable。

2. **证明带自描述 type 不是 CheckTx 守卫余量：** 看见 Usage 这句，不是已经 CheckTx 守卫余量 bundled 第三句 interchangeable，不是 405 checktxguard interchangeable。

3. **看见 type 字段 不是 Snapshot 高度余量：** 看见 self-describing type，不是已经 Snapshot 高度余量 bundled 第三句 interchangeable，不是 406 snapheight interchangeable。

官方把 Query Usage proof type、ProofOp.type 按键查、CheckTx 守卫余量 / Snapshot 高度余量写成三个名字。把它们叫成一个「看见 Merkle proof self-describing type 就已经 ProofOp 按键查 interchangeable / 就已经 CheckTx 守卫余量 interchangeable / 就已经 Snapshot 高度余量 interchangeable」，会把 not ProofOp、not CheckTx 守卫余量、not Snapshot 高度余量 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query Usage Merkle proof self-describing type not ProofOp 按键查 / not CheckTx 守卫余量 / not Snapshot 高度余量 正式三事（487 余量），先数清问的是 Merkle proof self-describing type 是不是 ProofOp 按键查 / 325、是不是 CheckTx 守卫余量 / 405，还是看见 type 字段 是不是 Snapshot 高度余量 / 406，再决定要不要同一次发布。487 queryusage vs querystate bundled unbundling 在本页 item 3 完成。
