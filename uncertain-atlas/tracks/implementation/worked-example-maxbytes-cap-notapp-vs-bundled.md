# 例：看见应用自己卡体积 is not already engine-off interchangeable / not already only-app-ruler interchangeable / not already settled interchangeable

**层次**：实现 / 应用自己卡体积 not already engine-off / not already only-app-ruler / not already settled 正式三事（337 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / BlockParams.MaxBytes。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、mempool。本页是「应用自己卡体积 not already engine-off / not already only-app-ruler / not already settled 正式三事（337 余量）/ not 918 maxbytes-cap-notapp interchangeable / not 337 maxbytes-cap-vs-unlimited bundled interchangeable」，不是上限 bundled（337），也不是仓库默认 MaxBytes 已经是活性 SLA（63），也不是头和证据开销已经从 MaxBytes 扣完（344）。不要另写怎样设 MaxBytes 或怎样算块开销。

## 官方三件事

1. **看见应用自己卡体积 / 看见 MAY 写成 -1 这份尺 is not already 已经引擎不管了 interchangeable，也不是已经上限 bundled（337） interchangeable / 918 maxbytes-cap-notapp interchangeable / 917 maxbytes-cap-notunlim interchangeable / 337 maxbytes-cap item 1 -1 就按 100 MB 验 interchangeable，也不是已经应用自己卡体积 not already engine-off / not already only-app-ruler / not already settled 正式三事 bundled（337 item 2 余量） interchangeable / 337 maxbytes-cap item 2 interchangeable。**  
   官方写：应用若要自己管块大小，可在应用侧设字节上限，用 PrepareProposal 卡住回包、用 ProcessProposal 拒超限块，这时 MAY 把 MaxBytes 写成 -1。看见应用自己卡，不是引擎已经不管 interchangeable——本页从 337 item 2 侧钉 not already engine-off 单句。337 maxbytes-cap vs unlimited bundled unbundling 在本页 item 2 续。

2. **看见 MAY 写成 -1 / 看见 Process 会拒 / 这份尺 is not already 已经只有应用这一把尺 interchangeable，也不是已经上限 bundled（337） interchangeable / 918 maxbytes-cap-notapp interchangeable / 337 maxbytes-cap item 3 合法范围 interchangeable / 919 maxbytes-cap-not21 interchangeable，也不是已经仓库默认 MaxBytes 已经是活性 SLA interchangeable / 63 maxbytes-sla interchangeable。**  
   官方把 MAY 写成 -1 和已经没有 100 MB 那把尺分开——337 bundled 第二件事常与 63 混成「看见应用自己卡就已经引擎不管或已经是默认 SLA interchangeable」，本页钉 not already only-app-ruler 单句。

3. **看见 Process 会拒 / 看见应用自己卡 / 这份尺 is not already 已经交差 interchangeable，也不是已经上限 bundled（337） interchangeable / 918 maxbytes-cap-notapp interchangeable / 917 maxbytes-cap-notunlim interchangeable，也不是已经头和证据开销已经从 MaxBytes 扣完 interchangeable / 344 maxbytes-overhead interchangeable。**  
   官方把 Process 会拒和已经交差分开。看见 Process 会拒，不是已经交差 interchangeable。337 maxbytes-cap vs unlimited bundled unbundling 在本页 item 2 续。

怎样设 MaxBytes、100 MB / 21 MB 取值、怎样算头和证据开销是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **应用自己卡体积 not already engine-off ≠ 已经引擎不管了 interchangeable：** 官方把应用侧上限和引擎那把 100 MB 尺分开。
- **看见 MAY 写成 -1 not already only-app-ruler ≠ 已经只有应用这一把尺 interchangeable：** 官方把 MAY 写成 -1 和已经没有 100 MB 那把尺分开。
- **看见 Process 会拒 not already settled ≠ 已经交差 interchangeable：** 官方把 Process 会拒和已经交差分开；337 maxbytes-cap vs unlimited bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 应用自己卡体积 | 不是已经引擎不管了 | 不是仓库默认 MaxBytes 已经是活性 SLA（63） |
| 看见 MAY 写成 -1 | 不是已经只有应用这一把尺 | 不是头和证据开销已经从 MaxBytes 扣完（344） |
| 看见 Process 会拒 | 不是已经交差 | 不是 -1 就已经没有上限（917） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看应用自己卡体积 not already engine-off / not already only-app-ruler / not already settled 正式三事（337 余量），必须分开是不是已经引擎不管了、是不是已经只有应用这一把尺、是不是已经交差。可以跳过「看见应用自己卡就已经引擎不管」。不要把 100 MB / 21 MB 当不确定常数。不要另写怎样设 MaxBytes 或怎样算块开销。337 maxbytes-cap vs unlimited bundled unbundling 在本页 item 2 续；续 [`worked-example-maxbytes-cap-not21-vs-bundled.md`](worked-example-maxbytes-cap-not21-vs-bundled.md)（不变量 919 item 3）。

## 本页不抄

- 怎样设 MaxBytes、100 MB / 21 MB 取值、怎样算头和证据开销。
- 上限 bundled。那是不变量 337。
- -1 就已经没有上限。那是不变量 337 item 1 余量 / 917。
- 仓库默认 MaxBytes 已经是活性 SLA。那是不变量 63。
- 头和证据开销已经从 MaxBytes 扣完。那是不变量 344。
