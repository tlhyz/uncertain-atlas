# 例：看见 BIP32-compatible is not already interoperable interchangeable / not already same-tree interchangeable / not already settled interchangeable

**层次**：应用 / BIP-43 BIP32-compatible not already interoperable / not already same-tree / not already settled 正式三事（266 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-43](https://github.com/bitcoin/bips/blob/master/bip-0043.mediawiki)（Deployed, Applications）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-43 BIP32-compatible not already interoperable / not already same-tree / not already settled 正式三事（266 余量）/ not 1118 purp43-notinterop interchangeable / not 266 purpose-vs-compatible bundled interchangeable」，不是用途层 bundled（266），也不是扩展公钥就已经能花（182），也不是同一份种子就已经是同一条币（1115）。不要另写怎样选用途号或从种子扫账户。

## 官方三件事

1. **看见 BIP32 compatible / 看见自称兼容 这份栏 is not already 已经能互操作 interchangeable，也不是已经用途层 bundled（266） interchangeable / 1118 purp43-notinterop interchangeable / 1119 purp43-notstruct interchangeable / 266 purpose item 2 subset-not-struct interchangeable，也不是已经 BIP-43 BIP32-compatible not already interoperable / not already same-tree / not already settled 正式三事 bundled（266 item 1 余量） interchangeable / 266 purpose item 1 interchangeable。**  
   官方写：分层确定性钱包结构是体验和安全上的重要一步，但规范给实现留了太多自由度。多家实现都可以自称 BIP32 compatible，底下却长出不同的逻辑结构，彼此不能互操作。看见自称兼容，不是已经能互操作 interchangeable——本页从 266 item 1 侧钉 not already interoperable 单句。266 purpose vs compatible bundled unbundling 在本页 item 1 启动。

2. **看见都能从同一份种子长钥 / 看见自称兼容 / 这份栏 is not already 已经同一套树 interchangeable，也不是已经用途层 bundled（266） interchangeable / 1118 purp43-notinterop interchangeable / 266 purpose item 3 prefix-not-btc interchangeable / 1120 purp43-notbtc interchangeable，也不是已经扩展公钥就已经能花 interchangeable / 182 xpub interchangeable。**  
   官方把都能从同一份种子长钥和已经同一套树分开。看见都能从同一份种子长钥，不是已经同一套树 interchangeable。本页钉 not already same-tree 单句。

3. **看见这句话相当没用 / 看见自称兼容 / 这份栏 is not already 已经交差 interchangeable，也不是已经用途层 bundled（266） interchangeable / 1118 purp43-notinterop interchangeable / 1119 purp43-notstruct interchangeable，也不是已经同一份种子就已经是同一条币 interchangeable / 1115 acc44-notcoin interchangeable。**  
   官方把这句话相当没用和已经交差分开。看见这句话相当没用，不是已经交差 interchangeable。266 purpose vs compatible bundled unbundling 在本页 item 1 启动。

用途号怎么取、魔数怎么写、SLIP 预留段是规范里的取值，本页不抄。

## 官方为什么这样拆

- **BIP-43 BIP32-compatible not already interoperable ≠ 已经能互操作 interchangeable：** 官方把自称 BIP32 compatible 写成相当没用，因为逻辑结构可以不一样。
- **看见都能从同一份种子长钥 not already same-tree ≠ 已经同一套树 interchangeable：** 官方把都能从同一份种子长钥和已经同一套树分开。
- **看见这句话相当没用 not already settled ≠ 已经交差 interchangeable：** 官方把这句话相当没用和已经交差分开；266 purpose vs compatible bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| BIP32 compatible / 自称兼容 | 不是已经能互操作 | 不是扩展公钥就已经能花（182） |
| 看见都能从同一份种子长钥 | 不是已经同一套树 | 不是同一份种子就已经是同一条币（1115） |
| 看见这句话相当没用 | 不是已经交差 | 不是自称 BIPxx 就已经是那份结构（1119） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-43 BIP32-compatible not already interoperable / not already same-tree / not already settled 正式三事（266 余量），必须分开是不是已经能互操作、是不是已经同一套树、是不是已经交差。可以跳过「看见 BIP32 compatible 就已经能互操作」。不要另写怎样选用途号或从种子扫账户。266 purpose vs compatible bundled unbundling 在本页 item 1 启动；续 [`worked-example-purp43-notstruct-vs-bundled.md`](worked-example-purp43-notstruct-vs-bundled.md)（不变量 1119 item 2）。

## 本页不抄

- 用途号取值、例路径、扩展钥版本魔数、SLIP 预留段。
- 怎样给新方案申请用途、怎样从种子枚举账户。
- 用途层 bundled。那是不变量 266。
- 扩展公钥就已经能花。那是不变量 182。
