# 例：看见 InitChain 回了空 ConsensusParams 不是已经没有参数；看见 Finalize 没回不是已经清掉；看见只改了一个字段不是已经只改这一项

**层次**：实现 / ConsensusParams。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Updating Consensus Parameters。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「InitChain 空参数不是已经没有参数 / Finalize 没回不是已经清掉 / 只改一个字段不是已经只改这一项」，不是 H 的参数更新已经在 H+1 生效，也不是 MaxGas 已经在执行。不要另写怎样编参数或怎样选上限。

## 官方三件事

规范把更新共识参数写成三件独立的实现事，不是「看见回了 ConsensusParams 就已经定了、已经能空着当清掉、已经能只改一项」一件事：

1. **看见 InitChain 回了空 ConsensusParams / 看见没回参数 不是已经没有参数，也不是已经用了应用自己的空参数。**  
   官方写：`InitChainResponse` 带一份 `ConsensusParams`。若是 `nil`，CometBFT **用创世文件里的参数**。若不空，CometBFT 用回包这份。看见回了空，不是已经没有参数。看见没回，不是已经删掉创世参数。看见能设初始参数，不是已经和 InitChain 空验证者名单同一句。
2. **看见 FinalizeBlock 回了空 / 看见没回 ConsensusParams 不是已经清掉，也不是已经改了。**  
   官方写：`FinalizeBlockResponse` 也收一份 `ConsensusParams`。若是 `nil`，CometBFT **什么也不做**。若不空，CometBFT 用回包这份。看见没回，不是已经清成默认。看见空着，不是已经改过。看见能更新，不是已经和 InitChain 空回包同一句。
3. **看见只改了其中一个字段 / 看见 Block 只填了 MaxBytes 不是已经只改这一项，也不是已经保持其余不变。**  
   官方写：空的 `ConsensusParams` 会被忽略。每一个**不空**的字段会**整份套上**。例如要改 `Block.MaxBytes`，应用必须把其余 `Block` 字段（如 `Block.MaxGas`）也写上，哪怕没变；否则那些字段会被更新成默认。看见只填了一项，不是已经只改这一项。看见没写的字段，不是已经保持原值。

怎样编 `ConsensusParams`、怎样选 MaxBytes / MaxGas、公钥类型表是规范里的取值或做法，本页不抄。H 的更新哪一高度生效是不变量 35，本页不抄。

## 官方为什么这样拆

- **InitChain 空参数 ≠ 已经没有参数：** 官方把回空和改用创世参数分开。
- **Finalize 没回 ≠ 已经清掉：** 官方把回空什么也不做和真的改参数分开。
- **只改一个字段 ≠ 已经只改这一项：** 官方把不空字段整份套上和其余被写成默认分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| InitChain 回空参数 | 不是已经没有参数 | 不是 InitChain 空验证者名单已经没有集合（318） |
| Finalize 没回 | 不是已经清掉 | 不是 H 的参数更新已经在 H+1 生效（35） |
| 只填一个 Block 字段 | 不是已经只改这一项 | 不是 MaxGas 已经在执行（315），也不是 MaxBytes 写成 -1 已经没有上限（299） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「ConsensusParams 已经回了」，必须分开 InitChain 空着是不是已经没有参数、Finalize 没回是不是已经清掉、只填一项是不是已经只改这一项。可以跳过「看见回了就已经改完」。不要另写怎样编参数或怎样选上限。不要把仓库默认 MaxBytes / MaxGas 当不确定默认。

## 本页不抄

- 怎样编 `ConsensusParams`、怎样选 MaxBytes / MaxGas、公钥类型表。
- H+1 生效。那是不变量 35。
- MaxGas 默认 -1。那是不变量 315。
- MaxBytes 写成 -1。那是不变量 299。
