# 例：看见 ConsensusParams.abci 是 ABCI 相关参数 is not already Prepare extension interchangeable / not already ABCI 2.0 interchangeable / not already settled interchangeable

**层次**：实现 / ConsensusParams.abci not already Prepare extension / not already ABCI 2.0 / not already settled 正式三事（386 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ConsensusParams。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ConsensusParams.abci not already Prepare extension / not already ABCI 2.0 / not already settled 正式三事（386 余量）/ not 771 paramsevidence-notextend interchangeable / not 386 paramsevidence-vs-maxbytes bundled interchangeable」，不是 ConsensusParams 余栏 bundled（386），也不是到了 H 就已经 Prepare 带了扩展（330）。不要另写怎样写 ConsensusParams 余栏。

## 官方三件事

1. **看见 ConsensusParams.`abci` 是 ABCI 相关参数 / 看见填了 abci / ConsensusParams 这份 ABCI 栏 is not already 已经到了 H 就已经 Prepare 带了扩展 interchangeable / 330 extend interchangeable，也不是已经 ConsensusParams 余栏 bundled（386） interchangeable / 771 paramsevidence-notextend interchangeable / 770 paramsevidence-notmaxbytes interchangeable / 386 paramsevidence item 1 evidence interchangeable，也不是已经 abci not already Prepare extension / not already ABCI 2.0 / not already settled 正式三事 bundled（386 item 2 余量） interchangeable / 386 paramsevidence item 2 interchangeable。**  
   官方写：`abci` 是和 ABCI 有关的参数。看见填了 abci，不是已经到了 H 就已经 Prepare 带了扩展 interchangeable——本页从 386 item 2 侧钉 not already Prepare extension 单句。386 paramsevidence vs maxbytes bundled unbundling 在本页 item 2 续。

2. **看见填了 abci / 看见有 ABCI 栏 / ConsensusParams 这份 ABCI 栏 is not already 已经切到 ABCI 2.0 interchangeable / 330 extend interchangeable，也不是已经 ConsensusParams 余栏 bundled（386） interchangeable / 771 paramsevidence-notextend interchangeable / 386 paramsevidence item 3 synchrony interchangeable / 772 paramsevidence-notpbts interchangeable。**  
   官方把这一栏和已经切到 ABCI 2.0 分开——386 bundled 第二件事常与 330 混成「看见填了 abci 就已经 Prepare 带了扩展或已经切到 ABCI 2.0 interchangeable」，本页钉 not already ABCI 2.0 单句。

3. **看见填了 abci / 看见能填 / ConsensusParams 这份 ABCI 栏 is not already 已经交差 interchangeable，也不是已经 ConsensusParams 余栏 bundled（386） interchangeable / 771 paramsevidence-notextend interchangeable / 770 paramsevidence-notmaxbytes interchangeable。**  
   官方把能填 ConsensusParams.abci 和已经交差分开。看见能填，不是已经交差 interchangeable。386 paramsevidence vs maxbytes bundled unbundling 在本页 item 2 续。

怎样写余下三栏、怎样设证据上限、怎样设 Precision 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **abci not already Prepare extension ≠ 330 interchangeable：** 官方把这一栏和到了 H 就已经 Prepare 带了扩展分开。
- **abci not already ABCI 2.0 ≠ 330 interchangeable：** 官方把有 ABCI 栏和已经切到 ABCI 2.0 分开。
- **abci not already settled ≠ 已经交差 interchangeable：** 官方把能填 abci 和已经交差分开；386 paramsevidence vs maxbytes bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ConsensusParams.abci 是 ABCI 相关参数 | 不是已经 Prepare 带了扩展（330） | 不是 ConsensusParams.evidence（770/386 item 1） |
| 看见填了 abci | 不是已经切到 ABCI 2.0（330） | 不是 ConsensusParams 余栏 bundled（386） |
| 看见能填 | 不是已经交差 | 不是 ConsensusParams.synchrony（772/386 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ConsensusParams.abci not already Prepare extension / not already ABCI 2.0 / not already settled 正式三事（386 余量），必须分开 abci 是不是已经 Prepare 带了扩展 interchangeable / 330、是不是已经切到 ABCI 2.0、是不是已经交差。可以跳过「看见填了 abci 就已经 Prepare 带了扩展」。不要另写怎样写 ConsensusParams 余栏。386 paramsevidence vs maxbytes bundled unbundling 在本页 item 2 续；完成 [`worked-example-paramsevidence-notpbts-vs-bundled.md`](worked-example-paramsevidence-notpbts-vs-bundled.md)（不变量 772 item 3）。

## 本页不抄

- 怎样写余下三栏、怎样设证据上限、怎样设 Precision。
- ConsensusParams 余栏 bundled。那是不变量 386。
- ConsensusParams.evidence。那是不变量 386 item 1 余量 / 770。
- ConsensusParams.synchrony。那是不变量 386 item 3 余量 / 772。
- 到了 H 就已经 Prepare 带了扩展。那是不变量 330。
