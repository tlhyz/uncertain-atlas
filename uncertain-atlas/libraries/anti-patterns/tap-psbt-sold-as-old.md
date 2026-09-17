# 反模式：看见旧 PSBT 栏就当成已经能装 Taproot / 看见输出脚本里的钥就当成已经是内部钥 / 看见 Taproot 输入就当成已经必须带整笔前交易

**层次**：应用 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[BIP-371](https://github.com/bitcoin/bips/blob/master/bip-0371.mediawiki)。  
**例**：[旧 PSBT 栏 ≠ 已经能装 Taproot](../../tracks/implementation/worked-example-tap-psbt-vs-old.md)。

## 塌法

1. 看见旧 PSBT 栏 / 看见 174 那套字段，就当成已经能装 Taproot，或当成已经能签 Taproot 输入。
2. 看见输出脚本里的钥 / 看见钥匙路径那张签，就当成已经是内部钥，或当成已经同一把钥。
3. 看见 Taproot 输入 / 看见 174 建议带整笔前交易，就当成已经必须带整笔前交易，或当成已经和其它输入同一套 UTXO 栏。
4. 看见旧软件会忽略新栏，就当成已经能签。
5. 看见本页内部钥，就当成已经是 86 那种派生钥。

## 为什么会出事

官方写：现有 PSBT 栏没法支持 Taproot。钥匙路径签直接对应输出脚本里的公钥；内部钥不一定就是那把。Taproot 签名会承诺金额和输出脚本，所以可以只带见证 UTXO。

## 和相邻反模式

- [psbt-sold-as-broadcast](psbt-sold-as-broadcast.md) 是看见包 ≠ 已经能广播，不是本页。
- [psbtv2-sold-as-v0](psbtv2-sold-as-v0.md) 是后继包 ≠ 已经是旧版固定未签交易，不是本页。
- [derived-sold-as-output-key](derived-sold-as-output-key.md) 是派生钥 ≠ 已经是输出钥，不是本页。
- [keypath-sold-as-tree](keypath-sold-as-tree.md) 是钥匙路径 ≠ 已经揭开有没有树，不是本页。
