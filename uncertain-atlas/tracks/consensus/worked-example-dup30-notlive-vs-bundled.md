# 例：看见后来又来一条同一标识而旧的还可花不是已经合法；看见本页不是已经保证所有 coinbase 标识都唯一；看见还没花光不是已经交差

**层次**：共识 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-30](https://github.com/bitcoin/bips/blob/master/bip-0030.mediawiki)（Deployed, Consensus soft fork）。  
**对应课文**：[L3.1](../../courses/level-03-bitcoin/L03-M01-nakamoto-finality.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识当已经唯一、M5.4、L5.4。本页是「BIP-30 unspent-collide not already legal / not already all-coinbase-unique / not already settled 正式三事（257 余量）/ not 1227 dup30-notlive interchangeable / not 257 duplicate-txid-vs-unique bundled interchangeable」，不是重复交易标识 bundled（257），也不是 coinbase 高度就已经在头上（173），也不是同一标识就已经唯一（1226）。不要另写怎样造重复 coinbase。

## 官方三件事

1. **看见后来又来一条同一标识、而旧的还可花 / 看见块里再装一条同一标识 这份规则 is not already 已经合法 interchangeable，也不是已经重复交易标识 bundled（257） interchangeable / 1227 dup30-notlive interchangeable / 1226 dup30-notuniq interchangeable / 257 dup item 1 same-not-uniq interchangeable，也不是已经 BIP-30 unspent-collide not already legal / not already all-coinbase-unique / not already settled 正式三事 bundled（257 item 2 余量） interchangeable / 257 dup item 2 interchangeable。**  
   官方写：新网络规则是：块不得包含一条交易，其标识与同一条链上更早、还不是完全花光的交易相同。看见后来又来一条同一标识、而旧的还可花，不是已经合法。

2. **看见本页 / 看见后来又来一条同一标识、而旧的还可花 / 这份规则 is not already 已经保证所有 coinbase 标识都唯一 interchangeable，也不是已经重复交易标识 bundled（257） interchangeable / 1227 dup30-notlive interchangeable / 257 dup item 3 spent-not-illegal interchangeable / 1228 dup30-notspent interchangeable，也不是已经 coinbase 高度就已经在头上 interchangeable / 173 height interchangeable。**  
   官方写：保证 coinbase 都唯一是更完整的方案，但要更多全网接受的改动，也挡不住基于更早重复 coinbase 再搭出来的重复交易。本页没选那条路。看见本页，不是已经保证所有 coinbase 标识都唯一。

3. **看见还没花光 / 看见后来又来一条同一标识、而旧的还可花 / 这份规则 is not already 已经交差 interchangeable，也不是已经重复交易标识 bundled（257） interchangeable / 1227 dup30-notlive interchangeable / 1226 dup30-notuniq interchangeable，也不是已经同一标识就已经唯一 interchangeable / 1226 uniq interchangeable。**  
   官方只禁还没花光的旧标识。看见还没花光，不是已经交差。

激活时间、例外高度是规范里的取值，本页不抄。不要另写怎样造重复 coinbase。

## 官方为什么这样拆

- **后来又来一条同一标识而旧的还可花 不是已经合法：** 官方只禁还没花光的旧标识。
- **本页 不是已经保证所有 coinbase 标识都唯一：** 官方没选保证 coinbase 都唯一那条路。
- **还没花光 不是已经交差：** 官方把还没花光和已经交差写成两件。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 合法 | 不是已经合法 | 不是已经有高度（173） |
| coinbase 唯一 | 不是已经保证所有 coinbase 标识都唯一 | 不是已经唯一（1226） |
| 交差 | 不是已经交差 | 不是已经花光可再出现（1228） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-30 unspent-collide not already legal / not already all-coinbase-unique / not already settled 正式三事（257 余量），必须分开是不是已经合法、是不是已经保证所有 coinbase 标识都唯一、是不是已经交差。可以跳过「看见同一标识就已经是同一笔可花输出」。不要另写怎样造重复 coinbase。257 duplicate txid vs unique bundled unbundling 在本页 item 2 续；续 [`worked-example-dup30-notspent-vs-bundled.md`](worked-example-dup30-notspent-vs-bundled.md)（不变量 1228 item 3）。

## 本页不抄

- 激活时间、例外高度、参考实现提交哈希。
- 怎样造重复 coinbase、怎样覆盖还没花光的输出、怎样把已确认交易打回一次确认。
