# 例：看见 Taproot 输入不是已经必须带整笔前交易；看见只带了见证 UTXO 不是已经是旧输入那套；看见 174 建议带整笔前交易不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-371](https://github.com/bitcoin/bips/blob/master/bip-0371.mediawiki)（Deployed, Applications, Specification）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-371 taproot-input not already must-prev-tx / not already same-utxo-fields / not already settled 正式三事（279 余量）/ not 1159 tap371-notprev interchangeable / not 279 tap-psbt-vs-old bundled interchangeable」，不是 Taproot 工作包栏 bundled（279），也不是后继包已经是旧版固定未签交易（186），也不是看见包就已经能广播（179）。不要另写怎样拼控制块。

## 官方三件事

1. **看见 Taproot 输入 / 看见 174 建议带整笔前交易 这份栏 is not already 已经必须带整笔前交易 interchangeable，也不是已经 Taproot 工作包栏 bundled（279） interchangeable / 1159 tap371-notprev interchangeable / 1157 tap371-notold interchangeable / 279 tap item 1 old-not-hold interchangeable，也不是已经 BIP-371 taproot-input not already must-prev-tx / not already same-utxo-fields / not already settled 正式三事 bundled（279 item 3 余量） interchangeable / 279 tap item 3 interchangeable。**  
   官方写：Taproot 签名会承诺本交易各输入花掉的金额和输出脚本，谎报会让签作废。所以 Taproot 输入可以只带见证 UTXO 栏。看见 174 那条建议，不是已经是本页。

2. **看见只带了见证 UTXO / 看见 Taproot 输入 / 这份栏 is not already 已经是旧输入那套 interchangeable，也不是已经 Taproot 工作包栏 bundled（279） interchangeable / 1159 tap371-notprev interchangeable / 279 tap item 2 key-not-inner interchangeable / 1158 tap371-notinner interchangeable，也不是已经后继包已经是旧版固定未签交易 interchangeable / 186 successor interchangeable。**  
   官方把承诺金额写成可以只带见证 UTXO。看见只带了见证 UTXO，不是已经是旧输入那套。

3. **看见 174 建议带整笔前交易 / 看见 Taproot 输入 / 这份栏 is not already 已经交差 interchangeable，也不是已经 Taproot 工作包栏 bundled（279） interchangeable / 1159 tap371-notprev interchangeable / 1157 tap371-notold interchangeable，也不是已经看见包就已经能广播 interchangeable / 179 psbt interchangeable。**  
   官方把 174 建议所有输入都带整笔前交易写成免得更新者谎报金额。看见 174 建议带整笔前交易，不是已经交差。

类型号、签名宽度、测试向量、控制块做法是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **Taproot 输入 不是已经必须带整笔前交易：** 官方把承诺金额写成可以只带见证 UTXO。
- **只带了见证 UTXO 不是已经是旧输入那套：** 官方把本页 UTXO 栏写成另一套。
- **174 建议带整笔前交易 不是已经交差：** 官方把建议和本页写成两句。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 整笔前交易 | 不是已经必须带 | 不是已经是后继包（186） |
| 见证 UTXO | 不是已经是旧输入那套 | 不是已经是内部钥（1158） |
| 交差 | 不是已经交差 | 不是已经能广播（179） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-371 taproot-input not already must-prev-tx / not already same-utxo-fields / not already settled 正式三事（279 余量），必须分开是不是已经必须带整笔前交易、是不是已经是旧输入那套、是不是已经交差。可以跳过「看见部分签名包就已经能签 Taproot」。不要另写怎样拼控制块。279 tap PSBT vs old bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 类型号、签名宽度、十六进制 / Base64 测试向量、例钥。
- 怎样拼控制块、怎样序列化叶子哈希、怎样构造见证。
