# 例：看见本页这种地址不是已经是赎回脚本；看见编的是脚本哈希不是已经是 16；看见能给人看不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-13](https://github.com/bitcoin/bips/blob/master/bip-0013.mediawiki)（Deployed, Applications, Specification）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-13 this-address not already redeem-script / not already 16 / not already settled 正式三事（297 余量）/ not 1208 p2sh13-not16 interchangeable / not 297 p2sh-address-vs-redeem bundled interchangeable」，不是付给脚本哈希地址 bundled（297），也不是付给脚本哈希就已经揭开赎回（170），也不是 Bech32 地址就已经有输出（174）。不要另写怎样按 Base58Check 编地址或怎样从版本字节认网。不要另写 BIP-12 / BIP-17。

## 官方三件事

1. **看见本页这种地址 / 看见编进去的是脚本哈希 这份地址 is not already 已经是赎回脚本 interchangeable，也不是已经付给脚本哈希地址 bundled（297） interchangeable / 1208 p2sh13-not16 interchangeable / 1209 p2sh13-notpaid interchangeable / 297 p2sh item 2 old-not-paid interchangeable，也不是已经 BIP-13 this-address not already redeem-script / not already 16 / not already settled 正式三事 bundled（297 item 1 余量） interchangeable / 297 p2sh item 1 interchangeable。**  
   官方写：本页这种地址编进去的是一段脚本的哈希，而不是一把椭圆曲线公钥的哈希。那二十个字节是将来用来赎回这些币的脚本的哈希。看见这种地址，不是已经有赎回脚本。

2. **看见编的是脚本哈希 / 看见本页这种地址 / 这份地址 is not already 已经是 16 interchangeable，也不是已经付给脚本哈希地址 bundled（297） interchangeable / 1208 p2sh13-not16 interchangeable / 297 p2sh item 3 only-not-who interchangeable / 1210 p2sh13-notwho interchangeable，也不是已经付给脚本哈希就已经揭开赎回 interchangeable / 170 redeem interchangeable。**  
   官方写：看见编的是脚本哈希，不是已经在走 16 那种花费规则。官方把「编的是脚本哈希」写成地址格式，不是链上花费规则。

3. **看见能给人看 / 看见本页这种地址 / 这份地址 is not already 已经交差 interchangeable，也不是已经付给脚本哈希地址 bundled（297） interchangeable / 1208 p2sh13-not16 interchangeable / 1209 p2sh13-notpaid interchangeable，也不是已经 Bech32 地址就已经有输出 interchangeable / 174 address interchangeable。**  
   官方写：看见能给人看，不是链上已经有这笔输出，也不是已经交差。

版本字节、开头字符、校验算法、编解码步骤是规范里的取值或做法，本页不抄。不要另写 BIP-12 / BIP-17。

## 官方为什么这样拆

- **本页这种地址 不是已经是赎回脚本：** 官方把编进去的二十个字节写成将来赎回脚本的哈希。
- **编的是脚本哈希 不是已经是 16：** 官方把地址格式和花费规则写成两件。
- **能给人看 不是已经交差：** 官方把能给人看成不是链上已经有输出。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 赎回 | 不是已经是赎回脚本 | 不是已经揭开赎回（170） |
| 16 | 不是已经是 16 | 不是已经有输出（174） |
| 交差 | 不是已经交差 | 不是已经付过（1209） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-13 this-address not already redeem-script / not already 16 / not already settled 正式三事（297 余量），必须分开是不是已经是赎回脚本、是不是已经是 16、是不是已经交差。可以跳过「看见这种地址就已经是 16」。不要另写怎样按 Base58Check 编地址或怎样从版本字节认网。不要另写 BIP-12 / BIP-17。297 p2sh address vs redeem bundled unbundling 在本页 item 1 启动；续 [`worked-example-p2sh13-notpaid-vs-bundled.md`](worked-example-p2sh13-notpaid-vs-bundled.md)（不变量 1209 item 2）。

## 本页不抄

- 版本字节取值、开头字符、Base58Check 步骤、校验算法。
- 怎样造这种地址、怎样从版本字节认网、怎样从地址还原脚本哈希。
