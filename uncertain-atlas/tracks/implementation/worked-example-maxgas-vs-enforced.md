# 例：看见 MaxGas 不是已经在执行；看见 GasUsed 不是已经算进共识；看见已提交块不是已经按气限验过

**层次**：实现 / 气。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Gas。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「MaxGas 不是已经在执行 / GasUsed 不是已经算进共识 / 已提交块不是已经按气限验过」，不是 MaxBytes 写成 -1 已经没有上限，也不是仓库默认 MaxBytes 已经是第一轮 SLA。不要另写怎样计量气或怎样在 Prepare 里卡上限。

## 官方三件事

规范把 CometBFT 的气写成三件独立的实现事，不是「看见有 MaxGas 就已经在执行、已经按 GasUsed 验、已经保证已提交块守上限」一件事：

1. **看见 MaxGas / 看见回包里有气字段 / 看见官方说学了以太坊 不是已经在执行，也不是已经有意义。**  
   官方写：CometBFT 学了类似的抽象，但只用得**可选且弱**，让应用自己定义执行代价。`ConsensusParams.Block.MaxGas` 限制一块里所有交易能用的总气。**默认值是 `-1`，表示块气限不执行，或者说气这个概念没有意义。** 看见字段在，不是已经在卡。看见写成 -1，不是已经和 MaxBytes 写成 -1 同一句。看见学了以太坊，不是已经有费用市场。
2. **看见 GasWanted / 看见 GasUsed 不是已经由 CometBFT 按实用气验过，也不是已经算进共识。**  
   官方写：回包里有 `GasWanted`（发送者愿意用的上限）和 `GasUsed`（实际用了多少）。应用应强制 `GasUsed <= GasWanted`，执行或校验应在用超之前失败。当 `MaxGas > -1` 时，CometBFT 只强制：内存池里每笔 `GasWanted <= MaxGas`，提议一块时 `GasWanted` 之和 `<= MaxGas`。**`GasUsed` 字段被 CometBFT 忽略。** 看见有 GasUsed，不是已经算进共识。看见 GasWanted 过了池门，不是已经按实用气验过。
3. **看见已提交块 / 看见旧版只在内存池管气 不是已经保证这块守了气限，也不是已经由共识层验过。**  
   官方写：v0.34.x 及更早，CometBFT **在共识里不强制任何气规则**，只在内存池管。因此**不保证**已提交块满足这些规则。超了气限时，要由应用回非零码。从 v0.37.x 有了 `PrepareProposal` / `ProcessProposal` 之后，应用才能让所有被提议、被投票、因而被决定的块都守 `MaxGas`。看见块已经提交，不是已经按气验过。看见池子守了，不是共识已经守了。看见有了 Prepare / Process，不是默认已经在卡气。

怎样计量气、怎样在 Prepare 里卡上限、以太坊费用市场是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **有 MaxGas ≠ 已经在执行：** 官方把可选弱抽象和默认 -1 没有意义分开。
- **有 GasUsed ≠ 已经算进共识：** 官方把应用应守的不等式和引擎忽略 GasUsed 分开。
- **已提交 ≠ 已经按气验过：** 官方把旧版只在池里管、和应用必须自己用 Prepare / Process 卡住分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| MaxGas 默认 -1 | 不是已经在执行，也不是已经有意义 | 不是 MaxBytes 写成 -1 已经没有上限（299） |
| GasUsed | 不是已经算进共识 | 不是仓库默认 MaxBytes 已经是第一轮 SLA（63） |
| 已提交块 | 不是已经按气验过 | 不是四门已经结算（33） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「已经有气限」，必须分开 MaxGas 是不是已经在执行、GasUsed 是不是已经算进共识、已提交块是不是已经按气验过。可以跳过「看见有 MaxGas 就已经在卡」。不要另写怎样计量气或怎样在 Prepare 里卡上限。315 maxgas vs enforced bundled unbundling 启动（704 item 1）；精读 [`worked-example-maxgas-notenforced-vs-bundled.md`](worked-example-maxgas-notenforced-vs-bundled.md)（不变量 704 item 1）。

## 本页不抄

- 怎样计量气、怎样在 Prepare 里卡上限、以太坊费用市场。
- 怎样写四门。那是不变量 33。
- ExecTxResult 的 Code / Data。那是另一对象。
