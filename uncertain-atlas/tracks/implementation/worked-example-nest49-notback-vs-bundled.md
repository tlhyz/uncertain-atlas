# 例：看见 dedicated-account is not already backward-compatible interchangeable / not already same-household interchangeable / not already settled interchangeable

**层次**：应用 / BIP-49 dedicated-account not already backward-compatible / not already same-household / not already settled 正式三事（268 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-49](https://github.com/bitcoin/bips/blob/master/bip-0049.mediawiki)（Deployed, Applications）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-49 dedicated-account not already backward-compatible / not already same-household / not already settled 正式三事（268 余量）/ not 1125 nest49-notback interchangeable / not 268 nested-vs-same-account bundled interchangeable」，不是嵌套隔离见证挂在旧账户上 bundled（268），也不是 BIP32 compatible 就已经能互操作（1118），也不是用途层就已经能互操作（266）。不要另写怎样套脚本或从种子扫嵌套地址。

## 官方三件事

1. **看见专用隔离见证账户 / 换了用途 这份栏 is not already 已经向后兼容 interchangeable，也不是已经嵌套挂旧账户 bundled（268） interchangeable / 1125 nest49-notback interchangeable / 1124 nest49-notold interchangeable / 268 nested item 1 same-not-recover interchangeable，也不是已经 BIP-49 dedicated-account not already backward-compatible / not already same-household / not already settled 正式三事 bundled（268 item 2 余量） interchangeable / 268 nested item 2 interchangeable。**  
   官方写：用户需要另开专用的隔离见证账户，好让只有兼容本页的钱包才会发现并正确处理。本页按设计不向后兼容。看见专用账户，不是旧钱包已经能吃 interchangeable——本页从 268 item 2 侧钉 not already backward-compatible 单句。268 nested vs same-account bundled unbundling 在本页 item 2 续。

2. **看见换了用途 / 看见专用隔离见证账户 / 这份栏 is not already 已经是原来那户 interchangeable，也不是已经嵌套挂旧账户 bundled（268） interchangeable / 1125 nest49-notback interchangeable / 268 nested item 3 appeared-not-complete interchangeable / 1126 nest49-notbal interchangeable，也不是已经 BIP32 compatible 就已经能互操作 interchangeable / 1118 purp43-notinterop interchangeable。**  
   官方把换了用途和已经是原来那户分开。看见换了用途，不是已经是 BIP44 那户 interchangeable。本页钉 not already same-household 单句。

3. **看见不会本页的钱包根本发现不了这些账户 / 看见专用账户 / 这份栏 is not already 已经交差 interchangeable，也不是已经嵌套挂旧账户 bundled（268） interchangeable / 1125 nest49-notback interchangeable / 1124 nest49-notold interchangeable，也不是已经用途层就已经能互操作 interchangeable / 266 purpose interchangeable。**  
   官方把失败会更显眼写成故意选这条路的理由。看见不会本页的钱包根本发现不了这些账户，不是已经交差 interchangeable。268 nested vs same-account bundled unbundling 在本页 item 2 续。

用途号、扩展钥前缀、脚本套法、测试向量是规范里的取值，本页不抄。

## 官方为什么这样拆

- **BIP-49 dedicated-account not already backward-compatible ≠ 已经向后兼容 interchangeable：** 官方故意让不会本页的钱包完全发现不了。
- **看见换了用途 not already same-household ≠ 已经是原来那户 interchangeable：** 官方把换用途和已经是 BIP44 那户分开。
- **看见不会本页的钱包根本发现不了这些账户 not already settled ≠ 已经交差 interchangeable：** 官方把失败更显眼写成故意选这条路的理由；268 nested vs same-account bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 专用隔离见证账户 / 换了用途 | 不是已经向后兼容 | 不是 BIP32 compatible 就已经能互操作（1118） |
| 看见换了用途 | 不是已经是原来那户 | 不是用途层就已经能互操作（266） |
| 看见不会本页的钱包根本发现不了这些账户 | 不是已经交差 | 不是账户出现了就已经齐（1126） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-49 dedicated-account not already backward-compatible / not already same-household / not already settled 正式三事（268 余量），必须分开是不是已经向后兼容、是不是已经是原来那户、是不是已经交差。可以跳过「看见旧账户还在就已经找回新脚本」。不要另写怎样套脚本或从种子扫嵌套地址。268 nested vs same-account bundled unbundling 在本页 item 2 续；续 [`worked-example-nest49-notbal-vs-bundled.md`](worked-example-nest49-notbal-vs-bundled.md)（不变量 1126 item 3）。

## 本页不抄

- 用途号、扩展钥版本魔数、脚本套法、测试向量、例地址。
- 怎样从同一批钥编出嵌套地址、怎样扫未花输出。
- 嵌套隔离见证挂在旧账户上 bundled。那是不变量 268。
- BIP32 compatible 就已经能互操作。那是不变量 1118。
