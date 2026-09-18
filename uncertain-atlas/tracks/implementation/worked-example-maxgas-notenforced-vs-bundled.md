# 例：看见字段在 / 写成 -1 / 学了以太坊 is not already already enforcing interchangeable / already MaxBytes synonym interchangeable / already fee market interchangeable

**层次**：实现 / MaxGas 不是已经在执行 not already enforcing / not already MaxBytes synonym / not already fee market 正式三事（315 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Gas。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「MaxGas 不是已经在执行 not already enforcing / not already MaxBytes synonym / not already fee market 正式三事（315 余量）/ not 704 maxgas-notenforced interchangeable / not 315 maxgas bundled interchangeable」，不是 MaxGas vs enforced bundled（315），也不是 GasUsed 不是已经算进共识（705 item 2 余量）或已提交块不是已经按气验过（706 item 3 余量）。不要另写怎样计量气或怎样在 Prepare 里卡上限。

## 官方三件事

规范把 Requirements 里 CometBFT 学了类似的抽象、但只用得**可选且弱**、让应用自己定义执行代价、`ConsensusParams.Block.MaxGas` 限制一块里所有交易能用的总气、**默认值是 `-1`，表示块气限不执行，或者说气这个概念没有意义** 和「已经是字段在就已经在执行 interchangeable / 已经是写成 -1 就已经和 MaxBytes 写成 -1 同一句 interchangeable / 已经是学了以太坊就已经有费用市场 interchangeable / 已经是 MaxGas vs enforced bundled interchangeable」分开写成三件独立的实现事，不是「看见有 MaxGas 就已经在卡 interchangeable / 就已经和 MaxBytes -1 同一句 interchangeable / 就已经有费用市场 interchangeable」一件事：

1. **看见 MaxGas / 看见字段在 / 看见回包里有气字段 is not already 已经在执行 interchangeable / 已经 enforcing interchangeable / 已经在卡 interchangeable / 315 maxgas bundled interchangeable / 299 maxbytes interchangeable / maxgas-sold-as-enforced interchangeable，也不是已经 MaxGas vs enforced bundled（315） interchangeable / 704 maxgas-notenforced interchangeable / 315 maxgas item 1 interchangeable，也不是已经 MaxGas 不是已经在执行 not already enforcing / not already MaxBytes synonym / not already fee market 正式三事 bundled（315 item 1 余量） interchangeable / 315 maxgas item 1 interchangeable，也不是已经 GasUsed 不是已经算进共识（705） interchangeable / 706 maxgas-notcommitted interchangeable / 33 four gates interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：CometBFT 学了类似的抽象，但只用得**可选且弱**；默认 `-1` 表示块气限不执行。看见字段在，不是已经在卡 interchangeable——315 钉 bundled 三事，本页从 item 1 侧钉 not already enforcing 单句。看见 MaxGas，不是已经 MaxGas vs enforced bundled（315） interchangeable——315 钉 bundled，本页钉 item 1 第一件事。看见回包里有气字段，不是已经 GasUsed 不是已经算进共识（705） interchangeable——705 另钉 item 2，本页钉 item 1 第一件事。315 maxgas vs enforced bundled unbundling 在本页 item 1 启动。

2. **看见写成 -1 / 看见默认 -1 / 看见 MaxGas = -1 is not already 已经和 MaxBytes 写成 -1 同一句 interchangeable / 已经 MaxBytes synonym interchangeable / 已经没有上限同一句 interchangeable / 315 maxgas bundled interchangeable / 299 maxbytes interchangeable，也不是已经 MaxGas vs enforced bundled（315） interchangeable / 704 maxgas-notenforced interchangeable / 315 maxgas item 2 GasUsed interchangeable / 315 maxgas item 3 已提交 interchangeable，也不是已经 MaxGas 不是已经在执行 not already enforcing / not already MaxBytes synonym / not already fee market 正式三事 bundled（315 item 1 余量） interchangeable / 315 maxgas item 1 interchangeable，也不是已经在执行（本页第一件事） interchangeable。**  
   官方把默认 `-1` 表示块气限不执行 / 气这个概念没有意义 和已经和 MaxBytes 写成 -1 同一句路径分开——写成 -1，不等于已经和 MaxBytes -1 同一句。看见写成 -1，不是已经和 MaxBytes 写成 -1 同一句 interchangeable——本页钉 not already MaxBytes synonym 单句。看见默认 -1，不是已经 GasUsed 不是已经算进共识（705） interchangeable——705 另钉 item 2，本页钉 item 1 第二件事。看见 MaxGas = -1，不是已经已提交块不是已经按气验过（706） interchangeable——706 另钉 item 3，本页钉 item 1 第二件事。315 maxgas vs enforced bundled unbundling 在本页 item 1 启动。

3. **看见学了以太坊 / 看见官方说学了类似抽象 / 看见类似以太坊气 is not already 已经有费用市场 interchangeable / 已经 fee market interchangeable / 已经以太坊费用市场 interchangeable / 315 maxgas bundled interchangeable / 33 four gates interchangeable，也不是已经 MaxGas vs enforced bundled（315） interchangeable / 704 maxgas-notenforced interchangeable / 315 maxgas item 2 / 315 maxgas item 3，也不是已经 MaxGas 不是已经在执行 not already enforcing / not already MaxBytes synonym / not already fee market 正式三事 bundled（315 item 1 余量） interchangeable / 315 maxgas item 1 interchangeable，也不是已经在执行（本页第一件事） interchangeable / 已经和 MaxBytes -1 同一句（本页第二件事） interchangeable。**  
   官方把学了类似抽象和已经有费用市场路径分开——学了以太坊，不等于已经有费用市场。看见学了以太坊，不是已经有费用市场 interchangeable——本页钉 not already fee market 单句。看见官方说学了类似抽象，不是已经在执行（本页第一件事） interchangeable——三件事分开钉。看见类似以太坊气，不是已经四门已经结算（33） interchangeable——33 另钉。315 maxgas vs enforced bundled unbundling 在本页 item 1 完成。

怎样计量气、怎样在 Prepare 里卡上限、以太坊费用市场是规范里的取值或做法，本页不抄。MaxGas vs enforced bundled（315）、GasUsed 不是已经算进共识（315 item 2 余量 / 705）、已提交块不是已经按气验过（315 item 3 余量 / 706）、MaxBytes 写成 -1 已经没有上限（299）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **字段在 not already enforcing ≠ 315 / 299 interchangeable：** 官方把可选弱抽象单句和已经在卡路径分开。
- **写成 -1 not already MaxBytes synonym ≠ 已经和 MaxBytes -1 同一句 interchangeable：** 官方把默认 -1 气无意义单句和 MaxBytes -1 路径分开。
- **学了以太坊 not already fee market ≠ 已经有费用市场 interchangeable：** 官方把学了类似抽象单句和已经有费用市场路径分开；315 maxgas vs enforced bundled unbundling 在本页 item 1 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 字段在 | 不是 already enforcing | 不是 GasUsed alone（705） |
| 写成 -1 | 不是 already MaxBytes synonym | 不是 MaxBytes -1 alone（299） |
| 学了以太坊 | 不是 already fee market | 不是已提交按气验 alone（706） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 MaxGas 不是已经在执行 not already enforcing / not already MaxBytes synonym / not already fee market 正式三事（315 余量），必须分开字段在 是不是 already enforcing interchangeable / 315 maxgas bundled interchangeable / maxgas-sold-as-enforced interchangeable、写成 -1 是不是 already MaxBytes synonym interchangeable、学了以太坊 是不是 already fee market interchangeable。可以跳过「看见有 MaxGas 就已经在卡 interchangeable / 就已经和 MaxBytes -1 同一句 interchangeable / 就已经有费用市场 interchangeable」。不要另写怎样计量气。315 maxgas vs enforced bundled unbundling 在本页 item 1 完成；续 [`worked-example-maxgas-notgasused-vs-bundled.md`](worked-example-maxgas-notgasused-vs-bundled.md)（不变量 705 item 2，待写）。

## 本页不抄

- 怎样计量气、怎样在 Prepare 里卡上限、以太坊费用市场。
- MaxGas vs enforced bundled。那是不变量 315。
- GasUsed 不是已经算进共识。那是不变量 315 item 2 余量 / 705。
- 已提交块不是已经按气验过。那是不变量 315 item 3 余量 / 706。
- MaxBytes 写成 -1 已经没有上限。那是不变量 299。
- 四门已经结算。那是不变量 33。
