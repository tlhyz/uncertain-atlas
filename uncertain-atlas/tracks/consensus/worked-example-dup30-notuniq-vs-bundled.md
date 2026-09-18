# 例：看见同一交易标识不是已经唯一；看见许多确认不是已经不怕被覆盖；看见同一标识不是已经交差

**层次**：共识 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-30](https://github.com/bitcoin/bips/blob/master/bip-0030.mediawiki)（Deployed, Consensus soft fork）。  
**对应课文**：[L3.1](../../courses/level-03-bitcoin/L03-M01-nakamoto-finality.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识当已经唯一、M5.4、L5.4。本页是「BIP-30 same-txid not already unique / not already same-outputs / not already settled 正式三事（257 余量）/ not 1226 dup30-notuniq interchangeable / not 257 duplicate-txid-vs-unique bundled interchangeable」，不是重复交易标识 bundled（257），也不是 txid 就已经含见证（152），也不是进了块的 coinbase 就已经能花（163）。不要另写怎样造重复 coinbase。

## 官方三件事

1. **看见同一交易标识 / 看见同一个哈希 这份标识 is not already 已经唯一 interchangeable，也不是已经重复交易标识 bundled（257） interchangeable / 1226 dup30-notuniq interchangeable / 1227 dup30-notlive interchangeable / 257 dup item 2 unspent-not-legal interchangeable，也不是已经 BIP-30 same-txid not already unique / not already same-outputs / not already settled 正式三事 bundled（257 item 1 余量） interchangeable / 257 dup item 1 interchangeable。**  
   官方写：参考实现一直假定不会出现标识相同的交易。这不成立。尤其 coinbase 很容易重复；在重复的 coinbase 上再搭，普通交易也能重复。看见同一个交易标识，不是已经只有一组可花输出，也不是已经不能再覆盖。

2. **看见许多确认 / 看见同一交易标识 / 这份标识 is not already 已经不怕被覆盖 interchangeable，也不是已经重复交易标识 bundled（257） interchangeable / 1226 dup30-notuniq interchangeable / 257 dup item 3 spent-not-illegal interchangeable / 1228 dup30-notspent interchangeable，也不是已经 txid 就已经含见证 interchangeable / 152 wtxid interchangeable。**  
   官方写：有一种攻击会利用参考实现怎么处理重复交易，能把已经充分确认的交易打回只剩一次确认，从而再变得完全不能花。另一种攻击能让网络的一部分分叉。看见许多确认，不是已经不怕这种覆盖。

3. **看见同一标识 / 看见同一交易标识 / 这份标识 is not already 已经交差 interchangeable，也不是已经重复交易标识 bundled（257） interchangeable / 1226 dup30-notuniq interchangeable / 1227 dup30-notlive interchangeable，也不是已经进了块的 coinbase 就已经能花 interchangeable / 163 mature interchangeable。**  
   官方把「假定不会重复」写成假的。看见同一标识，不是已经交差。

激活时间、例外高度是规范里的取值，本页不抄。不要另写怎样造重复 coinbase。

## 官方为什么这样拆

- **同一交易标识 不是已经唯一：** 官方把假定不会重复写成假的。
- **许多确认 不是已经不怕被覆盖：** 官方把充分确认打回一次确认写成攻击。
- **同一标识 不是已经交差：** 官方把同一哈希和同一笔钱写成两件。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 唯一 | 不是已经唯一 | 不是已经含见证（152） |
| 覆盖 | 不是已经不怕被覆盖 | 不是已经能花（163） |
| 交差 | 不是已经交差 | 不是已经合法（1227） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-30 same-txid not already unique / not already same-outputs / not already settled 正式三事（257 余量），必须分开是不是已经唯一、是不是已经不怕被覆盖、是不是已经交差。可以跳过「看见同一标识就已经是同一笔可花输出」。不要另写怎样造重复 coinbase。257 duplicate txid vs unique bundled unbundling 在本页 item 1 启动；续 [`worked-example-dup30-notlive-vs-bundled.md`](worked-example-dup30-notlive-vs-bundled.md)（不变量 1227 item 2）。

## 本页不抄

- 激活时间、例外高度、参考实现提交哈希。
- 怎样造重复 coinbase、怎样覆盖还没花光的输出、怎样把已确认交易打回一次确认。
