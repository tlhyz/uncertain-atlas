# 例：看见能发请求不是已经解析完；看见回了记录不是已经核过签名；看见能发请求不是已经验过是那个节点签的

**层次**：网络 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-868](https://eips.ethereum.org/EIPS/eip-868)（Final, Networking；依赖 8、778）。  
**对应课文**：[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.1、L5.4、05b。本页是「EIP-868 request not already parsed / not already signed-ok / not already verified 正式三事（241 余量）/ not 1293 enreq-notreq interchangeable / not 241 enr-request-vs-have bundled interchangeable」，不是 enr request vs have bundled（241），也不是已经 enr-newest（240），也不是已经 eip8-compat（235）。不要另写 怎样造放大流量、怎样伪造答复、怎样用过期包试探。

## 官方三件事

1. **看见能发请求 / 看见能发请求 这份对象 is not already 已经解析完 interchangeable，也不是已经 enr request vs have bundled（241） interchangeable / 1293 enreq-notreq interchangeable / 1292 enreq-notping interchangeable，也不是已经 EIP-868 request not already parsed / not already signed-ok / not already verified 正式三事 bundled（241 item 2 余量） interchangeable / 241 enreq item 2 interchangeable。**  
   官方把能发请求和已经解析完写成两件。看见能发请求，不是已经解析完。

2. **看见回了记录 / 看见能发请求 / 这份对象 is not already 已经核过签名 interchangeable，也不是已经 enr request vs have bundled（241） interchangeable / 1293 enreq-notreq interchangeable / 1294 enreq-notfind interchangeable，也不是已经 enr-newest interchangeable / 240 enr-newest interchangeable。**  
   官方把回了记录和已经核过签名写成两件。看见回了记录，不是已经核过签名。

3. **看见能发请求 / 看见回了记录 / 这份对象 is not already 已经验过是那个节点签的 interchangeable，也不是已经 enr request vs have bundled（241） interchangeable / 1293 enreq-notreq interchangeable / 1292 enreq-notping interchangeable，也不是已经 eip8-compat interchangeable / 235 eip8-compat interchangeable。**  
   官方把能发请求和已经验过是那个节点签的写成两件。看见能发请求，不是已经验过是那个节点签的。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样造放大流量、怎样伪造答复、怎样用过期包试探。

## 官方为什么这样拆

- **能发请求 不是已经解析：官方把要和核签写成两步。**
- **回了记录 不是已经核过签名：官方写收到答复的人应核这份记录是由发出答复的那个节点签的。**
- **能要 不是已经验过是那个节点签的：官方写看见能要，不是已经验过。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经解析完 | 不是已经解析完 | 不是已经enr-newest（240） |
| 已经核过签名 | 不是已经核过签名 | 不是已经eip8-compat（235） |
| 已经验过是那个节点签的 | 不是已经验过是那个节点签的 | 不是已经1292 enreq-notping |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-868 request not already parsed / not already signed-ok / not already verified 正式三事（241 余量），必须分开是不是已经解析完、是不是已经核过签名、是不是已经验过是那个节点签的。可以跳过「看见 ping 带了序号就已经有当前记录」。不要另写 怎样造放大流量、怎样伪造答复、怎样用过期包试探。241 enr request vs have bundled unbundling 在本页 item 2 续；续 [`worked-example-enreq-notfind-vs-bundled.md`](worked-example-enreq-notfind-vs-bundled.md)（不变量 1294 item 3）。

## 本页不抄

- 包类型号、过期字段怎么填、查找跳数。
- 怎样造放大流量、怎样伪造答复、怎样用过期包试探。
