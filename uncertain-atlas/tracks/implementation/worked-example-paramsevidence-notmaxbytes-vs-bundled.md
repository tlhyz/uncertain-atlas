# 例：看见 ConsensusParams.evidence 限制拜占庭证据是否合法 is not already evidence MaxBytes interchangeable / not already unbonding interchangeable / not already settled interchangeable

**层次**：实现 / ConsensusParams.evidence not already evidence MaxBytes / not already unbonding / not already settled 正式三事（386 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ConsensusParams。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ConsensusParams.evidence not already evidence MaxBytes / not already unbonding / not already settled 正式三事（386 余量）/ not 770 paramsevidence-notmaxbytes interchangeable / not 386 paramsevidence-vs-maxbytes bundled interchangeable」，不是 ConsensusParams 余栏 bundled（386），也不是证据 MaxBytes 就已经是块 MaxBytes（331），也不是 ConsensusParams.block 就已经是 MaxBytes 上限（385）。不要另写怎样写 ConsensusParams 余栏。

## 官方三件事

1. **看见 ConsensusParams.`evidence` 限制拜占庭证据是否合法 / 看见填了 evidence / ConsensusParams 这份证据栏 is not already 已经是证据 MaxBytes interchangeable / 331 evidencemax interchangeable，也不是已经 ConsensusParams 余栏 bundled（386） interchangeable / 770 paramsevidence-notmaxbytes interchangeable / 771 paramsevidence-notextend interchangeable / 386 paramsevidence item 2 abci interchangeable，也不是已经 evidence not already evidence MaxBytes / not already unbonding / not already settled 正式三事 bundled（386 item 1 余量） interchangeable / 386 paramsevidence item 1 interchangeable。**  
   官方写：`evidence` 限制拜占庭行为证据是否合法。看见填了 evidence，不是已经是证据 MaxBytes interchangeable——本页从 386 item 1 侧钉 not already evidence MaxBytes 单句。386 paramsevidence vs maxbytes bundled unbundling 在本页 item 1 启动。

2. **看见填了 evidence / 看见能限证据 / ConsensusParams 这份证据栏 is not already 已经盖住解绑 interchangeable，也不是已经 ConsensusParams 余栏 bundled（386） interchangeable / 770 paramsevidence-notmaxbytes interchangeable / 386 paramsevidence item 3 synchrony interchangeable / 772 paramsevidence-notpbts interchangeable，也不是已经证据 MaxBytes 就已经是块 MaxBytes interchangeable / 331 evidencemax interchangeable。**  
   官方把这一栏和已经盖住解绑分开——386 bundled 第一件事常与 331 混成「看见填了 evidence 就已经是证据 MaxBytes 或已经盖住解绑 interchangeable」，本页钉 not already unbonding 单句。

3. **看见填了 evidence / 看见有字段 / ConsensusParams 这份证据栏 is not already 已经交差 interchangeable，也不是已经 ConsensusParams 余栏 bundled（386） interchangeable / 770 paramsevidence-notmaxbytes interchangeable / 771 paramsevidence-notextend interchangeable。**  
   官方把能填 ConsensusParams.evidence 和已经交差分开。看见有字段，不是已经交差 interchangeable。386 paramsevidence vs maxbytes bundled unbundling 在本页 item 1 启动。

怎样写余下三栏、怎样设证据上限、怎样设 Precision 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **evidence not already evidence MaxBytes ≠ 331 interchangeable：** 官方把这一栏和证据 MaxBytes 那把尺分开。
- **evidence not already unbonding ≠ 已经盖住解绑 interchangeable：** 官方把能限证据和已经盖住解绑分开。
- **evidence not already settled ≠ 已经交差 interchangeable：** 官方把有字段和已经交差分开；386 paramsevidence vs maxbytes bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ConsensusParams.evidence 限制拜占庭证据是否合法 | 不是已经是证据 MaxBytes（331） | 不是 ConsensusParams.abci（771/386 item 2） |
| 看见填了 evidence | 不是已经盖住解绑 | 不是 ConsensusParams.block（385） |
| 看见有字段 | 不是已经交差 | 不是 ConsensusParams 余栏 bundled（386） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ConsensusParams.evidence not already evidence MaxBytes / not already unbonding / not already settled 正式三事（386 余量），必须分开 evidence 是不是已经是证据 MaxBytes interchangeable / 331、是不是已经盖住解绑、是不是已经交差。可以跳过「看见填了 evidence 就已经是证据 MaxBytes」。不要另写怎样写 ConsensusParams 余栏。386 paramsevidence vs maxbytes bundled unbundling 在本页 item 1 启动；续 [`worked-example-paramsevidence-notextend-vs-bundled.md`](worked-example-paramsevidence-notextend-vs-bundled.md)（不变量 771 item 2）。

## 本页不抄

- 怎样写余下三栏、怎样设证据上限、怎样设 Precision。
- ConsensusParams 余栏 bundled。那是不变量 386。
- ConsensusParams.abci。那是不变量 386 item 2 余量 / 771。
- ConsensusParams.synchrony。那是不变量 386 item 3 余量 / 772。
- 证据 MaxBytes 就已经是块 MaxBytes。那是不变量 331。
- ConsensusParams.block 就已经是 MaxBytes 上限。那是不变量 385。
