# 例：看见 same-xpub-prefix is not already bitcoin-only interchangeable / not already BIP32-default-account interchangeable / not already settled interchangeable

**层次**：应用 / BIP-43 same-xpub-prefix not already bitcoin-only / not already BIP32-default-account / not already settled 正式三事（266 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-43](https://github.com/bitcoin/bips/blob/master/bip-0043.mediawiki)（Deployed, Applications）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-43 same-xpub-prefix not already bitcoin-only / not already BIP32-default-account / not already settled 正式三事（266 余量）/ not 1120 purp43-notbtc interchangeable / not 266 purpose-vs-compatible bundled interchangeable」，不是用途层 bundled（266），也不是扩展公钥就已经能花（182），也不是 BIP-44 账户号就已经有过往（1116）。不要另写怎样选用途号或从种子扫账户。

## 官方三件事

1. **看见同一套扩展钥前缀 / 同一套版本魔数 这份栏 is not already 已经是比特币专用 interchangeable，也不是已经用途层 bundled（266） interchangeable / 1120 purp43-notbtc interchangeable / 1118 purp43-notinterop interchangeable / 266 purpose item 1 compat-not-interop interchangeable，也不是已经 BIP-43 same-xpub-prefix not already bitcoin-only / not already BIP32-default-account / not already settled 正式三事 bundled（266 item 3 余量） interchangeable / 266 purpose item 3 interchangeable。**  
   官方写：这套方案一次可以给多种币、甚至完全无关的东西长节点，所以没有必要再给扩展钥另写一套版本魔数；建议继续用同一套公钥 / 私钥前缀。看见还是那套前缀，不是已经是比特币专用 interchangeable——本页从 266 item 3 侧钉 not already bitcoin-only 单句。266 purpose vs compatible bundled unbundling 在本页 item 3 完成。

2. **看见默认账户支 / 看见同一套前缀 / 这份栏 is not already 已经是 BIP32 默认账户 interchangeable，也不是已经用途层 bundled（266） interchangeable / 1120 purp43-notbtc interchangeable / 266 purpose item 2 subset-not-struct interchangeable / 1119 purp43-notstruct interchangeable，也不是已经扩展公钥就已经能花 interchangeable / 182 xpub interchangeable。**  
   官方把默认账户支和已经是 BIP32 默认账户分开。看见默认账户支，不是已经是 BIP32 默认账户 interchangeable。本页钉 not already BIP32-default-account 单句。

3. **看见不必另开魔数 / 看见同一套前缀 / 这份栏 is not already 已经交差 interchangeable，也不是已经用途层 bundled（266） interchangeable / 1120 purp43-notbtc interchangeable / 1118 purp43-notinterop interchangeable，也不是已经 BIP-44 账户号就已经有过往 interchangeable / 1116 acc44-notpast interchangeable。**  
   官方把不必另开魔数和已经交差分开。看见不必另开魔数，不是已经交差 interchangeable。266 purpose vs compatible bundled unbundling 在本页 item 3 完成。

用途号怎么取、魔数怎么写、SLIP 预留段是规范里的取值，本页不抄。

## 官方为什么这样拆

- **BIP-43 same-xpub-prefix not already bitcoin-only ≠ 已经是比特币专用 interchangeable：** 官方把还能给别的币、甚至无关的东西长节点写成不必另开魔数。
- **看见默认账户支 not already BIP32-default-account ≠ 已经是 BIP32 默认账户 interchangeable：** 官方把默认账户支和已经是 BIP32 默认账户分开。
- **看见不必另开魔数 not already settled ≠ 已经交差 interchangeable：** 官方把不必另开魔数和已经交差分开；266 purpose vs compatible bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 同一套扩展钥前缀 / 同一套版本魔数 | 不是已经是比特币专用 | 不是扩展公钥就已经能花（182） |
| 看见默认账户支 | 不是已经是 BIP32 默认账户 | 不是 BIP-44 账户号就已经有过往（1116） |
| 看见不必另开魔数 | 不是已经交差 | 不是自称兼容就已经能互操作（1118） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-43 same-xpub-prefix not already bitcoin-only / not already BIP32-default-account / not already settled 正式三事（266 余量），必须分开是不是已经是比特币专用、是不是已经是 BIP32 默认账户、是不是已经交差。可以跳过「看见 BIP32 compatible 就已经能互操作」。不要另写怎样选用途号或从种子扫账户。266 purpose vs compatible bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 用途号取值、例路径、扩展钥版本魔数、SLIP 预留段。
- 怎样给新方案申请用途、怎样从种子枚举账户。
- 用途层 bundled。那是不变量 266。
- 扩展公钥就已经能花。那是不变量 182。
