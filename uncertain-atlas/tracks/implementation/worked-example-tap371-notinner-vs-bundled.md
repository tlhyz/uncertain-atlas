# 例：看见输出脚本里的钥不是已经是内部钥；看见钥匙路径签不是已经不必再给内部钥；看见 341 建议用钥对自己的哈希做微调不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-371](https://github.com/bitcoin/bips/blob/master/bip-0371.mediawiki)（Deployed, Applications, Specification）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-371 output-script-key not already internal-key / not already same-key / not already settled 正式三事（279 余量）/ not 1158 tap371-notinner interchangeable / not 279 tap-psbt-vs-old bundled interchangeable」，不是 Taproot 工作包栏 bundled（279），也不是派生钥就已经是输出钥（1136），也不是钥匙路径就已经揭开有没有树（153）。不要另写怎样拼控制块。

## 官方三件事

1. **看见输出脚本里的钥 / 看见钥匙路径那张签 这份栏 is not already 已经是内部钥 interchangeable，也不是已经 Taproot 工作包栏 bundled（279） interchangeable / 1158 tap371-notinner interchangeable / 1157 tap371-notold interchangeable / 279 tap item 1 old-not-hold interchangeable，也不是已经 BIP-371 output-script-key not already internal-key / not already same-key / not already settled 正式三事 bundled（279 item 2 余量） interchangeable / 279 tap item 2 interchangeable。**  
   官方写：内部钥不一定就是输出脚本里那把。看见输出脚本里的钥，不是已经有内部钥。

2. **看见钥匙路径签 / 看见输出脚本里的钥 / 这份栏 is not already 已经不必再给内部钥 interchangeable，也不是已经 Taproot 工作包栏 bundled（279） interchangeable / 1158 tap371-notinner interchangeable / 279 tap item 3 in-not-prev interchangeable / 1159 tap371-notprev interchangeable，也不是已经派生钥就已经是输出钥 interchangeable / 1136 tap86-notout interchangeable。**  
   官方写：钥匙路径那张签直接对应输出脚本里的公钥，所以不必再附一把钥的元数据。签名人可能必须先知道内部钥是什么，才能判断自己能不能签。看见钥匙路径签，不是已经不必再给内部钥。

3. **看见 341 建议用钥对自己的哈希做微调 / 看见输出脚本里的钥 / 这份栏 is not already 已经交差 interchangeable，也不是已经 Taproot 工作包栏 bundled（279） interchangeable / 1158 tap371-notinner interchangeable / 1157 tap371-notold interchangeable，也不是已经钥匙路径就已经揭开有没有树 interchangeable / 153 keypath interchangeable。**  
   官方把钥匙路径签和内部钥写成两份对象。看见 341 建议用钥对自己的哈希做微调，不是已经交差。

类型号、签名宽度、测试向量、控制块做法是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **输出脚本里的钥 不是已经是内部钥：** 官方把内部钥和输出脚本里那把写成两份。
- **钥匙路径签 不是已经不必再给内部钥：** 官方把签名人可能必须先知道内部钥写成另一句。
- **341 微调建议 不是已经交差：** 官方把两份对象写成两句。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 内部钥 | 不是已经是内部钥 | 不是已经是输出钥（1136） |
| 钥匙路径签 | 不是已经不必再给内部钥 | 不是已经能装旧栏（1157） |
| 交差 | 不是已经交差 | 不是已经揭开有没有树（153） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-371 output-script-key not already internal-key / not already same-key / not already settled 正式三事（279 余量），必须分开是不是已经是内部钥、是不是已经不必再给内部钥、是不是已经交差。可以跳过「看见部分签名包就已经能签 Taproot」。不要另写怎样拼控制块。279 tap PSBT vs old bundled unbundling 在本页 item 2 续；续 [`worked-example-tap371-notprev-vs-bundled.md`](worked-example-tap371-notprev-vs-bundled.md)（不变量 1159 item 3）。

## 本页不抄

- 类型号、签名宽度、十六进制 / Base64 测试向量、例钥。
- 怎样拼控制块、怎样序列化叶子哈希、怎样构造见证。
