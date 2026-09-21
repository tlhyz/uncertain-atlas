# 例：看见 MaxBytes 写成 -1 / 看见引擎按 100 MB 验 / 看见能打满 is not already already unlimited interchangeable / already no-cap interchangeable / already free-return interchangeable

**层次**：实现 / MaxBytes 写成 -1 就按 100 MB 验不是已经没有上限 not already unlimited / not already no-cap / not already free-return 正式三事（337 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / BlockParams.MaxBytes。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「MaxBytes 写成 -1 就按 100 MB 验不是已经没有上限 not already unlimited / not already no-cap / not already free-return 正式三事（337 余量）/ not 764 maxbytes-notunlimited interchangeable / not 337 maxbytescap bundled interchangeable」，不是 MaxBytes cap bundled（337），也不是应用自己卡体积不是已经引擎不管了（765 item 2 余量）或必须 -1 或不超过 100 MB 不是已经是默认 21 MB（766 item 3 余量）。不要另写怎样设 MaxBytes 或怎样算块开销。

## 官方三件事

规范把 Requirements 里 `MaxBytes` 写成 -1、引擎按 100 MB 验 和「已经是写成 -1 就已经没有上限 interchangeable / 已经是按 100 MB 验就已经没有引擎帽 interchangeable / 已经是能打满就已经可以随便回 interchangeable / 已经是 maxbytescap bundled interchangeable」分开写成三件独立的实现事，不是「看见写成 -1 就已经没有上限 interchangeable / 就已经没有引擎帽 interchangeable / 就已经可以随便回 interchangeable」一件事：

1. **看见 MaxBytes 写成 -1 / 看见写成 -1 / 看见 -1 那一档 is not already 已经没有上限 interchangeable / 已经 unlimited interchangeable / 已经无上限交差 interchangeable / 337 maxbytescap bundled interchangeable / 299 evidence-reap interchangeable / maxbytescap-sold-as-unlimited interchangeable，也不是已经 MaxBytes cap bundled（337） interchangeable / 764 maxbytes-notunlimited interchangeable / 337 maxbytescap item 1 interchangeable，也不是已经 MaxBytes 写成 -1 就按 100 MB 验不是已经没有上限 not already unlimited / not already no-cap / not already free-return 正式三事 bundled（337 item 1 余量） interchangeable / 337 maxbytescap item 1 interchangeable，也不是已经应用自己卡体积不是已经引擎不管了（765） interchangeable / 766 maxbytes-notdefault21 interchangeable / 63 maxbytes-sla interchangeable，也不是已经整池都给 Prepare 就已经没有上限（299） interchangeable。**  
   官方写：应用若写成 -1，共识会把**实际要验的值**当成 100 MB。看见写成 -1，不是已经 unlimited interchangeable——337 钉 bundled 三事，本页从 item 1 侧钉 not already unlimited 单句。看见写成 -1，不是已经 MaxBytes cap bundled（337） interchangeable——337 钉 bundled，本页钉 item 1 第一件事。看见写成 -1，不是已经整池都给 Prepare 就已经没有上限（299） interchangeable——299 另钉。337 maxbytescap vs unlimited bundled unbundling 在本页 item 1 启动。

2. **看见引擎按 100 MB 验 / 看见实际要验的值是 100 MB / 看见 100 MB 那把尺 is not already 已经没有引擎帽 interchangeable / 已经 no-cap interchangeable / 已经帽没了交差 interchangeable / 337 maxbytescap bundled interchangeable / 299 evidence-reap interchangeable，也不是已经 MaxBytes cap bundled（337） interchangeable / 764 maxbytes-notunlimited interchangeable / 337 maxbytescap item 2 引擎不管 interchangeable / 337 maxbytescap item 3 默认 21 MB interchangeable，也不是已经 MaxBytes 写成 -1 就按 100 MB 验不是已经没有上限 not already unlimited / not already no-cap / not already free-return 正式三事 bundled（337 item 1 余量） interchangeable / 337 maxbytescap item 1 interchangeable，也不是已经没有上限（本页第一件事） interchangeable。**  
   官方写：看见按 100 MB 验，不是已经和「整池都给 Prepare、应用仍不得超过 MaxTxBytes」同一句。看见引擎按 100 MB 验，不是已经 no-cap interchangeable——本页钉 not already no-cap 单句。看见 100 MB 那把尺，不是已经没有上限（本页第一件事） interchangeable——三件事分开钉。337 maxbytescap vs unlimited bundled unbundling 在本页 item 1 启动。

3. **看见能打满 / 看见应用已经可以随便回的联想 / 看见整池都给了 Prepare is not already 已经可以随便回 interchangeable / 已经 free-return interchangeable / 已经随便交差 interchangeable / 337 maxbytescap bundled interchangeable / 299 evidence-reap interchangeable，也不是已经 MaxBytes cap bundled（337） interchangeable / 764 maxbytes-notunlimited interchangeable / 337 maxbytescap item 2 / 337 maxbytescap item 3，也不是已经 MaxBytes 写成 -1 就按 100 MB 验不是已经没有上限 not already unlimited / not already no-cap / not already free-return 正式三事 bundled（337 item 1 余量） interchangeable / 337 maxbytescap item 1 interchangeable，也不是已经没有上限（本页第一件事） interchangeable / 已经没有引擎帽（本页第二件事） interchangeable。**  
   官方写：看见能打满，不是已经交差。看见应用已经可以随便回的联想，不是已经 free-return interchangeable——本页钉 not already free-return 单句。看见整池都给了 Prepare，不是已经整池都给 Prepare 就已经没有上限（299） interchangeable——299 另钉。看见能打满，不是已经没有引擎帽（本页第二件事） interchangeable——三件事分开钉。337 maxbytescap vs unlimited bundled unbundling 在本页 item 1 启动。

怎样设 `MaxBytes`、100 MB / 21 MB 取值、怎样算头和证据开销是规范里的取值或做法，本页不抄。MaxBytes cap bundled（337）、应用自己卡体积不是已经引擎不管了（337 item 2 余量 / 765）、必须 -1 或不超过 100 MB 不是已经是默认 21 MB（337 item 3 余量 / 766）、整池都给 Prepare 就已经没有上限（299）、仓库默认 MaxBytes 已经是活性 SLA（63）、证据 MaxBytes 已经是块 MaxBytes（331）是另外那套，本页不抄。

## 官方为什么这样拆

- **写成 -1 not already unlimited ≠ 337 / 299 interchangeable：** 官方把 -1 和引擎仍按 100 MB 验分开。
- **按 100 MB 验 not already no-cap ≠ 已经没有引擎帽 interchangeable：** 官方把 100 MB 那把尺和帽没了分开。
- **能打满 not already free-return ≠ 已经可以随便回 interchangeable：** 官方把能打满和已经可以随便回分开；337 maxbytescap vs unlimited bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 写成 -1 | 不是 already unlimited | 不是整池都给 Prepare 就已经没有上限 alone（299） |
| 按 100 MB 验 | 不是 already no-cap | 不是仓库默认 MaxBytes 已经是活性 SLA alone（63） |
| 能打满 | 不是 already free-return | 不是证据 MaxBytes 已经是块 MaxBytes alone（331） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 MaxBytes 写成 -1 就按 100 MB 验不是已经没有上限 not already unlimited / not already no-cap / not already free-return 正式三事（337 余量），必须分开写成 -1 是不是 already unlimited interchangeable / 337 maxbytescap bundled interchangeable / maxbytescap-sold-as-unlimited interchangeable、按 100 MB 验 是不是 already no-cap interchangeable、能打满 是不是 already free-return interchangeable。可以跳过「看见写成 -1 就已经没有上限 interchangeable / 就已经没有引擎帽 interchangeable / 就已经可以随便回 interchangeable」。不要把 100 MB / 21 MB 当不确定常数。不要另写怎样设 MaxBytes 或怎样算块开销。337 maxbytescap vs unlimited bundled unbundling 在本页 item 1 启动；续 [`worked-example-maxbytes-notengineoff-vs-bundled.md`](worked-example-maxbytes-notengineoff-vs-bundled.md)（不变量 765 item 2）已写；完成见 766。

## 本页不抄

- 怎样设 `MaxBytes`、100 MB / 21 MB 取值、怎样算头和证据开销。
- MaxBytes cap bundled。那是不变量 337。
- 应用自己卡体积不是已经引擎不管了。那是不变量 337 item 2 余量 / 765。
- 必须 -1 或不超过 100 MB 不是已经是默认 21 MB。那是不变量 337 item 3 余量 / 766。
- 整池都给 Prepare 就已经没有上限。那是不变量 299。
- 仓库默认 MaxBytes 已经是活性 SLA。那是不变量 63。
- 证据 MaxBytes 已经是块 MaxBytes。那是不变量 331。
