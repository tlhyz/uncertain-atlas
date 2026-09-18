# 例：看见签过的记录不是已经是最新一份；看见能验不是已经比过序号；看见签过的记录不是全网已经换完

**层次**：网络 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-778](https://eips.ethereum.org/EIPS/eip-778)（Final, Networking）。  
**对应课文**：[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.1、L5.4、05b。本页是「EIP-778 signed not already newest / not already compared / not already network-swapped 正式三事（240 余量）/ not 1290 enr-notnew interchangeable / not 240 enr-vs-newest bundled interchangeable」，不是 enr vs newest bundled（240），也不是已经 enr-request（241），也不是已经 forkid-same（239）。不要另写 怎样造记录、怎样磨序号、怎样靠 DNS 冒充邻居。

## 官方三件事

1. **看见签过的记录 / 看见签过的记录 这份对象 is not already 已经是最新一份 interchangeable，也不是已经 enr vs newest bundled（240） interchangeable / 1290 enr-notnew interchangeable / 1289 enr-notkeys interchangeable，也不是已经 EIP-778 signed not already newest / not already compared / not already network-swapped 正式三事 bundled（240 item 2 余量） interchangeable / 240 enr item 2 interchangeable。**  
   官方把签过的记录和已经是最新一份写成两件。看见签过的记录，不是已经是最新一份。

2. **看见能验 / 看见签过的记录 / 这份对象 is not already 已经比过序号 interchangeable，也不是已经 enr vs newest bundled（240） interchangeable / 1290 enr-notnew interchangeable / 1291 enr-notid interchangeable，也不是已经 enr-request interchangeable / 241 enr-request interchangeable。**  
   官方把能验和已经比过序号写成两件。看见能验，不是已经比过序号。

3. **看见签过的记录 / 看见能验 / 这份对象 is not already 全网已经换完 interchangeable，也不是已经 enr vs newest bundled（240） interchangeable / 1290 enr-notnew interchangeable / 1289 enr-notkeys interchangeable，也不是已经 forkid-same interchangeable / 239 forkid-same interchangeable。**  
   官方把签过的记录和全网已经换完写成两件。看见签过的记录，不是全网已经换完。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样造记录、怎样磨序号、怎样靠 DNS 冒充邻居。

## 官方为什么这样拆

- **签过 不是已经最新：官方要的是权威更新，不是验过签就永远这一份。**
- **能验 不是已经比过序号：官方写记录一变，节点应把序号加大并再发布。**
- **看见序号 不是全网已经换完：官方写别人应能判断哪一份更新。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是最新一份 | 不是已经是最新一份 | 不是已经enr-request（241） |
| 已经比过序号 | 不是已经比过序号 | 不是已经forkid-same（239） |
| 全网已经换完 | 不是全网已经换完 | 不是已经1289 enr-notkeys |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-778 signed not already newest / not already compared / not already network-swapped 正式三事（240 余量），必须分开是不是已经是最新一份、是不是已经比过序号、是不是全网已经换完。可以跳过「看见签过的节点记录就已经是最新一份」。不要另写 怎样造记录、怎样磨序号、怎样靠 DNS 冒充邻居。240 enr vs newest bundled unbundling 在本页 item 2 续；续 [`worked-example-enr-notid-vs-bundled.md`](worked-example-enr-notid-vs-bundled.md)（不变量 1291 item 3）。

## 本页不抄

- 测试向量、例钥、节点标识、例地址、例端口、编码上限取值。
- 怎样造记录、怎样磨序号、怎样靠 DNS 冒充邻居。
