# 模式：点名 retc-nottx 杠

**层次**：实现 / EIP-170 oog-fail not already whole-tx-illegal / not already leftover-gas / not already 177 正式三事（185 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-170](https://eips.ethereum.org/EIPS/eip-170)（Final, Core, Contract code size limit）。  
**对应**：[`../tracks/implementation/worked-example-retc-nottx-vs-bundled.md`](../tracks/implementation/worked-example-retc-nottx-vs-bundled.md)。

- **这次失败是耗尽气不是已经整笔非法 不是已经整笔非法：看见这次失败是耗尽气不是已经整笔非法，不是已经整笔非法 interchangeable / 1441 retc-nottx interchangeable。**
- **OOG fail is not already whole-tx illegal 不是已经是带回剩余气的回滚：看见OOG fail is not already whole-tx illegal，不是已经是带回剩余气的回滚 interchangeable / 1441 retc-nottx interchangeable。**
- **这次失败是耗尽气不是已经整笔非法 不是已经是不变量 177：看见这次失败是耗尽气不是已经整笔非法，不是已经是不变量 177 interchangeable / 1441 retc-nottx interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-170 returned 正式三事（185 余量），必须分开 not already initcode-bound、not already whole-tx-illegal、not already free-disk 三件事。
