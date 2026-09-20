# 例：看见锁定不是已经激活不是已经激活；看见LOCKED_IN is not already ACTIVE不是已经是不变量 165；看见锁定不是已经激活不是已经是不变量 41

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-9](https://github.com/bitcoin/bips/blob/master/bip-0009.mediawiki)（Version bits with timeout and delay）。  
**对应课文**：[L3.3](../../courses/level-03-bitcoin/L03-M03-conservative-evolution.md)。  
**不要写进**：`index/03` 共识行、M3.3、L3.3。本页是「BIP-9 locked-in not already active / not already 165 / not already 41 正式三事（171 余量）/ not 1546 vb9-notact interchangeable / not 171 versionbit-vs-active bundled interchangeable」，不是 versionbit vs active bundled（171），也不是已经 CSV部署名≠操作码（165），也不是已经 MTP三把尺（41）。不要另写 怎样假示意、怎样拖激活、怎样复用位去骗旧软件。

## 官方三件事

1. **看见锁定不是已经激活 / 看见锁定不是已经激活 这份对象 is not already 已经激活 interchangeable，也不是已经 versionbit vs active bundled（171） interchangeable / 1546 vb9-notact interchangeable / 1545 vb9-notlock interchangeable，也不是已经 BIP-9 locked-in not already active / not already 165 / not already 41 正式三事 bundled（171 item 2 余量） interchangeable / 171 vb9 item 2 interchangeable。**  
   官方把锁定不是已经激活和已经激活写成两件。看见锁定不是已经激活，不是已经激活。

2. **看见LOCKED_IN is not already ACTIVE / 看见锁定不是已经激活 / 这份对象 is not already 已经是不变量 165 interchangeable，也不是已经 versionbit vs active bundled（171） interchangeable / 1546 vb9-notact interchangeable / 1547 vb9-notfail interchangeable，也不是已经 CSV部署名≠操作码 interchangeable / 165 CSV部署名≠操作码 interchangeable。**  
   官方把LOCKED_IN is not already ACTIVE和已经是不变量 165写成两件。看见LOCKED_IN is not already ACTIVE，不是已经是不变量 165。

3. **看见锁定不是已经激活 / 看见LOCKED_IN is not already ACTIVE / 这份对象 is not already 已经是不变量 41 interchangeable，也不是已经 versionbit vs active bundled（171） interchangeable / 1546 vb9-notact interchangeable / 1545 vb9-notlock interchangeable，也不是已经 MTP三把尺 interchangeable / 41 MTP三把尺 interchangeable。**  
   官方把锁定不是已经激活和已经是不变量 41写成两件。看见锁定不是已经激活，不是已经是不变量 41。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样假示意、怎样拖激活、怎样复用位去骗旧软件。

## 官方为什么这样拆

- **锁定不是已经激活 interchangeable：官方写 LOCKED_IN 再过一个调整窗才自动变成 ACTIVE，新规则只对 ACTIVE 的块强制。**
- **看见本页不是已经是不变量 165。**
- **看见本页不是已经是不变量 41。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经激活 | 不是已经激活 | 不是已经CSV部署名≠操作码（165） |
| 已经是不变量 165 | 不是已经是不变量 165 | 不是已经MTP三把尺（41） |
| 已经是不变量 41 | 不是已经是不变量 41 | 不是已经1545 vb9-notlock |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-9 locked-in not already active / not already 165 / not already 41 正式三事（171 余量），必须分开是不是已经激活、是不是已经是不变量 165、是不是已经是不变量 41。可以跳过「看见置位就已经激活」。不要另写 怎样假示意、怎样拖激活、怎样复用位去骗旧软件。171 versionbit vs active bundled unbundling 在本页 item 2 续；续 [`worked-example-vb9-notfail-vs-bundled.md`](worked-example-vb9-notfail-vs-bundled.md)（不变量 1547 item 3）。

## 本页不抄

- 阈值、窗长、版本取值范围、位数、开始秒数。
- 怎样假示意、怎样拖激活、怎样复用位去骗旧软件。
