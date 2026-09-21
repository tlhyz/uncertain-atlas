# 例：看见填了两个 / 看见这两个参数用于 PBTS / 看见参数在 is not already already pbts-enabled interchangeable / already switched interchangeable / already cannot-off interchangeable

**层次**：实现 / 填了两个不是已经启用 PBTS not already pbts-enabled / not already switched / not already cannot-off 正式三事（336 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / SynchronyParams.Precision / SynchronyParams.MessageDelay。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「填了两个不是已经启用 PBTS not already pbts-enabled / not already switched / not already cannot-off 正式三事（336 余量）/ not 762 precision-notpbts interchangeable / not 336 precision bundled interchangeable」，不是 Precision bundled（336），也不是填了 Precision 不是已经是 MessageDelay（761 item 1 余量）或用于 PBTS 不是已经是永恒常数（763 item 3 余量）。不要另写怎样设 PRECISION / MSGDELAY 或怎样选启用高度。

## 官方三件事

规范把 Requirements 里填了两个同步参数、写了用于 PBTS 和「已经是填了两个就已经启用 PBTS interchangeable / 已经是写了用于 PBTS 就已经切到 PBTS interchangeable / 已经是参数在就已经不能关 interchangeable / 已经是 precision bundled interchangeable」分开写成三件独立的实现事，不是「看见填了两个就已经启用 PBTS interchangeable / 就已经切到 PBTS interchangeable / 就已经不能关 interchangeable」一件事：

1. **看见填了两个 / 看见 Precision 和 MessageDelay 都填了 / 看见两把尺都在 is not already 已经启用 PBTS interchangeable / 已经 pbts-enabled interchangeable / 已经到了 PbtsEnableHeight 交差 interchangeable / 336 precision bundled interchangeable / 40 block-time interchangeable / precision-sold-as-msgdelay interchangeable，也不是已经 Precision bundled（336） interchangeable / 762 precision-notpbts interchangeable / 336 precision item 2 interchangeable，也不是已经填了两个不是已经启用 PBTS not already pbts-enabled / not already switched / not already cannot-off 正式三事 bundled（336 item 2 余量） interchangeable / 336 precision item 2 interchangeable，也不是已经填了 Precision 不是已经是 MessageDelay（761） interchangeable / 763 precision-noteternal interchangeable / 330 veheight interchangeable，也不是已经块时间必须点名算法（40） interchangeable。**  
   官方写：这两个参数都由 PBTS 算法使用。看见填了两个，不是已经到了 `PbtsEnableHeight`。看见填了两个，不是已经 pbts-enabled interchangeable——336 钉 bundled 三事，本页从 item 2 侧钉 not already pbts-enabled 单句。看见两把尺都在，不是已经 Precision bundled（336） interchangeable——336 钉 bundled，本页钉 item 2 第一件事。看见填了两个，不是已经到了 H 已经 Prepare 带了扩展（330） interchangeable——330 另钉。336 precision vs msgdelay bundled unbundling 在本页 item 2 续。

2. **看见这两个参数用于 PBTS / 看见写了用于 PBTS / 看见参数写给 PBTS is not already 已经切到 PBTS interchangeable / 已经 switched interchangeable / 已经切过去交差 interchangeable / 336 precision bundled interchangeable / 330 veheight interchangeable，也不是已经 Precision bundled（336） interchangeable / 762 precision-notpbts interchangeable / 336 precision item 1 MessageDelay interchangeable / 336 precision item 3 永恒常数 interchangeable，也不是已经填了两个不是已经启用 PBTS not already pbts-enabled / not already switched / not already cannot-off 正式三事 bundled（336 item 2 余量） interchangeable / 336 precision item 2 interchangeable，也不是已经启用 PBTS（本页第一件事） interchangeable。**  
   官方写：看见写了用于 PBTS，不是已经切到 PBTS。看见这两个参数用于 PBTS，不是已经 switched interchangeable——本页钉 not already switched 单句。看见参数写给 PBTS，不是已经启用 PBTS（本页第一件事） interchangeable——三件事分开钉。336 precision vs msgdelay bundled unbundling 在本页 item 2 续。

3. **看见参数在 / 看见同步参数还在 / 看见两把尺还在表里 is not already 已经不能关 interchangeable / 已经 cannot-off interchangeable / 已经永远开着交差 interchangeable / 336 precision bundled interchangeable / 330 veheight interchangeable，也不是已经 Precision bundled（336） interchangeable / 762 precision-notpbts interchangeable / 336 precision item 1 / 336 precision item 3，也不是已经填了两个不是已经启用 PBTS not already pbts-enabled / not already switched / not already cannot-off 正式三事 bundled（336 item 2 余量） interchangeable / 336 precision item 2 interchangeable，也不是已经启用 PBTS（本页第一件事） interchangeable / 已经切到 PBTS（本页第二件事） interchangeable。**  
   官方写：看见参数在，不是已经不能关，也不是已经是扩展启用高度那种切换。看见同步参数还在，不是已经 cannot-off interchangeable——本页钉 not already cannot-off 单句。看见两把尺还在表里，不是已经切到 PBTS（本页第二件事） interchangeable——三件事分开钉。336 precision vs msgdelay bundled unbundling 在本页 item 2 续。

怎样设 `PRECISION` / `MSGDELAY`、默认毫秒、怎样选 `PbtsEnableHeight` 是规范里的取值或做法，本页不抄。Precision bundled（336）、填了 Precision 不是已经是 MessageDelay（336 item 1 余量 / 761）、用于 PBTS 不是已经是永恒常数（336 item 3 余量 / 763）、块时间必须点名算法（40）、到了 H 已经 Prepare 带了扩展（330）、立刻整块执行已经离开关键路径（327）是另外那套，本页不抄。

## 官方为什么这样拆

- **填了两个 not already pbts-enabled ≠ 336 / 40 interchangeable：** 官方把参数存在和 PBTS 已经打开分开。
- **写了用于 PBTS not already switched ≠ 已经切到 PBTS interchangeable：** 官方把用于 PBTS 和已经切到 PBTS 分开。
- **参数在 not already cannot-off ≠ 已经不能关 interchangeable：** 官方把参数在和已经不能关、扩展启用高度那种切换分开；336 precision vs msgdelay bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 填了两个 | 不是 already pbts-enabled | 不是填了 Precision 就已经是 MessageDelay alone（761） |
| 写了用于 PBTS | 不是 already switched | 不是到了 H 已经 Prepare 带了扩展 alone（330） |
| 参数在 | 不是 already cannot-off | 不是用于 PBTS 就已经是永恒常数 alone（763） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看填了两个不是已经启用 PBTS not already pbts-enabled / not already switched / not already cannot-off 正式三事（336 余量），必须分开填了两个 是不是 already pbts-enabled interchangeable / 336 precision bundled interchangeable / precision-sold-as-msgdelay interchangeable、写了用于 PBTS 是不是 already switched interchangeable、参数在 是不是 already cannot-off interchangeable。可以跳过「看见填了两个就已经启用 PBTS interchangeable / 就已经切到 PBTS interchangeable / 就已经不能关 interchangeable」。可以跳过「看见填了同步参数就已经是 PBTS」。不要另写怎样设 PRECISION / MSGDELAY 或怎样选启用高度。336 precision vs msgdelay bundled unbundling 在本页 item 2 续（761 + 762）；续 [`worked-example-precision-noteternal-vs-bundled.md`](worked-example-precision-noteternal-vs-bundled.md)（不变量 763 item 3）。

## 本页不抄

- 怎样设 `PRECISION` / `MSGDELAY`、默认毫秒、怎样选 `PbtsEnableHeight`。
- Precision bundled。那是不变量 336。
- 填了 Precision 不是已经是 MessageDelay。那是不变量 336 item 1 余量 / 761。
- 用于 PBTS 不是已经是永恒常数。那是不变量 336 item 3 余量 / 763。
- 块时间必须点名算法。那是不变量 40。
- 到了 H 已经 Prepare 带了扩展。那是不变量 330。
- 立刻整块执行已经离开关键路径。那是不变量 327。
