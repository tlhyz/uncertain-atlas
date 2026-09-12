# 反模式：看见同一交易标识就当成已经唯一 / 已经同一组可花输出 / 已经不怕被覆盖

**层次**：共识 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[BIP-30](https://github.com/bitcoin/bips/blob/master/bip-0030.mediawiki)。  
**例**：[同一交易标识 ≠ 已经唯一](../../tracks/consensus/worked-example-duplicate-txid-vs-unique.md)。

## 塌法

1. 看见同一个交易标识，就当成已经唯一，或当成已经同一组可花输出。
2. 看见许多确认，就当成已经不怕被覆盖，或当成已经不能打回一次确认。
3. 看见后来又出现已经花光的那条标识，就当成已经非法，或当成旧输出又活了。
4. 看见本页，就当成已经保证所有 coinbase 标识都唯一。
5. 看见重组，就当成可花集合已经自动不变。

## 为什么会出事

官方写：假定不会出现标识相同的交易，这不成立。块不得再装去撞还没花光的旧标识。已经花光的允许再出现，好让以后还能剪枝。加上再拿掉之后，可花输出集合不得被改掉。本页没选「保证 coinbase 都唯一」那条路。

## 和相邻反模式

- [txid-sold-as-wtxid](txid-sold-as-wtxid.md) 是交易哈希 ≠ 已经含见证，不是本页这条重复标识。
- [coinbase-sold-as-spendable](coinbase-sold-as-spendable.md) 是进了块的 coinbase ≠ 已经能花，不是本页。
- [header-sold-as-height](header-sold-as-height.md) 是看见头 ≠ 高度已在头上，不是本页。
