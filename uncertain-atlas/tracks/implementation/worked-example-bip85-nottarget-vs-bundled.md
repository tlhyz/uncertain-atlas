# 例：看见 derived-entropy is not already target-wallet-seed interchangeable / not already this-tree-key interchangeable / not already settled interchangeable

**层次**：应用 / BIP-85 derived-entropy not already target-wallet-seed / not already this-tree-key / not already settled 正式三事（286 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-85](https://github.com/bitcoin/bips/blob/master/bip-0085.mediawiki)（Deployed, Applications, Informational）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-85 derived-entropy not already target-wallet-seed / not already this-tree-key / not already settled 正式三事（286 余量）/ not 1123 bip85-nottarget interchangeable / not 286 entropy-vs-seed bundled interchangeable」，不是从一把扩展根钥导出熵 bundled（286），也不是助记词就已经是二进制种子（183），也不是同一份种子就已经是同一条币（1115）。不要另写怎样从子钥算出熵。

## 官方三件事

1. **看见派生出的熵 / 看见截过的比特 这份栏 is not already 已经是目标钱包的种子 interchangeable，也不是已经导出熵 bundled（286） interchangeable / 1123 bip85-nottarget interchangeable / 1121 bip85-notcover interchangeable / 286 entropy item 1 one-not-cover interchangeable，也不是已经 BIP-85 derived-entropy not already target-wallet-seed / not already this-tree-key / not already settled 正式三事 bundled（286 item 3 余量） interchangeable / 286 entropy item 3 interchangeable。**  
   官方写：用 32 本身导出「初始熵」，再按目标钱包自己的标准去造助记词或种子。看见导出了熵，不是已经是目标钱包的种子 interchangeable——本页从 286 item 3 侧钉 not already target-wallet-seed 单句。286 entropy vs seed bundled unbundling 在本页 item 3 完成。

2. **看见给另一个应用用了 / 看见派生出的熵 / 这份栏 is not already 已经是本钱包里的钥 interchangeable，也不是已经导出熵 bundled（286） interchangeable / 1123 bip85-nottarget interchangeable / 286 entropy item 2 root-not-invert interchangeable / 1122 bip85-notinvert interchangeable，也不是已经助记词就已经是二进制种子 interchangeable / 183 mnemonic interchangeable。**  
   官方把给另一个应用用了和已经是本钱包里的钥分开。看见给另一个应用用了，不是已经是本钱包里的钥 interchangeable。本页钉 not already this-tree-key 单句。

3. **看见其余截掉 / 看见派生出的熵 / 这份栏 is not already 已经交差 interchangeable，也不是已经导出熵 bundled（286） interchangeable / 1123 bip85-nottarget interchangeable / 1121 bip85-notcover interchangeable，也不是已经同一份种子就已经是同一条币 interchangeable / 1115 acc44-notcoin interchangeable。**  
   官方把其余截掉和已经交差分开。看见其余截掉，不是已经交差 interchangeable。286 entropy vs seed bundled unbundling 在本页 item 3 完成。

应用编号、路径常数、测试向量、例句、变换配方是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **BIP-85 derived-entropy not already target-wallet-seed ≠ 已经是目标钱包的种子 interchangeable：** 官方把本页熵写成只是目标标准的输入，不是已经长出那棵树。
- **看见给另一个应用用了 not already this-tree-key ≠ 已经是本钱包里的钥 interchangeable：** 官方把给另一个应用用了和已经是本钱包里的钥分开。
- **看见其余截掉 not already settled ≠ 已经交差 interchangeable：** 官方把其余截掉和已经交差分开；286 entropy vs seed bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 派生出的熵 / 截过的比特 | 不是已经是目标钱包的种子 | 不是助记词就已经是二进制种子（183） |
| 看见给另一个应用用了 | 不是已经是本钱包里的钥 | 不是同一份种子就已经是同一条币（1115） |
| 看见其余截掉 | 不是已经交差 | 不是一份助记词就已经能备齐所有钱包（1121） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-85 derived-entropy not already target-wallet-seed / not already this-tree-key / not already settled 正式三事（286 余量），必须分开是不是已经是目标钱包的种子、是不是已经是本钱包里的钥、是不是已经交差。可以跳过「看见一份种子就已经能喂给所有钱包」。不要另写怎样从子钥算出熵。286 entropy vs seed bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 应用编号、路径常数、测试向量、例句、变换配方。
- 怎样硬化派生、怎样做 HMAC、怎样截比特、怎样再喂进目标标准。
- 从一把扩展根钥导出熵 bundled。那是不变量 286。
- 助记词就已经是二进制种子。那是不变量 183。
