# 反模式：看见付款 URI 就当成已经授权 / 已经付了 / 路径空就已经没有指示

**层次**：生命周期 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[BIP-321](https://github.com/bitcoin/bips/blob/master/bip-0321.mediawiki)。  
**例**：[付款 URI ≠ 已经授权](../../tracks/lifecycle/worked-example-uri-vs-authorized.md)。

## 塌法

1. 看见付款 URI，就当成已经授权，或当成已经付了，或当成已经广播。
2. 看见路径没有链上地址，就当成已经没有付款指示，或当成已经非法。
3. 看见路径上有地址，就当成已经只有这一种付法，或当成已经付到链上。
4. 看见不认识的必选参数，就当成已经能付；看见打开了回执，就当成已经确认。
5. 看见本页，就当成已经写了远程取单，或当成已经是地址串。

## 为什么会出事

官方写：没有用户授权，不得按 URI 行事。路径可以空，只要查询里至少有一条指示。不认识的必选参数让整条非法。回执不是已经确认，也不得打开浏览器方案。本页替换 BIP-21，不是已经覆盖远程取单。

## 和相邻反模式

- [uri-fetch-sold-as-verify](uri-fetch-sold-as-verify.md) 是远程取单 ≠ 已经验证，不是本页这条 URI 方案。
- [address-sold-as-utxo](address-sold-as-utxo.md) 是看见地址串 ≠ 已经有输出，不是本页。
- [psbt-sold-as-broadcast](psbt-sold-as-broadcast.md) 是看见部分签名包 ≠ 已经能广播，不是本页。
