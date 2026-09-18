# 例：看见 shared-threshold-master is not already enough interchangeable / not already must-store-each interchangeable / not already settled interchangeable

**层次**：应用 / BIP-67 shared-threshold-master not already enough / not already must-store-each / not already settled 正式三事（270 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-67](https://github.com/bitcoin/bips/blob/master/bip-0067.mediawiki)（Complete, Applications）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-67 shared-threshold-master not already enough / not already must-store-each / not already settled 正式三事（270 余量）/ not 1134 sort67-notshare interchangeable / not 270 sorted-vs-one-address bundled interchangeable」，不是确定性多签地址 bundled（270），也不是扩展公钥就已经能花（182），也不是共享主公钥就已经是本页（1130）。不要另写怎样按字节字典序排公钥，也不要另写 BIP-11 / BIP-45。

## 官方三件事

1. **看见只共享门限和参与者主公钥 这份栏 is not already 已经够了 interchangeable，也不是已经确定性多签地址 bundled（270） interchangeable / 1134 sort67-notshare interchangeable / 1133 sort67-notaddr interchangeable / 270 sorted item 1 keys-not-same interchangeable，也不是已经 BIP-67 shared-threshold-master not already enough / not already must-store-each / not already settled 正式三事 bundled（270 item 2 余量） interchangeable / 270 sorted item 2 interchangeable。**  
   官方写：采用本页排序和编码之后，合规钱包对同一套钥、同一门限总会长出同一条 P2SH 地址。看见只共享了门限和主公钥，不是已经够了 interchangeable——本页从 270 item 2 侧钉 not already enough 单句。270 sorted vs one-address bundled unbundling 在本页 item 2 续。

2. **看见还没采用本页 / 看见只共享门限和主公钥 / 这份栏 is not already 已经必须为每个地址另存一份状态 interchangeable，也不是已经确定性多签地址 bundled（270） interchangeable / 1134 sort67-notshare interchangeable / 270 sorted item 3 uncomp-not-this interchangeable / 1135 sort67-notuncomp interchangeable，也不是已经扩展公钥就已经能花 interchangeable / 182 xpub interchangeable。**  
   官方把还没采用本页和已经必须为每个地址另存一份状态分开。看见还没采用本页，不是已经必须为每个地址另存一份状态 interchangeable。本页钉 not already must-store-each 单句。

3. **看见代签服务之外的一方也能找回 / 看见只共享门限和主公钥 / 这份栏 is not already 已经交差 interchangeable，也不是已经确定性多签地址 bundled（270） interchangeable / 1134 sort67-notshare interchangeable / 1133 sort67-notaddr interchangeable，也不是已经共享主公钥就已经是本页 interchangeable / 1130 cos45-notmaster interchangeable。**  
   官方把这能让代签服务之外的一方在服务不帮忙时也能找回钱包写成采用本页之后才成立。看见代签服务之外的一方也能找回，不是已经交差 interchangeable。270 sorted vs one-address bundled unbundling 在本页 item 2 续。

压缩钥例、地址例、脚本十六进制、怎样按字节字典序排是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **BIP-67 shared-threshold-master not already enough ≠ 已经够了 interchangeable：** 官方把只要这两样各钱包就会长出同一批地址写成采用本页之后才成立。
- **看见还没采用本页 not already must-store-each ≠ 已经必须为每个地址另存一份状态 interchangeable：** 官方把还没采用本页和已经必须另存状态分开。
- **看见代签服务之外的一方也能找回 not already settled ≠ 已经交差 interchangeable：** 官方把找回写成采用本页之后才成立；270 sorted vs one-address bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 只共享门限和参与者主公钥 | 不是已经够了 | 不是扩展公钥就已经能花（182） |
| 看见还没采用本页 | 不是已经必须为每个地址另存一份状态 | 不是共享主公钥就已经是本页（1130） |
| 看见代签服务之外的一方也能找回 | 不是已经交差 | 不是未压缩钥就已经是本页（1135） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-67 shared-threshold-master not already enough / not already must-store-each / not already settled 正式三事（270 余量），必须分开是不是已经够了、是不是已经必须为每个地址另存一份状态、是不是已经交差。可以跳过「看见同一套钥就已经是同一条地址」。不要另写怎样按字节字典序排公钥，也不要另写 BIP-11 / BIP-45。270 sorted vs one-address bundled unbundling 在本页 item 2 续；续 [`worked-example-sort67-notuncomp-vs-bundled.md`](worked-example-sort67-notuncomp-vs-bundled.md)（不变量 1135 item 3）。

## 本页不抄

- 压缩钥例、地址例、脚本十六进制、测试向量。
- 怎样按字节字典序排公钥、OP_2 / OP_3 拼法。
- 确定性多签地址 bundled。那是不变量 270。
- 扩展公钥就已经能花。那是不变量 182。
