# 例：看见未压缩钥不是已经带齐见证对；看见永远有两份不是已经有四份；看见总是那两份旧脚本不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-384](https://github.com/bitcoin/bips/blob/master/bip-0384.mediawiki)（Deployed, Applications, Informational）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-384 uncompressed-key not already have-witness-pair / not already fixed-four / not already settled 正式三事（281 余量）/ not 1164 combo384-notwitpair interchangeable / not 281 combo-vs-one-script bundled interchangeable」，不是 combo 描述符 bundled（281），也不是未压缩钥就已经允许进 wpkh（1152），也不是看见描述符就已经是地址（184）。不要另写怎样拼那几份输出脚本。

## 官方三件事

1. **看见未压缩钥 / 看见总是那两份旧脚本 这份栏 is not already 已经带齐见证对 interchangeable，也不是已经 combo 描述符 bundled（281） interchangeable / 1164 combo384-notwitpair interchangeable / 1163 combo384-notone interchangeable / 281 combo item 1 combo-not-one interchangeable，也不是已经 BIP-384 uncompressed-key not already have-witness-pair / not already fixed-four / not already settled 正式三事 bundled（281 item 2 余量） interchangeable / 281 combo item 2 interchangeable。**  
   官方写：combo 永远产出 P2PK 和 P2PKH。只有钥本身是或能长出压缩公钥时，才再产出 P2WPKH 和 P2SH-P2WPKH。看见未压缩钥，不是已经有那一对见证脚本。

2. **看见永远有两份 / 看见未压缩钥 / 这份栏 is not already 已经有四份 interchangeable，也不是已经 combo 描述符 bundled（281） interchangeable / 1164 combo384-notwitpair interchangeable / 281 combo item 3 combo-not-pol interchangeable / 1165 combo384-notpol interchangeable，也不是已经未压缩钥就已经允许进 wpkh interchangeable / 1152 wpkh382-notuncomp interchangeable。**  
   官方把见证那一对写成只在压缩钥时才出现。看见永远有两份，不是已经有四份。

3. **看见总是那两份旧脚本 / 看见未压缩钥 / 这份栏 is not already 已经交差 interchangeable，也不是已经 combo 描述符 bundled（281） interchangeable / 1164 combo384-notwitpair interchangeable / 1163 combo384-notone interchangeable，也不是已经看见描述符就已经是地址 interchangeable / 184 descriptor interchangeable。**  
   官方把 P2PK / P2PKH 写成永远有，见证对另写成条件。看见总是那两份旧脚本，不是已经交差。

脚本模板、测试向量、例钥、十六进制脚本是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **未压缩钥 不是已经带齐见证对：** 官方把见证对写成只在压缩钥时才出现。
- **永远有两份 不是已经有四份：** 官方把四份写成压缩钥才另出。
- **总是那两份旧脚本 不是已经交差：** 官方把永远两份和条件四份写成两句。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 见证对 | 不是已经带齐 | 不是已经允许进 wpkh（1152） |
| 四份 | 不是已经固定四份 | 不是已经是一份钱包策略（1165） |
| 交差 | 不是已经交差 | 不是已经是地址（184） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-384 uncompressed-key not already have-witness-pair / not already fixed-four / not already settled 正式三事（281 余量），必须分开是不是已经带齐见证对、是不是已经有四份、是不是已经交差。可以跳过「看见一把钥就已经是一种输出脚本」。不要另写怎样拼那几份输出脚本。281 combo vs one-script bundled unbundling 在本页 item 2 续；续 [`worked-example-combo384-notpol-vs-bundled.md`](worked-example-combo384-notpol-vs-bundled.md)（不变量 1165 item 3）。

## 本页不抄

- 脚本模板、测试向量、例钥、十六进制脚本。
- 怎样拼 P2PK / P2PKH / P2WPKH / P2SH-P2WPKH、怎样判断压缩、怎样嵌套。
