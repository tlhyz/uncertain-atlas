# 例：看见 Info 请求 version 是 CometBFT 软件语义版本 is not already app_version interchangeable / not already header AppHash interchangeable / not already settled interchangeable

**层次**：实现 / Info 请求 version not already app_version / not already header AppHash / not already settled 正式三事（379 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Info 请求 version not already app_version / not already header AppHash / not already settled 正式三事（379 余量）/ not 791 infover-notappver interchangeable / not 379 infover-vs-appversion bundled interchangeable」，不是 Info 请求版本 bundled（379），也不是 Info 用来握手对齐就已经是快照重放（370），也不是 Info 回包 version 就已经是 app_version（389/762），也不是 ConsensusParams.version 就已经是 app_version 进了头（385/775）。不要另写怎样写 Info 请求版本。

## 官方三件事

1. **看见 Info 请求 `version` 是 CometBFT 软件语义版本 / 看见填了 `version` / Info 这份软件版本 is not already 已经是回包里的 `app_version` interchangeable / 370 appver interchangeable，也不是已经 Info 请求版本 bundled（379） interchangeable / 791 infover-notappver interchangeable / 792 infover-notaligned interchangeable / 379 infover item 2 block_version interchangeable，也不是已经 version not already app_version / not already header AppHash / not already settled 正式三事 bundled（379 item 1 余量） interchangeable / 379 infover item 1 interchangeable。**  
   官方写：请求里的 `version` 是 CometBFT 软件的语义版本。看见填了 `version`，不是已经是回包里的 `app_version` interchangeable——本页从 379 item 1 侧钉 not already app_version 单句。379 infover vs appversion bundled unbundling 在本页 item 1 启动。

2. **看见填了 `version` / 看见有软件版本 / Info 这份软件版本 is not already 已经印进每块头 interchangeable / 370 appver interchangeable，也不是已经 Info 请求版本 bundled（379） interchangeable / 791 infover-notappver interchangeable / 379 infover item 3 abci_version interchangeable / 793 infover-nothandshake interchangeable，也不是已经 Info 回包 version 就已经是 app_version interchangeable / 389 infodata / 762 infodata-notappversion interchangeable，也不是已经 ConsensusParams.version 就已经是 app_version 进了头 interchangeable / 385 paramsblock / 775 paramsblock-notappver interchangeable。**  
   官方把有软件版本和已经印进每块头分开——379 bundled 第一件事常与 370 / 389 / 385 混成「看见填了 version 就已经是 app_version 或已经印进本头 AppHash interchangeable」，本页钉 not already header AppHash 单句。

3. **看见填了 `version` / 看见能回 / Info 这份软件版本 is not already 已经交差 interchangeable，也不是已经 Info 请求版本 bundled（379） interchangeable / 791 infover-notappver interchangeable / 792 infover-notaligned interchangeable。**  
   官方把能回 version 和已经交差分开。看见能回，不是已经交差 interchangeable。379 infover vs appversion bundled unbundling 在本页 item 1 启动。

怎样写 Info 请求、怎样对版本、怎样显示 X.X.x 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **version not already app_version ≠ 370 interchangeable：** 官方把引擎软件版本和应用 app_version 分开。
- **version not already header AppHash ≠ 370 interchangeable：** 官方把有软件版本和已经印进每块头分开。
- **version not already settled ≠ 已经交差 interchangeable：** 官方把能回 version 和已经交差分开；379 infover vs appversion bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Info 请求 version 是 CometBFT 软件语义版本 | 不是已经是 app_version（370） | 不是 block_version / p2p_version（792/379 item 2） |
| 看见填了 version | 不是已经印进本头 AppHash（370） | 不是 Info 回包 version（389/762） |
| 看见能回 | 不是已经交差 | 不是 ConsensusParams.version（385/775） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info 请求 version not already app_version / not already header AppHash / not already settled 正式三事（379 余量），必须分开 version 是不是已经是 app_version interchangeable / 370、是不是已经印进本头 AppHash、是不是已经交差。可以跳过「看见填了 version 就已经是 app_version」。不要另写怎样写 Info 请求版本。379 infover vs appversion bundled unbundling 在本页 item 1 启动；续 [`worked-example-infover-notaligned-vs-bundled.md`](worked-example-infover-notaligned-vs-bundled.md)（不变量 792 item 2）。

## 本页不抄

- 怎样写 Info 请求、怎样对版本、怎样显示 X.X.x。
- Info 请求版本 bundled。那是不变量 379。
- block_version / p2p_version。那是不变量 379 item 2 余量 / 792。
- abci_version。那是不变量 379 item 3 余量 / 793。
- Info 用来握手对齐就已经是快照重放。那是不变量 370。
- Info 回包 version 就已经是 app_version。那是不变量 389 / 762。
- ConsensusParams.version 就已经是 app_version 进了头。那是不变量 385 / 775。
