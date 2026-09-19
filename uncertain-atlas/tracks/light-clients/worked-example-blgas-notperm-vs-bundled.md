# 例：看见付了blob fee不是数据已经永存不是已经永存；看见paying blob fee is not already perpetual data不是已经更安全；看见付了blob fee不是数据已经永存不是已经是不变量 101

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-4844](https://eips.ethereum.org/EIPS/eip-4844)（Shard Blob Transactions）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-4844 blob-fee-paid not already perpetual / not already safer / not already 101 正式三事（145 余量）/ not 1493 blgas-notperm interchangeable / not 145 blob-fee-vs-gas bundled interchangeable」，不是 blob fee vs gas bundled（145），也不是已经 气≠墙钟（101），也不是已经 策略≠共识（144）。不要另写 怎样扣 sidecar。

## 官方三件事

1. **看见付了blob fee不是数据已经永存 / 看见付了blob fee不是数据已经永存 这份对象 is not already 已经永存 interchangeable，也不是已经 blob fee vs gas bundled（145） interchangeable / 1493 blgas-notperm interchangeable / 1491 blgas-notexec interchangeable，也不是已经 EIP-4844 blob-fee-paid not already perpetual / not already safer / not already 101 正式三事 bundled（145 item 3 余量） interchangeable / 145 blgas item 3 interchangeable。**  
   官方把付了blob fee不是数据已经永存和已经永存写成两件。看见付了blob fee不是数据已经永存，不是已经永存。

2. **看见paying blob fee is not already perpetual data / 看见付了blob fee不是数据已经永存 / 这份对象 is not already 已经更安全 interchangeable，也不是已经 blob fee vs gas bundled（145） interchangeable / 1493 blgas-notperm interchangeable / 1492 blgas-notbyte interchangeable，也不是已经 气≠墙钟 interchangeable / 101 气≠墙钟 interchangeable。**  
   官方把paying blob fee is not already perpetual data和已经更安全写成两件。看见paying blob fee is not already perpetual data，不是已经更安全。

3. **看见付了blob fee不是数据已经永存 / 看见paying blob fee is not already perpetual data / 这份对象 is not already 已经是不变量 101 interchangeable，也不是已经 blob fee vs gas bundled（145） interchangeable / 1493 blgas-notperm interchangeable / 1491 blgas-notexec interchangeable，也不是已经 策略≠共识 interchangeable / 144 策略≠共识 interchangeable。**  
   官方把付了blob fee不是数据已经永存和已经是不变量 101写成两件。看见付了blob fee不是数据已经永存，不是已经是不变量 101。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样扣 sidecar。

## 官方为什么这样拆

- **付了blob fee不是数据已经永存 interchangeable：官方写共识层负责为数据可用持久化 blob，执行层不负责；付费不是永存。**
- **看见付费不是已经更安全。**
- **看见本页不是已经是不变量 101。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经永存 | 不是已经永存 | 不是已经气≠墙钟（101） |
| 已经更安全 | 不是已经更安全 | 不是已经策略≠共识（144） |
| 已经是不变量 101 | 不是已经是不变量 101 | 不是已经1491 blgas-notexec |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-4844 blob-fee-paid not already perpetual / not already safer / not already 101 正式三事（145 余量），必须分开是不是已经永存、是不是已经更安全、是不是已经是不变量 101。可以跳过「都叫 gas 就已经是同一本账」。不要另写 怎样扣 sidecar。145 blob-fee vs gas bundled unbundling 在本页 item 3 完成；本页收束本批。下一份仍捆着的以太坊官方对象：blob-schedule（200）。

## 本页不抄

- 每块上限、目标、GAS_PER_BLOB、兆字节、官网 rollup 倍数。
- 怎样扣 sidecar。
