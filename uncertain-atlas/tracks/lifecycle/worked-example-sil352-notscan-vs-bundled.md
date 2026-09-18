# 例：看见扫过不是已经收到；看见没扫到不是已经没人付；看见轻客户端过滤器对上不是已经是本页这种发现

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-352](https://github.com/bitcoin/bips/blob/master/bip-0352.mediawiki)（Complete, Applications）。  
**对应课文**：[L0.7](../../courses/level-00-machine/L00-M07-one-payment-lifecycle.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-352 scanned not already received / not already spendable / not already settled 正式三事（260 余量）/ not 1218 sil352-notscan interchangeable / not 260 silent-payment-vs-output bundled interchangeable」，不是静默付款 bundled（260），也不是扩展公钥就已经能花（182），也不是签过就已经控制资金（258）。不要另写怎样派生输出。

## 官方三件事

1. **看见扫过 / 看见扫过一遍 这份指示 is not already 已经收到 interchangeable，也不是已经静默付款 bundled（260） interchangeable / 1218 sil352-notscan interchangeable / 1217 sil352-notout interchangeable / 260 silent item 1 addr-not-out interchangeable，也不是已经 BIP-352 scanned not already received / not already spendable / not already settled 正式三事 bundled（260 item 2 余量） interchangeable / 260 silent item 2 interchangeable。**  
   官方写：代价是钱包必须扫链才能发现付款。本页把扫描职责和花费职责分开：扫描可以在线，花费钥可以留在离线冷存。看见扫过一遍，不是已经收到，也不是已经能从冷存花。

2. **看见没扫到 / 看见扫过 / 这份指示 is not already 已经没人付 interchangeable，也不是已经静默付款 bundled（260） interchangeable / 1218 sil352-notscan interchangeable / 260 silent item 3 reuse-not-same interchangeable / 1219 sil352-notreuse interchangeable，也不是已经扩展公钥就已经能花 interchangeable / 182 xpub interchangeable。**  
   官方写：看见没扫到，不是已经没人付。轻客户端怎么扫，官方写成仍在研究。

3. **看见轻客户端过滤器对上 / 看见扫过 / 这份指示 is not already 已经是本页这种发现 interchangeable，也不是已经静默付款 bundled（260） interchangeable / 1218 sil352-notscan interchangeable / 1217 sil352-notout interchangeable，也不是已经签过就已经控制资金 interchangeable / 258 signed interchangeable。**  
   官方写：看见轻客户端过滤器对上，不是已经是本页这种发现，也不是已经交差。

派生怎么算、编码字符、测试向量是规范里的取值，本页不抄。不要另写怎样派生输出。

## 官方为什么这样拆

- **扫过 不是已经收到：** 官方把发现写成必须扫链，并把扫描和花费分开。
- **没扫到 不是已经没人付：** 官方把没扫到写成不是已经没人付。
- **轻客户端过滤器对上 不是已经是本页这种发现：** 官方把轻客户端怎么扫写成仍在研究。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 收到 | 不是已经收到 | 不是已经能花（182） |
| 没人付 | 不是已经没人付 | 不是已经控制资金（258） |
| 发现 | 不是已经是本页这种发现 | 不是已经有输出（1217） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-352 scanned not already received / not already spendable / not already settled 正式三事（260 余量），必须分开是不是已经收到、是不是已经没人付、是不是已经是本页这种发现。可以跳过「看见收款码就已经付到链上」。不要另写怎样派生输出。260 silent payment vs output bundled unbundling 在本页 item 2 续；续 [`worked-example-sil352-notreuse-vs-bundled.md`](worked-example-sil352-notreuse-vs-bundled.md)（不变量 1219 item 3）。

## 本页不抄

- 派生公式、标签哈希、可读前缀字面量、例地址、测试向量。
- 怎样扫链、怎样从输入拼共享秘密、怎样用标签把付款连起来。
