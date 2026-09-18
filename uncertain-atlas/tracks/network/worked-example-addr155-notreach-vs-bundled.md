# 例：看见后继地址流言不是已经连得上；看见更长容器不是已经可达；看见后继地址消息不是旧格式已经退役

**层次**：网络 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-155](https://github.com/bitcoin/bips/blob/master/bip-0155.mediawiki)（Deployed, Peer Services）。  
**对应课文**：[L3.4](../../courses/level-03-bitcoin/L03-M04-network-and-eclipse.md)、[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：index/03 共识行、Ethereum 行、M5.4、L5.1、L5.4、05b。本页是「BIP-155 addrv2-gossip not already connected / not already reachable / not already old-retired 正式三事（246 余量）/ not 1232 addr155-notreach interchangeable / not 246 addrv2-vs-reachable bundled interchangeable」，不是 addrv2 bundled（246），也不是第 2 版传输就已经私人（242），也不是发现记录就已经是当前记录（241）。不要另写 怎样按传了哪些网认出节点、怎样骗节点去传无效地址、怎样把同一份地址拆成两个身份。

## 官方三件事

1. **看见后继地址流言 / 看见更长容器 这份对象 is not already 已经连得上 interchangeable，也不是已经 addrv2 bundled（246） interchangeable / 1232 addr155-notreach interchangeable / 1233 addr155-notpref interchangeable / 246 addrv2 item 2 interchangeable，也不是已经 BIP-155 addrv2-gossip not already connected / not already reachable / not already old-retired 正式三事 bundled（246 item 1 余量） interchangeable / 246 addrv2 item 1 interchangeable。**  
   官方写：要新增一条点对点消息，好在网上流言更长的节点地址。旧地址消息只有固定宽度，装不下新一代洋葱地址、I2P，以及别的更长端点。看见后继地址消息，不是已经连上这个节点，也不是已经可达，也不是旧地址格式已经对所有对等节点退役。

2. **看见更长容器 / 看见后继地址流言 / 这份对象 is not already 已经可达 interchangeable，也不是已经 addrv2 bundled（246） interchangeable / 1232 addr155-notreach interchangeable / 1234 addr155-notnet interchangeable，也不是已经 v2-private interchangeable / 242 v2-private interchangeable。**  
   官方把更长容器和已经连得上写成两件。看见能装洋葱或 I2P，不是已经拨通。

3. **看见后继地址消息 / 看见后继地址流言 / 这份对象 is not already 旧地址格式已经退役 interchangeable，也不是已经 addrv2 bundled（246） interchangeable / 1232 addr155-notreach interchangeable / 1233 addr155-notpref interchangeable，也不是已经 v1-fallback interchangeable / 112 v1-fallback interchangeable。**  
   官方把后继地址消息和旧格式已经退役写成两件。看见后继地址消息，不是旧格式已经退役。

网络编号取值、一次条数上限、地址字节上限、各网编码步骤是规范里的数字和算法，本页不抄。不要另写 怎样按传了哪些网认出节点、怎样骗节点去传无效地址、怎样把同一份地址拆成两个身份。

## 官方为什么这样拆

- **后继地址流言 不是已经连得上：官方只给流言换容器。看见能装洋葱或 I2P，不是已经拨通。**
- **更长容器 不是已经可达：官方把能传更长端点和已经拨通写成两件。**
- **后继地址消息 不是旧格式已经退役：没发 sendaddrv2 的旧对等节点继续收旧地址消息。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经连得上 | 不是已经连得上 | 不是已经v2-private（242） |
| 已经可达 | 不是已经可达 | 不是已经v1-fallback（112） |
| 旧地址格式已经退役 | 不是旧地址格式已经退役 | 不是已经1233 addr155-notpref |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-155 addrv2-gossip not already connected / not already reachable / not already old-retired 正式三事（246 余量），必须分开是不是已经连得上、是不是已经可达、是不是旧地址格式已经退役。可以跳过「看见后继地址流言就已经连上邻居」。不要另写 怎样按传了哪些网认出节点、怎样骗节点去传无效地址、怎样把同一份地址拆成两个身份。246 addrv2 vs reachable bundled unbundling 在本页 item 1 启动；续 [`worked-example-addr155-notpref-vs-bundled.md`](worked-example-addr155-notpref-vs-bundled.md)（不变量 1233 item 2）。

## 本页不抄

- 网络编号取值、一次条数上限、地址字节上限、各网编码步骤、校验算法。
- 怎样按传了哪些网认出节点、怎样骗节点去传无效地址、怎样把同一份地址拆成两个身份。
