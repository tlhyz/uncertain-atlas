# 例：看见收款方加了输入不是已经另开一笔；看见提案存在不是已经对全网私人；看见一笔 payjoin 交易不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-78](https://github.com/bitcoin/bips/blob/master/bip-0078.mediawiki)（Deployed, Applications, Specification）。取代 BIP-79。  
**对应课文**：[L0.7](../../courses/level-00-machine/L00-M07-one-payment-lifecycle.md)、[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-78 added-input not already other-tx / not already network-private / not already settled 正式三事（290 余量）/ not 1186 pj78-notmerge interchangeable / not 290 payjoin-vs-original bundled interchangeable」，不是 payjoin 付款 bundled（290），也不是策略就已经是共识（144），也不是付款 URI 就已经授权（255）。不要另写怎样构造提案或怎样加费。

## 官方三件事

1. **看见收款方加了输入 / 看见合并整理 这份付款 is not already 已经另开一笔 interchangeable，也不是已经 payjoin 付款 bundled（290） interchangeable / 1186 pj78-notmerge interchangeable / 1184 pj78-noturi interchangeable / 290 pj item 1 uri-not-pay interchangeable，也不是已经 BIP-78 added-input not already other-tx / not already network-private / not already settled 正式三事 bundled（290 item 3 余量） interchangeable / 290 pj item 3 interchangeable。**  
   官方写：收款方可以整理自己的未花输出、也可以把自己的付款并进这一笔，并不另开一笔交易。看见加了输入，不是已经另开一笔。

2. **看见提案存在 / 看见收款方加了输入 / 这份付款 is not already 已经对全网私人 interchangeable，也不是已经 payjoin 付款 bundled（290） interchangeable / 1186 pj78-notmerge interchangeable / 290 pj item 2 orig-not-prop interchangeable / 1185 pj78-notorig interchangeable，也不是已经策略就已经是共识 interchangeable / 144 policy interchangeable。**  
   官方写：这份提案存在，也会让那三条启发式对没用本页的人变得不可靠。看见提案存在，不是已经对全网私人。

3. **看见一笔 payjoin 交易 / 看见收款方加了输入 / 这份付款 is not already 已经交差 interchangeable，也不是已经 payjoin 付款 bundled（290） interchangeable / 1186 pj78-notmerge interchangeable / 1184 pj78-noturi interchangeable，也不是已经付款 URI 就已经授权 interchangeable / 255 uri interchangeable。**  
   官方写：收款方必须确认原始包里的输入以前没见过：既挡探测，也挡把一笔 payjoin 交易再拿来当新的原始包。看见一笔 payjoin 交易，不是已经能再当原始包，也不是已经交差。

HTTP 配方、加费公式、发送方/收款方核对清单、怎样构造或下毒、混输入宽限期、版本不支持载荷是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **收款方加了输入 不是已经另开一笔：** 官方把合并整理写成不另开交易。
- **提案存在 不是已经对全网私人：** 官方把启发式写成只对没用本页的人不可靠。
- **一笔 payjoin 交易 不是已经交差：** 官方把再当原始包写成必须挡。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 另开 | 不是已经另开一笔 | 不是已经是共识（144） |
| 私人 | 不是已经对全网私人 | 不是已经授权（255） |
| 交差 | 不是已经交差 | 不是已经是提案（1185） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-78 added-input not already other-tx / not already network-private / not already settled 正式三事（290 余量），必须分开是不是已经另开一笔、是不是已经对全网私人、是不是已经交差。可以跳过「看见 pj= 就已经是 payjoin 付款」。不要另写怎样构造提案或怎样加费。290 payjoin vs original bundled unbundling 在本页 item 3 完成。

## 本页不抄

- HTTP POST / base64 / Content-Type / Access-Control-Allow-Origin、错误 JSON、加费公式、核对清单。
- 怎样构造提案、怎样加费、怎样下毒启发式、怎样混输入、怎样回版本不支持。
