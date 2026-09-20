# 例：看见blob gas不是普通执行gas不是已经是普通执行gas；看见blob gas is not already ordinary execution gas不是已经是不变量 23；看见blob gas不是普通执行gas不是已经 145 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-4844](https://eips.ethereum.org/EIPS/eip-4844)（Shard Blob Transactions）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-4844 blob-gas not already execution-gas / not already 23 / not already 145-bundled 正式三事（145 余量）/ not 1491 blgas-notexec interchangeable / not 145 blob-fee-vs-gas bundled interchangeable」，不是 blob fee vs gas bundled（145），也不是已经 短时承诺≠永存DA（23），也不是已经 抬高日程≠已改气种（200）。不要另写 怎样扣 sidecar。

## 官方三件事

1. **看见blob gas不是普通执行gas / 看见blob gas不是普通执行gas 这份对象 is not already 已经是普通执行gas interchangeable，也不是已经 blob fee vs gas bundled（145） interchangeable / 1491 blgas-notexec interchangeable / 1492 blgas-notbyte interchangeable，也不是已经 EIP-4844 blob-gas not already execution-gas / not already 23 / not already 145-bundled 正式三事 bundled（145 item 1 余量） interchangeable / 145 blgas item 1 interchangeable。**  
   官方把blob gas不是普通执行gas和已经是普通执行gas写成两件。看见blob gas不是普通执行gas，不是已经是普通执行gas。

2. **看见blob gas is not already ordinary execution gas / 看见blob gas不是普通执行gas / 这份对象 is not already 已经是不变量 23 interchangeable，也不是已经 blob fee vs gas bundled（145） interchangeable / 1491 blgas-notexec interchangeable / 1493 blgas-notperm interchangeable，也不是已经 短时承诺≠永存DA interchangeable / 23 短时承诺≠永存DA interchangeable。**  
   官方把blob gas is not already ordinary execution gas和已经是不变量 23写成两件。看见blob gas is not already ordinary execution gas，不是已经是不变量 23。

3. **看见blob gas不是普通执行gas / 看见blob gas is not already ordinary execution gas / 这份对象 is not already 已经 145 bundled interchangeable，也不是已经 blob fee vs gas bundled（145） interchangeable / 1491 blgas-notexec interchangeable / 1492 blgas-notbyte interchangeable，也不是已经 抬高日程≠已改气种 interchangeable / 200 抬高日程≠已改气种 interchangeable。**  
   官方把blob gas不是普通执行gas和已经 145 bundled写成两件。看见blob gas不是普通执行gas，不是已经 145 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样扣 sidecar。

## 官方为什么这样拆

- **blob gas不是普通执行gas interchangeable：官方写它是新的气种，独立于普通 gas，目前只有 blob 按 blob gas 计价。**
- **看见本页不是已经是不变量 23。**
- **看见读数旋钮不是已经 145 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是普通执行gas | 不是已经是普通执行gas | 不是已经短时承诺≠永存DA（23） |
| 已经是不变量 23 | 不是已经是不变量 23 | 不是已经抬高日程≠已改气种（200） |
| 已经 145 bundled | 不是已经 145 bundled | 不是已经1492 blgas-notbyte |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-4844 blob-gas not already execution-gas / not already 23 / not already 145-bundled 正式三事（145 余量），必须分开是不是已经是普通执行gas、是不是已经是不变量 23、是不是已经 145 bundled。可以跳过「都叫 gas 就已经是同一本账」。不要另写 怎样扣 sidecar。145 blob-fee vs gas bundled unbundling 在本页 item 1 启动；续 [`worked-example-blgas-notbyte-vs-bundled.md`](worked-example-blgas-notbyte-vs-bundled.md)（不变量 1492 item 2）。

## 本页不抄

- 每块上限、目标、GAS_PER_BLOB、兆字节、官网 rollup 倍数。
- 怎样扣 sidecar。
