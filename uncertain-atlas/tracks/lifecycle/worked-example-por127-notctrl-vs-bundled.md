# 例：看见其余输入签过不是已经是 258 那种控制资金；看见承诺了消息不是已经付过；看见某一块时有过不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-127](https://github.com/bitcoin/bips/blob/master/bip-0127.mediawiki)（Complete, Applications, Specification）。  
**对应课文**：[L0.7](../../courses/level-00-machine/L00-M07-one-payment-lifecycle.md)、[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-127 remaining-signed not already 258-control / not already paid / not already settled 正式三事（293 余量）/ not 1197 por127-notctrl interchangeable / not 293 reserves-vs-spend bundled interchangeable」，不是储备证明 bundled（293），也不是签过就已经控制资金（258），也不是地址串就已经有输出（174）。不要另写怎样造承诺输入或怎样填 POR 栏。

## 官方三件事

1. **看见其余输入签过 / 看见承诺了消息 这份证明 is not already 已经是 258 那种控制资金 interchangeable，也不是已经储备证明 bundled（293） interchangeable / 1197 por127-notctrl interchangeable / 1196 por127-notspend interchangeable / 293 por item 1 tx-not-spend interchangeable，也不是已经 BIP-127 remaining-signed not already 258-control / not already paid / not already settled 正式三事 bundled（293 item 2 余量） interchangeable / 293 por item 2 interchangeable。**  
   官方写：其余输入的签名必须承诺到那笔承诺输入。这份证明靠承诺一条消息，挡住别人拿去复用。看见其余输入签过，不是已经肯签真正的花费，也不是已经是 258 那种资金证明清单。

2. **看见承诺了消息 / 看见其余输入签过 / 这份证明 is not already 已经付过 interchangeable，也不是已经储备证明 bundled（293） interchangeable / 1197 por127-notctrl interchangeable / 293 por item 3 por-not-spend interchangeable / 1198 por127-notpor interchangeable，也不是已经签过就已经控制资金 interchangeable / 258 signed-is-control interchangeable。**  
   官方写：它允许核：出示的人在某一块时手里有这些币，不管那之后发生了什么。官方另写：这种构造在隐私上有已知短处；本页只是把业界已经在用的办法写成标准，不是那种更藏余额的储备证明研究。看见承诺了消息，不是已经付过。

3. **看见某一块时有过 / 看见其余输入签过 / 这份证明 is not already 已经交差 interchangeable，也不是已经储备证明 bundled（293） interchangeable / 1197 por127-notctrl interchangeable / 1196 por127-notspend interchangeable，也不是已经地址串就已经有输出 interchangeable / 174 address interchangeable。**  
   官方把某一块时有过和现在还能花写成两件。看见某一块时有过，不是现在还能花，也不是已经交差。

哈希前缀、栏类型号、怎样给设备填假数据是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **其余输入签过 不是已经是 258 那种控制资金：** 官方把承诺到承诺输入和 258 那种清单写成不同对象。
- **承诺了消息 不是已经付过：** 官方把挡住复用写成不是已经付过。
- **某一块时有过 不是已经交差：** 官方把某一块时有过写成不是现在还能花。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 控制 | 不是已经是 258 那种控制资金 | 不是已经控制资金（258） |
| 付过 | 不是已经付过 | 不是已经有输出（174） |
| 交差 | 不是已经交差 | 不是已经能花（1196） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-127 remaining-signed not already 258-control / not already paid / not already settled 正式三事（293 余量），必须分开是不是已经是 258 那种控制资金、是不是已经付过、是不是已经交差。可以跳过「看见一份像交易的证明就已经能花」。不要另写怎样造承诺输入或怎样填 POR 栏。293 reserves vs spend bundled unbundling 在本页 item 2 续；续 [`worked-example-por127-notpor-vs-bundled.md`](worked-example-por127-notpor-vs-bundled.md)（不变量 1198 item 3）。

## 本页不抄

- 哈希前缀拼法、栏类型号、测试向量、怎样给设备填假前交易。
- 怎样造承诺输入、怎样算承诺哈希、怎样填 POR 栏。
