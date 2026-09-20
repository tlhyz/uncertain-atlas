# 例：看见子孙继承信号不是自己已经明示加入不是已经明示加入；看见an inherited replace signal is not already an explicit opt-in不是已经是不变量 144；看见子孙继承信号不是自己已经明示加入不是已经是不变量 165

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-125](https://github.com/bitcoin/bips/blob/master/bip-0125.mediawiki)（Opt-in Full Replace-by-Fee Signaling）。  
**对应课文**：[L3.2](../../courses/level-03-bitcoin/L03-M02-fees-and-standardness.md)。  
**不要写进**：`index/03` 共识行、M3.2、L3.2。本页是「BIP-125 inherited-signal not already explicit-join / not already 144 / not already 165 正式三事（166 余量）/ not 1526 rbfs-notjoin interchangeable / not 166 rbf-signal-vs-replaced bundled interchangeable」，不是 rbf signal vs replaced bundled（166），也不是已经 策略≠共识（144），也不是已经 CSV≠绝对锁（165）。不要另写 怎样构造替换、怎样钉死、怎样挤掉商家看见的那笔。

## 官方三件事

1. **看见子孙继承信号不是自己已经明示加入 / 看见子孙继承信号不是自己已经明示加入 这份对象 is not already 已经明示加入 interchangeable，也不是已经 rbf signal vs replaced bundled（166） interchangeable / 1526 rbfs-notjoin interchangeable / 1524 rbfs-notrep interchangeable，也不是已经 BIP-125 inherited-signal not already explicit-join / not already 144 / not already 165 正式三事 bundled（166 item 3 余量） interchangeable / 166 rbfs item 3 interchangeable。**  
   官方把子孙继承信号不是自己已经明示加入和已经明示加入写成两件。看见子孙继承信号不是自己已经明示加入，不是已经明示加入。

2. **看见an inherited replace signal is not already an explicit opt-in / 看见子孙继承信号不是自己已经明示加入 / 这份对象 is not already 已经是不变量 144 interchangeable，也不是已经 rbf signal vs replaced bundled（166） interchangeable / 1526 rbfs-notjoin interchangeable / 1525 rbfs-notlock interchangeable，也不是已经 策略≠共识 interchangeable / 144 策略≠共识 interchangeable。**  
   官方把an inherited replace signal is not already an explicit opt-in和已经是不变量 144写成两件。看见an inherited replace signal is not already an explicit opt-in，不是已经是不变量 144。

3. **看见子孙继承信号不是自己已经明示加入 / 看见an inherited replace signal is not already an explicit opt-in / 这份对象 is not already 已经是不变量 165 interchangeable，也不是已经 rbf signal vs replaced bundled（166） interchangeable / 1526 rbfs-notjoin interchangeable / 1524 rbfs-notrep interchangeable，也不是已经 CSV≠绝对锁 interchangeable / 165 CSV≠绝对锁 interchangeable。**  
   官方把子孙继承信号不是自己已经明示加入和已经是不变量 165写成两件。看见子孙继承信号不是自己已经明示加入，不是已经是不变量 165。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样构造替换、怎样钉死、怎样挤掉商家看见的那笔。

## 官方为什么这样拆

- **子孙继承信号不是自己已经明示加入 interchangeable：官方写祖先未确认且示意了，子孙在本策略下可替换，不是自己已经明示。**
- **看见本页不是已经是不变量 144。**
- **看见本页不是已经是不变量 165。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经明示加入 | 不是已经明示加入 | 不是已经策略≠共识（144） |
| 已经是不变量 144 | 不是已经是不变量 144 | 不是已经CSV≠绝对锁（165） |
| 已经是不变量 165 | 不是已经是不变量 165 | 不是已经1524 rbfs-notrep |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-125 inherited-signal not already explicit-join / not already 144 / not already 165 正式三事（166 余量），必须分开是不是已经明示加入、是不是已经是不变量 144、是不是已经是不变量 165。可以跳过「看见带了 RBF 就已经换掉」。不要另写 怎样构造替换、怎样钉死、怎样挤掉商家看见的那笔。166 rbf-signal vs replaced bundled unbundling 在本页 item 3 完成；本页收束本批。下一份仍捆着的官方对象：csv-vs-cltv（165）。

## 本页不抄

- 终值常数、替换条数、最低中继费率例子。
- 怎样构造替换、怎样钉死、怎样挤掉商家看见的那笔。
