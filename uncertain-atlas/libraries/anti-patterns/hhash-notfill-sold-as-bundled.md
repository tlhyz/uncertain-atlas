# 反模式：把 EIP-2935 sys-write not already window-full / not already 169 / not already 157 正式三事（195 余量） 写成已经 已经填满窗口 / 已经是不变量 169 / 已经是不变量 157

**层次**：实现 / EIP-2935 sys-write not already window-full / not already 169 / not already 157 正式三事（195 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-2935](https://eips.ethereum.org/EIPS/eip-2935)（Serve historical block hashes from state）。  
**对应**：[`../tracks/light-clients/worked-example-hhash-notfill-vs-bundled.md`](../tracks/light-clients/worked-example-hhash-notfill-vs-bundled.md)。

把 EIP-2935 sys-write not already window-full / not already 169 / not already 157 正式三事（195 余量） 写成已经 已经填满窗口 / 已经是不变量 169 / 已经是不变量 157，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-2935 history-hash 正式三事（195 余量），必须分开 not already BLOCKHASH、not already window-full、not already opcode-changed 三件事，不要和 195 / 169 / 157 / 1500 / 1502 糊成一句。

也不是：

- [hhash-notbh-sold-as-bundled](hhash-notbh-sold-as-bundled.md) 是 notbh 单句边界（1500），不是本页边界。
- [hhash-notsem-sold-as-bundled](hhash-notsem-sold-as-bundled.md) 是 notsem 单句边界（1502），不是本页边界。
- [bres-notacct-sold-as-bundled](bres-notacct-sold-as-bundled.md) 是 EIP-7918 blob 底价边界（201/1497），不是本页历史哈希边界。
