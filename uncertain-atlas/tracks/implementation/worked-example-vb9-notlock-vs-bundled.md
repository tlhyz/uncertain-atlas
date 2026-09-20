# 例：看见版本位被置上不是已经锁定不是已经锁定；看见setting a version bit is not already LOCKED_IN不是已经是不变量 173；看见版本位被置上不是已经锁定不是已经 171 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-9](https://github.com/bitcoin/bips/blob/master/bip-0009.mediawiki)（Version bits with timeout and delay）。  
**对应课文**：[L3.3](../../courses/level-03-bitcoin/L03-M03-conservative-evolution.md)。  
**不要写进**：`index/03` 共识行、M3.3、L3.3。本页是「BIP-9 bit-set not already locked-in / not already 173 / not already 171-bundled 正式三事（171 余量）/ not 1545 vb9-notlock interchangeable / not 171 versionbit-vs-active bundled interchangeable」，不是 versionbit vs active bundled（171），也不是已经 高度≠已在头上（173），也不是已经 CSV部署名≠操作码（165）。不要另写 怎样假示意、怎样拖激活、怎样复用位去骗旧软件。

## 官方三件事

1. **看见版本位被置上不是已经锁定 / 看见版本位被置上不是已经锁定 这份对象 is not already 已经锁定 interchangeable，也不是已经 versionbit vs active bundled（171） interchangeable / 1545 vb9-notlock interchangeable / 1546 vb9-notact interchangeable，也不是已经 BIP-9 bit-set not already locked-in / not already 173 / not already 171-bundled 正式三事 bundled（171 item 1 余量） interchangeable / 171 vb9 item 1 interchangeable。**  
   官方把版本位被置上不是已经锁定和已经锁定写成两件。看见版本位被置上不是已经锁定，不是已经锁定。

2. **看见setting a version bit is not already LOCKED_IN / 看见版本位被置上不是已经锁定 / 这份对象 is not already 已经是不变量 173 interchangeable，也不是已经 versionbit vs active bundled（171） interchangeable / 1545 vb9-notlock interchangeable / 1547 vb9-notfail interchangeable，也不是已经 高度≠已在头上 interchangeable / 173 高度≠已在头上 interchangeable。**  
   官方把setting a version bit is not already LOCKED_IN和已经是不变量 173写成两件。看见setting a version bit is not already LOCKED_IN，不是已经是不变量 173。

3. **看见版本位被置上不是已经锁定 / 看见setting a version bit is not already LOCKED_IN / 这份对象 is not already 已经 171 bundled interchangeable，也不是已经 versionbit vs active bundled（171） interchangeable / 1545 vb9-notlock interchangeable / 1546 vb9-notact interchangeable，也不是已经 CSV部署名≠操作码 interchangeable / 165 CSV部署名≠操作码 interchangeable。**  
   官方把版本位被置上不是已经锁定和已经 171 bundled写成两件。看见版本位被置上不是已经锁定，不是已经 171 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样假示意、怎样拖激活、怎样复用位去骗旧软件。

## 官方为什么这样拆

- **版本位被置上不是已经锁定 interchangeable：官方写 STARTED 窗里置位是示意，够数之后下一状态才是 LOCKED_IN。**
- **看见本页不是已经是不变量 173。**
- **看见版本位不是已经 171 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经锁定 | 不是已经锁定 | 不是已经高度≠已在头上（173） |
| 已经是不变量 173 | 不是已经是不变量 173 | 不是已经CSV部署名≠操作码（165） |
| 已经 171 bundled | 不是已经 171 bundled | 不是已经1546 vb9-notact |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-9 bit-set not already locked-in / not already 173 / not already 171-bundled 正式三事（171 余量），必须分开是不是已经锁定、是不是已经是不变量 173、是不是已经 171 bundled。可以跳过「看见置位就已经激活」。不要另写 怎样假示意、怎样拖激活、怎样复用位去骗旧软件。171 versionbit vs active bundled unbundling 在本页 item 1 启动；续 [`worked-example-vb9-notact-vs-bundled.md`](worked-example-vb9-notact-vs-bundled.md)（不变量 1546 item 2）。

## 本页不抄

- 阈值、窗长、版本取值范围、位数、开始秒数。
- 怎样假示意、怎样拖激活、怎样复用位去骗旧软件。
