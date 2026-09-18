# 模式：点名 raw385-notaddr 杠

**层次**：应用 / BIP-385 addr not already nestable-in-sh-wsh / not already output-script-written / not already settled 正式三事（282 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-385](https://github.com/bitcoin/bips/blob/master/bip-0385.mediawiki)（Deployed, Applications, Informational）。  
**对应**：[`../tracks/implementation/worked-example-raw385-notaddr-vs-bundled.md`](../tracks/implementation/worked-example-raw385-notaddr-vs-bundled.md)。

- **addr 不是已经能套进 sh / wsh：** 看见 addr，不是已经能套进 sh / wsh interchangeable / 1167 raw385-notaddr interchangeable。
- **一个地址 不是已经把输出脚本写在描述符里：** 看见一个地址，不是已经把输出脚本写在描述符里 interchangeable / 1167 raw385-notaddr interchangeable。
- **用 addr 包住了地址 不是已经交差：** 看见用 addr 包住了地址，不是已经交差 interchangeable / 1167 raw385-notaddr interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 addr 正式三事（282 余量），必须分开 not already nestable-in-sh-wsh、not already output-script-written、not already settled 三件事。
