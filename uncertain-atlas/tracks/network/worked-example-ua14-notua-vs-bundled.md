# 例：看见user agent不是已经可以按实现改行为；看见一条 user agent不是已经可以按这家实现换规则；看见user agent不是已经是本页允许的行为

**层次**：网络 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-14](https://github.com/bitcoin/bips/blob/master/bip-0014.mediawiki)（Deployed, Peer Services）。  
**对应课文**：[L3.4](../../courses/level-03-bitcoin/L03-M04-network-and-eclipse.md)、[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：Ethereum 行、L5.1、05b、M5.4、L5.4、03 共识。本页是「BIP-14 user-agent not already change-behavior / not already swap-rules / not already allowed-fingerprint 正式三事（263 余量）/ not 1272 ua14-notua interchangeable / not 263 ua-vs-protocol bundled interchangeable」，不是 ua vs protocol bundled（263），也不是已经 feature-enabled（259），也不是已经 pong-live（262）。不要另写 怎样按 user agent 指纹认人、怎样靠它排斥故障客户端、怎样按实现换协议。

## 官方三件事

1. **看见user agent / 看见user agent 这份对象 is not already 已经可以按实现改行为 interchangeable，也不是已经 ua vs protocol bundled（263） interchangeable / 1272 ua14-notua interchangeable / 1271 ua14-notcli interchangeable，也不是已经 BIP-14 user-agent not already change-behavior / not already swap-rules / not already allowed-fingerprint 正式三事 bundled（263 item 2 余量） interchangeable / 263 ua item 2 interchangeable。**  
   官方把user agent和已经可以按实现改行为写成两件。看见user agent，不是已经可以按实现改行为。

2. **看见一条 user agent / 看见user agent / 这份对象 is not already 已经可以按这家实现换规则 interchangeable，也不是已经 ua vs protocol bundled（263） interchangeable / 1272 ua14-notua interchangeable / 1273 ua14-notsame interchangeable，也不是已经 feature-enabled interchangeable / 259 feature-enabled interchangeable。**  
   官方把一条 user agent和已经可以按这家实现换规则写成两件。看见一条 user agent，不是已经可以按这家实现换规则。

3. **看见user agent / 看见一条 user agent / 这份对象 is not already 已经是本页允许的行为 interchangeable，也不是已经 ua vs protocol bundled（263） interchangeable / 1272 ua14-notua interchangeable / 1271 ua14-notcli interchangeable，也不是已经 pong-live interchangeable / 262 pong-live interchangeable。**  
   官方把user agent和已经是本页允许的行为写成两件。看见user agent，不是已经是本页允许的行为。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样按 user agent 指纹认人、怎样靠它排斥故障客户端、怎样按实现换协议。

## 官方为什么这样拆

- **user agent 不是已经可以按实现改行为：官方把按实现换协议写成会撕开网络。**
- **靠 user agent 认人 不是已经可以按这家换规则：官方写它不提供按不同实现绕开的方法。**
- **按 user agent 排斥 不是已经是本页允许的行为：官方把按 user agent 去排斥故障客户端写成极不推荐。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经可以按实现改行为 | 不是已经可以按实现改行为 | 不是已经feature-enabled（259） |
| 已经可以按这家实现换规则 | 不是已经可以按这家实现换规则 | 不是已经pong-live（262） |
| 已经是本页允许的行为 | 不是已经是本页允许的行为 | 不是已经1271 ua14-notcli |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-14 user-agent not already change-behavior / not already swap-rules / not already allowed-fingerprint 正式三事（263 余量），必须分开是不是已经可以按实现改行为、是不是已经可以按这家实现换规则、是不是已经是本页允许的行为。可以跳过「看见 user agent 就已经按这家换规则」。不要另写 怎样按 user agent 指纹认人、怎样靠它排斥故障客户端、怎样按实现换协议。263 ua vs protocol bundled unbundling 在本页 item 2 续；续 [`worked-example-ua14-notsame-vs-bundled.md`](worked-example-ua14-notsame-vs-bundled.md)（不变量 1273 item 3）。

## 本页不抄

- user agent 栈写法、保留分隔符、例串、剥开时的版本数字。
- 怎样按 user agent 指纹认人、怎样靠它排斥故障客户端、怎样按实现换协议。
