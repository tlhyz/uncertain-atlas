# 反模式：把 Merkle proof self-describing-type not already ProofOp-type / not already apphash-aligned / not already settled 正式三事（405 余量） 写成已经 已经是 ProofOp 类型 / 已经对上 AppHash / 已经交差

**层次**：实现 / Merkle proof self-describing-type not already ProofOp-type / not already apphash-aligned / not already settled 正式三事（405 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage / Query Usage。  
**对应**：[`../tracks/implementation/worked-example-cguard-notproof-vs-bundled.md`](../tracks/implementation/worked-example-cguard-notproof-vs-bundled.md)。

把 Merkle proof self-describing-type not already ProofOp-type / not already apphash-aligned / not already settled 正式三事（405 余量） 写成已经 已经是 ProofOp 类型 / 已经对上 AppHash / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看自描述 type 正式三事（405 余量），必须分开 not already ProofOp-type、not already apphash-aligned、not already settled 三件事，不要和 405 / 325 / 1101 / 1103 / 1104 糊成一句。

也不是：

- [cguard-notreplay-sold-as-bundled](cguard-notreplay-sold-as-bundled.md) 是来源仍未保证不重放单句边界（1104 item 2），不是本页自描述 type 仍未是 ProofOp 类型边界。
- ProofOp.type 就已经是按键查是不变量 325，不是本页能支持多种树仍未对上 AppHash 边界。
