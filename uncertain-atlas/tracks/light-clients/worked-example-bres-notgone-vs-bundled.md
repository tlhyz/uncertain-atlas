# 例：看见执行费主导不是已经没有blob价不是已经没有blob价；看见execution-cost dominance is not already a missing blob price不是已经是不变量 158；看见执行费主导不是已经没有blob价不是已经是不变量 197

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-7918](https://eips.ethereum.org/EIPS/eip-7918)（Blob base fee bounded by execution cost）。  
**对应课文**：[L5.4](../../courses/level-05-ethereum/L05-M04-state-blobs-mev.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-7918 exec-dominant not already blob-priceless / not already 158 / not already 197 正式三事（201 余量）/ not 1498 bres-notgone interchangeable / not 201 blob-reserve-vs-execution bundled interchangeable」，不是 blob reserve vs execution bundled（201），也不是已经 基础费≠小费（158），也不是已经 calldata地板≠执行气（197）。不要另写 怎样等下限灌 blob、怎样绕过底价。

## 官方三件事

1. **看见执行费主导不是已经没有blob价 / 看见执行费主导不是已经没有blob价 这份对象 is not already 已经没有blob价 interchangeable，也不是已经 blob reserve vs execution bundled（201） interchangeable / 1498 bres-notgone interchangeable / 1497 bres-notacct interchangeable，也不是已经 EIP-7918 exec-dominant not already blob-priceless / not already 158 / not already 197 正式三事 bundled（201 item 2 余量） interchangeable / 201 bres item 2 interchangeable。**  
   官方把执行费主导不是已经没有blob价和已经没有blob价写成两件。看见执行费主导不是已经没有blob价，不是已经没有blob价。

2. **看见execution-cost dominance is not already a missing blob price / 看见执行费主导不是已经没有blob价 / 这份对象 is not already 已经是不变量 158 interchangeable，也不是已经 blob reserve vs execution bundled（201） interchangeable / 1498 bres-notgone interchangeable / 1499 bres-notsch interchangeable，也不是已经 基础费≠小费 interchangeable / 158 基础费≠小费 interchangeable。**  
   官方把execution-cost dominance is not already a missing blob price和已经是不变量 158写成两件。看见execution-cost dominance is not already a missing blob price，不是已经是不变量 158。

3. **看见执行费主导不是已经没有blob价 / 看见execution-cost dominance is not already a missing blob price / 这份对象 is not already 已经是不变量 197 interchangeable，也不是已经 blob reserve vs execution bundled（201） interchangeable / 1498 bres-notgone interchangeable / 1497 bres-notacct interchangeable，也不是已经 calldata地板≠执行气 interchangeable / 197 calldata地板≠执行气 interchangeable。**  
   官方把执行费主导不是已经没有blob价和已经是不变量 197写成两件。看见执行费主导不是已经没有blob价，不是已经是不变量 197。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样等下限灌 blob、怎样绕过底价。

## 官方为什么这样拆

- **执行费主导不是已经没有blob价 interchangeable：官方写价信号暂时看不见，blob 基础费还在。**
- **看见本页不是已经是不变量 158。**
- **看见本页不是已经是不变量 197。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经没有blob价 | 不是已经没有blob价 | 不是已经基础费≠小费（158） |
| 已经是不变量 158 | 不是已经是不变量 158 | 不是已经calldata地板≠执行气（197） |
| 已经是不变量 197 | 不是已经是不变量 197 | 不是已经1497 bres-notacct |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7918 exec-dominant not already blob-priceless / not already 158 / not already 197 正式三事（201 余量），必须分开是不是已经没有blob价、是不是已经是不变量 158、是不是已经是不变量 197。可以跳过「看见 7918 就已经并了两套气」。不要另写 怎样等下限灌 blob、怎样绕过底价。201 blob-reserve vs execution bundled unbundling 在本页 item 2 续；续 [`worked-example-bres-notsch-vs-bundled.md`](worked-example-bres-notsch-vs-bundled.md)（不变量 1499 item 3）。

## 本页不抄

- 底价常数、气种比、规范下限取值、百分比、点评估气价。
- 怎样等下限灌 blob、怎样绕过底价。
