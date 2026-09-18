# 例：看见只有本页这种地址不是已经知道付给谁；看见地址上没有身份不是已经核过收款人；看见本页已部署不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-13](https://github.com/bitcoin/bips/blob/master/bip-0013.mediawiki)（Deployed, Applications, Specification）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-13 address-only not already know-payee / not already identity / not already settled 正式三事（297 余量）/ not 1210 p2sh13-notwho interchangeable / not 297 p2sh-address-vs-redeem bundled interchangeable」，不是付给脚本哈希地址 bundled（297），也不是同一套钥就已经是同一条 P2SH 地址（270），也不是付给脚本哈希就已经揭开赎回（170）。不要另写怎样按 Base58Check 编地址或怎样从版本字节认网。不要另写 BIP-12 / BIP-17。

## 官方三件事

1. **看见只有本页这种地址 / 看见地址上没有身份 这份地址 is not already 已经知道付给谁 interchangeable，也不是已经付给脚本哈希地址 bundled（297） interchangeable / 1210 p2sh13-notwho interchangeable / 1208 p2sh13-not16 interchangeable / 297 p2sh item 1 addr-not-16 interchangeable，也不是已经 BIP-13 address-only not already know-payee / not already identity / not already settled 正式三事 bundled（297 item 3 余量） interchangeable / 297 p2sh item 3 interchangeable。**  
   官方动机写：让钱包能端到端付钱给托管或其它复杂条件，也让第三方钱包安保能接。官方理由另写：有人批评地址本身没有身份信息；只有地址，怎么确定付给的是你以为的那一方？看见只有地址，不是已经核过收款人，也不是已经知道付给谁。

2. **看见地址上没有身份 / 看见只有本页这种地址 / 这份地址 is not already 已经核过收款人 interchangeable，也不是已经付给脚本哈希地址 bundled（297） interchangeable / 1210 p2sh13-notwho interchangeable / 297 p2sh item 2 old-not-paid interchangeable / 1209 p2sh13-notpaid interchangeable，也不是已经同一套钥就已经是同一条 P2SH 地址 interchangeable / 270 same-p2sh interchangeable。**  
   官方写：本页不是要一次解决全部好用或安全问题；以后应另有更友好的付款办法。看见地址上没有身份，不是已经核过收款人。

3. **看见本页已部署 / 看见只有本页这种地址 / 这份地址 is not already 已经交差 interchangeable，也不是已经付给脚本哈希地址 bundled（297） interchangeable / 1210 p2sh13-notwho interchangeable / 1208 p2sh13-not16 interchangeable，也不是已经付给脚本哈希就已经揭开赎回 interchangeable / 170 redeem interchangeable。**  
   官方把「地址没有身份」和「以后另写更友好付款」写成未解决的事。看见本页已部署，不是付款体验已经齐，也不是已经交差。

版本字节、开头字符、校验算法、编解码步骤是规范里的取值或做法，本页不抄。不要另写 BIP-12 / BIP-17。

## 官方为什么这样拆

- **只有本页这种地址 不是已经知道付给谁：** 官方把只有地址写成怎么确定付给的是你以为的那一方。
- **地址上没有身份 不是已经核过收款人：** 官方把本页写成不是一次解决全部好用或安全问题。
- **本页已部署 不是已经交差：** 官方把以后另写更友好付款写成未解决。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 付给谁 | 不是已经知道付给谁 | 不是已经同一条地址（270） |
| 身份 | 不是已经核过收款人 | 不是已经揭开赎回（170） |
| 交差 | 不是已经交差 | 不是已经是 16（1208） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-13 address-only not already know-payee / not already identity / not already settled 正式三事（297 余量），必须分开是不是已经知道付给谁、是不是已经核过收款人、是不是已经交差。可以跳过「看见这种地址就已经是 16」。不要另写怎样按 Base58Check 编地址或怎样从版本字节认网。不要另写 BIP-12 / BIP-17。297 p2sh address vs redeem bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 版本字节取值、开头字符、Base58Check 步骤、校验算法。
- 怎样造这种地址、怎样从版本字节认网、怎样从地址还原脚本哈希。
