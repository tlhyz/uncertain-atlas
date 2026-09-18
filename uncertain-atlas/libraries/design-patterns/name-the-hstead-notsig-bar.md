# 模式：点名 hstead-notsig 杠

**层次**：实现 / EIP-2 high-s not already ECRECOVER-rejects / not already BIP-66 / not already EIP-155 正式四事（234 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-2](https://eips.ethereum.org/EIPS/eip-2)（Final, Core, Homestead）。  
**对应**：[`../tracks/implementation/worked-example-hstead-notsig-vs-bundled.md`](../tracks/implementation/worked-example-hstead-notsig-vs-bundled.md)。

- **交易拒高 s 不是已经让预编译拒 不是已经让 ECRECOVER 拒高 s：看见交易拒高 s 不是已经让预编译拒，不是已经让 ECRECOVER 拒高 s interchangeable / 1347 hstead-notsig interchangeable。**
- **tx rejects high s is not ECRECOVER rejects 不是已经是比特币 DER 低 s：看见tx rejects high s is not ECRECOVER rejects，不是已经是比特币 DER 低 s interchangeable / 1347 hstead-notsig interchangeable。**
- **交易拒高 s 不是已经让预编译拒 不是已经把链标识写进签名：看见交易拒高 s 不是已经让预编译拒，不是已经把链标识写进签名 interchangeable / 1347 hstead-notsig interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Homestead 硬分叉正式四事（234 余量），必须分开 not already CREATE-repriced、not already ECRECOVER-rejects、not already code-limit、not already bomb-gone。
