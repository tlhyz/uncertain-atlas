# 例：看见 InitChain once-at-genesis is not already crash-recall interchangeable / not already skip-step interchangeable / not already past-genesis interchangeable

**层次**：实现 / InitChain once-at-genesis not already crash-recall / not already skip-step / not already past-genesis 正式三事（412 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「InitChain once-at-genesis not already crash-recall / not already skip-step / not already past-genesis 正式三事（412 余量）/ not 1091 ionce-notcrash interchangeable / not 412 initonce-vs-crash bundled interchangeable」，不是 InitChain Usage 余量 bundled（412），也不是崩溃后第一块 Commit 之前再调 InitChain 就已经交差（320），也不是创世文件与应用段就已经交差（303）。不要另写怎样写 InitChain Usage 余量。

## 官方三件事

1. **看见 InitChain 创世时只调一次 / 看见调了一次 这份栏 is not already 已经是崩溃后再调 interchangeable，也不是已经 InitChain Usage 余量 bundled（412） interchangeable / 1091 ionce-notcrash interchangeable / 1092 ionce-notempty interchangeable / 412 initonce item 2 decide interchangeable，也不是已经 InitChain once-at-genesis not already crash-recall / not already skip-step / not already past-genesis 正式三事 bundled（412 item 1 余量） interchangeable / 412 initonce item 1 interchangeable。**  
   官方写：Called once upon genesis。看见创世时只调一次，不是已经是崩溃后再调 interchangeable——本页从 412 item 1 侧钉 not already crash-recall 单句。412 initonce vs crash bundled unbundling 在本页 item 1 启动。

2. **看见调了一次 / 看见创世时只调一次 / 这份栏 is not already 已经能跳步 interchangeable，也不是已经 InitChain Usage 余量 bundled（412） interchangeable / 1091 ionce-notcrash interchangeable / 412 initonce item 3 empty-update interchangeable / 1093 ionce-notchg interchangeable，也不是已经崩溃后第一块 Commit 之前再调 InitChain 就已经交差 interchangeable / 320 crashrec interchangeable。**  
   官方把调了一次和已经能跳步分开。看见调了一次，不是已经能跳步 interchangeable。本页钉 not already skip-step 单句。

3. **看见有创世调用 / 看见创世时只调一次 / 这份栏 is not already 已经过了 genesis_time interchangeable，也不是已经 InitChain Usage 余量 bundled（412） interchangeable / 1091 ionce-notcrash interchangeable / 1092 ionce-notempty interchangeable，也不是已经创世文件与应用段就已经交差 interchangeable / 303 genesis interchangeable。**  
   官方把有创世调用和已经过了 genesis_time 分开。看见有创世调用，不是已经过了 genesis_time interchangeable。412 initonce vs crash bundled unbundling 在本页 item 1 启动。

怎样写 InitChain Usage 余量、怎样决定接受创世集合、怎样从空集合更新是规范里的做法，本页不抄。

## 官方为什么这样拆

- **InitChain once-at-genesis not already crash-recall ≠ 已经是崩溃后再调 interchangeable：** 官方把创世时只调一次和崩溃后再调分开。
- **看见调了一次 not already skip-step ≠ 已经能跳步 interchangeable：** 官方把调了一次和已经能跳步分开。
- **看见有创世调用 not already past-genesis ≠ 已经过了 genesis_time interchangeable：** 官方把有创世调用和已经过了 genesis_time 分开；412 initonce vs crash bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| InitChain 创世时只调一次 | 不是已经是崩溃后再调 | 不是崩溃后第一块 Commit 之前再调 InitChain 就已经交差（320） |
| 看见调了一次 | 不是已经能跳步 | 不是创世文件与应用段就已经交差（303） |
| 看见有创世调用 | 不是已经过了 genesis_time | 不是能决定就已经没有集合（1092） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain once-at-genesis not already crash-recall / not already skip-step / not already past-genesis 正式三事（412 余量），必须分开是不是已经是崩溃后再调、是不是已经能跳步、是不是已经过了 genesis_time。可以跳过「看见填了 InitChain Usage 余量就已经是崩溃后再调」。不要另写怎样写 InitChain Usage 余量。412 initonce vs crash bundled unbundling 在本页 item 1 启动；续 [`worked-example-ionce-notempty-vs-bundled.md`](worked-example-ionce-notempty-vs-bundled.md)（不变量 1092 item 2）。

## 本页不抄

- 怎样写 InitChain Usage 余量、怎样决定接受创世集合、怎样从空集合更新。
- InitChain Usage 余量 bundled。那是不变量 412。
- 崩溃后第一块 Commit 之前再调 InitChain 就已经交差。那是不变量 320。
- 创世文件与应用段就已经交差。那是不变量 303。
