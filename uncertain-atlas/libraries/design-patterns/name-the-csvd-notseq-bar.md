# 模式：点名 csvd-notseq 杠

**层次**：实现 / BIP-112 script-csv not already nsequence-locked / not already 164 / not already 165-bundled 正式三事（165 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-112](https://github.com/bitcoin/bips/blob/master/bip-0112.mediawiki)（CHECKSEQUENCEVERIFY）。对照 [BIP-68](https://github.com/bitcoin/bips/blob/master/bip-0068.mediawiki)。  
**对应**：[`../tracks/state-models/worked-example-csvd-notseq-vs-bundled.md`](../tracks/state-models/worked-example-csvd-notseq-vs-bundled.md)。

- **脚本里的CSV不是nSequence已经把输出相对锁住 不是已经相对锁住：看见脚本里的CSV不是nSequence已经把输出相对锁住，不是已经相对锁住 interchangeable / 1527 csvd-notseq interchangeable。**
- **script CSV is not already a relative lock from nSequence 不是已经是不变量 164：看见script CSV is not already a relative lock from nSequence，不是已经是不变量 164 interchangeable / 1527 csvd-notseq interchangeable。**
- **脚本里的CSV不是nSequence已经把输出相对锁住 不是已经 165 bundled：看见脚本里的CSV不是nSequence已经把输出相对锁住，不是已经 165 bundled interchangeable / 1527 csvd-notseq interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-112 CSV 正式三事（165 余量），必须分开 not already nsequence-locked、not already absolute-lock、not already opcode 三件事。
