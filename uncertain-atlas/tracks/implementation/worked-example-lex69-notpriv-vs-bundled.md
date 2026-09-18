# 例：看见按字典序排了不是已经私人；看见确定排过不是已经是随机打乱；看见能给 CoinJoin 用不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-69](https://github.com/bitcoin/bips/blob/master/bip-0069.mediawiki)（Complete, Applications, Informational）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-69 lex-order not already private / not already random / not already settled 正式三事（291 余量）/ not 1189 lex69-notpriv interchangeable / not 291 order-vs-lex bundled interchangeable」，不是输入输出字典序 bundled（291），也不是提案存在就已经对全网私人（1186），也不是同一交易标识就已经唯一（257）。不要另写怎样按前交易哈希排输入。

## 官方三件事

1. **看见按字典序排了 / 看见确定排过 这份顺序 is not already 已经私人 interchangeable，也不是已经输入输出字典序 bundled（291） interchangeable / 1189 lex69-notpriv interchangeable / 1187 lex69-nothabit interchangeable / 291 lex item 1 habit-not-std interchangeable，也不是已经 BIP-69 lex-order not already private / not already random / not already settled 正式三事 bundled（291 item 3 余量） interchangeable / 291 lex item 3 interchangeable。**  
   官方写：本页要的是确定、无歧义、只靠链上公开对象的排法，好让全节点和 SPV 都能核。看见按公开对象排了，不是已经对观察者私人。

2. **看见确定排过 / 看见按字典序排了 / 这份顺序 is not already 已经是随机打乱 interchangeable，也不是已经输入输出字典序 bundled（291） interchangeable / 1189 lex69-notpriv interchangeable / 291 lex item 2 lex-not-cons interchangeable / 1188 lex69-notcons interchangeable，也不是已经提案存在就已经对全网私人 interchangeable / 1186 pj78-notmerge interchangeable。**  
   官方写：随机排能挡一些隐私弱点，可是非确定排法不好审计；恶意实现甚至能把主私钥的比特编进顺序里。看见确定排过，不是已经随机。

3. **看见能给 CoinJoin 用 / 看见按字典序排了 / 这份顺序 is not already 已经交差 interchangeable，也不是已经输入输出字典序 bundled（291） interchangeable / 1189 lex69-notpriv interchangeable / 1187 lex69-nothabit interchangeable，也不是已经同一交易标识就已经唯一 interchangeable / 257 txid interchangeable。**  
   官方写：多方交易（例如 CoinJoin）也能按同一套排。看见能给 CoinJoin 用，不是已经是 CoinJoin，也不是已经交差。

比较算法、反字节序哈希、金额优先、例交易、脚本十六进制是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **按字典序排了 不是已经私人：** 官方把按公开对象排写成观察者仍能看见。
- **确定排过 不是已经是随机打乱：** 官方把确定可审计和随机打乱写成两条路。
- **能给 CoinJoin 用 不是已经交差：** 官方把能共用排法写成不是已经是 CoinJoin。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 私人 | 不是已经私人 | 不是已经对全网私人（1186） |
| 随机 | 不是已经是随机打乱 | 不是已经唯一（257） |
| 交差 | 不是已经交差 | 不是已经是共识（1188） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-69 lex-order not already private / not already random / not already settled 正式三事（291 余量），必须分开是不是已经私人、是不是已经是随机打乱、是不是已经交差。可以跳过「看见排过就已经没有指纹」。不要另写怎样按前交易哈希排输入。291 order vs lex bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 比较算法、反字节序、金额优先、例交易哈希、脚本十六进制、语言库名单。
- 怎样按前交易哈希排输入、怎样按金额排输出、怎样审计随机排。
