# 例：看见钥占位不是已经是那把精确公钥；看见列开了扩展公钥不是已经是描述符里那把 KEY；看见账户根不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-388](https://github.com/bitcoin/bips/blob/master/bip-0388.mediawiki)（Complete, Applications, Specification）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-388 key-placeholder not already exact-pubkey / not already fully-derived / not already settled 正式三事（280 余量）/ not 1161 pol388-notkey interchangeable / not 280 policy-vs-descriptor bundled interchangeable」，不是钱包策略 bundled（280），也不是已经 BIP32 compatible（1118），也不是看见描述符就已经是地址（184）。不要另写怎样编译占位。

## 官方三件事

1. **看见钥占位 / 看见账户根 这份栏 is not already 已经是那把精确公钥 interchangeable，也不是已经钱包策略 bundled（280） interchangeable / 1161 pol388-notkey interchangeable / 1160 pol388-notdesc interchangeable / 280 pol item 1 pol-not-desc interchangeable，也不是已经 BIP-388 key-placeholder not already exact-pubkey / not already fully-derived / not already settled 正式三事 bundled（280 item 2 余量） interchangeable / 280 pol item 2 interchangeable。**  
   官方写：KEY 表达式永远对应最终脚本里那一把精确公钥，派生步骤都写在 KEY 里。看见占位，不是已经对上某一把脚本公钥。

2. **看见列开了扩展公钥 / 看见钥占位 / 这份栏 is not already 已经是描述符里那把 KEY interchangeable，也不是已经钱包策略 bundled（280） interchangeable / 1161 pol388-notkey interchangeable / 280 pol item 3 reg-not-approve interchangeable / 1162 pol388-notreg interchangeable，也不是已经 BIP32 compatible interchangeable / 1118 purp43 interchangeable。**  
   官方写：钥占位对应这个账户所有可能 UTXO 的公钥根，占位里不许再写派生。看见列开了扩展公钥，不是已经是描述符里那把 KEY。

3. **看见账户根 / 看见钥占位 / 这份栏 is not already 已经交差 interchangeable，也不是已经钱包策略 bundled（280） interchangeable / 1161 pol388-notkey interchangeable / 1160 pol388-notdesc interchangeable，也不是已经看见描述符就已经是地址 interchangeable / 184 descriptor interchangeable。**  
   官方把 KEY 的派生和占位的账户根写成两套。看见账户根，不是已经交差。

占位写法、编译步骤、测试向量、例路径是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **钥占位 不是已经是那把精确公钥：** 官方把 KEY 写成最终脚本里那一把。
- **列开了扩展公钥 不是已经是描述符里那把 KEY：** 官方把占位写成账户根，不许再派生。
- **账户根 不是已经交差：** 官方把两套写成两句。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 占位 | 不是已经是精确公钥 | 不是已经 BIP32 compatible（1118） |
| 扩展公钥列 | 不是已经是那把 KEY | 不是已经是一条描述符（1160） |
| 交差 | 不是已经交差 | 不是已经是地址（184） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-388 key-placeholder not already exact-pubkey / not already fully-derived / not already settled 正式三事（280 余量），必须分开是不是已经是那把精确公钥、是不是已经是描述符里那把 KEY、是不是已经交差。可以跳过「看见账户就已经是一条描述符」。不要另写怎样编译占位。280 policy vs descriptor bundled unbundling 在本页 item 2 续；续 [`worked-example-pol388-notreg-vs-bundled.md`](worked-example-pol388-notreg-vs-bundled.md)（不变量 1162 item 3）。

## 本页不抄

- 占位写法、编译步骤、测试向量、例路径、指纹宽度。
- 怎样做登记证明、怎样排序占位、怎样限制多路径。
