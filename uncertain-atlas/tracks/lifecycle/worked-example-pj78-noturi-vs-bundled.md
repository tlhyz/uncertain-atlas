# 例：看见带 pj= 的付款 URI 不是已经是 payjoin 付款；看见端点不是已经有原始包；看见 pjos=0 不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-78](https://github.com/bitcoin/bips/blob/master/bip-0078.mediawiki)（Deployed, Applications, Specification）。取代 BIP-79。  
**对应课文**：[L0.7](../../courses/level-00-machine/L00-M07-one-payment-lifecycle.md)、[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-78 pj-uri not already payjoin-payment / not already original / not already settled 正式三事（290 余量）/ not 1184 pj78-noturi interchangeable / not 290 payjoin-vs-original bundled interchangeable」，不是 payjoin 付款 bundled（290），也不是付款 URI 就已经授权（255），也不是部分签名包就已经能广播（179）。不要另写怎样构造提案或怎样加费。

## 官方三件事

1. **看见带 pj= 的付款 URI / 看见 payjoin 端点 这份付款 is not already 已经是 payjoin 付款 interchangeable，也不是已经 payjoin 付款 bundled（290） interchangeable / 1184 pj78-noturi interchangeable / 1185 pj78-notorig interchangeable / 290 pj item 2 orig-not-prop interchangeable，也不是已经 BIP-78 pj-uri not already payjoin-payment / not already original / not already settled 正式三事 bundled（290 item 1 余量） interchangeable / 290 pj item 1 interchangeable。**  
   官方写：收款方出示一条 BIP-21 URI，上面用 pj= 描述一个端点，发送方把原始包 POST 到那里。看见 pj=，不是已经付过。

2. **看见 payjoin 端点 / 看见带 pj= 的付款 URI / 这份付款 is not already 已经有原始包 interchangeable，也不是已经 payjoin 付款 bundled（290） interchangeable / 1184 pj78-noturi interchangeable / 290 pj item 3 add-not-other interchangeable / 1186 pj78-notmerge interchangeable，也不是已经付款 URI 就已经授权 interchangeable / 255 uri interchangeable。**  
   官方另写：pjos=0 是另一条信号，发送方必须禁止替换付款输出。金额参数不是必须的。看见端点，不是已经有原始包。看见 pjos=0，不是已经做完 payjoin。

3. **看见 pjos=0 / 看见带 pj= 的付款 URI / 这份付款 is not already 已经交差 interchangeable，也不是已经 payjoin 付款 bundled（290） interchangeable / 1184 pj78-noturi interchangeable / 1185 pj78-notorig interchangeable，也不是已经部分签名包就已经能广播 interchangeable / 179 psbt interchangeable。**  
   官方把 pj= 写成端点描述，把 pjos=0 写成另一条禁止替换信号。看见 pjos=0，不是已经交差。

HTTP 配方、加费公式、发送方/收款方核对清单、怎样构造或下毒、混输入宽限期、版本不支持载荷是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **带 pj= 的付款 URI 不是已经是 payjoin 付款：** 官方把 pj= 写成端点描述。
- **端点 不是已经有原始包：** 官方把端点和原始包写成两步。
- **pjos=0 不是已经交差：** 官方把禁止替换写成另一条信号。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 付款 | 不是已经是 payjoin 付款 | 不是已经授权（255） |
| 原始包 | 不是已经有原始包 | 不是已经能广播（179） |
| 交差 | 不是已经交差 | 不是已经是提案（1185） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-78 pj-uri not already payjoin-payment / not already original / not already settled 正式三事（290 余量），必须分开是不是已经是 payjoin 付款、是不是已经有原始包、是不是已经交差。可以跳过「看见 pj= 就已经是 payjoin 付款」。不要另写怎样构造提案或怎样加费。290 payjoin vs original bundled unbundling 在本页 item 1 启动；续 [`worked-example-pj78-notorig-vs-bundled.md`](worked-example-pj78-notorig-vs-bundled.md)（不变量 1185 item 2）。

## 本页不抄

- HTTP POST / base64 / Content-Type / Access-Control-Allow-Origin、错误 JSON、加费公式、核对清单。
- 怎样构造提案、怎样加费、怎样下毒启发式、怎样混输入、怎样回版本不支持。
