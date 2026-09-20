# 模式：点名 shft-notsdiv 杠

**层次**：实现 / EIP-145 SAR not already signed-div / not already same-rounding / not already same-operand-order 正式三事（231 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-145](https://eips.ethereum.org/EIPS/eip-145)（Final, Core, bitwise shifting）。  
**对应**：[`../tracks/implementation/worked-example-shft-notsdiv-vs-bundled.md`](../tracks/implementation/worked-example-shft-notsdiv-vs-bundled.md)。

- **算术右移不是已经是有符号除 不是已经是有符号除：看见算术右移不是已经是有符号除，不是已经是有符号除 interchangeable / 1405 shft-notsdiv interchangeable。**
- **SAR is not already signed division 不是已经是同一条舍入：看见SAR is not already signed division，不是已经是同一条舍入 interchangeable / 1405 shft-notsdiv interchangeable。**
- **算术右移不是已经是有符号除 不是已经和加减同一套操作数顺序：看见算术右移不是已经是有符号除，不是已经和加减同一套操作数顺序 interchangeable / 1405 shft-notsdiv interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-145 SHIFT 正式三事（231 余量），必须分开 not already arith-composed、not already signed-div、not already bitfield-product 三件事。
