# 例：看见未压缩钥不是已经允许进 wpkh；看见任意钥不是已经允许出现在 wsh 下面；看见 381 还收未压缩不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-382](https://github.com/bitcoin/bips/blob/master/bip-0382.mediawiki)（Deployed, Applications, Informational）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-382 uncompressed-key not already allowed-in-wpkh / not already allowed-under-wsh / not already settled 正式三事（277 余量）/ not 1152 wpkh382-notuncomp interchangeable / not 277 wpkh-vs-compressed bundled interchangeable」，不是隔离见证描述符 bundled（277），也不是压缩钥就已经是 x-only（1147），也不是看见描述符就已经是地址（184）。不要另写怎样拼见证程序。

## 官方三件事

1. **看见未压缩钥 / 看见任意钥 这份栏 is not already 已经允许进 wpkh interchangeable，也不是已经隔离见证描述符 bundled（277） interchangeable / 1152 wpkh382-notuncomp interchangeable / 1151 wpkh382-nottop interchangeable / 277 wpkh item 1 wpkh-not-top interchangeable，也不是已经 BIP-382 uncompressed-key not already allowed-in-wpkh / not already allowed-under-wsh / not already settled 正式三事 bundled（277 item 2 余量） interchangeable / 277 wpkh item 2 interchangeable。**  
   官方写：`wpkh` 里只能放本身是压缩公钥、或能长出压缩公钥的钥。看见未压缩钥，不是已经允许进 `wpkh`。

2. **看见任意钥 / 看见未压缩钥 / 这份栏 is not already 已经允许出现在 wsh 下面 interchangeable，也不是已经隔离见证描述符 bundled（277） interchangeable / 1152 wpkh382-notuncomp interchangeable / 277 wpkh item 3 wsh-not-wit interchangeable / 1153 wpkh382-notwit interchangeable，也不是已经压缩钥就已经是 x-only interchangeable / 1147 tr386-notxonly interchangeable。**  
   官方写：`wsh` 下面任何一层脚本表达式里出现的钥表达式，都只能产出压缩公钥。看见任意钥，不是已经允许出现在 `wsh` 下面。

3. **看见 381 还收未压缩 / 看见未压缩钥 / 这份栏 is not already 已经交差 interchangeable，也不是已经隔离见证描述符 bundled（277） interchangeable / 1152 wpkh382-notuncomp interchangeable / 1151 wpkh382-nottop interchangeable，也不是已经看见描述符就已经是地址 interchangeable / 184 descriptor interchangeable。**  
   官方把压缩写成 `wpkh` 和 `wsh` 下面的硬条件。看见 381 还收未压缩，不是已经是本页，也不是已经交差。

脚本模板、测试向量、例钥、十六进制脚本是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **未压缩钥 不是已经允许进 wpkh：** 官方把 wpkh 写成只收压缩钥。
- **任意钥 不是已经允许出现在 wsh 下面：** 官方把 wsh 下面写成只能产出压缩公钥。
- **381 还收未压缩 不是已经交差：** 官方把本页压缩条件写成独立一句。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| wpkh 压缩 | 不是已经允许未压缩 | 不是已经是 x-only（1147） |
| wsh 下面 | 不是已经允许任意钥 | 不是已经有见证脚本（1153） |
| 交差 | 不是已经交差 | 不是已经是地址（184） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-382 uncompressed-key not already allowed-in-wpkh / not already allowed-under-wsh / not already settled 正式三事（277 余量），必须分开是不是已经允许进 wpkh、是不是已经允许出现在 wsh 下面、是不是已经交差。可以跳过「看见隔离见证表达式就已经是 381 那套放置」。不要另写怎样拼见证程序。277 wpkh vs compressed bundled unbundling 在本页 item 2 续；续 [`worked-example-wpkh382-notwit-vs-bundled.md`](worked-example-wpkh382-notwit-vs-bundled.md)（不变量 1153 item 3）。

## 本页不抄

- 脚本模板、测试向量、例钥、十六进制脚本。
- 怎样算 HASH160 / SHA256、怎样拼见证程序、怎样嵌套。
