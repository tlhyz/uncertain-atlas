# 反模式：把 EIP-145 SAR not already signed-div / not already same-rounding / not already same-operand-order 正式三事（231 余量） 写成已经 已经是有符号除 / 已经是同一条舍入 / 已经和加减同一套操作数顺序

**层次**：实现 / EIP-145 SAR not already signed-div / not already same-rounding / not already same-operand-order 正式三事（231 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-145](https://eips.ethereum.org/EIPS/eip-145)（Final, Core, bitwise shifting）。  
**对应**：[`../tracks/implementation/worked-example-shft-notsdiv-vs-bundled.md`](../tracks/implementation/worked-example-shft-notsdiv-vs-bundled.md)。

把 EIP-145 SAR not already signed-div / not already same-rounding / not already same-operand-order 正式三事（231 余量） 写成已经 已经是有符号除 / 已经是同一条舍入 / 已经和加减同一套操作数顺序，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-145 SHIFT 正式三事（231 余量），必须分开 not already arith-composed、not already signed-div、not already bitfield-product 三件事，不要和 231 / 216 / 230 / 1404 / 1406 糊成一句。

也不是：

- [shft-notarith-sold-as-bundled](shft-notarith-sold-as-bundled.md) 是 notarith 单句边界（1404），不是本页边界。
- [shft-notpack-sold-as-bundled](shft-notpack-sold-as-bundled.md) 是 notpack 单句边界（1406），不是本页边界。
- [bbfee-not3198-sold-as-bundled](bbfee-not3198-sold-as-bundled.md) 是 EIP-7516 blob 基础费边界（219/1401），不是本页 SHIFT 边界。
