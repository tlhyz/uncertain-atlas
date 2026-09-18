# 例：看见派生出的子钥不是已经能不带微调去签；看见写了微调不是已经是 x-only 那种微调；看见一次签名会话不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-328](https://github.com/bitcoin/bips/blob/master/bip-0328.mediawiki)（Complete, Applications, Informational）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-328 child-key not already sign-without-tweak / not already x-only-tweak / not already settled 正式三事（283 余量）/ not 1171 musig328-nottweak interchangeable / not 283 musig-xpub-vs-aggregate bundled interchangeable」，不是聚合钥派生 bundled（283），也不是派生钥就已经是输出钥（1136），也不是压缩钥就已经是 x-only（1147）。不要另写怎样算派生微调。

## 官方三件事

1. **看见派生出的子钥 / 看见一次签名会话 这份栏 is not already 已经能不带微调去签 interchangeable，也不是已经聚合钥派生 bundled（283） interchangeable / 1171 musig328-nottweak interchangeable / 1169 musig328-notxpub interchangeable / 283 musig item 1 agg-not-xpub interchangeable，也不是已经 BIP-328 child-key not already sign-without-tweak / not already x-only-tweak / not already settled 正式三事 bundled（283 item 3 余量） interchangeable / 283 musig item 3 interchangeable。**  
   官方写：签名时，所有签名人都必须算出 BIP-32 派生用到的那些微调。看见子钥，不是已经能直接当聚合钥去签。

2. **看见写了微调 / 看见子钥 / 这份栏 is not already 已经是 x-only 那种微调 interchangeable，也不是已经聚合钥派生 bundled（283） interchangeable / 1171 musig328-nottweak interchangeable / 283 musig item 2 synth-not-hard interchangeable / 1170 musig328-nothard interchangeable，也不是已经压缩钥就已经是 x-only interchangeable / 1147 tr386-notxonly interchangeable。**  
   官方写：每一步用的是派生算法里算出的那一份微调，并且以明文微调模式放进会话。看见写了微调，不是已经是 x-only 那种微调。

3. **看见一次签名会话 / 看见子钥 / 这份栏 is not already 已经交差 interchangeable，也不是已经聚合钥派生 bundled（283） interchangeable / 1171 musig328-nottweak interchangeable / 1169 musig328-notxpub interchangeable，也不是已经派生钥就已经是输出钥 interchangeable / 1136 tap86-notout interchangeable。**  
   官方把每一步派生微调写成签名会话里必须带上的对象。看见一次签名会话，不是已经交差。

固定链码取值、测试向量、例钥、派生公式是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **子钥 不是已经能不带微调去签：** 官方把派生微调写成签名会话里必须带上。
- **写了微调 不是已经是 x-only 那种微调：** 官方把本页微调写成 BIP-32 明文微调。
- **一次签名会话 不是已经交差：** 官方把必须带微调和已经交差写成两句。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 不带微调去签 | 不是已经能直接签 | 不是已经是输出钥（1136） |
| x-only 微调 | 不是已经是 x-only 那种 | 不是已经是 x-only（1147） |
| 交差 | 不是已经交差 | 不是已经能硬化（1170） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-328 child-key not already sign-without-tweak / not already x-only-tweak / not already settled 正式三事（283 余量），必须分开是不是已经能不带微调去签、是不是已经是 x-only 那种微调、是不是已经交差。可以跳过「看见聚合钥就已经能当普通扩展公钥用」。不要另写怎样算派生微调。283 musig xpub vs aggregate bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 固定链码取值、测试向量、例钥、派生公式。
- 怎样造合成扩展公钥、怎样算每一步微调、怎样放进签名会话。
