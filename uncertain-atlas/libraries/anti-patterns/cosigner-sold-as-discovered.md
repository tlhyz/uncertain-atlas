# 反模式：看见共享主公钥就当成已经是本页 / 看见能独立长地址就当成已经能独立签 / 看见前面分支没有交易就当成已经发现完

**层次**：应用 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[BIP-45](https://github.com/bitcoin/bips/blob/master/bip-0045.mediawiki)。  
**例**：[共享主公钥 ≠ 已经是本页](../../tracks/implementation/worked-example-cosigner-vs-discovered.md)。

## 塌法

1. 看见共享主公钥 / 看见扩展公钥，就当成已经是本页，或当成已经够了。
2. 看见能独立长地址 / 看见不必通信就能长地址，就当成已经能独立造交易，或当成已经能独立签名。
3. 看见同一条路径，就当成已经是同一个人的钥。
4. 看见前面的联合签名人分支没有交易，就当成已经发现完，或当成已经可以只扫第一支。
5. 看见余额为零，就当成已经没有这一支，或当成已经是 BIP-44 那套停搜。

## 为什么会出事

官方写：各方不共享主公钥，只共享硬化用途层扩展公钥。长地址不应当要求各方通信；造交易和签名要求通信。发现看过往、不看余额；和 BIP-44 相反，即使前面的分支没有交易，也必须检查每一个联合签名人分支。

## 和相邻反模式

- [sorted-sold-as-one-address](sorted-sold-as-one-address.md) 是同一套钥 ≠ 已经是同一条 P2SH 地址，不是本页这条多方结构。
- [account-sold-as-discovered](account-sold-as-discovered.md) 是余额为零 ≠ 已经发现完那句账户发现，不是本页每一支都要查。
- [xpub-sold-as-spendable](xpub-sold-as-spendable.md) 是扩展公钥 ≠ 已经能花，不是本页。
