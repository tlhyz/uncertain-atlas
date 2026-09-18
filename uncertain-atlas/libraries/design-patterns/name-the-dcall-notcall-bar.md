# 模式：点名 dcall-notcall 杠

**层次**：实现 / EIP-7 parent-sender not already CALL / not already stipend / not already creates-account 正式三事（233 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-7](https://eips.ethereum.org/EIPS/eip-7)（Final, Core, Homestead, DELEGATECALL）。  
**对应**：[`../tracks/implementation/worked-example-dcall-notcall-vs-bundled.md`](../tracks/implementation/worked-example-dcall-notcall-vs-bundled.md)。

- **父作用域发送者传到子作用域不是已经是普通 CALL 不是已经是普通 CALL：看见父作用域发送者传到子作用域不是已经是普通 CALL，不是已经是普通 CALL interchangeable / 1378 dcall-notcall interchangeable。**
- **parent sender to child is not already CALL 不是已经有 CALL 那笔津贴：看见parent sender to child is not already CALL，不是已经有 CALL 那笔津贴 interchangeable / 1378 dcall-notcall interchangeable。**
- **父作用域发送者传到子作用域不是已经是普通 CALL 不是已经因此创建账户：看见父作用域发送者传到子作用域不是已经是普通 CALL，不是已经因此创建账户 interchangeable / 1378 dcall-notcall interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7 DELEGATECALL 正式三事（233 余量），必须分开 not already CALLCODE、not already CALL、not already 7702 三件事。
