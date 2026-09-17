# 反模式：看见 multi 就当成已经按字典序排 / 看见门限就当成已经同一套上限 / 看见多把扩展钥就当成已经各自编号

**层次**：应用 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[BIP-383](https://github.com/bitcoin/bips/blob/master/bip-0383.mediawiki)。  
**例**：[multi ≠ 已经按字典序排](../../tracks/implementation/worked-example-multi-vs-sortedmulti.md)。

## 塌法

1. 看见 multi / 看见按书写顺序放钥，就当成已经是 sortedmulti，或当成已经按字典序排。
2. 看见门限 / 看见钥数，就当成已经同一套上限，或当成已经随便几把。
3. 看见套进了脚本哈希，就当成已经是顶层那三把。
4. 看见多把扩展钥 / 看见各钥自己的派生路径，就当成已经可以各走各的下标。
5. 看见本页排序，就当成已经是 67 那种地址排序。

## 为什么会出事

官方写：`multi` 按给出的顺序写钥，`sortedmulti` 在产出输出脚本时再按字典序排，而且排的是派生完之后的钥。能出现的钥数还要看外层。多把扩展钥用同一个子下标齐步变。

## 和相邻反模式

- [sorted-sold-as-one-address](sorted-sold-as-one-address.md) 是同一套钥 ≠ 已经是同一条 P2SH 地址，不是本页这条描述符表达式。
- [xpub-sold-as-spendable](xpub-sold-as-spendable.md) 是扩展公钥 ≠ 已经能花，不是本页。
- [hash-sold-as-redeem](hash-sold-as-redeem.md) 是付给脚本哈希 ≠ 已经揭开赎回，不是本页。
