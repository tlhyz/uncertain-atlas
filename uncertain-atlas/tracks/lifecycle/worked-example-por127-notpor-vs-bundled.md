# 例：看见 POR 栏不是已经是普通花费；看见硬件钱包弹出确认不是已经有前一笔未花输出；看见问要不要全部打走不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-127](https://github.com/bitcoin/bips/blob/master/bip-0127.mediawiki)（Complete, Applications, Specification）。  
**对应课文**：[L0.7](../../courses/level-00-machine/L00-M07-one-payment-lifecycle.md)、[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-127 por-field not already ordinary-spend / not already have-prev-utxo / not already settled 正式三事（293 余量）/ not 1198 por127-notpor interchangeable / not 293 reserves-vs-spend bundled interchangeable」，不是储备证明 bundled（293），也不是部分签名包就已经能广播（179），也不是扩展公钥就已经能花（182）。不要另写怎样造承诺输入或怎样填 POR 栏。

## 官方三件事

1. **看见 POR 栏 / 看见硬件钱包弹出确认 这份证明 is not already 已经是普通花费 interchangeable，也不是已经储备证明 bundled（293） interchangeable / 1198 por127-notpor interchangeable / 1196 por127-notspend interchangeable / 293 por item 1 tx-not-spend interchangeable，也不是已经 BIP-127 por-field not already ordinary-spend / not already have-prev-utxo / not already settled 正式三事 bundled（293 item 3 余量） interchangeable / 293 por item 3 interchangeable。**  
   官方写：承诺输入并不花掉链上已有的未花输出，也不该被签。硬件签名器常常要每一笔输入的前交易，这份数据对承诺输入并不存在。设备若不认得这是储备证明，会当成普通交易，问用户是不是要把这些币全部打走。看见硬件钱包在问「要不要全部打走」，不是已经是花费。

2. **看见硬件钱包弹出确认 / 看见 POR 栏 / 这份证明 is not already 已经有前一笔未花输出 interchangeable，也不是已经储备证明 bundled（293） interchangeable / 1198 por127-notpor interchangeable / 293 por item 2 signed-not-ctrl interchangeable / 1197 por127-notctrl interchangeable，也不是已经部分签名包就已经能广播 interchangeable / 179 psbt interchangeable。**  
   官方写：本页往 174 的输入图里加一栏承诺消息。处理这一栏的钱包必须核：前一出点的交易标识对得上那条加了前缀的消息；必须把这一输入的金额当成 0，不必再要前一笔输出。看见有 POR 栏，不是已经有前一笔未花输出。

3. **看见问要不要全部打走 / 看见 POR 栏 / 这份证明 is not already 已经交差 interchangeable，也不是已经储备证明 bundled（293） interchangeable / 1198 por127-notpor interchangeable / 1196 por127-notspend interchangeable，也不是已经扩展公钥就已经能花 interchangeable / 182 xpub interchangeable。**  
   官方写：应当把承诺消息拿给用户看，再签其余输入；应当只出承诺到这一输入的签。看见硬件钱包在问全部打走，不是已经交差。

哈希前缀、栏类型号、怎样给设备填假数据是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **POR 栏 不是已经是普通花费：** 官方把设备会误当成全部打走写成必须另开一栏的理由。
- **硬件钱包弹出确认 不是已经有前一笔未花输出：** 官方把承诺输入写成不必再要前一笔输出。
- **问要不要全部打走 不是已经交差：** 官方把给用户看承诺消息再签其余输入写成另一步。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 花费 | 不是已经是普通花费 | 不是已经能广播（179） |
| 前一出 | 不是已经有前一笔未花输出 | 不是已经能花（182） |
| 交差 | 不是已经交差 | 不是已经能花（1196） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-127 por-field not already ordinary-spend / not already have-prev-utxo / not already settled 正式三事（293 余量），必须分开是不是已经是普通花费、是不是已经有前一笔未花输出、是不是已经交差。可以跳过「看见一份像交易的证明就已经能花」。不要另写怎样造承诺输入或怎样填 POR 栏。293 reserves vs spend bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 哈希前缀拼法、栏类型号、测试向量、怎样给设备填假前交易。
- 怎样造承诺输入、怎样算承诺哈希、怎样填 POR 栏。
