# 例：看见 uncompressed-key is not already this-page interchangeable / not already network-rule interchangeable / not already settled interchangeable

**层次**：应用 / BIP-67 uncompressed-key not already this-page / not already network-rule / not already settled 正式三事（270 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-67](https://github.com/bitcoin/bips/blob/master/bip-0067.mediawiki)（Complete, Applications）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-67 uncompressed-key not already this-page / not already network-rule / not already settled 正式三事（270 余量）/ not 1135 sort67-notuncomp interchangeable / not 270 sorted-vs-one-address bundled interchangeable」，不是确定性多签地址 bundled（270），也不是本页多签就已经不排序（1129），也不是能独立长地址就已经能独立签（1131）。不要另写怎样按字节字典序排公钥，也不要另写 BIP-11 / BIP-45。

## 官方三件事

1. **看见未压缩钥 / 看见一条 P2SH 地址 这份栏 is not already 已经是本页 interchangeable，也不是已经确定性多签地址 bundled（270） interchangeable / 1135 sort67-notuncomp interchangeable / 1133 sort67-notaddr interchangeable / 270 sorted item 1 keys-not-same interchangeable，也不是已经 BIP-67 uncompressed-key not already this-page / not already network-rule / not already settled 正式三事 bundled（270 item 3 余量） interchangeable / 270 sorted item 3 interchangeable。**  
   官方写：未压缩钥和本页不兼容。兼容实现不应当自动把钥压成压缩形式。看见未压缩钥，不是已经是本页 interchangeable——本页从 270 item 3 侧钉 not already this-page 单句。270 sorted vs one-address bundled unbundling 在本页 item 3 完成。

2. **看见一条 P2SH 地址 / 看见未压缩钥 / 这份栏 is not already 已经能当网络规则 interchangeable，也不是已经确定性多签地址 bundled（270） interchangeable / 1135 sort67-notuncomp interchangeable / 270 sorted item 2 share-not-enough interchangeable / 1134 sort67-notshare interchangeable，也不是已经本页多签就已经不排序 interchangeable / 1129 msig48-notsort interchangeable。**  
   官方写：P2SH 地址并不露出里面的脚本，所以本页不能写成网络规则，那样会硬分叉。看见一条 P2SH 地址，不是已经能当网络规则 interchangeable。本页钉 not already network-rule 单句。

3. **看见一群人没有全部合规 / 看见未压缩钥 / 这份栏 is not already 已经交差 interchangeable，也不是已经确定性多签地址 bundled（270） interchangeable / 1135 sort67-notuncomp interchangeable / 1133 sort67-notaddr interchangeable，也不是已经能独立长地址就已经能独立签 interchangeable / 1131 cos45-notsign interchangeable。**  
   官方把一群人没有全部合规时可能有人长出别人认不出的地址写成独立后果。看见一群人没有全部合规，不是已经交差 interchangeable。270 sorted vs one-address bundled unbundling 在本页 item 3 完成。

压缩钥例、地址例、脚本十六进制、怎样按字节字典序排是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **BIP-67 uncompressed-key not already this-page ≠ 已经是本页 interchangeable：** 官方禁止自动压缩，并把未压缩钥写成对端实现不兼容。
- **看见一条 P2SH 地址 not already network-rule ≠ 已经能当网络规则 interchangeable：** 官方把本页写成不能当网络规则，那样会硬分叉。
- **看见一群人没有全部合规 not already settled ≠ 已经交差 interchangeable：** 官方把可能有人长出别人认不出的地址写成独立后果；270 sorted vs one-address bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 未压缩钥 / 一条 P2SH 地址 | 不是已经是本页 | 不是本页多签就已经不排序（1129） |
| 看见一条 P2SH 地址 | 不是已经能当网络规则 | 不是能独立长地址就已经能独立签（1131） |
| 看见一群人没有全部合规 | 不是已经交差 | 不是同一套钥就已经是同一条赎回（1133） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-67 uncompressed-key not already this-page / not already network-rule / not already settled 正式三事（270 余量），必须分开是不是已经是本页、是不是已经能当网络规则、是不是已经交差。可以跳过「看见同一套钥就已经是同一条地址」。不要另写怎样按字节字典序排公钥，也不要另写 BIP-11 / BIP-45。270 sorted vs one-address bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 压缩钥例、地址例、脚本十六进制、测试向量。
- 怎样按字节字典序排公钥、OP_2 / OP_3 拼法。
- 确定性多签地址 bundled。那是不变量 270。
- 本页多签就已经不排序。那是不变量 1129。
