# 例：看见 ConsensusParams.evidence 限制拜占庭证据是否合法不是已经是证据 MaxBytes；看见 ConsensusParams.abci 是 ABCI 相关参数不是已经 Prepare 带了扩展；看见 ConsensusParams.synchrony 定提案时间戳合法界不是已经是 PBTS

**层次**：实现 / ConsensusParams 余栏。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ConsensusParams。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「ConsensusParams.evidence 限制拜占庭证据是否合法不是已经是证据 MaxBytes / ConsensusParams.abci 是 ABCI 相关参数不是已经 Prepare 带了扩展 / ConsensusParams.synchrony 定提案时间戳合法界不是已经是 PBTS」，不是证据 MaxBytes 就已经是块 MaxBytes，也不是到了 H 就已经 Prepare 带了扩展。不要另写怎样写 ConsensusParams 余栏。

## 官方三件事

规范把 `evidence` 限制拜占庭证据是否合法、`abci` 是 ABCI 相关参数、`synchrony` 定提案时间戳合法界写成三件独立的实现事，不是「看见填了余下三栏就已经是证据 MaxBytes、已经 Prepare 带了扩展、已经是 PBTS」一件事：

1. **看见 ConsensusParams.`evidence` 限制拜占庭证据是否合法 / 看见填了 evidence 不是已经是证据 MaxBytes，也不是已经盖住解绑。**  
   官方写：`evidence` 限制拜占庭行为证据是否合法。看见填了 evidence，不是已经是证据 MaxBytes。看见能限证据，不是已经盖住解绑。看见有字段，不是已经交差。
2. **看见 ConsensusParams.`abci` 是 ABCI 相关参数 / 看见填了 abci 不是已经 Prepare 带了扩展，也不是已经切到 ABCI 2.0。**  
   官方写：`abci` 是和 ABCI 有关的参数。看见填了 abci，不是已经到了 H 就已经 Prepare 带了扩展。看见有 ABCI 栏，不是已经切到 ABCI 2.0。看见能填，不是已经交差。
3. **看见 ConsensusParams.`synchrony` 定提案时间戳合法界 / 看见填了 synchrony 不是已经是 PBTS，也不是已经是 Precision 就已经是 MessageDelay。**  
   官方写：`synchrony` 定一份提案时间戳的合法界。看见填了 synchrony，不是已经启用 PBTS。看见有同步栏，不是已经是 Precision 就已经是 MessageDelay。看见能填，不是已经交差。

怎样写余下三栏、怎样设证据上限、怎样设 Precision 是规范里的做法，本页不抄。证据 MaxBytes 就已经是块 MaxBytes 是不变量 331，本页不抄。

## 官方为什么这样拆

- **ConsensusParams.evidence 限制拜占庭证据是否合法 ≠ 已经是证据 MaxBytes：** 官方把这一栏和证据 MaxBytes 那把尺分开。
- **ConsensusParams.abci 是 ABCI 相关参数 ≠ 已经 Prepare 带了扩展：** 官方把这一栏和到了 H 就已经 Prepare 带了扩展分开。
- **ConsensusParams.synchrony 定提案时间戳合法界 ≠ 已经是 PBTS：** 官方把这一栏和填了同步参数就已经是 PBTS 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ConsensusParams.evidence 限制拜占庭证据是否合法 | 不是已经是证据 MaxBytes | 不是证据 MaxBytes 就已经是块 MaxBytes（331） |
| ConsensusParams.abci 是 ABCI 相关参数 | 不是已经 Prepare 带了扩展 | 不是到了 H 就已经 Prepare 带了扩展（330） |
| ConsensusParams.synchrony 定提案时间戳合法界 | 不是已经是 PBTS | 不是填了 Precision 就已经是 MessageDelay（336） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了余下三栏就已经是证据 MaxBytes、已经 Prepare 带了扩展、已经是 PBTS」，必须分开 ConsensusParams.evidence 限制拜占庭证据是否合法是不是已经是证据 MaxBytes、ConsensusParams.abci 是 ABCI 相关参数是不是已经 Prepare 带了扩展、ConsensusParams.synchrony 定提案时间戳合法界是不是已经是 PBTS。可以跳过「看见填了余下三栏就已经是证据 MaxBytes」。不要另写怎样写 ConsensusParams 余栏。

## 本页不抄

- 怎样写余下三栏、怎样设证据上限、怎样设 Precision。
- 证据 MaxBytes 就已经是块 MaxBytes。那是不变量 331。
- 到了 H 就已经 Prepare 带了扩展。那是不变量 330。
- 填了 Precision 就已经是 MessageDelay。那是不变量 336。
