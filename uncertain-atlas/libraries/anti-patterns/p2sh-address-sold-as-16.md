# 反模式：看见本页这种地址就当成已经是 16 / 看见旧软件报无效就当成已经付过 / 看见只有地址就当成已经知道付给谁

**层次**：应用 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[BIP-13](https://github.com/bitcoin/bips/blob/master/bip-0013.mediawiki)。  
**例**：[本页这种地址 ≠ 已经是赎回脚本](../../tracks/implementation/worked-example-p2sh-address-vs-redeem.md)。

## 塌法

1. 看见本页这种地址 / 看见编进去的是脚本哈希，就当成已经是赎回脚本，或当成已经是 16。
2. 看见旧实现拿到本页这种地址 / 看见它报无效并拒绝造交易，就当成已经付过，或当成已经懂了付给脚本哈希。
3. 看见只有本页这种地址 / 看见地址上没有身份，就当成已经确定付给谁。
4. 看见本页已部署，就当成付款体验已经齐。
5. 看见这种地址，就当成已经是 Bech32 那种原生见证地址。

## 为什么会出事

官方写：本页编的是脚本哈希，不是公钥哈希，也不是花费时揭开赎回的那条规则。旧实现拿到会报无效并拒绝造交易。地址本身没有身份；本页不是一次解决全部好用或安全问题。

## 和相邻反模式

- [hash-sold-as-redeem](hash-sold-as-redeem.md) 是链上哈希 ≠ 已经揭开赎回，不是本页这种地址写法。
- [address-sold-as-utxo](address-sold-as-utxo.md) 是 Bech32 地址串 ≠ 已经有输出，不是本页。
- [sorted-sold-as-one-address](sorted-sold-as-one-address.md) 是同一套钥 ≠ 已经是同一条 P2SH 地址，不是本页。
- [encrypted-sold-as-key](encrypted-sold-as-key.md) 是加密私钥记录 ≠ 已经能用，不是本页。
