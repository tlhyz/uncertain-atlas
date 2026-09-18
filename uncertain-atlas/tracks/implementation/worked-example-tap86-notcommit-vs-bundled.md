# 例：看见 no-script-path-needed is not already uncommitted interchangeable / not already no-script-path interchangeable / not already settled interchangeable

**层次**：应用 / BIP-86 no-script-path-needed not already uncommitted / not already no-script-path / not already settled 正式三事（272 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-86](https://github.com/bitcoin/bips/blob/master/bip-0086.mediawiki)（Deployed, Applications）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-86 no-script-path-needed not already uncommitted / not already no-script-path / not already settled 正式三事（272 余量）/ not 1137 tap86-notcommit interchangeable / not 272 derived-vs-output-key bundled interchangeable」，不是单钥 P2TR 派生 bundled（272），也不是已经是 tapscript 语义（189），也不是未压缩钥就已经是本页（1135）。不要另写怎样算标签微调，也不要另写 BIP-84。

## 官方三件事

1. **看见不需要脚本路径 / 看见单钥 这份栏 is not already 已经不承诺脚本路径 interchangeable，也不是已经单钥 P2TR 派生 bundled（272） interchangeable / 1137 tap86-notcommit interchangeable / 1136 tap86-notout interchangeable / 272 derived item 1 derived-not-output interchangeable，也不是已经 BIP-86 no-script-path-needed not already uncommitted / not already no-script-path / not already settled 正式三事 bundled（272 item 2 余量） interchangeable / 272 derived item 2 interchangeable。**  
   官方引用 341：若花费条件并不需要脚本路径，输出钥仍应当承诺一条不可花的脚本路径，而不是没有脚本路径。看见不需要脚本路径，不是已经不承诺 interchangeable——本页从 272 item 2 侧钉 not already uncommitted 单句。272 derived vs output-key bundled unbundling 在本页 item 2 续。

2. **看见单钥 / 看见不需要脚本路径 / 这份栏 is not already 已经是没有脚本路径那种输出 interchangeable，也不是已经单钥 P2TR 派生 bundled（272） interchangeable / 1137 tap86-notcommit interchangeable / 272 derived item 3 seed-not-recover interchangeable / 1138 tap86-notseed interchangeable，也不是已经是 tapscript 语义 interchangeable / 189 tapscript interchangeable。**  
   官方把单钥和已经可以不微调分开。看见单钥，不是已经可以不微调 interchangeable。本页钉 not already no-script-path 单句。

3. **看见仍应当承诺一条不可花的脚本路径 / 看见不需要脚本路径 / 这份栏 is not already 已经交差 interchangeable，也不是已经单钥 P2TR 派生 bundled（272） interchangeable / 1137 tap86-notcommit interchangeable / 1136 tap86-notout interchangeable，也不是已经未压缩钥就已经是本页 interchangeable / 1135 sort67-notuncomp interchangeable。**  
   官方把仍应当承诺一条不可花脚本路径写成 341 的要求，不是已经交差。看见仍应当承诺一条不可花的脚本路径，不是已经交差 interchangeable。272 derived vs output-key bundled unbundling 在本页 item 2 续。

用途号、测试向量、地址例、怎样算标签微调是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **BIP-86 no-script-path-needed not already uncommitted ≠ 已经不承诺脚本路径 interchangeable：** 官方把仍应当承诺一条不可花脚本路径写成 341 的要求。
- **看见单钥 not already no-script-path ≠ 已经是没有脚本路径那种输出 interchangeable：** 官方把单钥和已经可以不微调分开。
- **看见仍应当承诺一条不可花的脚本路径 not already settled ≠ 已经交差 interchangeable：** 官方把 341 的要求和已经交差分开；272 derived vs output-key bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 不需要脚本路径 / 单钥 | 不是已经不承诺脚本路径 | 不是已经是 tapscript 语义（189） |
| 看见单钥 | 不是已经是没有脚本路径那种输出 | 不是未压缩钥就已经是本页（1135） |
| 看见仍应当承诺一条不可花的脚本路径 | 不是已经交差 | 不是种子备份就已经能找回（1138） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-86 no-script-path-needed not already uncommitted / not already no-script-path / not already settled 正式三事（272 余量），必须分开是不是已经不承诺脚本路径、是不是已经是没有脚本路径那种输出、是不是已经交差。可以跳过「看见种子就已经能找回 Taproot」。不要另写怎样算标签微调，也不要另写 BIP-84。272 derived vs output-key bundled unbundling 在本页 item 2 续；续 [`worked-example-tap86-notseed-vs-bundled.md`](worked-example-tap86-notseed-vs-bundled.md)（不变量 1138 item 3）。

## 本页不抄

- 用途号、测试向量、地址例、助记词例、扩展钥例。
- 怎样算标签微调、怎样 lift、怎样拼见证。
- 单钥 P2TR 派生 bundled。那是不变量 272。
- 已经是 tapscript 语义。那是不变量 189。
