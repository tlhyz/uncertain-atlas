# 例：看见抬高blob目标上限不是已经改了两套气的拆分不是已经改了两套气的拆分；看见raising the blob schedule is not already a gas-split change不是已经是不变量 145；看见抬高blob目标上限不是已经改了两套气的拆分不是已经 200 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-7691](https://eips.ethereum.org/EIPS/eip-7691)（Blob throughput increase）。  
**对应课文**：[L5.4](../../courses/level-05-ethereum/L05-M04-state-blobs-mev.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-7691 raise-schedule not already gas-split-changed / not already 145 / not already 200-bundled 正式三事（200 余量）/ not 1494 bsch-notgas interchangeable / not 200 blob-schedule-vs-4844 bundled interchangeable」，不是 blob schedule vs 4844 bundled（200），也不是已经 blob气≠执行气（145），也不是已经 KZG≠DAS（23）。不要另写 怎样灌满 blob、怎样空块压费、怎样给本地出块加旗标。

## 官方三件事

1. **看见抬高blob目标上限不是已经改了两套气的拆分 / 看见抬高blob目标上限不是已经改了两套气的拆分 这份对象 is not already 已经改了两套气的拆分 interchangeable，也不是已经 blob schedule vs 4844 bundled（200） interchangeable / 1494 bsch-notgas interchangeable / 1495 bsch-notratio interchangeable，也不是已经 EIP-7691 raise-schedule not already gas-split-changed / not already 145 / not already 200-bundled 正式三事 bundled（200 item 1 余量） interchangeable / 200 bsch item 1 interchangeable。**  
   官方把抬高blob目标上限不是已经改了两套气的拆分和已经改了两套气的拆分写成两件。看见抬高blob目标上限不是已经改了两套气的拆分，不是已经改了两套气的拆分。

2. **看见raising the blob schedule is not already a gas-split change / 看见抬高blob目标上限不是已经改了两套气的拆分 / 这份对象 is not already 已经是不变量 145 interchangeable，也不是已经 blob schedule vs 4844 bundled（200） interchangeable / 1494 bsch-notgas interchangeable / 1496 bsch-notel interchangeable，也不是已经 blob气≠执行气 interchangeable / 145 blob气≠执行气 interchangeable。**  
   官方把raising the blob schedule is not already a gas-split change和已经是不变量 145写成两件。看见raising the blob schedule is not already a gas-split change，不是已经是不变量 145。

3. **看见抬高blob目标上限不是已经改了两套气的拆分 / 看见raising the blob schedule is not already a gas-split change / 这份对象 is not already 已经 200 bundled interchangeable，也不是已经 blob schedule vs 4844 bundled（200） interchangeable / 1494 bsch-notgas interchangeable / 1495 bsch-notratio interchangeable，也不是已经 KZG≠DAS interchangeable / 23 KZG≠DAS interchangeable。**  
   官方把抬高blob目标上限不是已经改了两套气的拆分和已经 200 bundled写成两件。看见抬高blob目标上限不是已经改了两套气的拆分，不是已经 200 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样灌满 blob、怎样空块压费、怎样给本地出块加旗标。

## 官方为什么这样拆

- **抬高blob目标上限不是已经改了两套气的拆分 interchangeable：官方写本页是短期吞吐提升，不是已经改了 blob 气与执行气的拆分。**
- **看见本页不是已经是不变量 145。**
- **看见读数旋钮不是已经 200 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经改了两套气的拆分 | 不是已经改了两套气的拆分 | 不是已经blob气≠执行气（145） |
| 已经是不变量 145 | 不是已经是不变量 145 | 不是已经KZG≠DAS（23） |
| 已经 200 bundled | 不是已经 200 bundled | 不是已经1495 bsch-notratio |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7691 raise-schedule not already gas-split-changed / not already 145 / not already 200-bundled 正式三事（200 余量），必须分开是不是已经改了两套气的拆分、是不是已经是不变量 145、是不是已经 200 bundled。可以跳过「看见 7691 就已经上了 DAS」。不要另写 怎样灌满 blob、怎样空块压费、怎样给本地出块加旗标。200 blob-schedule vs 4844 bundled unbundling 在本页 item 1 启动；续 [`worked-example-bsch-notratio-vs-bundled.md`](worked-example-bsch-notratio-vs-bundled.md)（不变量 1495 item 2）。

## 本页不抄

- 目标条数、上限条数、blob 气上限、调价分母、百分比。
- 怎样灌满 blob、怎样空块压费、怎样给本地出块加旗标。
