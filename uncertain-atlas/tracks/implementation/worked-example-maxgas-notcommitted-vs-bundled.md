# 例：看见块已经提交 / 池子守了 / 有了 Prepare Process is not already already gas-checked interchangeable / already consensus-enforced interchangeable / already default Prepare Process capping interchangeable

**层次**：实现 / 已提交块不是已经按气验过 not already gas-checked / not already consensus-enforced / not already default Prepare Process capping 正式三事（315 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Gas。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「已提交块不是已经按气验过 not already gas-checked / not already consensus-enforced / not already default Prepare Process capping 正式三事（315 余量）/ not 706 maxgas-notcommitted interchangeable / not 315 maxgas bundled interchangeable」，不是 MaxGas vs enforced bundled（315），也不是 MaxGas 不是已经在执行（704 item 1 余量）或 GasUsed 不是已经算进共识（705 item 2 余量）。不要另写怎样计量气或怎样在 Prepare 里卡上限。

## 官方三件事

规范把 Requirements 里 v0.34.x 及更早 CometBFT **在共识里不强制任何气规则**、只在内存池管、因此**不保证**已提交块满足这些规则、超了气限时要由应用回非零码、从 v0.37.x 有了 `PrepareProposal` / `ProcessProposal` 之后应用才能让所有被提议、被投票、因而被决定的块都守 `MaxGas` 和「已经是块已经提交就已经按气验过 interchangeable / 已经是池子守了就已经共识守了 interchangeable / 已经是有了 Prepare / Process 就已经默认在卡气 interchangeable / 已经是 MaxGas vs enforced bundled interchangeable」分开写成三件独立的实现事，不是「看见已提交 就已经按气验过 interchangeable / 就已经共识守了 interchangeable / 就已经默认卡气 interchangeable」一件事：

1. **看见块已经提交 / 看见已提交块 / 看见旧版只在内存池管气 is not already 已经按气验过 interchangeable / 已经 gas-checked interchangeable / 已经保证这块守了气限 interchangeable / 315 maxgas bundled interchangeable / 33 four gates interchangeable / maxgas-sold-as-enforced interchangeable，也不是已经 MaxGas vs enforced bundled（315） interchangeable / 706 maxgas-notcommitted interchangeable / 315 maxgas item 3 interchangeable，也不是已经已提交块不是已经按气验过 not already gas-checked / not already consensus-enforced / not already default Prepare Process capping 正式三事 bundled（315 item 3 余量） interchangeable / 315 maxgas item 3 interchangeable，也不是已经 MaxGas 不是已经在执行（704） interchangeable / 705 maxgas-notgasused interchangeable / 299 maxbytes interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：v0.34.x 及更早在共识里不强制任何气规则，因此**不保证**已提交块满足这些规则。看见块已经提交，不是已经按气验过 interchangeable——315 钉 bundled 三事，本页从 item 3 侧钉 not already gas-checked 单句。看见已提交块，不是已经 MaxGas vs enforced bundled（315） interchangeable——315 钉 bundled，本页钉 item 3 第一件事。看见旧版只在内存池管气，不是已经 MaxGas 不是已经在执行（704） interchangeable——704 另钉 item 1，本页钉 item 3 第一件事。315 maxgas vs enforced bundled unbundling 在本页 item 3 启动。

2. **看见池子守了 / 看见内存池管了气 / 看见只在内存池管 is not already 已经共识守了 interchangeable / 已经 consensus-enforced interchangeable / 已经由共识层验过 interchangeable / 315 maxgas bundled interchangeable / 705 maxgas-notgasused interchangeable，也不是已经 MaxGas vs enforced bundled（315） interchangeable / 706 maxgas-notcommitted interchangeable / 315 maxgas item 1 字段在 interchangeable / 315 maxgas item 2 GasUsed interchangeable，也不是已经已提交块不是已经按气验过 not already gas-checked / not already consensus-enforced / not already default Prepare Process capping 正式三事 bundled（315 item 3 余量） interchangeable / 315 maxgas item 3 interchangeable，也不是已经按气验过（本页第一件事） interchangeable。**  
   官方把只在内存池管和已经由共识层验过路径分开——池子守了，不等于共识已经守了。看见池子守了，不是已经共识守了 interchangeable——本页钉 not already consensus-enforced 单句。看见内存池管了气，不是已经 GasUsed 不是已经算进共识（705） interchangeable——705 另钉 item 2，本页钉 item 3 第二件事。看见只在内存池管，不是已经 MaxGas 不是已经在执行（704） interchangeable——704 另钉 item 1，本页钉 item 3 第二件事。315 maxgas vs enforced bundled unbundling 在本页 item 3 启动。

3. **看见有了 Prepare / Process / 看见 v0.37.x 有了 PrepareProposal ProcessProposal / 看见应用能用 Prepare Process 卡 MaxGas is not already 已经默认在卡气 interchangeable / 已经 default Prepare Process capping interchangeable / 已经默认守 MaxGas interchangeable / 315 maxgas bundled interchangeable / 33 four gates interchangeable，也不是已经 MaxGas vs enforced bundled（315） interchangeable / 706 maxgas-notcommitted interchangeable / 315 maxgas item 1 / 315 maxgas item 2，也不是已经已提交块不是已经按气验过 not already gas-checked / not already consensus-enforced / not already default Prepare Process capping 正式三事 bundled（315 item 3 余量） interchangeable / 315 maxgas item 3 interchangeable，也不是已经按气验过（本页第一件事） interchangeable / 已经共识守了（本页第二件事） interchangeable。**  
   官方把有了 Prepare / Process 之后应用才能让被决定的块都守 MaxGas 和已经默认在卡气路径分开——有了 Prepare / Process，不等于默认已经在卡气。看见有了 Prepare / Process，不是已经默认在卡气 interchangeable——本页钉 not already default Prepare Process capping 单句。看见 v0.37.x 有了 PrepareProposal / ProcessProposal，不是已经按气验过（本页第一件事） interchangeable——三件事分开钉。看见应用能用 Prepare / Process 卡 MaxGas，不是已经四门已经结算（33） interchangeable——33 另钉。315 maxgas vs enforced bundled unbundling 在本页 item 3 完成。

怎样计量气、怎样在 Prepare 里卡上限、以太坊费用市场是规范里的取值或做法，本页不抄。MaxGas vs enforced bundled（315）、MaxGas 不是已经在执行（315 item 1 余量 / 704）、GasUsed 不是已经算进共识（315 item 2 余量 / 705）、MaxBytes 写成 -1（299）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **块已经提交 not already gas-checked ≠ 315 / 33 interchangeable：** 官方把不保证已提交块守气限单句和已经按气验过路径分开。
- **池子守了 not already consensus-enforced ≠ 已经由共识层验过 interchangeable：** 官方把只在内存池管单句和已经共识守了路径分开。
- **有了 Prepare / Process not already default Prepare Process capping ≠ 已经默认在卡气 interchangeable：** 官方把能力单句和默认已经在卡气路径分开；315 maxgas vs enforced bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 块已经提交 | 不是 already gas-checked | 不是字段在 alone（704） |
| 池子守了 | 不是 already consensus-enforced | 不是 GasUsed alone（705） |
| 有了 Prepare / Process | 不是 already default Prepare Process capping | 不是四门 alone（33） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看已提交块不是已经按气验过 not already gas-checked / not already consensus-enforced / not already default Prepare Process capping 正式三事（315 余量），必须分开块已经提交 是不是 already gas-checked interchangeable / 315 maxgas bundled interchangeable / maxgas-sold-as-enforced interchangeable、池子守了 是不是 already consensus-enforced interchangeable、有了 Prepare / Process 是不是 already default Prepare Process capping interchangeable。可以跳过「看见已提交就已经按气验过 interchangeable / 就已经共识守了 interchangeable / 就已经默认卡气 interchangeable」。不要另写怎样在 Prepare 里卡上限。315 maxgas vs enforced bundled unbundling 在本页 item 3 完成（704 + 705 + 706）。

## 本页不抄

- 怎样计量气、怎样在 Prepare 里卡上限、以太坊费用市场。
- MaxGas vs enforced bundled。那是不变量 315。
- MaxGas 不是已经在执行。那是不变量 315 item 1 余量 / 704。
- GasUsed 不是已经算进共识。那是不变量 315 item 2 余量 / 705。
- MaxBytes 写成 -1。那是不变量 299。
- 四门已经结算。那是不变量 33。
