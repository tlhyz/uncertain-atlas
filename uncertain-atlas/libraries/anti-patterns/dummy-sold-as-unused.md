# 反模式：看见多余栈元素就当成已经随便填 / 看见隔离见证就当成已经没有这条延展 / 看见策略已经要就当成已经是共识

**层次**：共识 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[BIP-147](https://github.com/bitcoin/bips/blob/master/bip-0147.mediawiki)。  
**例**：[dummy ≠ 已经随便填](../../tracks/implementation/worked-example-dummy-vs-empty.md)。

## 塌法

1. 看见多重签验过，就当成已经看过 dummy，或当成 dummy 已经随便填。
2. 看见 dummy 不是空，就当成已经合法。
3. 看见隔离见证已经开 / txid 不能被第三方改，就当成已经没有这条延展。
4. 看见转发策略已经要空 dummy，就当成共识已经要。
5. 看见 BIP-62 菜谱，就当成已经是本页这一条。

## 为什么会出事

官方写：dummy 必须是空字节，否则脚本立刻为假。隔离见证之后这条仍改 wtxid，并可能伤紧凑块。策略早就执行不是共识已经要。本页是从 BIP-62 里抽出来的一条，不是整份菜谱。

## 和相邻反模式

- [valid-sold-as-der](valid-sold-as-der.md) 是验得过 ≠ 已经是严格 DER，不是本页这条 dummy。
- [txid-sold-as-wtxid](txid-sold-as-wtxid.md) 是两个哈希不是一回事，不是本页。
- [policy-sold-as-consensus](policy-sold-as-consensus.md) 是策略大门总原则，不是本页这条空 dummy。
