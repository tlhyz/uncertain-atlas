# 例：看见calldata地板不是已经改了执行气不是已经改了执行气；看见calldata floor is not already execution-gas changed不是已经是不变量 145；看见calldata地板不是已经改了执行气不是已经 197 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-7623](https://eips.ethereum.org/EIPS/eip-7623)（Increase calldata cost）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-7623 calldata-floor not already execution-gas / not already 145 / not already 197-bundled 正式三事（197 余量）/ not 1467 cflr-notexec interchangeable / not 197 calldata-floor-vs-execution bundled interchangeable」，不是 calldata floor vs execution bundled（197），也不是已经 blob气≠执行气（145），也不是已经 RLP编码硬帽≠已改气限（202）。不要另写 怎样堆零字节载荷、怎样停在阈值下走便宜 calldata、怎样把数据交易和计算交易捆在一起躲开地板。

## 官方三件事

1. **看见calldata地板不是已经改了执行气 / 看见calldata地板不是已经改了执行气 这份对象 is not already 已经改了执行气 interchangeable，也不是已经 calldata floor vs execution bundled（197） interchangeable / 1467 cflr-notexec interchangeable / 1468 cflr-notxfer interchangeable，也不是已经 EIP-7623 calldata-floor not already execution-gas / not already 145 / not already 197-bundled 正式三事 bundled（197 item 1 余量） interchangeable / 197 cflr item 1 interchangeable。**  
   官方把calldata地板不是已经改了执行气和已经改了执行气写成两件。看见calldata地板不是已经改了执行气，不是已经改了执行气。

2. **看见calldata floor is not already execution-gas changed / 看见calldata地板不是已经改了执行气 / 这份对象 is not already 已经是不变量 145 interchangeable，也不是已经 calldata floor vs execution bundled（197） interchangeable / 1467 cflr-notexec interchangeable / 1469 cflr-notburn interchangeable，也不是已经 blob气≠执行气 interchangeable / 145 blob气≠执行气 interchangeable。**  
   官方把calldata floor is not already execution-gas changed和已经是不变量 145写成两件。看见calldata floor is not already execution-gas changed，不是已经是不变量 145。

3. **看见calldata地板不是已经改了执行气 / 看见calldata floor is not already execution-gas changed / 这份对象 is not already 已经 197 bundled interchangeable，也不是已经 calldata floor vs execution bundled（197） interchangeable / 1467 cflr-notexec interchangeable / 1468 cflr-notxfer interchangeable，也不是已经 RLP编码硬帽≠已改气限 interchangeable / 202 RLP编码硬帽≠已改气限 interchangeable。**  
   官方把calldata地板不是已经改了执行气和已经 197 bundled写成两件。看见calldata地板不是已经改了执行气，不是已经 197 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样堆零字节载荷、怎样停在阈值下走便宜 calldata、怎样把数据交易和计算交易捆在一起躲开地板。

## 官方为什么这样拆

- **calldata地板不是已经改了执行气 interchangeable：官方写地板是数据为主交易取较大值，不是普通执行气已经改了。**
- **看见本页不是已经是不变量 145。**
- **看见读数旋钮不是已经 197 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经改了执行气 | 不是已经改了执行气 | 不是已经blob气≠执行气（145） |
| 已经是不变量 145 | 不是已经是不变量 145 | 不是已经RLP编码硬帽≠已改气限（202） |
| 已经 197 bundled | 不是已经 197 bundled | 不是已经1468 cflr-notxfer |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7623 calldata-floor not already execution-gas / not already 145 / not already 197-bundled 正式三事（197 余量），必须分开是不是已经改了执行气、是不是已经是不变量 145、是不是已经 197 bundled。可以跳过「看见地板就已经改了执行气」。不要另写 怎样堆零字节载荷、怎样停在阈值下走便宜 calldata、怎样把数据交易和计算交易捆在一起躲开地板。197 calldata-floor vs execution bundled unbundling 在本页 item 1 启动；续 [`worked-example-cflr-notxfer-vs-bundled.md`](worked-example-cflr-notxfer-vs-bundled.md)（不变量 1468 item 2）。

## 本页不抄

- 标准 token 成本、地板每 token、旧最大载荷、平均块、气限除以旧非零字节成本。
- 怎样堆零字节载荷、怎样停在阈值下走便宜 calldata、怎样把数据交易和计算交易捆在一起躲开地板。
