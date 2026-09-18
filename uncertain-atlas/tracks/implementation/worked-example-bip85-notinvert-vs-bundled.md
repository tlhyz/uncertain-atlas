# 例：看见 xprv-root is not already invertible-to-mnemonic interchangeable / not already the-entropy interchangeable / not already settled interchangeable

**层次**：应用 / BIP-85 xprv-root not already invertible-to-mnemonic / not already the-entropy / not already settled 正式三事（286 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-85](https://github.com/bitcoin/bips/blob/master/bip-0085.mediawiki)（Deployed, Applications, Informational）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-85 xprv-root not already invertible-to-mnemonic / not already the-entropy / not already settled 正式三事（286 余量）/ not 1122 bip85-notinvert interchangeable / not 286 entropy-vs-seed bundled interchangeable」，不是从一把扩展根钥导出熵 bundled（286），也不是扩展公钥就已经能花（182），也不是助记词就已经是二进制种子（183）。不要另写怎样从子钥算出熵。

## 官方三件事

1. **看见扩展根钥 / 看见派生出的子私钥 这份栏 is not already 已经能倒回助记词 interchangeable，也不是已经导出熵 bundled（286） interchangeable / 1122 bip85-notinvert interchangeable / 1121 bip85-notcover interchangeable / 286 entropy item 1 one-not-cover interchangeable，也不是已经 BIP-85 xprv-root not already invertible-to-mnemonic / not already the-entropy / not already settled 正式三事 bundled（286 item 2 余量） interchangeable / 286 entropy item 2 interchangeable。**  
   官方写：存下助记词就够重建整棵 32 钥链，但扩展根钥不能倒回助记词。看见扩展根钥，不是已经能倒回助记词 interchangeable——本页从 286 item 2 侧钉 not already invertible-to-mnemonic 单句。286 entropy vs seed bundled unbundling 在本页 item 2 续。

2. **看见子私钥 / 看见扩展根钥 / 这份栏 is not already 已经是那份熵 interchangeable，也不是已经导出熵 bundled（286） interchangeable / 1122 bip85-notinvert interchangeable / 286 entropy item 3 entropy-not-target interchangeable / 1123 bip85-nottarget interchangeable，也不是已经扩展公钥就已经能花 interchangeable / 182 xpub interchangeable。**  
   官方把子私钥和已经是那份熵分开。看见子私钥，不是已经是那份熵 interchangeable。本页钉 not already the-entropy 单句。

3. **看见本页不关心这把根钥当初怎么来 / 看见扩展根钥 / 这份栏 is not already 已经交差 interchangeable，也不是已经导出熵 bundled（286） interchangeable / 1122 bip85-notinvert interchangeable / 1121 bip85-notcover interchangeable，也不是已经助记词就已经是二进制种子 interchangeable / 183 mnemonic interchangeable。**  
   官方把本页不关心来源和已经交差分开。看见本页不关心这把根钥当初怎么来，不是已经交差 interchangeable。286 entropy vs seed bundled unbundling 在本页 item 2 续。

应用编号、路径常数、测试向量、例句、变换配方是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **BIP-85 xprv-root not already invertible-to-mnemonic ≠ 已经能倒回助记词 interchangeable：** 官方把助记词能重建钥链、根钥不能倒回写成两步。
- **看见子私钥 not already the-entropy ≠ 已经是那份熵 interchangeable：** 官方把子钥还要再变成熵写成另一步。
- **看见本页不关心来源 not already settled ≠ 已经交差 interchangeable：** 官方把本页不关心来源和已经交差分开；286 entropy vs seed bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 扩展根钥 / 派生出的子私钥 | 不是已经能倒回助记词 | 不是扩展公钥就已经能花（182） |
| 看见子私钥 | 不是已经是那份熵 | 不是助记词就已经是二进制种子（183） |
| 看见本页不关心来源 | 不是已经交差 | 不是派生出的熵就已经是目标种子（1123） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-85 xprv-root not already invertible-to-mnemonic / not already the-entropy / not already settled 正式三事（286 余量），必须分开是不是已经能倒回助记词、是不是已经是那份熵、是不是已经交差。可以跳过「看见一份种子就已经能喂给所有钱包」。不要另写怎样从子钥算出熵。286 entropy vs seed bundled unbundling 在本页 item 2 续；续 [`worked-example-bip85-nottarget-vs-bundled.md`](worked-example-bip85-nottarget-vs-bundled.md)（不变量 1123 item 3）。

## 本页不抄

- 应用编号、路径常数、测试向量、例句、变换配方。
- 怎样硬化派生、怎样做 HMAC、怎样截比特、怎样再喂进目标标准。
- 从一把扩展根钥导出熵 bundled。那是不变量 286。
- 扩展公钥就已经能花。那是不变量 182。
