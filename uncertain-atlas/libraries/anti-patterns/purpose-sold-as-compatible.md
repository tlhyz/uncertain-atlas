# 反模式：看见 BIP32 compatible 就当成已经能互操作 / 看见自称 BIPxx compatible 就当成已经是那份结构 / 看见同一套扩展钥前缀就当成已经是比特币专用

**层次**：应用 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[BIP-43](https://github.com/bitcoin/bips/blob/master/bip-0043.mediawiki)。  
**例**：[BIP32 compatible ≠ 已经能互操作](../../tracks/implementation/worked-example-purpose-vs-compatible.md)。

## 塌法

1. 看见 BIP32 compatible，就当成已经能互操作，或当成已经是同一套逻辑结构。
2. 看见都能从同一份种子长钥，就当成已经能互相发现账户。
3. 看见自称 BIPxx compatible / 只实现了其中一部分，就当成已经是那份 BIP 写的结构。
4. 看见用途号，就当成已经支持那份 BIP 的全部能力。
5. 看见同一套扩展钥前缀，就当成已经只服务一条链，或当成已经是 BIP32 默认账户。

## 为什么会出事

官方写：多家实现都可以自称 BIP32 compatible，底下却长出不同的逻辑结构。有限结构应当另写 BIP、另给用途，而不是抽子集还挂原名。这套方案一次可以给多种币、甚至完全无关的东西长节点，所以继续用同一套前缀；默认账户支已经被占了。

## 和相邻反模式

- [xpub-sold-as-spendable](xpub-sold-as-spendable.md) 是扩展公钥 ≠ 已经能花，不是本页这条用途层。
- [keys-sold-as-scripts](keys-sold-as-scripts.md) 是备份 ≠ 已经知道脚本，不是本页。
- [miniscript-sold-as-script](miniscript-sold-as-script.md) 是分析语言 ≠ 已经上链，不是本页。
