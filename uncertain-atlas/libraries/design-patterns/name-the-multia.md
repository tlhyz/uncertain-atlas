# 模式：把 tapscript 多签描述符三件事说成三个名字

**层次**：应用 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[BIP-387](https://github.com/bitcoin/bips/blob/master/bip-0387.mediawiki)。  
**例**：[multi_a ≠ 已经是 383 那种 multi](../../tracks/implementation/worked-example-multia-vs-tr.md)。

## 三个名字

1. **只许在 tr 里：** 看见 multi_a / sortedmulti_a 不是已经是 383 那种 multi，也不是已经能当顶层。
2. **门限编码分档：** 看见门限不是已经同一套编码，也不是已经是 383 那种外层钥数界。
3. **x-only 排序：** 看见 sortedmulti_a 不是已经是 383 那种排序。

## 为什么要分开叫

官方把本页写成只产出 tapscript、只许出现在 `tr` 里，又按门限是否超过一小档写成两套写法，还把本页排序写成排 x-only 公钥。把它们叫成一个「看见又一种 multi 就已经是 383」，会把 383 那种多签和 `tr` 有没有树一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果导出 tapscript 多签描述符，先数清问的是只许在 `tr` 里、门限编码分档，还是 x-only 已经排过，再决定要不要同一次发布。
