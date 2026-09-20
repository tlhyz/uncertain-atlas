# 反模式：把 EIP-7623 calldata-floor not already execution-gas / not already 145 / not already 197-bundled 正式三事（197 余量） 写成已经 已经改了执行气 / 已经是不变量 145 / 已经 197 bundled

**层次**：实现 / EIP-7623 calldata-floor not already execution-gas / not already 145 / not already 197-bundled 正式三事（197 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-7623](https://eips.ethereum.org/EIPS/eip-7623)（Increase calldata cost）。  
**对应**：[`../tracks/implementation/worked-example-cflr-notexec-vs-bundled.md`](../tracks/implementation/worked-example-cflr-notexec-vs-bundled.md)。

把 EIP-7623 calldata-floor not already execution-gas / not already 145 / not already 197-bundled 正式三事（197 余量） 写成已经 已经改了执行气 / 已经是不变量 145 / 已经 197 bundled，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7623 calldata-floor 正式三事（197 余量），必须分开 not already execution-gas、not already transfer-dearer、not already burned 三件事，不要和 197 / 145 / 202 / 1468 / 1469 糊成一句。

也不是：

- [cflr-notxfer-sold-as-bundled](cflr-notxfer-sold-as-bundled.md) 是 notxfer 单句边界（1468），不是本页边界。
- [cflr-notburn-sold-as-bundled](cflr-notburn-sold-as-bundled.md) 是 notburn 单句边界（1469），不是本页边界。
- [rcap-notgas-sold-as-bundled](rcap-notgas-sold-as-bundled.md) 是 EIP-7934 编码硬帽边界（202/1464），不是本页 calldata 地板边界。
