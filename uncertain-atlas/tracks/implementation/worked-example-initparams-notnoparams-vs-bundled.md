# 例：看见 InitChain 请求 consensus_params 是起步共识参数 is not already no params interchangeable / not already empty response interchangeable / not already settled interchangeable

**层次**：实现 / InitChain 请求 consensus_params not already no params / not already empty response / not already settled 正式三事（388 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「InitChain 请求 consensus_params not already no params / not already empty response / not already settled 正式三事（388 余量）/ not 764 initparams-notnoparams interchangeable / not 388 initparams-vs-empty bundled interchangeable」，不是 InitChain 请求余栏 bundled（388），也不是 InitChain 回了空 ConsensusParams 就已经没有参数（319），也不是 InitChain Usage 空集合（495/695）。不要另写怎样写 InitChain 请求余栏。

## 官方三件事

1. **看见 InitChain 请求 `consensus_params` 是起步共识参数 / 看见填了起步参数 / InitChain 这份请求栏 is not already 已经没有参数 interchangeable / 319 emptyparams interchangeable，也不是已经 InitChain 请求余栏 bundled（388） interchangeable / 764 initparams-notnoparams interchangeable / 765 initparams-notnoset interchangeable / 388 initparams item 2 validators interchangeable，也不是已经 consensus_params not already no params / not already empty response / not already settled 正式三事 bundled（388 item 1 余量） interchangeable / 388 initparams item 1 interchangeable。**  
   官方写：`consensus_params` 是起步时共识关键参数。看见填了起步参数，不是已经没有参数 interchangeable——本页从 388 item 1 侧钉 not already no params 单句。388 initparams vs empty bundled unbundling 在本页 item 1 启动。

2. **看见填了起步参数 / 看见有这份请求栏 / InitChain 这份请求栏 is not already 已经是 InitChain 回了空就改用创世参数 interchangeable / 319 emptyparams interchangeable，也不是已经 InitChain 请求余栏 bundled（388） interchangeable / 764 initparams-notnoparams interchangeable / 388 initparams item 3 app_state_bytes interchangeable / 766 initparams-notverified interchangeable，也不是已经 InitChain Usage 空集合 interchangeable / 495 initchainusage / 695–700 interchangeable。**  
   官方把请求里的起步参数和回包空着就已经没有参数分开——388 bundled 第一件事常与 319 / 495 混成「看见填了起步参数就已经没有参数或已经用了回包空参数 interchangeable」，本页钉 not already empty response 单句。

3. **看见填了起步参数 / 看见能填 / InitChain 这份请求栏 is not already 已经交差 interchangeable，也不是已经 InitChain 请求余栏 bundled（388） interchangeable / 764 initparams-notnoparams interchangeable / 765 initparams-notnoset interchangeable。**  
   官方把能填 InitChain 请求 consensus_params 和已经交差分开。看见能填，不是已经交差 interchangeable。388 initparams vs empty bundled unbundling 在本页 item 1 启动。

怎样写 InitChain 请求余栏、怎样选起步参数、怎样排起步名单是规范里的做法，本页不抄。

## 官方为什么这样拆

- **consensus_params not already no params ≠ 319 interchangeable：** 官方把请求里的起步参数和回包空着就已经没有参数分开。
- **consensus_params not already empty response ≠ 319/495 interchangeable：** 官方把有这份请求栏和已经用了回包空参数 / InitChain Usage 分开。
- **consensus_params not already settled ≠ 已经交差 interchangeable：** 官方把能填起步参数和已经交差分开；388 initparams vs empty bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| InitChain 请求 consensus_params 是起步共识参数 | 不是已经没有参数（319） | 不是 InitChain 请求 validators（765/388 item 2） |
| 看见填了起步参数 | 不是已经用了回包空参数（319） | 不是 InitChain Usage（495/695） |
| 看见能填 | 不是已经交差 | 不是 InitChain 请求余栏 bundled（388） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain 请求 consensus_params not already no params / not already empty response / not already settled 正式三事（388 余量），必须分开 consensus_params 是不是已经没有参数 interchangeable / 319、是不是已经用了回包空参数、是不是已经交差。可以跳过「看见填了起步参数就已经没有参数」。不要另写怎样写 InitChain 请求余栏。388 initparams vs empty bundled unbundling 在本页 item 1 启动；续 [`worked-example-initparams-notnoset-vs-bundled.md`](worked-example-initparams-notnoset-vs-bundled.md)（不变量 765 item 2）。

## 本页不抄

- 怎样写 InitChain 请求余栏、怎样选起步参数、怎样排起步名单。
- InitChain 请求余栏 bundled。那是不变量 388。
- InitChain 请求 validators。那是不变量 388 item 2 余量 / 765。
- InitChain 请求 app_state_bytes。那是不变量 388 item 3 余量 / 766。
- InitChain 回了空 ConsensusParams 就已经没有参数。那是不变量 319。
- InitChain Usage 空集合 / 决定参数。那是不变量 495 / 695–700。
