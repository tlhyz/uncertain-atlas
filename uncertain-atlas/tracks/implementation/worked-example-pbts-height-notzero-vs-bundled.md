# 例：看见写成 0 不是已经启用 PBTS is not already Precision is PBTS interchangeable / not already field-present interchangeable / not already settled interchangeable

**层次**：实现 / 写成 0 不是已经启用 PBTS not already Precision is PBTS / not already field-present / not already settled 正式三事（343 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / FeatureParams.PbtsEnableHeight。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「写成 0 不是已经启用 PBTS not already Precision is PBTS / not already field-present / not already settled 正式三事（343 余量）/ not 884 pbts-height-notzero interchangeable / not 343 pbts-height-vs-params bundled interchangeable」，不是 PbtsEnableHeight bundled（343），也不是 Precision 已经是 MessageDelay（336），也不是到了 H 已经 Prepare 带了扩展（330）。不要另写怎样设 PbtsEnableHeight。

## 官方三件事

1. **看见写成 0 / 看见大于 0 才是启用高度 这份 0 is not already 已经启用 PBTS interchangeable，也不是已经 PbtsEnableHeight bundled（343） interchangeable / 884 pbts-height-notzero interchangeable / 885 pbts-height-notbft interchangeable / 343 pbts item 2 BFT Time interchangeable，也不是已经写成 0 不是已经启用 PBTS not already Precision is PBTS / not already field-present / not already settled 正式三事 bundled（343 item 1 余量） interchangeable / 343 pbts item 1 interchangeable。**  
   官方写：`PbtsEnableHeight` 要么是 0，要么是一个正高度。0 表示 PBTS 关掉。大于 0 才标出将要（或已经）启用的那一高。看见写成 0，不是已经启用 interchangeable——本页从 343 item 1 侧钉 not already enabled 单句。343 pbts vs params bundled unbundling 在本页 item 1 启动。

2. **看见填了 Precision / MessageDelay / 这份 0 is not already 已经填了 Precision 就是 PBTS interchangeable，也不是已经 PbtsEnableHeight bundled（343） interchangeable / 884 pbts-height-notzero interchangeable / 343 pbts item 3 不能关 interchangeable / 886 pbts-height-notlock interchangeable，也不是已经 Precision 已经是 MessageDelay interchangeable / 336 precision interchangeable。**  
   官方把填了 Precision / MessageDelay 和已经到了这个高度分开——343 bundled 第一件事常与 336 混成「看见填了同步参数就已经启用或已经是 Precision=MessageDelay interchangeable」，本页钉 not already Precision is PBTS 单句。

3. **看见字段在 / 看见写成 0 / 这份 0 is not already 已经交差 interchangeable，也不是已经 PbtsEnableHeight bundled（343） interchangeable / 884 pbts-height-notzero interchangeable / 885 pbts-height-notbft interchangeable，也不是已经到了 H 已经 Prepare 带了扩展 interchangeable / 330 height-H interchangeable。**  
   官方把字段在和已经切算法 / 已经交差分开。看见字段在，不是已经切算法 interchangeable。343 pbts vs params bundled unbundling 在本页 item 1 启动。

怎样设 `PbtsEnableHeight`、默认取值、怎样选启用高度是规范里的做法，本页不抄。

## 官方为什么这样拆

- **写成 0 不是已经启用 PBTS not already enabled ≠ 已经启用 PBTS interchangeable：** 官方把关掉取值和已经启用分开。
- **看见填了 Precision not already Precision is PBTS ≠ 已经填了 Precision 就是 PBTS interchangeable：** 官方把同步参数两把尺和已经启用分开。
- **看见字段在 not already settled ≠ 已经交差 interchangeable：** 官方把字段在和已经交差分开；343 pbts vs params bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 写成 0 不是已经启用 PBTS | 不是已经填了 Precision 就是 PBTS | 不是 Precision 已经是 MessageDelay（336） |
| 看见填了 Precision | 不是已经到了这个高度 | 不是到了 H 已经 Prepare 带了扩展（330） |
| 看见字段在 | 不是已经交差 | 不是 H 之前仍用 BFT Time（885） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看写成 0 不是已经启用 PBTS not already Precision is PBTS / not already field-present / not already settled 正式三事（343 余量），必须分开是不是已经启用、是不是已经填了 Precision 就是 PBTS、是不是已经交差。可以跳过「看见填了同步参数就已经启用」。不要把写成 0 当已经切到 PBTS。不要另写怎样设 PbtsEnableHeight。343 pbts vs params bundled unbundling 在本页 item 1 启动；续 [`worked-example-pbts-height-notbft-vs-bundled.md`](worked-example-pbts-height-notbft-vs-bundled.md)（不变量 885 item 2）。

## 本页不抄

- 怎样设 `PbtsEnableHeight`、默认取值、怎样选启用高度。
- PbtsEnableHeight bundled。那是不变量 343。
- H 之前仍用 BFT Time。那是不变量 343 item 2 余量 / 885。
- Precision 已经是 MessageDelay。那是不变量 336。
- 到了 H 已经 Prepare 带了扩展。那是不变量 330。
