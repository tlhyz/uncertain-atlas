# 反模式：看见旧 PSBT 栏就当成已经能装 MuSig2 / 看见聚合钥栏就当成已经是输出钥 / 看见参与者钥就当成已经有部分签

**层次**：应用 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[BIP-373](https://github.com/bitcoin/bips/blob/master/bip-0373.mediawiki)。  
**例**：[旧 PSBT 栏 ≠ 已经能装 MuSig2](../../tracks/implementation/worked-example-musig-psbt-vs-tap.md)。

## 塌法

1. 看见旧 PSBT 栏 / 看见 371 那套 Taproot 栏，就当成已经能装 MuSig2，或当成已经能走完多轮。
2. 看见聚合钥栏 / 看见压缩聚合钥，就当成已经是 Taproot 输出钥，或当成已经是内部钥，或当成已经是 x-only。
3. 看见参与者钥 / 看见 nonce 栏，就当成已经有部分签，或当成已经是 BIP-340 那张签。
4. 看见部分签齐了，就当成已经抽出、已经能广播。
5. 看见本页聚合钥，就当成已经是合成扩展公钥。

## 为什么会出事

官方写：现有工作包栏没法支持 MuSig2，因为它引入了新概念，还要多几轮通信。栏里的聚合钥不一定出现在输出钥、内部钥或脚本里。nonce 栏和部分签栏里的参与者公钥不是内部钥，也不是派生出它的那把聚合钥。名单、nonce、部分签、最后那张 BIP-340 签是四步。

## 和相邻反模式

- [tap-psbt-sold-as-old](tap-psbt-sold-as-old.md) 是旧 PSBT 栏 ≠ 已经能装 Taproot，不是本页。
- [musig-xpub-sold-as-xpub](musig-xpub-sold-as-xpub.md) 是聚合钥 ≠ 已经是扩展公钥，不是本页。
- [psbt-sold-as-broadcast](psbt-sold-as-broadcast.md) 是工作包 ≠ 已经能广播，不是本页。
