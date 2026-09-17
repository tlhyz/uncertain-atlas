# 例：看见 -1 就按 100 MB 验 is not already unlimited interchangeable / not already free to return anything interchangeable / not already settled interchangeable

**层次**：实现 / -1 就按 100 MB 验 not already unlimited / not already free to return anything / not already settled 正式三事（337 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / BlockParams.MaxBytes。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、mempool。本页是「-1 就按 100 MB 验 not already unlimited / not already free to return anything / not already settled 正式三事（337 余量）/ not 917 maxbytes-cap-notunlim interchangeable / not 337 maxbytes-cap-vs-unlimited bundled interchangeable」，不是上限 bundled（337），也不是整池都给 Prepare 就已经没有上限（299），也不是 MaxGas 默认 -1 就已经没有气限（315/914）。不要另写怎样设 MaxBytes 或怎样算块开销。

## 官方三件事

1. **看见 MaxBytes 写成 -1 / 看见引擎按 100 MB 验 这份字段 is not already 已经没有上限 interchangeable，也不是已经上限 bundled（337） interchangeable / 917 maxbytes-cap-notunlim interchangeable / 918 maxbytes-cap-notapp interchangeable / 337 maxbytes-cap item 2 应用自己卡 interchangeable，也不是已经 -1 就按 100 MB 验 not already unlimited / not already free to return anything / not already settled 正式三事 bundled（337 item 1 余量） interchangeable / 337 maxbytes-cap item 1 interchangeable。**  
   官方写：应用若写成 -1，共识会把实际要验的值当成 100 MB，并把内存池里所有交易交给 PrepareProposal。看见写成 -1，不是已经没有上限 interchangeable——本页从 337 item 1 侧钉 not already unlimited 单句。337 maxbytes-cap vs unlimited bundled unbundling 在本页 item 1 启动。

2. **看见按 100 MB 验 / 看见能打满 / 这份字段 is not already 已经应用可以随便回 interchangeable，也不是已经上限 bundled（337） interchangeable / 917 maxbytes-cap-notunlim interchangeable / 337 maxbytes-cap item 3 合法范围 interchangeable / 919 maxbytes-cap-not21 interchangeable，也不是已经整池都给 Prepare 就已经没有上限 interchangeable / 299 maxbytes-pool interchangeable。**  
   官方把按 100 MB 验和已经和「整池都给 Prepare、应用仍不得超过 MaxTxBytes」同一句分开——337 bundled 第一件事常与 299 混成「看见写成 -1 就已经没有上限或已经随便回 interchangeable」，本页钉 not already free to return anything 单句。

3. **看见能打满 / 看见写成 -1 / 这份字段 is not already 已经交差 interchangeable，也不是已经上限 bundled（337） interchangeable / 917 maxbytes-cap-notunlim interchangeable / 918 maxbytes-cap-notapp interchangeable，也不是已经 MaxGas -1 就已经没有气限 interchangeable / 315/914 maxgas-noton interchangeable。**  
   官方把能打满和已经交差分开。看见能打满，不是已经交差 interchangeable。337 maxbytes-cap vs unlimited bundled unbundling 在本页 item 1 启动。

怎样设 MaxBytes、100 MB / 21 MB 取值、怎样算头和证据开销是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **-1 就按 100 MB 验 not already unlimited ≠ 已经没有上限 interchangeable：** 官方把写成 -1 和引擎仍按 100 MB 验分开。
- **看见按 100 MB 验 not already free to return anything ≠ 已经应用可以随便回 interchangeable：** 官方把 100 MB 那把尺和已经和 299 同一句分开。
- **看见能打满 not already settled ≠ 已经交差 interchangeable：** 官方把能打满和已经交差分开；337 maxbytes-cap vs unlimited bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| MaxBytes 写成 -1 | 不是已经没有上限，也不是已经随便回 | 不是整池都给 Prepare 就已经没有上限（299） |
| 看见按 100 MB 验 | 不是已经随便回 | 不是 MaxGas 默认 -1 就已经没有气限（315/914） |
| 看见能打满 | 不是已经交差 | 不是应用自己卡就已经引擎不管了（918） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 -1 就按 100 MB 验 not already unlimited / not already free to return anything / not already settled 正式三事（337 余量），必须分开是不是已经没有上限、是不是已经随便回、是不是已经交差。可以跳过「看见写成 -1 就已经没有上限」。不要把 100 MB / 21 MB 当不确定常数。不要另写怎样设 MaxBytes 或怎样算块开销。337 maxbytes-cap vs unlimited bundled unbundling 在本页 item 1 启动；续 [`worked-example-maxbytes-cap-notapp-vs-bundled.md`](worked-example-maxbytes-cap-notapp-vs-bundled.md)（不变量 918 item 2）。

## 本页不抄

- 怎样设 MaxBytes、100 MB / 21 MB 取值、怎样算头和证据开销。
- 上限 bundled。那是不变量 337。
- 应用自己卡就已经引擎不管了。那是不变量 337 item 2 余量 / 918。
- 整池都给 Prepare 就已经没有上限。那是不变量 299。
