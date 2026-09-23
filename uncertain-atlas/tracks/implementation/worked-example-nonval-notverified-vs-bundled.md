# 例：看见立刻 ACCEPT / 看见不是验证者 / 看见规范允许 is not already already verified interchangeable / already settled interchangeable / already processalso interchangeable

**层次**：实现 / 非验证者可以立刻回 ACCEPT 不是已经验过这块 not already verified / not already settled / not already processalso 正式三事（354 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「非验证者可以立刻回 ACCEPT 不是已经验过这块 not already verified / not already settled / not already processalso 正式三事（354 余量）/ not 817 nonval-notverified interchangeable / not 354 processwhen bundled interchangeable」，不是 Process 何时调用 bundled（354），也不是 Process 调用是同步的不是已经能在返回之后再改裁决（815 item 1 余量）或只做基本检查再异步 Process 不是已经还能再 Reject（816 item 2 余量）。不要另写怎样写 Process 何时调用。

## 官方三件事

规范把 Methods 里非验证者可以立刻回 `ACCEPT`、不是验证者、规范允许 和「已经是立刻 ACCEPT 就已经验过这块 interchangeable / 已经是不是验证者就已经交差 interchangeable / 已经是规范允许就已经是提议者那边也会叫 Process interchangeable / 已经是 processwhen bundled interchangeable」分开写成三件独立的实现事，不是「看见立刻 ACCEPT 就已经验过这块 interchangeable / 就已经交差 interchangeable / 就已经是提议者那边也会叫 Process interchangeable」一件事：

1. **看见非验证者可以立刻回 `ACCEPT` / 看见立刻 `ACCEPT` / 看见立刻回了 ACCEPT is not already 已经验过这块 interchangeable / 已经 verified interchangeable / 已经验过交差 interchangeable / 354 processwhen bundled interchangeable / 33 fourgates interchangeable / processwhen-sold-as-later interchangeable，也不是已经 Process 何时调用 bundled（354） interchangeable / 817 nonval-notverified interchangeable / 354 processwhen item 3 interchangeable，也不是已经非验证者可以立刻回 ACCEPT 不是已经验过这块 not already verified / not already settled / not already processalso 正式三事 bundled（354 item 3 余量） interchangeable / 354 processwhen item 3 interchangeable，也不是已经能稍后改裁决（815） interchangeable / 816 async-notreject interchangeable / 351 processalso interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：若 *p* 不是验证者，且应用不想让非验证者处理 `ProcessProposal`，可以立刻回 `ACCEPT`。看见立刻 `ACCEPT`，不是已经验过。看见立刻 `ACCEPT`，不是已经 verified interchangeable——354 钉 bundled 三事，本页从 item 3 侧钉 not already verified 单句。看见非验证者可以立刻回 ACCEPT，不是已经 Process 何时调用 bundled（354） interchangeable——354 钉 bundled，本页钉 item 3 第一件事。看见立刻 ACCEPT，不是已经能稍后改裁决（815） interchangeable——815 另钉 item 1。看见立刻 ACCEPT，不是已经还能再 Reject（816） interchangeable——816 另钉 item 2。354 processwhen vs later bundled unbundling 在本页 item 3 完成。

2. **看见不是验证者 / 看见 *p* 不是验证者 / 看见非验证者 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 354 processwhen bundled interchangeable / 33 fourgates interchangeable，也不是已经 Process 何时调用 bundled（354） interchangeable / 817 nonval-notverified interchangeable / 354 processwhen item 1 同步 interchangeable / 354 processwhen item 2 异步 interchangeable，也不是已经非验证者可以立刻回 ACCEPT 不是已经验过这块 not already verified / not already settled / not already processalso 正式三事 bundled（354 item 3 余量） interchangeable / 354 processwhen item 3 interchangeable，也不是已经验过这块（本页第一件事） interchangeable。**  
   官方写：看见不是验证者，不是已经交差。看见 *p* 不是验证者，不是已经 settled interchangeable——本页钉 not already settled 单句。看见非验证者，不是已经验过这块（本页第一件事） interchangeable——三件事分开钉。354 processwhen vs later bundled unbundling 在本页 item 3 完成。

3. **看见规范允许 / 看见可以立刻回 / 看见不想让非验证者处理 is not already 已经是提议者那边也会叫 Process interchangeable / 已经 processalso interchangeable / 已经 processalso 交差 interchangeable / 354 processwhen bundled interchangeable / 351 processalso interchangeable，也不是已经 Process 何时调用 bundled（354） interchangeable / 817 nonval-notverified interchangeable / 354 processwhen item 1 / 354 processwhen item 2，也不是已经非验证者可以立刻回 ACCEPT 不是已经验过这块 not already verified / not already settled / not already processalso 正式三事 bundled（354 item 3 余量） interchangeable / 354 processwhen item 3 interchangeable，也不是已经验过这块（本页第一件事） interchangeable / 已经交差（本页第二件事） interchangeable。**  
   官方写：看见规范允许，不是已经是提议者那边也会叫 Process。看见可以立刻回，不是已经 processalso interchangeable——本页钉 not already processalso 单句。看见不想让非验证者处理，不是已经交差（本页第二件事） interchangeable——三件事分开钉。354 processwhen vs later bundled unbundling 在本页 item 3 完成。

怎样写 Process 何时调用、怎样写异步路径、怎样选非验证者立刻 ACCEPT 是规范里的做法，本页不抄。Process 何时调用 bundled（354）、Process 调用是同步的不是已经能在返回之后再改裁决（354 item 1 余量 / 815）、只做基本检查再异步 Process 不是已经还能再 Reject（354 item 2 余量 / 816）、立刻整块执行就已经离开关键路径（327）、四门已经结算（33）、Process 也会在提议者那边叫（351）是另外那套，本页不抄。

## 官方为什么这样拆

- **立刻 ACCEPT not already verified ≠ 354 / 33 interchangeable：** 官方把立刻 ACCEPT 和已经验过分开。
- **不是验证者 not already settled ≠ 已经交差 interchangeable：** 官方把不是验证者和已经交差分开。
- **规范允许 not already processalso ≠ 已经是提议者那边也会叫 Process interchangeable：** 官方把规范允许和已经是提议者那边也会叫 Process 分开；354 processwhen vs later bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 立刻 ACCEPT | 不是 already verified | 不是 Process 也会在提议者那边叫 alone（351） |
| 不是验证者 | 不是 already settled | 不是异步了 already still-revise alone（816） |
| 规范允许 | 不是 already processalso | 不是是同步的 already later-revise alone（815） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看非验证者可以立刻回 ACCEPT 不是已经验过这块 not already verified / not already settled / not already processalso 正式三事（354 余量），必须分开立刻 ACCEPT 是不是 already verified interchangeable / 354 processwhen bundled interchangeable / processwhen-sold-as-later interchangeable、不是验证者 是不是 already settled interchangeable、规范允许 是不是 already processalso interchangeable。可以跳过「看见立刻 ACCEPT 就已经验过这块 interchangeable / 就已经交差 interchangeable / 就已经是提议者那边也会叫 Process interchangeable」。不要另写怎样写 Process 何时调用。354 processwhen vs later bundled unbundling 在本页 item 3 完成（815 + 816 + 817）。

## 本页不抄

- 怎样写 Process 何时调用、怎样写异步路径、怎样选非验证者立刻 ACCEPT。
- Process 何时调用 bundled。那是不变量 354。
- Process 调用是同步的不是已经能在返回之后再改裁决。那是不变量 354 item 1 余量 / 815。
- 只做基本检查再异步 Process 不是已经还能再 Reject。那是不变量 354 item 2 余量 / 816。
- 立刻整块执行就已经离开关键路径。那是不变量 327。
- 四门已经结算。那是不变量 33。
- Process 也会在提议者那边叫。那是不变量 351。
