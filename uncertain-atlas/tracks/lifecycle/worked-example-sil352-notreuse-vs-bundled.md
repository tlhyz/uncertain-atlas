# 例：看见同一条静默付款地址再用不是已经同一笔输出；看见没有通知不是已经没有付款；看见再用不是已经把各次付款连上

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-352](https://github.com/bitcoin/bips/blob/master/bip-0352.mediawiki)（Complete, Applications）。  
**对应课文**：[L0.7](../../courses/level-00-machine/L00-M07-one-payment-lifecycle.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-352 reuse not already same-output / not already linked / not already settled 正式三事（260 余量）/ not 1219 sil352-notreuse interchangeable / not 260 silent-payment-vs-output bundled interchangeable」，不是静默付款 bundled（260），也不是后继校验就已经是旧方案（181），也不是过滤器对上就已经有块（243）。不要另写怎样派生输出。

## 官方三件事

1. **看见同一条静默付款地址再用 / 看见同一条码再用 这份指示 is not already 已经同一笔输出 interchangeable，也不是已经静默付款 bundled（260） interchangeable / 1219 sil352-notreuse interchangeable / 1217 sil352-notout interchangeable / 260 silent item 1 addr-not-out interchangeable，也不是已经 BIP-352 reuse not already same-output / not already linked / not already settled 正式三事 bundled（260 item 3 余量） interchangeable / 260 silent item 3 interchangeable。**  
   官方写：多次付款不得链回同一个发送者。不必再发链上通知。看见同一条静默付款地址再用，不是已经同一笔脚本，也不是已经同一笔输出。

2. **看见没有通知 / 看见同一条静默付款地址再用 / 这份指示 is not already 已经没有付款 interchangeable，也不是已经静默付款 bundled（260） interchangeable / 1219 sil352-notreuse interchangeable / 260 silent item 2 scan-not-recv interchangeable / 1218 sil352-notscan interchangeable，也不是已经后继校验就已经是旧方案 interchangeable / 181 bech32m interchangeable。**  
   官方写：链下通知只是把隐私和代价挪到别处，还多了通知送不到就丢钱的风险。看见没有通知，不是已经没有付款。

3. **看见再用 / 看见同一条静默付款地址再用 / 这份指示 is not already 已经把各次付款连上 interchangeable，也不是已经静默付款 bundled（260） interchangeable / 1219 sil352-notreuse interchangeable / 1217 sil352-notout interchangeable，也不是已经过滤器对上就已经有块 interchangeable / 243 filter interchangeable。**  
   官方把「避免误复用」和「不得链回同一发送者」写成两条独立目标。看见再用，不是已经把各次付款连上，也不是已经交差。

派生怎么算、编码字符、测试向量是规范里的取值，本页不抄。不要另写怎样派生输出。

## 官方为什么这样拆

- **同一条静默付款地址再用 不是已经同一笔输出：** 官方把每次仍应是新输出写成目标。
- **没有通知 不是已经没有付款：** 官方把不必再发链上通知写成另一句。
- **再用 不是已经把各次付款连上：** 官方把不得链回同一发送者写成独立目标。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 同一笔输出 | 不是已经同一笔输出 | 不是已经是旧方案（181） |
| 没有付款 | 不是已经没有付款 | 不是已经有块（243） |
| 连上 | 不是已经把各次付款连上 | 不是已经有输出（1217） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-352 reuse not already same-output / not already linked / not already settled 正式三事（260 余量），必须分开是不是已经同一笔输出、是不是已经没有付款、是不是已经把各次付款连上。可以跳过「看见收款码就已经付到链上」。不要另写怎样派生输出。260 silent payment vs output bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 派生公式、标签哈希、可读前缀字面量、例地址、测试向量。
- 怎样扫链、怎样从输入拼共享秘密、怎样用标签把付款连起来。
