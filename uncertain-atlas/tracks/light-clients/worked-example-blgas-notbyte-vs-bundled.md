# 例：看见EVM能访问承诺不是已经读到blob字节不是已经读到blob字节；看见EVM can read the commitment is not already sidecar bytes不是已经是不变量 197；看见EVM能访问承诺不是已经读到blob字节不是已经是不变量 201

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-4844](https://eips.ethereum.org/EIPS/eip-4844)（Shard Blob Transactions）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-4844 blobhash not already sidecar-bytes / not already 197 / not already 201 正式三事（145 余量）/ not 1492 blgas-notbyte interchangeable / not 145 blob-fee-vs-gas bundled interchangeable」，不是 blob fee vs gas bundled（145），也不是已经 calldata地板≠执行气（197），也不是已经 blob底价≠已并账（201）。不要另写 怎样扣 sidecar。

## 官方三件事

1. **看见EVM能访问承诺不是已经读到blob字节 / 看见EVM能访问承诺不是已经读到blob字节 这份对象 is not already 已经读到blob字节 interchangeable，也不是已经 blob fee vs gas bundled（145） interchangeable / 1492 blgas-notbyte interchangeable / 1491 blgas-notexec interchangeable，也不是已经 EIP-4844 blobhash not already sidecar-bytes / not already 197 / not already 201 正式三事 bundled（145 item 2 余量） interchangeable / 145 blgas item 2 interchangeable。**  
   官方把EVM能访问承诺不是已经读到blob字节和已经读到blob字节写成两件。看见EVM能访问承诺不是已经读到blob字节，不是已经读到blob字节。

2. **看见EVM can read the commitment is not already sidecar bytes / 看见EVM能访问承诺不是已经读到blob字节 / 这份对象 is not already 已经是不变量 197 interchangeable，也不是已经 blob fee vs gas bundled（145） interchangeable / 1492 blgas-notbyte interchangeable / 1493 blgas-notperm interchangeable，也不是已经 calldata地板≠执行气 interchangeable / 197 calldata地板≠执行气 interchangeable。**  
   官方把EVM can read the commitment is not already sidecar bytes和已经是不变量 197写成两件。看见EVM can read the commitment is not already sidecar bytes，不是已经是不变量 197。

3. **看见EVM能访问承诺不是已经读到blob字节 / 看见EVM can read the commitment is not already sidecar bytes / 这份对象 is not already 已经是不变量 201 interchangeable，也不是已经 blob fee vs gas bundled（145） interchangeable / 1492 blgas-notbyte interchangeable / 1491 blgas-notexec interchangeable，也不是已经 blob底价≠已并账 interchangeable / 201 blob底价≠已并账 interchangeable。**  
   官方把EVM能访问承诺不是已经读到blob字节和已经是不变量 201写成两件。看见EVM能访问承诺不是已经读到blob字节，不是已经是不变量 201。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样扣 sidecar。

## 官方为什么这样拆

- **EVM能访问承诺不是已经读到blob字节 interchangeable：官方写 EVM 执行不能访问这些数据，但能访问其承诺；BLOBHASH 吐出的是 versioned hash。**
- **看见本页不是已经是不变量 197。**
- **看见本页不是已经是不变量 201。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经读到blob字节 | 不是已经读到blob字节 | 不是已经calldata地板≠执行气（197） |
| 已经是不变量 197 | 不是已经是不变量 197 | 不是已经blob底价≠已并账（201） |
| 已经是不变量 201 | 不是已经是不变量 201 | 不是已经1491 blgas-notexec |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-4844 blobhash not already sidecar-bytes / not already 197 / not already 201 正式三事（145 余量），必须分开是不是已经读到blob字节、是不是已经是不变量 197、是不是已经是不变量 201。可以跳过「都叫 gas 就已经是同一本账」。不要另写 怎样扣 sidecar。145 blob-fee vs gas bundled unbundling 在本页 item 2 续；续 [`worked-example-blgas-notperm-vs-bundled.md`](worked-example-blgas-notperm-vs-bundled.md)（不变量 1493 item 3）。

## 本页不抄

- 每块上限、目标、GAS_PER_BLOB、兆字节、官网 rollup 倍数。
- 怎样扣 sidecar。
