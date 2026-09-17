# 例：看见 MaxGas is not already executing interchangeable / not already meaningful interchangeable / not already settled interchangeable

**层次**：实现 / MaxGas not already executing / not already meaningful / not already settled 正式三事（315 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Gas。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、mempool。本页是「MaxGas not already executing / not already meaningful / not already settled 正式三事（315 余量）/ not 914 maxgas-noton interchangeable / not 315 maxgas-vs-enforced bundled interchangeable」，不是气 bundled（315），也不是 MaxBytes 写成 -1 已经没有上限（299），也不是只填一项就已经只改这一项（319/910）。不要另写怎样计量气或怎样在 Prepare 里卡上限。

## 官方三件事

1. **看见 MaxGas / 看见回包里有气字段 这份字段 is not already 已经在执行 interchangeable，也不是已经气 bundled（315） interchangeable / 914 maxgas-noton interchangeable / 915 maxgas-notused interchangeable / 315 maxgas item 2 GasUsed interchangeable，也不是已经 MaxGas not already executing / not already meaningful / not already settled 正式三事 bundled（315 item 1 余量） interchangeable / 315 maxgas item 1 interchangeable。**  
   官方写：CometBFT 学了类似的抽象，但只用得可选且弱。ConsensusParams.Block.MaxGas 限制一块里所有交易能用的总气。默认值是 -1，表示块气限不执行，或者说气这个概念没有意义。看见字段在，不是已经在卡 interchangeable——本页从 315 item 1 侧钉 not already executing 单句。315 maxgas vs enforced bundled unbundling 在本页 item 1 启动。

2. **看见写成 -1 / 看见学了以太坊 / 这份字段 is not already 已经有意义 interchangeable，也不是已经气 bundled（315） interchangeable / 914 maxgas-noton interchangeable / 315 maxgas item 3 已提交 interchangeable / 916 maxgas-notblock interchangeable，也不是已经 MaxBytes 写成 -1 已经没有上限 interchangeable / 299 maxbytes-cap interchangeable。**  
   官方把写成 -1 和已经和 MaxBytes 写成 -1 同一句分开——315 bundled 第一件事常与 299 混成「看见有 MaxGas 就已经在执行或已经是 -1 没有上限 interchangeable」，本页钉 not already meaningful 单句。

3. **看见学了以太坊 / 看见字段在 / 这份字段 is not already 已经交差 interchangeable，也不是已经气 bundled（315） interchangeable / 914 maxgas-noton interchangeable / 915 maxgas-notused interchangeable，也不是已经有费用市场 interchangeable。**  
   官方把学了以太坊和已经有费用市场 / 已经交差分开。看见学了以太坊，不是已经交差 interchangeable。315 maxgas vs enforced bundled unbundling 在本页 item 1 启动。

怎样计量气、怎样在 Prepare 里卡上限、以太坊费用市场是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **MaxGas not already executing ≠ 已经在执行 interchangeable：** 官方把可选弱抽象和默认 -1 没有意义分开。
- **看见写成 -1 not already meaningful ≠ 已经有意义 interchangeable：** 官方把默认 -1 和已经在卡 / 已经和 MaxBytes -1 同一句分开。
- **看见学了以太坊 not already settled ≠ 已经交差 interchangeable：** 官方把学了以太坊和已经交差分开；315 maxgas vs enforced bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| MaxGas 默认 -1 | 不是已经在执行，也不是已经有意义 | 不是 MaxBytes 写成 -1 已经没有上限（299） |
| 看见写成 -1 | 不是已经有意义 | 不是只填一项就已经只改这一项（319/910） |
| 看见学了以太坊 | 不是已经交差 | 不是 GasUsed 就已经算进共识（915） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 MaxGas not already executing / not already meaningful / not already settled 正式三事（315 余量），必须分开是不是已经在执行、是不是已经有意义、是不是已经交差。可以跳过「看见有 MaxGas 就已经在卡」。不要把 MaxGas 默认 -1 当不确定默认。不要另写怎样计量气或怎样在 Prepare 里卡上限。315 maxgas vs enforced bundled unbundling 在本页 item 1 启动；续 [`worked-example-maxgas-notused-vs-bundled.md`](worked-example-maxgas-notused-vs-bundled.md)（不变量 915 item 2）。

## 本页不抄

- 怎样计量气、怎样在 Prepare 里卡上限、以太坊费用市场。
- 气 bundled。那是不变量 315。
- GasUsed 就已经算进共识。那是不变量 315 item 2 余量 / 915。
- MaxBytes 写成 -1 已经没有上限。那是不变量 299。
