# 例：看见签过的消息不是已经证明能控制资金；看见验过不是已经肯签真正的交易；看见签过不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-322](https://github.com/bitcoin/bips/blob/master/bip-0322.mediawiki)（Complete, Applications）。  
**对应课文**：[L0.7](../../courses/level-00-machine/L00-M07-one-payment-lifecycle.md)、[L1.2](../../courses/level-01-crypto/L01-M02-signatures.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-322 signed-message not already control / not already will-sign-spend / not already settled 正式三事（258 余量）/ not 1214 sig322-notctrl interchangeable / not 258 signed-message-vs-control bundled interchangeable」，不是签消息 bundled（258），也不是扩展公钥就已经能花（182），也不是 POR 看起来像交易就已经能花（293）。不要另写怎样拼虚拟交易。

## 官方三件事

1. **看见签过的消息 / 看见验过一条签消息 这份指示 is not already 已经证明能控制资金 interchangeable，也不是已经签消息 bundled（258） interchangeable / 1214 sig322-notctrl interchangeable / 1215 sig322-notprev interchangeable / 258 signed item 2 invoice-not-prev interchangeable，也不是已经 BIP-322 signed-message not already control / not already will-sign-spend / not already settled 正式三事 bundled（258 item 1 余量） interchangeable / 258 signed item 1 interchangeable。**  
   官方写：归根结底，没有任何签消息协议真能证明控制资金。签名一做出来就已经过时。握着密钥的人可以愿意替别人签消息，却不肯签真正的交易。看见验过一条签消息，不是已经能花，也不是已经控制那笔钱。

2. **看见验过 / 看见签过的消息 / 这份指示 is not already 已经肯签真正的交易 interchangeable，也不是已经签消息 bundled（258） interchangeable / 1214 sig322-notctrl interchangeable / 258 signed item 3 list-not-full interchangeable / 1216 sig322-notfund interchangeable，也不是已经扩展公钥就已经能花 interchangeable / 182 xpub interchangeable。**  
   官方写：没有任何签消息协议能修掉「愿意签消息却不肯签真正交易」这条限制。看见验过，不是已经肯签真正的交易。

3. **看见签过 / 看见签过的消息 / 这份指示 is not already 已经交差 interchangeable，也不是已经签消息 bundled（258） interchangeable / 1214 sig322-notctrl interchangeable / 1215 sig322-notprev interchangeable，也不是已经 POR 看起来像交易就已经能花 interchangeable / 293 por interchangeable。**  
   官方把「签过一条消息」和「已经控制资金」写成两件事。看见签过，不是已经交差。

编码前缀、虚拟交易怎么拼、测试向量是规范里的取值，本页不抄。不要另写怎样拼虚拟交易。

## 官方为什么这样拆

- **签过的消息 不是已经证明能控制资金：** 官方把没有任何签消息协议真能证明控制资金写成限制。
- **验过 不是已经肯签真正的交易：** 官方把愿意签消息却不肯签真正交易写成修不掉。
- **签过 不是已经交差：** 官方把签过和控制资金写成两件。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 控制资金 | 不是已经证明能控制资金 | 不是已经能花（182） |
| 肯签花费 | 不是已经肯签真正的交易 | 不是已经是 POR（293） |
| 交差 | 不是已经交差 | 不是已经付过（1215） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-322 signed-message not already control / not already will-sign-spend / not already settled 正式三事（258 余量），必须分开是不是已经证明能控制资金、是不是已经肯签真正的交易、是不是已经交差。可以跳过「看见签过就已经能花」。不要另写怎样拼虚拟交易。258 signed message vs control bundled unbundling 在本页 item 1 启动；续 [`worked-example-sig322-notprev-vs-bundled.md`](worked-example-sig322-notprev-vs-bundled.md)（不变量 1215 item 2）。

## 本页不抄

- 编码前缀、标签哈希、虚拟交易字段、PSBT 类型号、测试向量。
- 怎样拼能过验证器的签消息、怎样用资金证明假装齐或未花。
