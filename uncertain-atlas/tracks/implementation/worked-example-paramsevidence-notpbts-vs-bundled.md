# 例：看见 ConsensusParams.synchrony 定提案时间戳合法界 is not already PBTS interchangeable / not already Precision is MessageDelay interchangeable / not already settled interchangeable

**层次**：实现 / ConsensusParams.synchrony not already PBTS / not already Precision is MessageDelay / not already settled 正式三事（386 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ConsensusParams。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ConsensusParams.synchrony not already PBTS / not already Precision is MessageDelay / not already settled 正式三事（386 余量）/ not 772 paramsevidence-notpbts interchangeable / not 386 paramsevidence-vs-maxbytes bundled interchangeable」，不是 ConsensusParams 余栏 bundled（386），也不是填了 Precision 就已经是 MessageDelay（336）。不要另写怎样写 ConsensusParams 余栏。

## 官方三件事

1. **看见 ConsensusParams.`synchrony` 定提案时间戳合法界 / 看见填了 synchrony / ConsensusParams 这份同步栏 is not already 已经启用 PBTS interchangeable，也不是已经 ConsensusParams 余栏 bundled（386） interchangeable / 772 paramsevidence-notpbts interchangeable / 770 paramsevidence-notmaxbytes interchangeable / 386 paramsevidence item 1 evidence interchangeable，也不是已经 synchrony not already PBTS / not already Precision is MessageDelay / not already settled 正式三事 bundled（386 item 3 余量） interchangeable / 386 paramsevidence item 3 interchangeable。**  
   官方写：`synchrony` 定一份提案时间戳的合法界。看见填了 synchrony，不是已经启用 PBTS interchangeable——本页从 386 item 3 侧钉 not already PBTS 单句。386 paramsevidence vs maxbytes bundled unbundling 在本页 item 3 完成。

2. **看见填了 synchrony / 看见有同步栏 / ConsensusParams 这份同步栏 is not already 已经是 Precision 就已经是 MessageDelay interchangeable / 336 precision interchangeable，也不是已经 ConsensusParams 余栏 bundled（386） interchangeable / 772 paramsevidence-notpbts interchangeable / 386 paramsevidence item 2 abci interchangeable / 771 paramsevidence-notextend interchangeable。**  
   官方把这一栏和填了 Precision 就已经是 MessageDelay 分开——386 bundled 第三件事常与 336 混成「看见填了 synchrony 就已经是 PBTS 或已经是 Precision 就已经是 MessageDelay interchangeable」，本页钉 not already Precision is MessageDelay 单句。

3. **看见填了 synchrony / 看见能填 / ConsensusParams 这份同步栏 is not already 已经交差 interchangeable，也不是已经 ConsensusParams 余栏 bundled（386） interchangeable / 772 paramsevidence-notpbts interchangeable / 770 paramsevidence-notmaxbytes interchangeable。**  
   官方把能填 ConsensusParams.synchrony 和已经交差分开。看见能填，不是已经交差 interchangeable。386 paramsevidence vs maxbytes bundled unbundling 在本页 item 3 完成。

怎样写余下三栏、怎样设证据上限、怎样设 Precision 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **synchrony not already PBTS ≠ 已经是 PBTS interchangeable：** 官方把这一栏和填了同步参数就已经是 PBTS 分开。
- **synchrony not already Precision is MessageDelay ≠ 336 interchangeable：** 官方把有同步栏和填了 Precision 就已经是 MessageDelay 分开。
- **synchrony not already settled ≠ 已经交差 interchangeable：** 官方把能填 synchrony 和已经交差分开；386 paramsevidence vs maxbytes bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ConsensusParams.synchrony 定提案时间戳合法界 | 不是已经是 PBTS | 不是 ConsensusParams.evidence（770/386 item 1） |
| 看见填了 synchrony | 不是已经是 Precision 就已经是 MessageDelay（336） | 不是 ConsensusParams 余栏 bundled（386） |
| 看见能填 | 不是已经交差 | 不是 ConsensusParams.abci（771/386 item 2） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ConsensusParams.synchrony not already PBTS / not already Precision is MessageDelay / not already settled 正式三事（386 余量），必须分开 synchrony 是不是已经是 PBTS、是不是已经是 Precision 就已经是 MessageDelay interchangeable / 336、是不是已经交差。可以跳过「看见填了 synchrony 就已经是 PBTS」。不要另写怎样写 ConsensusParams 余栏。386 paramsevidence vs maxbytes bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写余下三栏、怎样设证据上限、怎样设 Precision。
- ConsensusParams 余栏 bundled。那是不变量 386。
- ConsensusParams.evidence。那是不变量 386 item 1 余量 / 770。
- ConsensusParams.abci。那是不变量 386 item 2 余量 / 771。
- 填了 Precision 就已经是 MessageDelay。那是不变量 336。
