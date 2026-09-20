# 反模式：把 EIP-7691 raise-schedule not already gas-split-changed / not already 145 / not already 200-bundled 正式三事（200 余量） 写成已经 已经改了两套气的拆分 / 已经是不变量 145 / 已经 200 bundled

**层次**：实现 / EIP-7691 raise-schedule not already gas-split-changed / not already 145 / not already 200-bundled 正式三事（200 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-7691](https://eips.ethereum.org/EIPS/eip-7691)（Blob throughput increase）。  
**对应**：[`../tracks/light-clients/worked-example-bsch-notgas-vs-bundled.md`](../tracks/light-clients/worked-example-bsch-notgas-vs-bundled.md)。

把 EIP-7691 raise-schedule not already gas-split-changed / not already 145 / not already 200-bundled 正式三事（200 余量） 写成已经 已经改了两套气的拆分 / 已经是不变量 145 / 已经 200 bundled，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7691 blob-schedule 正式三事（200 余量），必须分开 not already gas-split-changed、not already old-symmetric、not already el-activated 三件事，不要和 200 / 145 / 23 / 1495 / 1496 糊成一句。

也不是：

- [bsch-notratio-sold-as-bundled](bsch-notratio-sold-as-bundled.md) 是 notratio 单句边界（1495），不是本页边界。
- [bsch-notel-sold-as-bundled](bsch-notel-sold-as-bundled.md) 是 notel 单句边界（1496），不是本页边界。
- [blgas-notexec-sold-as-bundled](blgas-notexec-sold-as-bundled.md) 是 EIP-4844 blob 气种边界（145/1491），不是本页 blob 日程边界。
