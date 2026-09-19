# 例：看见预留地板气限不是已经烧到地板不是已经烧到地板；看见reserved floor gasLimit is not already burned to the floor不是已经更安全；看见预留地板气限不是已经烧到地板不是已经是不变量 101

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-7623](https://eips.ethereum.org/EIPS/eip-7623)（Increase calldata cost）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-7623 reserve-floor not already burned / not already safer / not already 101 正式三事（197 余量）/ not 1469 cflr-notburn interchangeable / not 197 calldata-floor-vs-execution bundled interchangeable」，不是 calldata floor vs execution bundled（197），也不是已经 initcode≠runtime（176），也不是已经 气≠墙钟（101）。不要另写 怎样堆零字节载荷、怎样停在阈值下走便宜 calldata、怎样把数据交易和计算交易捆在一起躲开地板。

## 官方三件事

1. **看见预留地板气限不是已经烧到地板 / 看见预留地板气限不是已经烧到地板 这份对象 is not already 已经烧到地板 interchangeable，也不是已经 calldata floor vs execution bundled（197） interchangeable / 1469 cflr-notburn interchangeable / 1467 cflr-notexec interchangeable，也不是已经 EIP-7623 reserve-floor not already burned / not already safer / not already 101 正式三事 bundled（197 item 3 余量） interchangeable / 197 cflr item 3 interchangeable。**  
   官方把预留地板气限不是已经烧到地板和已经烧到地板写成两件。看见预留地板气限不是已经烧到地板，不是已经烧到地板。

2. **看见reserved floor gasLimit is not already burned to the floor / 看见预留地板气限不是已经烧到地板 / 这份对象 is not already 已经更安全 interchangeable，也不是已经 calldata floor vs execution bundled（197） interchangeable / 1469 cflr-notburn interchangeable / 1468 cflr-notxfer interchangeable，也不是已经 initcode≠runtime interchangeable / 176 initcode≠runtime interchangeable。**  
   官方把reserved floor gasLimit is not already burned to the floor和已经更安全写成两件。看见reserved floor gasLimit is not already burned to the floor，不是已经更安全。

3. **看见预留地板气限不是已经烧到地板 / 看见reserved floor gasLimit is not already burned to the floor / 这份对象 is not already 已经是不变量 101 interchangeable，也不是已经 calldata floor vs execution bundled（197） interchangeable / 1469 cflr-notburn interchangeable / 1467 cflr-notexec interchangeable，也不是已经 气≠墙钟 interchangeable / 101 气≠墙钟 interchangeable。**  
   官方把预留地板气限不是已经烧到地板和已经是不变量 101写成两件。看见预留地板气限不是已经烧到地板，不是已经是不变量 101。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样堆零字节载荷、怎样停在阈值下走便宜 calldata、怎样把数据交易和计算交易捆在一起躲开地板。

## 官方为什么这样拆

- **预留地板气限不是已经烧到地板 interchangeable：官方写气限必须预留，实际 gasUsed 可以低于地板。**
- **看见预留不是已经更安全。**
- **看见本页不是已经是不变量 101。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经烧到地板 | 不是已经烧到地板 | 不是已经initcode≠runtime（176） |
| 已经更安全 | 不是已经更安全 | 不是已经气≠墙钟（101） |
| 已经是不变量 101 | 不是已经是不变量 101 | 不是已经1467 cflr-notexec |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7623 reserve-floor not already burned / not already safer / not already 101 正式三事（197 余量），必须分开是不是已经烧到地板、是不是已经更安全、是不是已经是不变量 101。可以跳过「看见地板就已经改了执行气」。不要另写 怎样堆零字节载荷、怎样停在阈值下走便宜 calldata、怎样把数据交易和计算交易捆在一起躲开地板。197 calldata-floor vs execution bundled unbundling 在本页 item 3 完成；本页收束本批。下一份仍捆着的以太坊官方对象：clz（208）。

## 本页不抄

- 标准 token 成本、地板每 token、旧最大载荷、平均块、气限除以旧非零字节成本。
- 怎样堆零字节载荷、怎样停在阈值下走便宜 calldata、怎样把数据交易和计算交易捆在一起躲开地板。
