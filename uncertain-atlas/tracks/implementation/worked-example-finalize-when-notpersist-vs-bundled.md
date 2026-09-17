# 例：看见先落决定再同步调 Finalize is not already settled interchangeable / not already persist app state interchangeable / not already sync means done interchangeable

**层次**：实现 / 先落决定再同步调 Finalize not already settled / not already persist app state / not already sync means done 正式三事（362 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「先落决定再同步调 Finalize not already settled / not already persist app state / not already sync means done 正式三事（362 余量）/ not 840 finalize-when-notpersist interchangeable / not 362 finalize-when-vs-decided bundled interchangeable」，不是 Finalize 何时调用 bundled（362），也不是 Finalize 改了就已经落盘（335），也不是 Commit persist（481），也不是 Finalize 回包义务就已经交差（363/838）。不要另写怎样写 Finalize 何时调用。

## 官方三件事

1. **看见先把 *v* 落成这一高的决定、再同步调 Finalize / 看见决定了 这份先落 is not already 已经交差 interchangeable，也不是已经 Finalize 何时调用 bundled（362） interchangeable / 840 finalize-when-notpersist interchangeable / 839 finalize-when-notcall interchangeable / 362 finalize-when item 1 +2/3 interchangeable，也不是已经先落决定再同步调 Finalize not already settled / not already persist app state / not already sync means done 正式三事 bundled（362 item 2 余量） interchangeable / 362 finalize-when item 2 interchangeable。**  
   官方写：*p* 先把 *v* 落成高度 *h* 的决定，再由 CometBFT 同步调 `FinalizeBlock`。看见决定了，不是已经交差 interchangeable——本页从 362 item 2 侧钉 not already settled 单句。362 finalize-when vs decided bundled unbundling 在本页 item 2 续。

2. **看见决定了 / 看见先落了决定 / 这份先落 is not already 已经落盘应用状态 interchangeable / 335 finpersist interchangeable，也不是已经 Finalize 何时调用 bundled（362） interchangeable / 840 finalize-when-notpersist interchangeable / 362 finalize-when item 3 回 AppHash interchangeable / 841 finalize-when-notheader interchangeable，也不是已经 Commit persist interchangeable / 481 commitpersist interchangeable。**  
   官方把先落了决定和已经落盘应用状态分开——362 bundled 第二件事常与 335 混成「看见决定了就已经交差或已经落盘应用状态 interchangeable」，本页钉 not already persist app state 单句。

3. **看见决定了 / 看见是同步的 / 这份先落 is not already 已经交差 interchangeable，也不是已经 Finalize 何时调用 bundled（362） interchangeable / 840 finalize-when-notpersist interchangeable / 839 finalize-when-notcall interchangeable，也不是已经 Finalize 回包义务就已经交差 interchangeable / 363 finalize-equiv / 838 finalize-equiv-notchanged interchangeable。**  
   官方把同步调用和已经交差分开。看见是同步的，不是已经交差 interchangeable。362 finalize-when vs decided bundled unbundling 在本页 item 2 续。

怎样写 Finalize 何时调用、怎样落决定、怎样算 ResultHash 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **先落决定再同步调 Finalize not already settled ≠ 已经交差 interchangeable：** 官方把落决定和交差分开。
- **看见先落了决定 not already persist app state ≠ 335 interchangeable：** 官方把先落决定和已经落盘应用状态分开。
- **看见是同步的 not already sync means done ≠ 已经交差 interchangeable：** 官方把同步调用和已经交差分开；362 finalize-when vs decided bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 先落决定再同步调 Finalize | 不是已经交差 | 不是 Finalize 改了就已经落盘（335） |
| 看见先落了决定 | 不是已经落盘应用状态 | 不是 Commit persist（481） |
| 看见是同步的 | 不是已经交差 | 不是 Finalize 回包义务就已经交差（363/838） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看先落决定再同步调 Finalize not already settled / not already persist app state / not already sync means done 正式三事（362 余量），必须分开是不是已经交差、是不是已经落盘应用状态、是不是同步调用就已经交差。可以跳过「看见决定了就已经交差」。不要另写怎样写 Finalize 何时调用。362 finalize-when vs decided bundled unbundling 在本页 item 2 续；续 [`worked-example-finalize-when-notheader-vs-bundled.md`](worked-example-finalize-when-notheader-vs-bundled.md)（不变量 841 item 3）。

## 本页不抄

- 怎样写 Finalize 何时调用、怎样落决定、怎样算 ResultHash。
- Finalize 何时调用 bundled。那是不变量 362。
- +2/3 precommit 才决定再调 Finalize。那是不变量 362 item 1 余量 / 839。
- Finalize 改了就已经落盘。那是不变量 335。
- Commit persist。那是不变量 481。
- Finalize 回包义务就已经交差。那是不变量 363 / 838。
