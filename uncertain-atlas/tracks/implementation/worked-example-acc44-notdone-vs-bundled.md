# 例：看见 zero-balance is not already discovery-done interchangeable / not already no-later-account interchangeable / not already settled interchangeable

**层次**：应用 / BIP-44 zero-balance not already discovery-done / not already no-later-account / not already settled 正式三事（267 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-44](https://github.com/bitcoin/bips/blob/master/bip-0044.mediawiki)（Deployed, Applications）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-44 zero-balance not already discovery-done / not already no-later-account / not already settled 正式三事（267 余量）/ not 1117 acc44-notdone interchangeable / not 267 account-vs-discovered bundled interchangeable」，不是多账户层次 bundled（267），也不是描述符就已经知道脚本（184），也不是助记词就已经是二进制种子（183）。不要另写怎样扫间隙或枚举账户。

## 官方三件事

1. **看见余额为零 / 看见一串没用过的地址 这份栏 is not already 已经发现完 interchangeable，也不是已经多账户层次 bundled（267） interchangeable / 1117 acc44-notdone interchangeable / 1115 acc44-notcoin interchangeable / 267 account item 1 seed-not-coin interchangeable，也不是已经 BIP-44 zero-balance not already discovery-done / not already no-later-account / not already settled 正式三事 bundled（267 item 3 余量） interchangeable / 267 account item 3 interchangeable。**  
   官方写：从外面导进种子之后，软件应当按过往去发现账户。算法看的是交易过往，不是账户余额；一户总额可以是零，发现仍会继续。看见余额为零，不是已经发现完 interchangeable——本页从 267 item 3 侧钉 not already discovery-done 单句。267 account vs discovered bundled unbundling 在本页 item 3 完成。

2. **看见停搜 / 看见余额为零 / 这份栏 is not already 已经没有后面的账户 interchangeable，也不是已经多账户层次 bundled（267） interchangeable / 1117 acc44-notdone interchangeable / 267 account item 2 account-not-past interchangeable / 1116 acc44-notpast interchangeable，也不是已经描述符就已经知道脚本 interchangeable / 184 descriptor interchangeable。**  
   官方把停搜和已经没有后面的账户分开。看见停搜，不是已经没有后面的账户 interchangeable。本页钉 not already no-later-account 单句。

3. **看见只扫外链 / 看见余额为零 / 这份栏 is not already 已经交差 interchangeable，也不是已经多账户层次 bundled（267） interchangeable / 1117 acc44-notdone interchangeable / 1115 acc44-notcoin interchangeable，也不是已经助记词就已经是二进制种子 interchangeable / 183 mnemonic interchangeable。**  
   官方把只扫外链和已经交差分开。看见只扫外链，不是已经交差 interchangeable。267 account vs discovered bundled unbundling 在本页 item 3 完成。

间隙条数、用途号、币种表、例路径是规范里的取值，本页不抄。

## 官方为什么这样拆

- **BIP-44 zero-balance not already discovery-done ≠ 已经发现完 interchangeable：** 官方把发现写成看过往、不看余额。
- **看见停搜 not already no-later-account ≠ 已经没有后面的账户 interchangeable：** 官方把停搜和已经没有后面的账户分开。
- **看见只扫外链 not already settled ≠ 已经交差 interchangeable：** 官方把只扫外链和已经交差分开；267 account vs discovered bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 余额为零 / 一串没用过的地址 | 不是已经发现完 | 不是描述符就已经知道脚本（184） |
| 看见停搜 | 不是已经没有后面的账户 | 不是助记词就已经是二进制种子（183） |
| 看见只扫外链 | 不是已经交差 | 不是同一份种子就已经是同一条币（1115） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-44 zero-balance not already discovery-done / not already no-later-account / not already settled 正式三事（267 余量），必须分开是不是已经发现完、是不是已经没有后面的账户、是不是已经交差。可以跳过「看见余额为零就已经扫完」。不要另写怎样扫间隙或枚举账户。267 account vs discovered bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 用途号、间隙条数、币种登记表、例路径。
- 怎样扫外链、怎样从种子枚举账户、怎样按间隙停搜。
- 多账户层次 bundled。那是不变量 267。
- 描述符就已经知道脚本。那是不变量 184。
