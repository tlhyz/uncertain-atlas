# 例：看见 derived-key is not already output-key interchangeable / not already witness-32 interchangeable / not already settled interchangeable

**层次**：应用 / BIP-86 derived-key not already output-key / not already witness-32 / not already settled 正式三事（272 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-86](https://github.com/bitcoin/bips/blob/master/bip-0086.mediawiki)（Deployed, Applications）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-86 derived-key not already output-key / not already witness-32 / not already settled 正式三事（272 余量）/ not 1136 tap86-notout interchangeable / not 272 derived-vs-output-key bundled interchangeable」，不是单钥 P2TR 派生 bundled（272），也不是钥匙路径就已经揭开有没有树（153），也不是同一套 BIP44 账户就已经能找回嵌套（1124）。不要另写怎样算标签微调，也不要另写 BIP-84。

## 官方三件事

1. **看见派生钥 / 看见 BIP32 路径 这份栏 is not already 已经是输出钥 interchangeable，也不是已经单钥 P2TR 派生 bundled（272） interchangeable / 1136 tap86-notout interchangeable / 1137 tap86-notcommit interchangeable / 272 derived item 2 path-not-uncommitted interchangeable，也不是已经 BIP-86 derived-key not already output-key / not already witness-32 / not already settled 正式三事 bundled（272 item 1 余量） interchangeable / 272 derived item 1 interchangeable。**  
   官方写：本页先按与 44 / 49 / 84 同一套账户结构长出一把派生钥，再把这把派生钥当成内部钥。输出钥是内部钥再加上对内部钥做标签微调后的点。看见路径对上了，不是已经对上了输出钥 interchangeable——本页从 272 item 1 侧钉 not already output-key 单句。272 derived vs output-key bundled unbundling 在本页 item 1 启动。

2. **看见内部钥 / 看见派生钥 / 这份栏 is not already 已经是见证里那 32 字节 interchangeable，也不是已经单钥 P2TR 派生 bundled（272） interchangeable / 1136 tap86-notout interchangeable / 272 derived item 3 seed-not-recover interchangeable / 1138 tap86-notseed interchangeable，也不是已经钥匙路径就已经揭开有没有树 interchangeable / 153 keypath interchangeable。**  
   官方把内部钥和见证里那 32 字节分开。看见内部钥，不是已经是见证里那 32 字节 interchangeable。本页钉 not already witness-32 单句。

3. **看见路径对上了 / 看见派生钥 / 这份栏 is not already 已经交差 interchangeable，也不是已经单钥 P2TR 派生 bundled（272） interchangeable / 1136 tap86-notout interchangeable / 1137 tap86-notcommit interchangeable，也不是已经同一套 BIP44 账户就已经能找回嵌套 interchangeable / 1124 nest49-notold interchangeable。**  
   官方把同一套 44 / 49 / 84 账户结构写成方法相同，不是已经交差。看见路径对上了，不是已经交差 interchangeable。272 derived vs output-key bundled unbundling 在本页 item 1 启动。

用途号、测试向量、地址例、怎样算标签微调是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **BIP-86 derived-key not already output-key ≠ 已经是输出钥 interchangeable：** 官方把内部钥和输出钥写成两步。
- **看见内部钥 not already witness-32 ≠ 已经是见证里那 32 字节 interchangeable：** 官方把内部钥和见证里那 32 字节分开。
- **看见路径对上了 not already settled ≠ 已经交差 interchangeable：** 官方把同一套账户结构写成方法相同，不是已经交差；272 derived vs output-key bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 派生钥 / BIP32 路径 | 不是已经是输出钥 | 不是钥匙路径就已经揭开有没有树（153） |
| 看见内部钥 | 不是已经是见证里那 32 字节 | 不是同一套 BIP44 账户就已经能找回嵌套（1124） |
| 看见路径对上了 | 不是已经交差 | 不是不需要脚本路径就已经不承诺（1137） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-86 derived-key not already output-key / not already witness-32 / not already settled 正式三事（272 余量），必须分开是不是已经是输出钥、是不是已经是见证里那 32 字节、是不是已经交差。可以跳过「看见种子就已经能找回 Taproot」。不要另写怎样算标签微调，也不要另写 BIP-84。272 derived vs output-key bundled unbundling 在本页 item 1 启动；续 [`worked-example-tap86-notcommit-vs-bundled.md`](worked-example-tap86-notcommit-vs-bundled.md)（不变量 1137 item 2）。

## 本页不抄

- 用途号、测试向量、地址例、助记词例、扩展钥例。
- 怎样算标签微调、怎样 lift、怎样拼见证。
- 单钥 P2TR 派生 bundled。那是不变量 272。
- 钥匙路径就已经揭开有没有树。那是不变量 153。
