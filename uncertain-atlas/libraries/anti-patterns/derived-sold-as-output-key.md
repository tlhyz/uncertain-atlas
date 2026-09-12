# 反模式：看见派生钥就当成已经是输出钥 / 看见不需要脚本路径就当成已经不承诺 / 看见种子备份就当成已经能找回单钥 P2TR

**层次**：应用 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[BIP-86](https://github.com/bitcoin/bips/blob/master/bip-0086.mediawiki)。  
**例**：[派生钥 ≠ 已经是输出钥](../../tracks/implementation/worked-example-derived-vs-output-key.md)。

## 塌法

1. 看见派生钥 / 看见 BIP32 路径，就当成已经是输出钥，或当成已经是链上那 32 字节。
2. 看见不需要脚本路径 / 看见单钥，就当成已经可以不微调，或当成已经没有脚本路径。
3. 看见种子备份，就当成已经能找回单钥 P2TR。
4. 看见已有描述符方案，就当成已经不必再写本页。
5. 看见同一套 44 / 49 / 84 结构，就当成已经向后兼容，或当成旧钱包已经能发现。

## 为什么会出事

官方写：派生钥先当成内部钥，输出钥是内部钥再加上对内部钥做标签微调后的点。若花费条件并不需要脚本路径，输出钥仍应当承诺一条不可花的脚本路径。许多钱包仍只用种子备份，备份里没有路径和脚本信息；本页按设计不向后兼容。

## 和相邻反模式

- [keypath-sold-as-tree](keypath-sold-as-tree.md) 是钥匙路径 ≠ 已经揭开有没有树，不是本页这条派生。
- [nested-sold-as-same-account](nested-sold-as-same-account.md) 是同一套 BIP44 账户 ≠ 已经能找回嵌套隔离见证，不是本页。
- [xpub-sold-as-spendable](xpub-sold-as-spendable.md) 是扩展公钥 ≠ 已经能花，不是本页。
