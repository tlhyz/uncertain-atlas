# 例：看见必须 -1 或不超过 100 MB is not already default-21 interchangeable / not already bandwidth-evaluated interchangeable / not already settled interchangeable

**层次**：实现 / 必须 -1 或不超过 100 MB not already default-21 / not already bandwidth-evaluated / not already settled 正式三事（337 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / BlockParams.MaxBytes。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、mempool。本页是「必须 -1 或不超过 100 MB not already default-21 / not already bandwidth-evaluated / not already settled 正式三事（337 余量）/ not 919 maxbytes-cap-not21 interchangeable / not 337 maxbytes-cap-vs-unlimited bundled interchangeable」，不是上限 bundled（337），也不是证据 MaxBytes 已经是块 MaxBytes（331），也不是 timeout 必须按满块投递延迟算就已经装得下（344/883）。不要另写怎样设 MaxBytes 或怎样算块开销。

## 官方三件事

1. **看见必须 MaxBytes == -1 或 0 < MaxBytes <= 100 MB / 看见默认能接到 21 MB 这份范围 is not already 已经是默认 21 MB interchangeable，也不是已经上限 bundled（337） interchangeable / 919 maxbytes-cap-not21 interchangeable / 917 maxbytes-cap-notunlim interchangeable / 337 maxbytes-cap item 1 -1 就按 100 MB 验 interchangeable，也不是已经必须 -1 或不超过 100 MB not already default-21 / not already bandwidth-evaluated / not already settled 正式三事 bundled（337 item 3 余量） interchangeable / 337 maxbytes-cap item 3 interchangeable。**  
   官方写：合法取值只能是 -1，或大于 0 且不超过 100 MB。默认值把最大 21 MB 的块当成合法。看见合法范围，不是已经是默认那档 interchangeable——本页从 337 item 3 侧钉 not already default-21 单句。337 maxbytes-cap vs unlimited bundled unbundling 在本页 item 3 完成。

2. **看见默认能接到 21 MB / 看见建议下调 / 这份范围 is not already 已经评估过带宽 interchangeable，也不是已经上限 bundled（337） interchangeable / 919 maxbytes-cap-not21 interchangeable / 337 maxbytes-cap item 2 应用自己卡 interchangeable / 918 maxbytes-cap-notapp interchangeable，也不是已经证据 MaxBytes 已经是块 MaxBytes interchangeable / 331 evidence-maxbytes interchangeable。**  
   官方把默认能接到 21 MB 和已经对照过 timeout_propose / 已经评估过传播带宽和延迟分开——337 bundled 第三件事常与 331 混成「看见合法范围就已经是默认 21 MB 或已经是证据那把尺 interchangeable」，本页钉 not already bandwidth-evaluated 单句。

3. **看见建议下调 / 看见合法范围 / 这份范围 is not already 已经交差 interchangeable，也不是已经上限 bundled（337） interchangeable / 919 maxbytes-cap-not21 interchangeable / 917 maxbytes-cap-notunlim interchangeable，也不是已经 timeout 必须按满块投递延迟算就已经装得下 interchangeable / 344/883 maxbytes-overhead-nottimeout interchangeable。**  
   官方把建议下调和已经下调 / 已经交差分开。看见建议下调，不是已经交差 interchangeable。337 maxbytes-cap vs unlimited bundled unbundling 在本页 item 3 完成。

怎样设 MaxBytes、100 MB / 21 MB 取值、怎样算头和证据开销是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **必须 -1 或不超过 100 MB not already default-21 ≠ 已经是默认 21 MB interchangeable：** 官方把合法范围和默认 21 MB 分开。
- **看见默认能接到 21 MB not already bandwidth-evaluated ≠ 已经评估过带宽 interchangeable：** 官方把默认能接到 21 MB 和已经对照过 timeout_propose 分开。
- **看见建议下调 not already settled ≠ 已经交差 interchangeable：** 官方把建议下调和已经下调 / 已经交差分开；337 maxbytes-cap vs unlimited bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 必须 -1 或不超过 100 MB | 不是已经是默认 21 MB | 不是证据 MaxBytes 已经是块 MaxBytes（331） |
| 看见默认能接到 21 MB | 不是已经评估过带宽 | 不是 timeout 必须按满块投递延迟算就已经装得下（344/883） |
| 看见建议下调 | 不是已经交差 | 不是 -1 就已经没有上限（917） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看必须 -1 或不超过 100 MB not already default-21 / not already bandwidth-evaluated / not already settled 正式三事（337 余量），必须分开是不是已经是默认 21 MB、是不是已经评估过带宽、是不是已经交差。可以跳过「看见合法范围就已经是默认 21 MB」。不要把 100 MB / 21 MB 当不确定常数。不要另写怎样设 MaxBytes 或怎样算块开销。337 maxbytes-cap vs unlimited bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样设 MaxBytes、100 MB / 21 MB 取值、怎样算头和证据开销。
- 上限 bundled。那是不变量 337。
- -1 就已经没有上限。那是不变量 337 item 1 余量 / 917。
- 证据 MaxBytes 已经是块 MaxBytes。那是不变量 331。
- timeout 必须按满块投递延迟算就已经装得下。那是不变量 344/883。
