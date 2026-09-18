# 例：看见ping 里有序号不是已经拿到当前记录；看见两边序号对上不是已经把记录取回来；看见ping 里有序号不是记录已经在手里

**层次**：网络 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-868](https://eips.ethereum.org/EIPS/eip-868)（Final, Networking；依赖 8、778）。  
**对应课文**：[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.1、L5.4、05b。本页是「EIP-868 ping not already have / not already fetched / not already in-hand 正式三事（241 余量）/ not 1292 enreq-notping interchangeable / not 241 enr-request-vs-have bundled interchangeable」，不是 enr request vs have bundled（241），也不是已经 enr-newest（240），也不是已经 forkid-same（239）。不要另写 怎样造放大流量、怎样伪造答复、怎样用过期包试探。

## 官方三件事

1. **看见ping 里有序号 / 看见ping 里有序号 这份对象 is not already 已经拿到当前记录 interchangeable，也不是已经 enr request vs have bundled（241） interchangeable / 1292 enreq-notping interchangeable / 1293 enreq-notreq interchangeable，也不是已经 EIP-868 ping not already have / not already fetched / not already in-hand 正式三事 bundled（241 item 1 余量） interchangeable / 241 enreq item 1 interchangeable。**  
   官方把ping 里有序号和已经拿到当前记录写成两件。看见ping 里有序号，不是已经拿到当前记录。

2. **看见两边序号对上 / 看见ping 里有序号 / 这份对象 is not already 已经把记录取回来 interchangeable，也不是已经 enr request vs have bundled（241） interchangeable / 1292 enreq-notping interchangeable / 1294 enreq-notfind interchangeable，也不是已经 enr-newest interchangeable / 240 enr-newest interchangeable。**  
   官方把两边序号对上和已经把记录取回来写成两件。看见两边序号对上，不是已经把记录取回来。

3. **看见ping 里有序号 / 看见两边序号对上 / 这份对象 is not already 记录已经在手里 interchangeable，也不是已经 enr request vs have bundled（241） interchangeable / 1292 enreq-notping interchangeable / 1293 enreq-notreq interchangeable，也不是已经 forkid-same interchangeable / 239 forkid-same interchangeable。**  
   官方把ping 里有序号和记录已经在手里写成两件。看见ping 里有序号，不是记录已经在手里。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样造放大流量、怎样伪造答复、怎样用过期包试探。

## 官方为什么这样拆

- **序号在 ping 里 不是已经有记录：官方要桥接当时的发现网和以后的发现网。**
- **两边序号对上 不是已经取回记录：官方写看见两边序号对上，不是已经把记录取回来。**
- **能通告序号 不是记录已经在手里：官方写看见能通告序号，不是记录已经在手里。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经拿到当前记录 | 不是已经拿到当前记录 | 不是已经enr-newest（240） |
| 已经把记录取回来 | 不是已经把记录取回来 | 不是已经forkid-same（239） |
| 记录已经在手里 | 不是记录已经在手里 | 不是已经1293 enreq-notreq |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-868 ping not already have / not already fetched / not already in-hand 正式三事（241 余量），必须分开是不是已经拿到当前记录、是不是已经把记录取回来、是不是记录已经在手里。可以跳过「看见 ping 带了序号就已经有当前记录」。不要另写 怎样造放大流量、怎样伪造答复、怎样用过期包试探。241 enr request vs have bundled unbundling 在本页 item 1 启动；续 [`worked-example-enreq-notreq-vs-bundled.md`](worked-example-enreq-notreq-vs-bundled.md)（不变量 1293 item 2）。

## 本页不抄

- 包类型号、过期字段怎么填、查找跳数。
- 怎样造放大流量、怎样伪造答复、怎样用过期包试探。
