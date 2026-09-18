# 例：看见发了 sendaddrv2 不是已经只收后继格式；看见偏好信号不是旧线已经退役；看见发或不发不是未请求偏好已经谈妥

**层次**：网络 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-155](https://github.com/bitcoin/bips/blob/master/bip-0155.mediawiki)（Deployed, Peer Services）。  
**对应课文**：[L3.4](../../courses/level-03-bitcoin/L03-M04-network-and-eclipse.md)、[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：index/03 共识行、Ethereum 行、M5.4、L5.1、L5.4、05b。本页是「BIP-155 sendaddrv2 not already only-v2 / not already old-retired / not already unsolicited-pref 正式三事（246 余量）/ not 1233 addr155-notpref interchangeable / not 246 addrv2-vs-reachable bundled interchangeable」，不是 addrv2 bundled（246），也不是第 2 版传输就已经私人（241），也不是发现记录就已经是当前记录（240）。不要另写 怎样按传了哪些网认出节点、怎样骗节点去传无效地址、怎样把同一份地址拆成两个身份。

## 官方三件事

1. **看见发了 sendaddrv2 / 看见偏好信号 这份对象 is not already 已经只收后继格式 interchangeable，也不是已经 addrv2 bundled（246） interchangeable / 1233 addr155-notpref interchangeable / 1232 addr155-notreach interchangeable / 246 addrv2 item 2 interchangeable，也不是已经 BIP-155 sendaddrv2 not already only-v2 / not already old-retired / not already unsolicited-pref 正式三事 bundled（246 item 2 余量） interchangeable / 246 addrv2 item 2 interchangeable。**  
   官方写：发出这条信号，表示这个节点能理解后继地址消息，并且更想收它而不是旧地址消息。发或不发，都不表示对「没要就送来的地址」有没有偏好。没发这条信号的旧对等节点，继续收旧地址消息；新引进的地址类型对这些旧对等节点忽略。看见发了 sendaddrv2，不是已经只收后继格式，也不是旧地址消息已经退役，也不是未请求地址偏好已经谈妥。

2. **看见偏好信号 / 看见发了 sendaddrv2 / 这份对象 is not already 旧地址消息已经退役 interchangeable，也不是已经 addrv2 bundled（246） interchangeable / 1233 addr155-notpref interchangeable / 1234 addr155-notnet interchangeable，也不是已经 discovery-record interchangeable / 241 discovery-record interchangeable。**  
   官方把「能懂后继格式」和「旧线已关」写成两件。看见偏好信号，不是旧地址消息已经退役。

3. **看见发或不发 / 看见发了 sendaddrv2 / 这份对象 is not already 未请求地址偏好已经谈妥 interchangeable，也不是已经 addrv2 bundled（246） interchangeable / 1233 addr155-notpref interchangeable / 1232 addr155-notreach interchangeable，也不是已经 node-record interchangeable / 240 node-record interchangeable。**  
   官方把发或不发和未请求地址偏好写成两件。看见发或不发，不是未请求地址偏好已经谈妥。

网络编号取值、一次条数上限、地址字节上限、各网编码步骤是规范里的数字和算法，本页不抄。不要另写 怎样按传了哪些网认出节点、怎样骗节点去传无效地址、怎样把同一份地址拆成两个身份。

## 官方为什么这样拆

- **发了 sendaddrv2 不是已经只收后继格式：官方把能懂、更想收写成信号，不是已经关掉旧线。**
- **偏好信号 不是旧线已经退役：没发这条信号的旧对等节点继续收旧地址消息。**
- **发或不发 不是未请求偏好已经谈妥：官方写发或不发都不表示对没要就送来的地址有没有偏好。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经只收后继格式 | 不是已经只收后继格式 | 不是已经discovery-record（241） |
| 旧地址消息已经退役 | 不是旧地址消息已经退役 | 不是已经node-record（240） |
| 未请求地址偏好已经谈妥 | 不是未请求地址偏好已经谈妥 | 不是已经1232 addr155-notreach |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-155 sendaddrv2 not already only-v2 / not already old-retired / not already unsolicited-pref 正式三事（246 余量），必须分开是不是已经只收后继格式、是不是旧地址消息已经退役、是不是未请求地址偏好已经谈妥。可以跳过「看见后继地址流言就已经连上邻居」。不要另写 怎样按传了哪些网认出节点、怎样骗节点去传无效地址、怎样把同一份地址拆成两个身份。246 addrv2 vs reachable bundled unbundling 在本页 item 2 续；续 [`worked-example-addr155-notnet-vs-bundled.md`](worked-example-addr155-notnet-vs-bundled.md)（不变量 1234 item 3）。

## 本页不抄

- 网络编号取值、一次条数上限、地址字节上限、各网编码步骤、校验算法。
- 怎样按传了哪些网认出节点、怎样骗节点去传无效地址、怎样把同一份地址拆成两个身份。
