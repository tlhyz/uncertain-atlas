# 例：看见登记过不是已经批准这笔花；看见写了 policy 不是已经是 379 那种语言；看见登记证明不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-388](https://github.com/bitcoin/bips/blob/master/bip-0388.mediawiki)（Complete, Applications, Specification）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-388 registered not already approved-this-spend / not already miniscript-policy / not already settled 正式三事（280 余量）/ not 1162 pol388-notreg interchangeable / not 280 policy-vs-descriptor bundled interchangeable」，不是钱包策略 bundled（280），也不是看见 Miniscript 就已经是链上脚本（191），也不是看见描述符就已经是地址（184）。不要另写怎样编译占位。

## 官方三件事

1. **看见登记过 / 看见登记证明 这份栏 is not already 已经批准这笔花 interchangeable，也不是已经钱包策略 bundled（280） interchangeable / 1162 pol388-notreg interchangeable / 1160 pol388-notdesc interchangeable / 280 pol item 1 pol-not-desc interchangeable，也不是已经 BIP-388 registered not already approved-this-spend / not already miniscript-policy / not already settled 正式三事 bundled（280 item 3 余量） interchangeable / 280 pol item 3 interchangeable。**  
   官方写：第一次用之前，用户要先在签名器上登记这份策略。登记证明让签名器确认用户以前批准过这份策略，才不必再走一遍昂贵核验。看见登记过，不是已经批准这一笔。

2. **看见写了 policy / 看见登记过 / 这份栏 is not already 已经是 379 那种语言 interchangeable，也不是已经钱包策略 bundled（280） interchangeable / 1162 pol388-notreg interchangeable / 280 pol item 2 key-not-exact interchangeable / 1161 pol388-notkey interchangeable，也不是已经看见 Miniscript 就已经是链上脚本 interchangeable / 191 miniscript interchangeable。**  
   官方另写：本页钱包策略和那种能编译成 Miniscript 的 policy 语言不是一回事。看见写了 policy，不是已经是 379 那种语言。

3. **看见登记证明 / 看见登记过 / 这份栏 is not already 已经交差 interchangeable，也不是已经钱包策略 bundled（280） interchangeable / 1162 pol388-notreg interchangeable / 1160 pol388-notdesc interchangeable，也不是已经看见描述符就已经是地址 interchangeable / 184 descriptor interchangeable。**  
   官方把登记证明写成可以少核验，不是已经签过这一笔。看见登记证明，不是已经交差。

占位写法、编译步骤、测试向量、例路径是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **登记过 不是已经批准这笔花：** 官方把登记证明写成可以少核验，不是已经签过这一笔。
- **写了 policy 不是已经是 379 那种语言：** 官方把本页策略和 Miniscript policy 写成两回事。
- **登记证明 不是已经交差：** 官方把登记和批准这一笔写成两句。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 登记 | 不是已经批准这笔花 | 不是已经是链上脚本（191） |
| policy 一词 | 不是已经是 379 那种语言 | 不是已经是精确公钥（1161） |
| 交差 | 不是已经交差 | 不是已经是一条描述符（1160） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-388 registered not already approved-this-spend / not already miniscript-policy / not already settled 正式三事（280 余量），必须分开是不是已经批准这笔花、是不是已经是 379 那种语言、是不是已经交差。可以跳过「看见账户就已经是一条描述符」。不要另写怎样编译占位。280 policy vs descriptor bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 占位写法、编译步骤、测试向量、例路径、指纹宽度。
- 怎样做登记证明、怎样排序占位、怎样限制多路径。
