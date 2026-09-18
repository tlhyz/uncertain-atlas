# 模式：点名 cr2-notcre 杠

**层次**：实现 / EIP-1014 CREATE2 not already CREATE-nonce / not already sender-nonce / not already 222-bundled 正式三事（222 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-1014](https://eips.ethereum.org/EIPS/eip-1014)（Final, Core, Skinny CREATE2）。  
**对应**：[`../tracks/implementation/worked-example-cr2-notcre-vs-bundled.md`](../tracks/implementation/worked-example-cr2-notcre-vs-bundled.md)。

- **盐创建指令不是已经是按序号占址 不是已经是按发送者加序号占址：看见盐创建指令不是已经是按序号占址，不是已经是按发送者加序号占址 interchangeable / 1389 cr2-notcre interchangeable。**
- **CREATE2 is not already CREATE 不是已经能和旧式创建地址撞上：看见CREATE2 is not already CREATE，不是已经能和旧式创建地址撞上 interchangeable / 1389 cr2-notcre interchangeable。**
- **盐创建指令不是已经是按序号占址 不是已经 222 bundled：看见盐创建指令不是已经是按序号占址，不是已经 222 bundled interchangeable / 1389 cr2-notcre interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7 DELEGATECALL 正式三事（222 余量），必须分开 not already CALLCODE、not already CALL、not already 7702 三件事。
