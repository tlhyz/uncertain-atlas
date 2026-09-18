# 例：看见指纹对上不是已经核过 KEY；看见第一地址不是已经各方确认同一份；看见钥记录不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-129](https://github.com/bitcoin/bips/blob/master/bip-0129.mediawiki)（Complete, Applications, Specification）。依赖 BIP-32、BIP-174、BIP-322、BIP-380、BIP-381、BIP-382、BIP-383。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-129 fingerprint not already verified-key / not already same-confirm / not already settled 正式三事（287 余量）/ not 1179 bsms129-notkey interchangeable / not 287 setup-vs-psbt bundled interchangeable」，不是跨厂安全多签开户 bundled（287），也不是描述符就已经是地址（184），也不是登记过就已经批准这笔花（1162）。不要另写怎样核对钥或怎样加密会话。

## 官方三件事

1. **看见指纹对上 / 看见钥记录 这份开户 is not already 已经核过 KEY interchangeable，也不是已经跨厂安全多签开户 bundled（287） interchangeable / 1179 bsms129-notkey interchangeable / 1178 bsms129-notsetup interchangeable / 287 bsms item 1 psbt-not-setup interchangeable，也不是已经 BIP-129 fingerprint not already verified-key / not already same-confirm / not already settled 正式三事 bundled（287 item 2 余量） interchangeable / 287 bsms item 2 interchangeable。**  
   官方写：签名器必须核对描述符或描述符模板里有没有自己的 KEY，而且必须做精确比对，不能走指纹那种捷径，因为指纹很容易伪造。看见指纹对上，不是已经对上那把 KEY。

2. **看见第一地址 / 看见指纹对上 / 这份开户 is not already 已经各方确认同一份 interchangeable，也不是已经跨厂安全多签开户 bundled（287） interchangeable / 1179 bsms129-notkey interchangeable / 287 bsms item 3 token-not-seed interchangeable / 1180 bsms129-nottoken interchangeable，也不是已经描述符就已经是地址 interchangeable / 184 descriptor interchangeable。**  
   官方另写：签名器必须给用户看钱包第一地址和政策参数。各方必须互相核：除了 KEY 位置，所有签名器看到的确认必须一样。看见第一地址，不是各方已经对过同一份。

3. **看见钥记录 / 看见指纹对上 / 这份开户 is not already 已经交差 interchangeable，也不是已经跨厂安全多签开户 bundled（287） interchangeable / 1179 bsms129-notkey interchangeable / 1178 bsms129-notsetup interchangeable，也不是已经登记过就已经批准这笔花 interchangeable / 1162 pol388-notreg interchangeable。**  
   官方把精确比对、第一地址确认、各方互核写成三道门。看见钥记录，不是已经交差。

记录行格式、加密配方、测试向量、描述符模板展开是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **指纹对上 不是已经核过 KEY：** 官方把精确比对写成不能走指纹捷径。
- **第一地址 不是已经各方确认同一份：** 官方把互核写成除了 KEY 位置必须一样。
- **钥记录 不是已经交差：** 官方把三道门写成三句。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| KEY | 不是已经核过 KEY | 不是已经是地址（184） |
| 互核 | 不是已经各方确认同一份 | 不是已经批准这笔花（1162） |
| 交差 | 不是已经交差 | 不是已经开过户（1178） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-129 fingerprint not already verified-key / not already same-confirm / not already settled 正式三事（287 余量），必须分开是不是已经核过 KEY、是不是已经各方确认同一份、是不是已经交差。可以跳过「看见部分签名包就已经开好了多签」。不要另写怎样核对钥或怎样加密会话。287 setup vs psbt bundled unbundling 在本页 item 2 续；续 [`worked-example-bsms129-nottoken-vs-bundled.md`](worked-example-bsms129-nottoken-vs-bundled.md)（不变量 1180 item 3）。

## 本页不抄

- 记录行格式、文件后缀、加密配方、TOKEN 宽度、测试向量、钥例、描述符模板展开。
- 怎样做精确比对、怎样造 TOKEN、怎样加密会话、怎样展开模板。
