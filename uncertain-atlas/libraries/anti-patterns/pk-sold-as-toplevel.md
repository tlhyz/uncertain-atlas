# 反模式：看见 pk 就当成已经和 pkh / sh 同一套放置 / 看见 sh 产出就当成已经有赎回脚本 / 看见熟悉脚本就当成已经能互操作

**层次**：应用 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[BIP-381](https://github.com/bitcoin/bips/blob/master/bip-0381.mediawiki)。  
**例**：[pk ≠ 已经和 pkh / sh 同一套放置](../../tracks/implementation/worked-example-pk-vs-toplevel.md)。

## 塌法

1. 看见 pk / 看见写在某一层，就当成已经是 pkh 那种放置，或当成已经能套进任意外层。
2. 看见脚本表达式，就当成已经能再套一层 sh。
3. 看见 sh 产出了 P2SH 输出脚本，就当成已经有赎回脚本，或当成已经能花。
4. 看见熟悉的标准脚本 / 看见旧节点认得输出，就当成已经能读这份描述符，或当成已经不必再写本页。
5. 看见本页赎回脚本，就当成已经是 16 那种哈希。

## 为什么会出事

官方写：`pk` 可以出现在任何一层，`pkh` 可以当顶层或套进 `sh` / `wsh`，`sh` 只能当顶层。`sh` 还会另造一份赎回脚本。这些是全新的描述符，和任何实现都不兼容；产出的脚本眼熟不是已经能互操作。

## 和相邻反模式

- [hash-sold-as-redeem](hash-sold-as-redeem.md) 是付给脚本哈希 ≠ 已经揭开赎回，不是本页这条描述符表达式。
- [tr-sold-as-tree](tr-sold-as-tree.md) 是 tr 没有树 ≠ 已经有脚本路径，不是本页。
- [multi-sold-as-sorted](multi-sold-as-sorted.md) 是 multi ≠ 已经按字典序排，不是本页。
