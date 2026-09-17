# 反模式：看见同一份种子就当成已经是同一条币 / 看见下一个账户号就当成已经有过往 / 看见余额为零就当成已经发现完

**层次**：应用 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[BIP-44](https://github.com/bitcoin/bips/blob/master/bip-0044.mediawiki)。  
**例**：[账户 ≠ 已经发现完](../../tracks/implementation/worked-example-account-vs-discovered.md)。

## 塌法

1. 看见同一份种子 / 同一颗主节点，就当成已经是同一条币，或当成已经可以混用地址。
2. 看见下一个账户号 / 去开新账户，就当成上一户已经有过往，或当成两户已经可以混花。
3. 看见余额为零，就当成已经没有这一户，或当成已经发现完。
4. 看见一串没用过的地址，就当成链上已经没有后面的付款。
5. 看见只扫了外链，就当成内链已经一起发现完。

## 为什么会出事

官方写：一颗主节点可以给无限种独立的币用，但挤在同一片空间有坏处。开新户应当等上一户已经有交易过往。发现看过往，不看余额；总额可以是零，发现仍会继续。只扫外链，因为内链只收从对应外链过来的币。

## 和相邻反模式

- [purpose-sold-as-compatible](purpose-sold-as-compatible.md) 是 BIP32 compatible ≠ 已经能互操作，不是本页这条账户发现。
- [xpub-sold-as-spendable](xpub-sold-as-spendable.md) 是扩展公钥 ≠ 已经能花，不是本页。
- [keys-sold-as-scripts](keys-sold-as-scripts.md) 是备份 ≠ 已经知道脚本，不是本页。
