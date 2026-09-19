# 反模式：把 EIP-2718 type-byte not already unpacked / not already 1559 / not already 167-bundled 正式三事（167 余量） 写成已经 已经解开内层字段 / 已经是 1559 / 已经 167 bundled

**层次**：实现 / EIP-2718 type-byte not already unpacked / not already 1559 / not already 167-bundled 正式三事（167 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-2718](https://eips.ethereum.org/EIPS/eip-2718)（Final, Core, Typed Transaction Envelope）。  
**对应**：[`../tracks/implementation/worked-example-tenv-notinner-vs-bundled.md`](../tracks/implementation/worked-example-tenv-notinner-vs-bundled.md)。

把 EIP-2718 type-byte not already unpacked / not already 1559 / not already 167-bundled 正式三事（167 余量） 写成已经 已经解开内层字段 / 已经是 1559 / 已经 167 bundled，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-2718 typed-envelope 正式三事（167 余量），必须分开 not already unpacked、not already envelope、not already type-matched 三件事，不要和 167 / 158 / 168 / 1456 / 1457 糊成一句。

也不是：

- [tenv-notenv-sold-as-bundled](tenv-notenv-sold-as-bundled.md) 是 notenv 单句边界（1456），不是本页边界。
- [tenv-notrcpt-sold-as-bundled](tenv-notrcpt-sold-as-bundled.md) 是 notrcpt 单句边界（1457），不是本页边界。
- [alist-notacc-sold-as-bundled](alist-notacc-sold-as-bundled.md) 是 EIP-2930 访问列表边界（168/1452），不是本页类型信封边界。
