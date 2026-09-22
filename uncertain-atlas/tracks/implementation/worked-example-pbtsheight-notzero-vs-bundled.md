# 例：看见写成 0 / 看见大于 0 才是启用高度 / 看见 PbtsEnableHeight is not already already enabled interchangeable / already precision-pbts interchangeable / already switched interchangeable

**层次**：实现 / 写成 0 不是已经启用 PBTS not already enabled / not already precision-pbts / not already switched 正式三事（343 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / FeatureParams.PbtsEnableHeight。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「写成 0 不是已经启用 PBTS not already enabled / not already precision-pbts / not already switched 正式三事（343 余量）/ not 782 pbtsheight-notzero interchangeable / not 343 pbtsheight bundled interchangeable」，不是 PbtsEnableHeight bundled（343），也不是 H 之前仍用 BFT Time 不是已经切到 PBTS（783 item 2 余量）或启用之后不能关不是已经是扩展启用高度那种切换（784 item 3 余量）。不要另写怎样设 PbtsEnableHeight。

## 官方三件事

规范把 Requirements 里 `PbtsEnableHeight` 写成 0 表示关掉、大于 0 才是启用高度 和「已经是写成 0 就已经启用 PBTS interchangeable / 已经是填了 Precision 就已经是 PBTS interchangeable / 已经是字段在就已经切算法 interchangeable / 已经是 pbtsheight bundled interchangeable」分开写成三件独立的实现事，不是「看见写成 0 就已经启用 interchangeable / 就已经填了 Precision 就是 PBTS interchangeable / 就已经切到 PBTS interchangeable」一件事：

1. **看见写成 0 / 看见大于 0 才是启用高度 / 看见 `PbtsEnableHeight` is not already 已经启用 PBTS interchangeable / 已经 enabled interchangeable / 已经启用交差 interchangeable / 343 pbtsheight bundled interchangeable / 762 precision-notpbts interchangeable / pbtsheight-sold-as-enabled interchangeable，也不是已经 PbtsEnableHeight bundled（343） interchangeable / 782 pbtsheight-notzero interchangeable / 343 pbtsheight item 1 interchangeable，也不是已经写成 0 不是已经启用 PBTS not already enabled / not already precision-pbts / not already switched 正式三事 bundled（343 item 1 余量） interchangeable / 343 pbtsheight item 1 interchangeable，也不是已经 H 之前仍用 BFT Time（783） interchangeable / 784 pbtsheight-notveheight interchangeable / 336 precision bundled interchangeable，也不是已经块时间必须点名算法（40） interchangeable。**  
   官方写：`PbtsEnableHeight` 要么是 0，要么是一个正高度。**0 表示 PBTS 关掉**。大于 0 才标出将要（或已经）启用的那一高。看见写成 0，不是已经 enabled interchangeable——343 钉 bundled 三事，本页从 item 1 侧钉 not already enabled 单句。看见大于 0 才是启用高度，不是已经 PbtsEnableHeight bundled（343） interchangeable——343 钉 bundled，本页钉 item 1 第一件事。看见写成 0，不是已经填了两个不是已经启用 PBTS（762） interchangeable——762 另钉 item 2。343 pbtsheight vs params bundled unbundling 在本页 item 1 启动。

2. **看见填了 Precision / 看见填了 MessageDelay / 看见同步参数在 is not already 已经填了 Precision 就是 PBTS interchangeable / 已经 precision-pbts interchangeable / 已经同步参数交差 interchangeable / 343 pbtsheight bundled interchangeable / 761 precision-notmsgdelay interchangeable / precision-sold-as-msgdelay interchangeable，也不是已经 PbtsEnableHeight bundled（343） interchangeable / 782 pbtsheight-notzero interchangeable / 343 pbtsheight item 2 BFT Time interchangeable / 343 pbtsheight item 3 不能关 interchangeable，也不是已经写成 0 不是已经启用 PBTS not already enabled / not already precision-pbts / not already switched 正式三事 bundled（343 item 1 余量） interchangeable / 343 pbtsheight item 1 interchangeable，也不是已经启用 PBTS（本页第一件事） interchangeable。**  
   官方写：看见填了 Precision / MessageDelay，不是已经到了这个高度。看见填了 Precision，不是已经 precision-pbts interchangeable——本页钉 not already precision-pbts 单句。看见同步参数在，不是已经 Precision 不是已经是 MessageDelay（761） interchangeable——761 另钉。看见填了 MessageDelay，不是已经启用 PBTS（本页第一件事） interchangeable——三件事分开钉。343 pbtsheight vs params bundled unbundling 在本页 item 1 启动。

3. **看见字段在 / 看见配置里有 PbtsEnableHeight / 看见 FeatureParams 里有这一栏 is not already 已经切算法 interchangeable / 已经 switched interchangeable / 已经切到 PBTS 交差 interchangeable / 343 pbtsheight bundled interchangeable / 40 block-time interchangeable / pbts-sold-as-mtp interchangeable，也不是已经 PbtsEnableHeight bundled（343） interchangeable / 782 pbtsheight-notzero interchangeable / 343 pbtsheight item 2 / 343 pbtsheight item 3，也不是已经写成 0 不是已经启用 PBTS not already enabled / not already precision-pbts / not already switched 正式三事 bundled（343 item 1 余量） interchangeable / 343 pbtsheight item 1 interchangeable，也不是已经启用 PBTS（本页第一件事） interchangeable / 已经填了 Precision 就是 PBTS（本页第二件事） interchangeable。**  
   官方写：看见字段在，不是已经切算法。看见配置里有 PbtsEnableHeight，不是已经 switched interchangeable——本页钉 not already switched 单句。看见 FeatureParams 里有这一栏，不是已经 H 之前仍用 BFT Time 不是已经切到 PBTS（783） interchangeable——783 另钉 item 2。看见字段在，不是已经填了 Precision 就是 PBTS（本页第二件事） interchangeable——三件事分开钉。343 pbtsheight vs params bundled unbundling 在本页 item 1 启动。

怎样设 `PbtsEnableHeight`、默认取值、怎样选启用高度是规范里的做法，本页不抄。PbtsEnableHeight bundled（343）、H 之前仍用 BFT Time 不是已经切到 PBTS（343 item 2 余量 / 783）、启用之后不能关不是已经是扩展启用高度那种切换（343 item 3 余量 / 784）、Precision bundled（336）、填了两个不是已经启用 PBTS（762）、块时间必须点名算法（40）、到了 H 已经 Prepare 带了扩展（330）是另外那套，本页不抄。

## 官方为什么这样拆

- **写成 0 not already enabled ≠ 343 / 762 interchangeable：** 官方把关掉取值和已经启用 PBTS 分开。
- **填了 Precision not already precision-pbts ≠ 已经填了 Precision 就是 PBTS interchangeable：** 官方把同步参数和 PBTS 启用高度分开。
- **字段在 not already switched ≠ 已经切算法 interchangeable：** 官方把字段在配置里和已经换钟分开；343 pbtsheight vs params bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 写成 0 | 不是 already enabled | 不是填了两个就是 PBTS alone（762） |
| 填了 Precision | 不是 already precision-pbts | 不是 Precision 已经是 MessageDelay alone（761） |
| 字段在 | 不是 already switched | 不是 H 之前仍用 BFT Time alone（783） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看写成 0 不是已经启用 PBTS not already enabled / not already precision-pbts / not already switched 正式三事（343 余量），必须分开写成 0 是不是 already enabled interchangeable / 343 pbtsheight bundled interchangeable / pbtsheight-sold-as-enabled interchangeable、填了 Precision 是不是 already precision-pbts interchangeable、字段在 是不是 already switched interchangeable。可以跳过「看见写成 0 就已经启用 interchangeable / 就已经填了 Precision 就是 PBTS interchangeable / 就已经切到 PBTS interchangeable」。不要把写成 0 当已经切到 PBTS。不要另写怎样设 PbtsEnableHeight。343 pbtsheight vs params bundled unbundling 在本页 item 1 启动；续 [`worked-example-pbtsheight-notbfttime-vs-bundled.md`](worked-example-pbtsheight-notbfttime-vs-bundled.md)（不变量 783 item 2）已写；完成见 784。

## 本页不抄

- 怎样设 `PbtsEnableHeight`、默认取值、怎样选启用高度。
- PbtsEnableHeight bundled。那是不变量 343。
- H 之前仍用 BFT Time 不是已经切到 PBTS。那是不变量 343 item 2 余量 / 783。
- 启用之后不能关不是已经是扩展启用高度那种切换。那是不变量 343 item 3 余量 / 784。
- Precision 不是已经是 MessageDelay。那是不变量 336 / 761。
- 填了两个不是已经启用 PBTS。那是不变量 762。
- 块时间必须点名算法。那是不变量 40。
- 到了 H 已经 Prepare 带了扩展。那是不变量 330。
