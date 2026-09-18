# 例：看见旧 PSBT 栏不是已经能装 Taproot；看见旧软件会忽略新栏不是已经能签；看见包还在不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-371](https://github.com/bitcoin/bips/blob/master/bip-0371.mediawiki)（Deployed, Applications, Specification）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-371 old-psbt-fields not already can-hold-taproot / not already can-sign-taproot / not already settled 正式三事（279 余量）/ not 1157 tap371-notold interchangeable / not 279 tap-psbt-vs-old bundled interchangeable」，不是 Taproot 工作包栏 bundled（279），也不是看见包就已经能广播（179），也不是派生钥就已经是输出钥（1136）。不要另写怎样拼控制块。

## 官方三件事

1. **看见旧 PSBT 栏 / 看见 174 那套字段 这份栏 is not already 已经能装 Taproot interchangeable，也不是已经 Taproot 工作包栏 bundled（279） interchangeable / 1157 tap371-notold interchangeable / 1158 tap371-notinner interchangeable / 279 tap item 2 key-not-inner interchangeable，也不是已经 BIP-371 old-psbt-fields not already can-hold-taproot / not already can-sign-taproot / not already settled 正式三事 bundled（279 item 1 余量） interchangeable / 279 tap item 1 interchangeable。**  
   官方写：现有 PSBT 栏没法支持 Taproot。新的签名算法，再加上脚本嵌进 Taproot 输出的方式，都和旧栏对不上。看见包还在，不是已经能装这些对象。

2. **看见旧软件会忽略新栏 / 看见旧 PSBT 栏 / 这份栏 is not already 已经能签 Taproot 输入 interchangeable，也不是已经 Taproot 工作包栏 bundled（279） interchangeable / 1157 tap371-notold interchangeable / 279 tap item 3 in-not-prev interchangeable / 1159 tap371-notprev interchangeable，也不是已经看见包就已经能广播 interchangeable / 179 psbt interchangeable。**  
   官方写：必须另开一套栏，才能把签 Taproot 输入所需的信息装进去。看见旧软件会忽略新栏，不是已经能签。

3. **看见包还在 / 看见旧 PSBT 栏 / 这份栏 is not already 已经交差 interchangeable，也不是已经 Taproot 工作包栏 bundled（279） interchangeable / 1157 tap371-notold interchangeable / 1158 tap371-notinner interchangeable，也不是已经派生钥就已经是输出钥 interchangeable / 1136 tap86-notout interchangeable。**  
   官方把新签法和脚本嵌法写成旧栏装不下。看见包还在，不是已经交差。

类型号、签名宽度、测试向量、控制块做法是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **旧 PSBT 栏 不是已经能装 Taproot：** 官方把旧栏写成装不下新签法和嵌法。
- **旧软件会忽略新栏 不是已经能签：** 官方把另开一套栏写成才能装签所需信息。
- **包还在 不是已经交差：** 官方把旧栏装不下写成独立一句。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 旧栏 | 不是已经能装 Taproot | 不是已经能广播（179） |
| 能签 | 不是已经能签 Taproot 输入 | 不是已经是内部钥（1158） |
| 交差 | 不是已经交差 | 不是已经是输出钥（1136） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-371 old-psbt-fields not already can-hold-taproot / not already can-sign-taproot / not already settled 正式三事（279 余量），必须分开是不是已经能装 Taproot、是不是已经能签、是不是已经交差。可以跳过「看见部分签名包就已经能签 Taproot」。不要另写怎样拼控制块。279 tap PSBT vs old bundled unbundling 在本页 item 1 启动；续 [`worked-example-tap371-notinner-vs-bundled.md`](worked-example-tap371-notinner-vs-bundled.md)（不变量 1158 item 2）。

## 本页不抄

- 类型号、签名宽度、十六进制 / Base64 测试向量、例钥。
- 怎样拼控制块、怎样序列化叶子哈希、怎样构造见证。
