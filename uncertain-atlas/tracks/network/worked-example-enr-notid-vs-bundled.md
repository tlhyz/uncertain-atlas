# 例：看见默认方案名不是已经换了发现协议；看见能走 DNS 转发不是已经换了签名方案；看见默认方案名不是已经从发现里找到

**层次**：网络 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-778](https://eips.ethereum.org/EIPS/eip-778)（Final, Networking）。  
**对应课文**：[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.1、L5.4、05b。本页是「EIP-778 scheme not already new-disc / not already new-scheme / not already found-trusted 正式三事（240 余量）/ not 1291 enr-notid interchangeable / not 240 enr-vs-newest bundled interchangeable」，不是 enr vs newest bundled（240），也不是已经 enr-request（241），也不是已经 eip8-compat（235）。不要另写 怎样造记录、怎样磨序号、怎样靠 DNS 冒充邻居。

## 官方三件事

1. **看见默认方案名 / 看见默认方案名 这份对象 is not already 已经换了发现协议 interchangeable，也不是已经 enr vs newest bundled（240） interchangeable / 1291 enr-notid interchangeable / 1289 enr-notkeys interchangeable，也不是已经 EIP-778 scheme not already new-disc / not already new-scheme / not already found-trusted 正式三事 bundled（240 item 3 余量） interchangeable / 240 enr item 3 interchangeable。**  
   官方把默认方案名和已经换了发现协议写成两件。看见默认方案名，不是已经换了发现协议。

2. **看见能走 DNS 转发 / 看见默认方案名 / 这份对象 is not already 已经换了签名方案 interchangeable，也不是已经 enr vs newest bundled（240） interchangeable / 1291 enr-notid interchangeable / 1290 enr-notnew interchangeable，也不是已经 enr-request interchangeable / 241 enr-request interchangeable。**  
   官方把能走 DNS 转发和已经换了签名方案写成两件。看见能走 DNS 转发，不是已经换了签名方案。

3. **看见默认方案名 / 看见能走 DNS 转发 / 这份对象 is not already 已经从发现里找到 interchangeable，也不是已经 enr vs newest bundled（240） interchangeable / 1291 enr-notid interchangeable / 1289 enr-notkeys interchangeable，也不是已经 eip8-compat interchangeable / 235 eip8-compat interchangeable。**  
   官方把默认方案名和已经从发现里找到写成两件。看见默认方案名，不是已经从发现里找到。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样造记录、怎样磨序号、怎样靠 DNS 冒充邻居。

## 官方为什么这样拆

- **默认方案名 不是已经换了发现协议：官方写本页只定义一种默认方案，兼容发现第 4 版那套密码。**
- **多写键 不是已经换了签名方案：官方把谁都能加键和换签名方案要实现共识分开写。**
- **能走 DNS 转发 不是已经从发现找到：官方写记录可以通过 DNS、ENS、线协议子协议等任意机制转。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经换了发现协议 | 不是已经换了发现协议 | 不是已经enr-request（241） |
| 已经换了签名方案 | 不是已经换了签名方案 | 不是已经eip8-compat（235） |
| 已经从发现里找到 | 不是已经从发现里找到 | 不是已经1289 enr-notkeys |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-778 scheme not already new-disc / not already new-scheme / not already found-trusted 正式三事（240 余量），必须分开是不是已经换了发现协议、是不是已经换了签名方案、是不是已经从发现里找到。可以跳过「看见签过的节点记录就已经是最新一份」。不要另写 怎样造记录、怎样磨序号、怎样靠 DNS 冒充邻居。240 enr vs newest bundled unbundling 在本页 item 3 完成；本页收束本批。

## 本页不抄

- 测试向量、例钥、节点标识、例地址、例端口、编码上限取值。
- 怎样造记录、怎样磨序号、怎样靠 DNS 冒充邻居。
