# 例：看见钱包策略不是已经是一条描述符；看见账户不是已经不必再展开；看见一份描述符模板不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-388](https://github.com/bitcoin/bips/blob/master/bip-0388.mediawiki)（Complete, Applications, Specification）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-388 wallet-policy not already one-descriptor / not already account-collapsed / not already settled 正式三事（280 余量）/ not 1160 pol388-notdesc interchangeable / not 280 policy-vs-descriptor bundled interchangeable」，不是钱包策略 bundled（280），也不是看见描述符就已经是地址（184），也不是旧 PSBT 栏就已经能装 Taproot（1157）。不要另写怎样编译占位。

## 官方三件事

1. **看见钱包策略 / 看见一个账户 这份栏 is not already 已经是一条描述符 interchangeable，也不是已经钱包策略 bundled（280） interchangeable / 1160 pol388-notdesc interchangeable / 1161 pol388-notkey interchangeable / 280 pol item 2 key-not-exact interchangeable，也不是已经 BIP-388 wallet-policy not already one-descriptor / not already account-collapsed / not already settled 正式三事 bundled（280 item 1 余量） interchangeable / 280 pol item 1 interchangeable。**  
   官方写：钱包策略由一份描述符模板，加上一列钥信息组成。看见策略，不是已经是 380 那条描述符。

2. **看见一个账户 / 看见钱包策略 / 这份栏 is not already 已经不必再展开 interchangeable，也不是已经钱包策略 bundled（280） interchangeable / 1160 pol388-notdesc interchangeable / 280 pol item 3 reg-not-approve interchangeable / 1162 pol388-notreg interchangeable，也不是已经看见描述符就已经是地址 interchangeable / 184 descriptor interchangeable。**  
   官方写：一个账户包接收款和找零地址。每一份钱包策略代表描述这个账户所需的全部描述符。看见账户，不是已经不必再展开。

3. **看见一份描述符模板 / 看见钱包策略 / 这份栏 is not already 已经交差 interchangeable，也不是已经钱包策略 bundled（280） interchangeable / 1160 pol388-notdesc interchangeable / 1161 pol388-notkey interchangeable，也不是已经旧 PSBT 栏就已经能装 Taproot interchangeable / 1157 tap371-notold interchangeable。**  
   官方把模板和钥信息列写成两份对象。看见一份描述符模板，不是已经交差。

占位写法、编译步骤、测试向量、例路径是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **钱包策略 不是已经是一条描述符：** 官方把模板和钥信息列写成两份。
- **账户 不是已经不必再展开：** 官方把一份策略写成账户所需的全部描述符。
- **描述符模板 不是已经交差：** 官方把两份对象写成两句。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 策略 | 不是已经是一条描述符 | 不是已经是地址（184） |
| 账户 | 不是已经不必再展开 | 不是已经是精确公钥（1161） |
| 交差 | 不是已经交差 | 不是已经能装 Taproot（1157） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-388 wallet-policy not already one-descriptor / not already account-collapsed / not already settled 正式三事（280 余量），必须分开是不是已经是一条描述符、是不是已经不必再展开、是不是已经交差。可以跳过「看见账户就已经是一条描述符」。不要另写怎样编译占位。280 policy vs descriptor bundled unbundling 在本页 item 1 启动；续 [`worked-example-pol388-notkey-vs-bundled.md`](worked-example-pol388-notkey-vs-bundled.md)（不变量 1161 item 2）。

## 本页不抄

- 占位写法、编译步骤、测试向量、例路径、指纹宽度。
- 怎样做登记证明、怎样排序占位、怎样限制多路径。
