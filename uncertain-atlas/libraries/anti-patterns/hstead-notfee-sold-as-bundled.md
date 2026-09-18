# 反模式：把 EIP-2 create-fee not already CREATE-repriced / not already opcode-gas / not already 234-bundled 正式四事（234 余量） 写成已经 已经改了 CREATE / 已经重定价操作码 / 已经 Homestead 四件事 bundled

**层次**：实现 / EIP-2 create-fee not already CREATE-repriced / not already opcode-gas / not already 234-bundled 正式四事（234 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-2](https://eips.ethereum.org/EIPS/eip-2)（Final, Core, Homestead）。  
**对应**：[`../tracks/implementation/worked-example-hstead-notfee-vs-bundled.md`](../tracks/implementation/worked-example-hstead-notfee-vs-bundled.md)。

把 EIP-2 create-fee not already CREATE-repriced / not already opcode-gas / not already 234-bundled 正式四事（234 余量） 写成已经 已经改了 CREATE / 已经重定价操作码 / 已经 Homestead 四件事 bundled，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal Usage SHOULD Accept default strategy 正式四事（234 余量），必须分开 not already CREATE-repriced、not already ECRECOVER-rejects、not already code-limit、not already bomb-gone，不要和 234 / 233 / 160 / 1347 / 1348 糊成一句。

也不是：

- [hstead-notsig-sold-as-bundled](hstead-notsig-sold-as-bundled.md) 是 notsig 单句边界（1347），不是本页边界。
- [hstead-notfail-sold-as-bundled](hstead-notfail-sold-as-bundled.md) 是 notfail 单句边界（1348），不是本页边界。
- [ewbcast-notlc-sold-as-bundled](ewbcast-notlc-sold-as-bundled.md) 是 ExtWhenBcast 广播不是 last_commit 边界（513/1345），不是本页 Homestead 四件事边界。
