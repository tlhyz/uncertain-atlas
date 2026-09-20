# 反模式：把 EIP-7918 no-subtract-target not already schedule-changed / not already 200 / not already 23 正式三事（201 余量） 写成已经 已经改了日程数字 / 已经是不变量 200 / 已经是不变量 23

**层次**：实现 / EIP-7918 no-subtract-target not already schedule-changed / not already 200 / not already 23 正式三事（201 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-7918](https://eips.ethereum.org/EIPS/eip-7918)（Blob base fee bounded by execution cost）。  
**对应**：[`../tracks/light-clients/worked-example-bres-notsch-vs-bundled.md`](../tracks/light-clients/worked-example-bres-notsch-vs-bundled.md)。

把 EIP-7918 no-subtract-target not already schedule-changed / not already 200 / not already 23 正式三事（201 余量） 写成已经 已经改了日程数字 / 已经是不变量 200 / 已经是不变量 23，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7918 blob-reserve 正式三事（201 余量），必须分开 not already gas-merged、not already blob-priceless、not already schedule-changed 三件事，不要和 201 / 200 / 23 / 1497 / 1498 糊成一句。

也不是：

- [bres-notacct-sold-as-bundled](bres-notacct-sold-as-bundled.md) 是 notacct 单句边界（1497），不是本页边界。
- [bres-notgone-sold-as-bundled](bres-notgone-sold-as-bundled.md) 是 notgone 单句边界（1498），不是本页边界。
- [bsch-notgas-sold-as-bundled](bsch-notgas-sold-as-bundled.md) 是 EIP-7691 blob 日程边界（200/1494），不是本页 blob 底价边界。
