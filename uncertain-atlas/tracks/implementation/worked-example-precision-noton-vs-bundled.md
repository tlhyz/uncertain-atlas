# 例：看见填了两个 is not already PBTS enabled interchangeable / not already cannot-disable interchangeable / not already settled interchangeable

**层次**：实现 / 填了两个 not already PBTS enabled / not already cannot-disable / not already settled 正式三事（336 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / SynchronyParams.Precision / SynchronyParams.MessageDelay。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「填了两个 not already PBTS enabled / not already cannot-disable / not already settled 正式三事（336 余量）/ not 924 precision-noton interchangeable / not 336 precision-vs-msgdelay bundled interchangeable」，不是同步参数 bundled（336），也不是到了 H 已经 Prepare 带了扩展（330），也不是立刻整块执行已经离开关键路径（327）。不要另写怎样设 PRECISION / MSGDELAY 或怎样选启用高度。

## 官方三件事

1. **看见填了两个 / 看见这两个参数用于 PBTS 这份配置 is not already 已经启用 PBTS interchangeable，也不是已经同步参数 bundled（336） interchangeable / 924 precision-noton interchangeable / 923 precision-notmsg interchangeable / 336 precision item 1 Precision interchangeable，也不是已经填了两个 not already PBTS enabled / not already cannot-disable / not already settled 正式三事 bundled（336 item 2 余量） interchangeable / 336 precision item 2 interchangeable。**  
   官方写：这两个参数都由 PBTS 算法使用。看见填了两个，不是已经到了 PbtsEnableHeight interchangeable——本页从 336 item 2 侧钉 not already PBTS enabled 单句。336 precision vs msgdelay bundled unbundling 在本页 item 2 续。

2. **看见写了用于 PBTS / 看见参数在 / 这份配置 is not already 已经不能关 interchangeable，也不是已经同步参数 bundled（336） interchangeable / 924 precision-noton interchangeable / 336 precision item 3 用于 PBTS interchangeable / 925 precision-notconst interchangeable，也不是已经到了 H 已经 Prepare 带了扩展 interchangeable / 330 ve-height interchangeable。**  
   官方把写了用于 PBTS 和已经切到 PBTS / 已经不能关分开——336 bundled 第二件事常与 330 混成「看见填了两个就已经启用 PBTS 或已经是扩展启用高度那种切换 interchangeable」，本页钉 not already cannot-disable 单句。

3. **看见参数在 / 看见填了两个 / 这份配置 is not already 已经交差 interchangeable，也不是已经同步参数 bundled（336） interchangeable / 924 precision-noton interchangeable / 923 precision-notmsg interchangeable，也不是已经立刻整块执行已经离开关键路径 interchangeable / 327 prepare-timeout interchangeable。**  
   官方把参数在和已经交差分开。看见参数在，不是已经交差 interchangeable。336 precision vs msgdelay bundled unbundling 在本页 item 2 续。

怎样设 PRECISION / MSGDELAY、默认毫秒、怎样选 PbtsEnableHeight 是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **填了两个 not already PBTS enabled ≠ 已经启用 PBTS interchangeable：** 官方把参数存在和 PBTS 已经打开分开。
- **看见写了用于 PBTS not already cannot-disable ≠ 已经不能关 interchangeable：** 官方把用于 PBTS 和已经不能关 / 已经是扩展启用高度那种切换分开。
- **看见参数在 not already settled ≠ 已经交差 interchangeable：** 官方把参数在和已经交差分开；336 precision vs msgdelay bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 填了两个 / 用于 PBTS | 不是已经启用 PBTS | 不是到了 H 已经 Prepare 带了扩展（330） |
| 看见写了用于 PBTS | 不是已经不能关 | 不是立刻整块执行已经离开关键路径（327） |
| 看见参数在 | 不是已经交差 | 不是 Precision 就已经是 MessageDelay（923） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看填了两个 not already PBTS enabled / not already cannot-disable / not already settled 正式三事（336 余量），必须分开是不是已经启用 PBTS、是不是已经不能关、是不是已经交差。可以跳过「看见填了两个就已经启用 PBTS」。不要另写怎样设 PRECISION / MSGDELAY 或怎样选启用高度。336 precision vs msgdelay bundled unbundling 在本页 item 2 续；续 [`worked-example-precision-notconst-vs-bundled.md`](worked-example-precision-notconst-vs-bundled.md)（不变量 925 item 3）。

## 本页不抄

- 怎样设 PRECISION / MSGDELAY、默认毫秒、怎样选 PbtsEnableHeight。
- 同步参数 bundled。那是不变量 336。
- Precision 就已经是 MessageDelay。那是不变量 336 item 1 余量 / 923。
- 到了 H 已经 Prepare 带了扩展。那是不变量 330。
- 立刻整块执行已经离开关键路径。那是不变量 327。
