# 例：看见部分签名包不是已经是跨厂安全多签开户；看见签流程不是已经核过成员；看见包还能签不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-129](https://github.com/bitcoin/bips/blob/master/bip-0129.mediawiki)（Complete, Applications, Specification）。依赖 BIP-32、BIP-174、BIP-322、BIP-380、BIP-381、BIP-382、BIP-383。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-129 psbt-flow not already secure-setup / not already members-checked / not already settled 正式三事（287 余量）/ not 1178 bsms129-notsetup interchangeable / not 287 setup-vs-psbt bundled interchangeable」，不是跨厂安全多签开户 bundled（287），也不是看见包就已经能广播（179），也不是登记过就已经批准这笔花（1162）。不要另写怎样核对钥或怎样加密会话。

## 官方三件事

1. **看见部分签名包 / 看见签流程 这份开户 is not already 已经是跨厂安全多签开户 interchangeable，也不是已经跨厂安全多签开户 bundled（287） interchangeable / 1178 bsms129-notsetup interchangeable / 1179 bsms129-notkey interchangeable / 287 bsms item 2 fp-not-key interchangeable，也不是已经 BIP-129 psbt-flow not already secure-setup / not already members-checked / not already settled 正式三事 bundled（287 item 1 余量） interchangeable / 287 bsms item 1 interchangeable。**  
   官方写：174 把多方签名体验理顺了。可是跨不同厂家安全开好多签钱包，还缺一份标准流程。看见包还能签，不是已经开过户。

2. **看见签流程 / 看见部分签名包 / 这份开户 is not already 已经核过成员、脚本类型、派生路径和门限 interchangeable，也不是已经跨厂安全多签开户 bundled（287） interchangeable / 1178 bsms129-notsetup interchangeable / 287 bsms item 3 token-not-seed interchangeable / 1180 bsms129-nottoken interchangeable，也不是已经登记过就已经批准这笔花 interchangeable / 1162 pol388-notreg interchangeable。**  
   官方另写：要管的是配置有没有被改、开户时钥和配置有没有漏出去、签名器有没有把配置存下来、用什么格式存。看见签流程齐了，不是成员名单已经核过。

3. **看见包还能签 / 看见部分签名包 / 这份开户 is not already 已经交差 interchangeable，也不是已经跨厂安全多签开户 bundled（287） interchangeable / 1178 bsms129-notsetup interchangeable / 1179 bsms129-notkey interchangeable，也不是已经看见包就已经能广播 interchangeable / 179 psbt interchangeable。**  
   官方把签流程和开户流程写成两件缺一不可的事。看见包还能签，不是已经交差。

记录行格式、加密配方、测试向量、描述符模板展开是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **部分签名包 不是已经是跨厂安全多签开户：** 官方把签流程和开户流程写成两件。
- **签流程 不是已经核过成员：** 官方把改配置、漏钥、存盘写成开户要管的事。
- **包还能签 不是已经交差：** 官方把还能签写成不是已经开过户。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 开户 | 不是已经是跨厂安全多签开户 | 不是已经能广播（179） |
| 成员 | 不是已经核过成员 | 不是已经批准这笔花（1162） |
| 交差 | 不是已经交差 | 不是已经核过 KEY（1179） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-129 psbt-flow not already secure-setup / not already members-checked / not already settled 正式三事（287 余量），必须分开是不是已经是跨厂安全多签开户、是不是已经核过成员、是不是已经交差。可以跳过「看见部分签名包就已经开好了多签」。不要另写怎样核对钥或怎样加密会话。287 setup vs psbt bundled unbundling 在本页 item 1 启动；续 [`worked-example-bsms129-notkey-vs-bundled.md`](worked-example-bsms129-notkey-vs-bundled.md)（不变量 1179 item 2）。

## 本页不抄

- 记录行格式、文件后缀、加密配方、TOKEN 宽度、测试向量、钥例、描述符模板展开。
- 怎样做精确比对、怎样造 TOKEN、怎样加密会话、怎样展开模板。
