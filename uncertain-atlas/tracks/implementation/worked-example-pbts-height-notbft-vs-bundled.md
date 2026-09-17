# 例：看见 H 之前仍用 BFT Time is not already switched to PBTS interchangeable / not already MTP interchangeable / not already settled interchangeable

**层次**：实现 / H 之前仍用 BFT Time not already switched to PBTS / not already MTP / not already settled 正式三事（343 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / FeatureParams.PbtsEnableHeight。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「H 之前仍用 BFT Time not already switched to PBTS / not already MTP / not already settled 正式三事（343 余量）/ not 885 pbts-height-notbft interchangeable / not 343 pbts-height-vs-params bundled interchangeable」，不是 PbtsEnableHeight bundled（343），也不是块时间必须点名算法（40），也不是到了 H 已经 Prepare 带了扩展（330）。不要另写怎样设 PbtsEnableHeight。

## 官方三件事

1. **看见 H 之前或写成 0 仍用 BFT Time / 看见到了 H 才用 PBTS 这份旧钟 is not already 已经切到 PBTS interchangeable，也不是已经 PbtsEnableHeight bundled（343） interchangeable / 885 pbts-height-notbft interchangeable / 884 pbts-height-notzero interchangeable / 343 pbts item 1 写成 0 interchangeable，也不是已经 H 之前仍用 BFT Time not already switched to PBTS / not already MTP / not already settled 正式三事 bundled（343 item 2 余量） interchangeable / 343 pbts item 2 interchangeable。**  
   官方写：到了配置高度，并且之后每一高，才用 PBTS 算法出时间戳、验时间戳。这一高之前，或这个值是 0，仍用旧的 BFT Time。看见写了用于 PBTS，不是已经切了 interchangeable——本页从 343 item 2 侧钉 not already switched to PBTS 单句。343 pbts vs params bundled unbundling 在本页 item 2 续。

2. **看见到了 H / 看见还能出合法提案 / 这份旧钟 is not already 已经是 MTP interchangeable，也不是已经 PbtsEnableHeight bundled（343） interchangeable / 885 pbts-height-notbft interchangeable / 343 pbts item 3 不能关 interchangeable / 886 pbts-height-notlock interchangeable，也不是已经块时间必须点名算法 interchangeable / 40 named-clock interchangeable。**  
   官方把到了 H 和已经是中位数时间分开——343 bundled 第二件事常与 40 混成「看见写了用于 PBTS 就已经切了或已经是 MTP interchangeable」，本页钉 not already MTP 单句。

3. **看见还能出合法提案 / 看见写了用于 PBTS / 这份旧钟 is not already 已经交差 interchangeable，也不是已经 PbtsEnableHeight bundled（343） interchangeable / 885 pbts-height-notbft interchangeable / 884 pbts-height-notzero interchangeable，也不是已经到了 H 已经 Prepare 带了扩展 interchangeable / 330 height-H interchangeable。**  
   官方把还能出合法提案和已经换完钟 / 已经交差分开。看见还能出合法提案，不是已经换完钟 interchangeable。343 pbts vs params bundled unbundling 在本页 item 2 续。

怎样设 `PbtsEnableHeight`、默认取值、怎样选启用高度是规范里的做法，本页不抄。

## 官方为什么这样拆

- **H 之前仍用 BFT Time not already switched to PBTS ≠ 已经切到 PBTS interchangeable：** 官方把旧钟和新钟哪一高换分开。
- **看见到了 H not already MTP ≠ 已经是 MTP interchangeable：** 官方把到了 H 和已经是中位数时间分开。
- **看见还能出合法提案 not already settled ≠ 已经交差 interchangeable：** 官方把还能出合法提案和已经交差分开；343 pbts vs params bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| H 之前仍用 BFT Time | 不是已经切到 PBTS | 不是块时间必须点名算法（40） |
| 看见到了 H | 不是已经是 MTP | 不是到了 H 已经 Prepare 带了扩展（330） |
| 看见还能出合法提案 | 不是已经交差 | 不是写成 0 就已经启用（884） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 H 之前仍用 BFT Time not already switched to PBTS / not already MTP / not already settled 正式三事（343 余量），必须分开是不是已经切到 PBTS、是不是已经是 MTP、是不是已经交差。可以跳过「看见写了用于 PBTS 就已经切了」。不要另写怎样设 PbtsEnableHeight。343 pbts vs params bundled unbundling 在本页 item 2 续；续 [`worked-example-pbts-height-notlock-vs-bundled.md`](worked-example-pbts-height-notlock-vs-bundled.md)（不变量 886 item 3）。

## 本页不抄

- 怎样设 `PbtsEnableHeight`、默认取值、怎样选启用高度。
- PbtsEnableHeight bundled。那是不变量 343。
- 写成 0 不是已经启用 PBTS。那是不变量 343 item 1 余量 / 884。
- 块时间必须点名算法。那是不变量 40。
- 到了 H 已经 Prepare 带了扩展。那是不变量 330。
