# 例：看见用于 PBTS / 看见能出合法提案 / 看见两把尺 is not already already eternal-constant interchangeable / already bft-median interchangeable / already clock-adjust interchangeable

**层次**：实现 / 用于 PBTS 不是已经是永恒常数 not already eternal-constant / not already bft-median / not already clock-adjust 正式三事（336 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / SynchronyParams.Precision / SynchronyParams.MessageDelay。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「用于 PBTS 不是已经是永恒常数 not already eternal-constant / not already bft-median / not already clock-adjust 正式三事（336 余量）/ not 763 precision-noteternal interchangeable / not 336 precision bundled interchangeable」，不是 Precision bundled（336），也不是填了 Precision 不是已经是 MessageDelay（761 item 1 余量）或填了两个不是已经启用 PBTS（762 item 2 余量）。不要另写怎样设 PRECISION / MSGDELAY 或怎样选启用高度。

## 官方三件事

规范把 Requirements 里用于 PBTS 的两把尺、能出合法提案 和「已经是用于 PBTS 就已经是永恒常数 interchangeable / 已经是能出合法提案就已经是 BFT Time 中位数 interchangeable / 已经是两把尺就已经是调整钟 interchangeable / 已经是 precision bundled interchangeable」分开写成三件独立的实现事，不是「看见用于 PBTS 就已经是永恒常数 interchangeable / 就已经是 BFT Time 中位数 interchangeable / 就已经是调整钟 interchangeable」一件事：

1. **看见用于 PBTS / 看见两把尺给 PBTS 用 / 看见写了 PBTS 用 is not already 已经是永恒常数 interchangeable / 已经 eternal-constant interchangeable / 已经抄成产品常数交差 interchangeable / 336 precision bundled interchangeable / 40 block-time interchangeable / precision-sold-as-msgdelay interchangeable，也不是已经 Precision bundled（336） interchangeable / 763 precision-noteternal interchangeable / 336 precision item 3 interchangeable，也不是已经用于 PBTS 不是已经是永恒常数 not already eternal-constant / not already bft-median / not already clock-adjust 正式三事 bundled（336 item 3 余量） interchangeable / 336 precision item 3 interchangeable，也不是已经填了 Precision 不是已经是 MessageDelay（761） interchangeable / 762 precision-notpbts interchangeable / 330 veheight interchangeable，也不是已经块时间必须点名算法（40） interchangeable。**  
   官方把它们写成 PBTS 用的两把尺，不是未标注版本的永恒共识常数。看见用于 PBTS，不是已经 eternal-constant interchangeable——336 钉 bundled 三事，本页从 item 3 侧钉 not already eternal-constant 单句。看见两把尺给 PBTS 用，不是已经 Precision bundled（336） interchangeable——336 钉 bundled，本页钉 item 3 第一件事。看见写了 PBTS 用，不是已经块时间必须点名算法（40） interchangeable——40 另钉。336 precision vs msgdelay bundled unbundling 在本页 item 3 完成。

2. **看见能出合法提案 / 看见仍能出合法提案 / 看见提案还能过 is not already 已经是 BFT Time 中位数 interchangeable / 已经 bft-median interchangeable / 已经是加权中位交差 interchangeable / 336 precision bundled interchangeable / 40 block-time interchangeable，也不是已经 Precision bundled（336） interchangeable / 763 precision-noteternal interchangeable / 336 precision item 1 MessageDelay interchangeable / 336 precision item 2 启用 PBTS interchangeable，也不是已经用于 PBTS 不是已经是永恒常数 not already eternal-constant / not already bft-median / not already clock-adjust 正式三事 bundled（336 item 3 余量） interchangeable / 336 precision item 3 interchangeable，也不是已经是永恒常数（本页第一件事） interchangeable。**  
   官方写：看见能出合法提案，不是已经是 MTP，也不是已经是上一高度 LastCommit 的加权中位。看见仍能出合法提案，不是已经 bft-median interchangeable——本页钉 not already bft-median 单句。看见提案还能过，不是已经是永恒常数（本页第一件事） interchangeable——三件事分开钉。336 precision vs msgdelay bundled unbundling 在本页 item 3 完成。

3. **看见两把尺 / 看见 Precision 和 MessageDelay / 看见同步参数两栏 is not already 已经是调整钟 interchangeable / 已经 clock-adjust interchangeable / 已经调钟交差 interchangeable / 336 precision bundled interchangeable / 40 block-time interchangeable，也不是已经 Precision bundled（336） interchangeable / 763 precision-noteternal interchangeable / 336 precision item 1 / 336 precision item 2，也不是已经用于 PBTS 不是已经是永恒常数 not already eternal-constant / not already bft-median / not already clock-adjust 正式三事 bundled（336 item 3 余量） interchangeable / 336 precision item 3 interchangeable，也不是已经是永恒常数（本页第一件事） interchangeable / 已经是 BFT Time 中位数（本页第二件事） interchangeable。**  
   官方写：看见能出合法提案，不是已经是调整钟。看见两把尺，不是已经 clock-adjust interchangeable——本页钉 not already clock-adjust 单句。看见 Precision 和 MessageDelay，不是已经是 BFT Time 中位数（本页第二件事） interchangeable——三件事分开钉。336 precision vs msgdelay bundled unbundling 在本页 item 3 完成。

怎样设 `PRECISION` / `MSGDELAY`、默认毫秒、怎样选 `PbtsEnableHeight` 是规范里的取值或做法，本页不抄。Precision bundled（336）、填了 Precision 不是已经是 MessageDelay（336 item 1 余量 / 761）、填了两个不是已经启用 PBTS（336 item 2 余量 / 762）、块时间必须点名算法（40）、到了 H 已经 Prepare 带了扩展（330）、立刻整块执行已经离开关键路径（327）是另外那套，本页不抄。

## 官方为什么这样拆

- **用于 PBTS not already eternal-constant ≠ 336 / 40 interchangeable：** 官方把这两把尺和永恒常数分开。
- **能出合法提案 not already bft-median ≠ 已经是 BFT Time 中位数 interchangeable：** 官方把能出合法提案和加权中位分开。
- **两把尺 not already clock-adjust ≠ 已经是调整钟 interchangeable：** 官方把两把尺和调整钟分开；336 precision vs msgdelay bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 用于 PBTS | 不是 already eternal-constant | 不是块时间必须点名算法 alone（40） |
| 能出合法提案 | 不是 already bft-median | 不是填了两个就已经启用 PBTS alone（762） |
| 两把尺 | 不是 already clock-adjust | 不是填了 Precision 就已经是 MessageDelay alone（761） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看用于 PBTS 不是已经是永恒常数 not already eternal-constant / not already bft-median / not already clock-adjust 正式三事（336 余量），必须分开用于 PBTS 是不是 already eternal-constant interchangeable / 336 precision bundled interchangeable / precision-sold-as-msgdelay interchangeable、能出合法提案 是不是 already bft-median interchangeable、两把尺 是不是 already clock-adjust interchangeable。可以跳过「看见用于 PBTS 就已经是永恒常数 interchangeable / 就已经是 BFT Time 中位数 interchangeable / 就已经是调整钟 interchangeable」。可以跳过「看见填了同步参数就已经是 PBTS」。不要另写怎样设 PRECISION / MSGDELAY 或怎样选启用高度。336 precision vs msgdelay bundled unbundling 在本页 item 3 完成（761 + 762 + 763）。

## 本页不抄

- 怎样设 `PRECISION` / `MSGDELAY`、默认毫秒、怎样选 `PbtsEnableHeight`。
- Precision bundled。那是不变量 336。
- 填了 Precision 不是已经是 MessageDelay。那是不变量 336 item 1 余量 / 761。
- 填了两个不是已经启用 PBTS。那是不变量 336 item 2 余量 / 762。
- 块时间必须点名算法。那是不变量 40。
- 到了 H 已经 Prepare 带了扩展。那是不变量 330。
- 立刻整块执行已经离开关键路径。那是不变量 327。
