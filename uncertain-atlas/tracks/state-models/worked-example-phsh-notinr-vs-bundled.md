# 例：看见哈希对上不是内层已经验过不是已经验过内层；看见hash matching is not already the inner script having been verified不是已经是不变量 152；看见哈希对上不是内层已经验过不是已经是不变量 297

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-16](https://github.com/bitcoin/bips/blob/master/bip-0016.mediawiki)（Pay to Script Hash）。  
**对应课文**：[L2.1](../../courses/level-02-state/L02-M01-utxo.md)。  
**不要写进**：`index/03` 共识行、M2.1、L2.1。本页是「BIP-16 hash-match not already inner-verified / not already 152 / not already 297 正式三事（170 余量）/ not 1535 phsh-notinr interchangeable / not 170 p2sh-hash-vs-redeem bundled interchangeable」，不是 p2sh hash vs redeem bundled（170），也不是已经 txid≠wtxid（152），也不是已经 P2SH地址≠赎回（297）。不要另写 怎样构造旧合法新非法的赎回、一确认攻击。

## 官方三件事

1. **看见哈希对上不是内层已经验过 / 看见哈希对上不是内层已经验过 这份对象 is not already 已经验过内层 interchangeable，也不是已经 p2sh hash vs redeem bundled（170） interchangeable / 1535 phsh-notinr interchangeable / 1533 phsh-notrev interchangeable，也不是已经 BIP-16 hash-match not already inner-verified / not already 152 / not already 297 正式三事 bundled（170 item 3 余量） interchangeable / 170 phsh item 3 interchangeable。**  
   官方把哈希对上不是内层已经验过和已经验过内层写成两件。看见哈希对上不是内层已经验过，不是已经验过内层。

2. **看见hash matching is not already the inner script having been verified / 看见哈希对上不是内层已经验过 / 这份对象 is not already 已经是不变量 152 interchangeable，也不是已经 p2sh hash vs redeem bundled（170） interchangeable / 1535 phsh-notinr interchangeable / 1534 phsh-notrun interchangeable，也不是已经 txid≠wtxid interchangeable / 152 txid≠wtxid interchangeable。**  
   官方把hash matching is not already the inner script having been verified和已经是不变量 152写成两件。看见hash matching is not already the inner script having been verified，不是已经是不变量 152。

3. **看见哈希对上不是内层已经验过 / 看见hash matching is not already the inner script having been verified / 这份对象 is not already 已经是不变量 297 interchangeable，也不是已经 p2sh hash vs redeem bundled（170） interchangeable / 1535 phsh-notinr interchangeable / 1533 phsh-notrev interchangeable，也不是已经 P2SH地址≠赎回 interchangeable / 297 P2SH地址≠赎回 interchangeable。**  
   官方把哈希对上不是内层已经验过和已经是不变量 297写成两件。看见哈希对上不是内层已经验过，不是已经是不变量 297。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样构造旧合法新非法的赎回、一确认攻击。

## 官方为什么这样拆

- **哈希对上不是内层已经验过 interchangeable：官方写对上之后弹出该脚本再当 scriptPubKey 验一次。**
- **看见本页不是已经是不变量 152。**
- **看见本页不是已经是不变量 297。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经验过内层 | 不是已经验过内层 | 不是已经txid≠wtxid（152） |
| 已经是不变量 152 | 不是已经是不变量 152 | 不是已经P2SH地址≠赎回（297） |
| 已经是不变量 297 | 不是已经是不变量 297 | 不是已经1533 phsh-notrev |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-16 hash-match not already inner-verified / not already 152 / not already 297 正式三事（170 余量），必须分开是不是已经验过内层、是不是已经是不变量 152、是不是已经是不变量 297。可以跳过「看见哈希对上就已经验过内层」。不要另写 怎样构造旧合法新非法的赎回、一确认攻击。170 p2sh hash vs redeem bundled unbundling 在本页 item 3 完成；本页收束本批。下一份仍捆着的官方对象：address-vs-utxo（174）。

## 本页不抄

- 激活票数、字节上限、例脚本、时间戳、操作码号。
- 怎样构造旧合法新非法的赎回、一确认攻击。
