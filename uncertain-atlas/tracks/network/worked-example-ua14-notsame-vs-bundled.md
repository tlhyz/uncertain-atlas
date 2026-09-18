# 例：看见同一协议版本不是已经是同一套实现；看见user agent 栈不是已经是协议能力；看见同一协议版本不是已经谈妥了某项功能

**层次**：网络 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-14](https://github.com/bitcoin/bips/blob/master/bip-0014.mediawiki)（Deployed, Peer Services）。  
**对应课文**：[L3.4](../../courses/level-03-bitcoin/L03-M04-network-and-eclipse.md)、[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：Ethereum 行、L5.1、05b、M5.4、L5.4、03 共识。本页是「BIP-14 same-proto not already same-impl / not already capability / not already feature 正式三事（263 余量）/ not 1273 ua14-notsame interchangeable / not 263 ua-vs-protocol bundled interchangeable」，不是 ua vs protocol bundled（263），也不是已经 feature-enabled（259），也不是已经 pong-live（262）。不要另写 怎样按 user agent 指纹认人、怎样靠它排斥故障客户端、怎样按实现换协议。

## 官方三件事

1. **看见同一协议版本 / 看见同一协议版本 这份对象 is not already 已经是同一套实现 interchangeable，也不是已经 ua vs protocol bundled（263） interchangeable / 1273 ua14-notsame interchangeable / 1271 ua14-notcli interchangeable，也不是已经 BIP-14 same-proto not already same-impl / not already capability / not already feature 正式三事 bundled（263 item 3 余量） interchangeable / 263 ua item 3 interchangeable。**  
   官方把同一协议版本和已经是同一套实现写成两件。看见同一协议版本，不是已经是同一套实现。

2. **看见user agent 栈 / 看见同一协议版本 / 这份对象 is not already 已经是协议能力 interchangeable，也不是已经 ua vs protocol bundled（263） interchangeable / 1273 ua14-notsame interchangeable / 1272 ua14-notua interchangeable，也不是已经 feature-enabled interchangeable / 259 feature-enabled interchangeable。**  
   官方把user agent 栈和已经是协议能力写成两件。看见user agent 栈，不是已经是协议能力。

3. **看见同一协议版本 / 看见user agent 栈 / 这份对象 is not already 已经谈妥了某项功能 interchangeable，也不是已经 ua vs protocol bundled（263） interchangeable / 1273 ua14-notsame interchangeable / 1271 ua14-notcli interchangeable，也不是已经 pong-live interchangeable / 262 pong-live interchangeable。**  
   官方把同一协议版本和已经谈妥了某项功能写成两件。看见同一协议版本，不是已经谈妥了某项功能。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样按 user agent 指纹认人、怎样靠它排斥故障客户端、怎样按实现换协议。

## 官方为什么这样拆

- **同一协议版本 不是已经是同一套实现：官方允许同一协议版本底下坐不同代码库。**
- **user agent 栈 不是已经是协议能力：官方写 user agent 只是信息。**
- **叠了几层名字 不是已经谈妥了某项功能：官方把协议版本用来区分节点，user agent 只是信息牌。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是同一套实现 | 不是已经是同一套实现 | 不是已经feature-enabled（259） |
| 已经是协议能力 | 不是已经是协议能力 | 不是已经pong-live（262） |
| 已经谈妥了某项功能 | 不是已经谈妥了某项功能 | 不是已经1271 ua14-notcli |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-14 same-proto not already same-impl / not already capability / not already feature 正式三事（263 余量），必须分开是不是已经是同一套实现、是不是已经是协议能力、是不是已经谈妥了某项功能。可以跳过「看见 user agent 就已经按这家换规则」。不要另写 怎样按 user agent 指纹认人、怎样靠它排斥故障客户端、怎样按实现换协议。263 ua vs protocol bundled unbundling 在本页 item 3 完成；本页收束本批。

## 本页不抄

- user agent 栈写法、保留分隔符、例串、剥开时的版本数字。
- 怎样按 user agent 指纹认人、怎样靠它排斥故障客户端、怎样按实现换协议。
