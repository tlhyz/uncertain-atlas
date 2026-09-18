# 例：看见后来又出现已经花光的那条标识不是已经非法；看见重组不是已经把花掉再重复的输出加回来；看见本页不是历史上那两处例外已经没了

**层次**：共识 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-30](https://github.com/bitcoin/bips/blob/master/bip-0030.mediawiki)（Deployed, Consensus soft fork）。  
**对应课文**：[L3.1](../../courses/level-03-bitcoin/L03-M01-nakamoto-finality.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识当已经唯一、M5.4、L5.4。本页是「BIP-30 spent-reappear not already illegal / not already revived / not already settled 正式三事（257 余量）/ not 1228 dup30-notspent interchangeable / not 257 duplicate-txid-vs-unique bundled interchangeable」，不是重复交易标识 bundled（257），也不是进了块的 coinbase 就已经能花（163），也不是 txid 就已经含见证（152）。不要另写怎样造重复 coinbase。

## 官方三件事

1. **看见后来又出现已经花光的那条标识 / 看见完全花光的交易再出现 这份规则 is not already 已经非法 interchangeable，也不是已经重复交易标识 bundled（257） interchangeable / 1228 dup30-notspent interchangeable / 1226 dup30-notuniq interchangeable / 257 dup item 1 same-not-uniq interchangeable，也不是已经 BIP-30 spent-reappear not already illegal / not already revived / not already settled 正式三事 bundled（257 item 3 余量） interchangeable / 257 dup item 3 interchangeable。**  
   官方写：完全花光的交易允许重复，为的是以后剪枝时不必给每一笔曾经存在的交易留证据。看见后来又出现已经花光的那条标识，不是已经非法，也不是旧输出又活了。

2. **看见重组 / 看见后来又出现已经花光的那条标识 / 这份规则 is not already 已经把花掉再重复的输出加回来 interchangeable，也不是已经重复交易标识 bundled（257） interchangeable / 1228 dup30-notspent interchangeable / 257 dup item 2 unspent-not-legal interchangeable / 1227 dup30-notlive interchangeable，也不是已经进了块的 coinbase 就已经能花 interchangeable / 163 mature interchangeable。**  
   官方写：无论选哪条修法，必须服从这条定律：先把块加上、再拿掉（重组）之后，可花输出集合不得被改掉。参考实现在临时加上的块里有重复交易时，不服从这条定律。看见重组，不是已经把花掉再重复的输出加回来。

3. **看见本页 / 看见后来又出现已经花光的那条标识 / 这份规则 is not already 历史上那两处例外已经没了 interchangeable，也不是已经重复交易标识 bundled（257） interchangeable / 1228 dup30-notspent interchangeable / 1226 dup30-notuniq interchangeable，也不是已经 txid 就已经含见证 interchangeable / 152 wtxid interchangeable。**  
   官方写：看见本页，不是历史上那两处例外已经没了，也不是已经交差。

激活时间、例外高度是规范里的取值，本页不抄。不要另写怎样造重复 coinbase。

## 官方为什么这样拆

- **已经花光后再出现 不是已经非法：** 官方为了剪枝允许花光后再用同一标识。
- **重组 不是已经把花掉再重复的输出加回来：** 官方把加上再拿掉不得改可花集合写成定律。
- **本页 不是历史上那两处例外已经没了：** 官方把本页和历史上两处例外写成两件。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 非法 | 不是已经非法 | 不是已经能花（163） |
| 加回 | 不是已经把花掉再重复的输出加回来 | 不是已经含见证（152） |
| 例外没了 | 不是历史上那两处例外已经没了 | 不是已经唯一（1226） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-30 spent-reappear not already illegal / not already revived / not already settled 正式三事（257 余量），必须分开是不是已经非法、是不是已经把花掉再重复的输出加回来、是不是历史上那两处例外已经没了。可以跳过「看见同一标识就已经是同一笔可花输出」。不要另写怎样造重复 coinbase。257 duplicate txid vs unique bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 激活时间、例外高度、参考实现提交哈希。
- 怎样造重复 coinbase、怎样覆盖还没花光的输出、怎样把已确认交易打回一次确认。
