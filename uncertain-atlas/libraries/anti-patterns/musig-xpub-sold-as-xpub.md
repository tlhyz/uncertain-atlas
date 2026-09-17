# 反模式：看见聚合钥就当成已经是扩展公钥 / 看见合成扩展公钥就当成已经能硬化 / 看见子钥就当成已经能不带微调去签

**层次**：应用 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[BIP-328](https://github.com/bitcoin/bips/blob/master/bip-0328.mediawiki)。  
**例**：[聚合钥 ≠ 已经是扩展公钥](../../tracks/implementation/worked-example-musig-xpub-vs-aggregate.md)。

## 塌法

1. 看见 MuSig2 聚合钥 / 看见一把普通公钥，就当成已经是扩展公钥，或当成已经能按 32 那种树往下长。
2. 看见合成扩展公钥 / 看见没有聚合私钥，就当成已经能做硬化派生，或当成已经能从许多扩展公钥再聚合。
3. 看见派生出的子钥 / 看见一次签名会话，就当成已经能不带微调去签，或当成已经按 x-only 微调。
4. 看见少存了几份扩展公钥，就当成已经是脚本多签那种各自派生再拼。
5. 看见本页合成扩展公钥，就当成已经能花。

## 为什么会出事

官方写：要从明文聚合公钥另造一份合成扩展公钥。没有聚合私钥，所以只能未硬化派生。签名时所有签名人都必须把每一步派生微调以明文微调模式放进会话。

## 和相邻反模式

- [xpub-sold-as-spendable](xpub-sold-as-spendable.md) 是扩展公钥 ≠ 已经能花，不是本页。
- [derived-sold-as-output-key](derived-sold-as-output-key.md) 是派生钥 ≠ 已经是输出钥，不是本页。
- [multi-sold-as-sorted](multi-sold-as-sorted.md) 是 multi ≠ 已经按字典序排，不是本页。
