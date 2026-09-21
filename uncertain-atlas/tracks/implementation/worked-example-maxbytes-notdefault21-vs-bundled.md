# 例：看见必须 -1 或不超过 100 MB / 看见默认能接到 21 MB / 看见建议下调 is not already already default-21 interchangeable / already bandwidth-assessed interchangeable / already tuned-down interchangeable

**层次**：实现 / 必须 -1 或不超过 100 MB 不是已经是默认 21 MB not already default-21 / not already bandwidth-assessed / not already tuned-down 正式三事（337 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / BlockParams.MaxBytes。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「必须 -1 或不超过 100 MB 不是已经是默认 21 MB not already default-21 / not already bandwidth-assessed / not already tuned-down 正式三事（337 余量）/ not 766 maxbytes-notdefault21 interchangeable / not 337 maxbytescap bundled interchangeable」，不是 MaxBytes cap bundled（337），也不是 MaxBytes 写成 -1 就按 100 MB 验不是已经没有上限（764 item 1 余量）或应用自己卡体积不是已经引擎不管了（765 item 2 余量）。不要另写怎样设 MaxBytes 或怎样算块开销。

## 官方三件事

规范把 Requirements 里合法取值范围、默认能接到 21 MB 和「已经是合法范围就已经是默认 21 MB interchangeable / 已经是默认能接到 21 MB 就已经评估过带宽 interchangeable / 已经是建议下调就已经下调 interchangeable / 已经是 maxbytescap bundled interchangeable」分开写成三件独立的实现事，不是「看见必须 -1 或不超过 100 MB 就已经是默认 21 MB interchangeable / 就已经评估过带宽 interchangeable / 就已经下调 interchangeable」一件事：

1. **看见必须 MaxBytes == -1 或 0 < MaxBytes <= 100 MB / 看见合法取值范围 / 看见合法范围那一档 is not already 已经是默认 21 MB interchangeable / 已经 default-21 interchangeable / 已经默认那档交差 interchangeable / 337 maxbytescap bundled interchangeable / 63 maxbytes-sla interchangeable / maxbytescap-sold-as-unlimited interchangeable，也不是已经 MaxBytes cap bundled（337） interchangeable / 766 maxbytes-notdefault21 interchangeable / 337 maxbytescap item 3 interchangeable，也不是已经必须 -1 或不超过 100 MB 不是已经是默认 21 MB not already default-21 / not already bandwidth-assessed / not already tuned-down 正式三事 bundled（337 item 3 余量） interchangeable / 337 maxbytescap item 3 interchangeable，也不是已经 MaxBytes 写成 -1 就按 100 MB 验不是已经没有上限（764） interchangeable / 765 maxbytes-notengineoff interchangeable / 331 evidencemaxbytes interchangeable，也不是已经仓库默认 MaxBytes 已经是活性 SLA（63） interchangeable。**  
   官方写：合法取值只能是 -1，或大于 0 且不超过 100 MB。看见合法范围，不是已经是默认那档。看见必须 -1 或不超过 100 MB，不是已经 default-21 interchangeable——337 钉 bundled 三事，本页从 item 3 侧钉 not already default-21 单句。看见合法取值范围，不是已经 MaxBytes cap bundled（337） interchangeable——337 钉 bundled，本页钉 item 3 第一件事。看见合法范围，不是已经仓库默认 MaxBytes 已经是活性 SLA（63） interchangeable——63 另钉。337 maxbytescap vs unlimited bundled unbundling 在本页 item 3 完成。

2. **看见默认能接到 21 MB / 看见默认值把最大 21 MB 当成合法 / 看见默认 21 MB is not already 已经评估过带宽 interchangeable / 已经 bandwidth-assessed interchangeable / 已经对照过 timeout_propose 交差 interchangeable / 337 maxbytescap bundled interchangeable / 63 maxbytes-sla interchangeable，也不是已经 MaxBytes cap bundled（337） interchangeable / 766 maxbytes-notdefault21 interchangeable / 337 maxbytescap item 1 没有上限 interchangeable / 337 maxbytescap item 2 引擎不管 interchangeable，也不是已经必须 -1 或不超过 100 MB 不是已经是默认 21 MB not already default-21 / not already bandwidth-assessed / not already tuned-down 正式三事 bundled（337 item 3 余量） interchangeable / 337 maxbytescap item 3 interchangeable，也不是已经是默认 21 MB（本页第一件事） interchangeable。**  
   官方写：看见默认能接到 21 MB，不是已经对照过 `timeout_propose`，也不是已经评估过传播带宽和延迟。看见默认值把最大 21 MB 当成合法，不是已经 bandwidth-assessed interchangeable——本页钉 not already bandwidth-assessed 单句。看见默认 21 MB，不是已经是默认那档（本页第一件事） interchangeable——三件事分开钉。337 maxbytescap vs unlimited bundled unbundling 在本页 item 3 完成。

3. **看见建议下调 / 看见强烈建议把默认往下调 / 看见建议调小 is not already 已经下调 interchangeable / 已经 tuned-down interchangeable / 已经调小交差 interchangeable / 337 maxbytescap bundled interchangeable / 63 maxbytes-sla interchangeable，也不是已经 MaxBytes cap bundled（337） interchangeable / 766 maxbytes-notdefault21 interchangeable / 337 maxbytescap item 1 / 337 maxbytescap item 2，也不是已经必须 -1 或不超过 100 MB 不是已经是默认 21 MB not already default-21 / not already bandwidth-assessed / not already tuned-down 正式三事 bundled（337 item 3 余量） interchangeable / 337 maxbytescap item 3 interchangeable，也不是已经是默认 21 MB（本页第一件事） interchangeable / 已经评估过带宽（本页第二件事） interchangeable。**  
   官方写：看见建议下调，不是已经下调。看见强烈建议把默认往下调，不是已经 tuned-down interchangeable——本页钉 not already tuned-down 单句。看见建议调小，不是已经评估过带宽（本页第二件事） interchangeable——三件事分开钉。337 maxbytescap vs unlimited bundled unbundling 在本页 item 3 完成。

怎样设 `MaxBytes`、100 MB / 21 MB 取值、怎样算头和证据开销是规范里的取值或做法，本页不抄。MaxBytes cap bundled（337）、MaxBytes 写成 -1 就按 100 MB 验不是已经没有上限（337 item 1 余量 / 764）、应用自己卡体积不是已经引擎不管了（337 item 2 余量 / 765）、整池都给 Prepare 就已经没有上限（299）、仓库默认 MaxBytes 已经是活性 SLA（63）、证据 MaxBytes 已经是块 MaxBytes（331）是另外那套，本页不抄。

## 官方为什么这样拆

- **合法范围 not already default-21 ≠ 337 / 63 interchangeable：** 官方把合法范围和默认 21 MB 分开。
- **默认能接到 21 MB not already bandwidth-assessed ≠ 已经评估过带宽 interchangeable：** 官方把默认能接到和已经评估过带宽、已经对照 timeout_propose 分开。
- **建议下调 not already tuned-down ≠ 已经下调 interchangeable：** 官方把建议下调和已经下调分开；337 maxbytescap vs unlimited bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 合法范围 | 不是 already default-21 | 不是仓库默认 MaxBytes 已经是活性 SLA alone（63） |
| 默认能接到 21 MB | 不是 already bandwidth-assessed | 不是应用自己卡就已经引擎不管了 alone（765） |
| 建议下调 | 不是 already tuned-down | 不是写成 -1 就已经没有上限 alone（764） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看必须 -1 或不超过 100 MB 不是已经是默认 21 MB not already default-21 / not already bandwidth-assessed / not already tuned-down 正式三事（337 余量），必须分开合法范围 是不是 already default-21 interchangeable / 337 maxbytescap bundled interchangeable / maxbytescap-sold-as-unlimited interchangeable、默认能接到 21 MB 是不是 already bandwidth-assessed interchangeable、建议下调 是不是 already tuned-down interchangeable。可以跳过「看见必须 -1 或不超过 100 MB 就已经是默认 21 MB interchangeable / 就已经评估过带宽 interchangeable / 就已经下调 interchangeable」。不要把 100 MB / 21 MB 当不确定常数。不要另写怎样设 MaxBytes 或怎样算块开销。337 maxbytescap vs unlimited bundled unbundling 在本页 item 3 完成（764 + 765 + 766）。

## 本页不抄

- 怎样设 `MaxBytes`、100 MB / 21 MB 取值、怎样算头和证据开销。
- MaxBytes cap bundled。那是不变量 337。
- MaxBytes 写成 -1 就按 100 MB 验不是已经没有上限。那是不变量 337 item 1 余量 / 764。
- 应用自己卡体积不是已经引擎不管了。那是不变量 337 item 2 余量 / 765。
- 整池都给 Prepare 就已经没有上限。那是不变量 299。
- 仓库默认 MaxBytes 已经是活性 SLA。那是不变量 63。
- 证据 MaxBytes 已经是块 MaxBytes。那是不变量 331。
