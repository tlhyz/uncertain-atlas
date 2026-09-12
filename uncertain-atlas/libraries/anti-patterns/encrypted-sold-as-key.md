# 反模式：看见加密私钥记录就当成已经能用 / 看见厂家代生成就当成已经能兑 / 看见地址哈希片段就当成已经是地址

**层次**：应用 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[BIP-38](https://github.com/bitcoin/bips/blob/master/bip-0038.mediawiki)。  
**例**：[加密私钥记录 ≠ 已经能用](../../tracks/implementation/worked-example-encrypted-key-vs-usable.md)。

## 塌法

1. 看见加密私钥记录 / 看见「还缺一样才能用」，就当成已经是私钥，或当成已经能签。
2. 看见厂家代生成 / 看见椭圆曲线倍点那条路，就当成已经和「拿已知私钥再加密」是同一条，或当成厂家已经能兑。
3. 看见明文里的地址哈希片段 / 看见这种打印前缀，就当成已经是地址，或当成已经解开。
4. 看见本页已部署，就当成已经推荐拿来当第一版备份。
5. 看见口令，就当成已经是助记词那种口令。

## 为什么会出事

官方写：记录里有凑回私钥所需的信息，就缺口令。共享生成那条路，厂家只知道从口令派生出来的一串。明文哈希片段只能按一定概率对上地址；完整地址要解开之后才有。评论摘要写：一致不鼓励实现。

## 和相邻反模式

- [mnemonic-sold-as-seed](mnemonic-sold-as-seed.md) 是助记词 ≠ 已经是种子，不是本页这种加密私钥记录。
- [xpub-sold-as-spendable](xpub-sold-as-spendable.md) 是扩展公钥 ≠ 已经能花，不是本页。
- [address-sold-as-utxo](address-sold-as-utxo.md) 是地址串 ≠ 已经有输出，不是本页这种明文哈希片段。
- [signed-message-sold-as-control](signed-message-sold-as-control.md) 是签过 ≠ 已经控制资金，不是本页。
