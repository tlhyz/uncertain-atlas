# 例：看见FindNode 找到人不是已经有当前记录；看见公钥不是已经拿到记录；看见FindNode 找到人不是放大面已经消失

**层次**：网络 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-868](https://eips.ethereum.org/EIPS/eip-868)（Final, Networking；依赖 8、778）。  
**对应课文**：[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.1、L5.4、05b。本页是「EIP-868 find not already have / not already trusted / not already no-amp 正式三事（241 余量）/ not 1294 enreq-notfind interchangeable / not 241 enr-request-vs-have bundled interchangeable」，不是 enr request vs have bundled（241），也不是已经 enr-newest（240），也不是已经 eip8-compat（235）。不要另写 怎样造放大流量、怎样伪造答复、怎样用过期包试探。

## 官方三件事

1. **看见FindNode 找到人 / 看见FindNode 找到人 这份对象 is not already 已经有当前记录 interchangeable，也不是已经 enr request vs have bundled（241） interchangeable / 1294 enreq-notfind interchangeable / 1292 enreq-notping interchangeable，也不是已经 EIP-868 find not already have / not already trusted / not already no-amp 正式三事 bundled（241 item 3 余量） interchangeable / 241 enreq item 3 interchangeable。**  
   官方把FindNode 找到人和已经有当前记录写成两件。看见FindNode 找到人，不是已经有当前记录。

2. **看见公钥 / 看见FindNode 找到人 / 这份对象 is not already 已经拿到记录 interchangeable，也不是已经 enr request vs have bundled（241） interchangeable / 1294 enreq-notfind interchangeable / 1293 enreq-notreq interchangeable，也不是已经 enr-newest interchangeable / 240 enr-newest interchangeable。**  
   官方把公钥和已经拿到记录写成两件。看见公钥，不是已经拿到记录。

3. **看见FindNode 找到人 / 看见公钥 / 这份对象 is not already 放大面已经消失 interchangeable，也不是已经 enr request vs have bundled（241） interchangeable / 1294 enreq-notfind interchangeable / 1292 enreq-notping interchangeable，也不是已经 eip8-compat interchangeable / 235 eip8-compat interchangeable。**  
   官方把FindNode 找到人和放大面已经消失写成两件。看见FindNode 找到人，不是放大面已经消失。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样造放大流量、怎样伪造答复、怎样用过期包试探。

## 官方为什么这样拆

- **FindNode 找到人 不是已经有记录：官方写找到节点后再发请求。**
- **看见公钥 不是已经有当前记录：官方写要按公钥解析当前记录，先递归查找。**
- **协议里有请求 不是放大面已经消失：官方把防护写成和 FindNode 同一类。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经有当前记录 | 不是已经有当前记录 | 不是已经enr-newest（240） |
| 已经拿到记录 | 不是已经拿到记录 | 不是已经eip8-compat（235） |
| 放大面已经消失 | 不是放大面已经消失 | 不是已经1292 enreq-notping |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-868 find not already have / not already trusted / not already no-amp 正式三事（241 余量），必须分开是不是已经有当前记录、是不是已经拿到记录、是不是放大面已经消失。可以跳过「看见 ping 带了序号就已经有当前记录」。不要另写 怎样造放大流量、怎样伪造答复、怎样用过期包试探。241 enr request vs have bundled unbundling 在本页 item 3 完成；本页收束本批。

## 本页不抄

- 包类型号、过期字段怎么填、查找跳数。
- 怎样造放大流量、怎样伪造答复、怎样用过期包试探。
