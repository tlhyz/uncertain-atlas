# 例：看见旧软件报无效不是已经付过；看见它不肯造交易不是已经走了 16；看见失败温和不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-13](https://github.com/bitcoin/bips/blob/master/bip-0013.mediawiki)（Deployed, Applications, Specification）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-13 old-reject not already paid / not already 16 / not already settled 正式三事（297 余量）/ not 1209 p2sh13-notpaid interchangeable / not 297 p2sh-address-vs-redeem bundled interchangeable」，不是付给脚本哈希地址 bundled（297），也不是 Bech32 地址就已经有输出（174），也不是后继校验就已经是旧方案（181）。不要另写怎样按 Base58Check 编地址或怎样从版本字节认网。不要另写 BIP-12 / BIP-17。

## 官方三件事

1. **看见旧实现拿到本页这种地址 / 看见它报无效并拒绝造交易 这份地址 is not already 已经付过 interchangeable，也不是已经付给脚本哈希地址 bundled（297） interchangeable / 1209 p2sh13-notpaid interchangeable / 1208 p2sh13-not16 interchangeable / 297 p2sh item 1 addr-not-16 interchangeable，也不是已经 BIP-13 old-reject not already paid / not already 16 / not already settled 正式三事 bundled（297 item 2 余量） interchangeable / 297 p2sh item 2 interchangeable。**  
   官方写：本页和旧实现不往后兼容，但失败是温和的——旧实现拿到这种新地址，会报地址无效，并拒绝造交易。看见旧软件报无效，不是已经广播，也不是已经付过。

2. **看见它不肯造交易 / 看见旧软件报无效 / 这份地址 is not already 已经走了 16 interchangeable，也不是已经付给脚本哈希地址 bundled（297） interchangeable / 1209 p2sh13-notpaid interchangeable / 297 p2sh item 3 only-not-who interchangeable / 1210 p2sh13-notwho interchangeable，也不是已经 Bech32 地址就已经有输出 interchangeable / 174 address interchangeable。**  
   官方写：看见它不肯造交易，不是已经走了 16。官方把旧实现拒造交易写成温和失败，不是已经广播。

3. **看见失败温和 / 看见旧软件报无效 / 这份地址 is not already 已经交差 interchangeable，也不是已经付给脚本哈希地址 bundled（297） interchangeable / 1209 p2sh13-notpaid interchangeable / 1208 p2sh13-not16 interchangeable，也不是已经后继校验就已经是旧方案 interchangeable / 181 bech32m interchangeable。**  
   官方写：看见失败温和，不是新软件已经付过，也不是已经交差。

版本字节、开头字符、校验算法、编解码步骤是规范里的取值或做法，本页不抄。不要另写 BIP-12 / BIP-17。

## 官方为什么这样拆

- **旧软件报无效 不是已经付过：** 官方把报无效并拒绝造交易写成温和失败。
- **不肯造交易 不是已经走了 16：** 官方把拒造写成不是已经走花费规则。
- **失败温和 不是已经交差：** 官方把温和失败写成不是新软件已经付过。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 付过 | 不是已经付过 | 不是已经有输出（174） |
| 16 | 不是已经走了 16 | 不是已经是旧方案（181） |
| 交差 | 不是已经交差 | 不是已经是赎回（1208） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-13 old-reject not already paid / not already 16 / not already settled 正式三事（297 余量），必须分开是不是已经付过、是不是已经走了 16、是不是已经交差。可以跳过「看见这种地址就已经是 16」。不要另写怎样按 Base58Check 编地址或怎样从版本字节认网。不要另写 BIP-12 / BIP-17。297 p2sh address vs redeem bundled unbundling 在本页 item 2 续；续 [`worked-example-p2sh13-notwho-vs-bundled.md`](worked-example-p2sh13-notwho-vs-bundled.md)（不变量 1210 item 3）。

## 本页不抄

- 版本字节取值、开头字符、Base58Check 步骤、校验算法。
- 怎样造这种地址、怎样从版本字节认网、怎样从地址还原脚本哈希。
