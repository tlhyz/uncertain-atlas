# 反模式：看见同一套 BIP44 账户就当成已经能找回嵌套隔离见证 / 看见专用账户就当成已经向后兼容 / 看见账户出现了就当成已经不用核余额

**层次**：应用 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[BIP-49](https://github.com/bitcoin/bips/blob/master/bip-0049.mediawiki)。  
**例**：[嵌套账户 ≠ 已经能挂在旧账户上找回](../../tracks/implementation/worked-example-nested-vs-same-account.md)。

## 塌法

1. 看见同一套 BIP44 账户 / 同一批钥再加隔离见证写法，就当成已经能找回这些币。
2. 看见旧账户还在，就当成嵌套隔离见证已经找回。
3. 看见专用账户 / 换了用途，就当成已经是原来那户，或当成已经向后兼容。
4. 看见账户出现了 / 看见有余额，就当成已经齐，或当成已经不用核余额。
5. 看见账户完全不出现，就当成币已经没了。

## 为什么会出事

官方写：把本页兼容的种子导进不会本页的钱包，账户也许会出现，可是也可能漏掉一部分未花输出。所以故意另开专用账户，要么出现、要么完全不出现，用户不必再核一遍余额。不会本页的钱包根本发现不了这些账户。

## 和相邻反模式

- [account-sold-as-discovered](account-sold-as-discovered.md) 是余额为零 ≠ 已经发现完，不是本页这条嵌套找回。
- [purpose-sold-as-compatible](purpose-sold-as-compatible.md) 是 BIP32 compatible ≠ 已经能互操作，不是本页。
- [xpub-sold-as-spendable](xpub-sold-as-spendable.md) 是扩展公钥 ≠ 已经能花，不是本页。
- [hash-sold-as-redeem](hash-sold-as-redeem.md) 是付给哈希 ≠ 已经揭开赎回，不是本页这条派生。
