# 反模式：看见现有多签派生习惯就当成已经要搬家 / 看见脚本类型层就当成已经是账户层 / 看见本页多签就当成已经不排序

**层次**：应用 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[BIP-48](https://github.com/bitcoin/bips/blob/master/bip-0048.mediawiki)。  
**例**：[脚本类型 ≠ 已经是账户层](../../tracks/implementation/worked-example-script-type-vs-account.md)。

## 塌法

1. 看见现有多签派生习惯 / 看见本页，就当成已经要搬家，或当成已经可以改路径。
2. 看见写了标准，就当成已经支持本页的钱包必须改。
3. 看见脚本类型层 / 看见账户层，就当成已经是同一层。
4. 看见本页，就当成已经把以后的脚本类型都写死，或当成每来一种脚本都要再写一份 BIP。
5. 看见本页多签 / 看见多签路径，就当成已经可以按随便的顺序拼，或当成已经是单签账户发现。

## 为什么会出事

官方写：本页要维持现有真实用法，不做破坏性改动，免得现有用户丢币。脚本类型另开一层，好给以后的脚本往下加。支持本页就自带按确定性排序公钥来派生所有可能的多签地址和脚本。

## 和相邻反模式

- [nested-sold-as-same-account](nested-sold-as-same-account.md) 是嵌套单签 ≠ 已经能挂在旧账户上找回，不是本页这条多签层次。
- [purpose-sold-as-compatible](purpose-sold-as-compatible.md) 是 BIP32 compatible ≠ 已经能互操作，不是本页。
- [account-sold-as-discovered](account-sold-as-discovered.md) 是余额为零 ≠ 已经发现完，不是本页。
