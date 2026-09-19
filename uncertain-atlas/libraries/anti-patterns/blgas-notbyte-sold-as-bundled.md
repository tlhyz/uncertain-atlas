# 反模式：把 EIP-4844 blobhash not already sidecar-bytes / not already 197 / not already 201 正式三事（145 余量） 写成已经 已经读到blob字节 / 已经是不变量 197 / 已经是不变量 201

**层次**：实现 / EIP-4844 blobhash not already sidecar-bytes / not already 197 / not already 201 正式三事（145 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-4844](https://eips.ethereum.org/EIPS/eip-4844)（Shard Blob Transactions）。  
**对应**：[`../tracks/light-clients/worked-example-blgas-notbyte-vs-bundled.md`](../tracks/light-clients/worked-example-blgas-notbyte-vs-bundled.md)。

把 EIP-4844 blobhash not already sidecar-bytes / not already 197 / not already 201 正式三事（145 余量） 写成已经 已经读到blob字节 / 已经是不变量 197 / 已经是不变量 201，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-4844 blob-fee 正式三事（145 余量），必须分开 not already execution-gas、not already sidecar-bytes、not already perpetual 三件事，不要和 145 / 197 / 201 / 1491 / 1493 糊成一句。

也不是：

- [blgas-notexec-sold-as-bundled](blgas-notexec-sold-as-bundled.md) 是 notexec 单句边界（1491），不是本页边界。
- [blgas-notperm-sold-as-bundled](blgas-notperm-sold-as-bundled.md) 是 notperm 单句边界（1493），不是本页边界。
- [hwin-notcons-sold-as-bundled](hwin-notcons-sold-as-bundled.md) 是 EIP-7642 历史窗边界（207/1488），不是本页 blob 气种边界。
