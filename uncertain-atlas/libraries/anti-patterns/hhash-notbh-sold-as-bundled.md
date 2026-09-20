# 反模式：把 EIP-2935 state-hash not already BLOCKHASH / not already 156 / not already 195-bundled 正式三事（195 余量） 写成已经 已经是BLOCKHASH / 已经是不变量 156 / 已经 195 bundled

**层次**：实现 / EIP-2935 state-hash not already BLOCKHASH / not already 156 / not already 195-bundled 正式三事（195 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-2935](https://eips.ethereum.org/EIPS/eip-2935)（Serve historical block hashes from state）。  
**对应**：[`../tracks/light-clients/worked-example-hhash-notbh-vs-bundled.md`](../tracks/light-clients/worked-example-hhash-notbh-vs-bundled.md)。

把 EIP-2935 state-hash not already BLOCKHASH / not already 156 / not already 195-bundled 正式三事（195 余量） 写成已经 已经是BLOCKHASH / 已经是不变量 156 / 已经 195 bundled，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-2935 history-hash 正式三事（195 余量），必须分开 not already BLOCKHASH、not already window-full、not already opcode-changed 三件事，不要和 195 / 156 / 157 / 1501 / 1502 糊成一句。

也不是：

- [hhash-notfill-sold-as-bundled](hhash-notfill-sold-as-bundled.md) 是 notfill 单句边界（1501），不是本页边界。
- [hhash-notsem-sold-as-bundled](hhash-notsem-sold-as-bundled.md) 是 notsem 单句边界（1502），不是本页边界。
- [bres-notacct-sold-as-bundled](bres-notacct-sold-as-bundled.md) 是 EIP-7918 blob 底价边界（201/1497），不是本页历史哈希边界。
