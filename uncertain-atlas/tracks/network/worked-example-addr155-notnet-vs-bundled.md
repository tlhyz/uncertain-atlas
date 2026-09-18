# 例：看见在传某种网上的地址不是已经连上那种网；看见同一份地址换了编号不是已经是另一个人；看见旧洋葱类型编号不是已经能当隐藏服务用

**层次**：网络 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-155](https://github.com/bitcoin/bips/blob/master/bip-0155.mediawiki)（Deployed, Peer Services）。  
**对应课文**：[L3.4](../../courses/level-03-bitcoin/L03-M04-network-and-eclipse.md)、[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：index/03 共识行、Ethereum 行、M5.4、L5.1、L5.4、05b。本页是「BIP-155 gossip-net not already connected-to-net / not already two-peers / not already hidden-service 正式三事（246 余量）/ not 1234 addr155-notnet interchangeable / not 246 addrv2-vs-reachable bundled interchangeable」，不是 addrv2 bundled（246），也不是第 2 版传输就已经私人（242），也不是发现记录就已经是当前记录（241）。不要另写 怎样按传了哪些网认出节点、怎样骗节点去传无效地址、怎样把同一份地址拆成两个身份。

## 官方三件事

1. **看见在传某种网上的地址 / 看见同一份地址换了编号 这份对象 is not already 已经连上那种网 interchangeable，也不是已经 addrv2 bundled（246） interchangeable / 1234 addr155-notnet interchangeable / 1232 addr155-notreach interchangeable / 246 addrv2 item 2 interchangeable，也不是已经 BIP-155 gossip-net not already connected-to-net / not already two-peers / not already hidden-service 正式三事 bundled（246 item 3 余量） interchangeable / 246 addrv2 item 3 interchangeable。**  
   官方写：建议把认识的各种网上的地址都传出去，即使自己此刻没连上其中几种；这能帮多宿主节点，也让旁观者更难看清这个节点连了哪些网。不认识的网不要传，因为没法核这些地址，会被骗去传无效地址。某些网的地址已经有自己的编号，不得再拿另一套编号重发；否则同一份地址会被当成两个对等节点。官方还写：某一种已经停运的旧洋葱类型不得再传、收到必须忽略。看见在传某种网上的地址，不是已经连上那种网。看见同一份地址换了编号，不是已经是另一个人。看见旧洋葱类型编号，不是已经能当隐藏服务用。

2. **看见同一份地址换了编号 / 看见在传某种网上的地址 / 这份对象 is not already 已经是另一个人 interchangeable，也不是已经 addrv2 bundled（246） interchangeable / 1234 addr155-notnet interchangeable / 1233 addr155-notpref interchangeable，也不是已经 v2-private interchangeable / 242 v2-private interchangeable。**  
   官方把同一份地址换编号和已经是另一个人写成两件。看见换了编号，不是已经是两个对等节点意义上的另一个人——官方禁止这样重发。

3. **看见旧洋葱类型编号 / 看见在传某种网上的地址 / 这份对象 is not already 已经能当隐藏服务用 interchangeable，也不是已经 addrv2 bundled（246） interchangeable / 1234 addr155-notnet interchangeable / 1232 addr155-notreach interchangeable，也不是已经 discovery-record interchangeable / 241 discovery-record interchangeable。**  
   官方把旧洋葱类型编号和已经能当隐藏服务用写成两件。看见旧洋葱类型编号，必须忽略，不是已经能用。

网络编号取值、一次条数上限、地址字节上限、各网编码步骤是规范里的数字和算法，本页不抄。不要另写 怎样按传了哪些网认出节点、怎样骗节点去传无效地址、怎样把同一份地址拆成两个身份。

## 官方为什么这样拆

- **传了某种网 不是已经连上那种网：官方故意让没连上的网也传，好让旁观者难看清。**
- **同一份地址换了编号 不是已经是另一个人：官方禁止用另一套编号重发，否则会被当成两个对等节点。**
- **旧洋葱类型编号 不是已经能当隐藏服务用：官方写已经停运的旧洋葱类型不得再传、收到必须忽略。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经连上那种网 | 不是已经连上那种网 | 不是已经v2-private（242） |
| 已经是另一个人 | 不是已经是另一个人 | 不是已经discovery-record（241） |
| 已经能当隐藏服务用 | 不是已经能当隐藏服务用 | 不是已经1232 addr155-notreach |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-155 gossip-net not already connected-to-net / not already two-peers / not already hidden-service 正式三事（246 余量），必须分开是不是已经连上那种网、是不是已经是另一个人、是不是已经能当隐藏服务用。可以跳过「看见后继地址流言就已经连上邻居」。不要另写 怎样按传了哪些网认出节点、怎样骗节点去传无效地址、怎样把同一份地址拆成两个身份。246 addrv2 vs reachable bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 网络编号取值、一次条数上限、地址字节上限、各网编码步骤、校验算法。
- 怎样按传了哪些网认出节点、怎样骗节点去传无效地址、怎样把同一份地址拆成两个身份。
