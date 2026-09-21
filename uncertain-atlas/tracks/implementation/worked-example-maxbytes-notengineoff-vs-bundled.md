# 例：看见应用自己卡体积 / 看见 MAY 写成 -1 / 看见 Process 会拒 is not already already engine-off interchangeable / already app-only-cap interchangeable / already no-100mb-ruler interchangeable

**层次**：实现 / 应用自己卡体积不是已经引擎不管了 not already engine-off / not already app-only-cap / not already no-100mb-ruler 正式三事（337 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / BlockParams.MaxBytes。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「应用自己卡体积不是已经引擎不管了 not already engine-off / not already app-only-cap / not already no-100mb-ruler 正式三事（337 余量）/ not 765 maxbytes-notengineoff interchangeable / not 337 maxbytescap bundled interchangeable」，不是 MaxBytes cap bundled（337），也不是 MaxBytes 写成 -1 就按 100 MB 验不是已经没有上限（764 item 1 余量）或必须 -1 或不超过 100 MB 不是已经是默认 21 MB（766 item 3 余量）。不要另写怎样设 MaxBytes 或怎样算块开销。

## 官方三件事

规范把 Requirements 里应用自己卡体积、MAY 写成 -1 和「已经是应用自己卡就已经引擎不管了 interchangeable / 已经是 MAY 写成 -1 就已经只有应用这一把尺 interchangeable / 已经是 Process 会拒就已经没有 100 MB 那把尺 interchangeable / 已经是 maxbytescap bundled interchangeable」分开写成三件独立的实现事，不是「看见应用自己卡体积就已经引擎不管了 interchangeable / 就已经只有应用这一把尺 interchangeable / 就已经没有 100 MB 那把尺 interchangeable」一件事：

1. **看见应用自己卡体积 / 看见应用侧设了字节上限 / 看见 Prepare 卡住回包 is not already 已经引擎不管了 interchangeable / 已经 engine-off interchangeable / 已经引擎关掉交差 interchangeable / 337 maxbytescap bundled interchangeable / 63 maxbytes-sla interchangeable / maxbytescap-sold-as-unlimited interchangeable，也不是已经 MaxBytes cap bundled（337） interchangeable / 765 maxbytes-notengineoff interchangeable / 337 maxbytescap item 2 interchangeable，也不是已经应用自己卡体积不是已经引擎不管了 not already engine-off / not already app-only-cap / not already no-100mb-ruler 正式三事 bundled（337 item 2 余量） interchangeable / 337 maxbytescap item 2 interchangeable，也不是已经 MaxBytes 写成 -1 就按 100 MB 验不是已经没有上限（764） interchangeable / 766 maxbytes-notdefault21 interchangeable / 299 evidence-reap interchangeable，也不是已经仓库默认 MaxBytes 已经是活性 SLA（63） interchangeable。**  
   官方写：应用若要自己管块大小，可在应用侧设字节上限，用 `PrepareProposal` 卡住回包、用 `ProcessProposal` 拒超限块。看见应用自己卡，不是引擎已经不管。看见应用自己卡体积，不是已经 engine-off interchangeable——337 钉 bundled 三事，本页从 item 2 侧钉 not already engine-off 单句。看见应用侧设了字节上限，不是已经 MaxBytes cap bundled（337） interchangeable——337 钉 bundled，本页钉 item 2 第一件事。看见 Prepare 卡住回包，不是已经仓库默认 MaxBytes 已经是活性 SLA（63） interchangeable——63 另钉。337 maxbytescap vs unlimited bundled unbundling 在本页 item 2 续。

2. **看见 MAY 写成 -1 / 看见这时可以写成 -1 / 看见应用自己卡时写 -1 is not already 已经只有应用这一把尺 interchangeable / 已经 app-only-cap interchangeable / 已经只有应用交差 interchangeable / 337 maxbytescap bundled interchangeable / 299 evidence-reap interchangeable，也不是已经 MaxBytes cap bundled（337） interchangeable / 765 maxbytes-notengineoff interchangeable / 337 maxbytescap item 1 没有上限 interchangeable / 337 maxbytescap item 3 默认 21 MB interchangeable，也不是已经应用自己卡体积不是已经引擎不管了 not already engine-off / not already app-only-cap / not already no-100mb-ruler 正式三事 bundled（337 item 2 余量） interchangeable / 337 maxbytescap item 2 interchangeable，也不是已经引擎不管了（本页第一件事） interchangeable。**  
   官方写：这时 **MAY** 把 `MaxBytes` 写成 -1。看见 MAY 写成 -1，不是已经只有应用这一把尺。看见这时可以写成 -1，不是已经 app-only-cap interchangeable——本页钉 not already app-only-cap 单句。看见应用自己卡时写 -1，不是已经引擎不管了（本页第一件事） interchangeable——三件事分开钉。337 maxbytescap vs unlimited bundled unbundling 在本页 item 2 续。

3. **看见 Process 会拒 / 看见 ProcessProposal 拒超限块 / 看见应用会拒超限 is not already 已经没有 100 MB 那把尺 interchangeable / 已经 no-100mb-ruler interchangeable / 已经 100 MB 尺没了交差 interchangeable / 337 maxbytescap bundled interchangeable / 764 maxbytes-notunlimited interchangeable，也不是已经 MaxBytes cap bundled（337） interchangeable / 765 maxbytes-notengineoff interchangeable / 337 maxbytescap item 1 / 337 maxbytescap item 3，也不是已经应用自己卡体积不是已经引擎不管了 not already engine-off / not already app-only-cap / not already no-100mb-ruler 正式三事 bundled（337 item 2 余量） interchangeable / 337 maxbytescap item 2 interchangeable，也不是已经引擎不管了（本页第一件事） interchangeable / 已经只有应用这一把尺（本页第二件事） interchangeable。**  
   官方写：看见 Process 会拒，不是已经只有应用在验，也不是已经没有 100 MB 那把尺。看见 ProcessProposal 拒超限块，不是已经 no-100mb-ruler interchangeable——本页钉 not already no-100mb-ruler 单句。看见应用会拒超限，不是已经只有应用这一把尺（本页第二件事） interchangeable——三件事分开钉。337 maxbytescap vs unlimited bundled unbundling 在本页 item 2 续。

怎样设 `MaxBytes`、100 MB / 21 MB 取值、怎样算头和证据开销是规范里的取值或做法，本页不抄。MaxBytes cap bundled（337）、MaxBytes 写成 -1 就按 100 MB 验不是已经没有上限（337 item 1 余量 / 764）、必须 -1 或不超过 100 MB 不是已经是默认 21 MB（337 item 3 余量 / 766）、整池都给 Prepare 就已经没有上限（299）、仓库默认 MaxBytes 已经是活性 SLA（63）、证据 MaxBytes 已经是块 MaxBytes（331）是另外那套，本页不抄。

## 官方为什么这样拆

- **应用自己卡体积 not already engine-off ≠ 337 / 63 interchangeable：** 官方把应用侧上限和引擎那把 100 MB 尺分开。
- **MAY 写成 -1 not already app-only-cap ≠ 已经只有应用这一把尺 interchangeable：** 官方把 MAY 写成 -1 和已经只有应用分开。
- **Process 会拒 not already no-100mb-ruler ≠ 已经没有 100 MB 那把尺 interchangeable：** 官方把 Process 会拒和 100 MB 尺还在分开；337 maxbytescap vs unlimited bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 应用自己卡体积 | 不是 already engine-off | 不是仓库默认 MaxBytes 已经是活性 SLA alone（63） |
| MAY 写成 -1 | 不是 already app-only-cap | 不是写成 -1 就已经没有上限 alone（764） |
| Process 会拒 | 不是 already no-100mb-ruler | 不是必须 -1 或不超过 100 MB 就已经是默认 21 MB alone（766） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看应用自己卡体积不是已经引擎不管了 not already engine-off / not already app-only-cap / not already no-100mb-ruler 正式三事（337 余量），必须分开应用自己卡体积 是不是 already engine-off interchangeable / 337 maxbytescap bundled interchangeable / maxbytescap-sold-as-unlimited interchangeable、MAY 写成 -1 是不是 already app-only-cap interchangeable、Process 会拒 是不是 already no-100mb-ruler interchangeable。可以跳过「看见应用自己卡体积就已经引擎不管了 interchangeable / 就已经只有应用这一把尺 interchangeable / 就已经没有 100 MB 那把尺 interchangeable」。不要把 100 MB / 21 MB 当不确定常数。不要另写怎样设 MaxBytes 或怎样算块开销。337 maxbytescap vs unlimited bundled unbundling 在本页 item 2 续（764 + 765）；续 [`worked-example-maxbytes-notdefault21-vs-bundled.md`](worked-example-maxbytes-notdefault21-vs-bundled.md)（不变量 766 item 3）已写；完成见 766。

## 本页不抄

- 怎样设 `MaxBytes`、100 MB / 21 MB 取值、怎样算头和证据开销。
- MaxBytes cap bundled。那是不变量 337。
- MaxBytes 写成 -1 就按 100 MB 验不是已经没有上限。那是不变量 337 item 1 余量 / 764。
- 必须 -1 或不超过 100 MB 不是已经是默认 21 MB。那是不变量 337 item 3 余量 / 766。
- 整池都给 Prepare 就已经没有上限。那是不变量 299。
- 仓库默认 MaxBytes 已经是活性 SLA。那是不变量 63。
- 证据 MaxBytes 已经是块 MaxBytes。那是不变量 331。
