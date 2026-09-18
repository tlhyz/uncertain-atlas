# 例：看见头上叔块哈希不是空不是已经数清有几个叔块；看见能调难度不是已经按个数调；看见头上叔块哈希不是空不是已经看整块

**层次**：共识 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-100](https://eips.ethereum.org/EIPS/eip-100)（Final, Core；Byzantium）。  
**对应课文**：[L3.1](../../courses/level-03-bitcoin/L03-M01-nakamoto-finality.md)。  
**不要写进**：`index/03` 状态行、M5.4、L5.1、L5.4、05b。本页是「EIP-100 header-approx not already counted / not already exact-k / not already whole-block 正式三事（238 余量）/ not 1296 udiff-notcount interchangeable / not 238 uncle-diff-vs-header bundled interchangeable」，不是 uncle diff vs header bundled（238），也不是已经 homestead-mean（234），也不是已经 mtp（41）。不要另写 怎样磨时间戳，怎样抬叔块率，怎样按精确个数复刻。

## 官方三件事

1. **看见头上叔块哈希不是空 / 看见头上叔块哈希不是空 这份对象 is not already 已经数清有几个叔块 interchangeable，也不是已经 uncle diff vs header bundled（238） interchangeable / 1296 udiff-notcount interchangeable / 1295 udiff-notbomb interchangeable，也不是已经 EIP-100 header-approx not already counted / not already exact-k / not already whole-block 正式三事 bundled（238 item 2 余量） interchangeable / 238 udiff item 2 interchangeable。**  
   官方把头上叔块哈希不是空和已经数清有几个叔块写成两件。看见头上叔块哈希不是空，不是已经数清有几个叔块。

2. **看见能调难度 / 看见头上叔块哈希不是空 / 这份对象 is not already 已经按个数调 interchangeable，也不是已经 uncle diff vs header bundled（238） interchangeable / 1296 udiff-notcount interchangeable / 1297 udiff-notden interchangeable，也不是已经 homestead-mean interchangeable / 234 homestead-mean interchangeable。**  
   官方把能调难度和已经按个数调写成两件。看见能调难度，不是已经按个数调。

3. **看见头上叔块哈希不是空 / 看见能调难度 / 这份对象 is not already 已经看整块 interchangeable，也不是已经 uncle diff vs header bundled（238） interchangeable / 1296 udiff-notcount interchangeable / 1295 udiff-notbomb interchangeable，也不是已经 mtp interchangeable / 41 mtp interchangeable。**  
   官方把头上叔块哈希不是空和已经看整块写成两件。看见头上叔块哈希不是空，不是已经看整块。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样磨时间戳，怎样抬叔块率，怎样按精确个数复刻。

## 官方为什么这样拆

- **只看头 不是已经数清：官方主动放弃精确个数，换空哈希 / 非空这一档。**
- **能调难度 不是已经按个数调：官方写精确式依赖整块，本页只用头上叔块哈希是不是空。**
- **头上叔块哈希不是空 不是已经看整块：官方写好让难度只吃头。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经数清有几个叔块 | 不是已经数清有几个叔块 | 不是已经homestead-mean（234） |
| 已经按个数调 | 不是已经按个数调 | 不是已经mtp（41） |
| 已经看整块 | 不是已经看整块 | 不是已经1295 udiff-notbomb |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-100 header-approx not already counted / not already exact-k / not already whole-block 正式三事（238 余量），必须分开是不是已经数清有几个叔块、是不是已经按个数调、是不是已经看整块。可以跳过「看见难度把叔块算进去就已经按个数调」。不要另写 怎样磨时间戳，怎样抬叔块率，怎样按精确个数复刻。238 uncle diff vs header bundled unbundling 在本页 item 2 续；续 [`worked-example-udiff-notden-vs-bundled.md`](worked-example-udiff-notden-vs-bundled.md)（不变量 1297 item 3）。

## 本页不抄

- 分叉高度、时间粒度、分母新旧取值、下限、叔块率估计。
- 怎样磨时间戳，怎样抬叔块率，怎样按精确个数复刻。
