# 例：看见能多写键被收下不是已经解释这些键；看见签过的记录不是已经有了可连的地址；看见能多写键被收下不是发现已经升级完

**层次**：网络 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-778](https://eips.ethereum.org/EIPS/eip-778)（Final, Networking）。  
**对应课文**：[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.1、L5.4、05b。本页是「EIP-778 keys not already interpreted / not already endpoint / not already disc-upgraded 正式三事（240 余量）/ not 1289 enr-notkeys interchangeable / not 240 enr-vs-newest bundled interchangeable」，不是 enr vs newest bundled（240），也不是已经 forkid-same（239），也不是已经 eip8-compat（235）。不要另写 怎样造记录、怎样磨序号、怎样靠 DNS 冒充邻居。

## 官方三件事

1. **看见能多写键被收下 / 看见能多写键被收下 这份对象 is not already 已经解释这些键 interchangeable，也不是已经 enr vs newest bundled（240） interchangeable / 1289 enr-notkeys interchangeable / 1290 enr-notnew interchangeable，也不是已经 EIP-778 keys not already interpreted / not already endpoint / not already disc-upgraded 正式三事 bundled（240 item 1 余量） interchangeable / 240 enr item 1 interchangeable。**  
   官方把能多写键被收下和已经解释这些键写成两件。看见能多写键被收下，不是已经解释这些键。

2. **看见签过的记录 / 看见能多写键被收下 / 这份对象 is not already 已经有了可连的地址 interchangeable，也不是已经 enr vs newest bundled（240） interchangeable / 1289 enr-notkeys interchangeable / 1291 enr-notid interchangeable，也不是已经 forkid-same interchangeable / 239 forkid-same interchangeable。**  
   官方把签过的记录和已经有了可连的地址写成两件。看见签过的记录，不是已经有了可连的地址。

3. **看见能多写键被收下 / 看见签过的记录 / 这份对象 is not already 发现已经升级完 interchangeable，也不是已经 enr vs newest bundled（240） interchangeable / 1289 enr-notkeys interchangeable / 1290 enr-notnew interchangeable，也不是已经 eip8-compat interchangeable / 235 eip8-compat interchangeable。**  
   官方把能多写键被收下和发现已经升级完写成两件。看见能多写键被收下，不是发现已经升级完。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样造记录、怎样磨序号、怎样靠 DNS 冒充邻居。

## 官方为什么这样拆

- **灵活格式 不是已经发现：官方说第 4 版发现转不了别的信息。**
- **签过 不是已经有端点：官方写没有端点信息的记录，只要签名合法，仍然有效。**
- **多写键 不是发现已经升级：官方写已有客户端应接受任何键值对，不论能不能解释。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经解释这些键 | 不是已经解释这些键 | 不是已经forkid-same（239） |
| 已经有了可连的地址 | 不是已经有了可连的地址 | 不是已经eip8-compat（235） |
| 发现已经升级完 | 不是发现已经升级完 | 不是已经1290 enr-notnew |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-778 keys not already interpreted / not already endpoint / not already disc-upgraded 正式三事（240 余量），必须分开是不是已经解释这些键、是不是已经有了可连的地址、是不是发现已经升级完。可以跳过「看见签过的节点记录就已经是最新一份」。不要另写 怎样造记录、怎样磨序号、怎样靠 DNS 冒充邻居。240 enr vs newest bundled unbundling 在本页 item 1 启动；续 [`worked-example-enr-notnew-vs-bundled.md`](worked-example-enr-notnew-vs-bundled.md)（不变量 1290 item 2）。

## 本页不抄

- 测试向量、例钥、节点标识、例地址、例端口、编码上限取值。
- 怎样造记录、怎样磨序号、怎样靠 DNS 冒充邻居。
