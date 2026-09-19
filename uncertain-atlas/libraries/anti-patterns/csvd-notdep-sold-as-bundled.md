# 反模式：把 BIP-112 csv-deploy not already opcode / not already 41 / not already 164 正式三事（165 余量） 写成已经 已经是操作码 / 已经是不变量 41 / 已经是不变量 164

**层次**：实现 / BIP-112 csv-deploy not already opcode / not already 41 / not already 164 正式三事（165 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-112](https://github.com/bitcoin/bips/blob/master/bip-0112.mediawiki)（CHECKSEQUENCEVERIFY）。对照 [BIP-68](https://github.com/bitcoin/bips/blob/master/bip-0068.mediawiki)。  
**对应**：[`../tracks/state-models/worked-example-csvd-notdep-vs-bundled.md`](../tracks/state-models/worked-example-csvd-notdep-vs-bundled.md)。

把 BIP-112 csv-deploy not already opcode / not already 41 / not already 164 正式三事（165 余量） 写成已经 已经是操作码 / 已经是不变量 41 / 已经是不变量 164，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-112 CSV 正式三事（165 余量），必须分开 not already nsequence-locked、not already absolute-lock、not already opcode 三件事，不要和 165 / 41 / 164 / 1527 / 1528 糊成一句。

也不是：

- [csvd-notseq-sold-as-bundled](csvd-notseq-sold-as-bundled.md) 是 notseq 单句边界（1527），不是本页边界。
- [csvd-notabs-sold-as-bundled](csvd-notabs-sold-as-bundled.md) 是 notabs 单句边界（1528），不是本页边界。
- [rbfs-notrep-sold-as-bundled](rbfs-notrep-sold-as-bundled.md) 是 BIP-125 RBF 边界（166/1524），不是本页 CSV 边界。
