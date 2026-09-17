# 反模式：看见 combo 就当成已经一种脚本 / 看见未压缩钥就当成已经带齐见证对 / 看见一份 combo 就当成已经是一份钱包策略

**层次**：应用 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[BIP-384](https://github.com/bitcoin/bips/blob/master/bip-0384.mediawiki)。  
**例**：[combo ≠ 已经一种脚本](../../tracks/implementation/worked-example-combo-vs-one-script.md)。

## 塌法

1. 看见 combo / 看见一把钥，就当成已经能套进 sh / wsh，或当成已经是一种输出脚本。
2. 看见未压缩钥 / 看见总是那两份旧脚本，就当成已经带齐见证对，或当成已经固定四份。
3. 看见一份 combo 产出两份或四份脚本，就当成已经是一份钱包策略，或当成已经把 381 / 382 那几条写齐。
4. 看见产出的脚本眼熟，就当成已经能读这份描述符。
5. 看见本页 combo，就当成已经是描述符已经是地址。

## 为什么会出事

官方写：`combo` 只能当顶层，只吃一把钥。永远产出 P2PK 和 P2PKH；只有压缩钥才再产出见证那一对。一份 combo 按这把钥产出两份或四份输出脚本，不是一个账户所需的全部描述符。

## 和相邻反模式

- [pk-sold-as-toplevel](pk-sold-as-toplevel.md) 是 pk ≠ 已经和 pkh / sh 同一套放置，不是本页。
- [wpkh-sold-as-toplevel](wpkh-sold-as-toplevel.md) 是 wpkh / wsh ≠ 已经只能顶层，不是本页。
- [policy-sold-as-descriptor](policy-sold-as-descriptor.md) 是钱包策略 ≠ 已经是一条描述符，不是本页。
