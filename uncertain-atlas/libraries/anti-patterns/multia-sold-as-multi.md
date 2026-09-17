# 反模式：看见 multi_a 就当成已经是 383 那种 multi / 看见门限就当成已经同一套编码 / 看见 sortedmulti_a 就当成已经是 383 那种排序

**层次**：应用 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[BIP-387](https://github.com/bitcoin/bips/blob/master/bip-0387.mediawiki)。  
**例**：[multi_a ≠ 已经是 383 那种 multi](../../tracks/implementation/worked-example-multia-vs-tr.md)。

## 塌法

1. 看见 multi_a / 看见 sortedmulti_a，就当成已经是 383 那种 multi，或当成已经能当顶层，或当成已经能套进 sh / wsh。
2. 看见门限 / 看见钥数，就当成已经同一套编码，或当成已经是 383 那种外层钥数界。
3. 看见 sortedmulti_a / 看见按字典序排，就当成已经是 383 那种排序，或当成已经排的是同一类钥。
4. 看见本页能进 tr，就当成已经有脚本路径。

## 为什么会出事

官方写：这两种表达式只产出 tapscript，也只允许出现在 `tr` 里面。产出的脚本还要看门限落在哪一档。`sortedmulti_a` 排的是派生完之后的 x-only 公钥。

## 和相邻反模式

- [multi-sold-as-sorted](multi-sold-as-sorted.md) 是 multi ≠ 已经按字典序排，不是本页这条 tapscript 表达式。
- [tr-sold-as-tree](tr-sold-as-tree.md) 是 tr 没有树 ≠ 已经有脚本路径，不是本页。
- [wpkh-sold-as-toplevel](wpkh-sold-as-toplevel.md) 是 wpkh / wsh ≠ 已经只能顶层，不是本页。
