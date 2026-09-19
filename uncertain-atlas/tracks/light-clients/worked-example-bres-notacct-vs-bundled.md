# 例：看见blob底价不是已经并成一套气不是已经并成一套气；看见a blob reserve floor is not already a merged gas ledger不是已经是不变量 145；看见blob底价不是已经并成一套气不是已经 201 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-7918](https://eips.ethereum.org/EIPS/eip-7918)（Blob base fee bounded by execution cost）。  
**对应课文**：[L5.4](../../courses/level-05-ethereum/L05-M04-state-blobs-mev.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-7918 reserve-floor not already gas-merged / not already 145 / not already 201-bundled 正式三事（201 余量）/ not 1497 bres-notacct interchangeable / not 201 blob-reserve-vs-execution bundled interchangeable」，不是 blob reserve vs execution bundled（201），也不是已经 blob气≠执行气（145），也不是已经 抬高日程≠已改气种（200）。不要另写 怎样等下限灌 blob、怎样绕过底价。

## 官方三件事

1. **看见blob底价不是已经并成一套气 / 看见blob底价不是已经并成一套气 这份对象 is not already 已经并成一套气 interchangeable，也不是已经 blob reserve vs execution bundled（201） interchangeable / 1497 bres-notacct interchangeable / 1498 bres-notgone interchangeable，也不是已经 EIP-7918 reserve-floor not already gas-merged / not already 145 / not already 201-bundled 正式三事 bundled（201 item 1 余量） interchangeable / 201 bres item 1 interchangeable。**  
   官方把blob底价不是已经并成一套气和已经并成一套气写成两件。看见blob底价不是已经并成一套气，不是已经并成一套气。

2. **看见a blob reserve floor is not already a merged gas ledger / 看见blob底价不是已经并成一套气 / 这份对象 is not already 已经是不变量 145 interchangeable，也不是已经 blob reserve vs execution bundled（201） interchangeable / 1497 bres-notacct interchangeable / 1499 bres-notsch interchangeable，也不是已经 blob气≠执行气 interchangeable / 145 blob气≠执行气 interchangeable。**  
   官方把a blob reserve floor is not already a merged gas ledger和已经是不变量 145写成两件。看见a blob reserve floor is not already a merged gas ledger，不是已经是不变量 145。

3. **看见blob底价不是已经并成一套气 / 看见a blob reserve floor is not already a merged gas ledger / 这份对象 is not already 已经 201 bundled interchangeable，也不是已经 blob reserve vs execution bundled（201） interchangeable / 1497 bres-notacct interchangeable / 1498 bres-notgone interchangeable，也不是已经 抬高日程≠已改气种 interchangeable / 200 抬高日程≠已改气种 interchangeable。**  
   官方把blob底价不是已经并成一套气和已经 201 bundled写成两件。看见blob底价不是已经并成一套气，不是已经 201 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样等下限灌 blob、怎样绕过底价。

## 官方为什么这样拆

- **blob底价不是已经并成一套气 interchangeable：官方写本页钩的是两套价的下限，4844 两套气还在。**
- **看见本页不是已经是不变量 145。**
- **看见底价旋钮不是已经 201 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经并成一套气 | 不是已经并成一套气 | 不是已经blob气≠执行气（145） |
| 已经是不变量 145 | 不是已经是不变量 145 | 不是已经抬高日程≠已改气种（200） |
| 已经 201 bundled | 不是已经 201 bundled | 不是已经1498 bres-notgone |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7918 reserve-floor not already gas-merged / not already 145 / not already 201-bundled 正式三事（201 余量），必须分开是不是已经并成一套气、是不是已经是不变量 145、是不是已经 201 bundled。可以跳过「看见 7918 就已经并了两套气」。不要另写 怎样等下限灌 blob、怎样绕过底价。201 blob-reserve vs execution bundled unbundling 在本页 item 1 启动；续 [`worked-example-bres-notgone-vs-bundled.md`](worked-example-bres-notgone-vs-bundled.md)（不变量 1498 item 2）。

## 本页不抄

- 底价常数、气种比、规范下限取值、百分比、点评估气价。
- 怎样等下限灌 blob、怎样绕过底价。
