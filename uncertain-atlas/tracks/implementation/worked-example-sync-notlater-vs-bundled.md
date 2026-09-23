# 例：看见是同步的 / 看见引擎在等 / 看见立刻执行 is not already already later-revise interchangeable / already left-critical interchangeable / already full-exec interchangeable

**层次**：实现 / Process 调用是同步的不是已经能在返回之后再改裁决 not already later-revise / not already left-critical / not already full-exec 正式三事（354 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Process 调用是同步的不是已经能在返回之后再改裁决 not already later-revise / not already left-critical / not already full-exec 正式三事（354 余量）/ not 815 sync-notlater interchangeable / not 354 processwhen bundled interchangeable」，不是 Process 何时调用 bundled（354），也不是只做基本检查再异步 Process 不是已经还能再 Reject（816 item 2 余量）或非验证者可以立刻回 ACCEPT 不是已经验过这块（817 item 3 余量）。不要另写怎样写 Process 何时调用。

## 官方三件事

规范把 Methods 里 CometBFT 调 `ProcessProposal` 是同步的 和「已经是同步的就已经能稍后改裁决 interchangeable / 已经是引擎在等就已经离开关键路径 interchangeable / 已经是立刻执行就已经是立刻整块执行就已经离开关键路径 interchangeable / 已经是 processwhen bundled interchangeable」分开写成三件独立的实现事，不是「看见是同步的就已经能稍后改裁决 interchangeable / 就已经离开关键路径 interchangeable / 就已经是立刻整块执行就已经离开关键路径 interchangeable」一件事：

1. **看见 Process 调用是同步的 / 看见是同步的 / 看见引擎在等回包 is not already 已经能在返回之后再改裁决 interchangeable / 已经 later-revise interchangeable / 已经稍后改裁决交差 interchangeable / 354 processwhen bundled interchangeable / 327 preparetimeout interchangeable / processwhen-sold-as-later interchangeable，也不是已经 Process 何时调用 bundled（354） interchangeable / 815 sync-notlater interchangeable / 354 processwhen item 1 interchangeable，也不是已经 Process 调用是同步的不是已经能在返回之后再改裁决 not already later-revise / not already left-critical / not already full-exec 正式三事 bundled（354 item 1 余量） interchangeable / 354 processwhen item 1 interchangeable，也不是已经还能再 Reject（816） interchangeable / 817 nonval-notverified interchangeable / 33 fourgates interchangeable，也不是已经立刻整块执行就已经离开关键路径（327） interchangeable。**  
   官方写：CometBFT 调 `ProcessProposal` 是同步的。看见是同步的，不是已经能稍后改裁决。看见是同步的，不是已经 later-revise interchangeable——354 钉 bundled 三事，本页从 item 1 侧钉 not already later-revise 单句。看见 Process 调用是同步的，不是已经 Process 何时调用 bundled（354） interchangeable——354 钉 bundled，本页钉 item 1 第一件事。看见是同步的，不是已经还能再 Reject（816） interchangeable——816 另钉 item 2。看见是同步的，不是已经立刻整块执行就已经离开关键路径（327） interchangeable——327 另钉。354 processwhen vs later bundled unbundling 在本页 item 1 启动。

2. **看见引擎在等 / 看见引擎在等回包 / 看见在等 is not already 已经离开关键路径 interchangeable / 已经 left-critical interchangeable / 已经离开关键路径交差 interchangeable / 354 processwhen bundled interchangeable / 327 preparetimeout interchangeable，也不是已经 Process 何时调用 bundled（354） interchangeable / 815 sync-notlater interchangeable / 354 processwhen item 2 异步 interchangeable / 354 processwhen item 3 非验证者 interchangeable，也不是已经 Process 调用是同步的不是已经能在返回之后再改裁决 not already later-revise / not already left-critical / not already full-exec 正式三事 bundled（354 item 1 余量） interchangeable / 354 processwhen item 1 interchangeable，也不是已经能稍后改裁决（本页第一件事） interchangeable。**  
   官方写：看见引擎在等，不是已经离开关键路径。看见引擎在等回包，不是已经 left-critical interchangeable——本页钉 not already left-critical 单句。看见在等，不是已经能稍后改裁决（本页第一件事） interchangeable——三件事分开钉。354 processwhen vs later bundled unbundling 在本页 item 1 启动。

3. **看见立刻执行 / 看见同步立刻执行 / 看见立刻调 is not already 已经是立刻整块执行就已经离开关键路径 interchangeable / 已经 full-exec interchangeable / 已经立刻整块离开关键路径交差 interchangeable / 354 processwhen bundled interchangeable / 327 preparetimeout interchangeable，也不是已经 Process 何时调用 bundled（354） interchangeable / 815 sync-notlater interchangeable / 354 processwhen item 2 / 354 processwhen item 3，也不是已经 Process 调用是同步的不是已经能在返回之后再改裁决 not already later-revise / not already left-critical / not already full-exec 正式三事 bundled（354 item 1 余量） interchangeable / 354 processwhen item 1 interchangeable，也不是已经能稍后改裁决（本页第一件事） interchangeable / 已经离开关键路径（本页第二件事） interchangeable。**  
   官方写：看见立刻执行，不是已经是立刻整块执行就已经离开关键路径。看见同步立刻执行，不是已经 full-exec interchangeable——本页钉 not already full-exec 单句。看见立刻调，不是已经离开关键路径（本页第二件事） interchangeable——三件事分开钉。354 processwhen vs later bundled unbundling 在本页 item 1 启动。

怎样写 Process 何时调用、怎样写异步路径、怎样选非验证者立刻 ACCEPT 是规范里的做法，本页不抄。Process 何时调用 bundled（354）、只做基本检查再异步 Process 不是已经还能再 Reject（354 item 2 余量 / 816）、非验证者可以立刻回 ACCEPT 不是已经验过这块（354 item 3 余量 / 817）、立刻整块执行就已经离开关键路径（327）、四门已经结算（33）、Process 也会在提议者那边叫（351）是另外那套，本页不抄。

## 官方为什么这样拆

- **是同步的 not already later-revise ≠ 354 / 327 interchangeable：** 官方把同步调用和稍后改裁决分开。
- **引擎在等 not already left-critical ≠ 已经离开关键路径 interchangeable：** 官方把引擎在等和已经离开关键路径分开。
- **立刻执行 not already full-exec ≠ 已经是立刻整块执行就已经离开关键路径 interchangeable：** 官方把立刻执行和立刻整块执行就已经离开关键路径分开；354 processwhen vs later bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 是同步的 | 不是 already later-revise | 不是立刻整块执行就已经离开关键路径 alone（327） |
| 引擎在等 | 不是 already left-critical | 不是异步还能 Reject alone（816） |
| 立刻执行 | 不是 already full-exec | 不是非验证者立刻 ACCEPT alone（817） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Process 调用是同步的不是已经能在返回之后再改裁决 not already later-revise / not already left-critical / not already full-exec 正式三事（354 余量），必须分开是同步的 是不是 already later-revise interchangeable / 354 processwhen bundled interchangeable / processwhen-sold-as-later interchangeable、引擎在等 是不是 already left-critical interchangeable、立刻执行 是不是 already full-exec interchangeable。可以跳过「看见是同步的就已经能稍后改裁决 interchangeable / 就已经离开关键路径 interchangeable / 就已经是立刻整块执行就已经离开关键路径 interchangeable」。不要另写怎样写 Process 何时调用。354 processwhen vs later bundled unbundling 在本页 item 1 启动；续 [`worked-example-async-notreject-vs-bundled.md`](worked-example-async-notreject-vs-bundled.md)（不变量 816 item 2）；完成见 817。

## 本页不抄

- 怎样写 Process 何时调用、怎样写异步路径、怎样选非验证者立刻 ACCEPT。
- Process 何时调用 bundled。那是不变量 354。
- 只做基本检查再异步 Process 不是已经还能再 Reject。那是不变量 354 item 2 余量 / 816。
- 非验证者可以立刻回 ACCEPT 不是已经验过这块。那是不变量 354 item 3 余量 / 817。
- 立刻整块执行就已经离开关键路径。那是不变量 327。
- 四门已经结算。那是不变量 33。
- Process 也会在提议者那边叫。那是不变量 351。
