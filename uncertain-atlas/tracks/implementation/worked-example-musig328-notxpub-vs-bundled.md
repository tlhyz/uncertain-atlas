# 例：看见 MuSig2 聚合钥不是已经是扩展公钥；看见能当普通公钥用不是已经能按 32 那种树往下长；看见一把普通公钥不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-328](https://github.com/bitcoin/bips/blob/master/bip-0328.mediawiki)（Complete, Applications, Informational）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-328 aggregate-key not already xpub / not already bip32-tree / not already settled 正式三事（283 余量）/ not 1169 musig328-notxpub interchangeable / not 283 musig-xpub-vs-aggregate bundled interchangeable」，不是聚合钥派生 bundled（283），也不是扩展公钥就已经能花（182），也不是一份包装就已经是 combo（1168）。不要另写怎样算派生微调。

## 官方三件事

1. **看见 MuSig2 聚合钥 / 看见一把普通公钥 这份栏 is not already 已经是扩展公钥 interchangeable，也不是已经聚合钥派生 bundled（283） interchangeable / 1169 musig328-notxpub interchangeable / 1170 musig328-nothard interchangeable / 283 musig item 2 synth-not-hard interchangeable，也不是已经 BIP-328 aggregate-key not already xpub / not already bip32-tree / not already settled 正式三事 bundled（283 item 1 余量） interchangeable / 283 musig item 1 interchangeable。**  
   官方写：本页指定怎样从 BIP-327 的明文聚合公钥造出一份合成扩展公钥。看见聚合钥，不是已经带了深度、子号和链码。

2. **看见能当普通公钥用 / 看见聚合钥 / 这份栏 is not already 已经能按 32 那种树往下长 interchangeable，也不是已经聚合钥派生 bundled（283） interchangeable / 1169 musig328-notxpub interchangeable / 283 musig item 3 child-not-tweak interchangeable / 1171 musig328-nottweak interchangeable，也不是已经扩展公钥就已经能花 interchangeable / 182 xpub interchangeable。**  
   官方写：聚合公钥看起来像普通公钥，所以可以这样用。看见能当普通公钥用，不是已经是 32 那种扩展公钥。

3. **看见一把普通公钥 / 看见聚合钥 / 这份栏 is not already 已经交差 interchangeable，也不是已经聚合钥派生 bundled（283） interchangeable / 1169 musig328-notxpub interchangeable / 1170 musig328-nothard interchangeable，也不是已经一份包装就已经是 combo interchangeable / 1168 raw385-notwrap interchangeable。**  
   官方把合成扩展公钥写成另造深度、子号和链码。看见一把普通公钥，不是已经交差。

固定链码取值、测试向量、例钥、派生公式是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **聚合钥 不是已经是扩展公钥：** 官方把合成扩展公钥写成另造深度、子号和链码。
- **能当普通公钥用 不是已经能按 32 那种树往下长：** 官方把看起来像普通公钥和已经是扩展公钥写成两句。
- **一把普通公钥 不是已经交差：** 官方把合成写成独立一句。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 扩展公钥 | 不是已经是扩展公钥 | 不是已经能花（182） |
| 32 那种树 | 不是已经能按 32 往下长 | 不是已经能硬化（1170） |
| 交差 | 不是已经交差 | 不是已经是一份包装（1168） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-328 aggregate-key not already xpub / not already bip32-tree / not already settled 正式三事（283 余量），必须分开是不是已经是扩展公钥、是不是已经能按 32 那种树往下长、是不是已经交差。可以跳过「看见聚合钥就已经能当普通扩展公钥用」。不要另写怎样算派生微调。283 musig xpub vs aggregate bundled unbundling 在本页 item 1 启动；续 [`worked-example-musig328-nothard-vs-bundled.md`](worked-example-musig328-nothard-vs-bundled.md)（不变量 1170 item 2）。

## 本页不抄

- 固定链码取值、测试向量、例钥、派生公式。
- 怎样造合成扩展公钥、怎样算每一步微调、怎样放进签名会话。
