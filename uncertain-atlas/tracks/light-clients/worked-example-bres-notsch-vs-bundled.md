# 例：看见不算目标不是已经改了日程数字不是已经改了日程数字；看见not subtracting the target is not already a schedule change不是已经是不变量 200；看见不算目标不是已经改了日程数字不是已经是不变量 23

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-7918](https://eips.ethereum.org/EIPS/eip-7918)（Blob base fee bounded by execution cost）。  
**对应课文**：[L5.4](../../courses/level-05-ethereum/L05-M04-state-blobs-mev.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-7918 no-subtract-target not already schedule-changed / not already 200 / not already 23 正式三事（201 余量）/ not 1499 bres-notsch interchangeable / not 201 blob-reserve-vs-execution bundled interchangeable」，不是 blob reserve vs execution bundled（201），也不是已经 抬高日程≠已改气种（200），也不是已经 KZG≠DAS（23）。不要另写 怎样等下限灌 blob、怎样绕过底价。

## 官方三件事

1. **看见不算目标不是已经改了日程数字 / 看见不算目标不是已经改了日程数字 这份对象 is not already 已经改了日程数字 interchangeable，也不是已经 blob reserve vs execution bundled（201） interchangeable / 1499 bres-notsch interchangeable / 1497 bres-notacct interchangeable，也不是已经 EIP-7918 no-subtract-target not already schedule-changed / not already 200 / not already 23 正式三事 bundled（201 item 3 余量） interchangeable / 201 bres item 3 interchangeable。**  
   官方把不算目标不是已经改了日程数字和已经改了日程数字写成两件。看见不算目标不是已经改了日程数字，不是已经改了日程数字。

2. **看见not subtracting the target is not already a schedule change / 看见不算目标不是已经改了日程数字 / 这份对象 is not already 已经是不变量 200 interchangeable，也不是已经 blob reserve vs execution bundled（201） interchangeable / 1499 bres-notsch interchangeable / 1498 bres-notgone interchangeable，也不是已经 抬高日程≠已改气种 interchangeable / 200 抬高日程≠已改气种 interchangeable。**  
   官方把not subtracting the target is not already a schedule change和已经是不变量 200写成两件。看见not subtracting the target is not already a schedule change，不是已经是不变量 200。

3. **看见不算目标不是已经改了日程数字 / 看见not subtracting the target is not already a schedule change / 这份对象 is not already 已经是不变量 23 interchangeable，也不是已经 blob reserve vs execution bundled（201） interchangeable / 1499 bres-notsch interchangeable / 1497 bres-notacct interchangeable，也不是已经 KZG≠DAS interchangeable / 23 KZG≠DAS interchangeable。**  
   官方把不算目标不是已经改了日程数字和已经是不变量 23写成两件。看见不算目标不是已经改了日程数字，不是已经是不变量 23。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样等下限灌 blob、怎样绕过底价。

## 官方为什么这样拆

- **不算目标不是已经改了日程数字 interchangeable：官方写超额更新规则，目标/上限数字没改。**
- **看见本页不是已经是不变量 200。**
- **看见本页不是已经是不变量 23。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经改了日程数字 | 不是已经改了日程数字 | 不是已经抬高日程≠已改气种（200） |
| 已经是不变量 200 | 不是已经是不变量 200 | 不是已经KZG≠DAS（23） |
| 已经是不变量 23 | 不是已经是不变量 23 | 不是已经1497 bres-notacct |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7918 no-subtract-target not already schedule-changed / not already 200 / not already 23 正式三事（201 余量），必须分开是不是已经改了日程数字、是不是已经是不变量 200、是不是已经是不变量 23。可以跳过「看见 7918 就已经并了两套气」。不要另写 怎样等下限灌 blob、怎样绕过底价。201 blob-reserve vs execution bundled unbundling 在本页 item 3 完成；本页收束本批。下一份仍捆着的以太坊官方对象：history-hash（195）。

## 本页不抄

- 底价常数、气种比、规范下限取值、百分比、点评估气价。
- 怎样等下限灌 blob、怎样绕过底价。
