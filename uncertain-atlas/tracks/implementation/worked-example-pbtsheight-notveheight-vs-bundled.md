# 例：看见启用之后不能关 / 看见不能写成当前高度或更矮 / 看见字段锁死 is not already already veheight-switch interchangeable / already can-disable interchangeable / already prepare-ext interchangeable

**层次**：实现 / 启用之后不能关不是已经是扩展启用高度那种切换 not already veheight-switch / not already can-disable / not already prepare-ext 正式三事（343 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / FeatureParams.PbtsEnableHeight。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「启用之后不能关不是已经是扩展启用高度那种切换 not already veheight-switch / not already can-disable / not already prepare-ext 正式三事（343 余量）/ not 784 pbtsheight-notveheight interchangeable / not 343 pbtsheight bundled interchangeable」，不是 PbtsEnableHeight bundled（343），也不是写成 0 不是已经启用 PBTS（782 item 1 余量）或 H 之前仍用 BFT Time 不是已经切到 PBTS（783 item 2 余量）。不要另写怎样设 PbtsEnableHeight。

## 官方三件事

规范把 Requirements 里 PBTS 一旦启用就不能关、不能写成当前高度或更矮 和「已经是不能关就已经是扩展启用高度那种切换 interchangeable / 已经是必须比当前高就已经能改回 0 interchangeable / 已经是字段锁死就已经 Prepare 带了扩展 interchangeable / 已经是 pbtsheight bundled interchangeable」分开写成三件独立的实现事，不是「看见启用之后不能关就已经是扩展启用高度那种切换 interchangeable / 就已经能关 interchangeable / 就已经 Prepare 带了扩展 interchangeable」一件事：

1. **看见启用之后不能关 / 看见 PBTS 一旦启用就不能关 / 看见时间戳算法锁死 is not already 已经是扩展启用高度那种切换 interchangeable / 已经 veheight-switch interchangeable / 已经是到了 H 才叫 ExtendVote 交差 interchangeable / 343 pbtsheight bundled interchangeable / 330 veheight interchangeable / pbtsheight-sold-as-enabled interchangeable，也不是已经 PbtsEnableHeight bundled（343） interchangeable / 784 pbtsheight-notveheight interchangeable / 343 pbtsheight item 3 interchangeable，也不是已经启用之后不能关不是已经是扩展启用高度那种切换 not already veheight-switch / not already can-disable / not already prepare-ext 正式三事 bundled（343 item 3 余量） interchangeable / 343 pbtsheight item 3 interchangeable，也不是已经写成 0 不是已经启用（782） interchangeable / 783 pbtsheight-notbfttime interchangeable / 346 abci20-upgrade interchangeable，也不是已经到了 H 已经 Prepare 带了扩展（330） interchangeable。**  
   官方写：PBTS 一旦启用就不能关。看见不能关，不是已经是到了 H 才开始叫 ExtendVote 那种切换。看见启用之后不能关，不是已经 veheight-switch interchangeable——343 钉 bundled 三事，本页从 item 3 侧钉 not already veheight-switch 单句。看见时间戳算法锁死，不是已经 PbtsEnableHeight bundled（343） interchangeable——343 钉 bundled，本页钉 item 3 第一件事。看见不能关，不是已经到了 H 已经 Prepare 带了扩展（330） interchangeable——330 另钉。343 pbtsheight vs params bundled unbundling 在本页 item 3 完成。

2. **看见不能写成当前高度或更矮 / 看见必须 `PbtsEnableHeight > [当前高度]` / 看见必须比当前高 is not already 已经能关 interchangeable / 已经 can-disable interchangeable / 已经能改回 0 交差 interchangeable / 343 pbtsheight bundled interchangeable / 58 enable-height interchangeable，也不是已经 PbtsEnableHeight bundled（343） interchangeable / 784 pbtsheight-notveheight interchangeable / 343 pbtsheight item 1 写成 0 interchangeable / 343 pbtsheight item 2 BFT Time interchangeable，也不是已经启用之后不能关不是已经是扩展启用高度那种切换 not already veheight-switch / not already can-disable / not already prepare-ext 正式三事 bundled（343 item 3 余量） interchangeable / 343 pbtsheight item 3 interchangeable，也不是已经是扩展启用高度那种切换（本页第一件事） interchangeable。**  
   官方写：不能写成低于或等于当前链高度。必须 `PbtsEnableHeight > [当前高度]`。看见必须比当前高，不是已经能改回 0。看见不能写成当前高度或更矮，不是已经 can-disable interchangeable——本页钉 not already can-disable 单句。看见必须比当前高，不是已经是扩展启用高度那种切换（本页第一件事） interchangeable——三件事分开钉。343 pbtsheight vs params bundled unbundling 在本页 item 3 完成。

3. **看见字段锁死 / 看见启用高度锁死 / 看见不能再改回关掉 is not already 已经 Prepare 带了扩展 interchangeable / 已经 prepare-ext interchangeable / 已经 Prepare 带扩展交差 interchangeable / 343 pbtsheight bundled interchangeable / veheight-sold-as-prepared interchangeable / 330 veheight interchangeable，也不是已经 PbtsEnableHeight bundled（343） interchangeable / 784 pbtsheight-notveheight interchangeable / 343 pbtsheight item 1 / 343 pbtsheight item 2，也不是已经启用之后不能关不是已经是扩展启用高度那种切换 not already veheight-switch / not already can-disable / not already prepare-ext 正式三事 bundled（343 item 3 余量） interchangeable / 343 pbtsheight item 3 interchangeable，也不是已经是扩展启用高度那种切换（本页第一件事） interchangeable / 已经能关（本页第二件事） interchangeable。**  
   官方写：看见字段锁死，不是已经 Prepare 带了扩展。看见启用高度锁死，不是已经 prepare-ext interchangeable——本页钉 not already prepare-ext 单句。看见不能再改回关掉，不是已经能关（本页第二件事） interchangeable——三件事分开钉。343 pbtsheight vs params bundled unbundling 在本页 item 3 完成。

怎样设 `PbtsEnableHeight`、默认取值、怎样选启用高度是规范里的做法，本页不抄。PbtsEnableHeight bundled（343）、写成 0 不是已经启用 PBTS（343 item 1 余量 / 782）、H 之前仍用 BFT Time 不是已经切到 PBTS（343 item 2 余量 / 783）、到了 H 已经 Prepare 带了扩展（330）、治理改 enable-height 会 panic（58）、必须协调升级（346）是另外那套，本页不抄。

## 官方为什么这样拆

- **启用之后不能关 not already veheight-switch ≠ 343 / 330 interchangeable：** 官方把时间戳算法锁死和投票扩展启用高度那种切换分开。
- **必须比当前高 not already can-disable ≠ 已经能关 interchangeable：** 官方把必须高于当前高度和已经能改回 0 分开。
- **字段锁死 not already prepare-ext ≠ 已经 Prepare 带了扩展 interchangeable：** 官方把字段锁死和 Prepare 已经带扩展分开；343 pbtsheight vs params bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 启用之后不能关 | 不是 already veheight-switch | 不是到了 H 已经 Prepare 带了扩展 alone（330） |
| 必须比当前高 | 不是 already can-disable | 不是写成 0 就已经启用 alone（782） |
| 字段锁死 | 不是 already prepare-ext | 不是 H 之前仍用 BFT Time alone（783） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看启用之后不能关不是已经是扩展启用高度那种切换 not already veheight-switch / not already can-disable / not already prepare-ext 正式三事（343 余量），必须分开启用之后不能关 是不是 already veheight-switch interchangeable / 343 pbtsheight bundled interchangeable / pbtsheight-sold-as-enabled interchangeable、必须比当前高 是不是 already can-disable interchangeable、字段锁死 是不是 already prepare-ext interchangeable。可以跳过「看见启用之后不能关就已经是扩展启用高度那种切换 interchangeable / 就已经能关 interchangeable / 就已经 Prepare 带了扩展 interchangeable」。不要把字段锁死当已经 Prepare 带了扩展。不要另写怎样设 PbtsEnableHeight。343 pbtsheight vs params bundled unbundling 在本页 item 3 完成（782 + 783 + 784）。

## 本页不抄

- 怎样设 `PbtsEnableHeight`、默认取值、怎样选启用高度。
- PbtsEnableHeight bundled。那是不变量 343。
- 写成 0 不是已经启用 PBTS。那是不变量 343 item 1 余量 / 782。
- H 之前仍用 BFT Time 不是已经切到 PBTS。那是不变量 343 item 2 余量 / 783。
- 到了 H 已经 Prepare 带了扩展。那是不变量 330。
- 治理改 enable-height 会 panic。那是不变量 58。
- 必须协调升级。那是不变量 346。
