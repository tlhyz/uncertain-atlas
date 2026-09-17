# 例：看见启用之后不能关 is not already vote-extension switch interchangeable / not already can disable interchangeable / not already settled interchangeable

**层次**：实现 / 启用之后不能关 not already vote-extension switch / not already can disable / not already settled 正式三事（343 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / FeatureParams.PbtsEnableHeight。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「启用之后不能关 not already vote-extension switch / not already can disable / not already settled 正式三事（343 余量）/ not 886 pbts-height-notlock interchangeable / not 343 pbts-height-vs-params bundled interchangeable」，不是 PbtsEnableHeight bundled（343），也不是到了 H 已经 Prepare 带了扩展（330），也不是必须协调升级（346/875）。不要另写怎样设 PbtsEnableHeight。

## 官方三件事

1. **看见启用之后不能关 / 看见不能写成当前高度或更矮 这份锁死 is not already 已经是扩展启用高度那种切换 interchangeable，也不是已经 PbtsEnableHeight bundled（343） interchangeable / 886 pbts-height-notlock interchangeable / 884 pbts-height-notzero interchangeable / 343 pbts item 1 写成 0 interchangeable，也不是已经启用之后不能关 not already vote-extension switch / not already can disable / not already settled 正式三事 bundled（343 item 3 余量） interchangeable / 343 pbts item 3 interchangeable。**  
   官方写：PBTS 一旦启用就不能关。不能写成低于或等于当前链高度。必须 `PbtsEnableHeight > [当前高度]`。看见不能关，不是已经是到了 H 才开始叫 ExtendVote 那种切换 interchangeable——本页从 343 item 3 侧钉 not already vote-extension switch 单句。343 pbts vs params bundled unbundling 在本页 item 3 完成。

2. **看见必须比当前高 / 看见字段锁死 / 这份锁死 is not already 已经能关 interchangeable，也不是已经 PbtsEnableHeight bundled（343） interchangeable / 886 pbts-height-notlock interchangeable / 343 pbts item 2 BFT Time interchangeable / 885 pbts-height-notbft interchangeable，也不是已经到了 H 已经 Prepare 带了扩展 interchangeable / 330 height-H interchangeable。**  
   官方把必须比当前高和已经能改回 0 分开——343 bundled 第三件事常与 330 / 346 混成「看见不能关就已经是扩展切换或已经能关 interchangeable」，本页钉 not already can disable 单句。

3. **看见字段锁死 / 看见不能关 / 这份锁死 is not already 已经交差 interchangeable，也不是已经 PbtsEnableHeight bundled（343） interchangeable / 886 pbts-height-notlock interchangeable / 884 pbts-height-notzero interchangeable，也不是已经必须协调升级 interchangeable / 346 / 875 abci20-upgrade-notfield interchangeable。**  
   官方把字段锁死和已经 Prepare 带了扩展 / 已经交差分开。看见字段锁死，不是已经 Prepare 带了扩展 interchangeable。343 pbts vs params bundled unbundling 在本页 item 3 完成。

怎样设 `PbtsEnableHeight`、默认取值、怎样选启用高度是规范里的做法，本页不抄。

## 官方为什么这样拆

- **启用之后不能关 not already vote-extension switch ≠ 已经是扩展启用高度那种切换 interchangeable：** 官方把时间戳算法锁死和投票扩展切换分开。
- **看见必须比当前高 not already can disable ≠ 已经能关 interchangeable：** 官方把必须比当前高和已经能改回 0 分开。
- **看见字段锁死 not already settled ≠ 已经交差 interchangeable：** 官方把字段锁死和已经交差分开；343 pbts vs params bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 启用之后不能关 | 不是已经是扩展启用高度那种切换 | 不是到了 H 已经 Prepare 带了扩展（330） |
| 看见必须比当前高 | 不是已经能关 | 不是必须协调升级（346/875） |
| 看见字段锁死 | 不是已经交差 | 不是写成 0 就已经启用（884） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看启用之后不能关 not already vote-extension switch / not already can disable / not already settled 正式三事（343 余量），必须分开是不是已经是扩展启用高度那种切换、是不是已经能关、是不是已经交差。可以跳过「看见不能关就已经是扩展切换」。不要另写怎样设 PbtsEnableHeight。343 pbts vs params bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样设 `PbtsEnableHeight`、默认取值、怎样选启用高度。
- PbtsEnableHeight bundled。那是不变量 343。
- 写成 0 不是已经启用 PBTS。那是不变量 343 item 1 余量 / 884。
- 到了 H 已经 Prepare 带了扩展。那是不变量 330。
- 必须协调升级。那是不变量 346 / 875。
