# 例：看见协议版本不是已经是客户端版本；看见协议版本不是已经是实现版本；看见协议版本不是已经抬了协议

**层次**：网络 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-14](https://github.com/bitcoin/bips/blob/master/bip-0014.mediawiki)（Deployed, Peer Services）。  
**对应课文**：[L3.4](../../courses/level-03-bitcoin/L03-M04-network-and-eclipse.md)、[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：Ethereum 行、L5.1、05b、M5.4、L5.4、03 共识。本页是「BIP-14 proto-ver not already client-ver / not already impl-ver / not already raised-proto 正式三事（263 余量）/ not 1271 ua14-notcli interchangeable / not 263 ua-vs-protocol bundled interchangeable」，不是 ua vs protocol bundled（263），也不是已经 feature-enabled（259），也不是已经 pong-live（262）。不要另写 怎样按 user agent 指纹认人、怎样靠它排斥故障客户端、怎样按实现换协议。

## 官方三件事

1. **看见协议版本 / 看见协议版本 这份对象 is not already 已经是客户端版本 interchangeable，也不是已经 ua vs protocol bundled（263） interchangeable / 1271 ua14-notcli interchangeable / 1272 ua14-notua interchangeable，也不是已经 BIP-14 proto-ver not already client-ver / not already impl-ver / not already raised-proto 正式三事 bundled（263 item 1 余量） interchangeable / 263 ua item 1 interchangeable。**  
   官方把协议版本和已经是客户端版本写成两件。看见协议版本，不是已经是客户端版本。

2. **看见协议版本 / 看见协议版本 / 这份对象 is not already 已经是实现版本 interchangeable，也不是已经 ua vs protocol bundled（263） interchangeable / 1271 ua14-notcli interchangeable / 1273 ua14-notsame interchangeable，也不是已经 feature-enabled interchangeable / 259 feature-enabled interchangeable。**  
   官方把协议版本和已经是实现版本写成两件。看见协议版本，不是已经是实现版本。

3. **看见协议版本 / 看见协议版本 / 这份对象 is not already 已经抬了协议 interchangeable，也不是已经 ua vs protocol bundled（263） interchangeable / 1271 ua14-notcli interchangeable / 1272 ua14-notua interchangeable，也不是已经 pong-live interchangeable / 262 pong-live interchangeable。**  
   官方把协议版本和已经抬了协议写成两件。看见协议版本，不是已经抬了协议。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样按 user agent 指纹认人、怎样靠它排斥故障客户端、怎样按实现换协议。

## 官方为什么这样拆

- **协议版本 不是已经是客户端版本：官方把协议版本从客户端版本里拆开。**
- **协议版本 不是已经是实现版本：官方写块上的版本反映的是造这块时的协议版本。**
- **实现发了新版本 不是已经抬了协议：官方把两套数字曾经是同一个写成要拆开的病。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是客户端版本 | 不是已经是客户端版本 | 不是已经feature-enabled（259） |
| 已经是实现版本 | 不是已经是实现版本 | 不是已经pong-live（262） |
| 已经抬了协议 | 不是已经抬了协议 | 不是已经1272 ua14-notua |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-14 proto-ver not already client-ver / not already impl-ver / not already raised-proto 正式三事（263 余量），必须分开是不是已经是客户端版本、是不是已经是实现版本、是不是已经抬了协议。可以跳过「看见 user agent 就已经按这家换规则」。不要另写 怎样按 user agent 指纹认人、怎样靠它排斥故障客户端、怎样按实现换协议。263 ua vs protocol bundled unbundling 在本页 item 1 启动；续 [`worked-example-ua14-notua-vs-bundled.md`](worked-example-ua14-notua-vs-bundled.md)（不变量 1272 item 2）。

## 本页不抄

- user agent 栈写法、保留分隔符、例串、剥开时的版本数字。
- 怎样按 user agent 指纹认人、怎样靠它排斥故障客户端、怎样按实现换协议。
