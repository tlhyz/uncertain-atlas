# 例：看见难度把叔块算进去不是已经改了出块奖励；看见可预期发行不是已经写了 Homestead 那次朝均值收敛；看见难度把叔块算进去不是已经没有炸弹

**层次**：共识 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-100](https://eips.ethereum.org/EIPS/eip-100)（Final, Core；Byzantium）。  
**对应课文**：[L3.1](../../courses/level-03-bitcoin/L03-M01-nakamoto-finality.md)。  
**不要写进**：`index/03` 状态行、M5.4、L5.1、L5.4、05b。本页是「EIP-100 uncles-in-diff not already reward / not already homestead-mean / not already no-bomb 正式三事（238 余量）/ not 1295 udiff-notbomb interchangeable / not 238 uncle-diff-vs-header bundled interchangeable」，不是 uncle diff vs header bundled（238），也不是已经 homestead-mean（234），也不是已经 coinbase-mature（163）。不要另写 怎样磨时间戳，怎样抬叔块率，怎样按精确个数复刻。

## 官方三件事

1. **看见难度把叔块算进去 / 看见难度把叔块算进去 这份对象 is not already 已经改了出块奖励 interchangeable，也不是已经 uncle diff vs header bundled（238） interchangeable / 1295 udiff-notbomb interchangeable / 1296 udiff-notcount interchangeable，也不是已经 EIP-100 uncles-in-diff not already reward / not already homestead-mean / not already no-bomb 正式三事 bundled（238 item 1 余量） interchangeable / 238 udiff item 1 interchangeable。**  
   官方把难度把叔块算进去和已经改了出块奖励写成两件。看见难度把叔块算进去，不是已经改了出块奖励。

2. **看见可预期发行 / 看见难度把叔块算进去 / 这份对象 is not already 已经写了 Homestead 那次朝均值收敛 interchangeable，也不是已经 uncle diff vs header bundled（238） interchangeable / 1295 udiff-notbomb interchangeable / 1297 udiff-notden interchangeable，也不是已经 homestead-mean interchangeable / 234 homestead-mean interchangeable。**  
   官方把可预期发行和已经写了 Homestead 那次朝均值收敛写成两件。看见可预期发行，不是已经写了 Homestead 那次朝均值收敛。

3. **看见难度把叔块算进去 / 看见可预期发行 / 这份对象 is not already 已经没有炸弹 interchangeable，也不是已经 uncle diff vs header bundled（238） interchangeable / 1295 udiff-notbomb interchangeable / 1296 udiff-notcount interchangeable，也不是已经 coinbase-mature interchangeable / 163 coinbase-mature interchangeable。**  
   官方把难度把叔块算进去和已经没有炸弹写成两件。看见难度把叔块算进去，不是已经没有炸弹。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样磨时间戳，怎样抬叔块率，怎样按精确个数复刻。

## 官方为什么这样拆

- **含叔块 不是已经齐了：官方说旧式只看父子时间，叔块率可以被拿来抬发行。**
- **本页 不是已经取消叔块奖励：官方写看见把叔块算进去，不是已经改了出块奖励。**
- **可预期发行 不是已经没有炸弹：本页改的是均值目标里有没有叔块，不是炸弹项。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经改了出块奖励 | 不是已经改了出块奖励 | 不是已经homestead-mean（234） |
| 已经写了 Homestead 那次朝均值收敛 | 不是已经写了 Homestead 那次朝均值收敛 | 不是已经coinbase-mature（163） |
| 已经没有炸弹 | 不是已经没有炸弹 | 不是已经1296 udiff-notcount |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-100 uncles-in-diff not already reward / not already homestead-mean / not already no-bomb 正式三事（238 余量），必须分开是不是已经改了出块奖励、是不是已经写了 Homestead 那次朝均值收敛、是不是已经没有炸弹。可以跳过「看见难度把叔块算进去就已经按个数调」。不要另写 怎样磨时间戳，怎样抬叔块率，怎样按精确个数复刻。238 uncle diff vs header bundled unbundling 在本页 item 1 启动；续 [`worked-example-udiff-notcount-vs-bundled.md`](worked-example-udiff-notcount-vs-bundled.md)（不变量 1296 item 2）。

## 本页不抄

- 分叉高度、时间粒度、分母新旧取值、下限、叔块率估计。
- 怎样磨时间戳，怎样抬叔块率，怎样按精确个数复刻。
