# 例：看见看见承诺哈希不是数据已经永存不是已经永存；看见seeing the commitment hash is not already perpetual data不是已经是不变量 145；看见看见承诺哈希不是数据已经永存不是已经是不变量 9

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-4844](https://eips.ethereum.org/EIPS/eip-4844)（KZG sidecar vs PeerDAS vs Celestia DAS）。对照 [EIP-7594](https://eips.ethereum.org/EIPS/eip-7594)。  
**对应课文**：[L5.4](../../courses/level-05-ethereum/L05-M04-state-blobs-mev.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-4844 hash-committed not already perpetual / not already 145 / not already 9 正式三事（23 余量）/ not 1517 kdas-notperm interchangeable / not 23 blob-vs-das bundled interchangeable」，不是 blob vs das bundled（23），也不是已经 blob气≠执行气（145），也不是已经 提交≠兑付（9）。不要另写 怎样扣列、怎样只问RPC就显示已抽样。

## 官方三件事

1. **看见看见承诺哈希不是数据已经永存 / 看见看见承诺哈希不是数据已经永存 这份对象 is not already 已经永存 interchangeable，也不是已经 blob vs das bundled（23） interchangeable / 1517 kdas-notperm interchangeable / 1515 kdas-notpeer interchangeable，也不是已经 EIP-4844 hash-committed not already perpetual / not already 145 / not already 9 正式三事 bundled（23 item 3 余量） interchangeable / 23 kdas item 3 interchangeable。**  
   官方把看见承诺哈希不是数据已经永存和已经永存写成两件。看见看见承诺哈希不是数据已经永存，不是已经永存。

2. **看见seeing the commitment hash is not already perpetual data / 看见看见承诺哈希不是数据已经永存 / 这份对象 is not already 已经是不变量 145 interchangeable，也不是已经 blob vs das bundled（23） interchangeable / 1517 kdas-notperm interchangeable / 1516 kdas-notcel interchangeable，也不是已经 blob气≠执行气 interchangeable / 145 blob气≠执行气 interchangeable。**  
   官方把seeing the commitment hash is not already perpetual data和已经是不变量 145写成两件。看见seeing the commitment hash is not already perpetual data，不是已经是不变量 145。

3. **看见看见承诺哈希不是数据已经永存 / 看见seeing the commitment hash is not already perpetual data / 这份对象 is not already 已经是不变量 9 interchangeable，也不是已经 blob vs das bundled（23） interchangeable / 1517 kdas-notperm interchangeable / 1515 kdas-notpeer interchangeable，也不是已经 提交≠兑付 interchangeable / 9 提交≠兑付 interchangeable。**  
   官方把看见承诺哈希不是数据已经永存和已经是不变量 9写成两件。看见看见承诺哈希不是数据已经永存，不是已经是不变量 9。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样扣列、怎样只问RPC就显示已抽样。

## 官方为什么这样拆

- **看见承诺哈希不是数据已经永存 interchangeable：官方写 sidecar 有服务窗，hash 还在不是袋还在。**
- **看见本页不是已经是不变量 145。**
- **看见本页不是已经是不变量 9。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经永存 | 不是已经永存 | 不是已经blob气≠执行气（145） |
| 已经是不变量 145 | 不是已经是不变量 145 | 不是已经提交≠兑付（9） |
| 已经是不变量 9 | 不是已经是不变量 9 | 不是已经1515 kdas-notpeer |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-4844 hash-committed not already perpetual / not already 145 / not already 9 正式三事（23 余量），必须分开是不是已经永存、是不是已经是不变量 145、是不是已经是不变量 9。可以跳过「看见 KZG 就已经是 DAS」。不要另写 怎样扣列、怎样只问RPC就显示已抽样。23 blob vs das bundled unbundling 在本页 item 3 完成；本页收束本批。下一份仍捆着的官方对象：assumevalid。

## 本页不抄

- 现行每块blob个数、fork epoch、动机段1/8、换算成天数。
- 怎样扣列、怎样只问RPC就显示已抽样。
