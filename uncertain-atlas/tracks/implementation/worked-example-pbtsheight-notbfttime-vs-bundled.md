# 例：看见 H 之前或写成 0 仍用 BFT Time / 看见到了 H 才用 PBTS / 看见还能出合法提案 is not already already switched-to-pbts interchangeable / already mtp interchangeable / already clock-changed interchangeable

**层次**：实现 / H 之前仍用 BFT Time 不是已经切到 PBTS not already switched-to-pbts / not already mtp / not already clock-changed 正式三事（343 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / FeatureParams.PbtsEnableHeight。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「H 之前仍用 BFT Time 不是已经切到 PBTS not already switched-to-pbts / not already mtp / not already clock-changed 正式三事（343 余量）/ not 783 pbtsheight-notbfttime interchangeable / not 343 pbtsheight bundled interchangeable」，不是 PbtsEnableHeight bundled（343），也不是写成 0 不是已经启用 PBTS（782 item 1 余量）或启用之后不能关不是已经是扩展启用高度那种切换（784 item 3 余量）。不要另写怎样设 PbtsEnableHeight。

## 官方三件事

规范把 Requirements 里 H 之前或写成 0 仍用 BFT Time、到了 H 才用 PBTS 和「已经是仍用 BFT Time 就已经切到 PBTS interchangeable / 已经是到了 H 就已经是 MTP interchangeable / 已经是能出合法提案就已经换完钟 interchangeable / 已经是 pbtsheight bundled interchangeable」分开写成三件独立的实现事，不是「看见 H 之前仍用 BFT Time 就已经切到 PBTS interchangeable / 就已经是 MTP interchangeable / 就已经换完钟 interchangeable」一件事：

1. **看见 H 之前或写成 0 仍用 BFT Time / 看见到了 H 才用 PBTS / 看见旧钟还在 is not already 已经切到 PBTS interchangeable / 已经 switched-to-pbts interchangeable / 已经切到 PBTS 交差 interchangeable / 343 pbtsheight bundled interchangeable / 40 block-time interchangeable / pbtsheight-sold-as-enabled interchangeable，也不是已经 PbtsEnableHeight bundled（343） interchangeable / 783 pbtsheight-notbfttime interchangeable / 343 pbtsheight item 2 interchangeable，也不是已经 H 之前仍用 BFT Time 不是已经切到 PBTS not already switched-to-pbts / not already mtp / not already clock-changed 正式三事 bundled（343 item 2 余量） interchangeable / 343 pbtsheight item 2 interchangeable，也不是已经写成 0 不是已经启用（782） interchangeable / 784 pbtsheight-notveheight interchangeable / 330 veheight interchangeable，也不是已经块时间必须点名算法（40） interchangeable。**  
   官方写：到了配置高度，并且之后每一高，才用 PBTS 算法出时间戳、验时间戳。**这一高之前，或这个值是 0**，仍用旧的 BFT Time。看见 H 之前仍用 BFT Time，不是已经 switched-to-pbts interchangeable——343 钉 bundled 三事，本页从 item 2 侧钉 not already switched-to-pbts 单句。看见到了 H 才用 PBTS，不是已经 PbtsEnableHeight bundled（343） interchangeable——343 钉 bundled，本页钉 item 2 第一件事。看见旧钟还在，不是已经块时间必须点名算法（40） interchangeable——40 另钉。343 pbtsheight vs params bundled unbundling 在本页 item 2 续。

2. **看见到了 H / 看见写了用于 PBTS / 看见配置高度到了 is not already 已经是 MTP interchangeable / 已经 mtp interchangeable / 已经中位数时间交差 interchangeable / 343 pbtsheight bundled interchangeable / pbts-sold-as-mtp interchangeable / 40 block-time interchangeable，也不是已经 PbtsEnableHeight bundled（343） interchangeable / 783 pbtsheight-notbfttime interchangeable / 343 pbtsheight item 1 写成 0 interchangeable / 343 pbtsheight item 3 不能关 interchangeable，也不是已经 H 之前仍用 BFT Time 不是已经切到 PBTS not already switched-to-pbts / not already mtp / not already clock-changed 正式三事 bundled（343 item 2 余量） interchangeable / 343 pbtsheight item 2 interchangeable，也不是已经切到 PBTS（本页第一件事） interchangeable。**  
   官方写：看见到了 H，不是已经是中位数时间。看见写了用于 PBTS，不是已经 mtp interchangeable——本页钉 not already mtp 单句。看见配置高度到了，不是已经切到 PBTS（本页第一件事） interchangeable——三件事分开钉。343 pbtsheight vs params bundled unbundling 在本页 item 2 续。

3. **看见还能出合法提案 / 看见仍能出合法提案 / 看见提案时间戳合法 is not already 已经换完钟 interchangeable / 已经 clock-changed interchangeable / 已经换钟交差 interchangeable / 343 pbtsheight bundled interchangeable / 782 pbtsheight-notzero interchangeable，也不是已经 PbtsEnableHeight bundled（343） interchangeable / 783 pbtsheight-notbfttime interchangeable / 343 pbtsheight item 1 / 343 pbtsheight item 3，也不是已经 H 之前仍用 BFT Time 不是已经切到 PBTS not already switched-to-pbts / not already mtp / not already clock-changed 正式三事 bundled（343 item 2 余量） interchangeable / 343 pbtsheight item 2 interchangeable，也不是已经切到 PBTS（本页第一件事） interchangeable / 已经是 MTP（本页第二件事） interchangeable。**  
   官方写：看见还能出合法提案，不是已经换完钟。看见仍能出合法提案，不是已经 clock-changed interchangeable——本页钉 not already clock-changed 单句。看见提案时间戳合法，不是已经是 MTP（本页第二件事） interchangeable——三件事分开钉。343 pbtsheight vs params bundled unbundling 在本页 item 2 续。

怎样设 `PbtsEnableHeight`、默认取值、怎样选启用高度是规范里的做法，本页不抄。PbtsEnableHeight bundled（343）、写成 0 不是已经启用 PBTS（343 item 1 余量 / 782）、启用之后不能关不是已经是扩展启用高度那种切换（343 item 3 余量 / 784）、块时间必须点名算法（40）、到了 H 已经 Prepare 带了扩展（330）、Precision bundled（336）是另外那套，本页不抄。

## 官方为什么这样拆

- **H 之前仍用 BFT Time not already switched-to-pbts ≠ 343 / 40 interchangeable：** 官方把旧钟还在和已经切到 PBTS 分开。
- **到了 H not already mtp ≠ 已经是 MTP interchangeable：** 官方把到了启用高度和已经是中位数时间分开。
- **能出合法提案 not already clock-changed ≠ 已经换完钟 interchangeable：** 官方把还能提案和已经换完钟分开；343 pbtsheight vs params bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| H 之前仍用 BFT Time | 不是 already switched-to-pbts | 不是块时间必须点名算法 alone（40） |
| 到了 H | 不是 already mtp | 不是写成 0 就已经启用 alone（782） |
| 能出合法提案 | 不是 already clock-changed | 不是启用之后不能关 alone（784） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 H 之前仍用 BFT Time 不是已经切到 PBTS not already switched-to-pbts / not already mtp / not already clock-changed 正式三事（343 余量），必须分开 H 之前仍用 BFT Time 是不是 already switched-to-pbts interchangeable / 343 pbtsheight bundled interchangeable / pbtsheight-sold-as-enabled interchangeable、到了 H 是不是 already mtp interchangeable、能出合法提案 是不是 already clock-changed interchangeable。可以跳过「看见 H 之前仍用 BFT Time 就已经切到 PBTS interchangeable / 就已经是 MTP interchangeable / 就已经换完钟 interchangeable」。不要把到了 H 当已经是 MTP。不要另写怎样设 PbtsEnableHeight。343 pbtsheight vs params bundled unbundling 在本页 item 2 续（782 + 783）；续 [`worked-example-pbtsheight-notveheight-vs-bundled.md`](worked-example-pbtsheight-notveheight-vs-bundled.md)（不变量 784 item 3）；完成见 784。

## 本页不抄

- 怎样设 `PbtsEnableHeight`、默认取值、怎样选启用高度。
- PbtsEnableHeight bundled。那是不变量 343。
- 写成 0 不是已经启用 PBTS。那是不变量 343 item 1 余量 / 782。
- 启用之后不能关不是已经是扩展启用高度那种切换。那是不变量 343 item 3 余量 / 784。
- 块时间必须点名算法。那是不变量 40。
- 到了 H 已经 Prepare 带了扩展。那是不变量 330。
- Precision 不是已经是 MessageDelay。那是不变量 336。
