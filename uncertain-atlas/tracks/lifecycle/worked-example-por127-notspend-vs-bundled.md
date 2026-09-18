# 例：看见储备证明交易不是已经能花；看见没有矿工费不是已经能确认；看见排得像交易不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-127](https://github.com/bitcoin/bips/blob/master/bip-0127.mediawiki)（Complete, Applications, Specification）。  
**对应课文**：[L0.7](../../courses/level-00-machine/L00-M07-one-payment-lifecycle.md)、[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-127 por-tx not already spendable / not already confirmable / not already settled 正式三事（293 余量）/ not 1196 por127-notspend interchangeable / not 293 reserves-vs-spend bundled interchangeable」，不是储备证明 bundled（293），也不是签过就已经控制资金（258），也不是部分签名包就已经能广播（179）。不要另写怎样造承诺输入或怎样填 POR 栏。

## 官方三件事

1. **看见储备证明交易 / 看见普通交易序列化 这份证明 is not already 已经能花 interchangeable，也不是已经储备证明 bundled（293） interchangeable / 1196 por127-notspend interchangeable / 1197 por127-notctrl interchangeable / 293 por item 2 signed-not-ctrl interchangeable，也不是已经 BIP-127 por-tx not already spendable / not already confirmable / not already settled 正式三事 bundled（293 item 1 余量） interchangeable / 293 por item 1 interchangeable。**  
   官方写：为了尽量兼容现有系统，证明按普通比特币交易来排。只做一处小改，干两件事：让这笔没法花，免得把资金置于险地；把证明绑到出示的人，免得抄别人的证明。第一笔输入叫承诺输入：前一出点的交易标识必须是对承诺消息做哈希，下标为 0。正是因为有这第一笔输入，这笔交易非法，永远确认不了。看见排得像交易，不是已经能花。

2. **看见没有矿工费 / 看见储备证明交易 / 这份证明 is not already 已经能确认 interchangeable，也不是已经储备证明 bundled（293） interchangeable / 1196 por127-notspend interchangeable / 293 por item 3 por-not-spend interchangeable / 1198 por127-notpor interchangeable，也不是已经签过就已经控制资金 interchangeable / 258 signed-is-control interchangeable。**  
   官方写：输出必须只有一笔，金额等于其余输入之和（承诺输入当 0），也就是没有矿工费。看见没有矿工费，不是已经是付款，也不是已经能确认。

3. **看见排得像交易 / 看见储备证明交易 / 这份证明 is not already 已经交差 interchangeable，也不是已经储备证明 bundled（293） interchangeable / 1196 por127-notspend interchangeable / 1197 por127-notctrl interchangeable，也不是已经部分签名包就已经能广播 interchangeable / 179 psbt interchangeable。**  
   官方把「排得像交易」和「第一笔输入让它永远确认不了」写成两件事。看见排得像交易，不是已经交差。

哈希前缀、栏类型号、怎样给设备填假数据是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **储备证明交易 不是已经能花：** 官方把兼容现有系统和第一笔输入让它没法花写成两件。
- **没有矿工费 不是已经能确认：** 官方把金额等于其余输入之和写成没有矿工费，不是已经是付款。
- **排得像交易 不是已经交差：** 官方把排得像交易和永远确认不了写成两句。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 能花 | 不是已经能花 | 不是已经控制资金（258） |
| 确认 | 不是已经能确认 | 不是已经能广播（179） |
| 交差 | 不是已经交差 | 不是已经是 258 控制（1197） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-127 por-tx not already spendable / not already confirmable / not already settled 正式三事（293 余量），必须分开是不是已经能花、是不是已经能确认、是不是已经交差。可以跳过「看见一份像交易的证明就已经能花」。不要另写怎样造承诺输入或怎样填 POR 栏。293 reserves vs spend bundled unbundling 在本页 item 1 启动；续 [`worked-example-por127-notctrl-vs-bundled.md`](worked-example-por127-notctrl-vs-bundled.md)（不变量 1197 item 2）。

## 本页不抄

- 哈希前缀拼法、栏类型号、测试向量、怎样给设备填假前交易。
- 怎样造承诺输入、怎样算承诺哈希、怎样填 POR 栏。
