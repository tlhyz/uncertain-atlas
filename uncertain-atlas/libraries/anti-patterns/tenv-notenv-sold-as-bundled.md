# 反模式：把 EIP-2718 legacy-RLP not already envelope / not already 155 / not already signed-type 正式三事（167 余量） 写成已经 已经是类型信封 / 已经是 155 / 已经把类型签进哈希

**层次**：实现 / EIP-2718 legacy-RLP not already envelope / not already 155 / not already signed-type 正式三事（167 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-2718](https://eips.ethereum.org/EIPS/eip-2718)（Final, Core, Typed Transaction Envelope）。  
**对应**：[`../tracks/implementation/worked-example-tenv-notenv-vs-bundled.md`](../tracks/implementation/worked-example-tenv-notenv-vs-bundled.md)。

把 EIP-2718 legacy-RLP not already envelope / not already 155 / not already signed-type 正式三事（167 余量） 写成已经 已经是类型信封 / 已经是 155 / 已经把类型签进哈希，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-2718 typed-envelope 正式三事（167 余量），必须分开 not already unpacked、not already envelope、not already type-matched 三件事，不要和 167 / 161 / 158 / 1455 / 1457 糊成一句。

也不是：

- [tenv-notinner-sold-as-bundled](tenv-notinner-sold-as-bundled.md) 是 notinner 单句边界（1455），不是本页边界。
- [tenv-notrcpt-sold-as-bundled](tenv-notrcpt-sold-as-bundled.md) 是 notrcpt 单句边界（1457），不是本页边界。
- [alist-notacc-sold-as-bundled](alist-notacc-sold-as-bundled.md) 是 EIP-2930 访问列表边界（168/1452），不是本页类型信封边界。
