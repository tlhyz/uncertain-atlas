# 例：看见 next-account-number is not already has-history interchangeable / not already same-identity interchangeable / not already settled interchangeable

**层次**：应用 / BIP-44 next-account-number not already has-history / not already same-identity / not already settled 正式三事（267 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-44](https://github.com/bitcoin/bips/blob/master/bip-0044.mediawiki)（Deployed, Applications）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-44 next-account-number not already has-history / not already same-identity / not already settled 正式三事（267 余量）/ not 1116 acc44-notpast interchangeable / not 267 account-vs-discovered bundled interchangeable」，不是多账户层次 bundled（267），也不是 BIP32 compatible 就已经能互操作（266），也不是嵌套隔离见证就已经是同一套账户（nested-vs-same-account）。不要另写怎样扫间隙或枚举账户。

## 官方三件事

1. **看见下一个账户号 / 去开新账户 这份栏 is not already 已经有过往 interchangeable，也不是已经多账户层次 bundled（267） interchangeable / 1116 acc44-notpast interchangeable / 1115 acc44-notcoin interchangeable / 267 account item 1 seed-not-coin interchangeable，也不是已经 BIP-44 next-account-number not already has-history / not already same-identity / not already settled 正式三事 bundled（267 item 2 余量） interchangeable / 267 account item 2 interchangeable。**  
   官方写：这一层把钥空间拆成彼此独立的用户身份，钱包不得把不同账户的币混在一起。软件应当阻止去开新账户，只要上一户还没有交易过往。看见账户号往上加，不是已经有过往 interchangeable——本页从 267 item 2 侧钉 not already has-history 单句。267 account vs discovered bundled unbundling 在本页 item 2 续。

2. **看见两户 / 看见下一个账户号 / 这份栏 is not already 已经和上一户同一身份 interchangeable，也不是已经多账户层次 bundled（267） interchangeable / 1116 acc44-notpast interchangeable / 267 account item 3 zero-not-done interchangeable / 1117 acc44-notdone interchangeable，也不是已经 BIP32 compatible 就已经能互操作 interchangeable / 266 purpose interchangeable。**  
   官方把两户和已经和上一户同一身份分开。看见两户，不是已经和上一户同一身份 interchangeable。本页钉 not already same-identity 单句。

3. **看见不得混花 / 看见下一个账户号 / 这份栏 is not already 已经交差 interchangeable，也不是已经多账户层次 bundled（267） interchangeable / 1116 acc44-notpast interchangeable / 1115 acc44-notcoin interchangeable，也不是已经嵌套隔离见证就已经是同一套账户 interchangeable / nested-vs-same-account interchangeable。**  
   官方把不得混花和已经交差分开。看见不得混花，不是已经交差 interchangeable。267 account vs discovered bundled unbundling 在本页 item 2 续。

间隙条数、用途号、币种表、例路径是规范里的取值，本页不抄。

## 官方为什么这样拆

- **BIP-44 next-account-number not already has-history ≠ 已经有过往 interchangeable：** 官方要求上一户还没有交易过往时，不得开新户。
- **看见两户 not already same-identity ≠ 已经和上一户同一身份 interchangeable：** 官方把两户和已经和上一户同一身份分开。
- **看见不得混花 not already settled ≠ 已经交差 interchangeable：** 官方把不得混花和已经交差分开；267 account vs discovered bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 下一个账户号 / 去开新账户 | 不是已经有过往 | 不是 BIP32 compatible 就已经能互操作（266） |
| 看见两户 | 不是已经和上一户同一身份 | 不是嵌套隔离见证就已经是同一套账户 |
| 看见不得混花 | 不是已经交差 | 不是余额为零就已经发现完（1117） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-44 next-account-number not already has-history / not already same-identity / not already settled 正式三事（267 余量），必须分开是不是已经有过往、是不是已经和上一户同一身份、是不是已经交差。可以跳过「看见余额为零就已经扫完」。不要另写怎样扫间隙或枚举账户。267 account vs discovered bundled unbundling 在本页 item 2 续；续 [`worked-example-acc44-notdone-vs-bundled.md`](worked-example-acc44-notdone-vs-bundled.md)（不变量 1117 item 3）。

## 本页不抄

- 用途号、间隙条数、币种登记表、例路径。
- 怎样扫外链、怎样从种子枚举账户、怎样按间隙停搜。
- 多账户层次 bundled。那是不变量 267。
- BIP32 compatible 就已经能互操作。那是不变量 266。
