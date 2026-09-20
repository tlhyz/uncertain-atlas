# 例：看见数据为主更贵不是已经让普通转账更贵不是已经让普通转账更贵；看见data-heavy dearer is not already transfer dearer不是已经是不变量 158；看见数据为主更贵不是已经让普通转账更贵不是已经是不变量 226

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-7623](https://eips.ethereum.org/EIPS/eip-7623)（Increase calldata cost）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-7623 data-heavy-dearer not already transfer-dearer / not already 158 / not already 226 正式三事（197 余量）/ not 1468 cflr-notxfer interchangeable / not 197 calldata-floor-vs-execution bundled interchangeable」，不是 calldata floor vs execution bundled（197），也不是已经 基础费≠小费（158），也不是已经 calldata-cut≠已改地板（226）。不要另写 怎样堆零字节载荷、怎样停在阈值下走便宜 calldata、怎样把数据交易和计算交易捆在一起躲开地板。

## 官方三件事

1. **看见数据为主更贵不是已经让普通转账更贵 / 看见数据为主更贵不是已经让普通转账更贵 这份对象 is not already 已经让普通转账更贵 interchangeable，也不是已经 calldata floor vs execution bundled（197） interchangeable / 1468 cflr-notxfer interchangeable / 1467 cflr-notexec interchangeable，也不是已经 EIP-7623 data-heavy-dearer not already transfer-dearer / not already 158 / not already 226 正式三事 bundled（197 item 2 余量） interchangeable / 197 cflr item 2 interchangeable。**  
   官方把数据为主更贵不是已经让普通转账更贵和已经让普通转账更贵写成两件。看见数据为主更贵不是已经让普通转账更贵，不是已经让普通转账更贵。

2. **看见data-heavy dearer is not already transfer dearer / 看见数据为主更贵不是已经让普通转账更贵 / 这份对象 is not already 已经是不变量 158 interchangeable，也不是已经 calldata floor vs execution bundled（197） interchangeable / 1468 cflr-notxfer interchangeable / 1469 cflr-notburn interchangeable，也不是已经 基础费≠小费 interchangeable / 158 基础费≠小费 interchangeable。**  
   官方把data-heavy dearer is not already transfer dearer和已经是不变量 158写成两件。看见data-heavy dearer is not already transfer dearer，不是已经是不变量 158。

3. **看见数据为主更贵不是已经让普通转账更贵 / 看见data-heavy dearer is not already transfer dearer / 这份对象 is not already 已经是不变量 226 interchangeable，也不是已经 calldata floor vs execution bundled（197） interchangeable / 1468 cflr-notxfer interchangeable / 1467 cflr-notexec interchangeable，也不是已经 calldata-cut≠已改地板 interchangeable / 226 calldata-cut≠已改地板 interchangeable。**  
   官方把数据为主更贵不是已经让普通转账更贵和已经是不变量 226写成两件。看见数据为主更贵不是已经让普通转账更贵，不是已经是不变量 226。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样堆零字节载荷、怎样停在阈值下走便宜 calldata、怎样把数据交易和计算交易捆在一起躲开地板。

## 官方为什么这样拆

- **数据为主更贵不是已经让普通转账更贵 interchangeable：官方写不以 calldata 为主的普通用户可以不受影响。**
- **看见本页不是已经是不变量 158。**
- **看见本页不是已经是不变量 226。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经让普通转账更贵 | 不是已经让普通转账更贵 | 不是已经基础费≠小费（158） |
| 已经是不变量 158 | 不是已经是不变量 158 | 不是已经calldata-cut≠已改地板（226） |
| 已经是不变量 226 | 不是已经是不变量 226 | 不是已经1467 cflr-notexec |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7623 data-heavy-dearer not already transfer-dearer / not already 158 / not already 226 正式三事（197 余量），必须分开是不是已经让普通转账更贵、是不是已经是不变量 158、是不是已经是不变量 226。可以跳过「看见地板就已经改了执行气」。不要另写 怎样堆零字节载荷、怎样停在阈值下走便宜 calldata、怎样把数据交易和计算交易捆在一起躲开地板。197 calldata-floor vs execution bundled unbundling 在本页 item 2 续；续 [`worked-example-cflr-notburn-vs-bundled.md`](worked-example-cflr-notburn-vs-bundled.md)（不变量 1469 item 3）。

## 本页不抄

- 标准 token 成本、地板每 token、旧最大载荷、平均块、气限除以旧非零字节成本。
- 怎样堆零字节载荷、怎样停在阈值下走便宜 calldata、怎样把数据交易和计算交易捆在一起躲开地板。
