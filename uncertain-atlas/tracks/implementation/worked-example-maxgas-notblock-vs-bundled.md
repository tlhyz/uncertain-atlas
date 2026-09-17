# 例：看见已提交块 is not already gas-checked interchangeable / not already consensus-enforced interchangeable / not already settled interchangeable

**层次**：实现 / 已提交块 not already gas-checked / not already consensus-enforced / not already settled 正式三事（315 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Gas。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、mempool。本页是「已提交块 not already gas-checked / not already consensus-enforced / not already settled 正式三事（315 余量）/ not 916 maxgas-notblock interchangeable / not 315 maxgas-vs-enforced bundled interchangeable」，不是气 bundled（315），也不是四门已经结算（33），也不是 CheckTx 绿就已经进块（33）。不要另写怎样计量气或怎样在 Prepare 里卡上限。

## 官方三件事

1. **看见已提交块 / 看见旧版只在内存池管气 这份块 is not already 已经保证这块守了气限 interchangeable，也不是已经气 bundled（315） interchangeable / 916 maxgas-notblock interchangeable / 914 maxgas-noton interchangeable / 315 maxgas item 1 MaxGas interchangeable，也不是已经已提交块 not already gas-checked / not already consensus-enforced / not already settled 正式三事 bundled（315 item 3 余量） interchangeable / 315 maxgas item 3 interchangeable。**  
   官方写：v0.34.x 及更早，CometBFT 在共识里不强制任何气规则，只在内存池管。因此不保证已提交块满足这些规则。看见块已经提交，不是已经按气验过 interchangeable——本页从 315 item 3 侧钉 not already gas-checked 单句。315 maxgas vs enforced bundled unbundling 在本页 item 3 完成。

2. **看见池子守了 / 看见有了 Prepare / Process / 这份块 is not already 已经由共识层验过 interchangeable，也不是已经气 bundled（315） interchangeable / 916 maxgas-notblock interchangeable / 315 maxgas item 2 GasUsed interchangeable / 915 maxgas-notused interchangeable，也不是已经四门已经结算 interchangeable / 33 four gates interchangeable。**  
   官方把池子守了和共识已经守了分开——315 bundled 第三件事常与 33 混成「看见已提交就已经按气验过或已经交差 interchangeable」，本页钉 not already consensus-enforced 单句。

3. **看见有了 Prepare / Process / 看见已提交 / 这份块 is not already 已经交差 interchangeable，也不是已经气 bundled（315） interchangeable / 916 maxgas-notblock interchangeable / 914 maxgas-noton interchangeable，也不是已经默认已经在卡气 interchangeable。**  
   官方把有了 Prepare / Process 和默认已经在卡气 / 已经交差分开。看见有了 Prepare / Process，不是已经交差 interchangeable。315 maxgas vs enforced bundled unbundling 在本页 item 3 完成。

怎样计量气、怎样在 Prepare 里卡上限、以太坊费用市场是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **已提交块 not already gas-checked ≠ 已经按气验过 interchangeable：** 官方把旧版只在池里管和应用必须自己用 Prepare / Process 卡住分开。
- **看见池子守了 not already consensus-enforced ≠ 已经由共识层验过 interchangeable：** 官方把池门和共识强制分开。
- **看见有了 Prepare / Process not already settled ≠ 已经交差 interchangeable：** 官方把有了 Prepare / Process 和已经交差分开；315 maxgas vs enforced bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已提交块 | 不是已经按气验过 | 不是四门已经结算（33） |
| 看见池子守了 | 不是已经由共识层验过 | 不是 CheckTx 绿就已经进块（33） |
| 看见有了 Prepare / Process | 不是已经交差 | 不是 MaxGas 就已经在执行（914） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看已提交块 not already gas-checked / not already consensus-enforced / not already settled 正式三事（315 余量），必须分开是不是已经按气验过、是不是已经由共识层验过、是不是已经交差。可以跳过「看见已提交就已经按气验过」。不要另写怎样计量气或怎样在 Prepare 里卡上限。315 maxgas vs enforced bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样计量气、怎样在 Prepare 里卡上限、以太坊费用市场。
- 气 bundled。那是不变量 315。
- MaxGas 就已经在执行。那是不变量 315 item 1 余量 / 914。
- 四门已经结算。那是不变量 33。
