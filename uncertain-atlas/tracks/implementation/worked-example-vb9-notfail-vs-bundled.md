# 例：看见超时未锁定不是已经可以当激活不是已经可以当激活；看见timing out without lock is not already treating it as active不是已经是不变量 173；看见超时未锁定不是已经可以当激活不是已经是不变量 144

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-9](https://github.com/bitcoin/bips/blob/master/bip-0009.mediawiki)（Version bits with timeout and delay）。  
**对应课文**：[L3.3](../../courses/level-03-bitcoin/L03-M03-conservative-evolution.md)。  
**不要写进**：`index/03` 共识行、M3.3、L3.3。本页是「BIP-9 timeout-failed not already treat-as-active / not already 173 / not already 144 正式三事（171 余量）/ not 1547 vb9-notfail interchangeable / not 171 versionbit-vs-active bundled interchangeable」，不是 versionbit vs active bundled（171），也不是已经 高度≠已在头上（173），也不是已经 策略≠共识（144）。不要另写 怎样假示意、怎样拖激活、怎样复用位去骗旧软件。

## 官方三件事

1. **看见超时未锁定不是已经可以当激活 / 看见超时未锁定不是已经可以当激活 这份对象 is not already 已经可以当激活 interchangeable，也不是已经 versionbit vs active bundled（171） interchangeable / 1547 vb9-notfail interchangeable / 1545 vb9-notlock interchangeable，也不是已经 BIP-9 timeout-failed not already treat-as-active / not already 173 / not already 144 正式三事 bundled（171 item 3 余量） interchangeable / 171 vb9 item 3 interchangeable。**  
   官方把超时未锁定不是已经可以当激活和已经可以当激活写成两件。看见超时未锁定不是已经可以当激活，不是已经可以当激活。

2. **看见timing out without lock is not already treating it as active / 看见超时未锁定不是已经可以当激活 / 这份对象 is not already 已经是不变量 173 interchangeable，也不是已经 versionbit vs active bundled（171） interchangeable / 1547 vb9-notfail interchangeable / 1546 vb9-notact interchangeable，也不是已经 高度≠已在头上 interchangeable / 173 高度≠已在头上 interchangeable。**  
   官方把timing out without lock is not already treating it as active和已经是不变量 173写成两件。看见timing out without lock is not already treating it as active，不是已经是不变量 173。

3. **看见超时未锁定不是已经可以当激活 / 看见timing out without lock is not already treating it as active / 这份对象 is not already 已经是不变量 144 interchangeable，也不是已经 versionbit vs active bundled（171） interchangeable / 1547 vb9-notfail interchangeable / 1545 vb9-notlock interchangeable，也不是已经 策略≠共识 interchangeable / 144 策略≠共识 interchangeable。**  
   官方把超时未锁定不是已经可以当激活和已经是不变量 144写成两件。看见超时未锁定不是已经可以当激活，不是已经是不变量 144。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样假示意、怎样拖激活、怎样复用位去骗旧软件。

## 官方为什么这样拆

- **超时未锁定不是已经可以当激活 interchangeable：官方写超时且尚未 LOCKED_IN 走 FAILED，超时优先于锁定。**
- **看见本页不是已经是不变量 173。**
- **看见本页不是已经是不变量 144。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经可以当激活 | 不是已经可以当激活 | 不是已经高度≠已在头上（173） |
| 已经是不变量 173 | 不是已经是不变量 173 | 不是已经策略≠共识（144） |
| 已经是不变量 144 | 不是已经是不变量 144 | 不是已经1545 vb9-notlock |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-9 timeout-failed not already treat-as-active / not already 173 / not already 144 正式三事（171 余量），必须分开是不是已经可以当激活、是不是已经是不变量 173、是不是已经是不变量 144。可以跳过「看见置位就已经激活」。不要另写 怎样假示意、怎样拖激活、怎样复用位去骗旧软件。171 versionbit vs active bundled unbundling 在本页 item 3 完成；本页收束本批。下一份仍捆着的官方对象：valid-vs-der（172）。

## 本页不抄

- 阈值、窗长、版本取值范围、位数、开始秒数。
- 怎样假示意、怎样拖激活、怎样复用位去骗旧软件。
