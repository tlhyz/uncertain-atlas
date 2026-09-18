# 模式：点名 stcall-notxfer 杠

**层次**：实现 / EIP-214 zero-value-CALL not already static-flag / not already readonly / not already 214-bundled 正式三事（178 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-214](https://eips.ethereum.org/EIPS/eip-214)（Final, Core, STATICCALL）。  
**对应**：[`../tracks/implementation/worked-example-stcall-notxfer-vs-bundled.md`](../tracks/implementation/worked-example-stcall-notxfer-vs-bundled.md)。

- **没转账的普通调用不是已经是静态帧 不是已经打开静态旗：看见没转账的普通调用不是已经是静态帧，不是已经打开静态旗 interchangeable / 1384 stcall-notxfer interchangeable。**
- **zero-value CALL is not already static 不是已经只读：看见zero-value CALL is not already static，不是已经只读 interchangeable / 1384 stcall-notxfer interchangeable。**
- **没转账的普通调用不是已经是静态帧 不是已经 214 bundled：看见没转账的普通调用不是已经是静态帧，不是已经 214 bundled interchangeable / 1384 stcall-notxfer interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7 DELEGATECALL 正式三事（178 余量），必须分开 not already CALLCODE、not already CALL、not already 7702 三件事。
