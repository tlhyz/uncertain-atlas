# 反模式：看见 wpkh / wsh 就当成已经只能顶层 / 看见未压缩钥就当成已经允许 / 看见 wsh 产出就当成已经有见证脚本

**层次**：应用 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[BIP-382](https://github.com/bitcoin/bips/blob/master/bip-0382.mediawiki)。  
**例**：[wpkh / wsh ≠ 已经只能顶层](../../tracks/implementation/worked-example-wpkh-vs-compressed.md)。

## 塌法

1. 看见 wpkh / 看见 wsh，就当成已经只能顶层，或当成已经是 381 那种 `sh` 只能顶层。
2. 看见能套进 sh，就当成已经能再套进 wsh。
3. 看见未压缩钥 / 看见任意钥，就当成已经允许进 wpkh，或当成已经允许出现在 wsh 下面。
4. 看见 wsh 产出了 P2WSH 输出脚本，就当成已经有见证脚本，或当成已经是 381 那份赎回脚本。
5. 看见本页嵌套，就当成已经是 49 那种账户找回。

## 为什么会出事

官方写：`wpkh` 和 `wsh` 都可以当顶层或套进 `sh`。`wpkh` 里只能放压缩钥。`wsh` 下面任何一层出现的钥都只能产出压缩公钥。`wsh` 还会另造一份见证脚本。

## 和相邻反模式

- [pk-sold-as-toplevel](pk-sold-as-toplevel.md) 是 pk ≠ 已经和 pkh / sh 同一套放置，不是本页。
- [nested-sold-as-same-account](nested-sold-as-same-account.md) 是同一套 BIP44 账户 ≠ 已经能找回嵌套隔离见证，不是本页。
- [hash-sold-as-redeem](hash-sold-as-redeem.md) 是付给脚本哈希 ≠ 已经揭开赎回，不是本页。
