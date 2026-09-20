# 例：看见新的目标上限比不是已经还是旧的对称调价不是已经还是旧对称；看见the new target-max ratio is not already the old symmetric pricing不是已经是不变量 23；看见新的目标上限比不是已经还是旧的对称调价不是已经是不变量 197

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-7691](https://eips.ethereum.org/EIPS/eip-7691)（Blob throughput increase）。  
**对应课文**：[L5.4](../../courses/level-05-ethereum/L05-M04-state-blobs-mev.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-7691 new-ratio not already old-symmetric / not already 23 / not already 197 正式三事（200 余量）/ not 1495 bsch-notratio interchangeable / not 200 blob-schedule-vs-4844 bundled interchangeable」，不是 blob schedule vs 4844 bundled（200），也不是已经 KZG≠DAS（23），也不是已经 calldata地板≠执行气（197）。不要另写 怎样灌满 blob、怎样空块压费、怎样给本地出块加旗标。

## 官方三件事

1. **看见新的目标上限比不是已经还是旧的对称调价 / 看见新的目标上限比不是已经还是旧的对称调价 这份对象 is not already 已经还是旧对称 interchangeable，也不是已经 blob schedule vs 4844 bundled（200） interchangeable / 1495 bsch-notratio interchangeable / 1494 bsch-notgas interchangeable，也不是已经 EIP-7691 new-ratio not already old-symmetric / not already 23 / not already 197 正式三事 bundled（200 item 2 余量） interchangeable / 200 bsch item 2 interchangeable。**  
   官方把新的目标上限比不是已经还是旧的对称调价和已经还是旧对称写成两件。看见新的目标上限比不是已经还是旧的对称调价，不是已经还是旧对称。

2. **看见the new target-max ratio is not already the old symmetric pricing / 看见新的目标上限比不是已经还是旧的对称调价 / 这份对象 is not already 已经是不变量 23 interchangeable，也不是已经 blob schedule vs 4844 bundled（200） interchangeable / 1495 bsch-notratio interchangeable / 1496 bsch-notel interchangeable，也不是已经 KZG≠DAS interchangeable / 23 KZG≠DAS interchangeable。**  
   官方把the new target-max ratio is not already the old symmetric pricing和已经是不变量 23写成两件。看见the new target-max ratio is not already the old symmetric pricing，不是已经是不变量 23。

3. **看见新的目标上限比不是已经还是旧的对称调价 / 看见the new target-max ratio is not already the old symmetric pricing / 这份对象 is not already 已经是不变量 197 interchangeable，也不是已经 blob schedule vs 4844 bundled（200） interchangeable / 1495 bsch-notratio interchangeable / 1494 bsch-notgas interchangeable，也不是已经 calldata地板≠执行气 interchangeable / 197 calldata地板≠执行气 interchangeable。**  
   官方把新的目标上限比不是已经还是旧的对称调价和已经是不变量 197写成两件。看见新的目标上限比不是已经还是旧的对称调价，不是已经是不变量 197。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样灌满 blob、怎样空块压费、怎样给本地出块加旗标。

## 官方为什么这样拆

- **新的目标上限比不是已经还是旧的对称调价 interchangeable：官方写本页打破对称，空段更敏感，不是已经还是旧对称。**
- **看见本页不是已经是不变量 23。**
- **看见本页不是已经是不变量 197。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经还是旧对称 | 不是已经还是旧对称 | 不是已经KZG≠DAS（23） |
| 已经是不变量 23 | 不是已经是不变量 23 | 不是已经calldata地板≠执行气（197） |
| 已经是不变量 197 | 不是已经是不变量 197 | 不是已经1494 bsch-notgas |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7691 new-ratio not already old-symmetric / not already 23 / not already 197 正式三事（200 余量），必须分开是不是已经还是旧对称、是不是已经是不变量 23、是不是已经是不变量 197。可以跳过「看见 7691 就已经上了 DAS」。不要另写 怎样灌满 blob、怎样空块压费、怎样给本地出块加旗标。200 blob-schedule vs 4844 bundled unbundling 在本页 item 2 续；续 [`worked-example-bsch-notel-vs-bundled.md`](worked-example-bsch-notel-vs-bundled.md)（不变量 1496 item 3）。

## 本页不抄

- 目标条数、上限条数、blob 气上限、调价分母、百分比。
- 怎样灌满 blob、怎样空块压费、怎样给本地出块加旗标。
