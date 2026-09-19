# 反模式：把 EIP-2930 outside-list not already forbidden / not already illegal / not already 1559 正式三事（168 余量） 写成已经 已经不能碰 / 已经非法 / 已经是 1559

**层次**：实现 / EIP-2930 outside-list not already forbidden / not already illegal / not already 1559 正式三事（168 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-2930](https://eips.ethereum.org/EIPS/eip-2930)（Final, Core, Optional access lists）。  
**对应**：[`../tracks/implementation/worked-example-alist-notban-vs-bundled.md`](../tracks/implementation/worked-example-alist-notban-vs-bundled.md)。

把 EIP-2930 outside-list not already forbidden / not already illegal / not already 1559 正式三事（168 余量） 写成已经 已经不能碰 / 已经非法 / 已经是 1559，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-2930 listed 正式三事（168 余量），必须分开 not already accessed、not already forbidden、not already ran-read 三件事，不要和 168 / 158 / 167 / 1452 / 1454 糊成一句。

也不是：

- [alist-notacc-sold-as-bundled](alist-notacc-sold-as-bundled.md) 是 notacc 单句边界（1452），不是本页边界。
- [alist-notread-sold-as-bundled](alist-notread-sold-as-bundled.md) 是 notread 单句边界（1454），不是本页边界。
- [cwarm-notwarm-sold-as-bundled](cwarm-notwarm-sold-as-bundled.md) 是 EIP-2929 冷热边界（169/1449），不是本页访问列表边界。
