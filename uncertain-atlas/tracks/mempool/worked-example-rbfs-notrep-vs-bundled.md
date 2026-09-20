# 例：看见选择加入替换信号不是已经换掉不是已经换掉；看见an opt-in replace signal is not already a replacement不是已经是不变量 144；看见选择加入替换信号不是已经换掉不是已经 166 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-125](https://github.com/bitcoin/bips/blob/master/bip-0125.mediawiki)（Opt-in Full Replace-by-Fee Signaling）。  
**对应课文**：[L3.2](../../courses/level-03-bitcoin/L03-M02-fees-and-standardness.md)。  
**不要写进**：`index/03` 共识行、M3.2、L3.2。本页是「BIP-125 opt-in-signal not already replaced / not already 144 / not already 166-bundled 正式三事（166 余量）/ not 1524 rbfs-notrep interchangeable / not 166 rbf-signal-vs-replaced bundled interchangeable」，不是 rbf signal vs replaced bundled（166），也不是已经 策略≠共识（144），也不是已经 CSV≠绝对锁（165）。不要另写 怎样构造替换、怎样钉死、怎样挤掉商家看见的那笔。

## 官方三件事

1. **看见选择加入替换信号不是已经换掉 / 看见选择加入替换信号不是已经换掉 这份对象 is not already 已经换掉 interchangeable，也不是已经 rbf signal vs replaced bundled（166） interchangeable / 1524 rbfs-notrep interchangeable / 1525 rbfs-notlock interchangeable，也不是已经 BIP-125 opt-in-signal not already replaced / not already 144 / not already 166-bundled 正式三事 bundled（166 item 1 余量） interchangeable / 166 rbfs item 1 interchangeable。**  
   官方把选择加入替换信号不是已经换掉和已经换掉写成两件。看见选择加入替换信号不是已经换掉，不是已经换掉。

2. **看见an opt-in replace signal is not already a replacement / 看见选择加入替换信号不是已经换掉 / 这份对象 is not already 已经是不变量 144 interchangeable，也不是已经 rbf signal vs replaced bundled（166） interchangeable / 1524 rbfs-notrep interchangeable / 1526 rbfs-notjoin interchangeable，也不是已经 策略≠共识 interchangeable / 144 策略≠共识 interchangeable。**  
   官方把an opt-in replace signal is not already a replacement和已经是不变量 144写成两件。看见an opt-in replace signal is not already a replacement，不是已经是不变量 144。

3. **看见选择加入替换信号不是已经换掉 / 看见an opt-in replace signal is not already a replacement / 这份对象 is not already 已经 166 bundled interchangeable，也不是已经 rbf signal vs replaced bundled（166） interchangeable / 1524 rbfs-notrep interchangeable / 1525 rbfs-notlock interchangeable，也不是已经 CSV≠绝对锁 interchangeable / 165 CSV≠绝对锁 interchangeable。**  
   官方把选择加入替换信号不是已经换掉和已经 166 bundled写成两件。看见选择加入替换信号不是已经换掉，不是已经 166 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样构造替换、怎样钉死、怎样挤掉商家看见的那笔。

## 官方为什么这样拆

- **选择加入替换信号不是已经换掉 interchangeable：官方写节点可以允许替换，带了信号不是已经换掉。**
- **看见本页不是已经是不变量 144。**
- **看见信号旋钮不是已经 166 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经换掉 | 不是已经换掉 | 不是已经策略≠共识（144） |
| 已经是不变量 144 | 不是已经是不变量 144 | 不是已经CSV≠绝对锁（165） |
| 已经 166 bundled | 不是已经 166 bundled | 不是已经1525 rbfs-notlock |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-125 opt-in-signal not already replaced / not already 144 / not already 166-bundled 正式三事（166 余量），必须分开是不是已经换掉、是不是已经是不变量 144、是不是已经 166 bundled。可以跳过「看见带了 RBF 就已经换掉」。不要另写 怎样构造替换、怎样钉死、怎样挤掉商家看见的那笔。166 rbf-signal vs replaced bundled unbundling 在本页 item 1 启动；续 [`worked-example-rbfs-notlock-vs-bundled.md`](worked-example-rbfs-notlock-vs-bundled.md)（不变量 1525 item 2）。

## 本页不抄

- 终值常数、替换条数、最低中继费率例子。
- 怎样构造替换、怎样钉死、怎样挤掉商家看见的那笔。
