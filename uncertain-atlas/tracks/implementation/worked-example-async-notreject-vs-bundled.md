# 例：看见异步了 / 看见先回了 / 看见还在跑 is not already already still-revise interchangeable / already still-reject interchangeable / already force-nil interchangeable

**层次**：实现 / 只做基本检查再异步 Process 不是已经还能再 Reject not already still-revise / not already still-reject / not already force-nil 正式三事（354 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「只做基本检查再异步 Process 不是已经还能再 Reject not already still-revise / not already still-reject / not already force-nil 正式三事（354 余量）/ not 816 async-notreject interchangeable / not 354 processwhen bundled interchangeable」，不是 Process 何时调用 bundled（354），也不是 Process 调用是同步的不是已经能在返回之后再改裁决（815 item 1 余量）或非验证者可以立刻回 ACCEPT 不是已经验过这块（817 item 3 余量）。不要另写怎样写 Process 何时调用。

## 官方三件事

规范把 Methods 里应用可以先做基本检查再异步处理这块、这时不能再 Reject、也不能再强迫 prevote/precommit `nil` 和「已经是异步了就已经还能改票 interchangeable / 已经是先回了就已经还能 Reject interchangeable / 已经是还在跑就已经能强迫 nil interchangeable / 已经是 processwhen bundled interchangeable」分开写成三件独立的实现事，不是「看见异步了就已经还能改票 interchangeable / 就已经还能 Reject interchangeable / 就已经能强迫 nil interchangeable」一件事：

1. **看见只做基本检查再异步 Process / 看见异步了 / 看见已经回了 `ACCEPT` is not already 已经还能改票 interchangeable / 已经 still-revise interchangeable / 已经还能改票交差 interchangeable / 354 processwhen bundled interchangeable / 33 fourgates interchangeable / processwhen-sold-as-later interchangeable，也不是已经 Process 何时调用 bundled（354） interchangeable / 816 async-notreject interchangeable / 354 processwhen item 2 interchangeable，也不是已经只做基本检查再异步 Process 不是已经还能再 Reject not already still-revise / not already still-reject / not already force-nil 正式三事 bundled（354 item 2 余量） interchangeable / 354 processwhen item 2 interchangeable，也不是已经能稍后改裁决（815） interchangeable / 817 nonval-notverified interchangeable / 327 preparetimeout interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：应用可以先做基本检查再异步处理这块；这时不能再 Reject，也不能再强迫 prevote/precommit `nil`。看见异步了，不是已经还能改票。看见异步了，不是已经 still-revise interchangeable——354 钉 bundled 三事，本页从 item 2 侧钉 not already still-revise 单句。看见只做基本检查再异步 Process，不是已经 Process 何时调用 bundled（354） interchangeable——354 钉 bundled，本页钉 item 2 第一件事。看见异步了，不是已经能稍后改裁决（815） interchangeable——815 另钉 item 1。看见异步了，不是已经四门已经结算（33） interchangeable——33 另钉。354 processwhen vs later bundled unbundling 在本页 item 2 续。

2. **看见先回了 / 看见已经回了 `ACCEPT` / 看见先回了 ACCEPT is not already 已经还能再 Reject interchangeable / 已经 still-reject interchangeable / 已经还能 Reject 交差 interchangeable / 354 processwhen bundled interchangeable / 33 fourgates interchangeable，也不是已经 Process 何时调用 bundled（354） interchangeable / 816 async-notreject interchangeable / 354 processwhen item 1 同步 interchangeable / 354 processwhen item 3 非验证者 interchangeable，也不是已经只做基本检查再异步 Process 不是已经还能再 Reject not already still-revise / not already still-reject / not already force-nil 正式三事 bundled（354 item 2 余量） interchangeable / 354 processwhen item 2 interchangeable，也不是已经还能改票（本页第一件事） interchangeable。**  
   官方写：看见先回了，不是已经还能 Reject。看见已经回了 `ACCEPT`，不是已经 still-reject interchangeable——本页钉 not already still-reject 单句。看见先回了 ACCEPT，不是已经还能改票（本页第一件事） interchangeable——三件事分开钉。354 processwhen vs later bundled unbundling 在本页 item 2 续。

3. **看见还在跑 / 看见异步还在跑 / 看见还在处理 is not already 已经能强迫 `nil` interchangeable / 已经 force-nil interchangeable / 已经强迫 nil 交差 interchangeable / 354 processwhen bundled interchangeable / 351 processalso interchangeable，也不是已经 Process 何时调用 bundled（354） interchangeable / 816 async-notreject interchangeable / 354 processwhen item 1 / 354 processwhen item 3，也不是已经只做基本检查再异步 Process 不是已经还能再 Reject not already still-revise / not already still-reject / not already force-nil 正式三事 bundled（354 item 2 余量） interchangeable / 354 processwhen item 2 interchangeable，也不是已经还能改票（本页第一件事） interchangeable / 已经还能 Reject（本页第二件事） interchangeable。**  
   官方写：看见还在跑，不是已经能强迫 `nil`。看见异步还在跑，不是已经 force-nil interchangeable——本页钉 not already force-nil 单句。看见还在处理，不是已经还能 Reject（本页第二件事） interchangeable——三件事分开钉。354 processwhen vs later bundled unbundling 在本页 item 2 续。

怎样写 Process 何时调用、怎样写异步路径、怎样选非验证者立刻 ACCEPT 是规范里的做法，本页不抄。Process 何时调用 bundled（354）、Process 调用是同步的不是已经能在返回之后再改裁决（354 item 1 余量 / 815）、非验证者可以立刻回 ACCEPT 不是已经验过这块（354 item 3 余量 / 817）、立刻整块执行就已经离开关键路径（327）、四门已经结算（33）、Process 也会在提议者那边叫（351）是另外那套，本页不抄。

## 官方为什么这样拆

- **异步了 not already still-revise ≠ 354 / 33 interchangeable：** 官方把异步处理和还能改票分开。
- **先回了 not already still-reject ≠ 已经还能再 Reject interchangeable：** 官方把先回了和已经还能 Reject 分开。
- **还在跑 not already force-nil ≠ 已经能强迫 nil interchangeable：** 官方把还在跑和已经能强迫 nil 分开；354 processwhen vs later bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 异步了 | 不是 already still-revise | 不是四门已经结算 alone（33） |
| 先回了 | 不是 already still-reject | 不是是同步的 already later-revise alone（815） |
| 还在跑 | 不是 already force-nil | 不是非验证者立刻 ACCEPT alone（817） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看只做基本检查再异步 Process 不是已经还能再 Reject not already still-revise / not already still-reject / not already force-nil 正式三事（354 余量），必须分开异步了 是不是 already still-revise interchangeable / 354 processwhen bundled interchangeable / processwhen-sold-as-later interchangeable、先回了 是不是 already still-reject interchangeable、还在跑 是不是 already force-nil interchangeable。可以跳过「看见异步了就已经还能改票 interchangeable / 就已经还能 Reject interchangeable / 就已经能强迫 nil interchangeable」。不要另写怎样写 Process 何时调用。354 processwhen vs later bundled unbundling 在本页 item 2 续（815 + 816）；完成 [`worked-example-nonval-notverified-vs-bundled.md`](worked-example-nonval-notverified-vs-bundled.md)（不变量 817 item 3）。

## 本页不抄

- 怎样写 Process 何时调用、怎样写异步路径、怎样选非验证者立刻 ACCEPT。
- Process 何时调用 bundled。那是不变量 354。
- Process 调用是同步的不是已经能在返回之后再改裁决。那是不变量 354 item 1 余量 / 815。
- 非验证者可以立刻回 ACCEPT 不是已经验过这块。那是不变量 354 item 3 余量 / 817。
- 立刻整块执行就已经离开关键路径。那是不变量 327。
- 四门已经结算。那是不变量 33。
- Process 也会在提议者那边叫。那是不变量 351。
