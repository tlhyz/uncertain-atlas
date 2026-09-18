# 例：看见 same-keys-threshold is not already same-redeem interchangeable / not already same-p2sh interchangeable / not already settled interchangeable

**层次**：应用 / BIP-67 same-keys-threshold not already same-redeem / not already same-p2sh / not already settled 正式三事（270 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-67](https://github.com/bitcoin/bips/blob/master/bip-0067.mediawiki)（Complete, Applications）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-67 same-keys-threshold not already same-redeem / not already same-p2sh / not already settled 正式三事（270 余量）/ not 1133 sort67-notaddr interchangeable / not 270 sorted-vs-one-address bundled interchangeable」，不是确定性多签地址 bundled（270），也不是付给脚本哈希就已经揭开赎回（170），也不是本页多签就已经不排序（1129）。不要另写怎样按字节字典序排公钥，也不要另写 BIP-11 / BIP-45。

## 官方三件事

1. **看见同一套钥 / 同一门限 这份栏 is not already 已经是同一条赎回脚本 interchangeable，也不是已经确定性多签地址 bundled（270） interchangeable / 1133 sort67-notaddr interchangeable / 1134 sort67-notshare interchangeable / 270 sorted item 2 share-not-enough interchangeable，也不是已经 BIP-67 same-keys-threshold not already same-redeem / not already same-p2sh / not already settled 正式三事 bundled（270 item 1 余量） interchangeable / 270 sorted item 1 interchangeable。**  
   官方写：赎回脚本并不要求公钥按某一种顺序或某一种编码。同一套钥、同一门限，可以有多到 2(n!) 条标准赎回脚本。看见钥集合对齐了，不是已经对齐了赎回脚本 interchangeable——本页从 270 item 1 侧钉 not already same-redeem 单句。270 sorted vs one-address bundled unbundling 在本页 item 1 启动。

2. **看见门限一样 / 看见同一套钥 / 这份栏 is not already 已经是同一条 P2SH 地址 interchangeable，也不是已经确定性多签地址 bundled（270） interchangeable / 1133 sort67-notaddr interchangeable / 270 sorted item 3 uncomp-not-this interchangeable / 1135 sort67-notuncomp interchangeable，也不是已经付给脚本哈希就已经揭开赎回 interchangeable / 170 hash interchangeable。**  
   官方把各有一条 P2SH 地址写成不要求顺序或编码的后果。看见门限一样，不是已经是同一条地址 interchangeable。本页钉 not already same-p2sh 单句。

3. **看见遵守顺序和编码 / 看见同一套钥 / 这份栏 is not already 已经交差 interchangeable，也不是已经确定性多签地址 bundled（270） interchangeable / 1133 sort67-notaddr interchangeable / 1134 sort67-notshare interchangeable，也不是已经本页多签就已经不排序 interchangeable / 1129 msig48-notsort interchangeable。**  
   官方把遵守顺序和编码才能让这一账户只有一条规范地址写成独立限制。看见遵守顺序和编码，不是已经交差 interchangeable。270 sorted vs one-address bundled unbundling 在本页 item 1 启动。

压缩钥例、地址例、脚本十六进制、怎样按字节字典序排是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **BIP-67 same-keys-threshold not already same-redeem ≠ 已经是同一条赎回脚本 interchangeable：** 官方把不要求顺序或编码写成可以长出多到 2(n!) 条标准赎回。
- **看见门限一样 not already same-p2sh ≠ 已经是同一条 P2SH 地址 interchangeable：** 官方把各有一条 P2SH 地址写成不要求顺序或编码的后果。
- **看见遵守顺序和编码 not already settled ≠ 已经交差 interchangeable：** 官方把遵守顺序和编码才能只有一条规范地址写成独立限制；270 sorted vs one-address bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 同一套钥 / 同一门限 | 不是已经是同一条赎回脚本 | 不是付给脚本哈希就已经揭开赎回（170） |
| 看见门限一样 | 不是已经是同一条 P2SH 地址 | 不是本页多签就已经不排序（1129） |
| 看见遵守顺序和编码 | 不是已经交差 | 不是只共享门限和主公钥就已经够了（1134） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-67 same-keys-threshold not already same-redeem / not already same-p2sh / not already settled 正式三事（270 余量），必须分开是不是已经是同一条赎回脚本、是不是已经是同一条 P2SH 地址、是不是已经交差。可以跳过「看见同一套钥就已经是同一条地址」。不要另写怎样按字节字典序排公钥，也不要另写 BIP-11 / BIP-45。270 sorted vs one-address bundled unbundling 在本页 item 1 启动；续 [`worked-example-sort67-notshare-vs-bundled.md`](worked-example-sort67-notshare-vs-bundled.md)（不变量 1134 item 2）。

## 本页不抄

- 压缩钥例、地址例、脚本十六进制、测试向量。
- 怎样按字节字典序排公钥、OP_2 / OP_3 拼法。
- 确定性多签地址 bundled。那是不变量 270。
- 付给脚本哈希就已经揭开赎回。那是不变量 170。
