# 反模式：把 EIP-2028 cheaper not already no-delay / not already no-security-change / not already 197 正式三事（226 余量） 写成已经 已经不伤网络延迟 / 安全 / 已经不改安全 / 已经是不变量 197

**层次**：实现 / EIP-2028 cheaper not already no-delay / not already no-security-change / not already 197 正式三事（226 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-2028](https://eips.ethereum.org/EIPS/eip-2028)（Final, Core, Transaction data gas cost reduction）。  
**对应**：[`../tracks/implementation/worked-example-cdcut-notsafe-vs-bundled.md`](../tracks/implementation/worked-example-cdcut-notsafe-vs-bundled.md)。

把 EIP-2028 cheaper not already no-delay / not already no-security-change / not already 197 正式三事（226 余量） 写成已经 已经不伤网络延迟 / 安全 / 已经不改安全 / 已经是不变量 197，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-2028 calldata-cut 正式三事（226 余量），必须分开 not already zero-cut、not already no-block-cap、not already no-delay 三件事，不要和 226 / 197 / 225 / 1422 / 1423 糊成一句。

也不是：

- [cdcut-notzero-sold-as-bundled](cdcut-notzero-sold-as-bundled.md) 是 notzero 单句边界（1422），不是本页边界。
- [cdcut-notcap-sold-as-bundled](cdcut-notcap-sold-as-bundled.md) 是 notcap 单句边界（1423），不是本页边界。
- [nmet-not1153-sold-as-bundled](nmet-not1153-sold-as-bundled.md) 是 EIP-2200 净计量边界（225/1419），不是本页 calldata 降价边界。
