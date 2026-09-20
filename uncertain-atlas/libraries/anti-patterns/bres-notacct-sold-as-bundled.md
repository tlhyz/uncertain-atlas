# 反模式：把 EIP-7918 reserve-floor not already gas-merged / not already 145 / not already 201-bundled 正式三事（201 余量） 写成已经 已经并成一套气 / 已经是不变量 145 / 已经 201 bundled

**层次**：实现 / EIP-7918 reserve-floor not already gas-merged / not already 145 / not already 201-bundled 正式三事（201 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-7918](https://eips.ethereum.org/EIPS/eip-7918)（Blob base fee bounded by execution cost）。  
**对应**：[`../tracks/light-clients/worked-example-bres-notacct-vs-bundled.md`](../tracks/light-clients/worked-example-bres-notacct-vs-bundled.md)。

把 EIP-7918 reserve-floor not already gas-merged / not already 145 / not already 201-bundled 正式三事（201 余量） 写成已经 已经并成一套气 / 已经是不变量 145 / 已经 201 bundled，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7918 blob-reserve 正式三事（201 余量），必须分开 not already gas-merged、not already blob-priceless、not already schedule-changed 三件事，不要和 201 / 145 / 200 / 1498 / 1499 糊成一句。

也不是：

- [bres-notgone-sold-as-bundled](bres-notgone-sold-as-bundled.md) 是 notgone 单句边界（1498），不是本页边界。
- [bres-notsch-sold-as-bundled](bres-notsch-sold-as-bundled.md) 是 notsch 单句边界（1499），不是本页边界。
- [bsch-notgas-sold-as-bundled](bsch-notgas-sold-as-bundled.md) 是 EIP-7691 blob 日程边界（200/1494），不是本页 blob 底价边界。
