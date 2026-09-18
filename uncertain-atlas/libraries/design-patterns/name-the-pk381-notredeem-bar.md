# 模式：点名 pk381-notredeem 杠

**层次**：应用 / BIP-381 sh-output not already have-redeem / not already spendable / not already settled 正式三事（276 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-381](https://github.com/bitcoin/bips/blob/master/bip-0381.mediawiki)（Deployed, Applications, Informational）。  
**对应**：[`../tracks/implementation/worked-example-pk381-notredeem-vs-bundled.md`](../tracks/implementation/worked-example-pk381-notredeem-vs-bundled.md)。

- **sh 产出 不是已经有赎回脚本：** 看见 P2SH 输出脚本，不是已经有赎回脚本 interchangeable / 1149 pk381-notredeem interchangeable。
- **套进了脚本表达式 不是已经能花：** 看见套进了脚本表达式，不是已经能花 interchangeable / 1149 pk381-notredeem interchangeable。
- **另造一份赎回脚本 不是已经交差：** 看见另造一份赎回脚本，不是已经交差 interchangeable / 1149 pk381-notredeem interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 sh 产出 正式三事（276 余量），必须分开 not already have-redeem、not already spendable、not already settled 三件事。
