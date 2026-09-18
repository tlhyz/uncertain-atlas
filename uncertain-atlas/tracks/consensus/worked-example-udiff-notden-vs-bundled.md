# 例：看见改了分母不是已经量过不确定的墙钟；看见可预期不是官网吞吐已经是事实；看见改了分母不是已经写了后来那些推迟炸弹

**层次**：共识 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-100](https://eips.ethereum.org/EIPS/eip-100)（Final, Core；Byzantium）。  
**对应课文**：[L3.1](../../courses/level-03-bitcoin/L03-M01-nakamoto-finality.md)。  
**不要写进**：`index/03` 状态行、M5.4、L5.1、L5.4、05b。本页是「EIP-100 denom not already wall-clock / not already throughput / not already later-fork 正式三事（238 余量）/ not 1297 udiff-notden interchangeable / not 238 uncle-diff-vs-header bundled interchangeable」，不是 uncle diff vs header bundled（238），也不是已经 homestead-mean（234），也不是已经 coinbase-mature（163）。不要另写 怎样磨时间戳，怎样抬叔块率，怎样按精确个数复刻。

## 官方三件事

1. **看见改了分母 / 看见改了分母 这份对象 is not already 已经量过不确定的墙钟 interchangeable，也不是已经 uncle diff vs header bundled（238） interchangeable / 1297 udiff-notden interchangeable / 1295 udiff-notbomb interchangeable，也不是已经 EIP-100 denom not already wall-clock / not already throughput / not already later-fork 正式三事 bundled（238 item 3 余量） interchangeable / 238 udiff item 3 interchangeable。**  
   官方把改了分母和已经量过不确定的墙钟写成两件。看见改了分母，不是已经量过不确定的墙钟。

2. **看见可预期 / 看见改了分母 / 这份对象 is not already 官网吞吐已经是事实 interchangeable，也不是已经 uncle diff vs header bundled（238） interchangeable / 1297 udiff-notden interchangeable / 1296 udiff-notcount interchangeable，也不是已经 homestead-mean interchangeable / 234 homestead-mean interchangeable。**  
   官方把可预期和官网吞吐已经是事实写成两件。看见可预期，不是官网吞吐已经是事实。

3. **看见改了分母 / 看见可预期 / 这份对象 is not already 已经写了后来那些推迟炸弹 interchangeable，也不是已经 uncle diff vs header bundled（238） interchangeable / 1297 udiff-notden interchangeable / 1295 udiff-notbomb interchangeable，也不是已经 coinbase-mature interchangeable / 163 coinbase-mature interchangeable。**  
   官方把改了分母和已经写了后来那些推迟炸弹写成两件。看见改了分母，不是已经写了后来那些推迟炸弹。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样磨时间戳，怎样抬叔块率，怎样按精确个数复刻。

## 官方为什么这样拆

- **改了分母 不是已经量过墙钟：官方写是为了让出块时间大致还在原来那一带。**
- **可预期 不是官网吞吐已经是事实：官网吞吐不得当事实。**
- **改了分母 不是已经写了后来那些推迟炸弹：看见可预期，不是已经写了后来那些推迟炸弹、改奖励的分叉。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经量过不确定的墙钟 | 不是已经量过不确定的墙钟 | 不是已经homestead-mean（234） |
| 官网吞吐已经是事实 | 不是官网吞吐已经是事实 | 不是已经coinbase-mature（163） |
| 已经写了后来那些推迟炸弹 | 不是已经写了后来那些推迟炸弹 | 不是已经1295 udiff-notbomb |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-100 denom not already wall-clock / not already throughput / not already later-fork 正式三事（238 余量），必须分开是不是已经量过不确定的墙钟、是不是官网吞吐已经是事实、是不是已经写了后来那些推迟炸弹。可以跳过「看见难度把叔块算进去就已经按个数调」。不要另写 怎样磨时间戳，怎样抬叔块率，怎样按精确个数复刻。238 uncle diff vs header bundled unbundling 在本页 item 3 完成；本页收束本批。

## 本页不抄

- 分叉高度、时间粒度、分母新旧取值、下限、叔块率估计。
- 怎样磨时间戳，怎样抬叔块率，怎样按精确个数复刻。
