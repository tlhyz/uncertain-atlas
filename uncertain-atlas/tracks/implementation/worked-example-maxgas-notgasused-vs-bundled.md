# 例：看见有 GasUsed / GasWanted 过了池门 / 应用应强制不等式 is not already already in consensus interchangeable / already practical-gas checked interchangeable / already engine-enforced inequality interchangeable

**层次**：实现 / GasUsed 不是已经算进共识 not already in consensus / not already practical-gas checked / not already engine-enforced inequality 正式三事（315 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Gas。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「GasUsed 不是已经算进共识 not already in consensus / not already practical-gas checked / not already engine-enforced inequality 正式三事（315 余量）/ not 705 maxgas-notgasused interchangeable / not 315 maxgas bundled interchangeable」，不是 MaxGas vs enforced bundled（315），也不是 MaxGas 不是已经在执行（704 item 1 余量）或已提交块不是已经按气验过（706 item 3 余量）。不要另写怎样计量气或怎样在 Prepare 里卡上限。

## 官方三件事

规范把 Requirements 里回包有 `GasWanted` / `GasUsed`、应用应强制 `GasUsed <= GasWanted`、当 `MaxGas > -1` 时 CometBFT 只强制内存池每笔 `GasWanted <= MaxGas` 与提议一块时 `GasWanted` 之和 `<= MaxGas`、**`GasUsed` 字段被 CometBFT 忽略** 和「已经是有 GasUsed 就已经算进共识 interchangeable / 已经是 GasWanted 过了池门就已经按实用气验过 interchangeable / 已经是应用应强制就已经由引擎强制该不等式 interchangeable / 已经是 MaxGas vs enforced bundled interchangeable」分开写成三件独立的实现事，不是「看见有 GasUsed 就已经算进共识 interchangeable / 就已经按实用气验过 interchangeable / 就已经由引擎强制不等式 interchangeable」一件事：

1. **看见有 GasUsed / 看见回包 GasUsed / 看见 GasUsed 字段在 is not already 已经算进共识 interchangeable / 已经 in consensus interchangeable / 已经被 CometBFT 用进共识 interchangeable / 315 maxgas bundled interchangeable / 704 maxgas-notenforced interchangeable / maxgas-sold-as-enforced interchangeable，也不是已经 MaxGas vs enforced bundled（315） interchangeable / 705 maxgas-notgasused interchangeable / 315 maxgas item 2 interchangeable，也不是已经 GasUsed 不是已经算进共识 not already in consensus / not already practical-gas checked / not already engine-enforced inequality 正式三事 bundled（315 item 2 余量） interchangeable / 315 maxgas item 2 interchangeable，也不是已经 MaxGas 不是已经在执行（704） interchangeable / 706 maxgas-notcommitted interchangeable / 33 four gates interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：**`GasUsed` 字段被 CometBFT 忽略。** 看见有 GasUsed，不是已经算进共识 interchangeable——315 钉 bundled 三事，本页从 item 2 侧钉 not already in consensus 单句。看见回包 GasUsed，不是已经 MaxGas vs enforced bundled（315） interchangeable——315 钉 bundled，本页钉 item 2 第一件事。看见 GasUsed 字段在，不是已经 MaxGas 不是已经在执行（704） interchangeable——704 另钉 item 1，本页钉 item 2 第一件事。315 maxgas vs enforced bundled unbundling 在本页 item 2 续。

2. **看见 GasWanted 过了池门 / 看见每笔 GasWanted <= MaxGas / 看见提议一块 GasWanted 之和 <= MaxGas is not already 已经按实用气验过 interchangeable / 已经 practical-gas checked interchangeable / 已经按 GasUsed 验过 interchangeable / 315 maxgas bundled interchangeable / 704 maxgas-notenforced interchangeable，也不是已经 MaxGas vs enforced bundled（315） interchangeable / 705 maxgas-notgasused interchangeable / 315 maxgas item 1 字段在 interchangeable / 315 maxgas item 3 已提交 interchangeable，也不是已经 GasUsed 不是已经算进共识 not already in consensus / not already practical-gas checked / not already engine-enforced inequality 正式三事 bundled（315 item 2 余量） interchangeable / 315 maxgas item 2 interchangeable，也不是已经算进共识（本页第一件事） interchangeable。**  
   官方把只强制 GasWanted 门和已经按实用气（GasUsed）验过路径分开——GasWanted 过了池门，不等于已经按 GasUsed 验过。看见 GasWanted 过了池门，不是已经按实用气验过 interchangeable——本页钉 not already practical-gas checked 单句。看见每笔 GasWanted <= MaxGas，不是已经 MaxGas 不是已经在执行（704） interchangeable——704 另钉 item 1，本页钉 item 2 第二件事。看见提议一块 GasWanted 之和 <= MaxGas，不是已经已提交块不是已经按气验过（706） interchangeable——706 另钉 item 3，本页钉 item 2 第二件事。315 maxgas vs enforced bundled unbundling 在本页 item 2 续。

3. **看见应用应强制 GasUsed <= GasWanted / 看见官方写应用应强制 / 看见执行或校验应在用超之前失败 is not already 已经由引擎强制该不等式 interchangeable / 已经 engine-enforced inequality interchangeable / 已经 CometBFT 强制 GasUsed <= GasWanted interchangeable / 315 maxgas bundled interchangeable / 33 four gates interchangeable，也不是已经 MaxGas vs enforced bundled（315） interchangeable / 705 maxgas-notgasused interchangeable / 315 maxgas item 1 / 315 maxgas item 3，也不是已经 GasUsed 不是已经算进共识 not already in consensus / not already practical-gas checked / not already engine-enforced inequality 正式三事 bundled（315 item 2 余量） interchangeable / 315 maxgas item 2 interchangeable，也不是已经算进共识（本页第一件事） interchangeable / 已经按实用气验过（本页第二件事） interchangeable。**  
   官方把应用应强制 `GasUsed <= GasWanted` 和已经由引擎强制该不等式路径分开——应用应强制，不等于引擎已经强制。看见应用应强制，不是已经由引擎强制该不等式 interchangeable——本页钉 not already engine-enforced inequality 单句。看见官方写应用应强制，不是已经算进共识（本页第一件事） interchangeable——三件事分开钉。看见执行或校验应在用超之前失败，不是已经四门已经结算（33） interchangeable——33 另钉。315 maxgas vs enforced bundled unbundling 在本页 item 2 完成。

怎样计量气、怎样在 Prepare 里卡上限、以太坊费用市场是规范里的取值或做法，本页不抄。MaxGas vs enforced bundled（315）、MaxGas 不是已经在执行（315 item 1 余量 / 704）、已提交块不是已经按气验过（315 item 3 余量 / 706）、MaxBytes 写成 -1（299）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **有 GasUsed not already in consensus ≠ 315 / 704 interchangeable：** 官方把 GasUsed 被忽略单句和已经算进共识路径分开。
- **GasWanted 过了池门 not already practical-gas checked ≠ 已经按 GasUsed 验过 interchangeable：** 官方把只强制 GasWanted 门单句和已经按实用气验过路径分开。
- **应用应强制 not already engine-enforced inequality ≠ 已经由引擎强制该不等式 interchangeable：** 官方把应用应强制单句和引擎已强制路径分开；315 maxgas vs enforced bundled unbundling 在本页 item 2 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 有 GasUsed | 不是 already in consensus | 不是字段在 alone（704） |
| GasWanted 过了池门 | 不是 already practical-gas checked | 不是已提交按气验 alone（706） |
| 应用应强制 | 不是 already engine-enforced inequality | 不是四门 alone（33） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 GasUsed 不是已经算进共识 not already in consensus / not already practical-gas checked / not already engine-enforced inequality 正式三事（315 余量），必须分开有 GasUsed 是不是 already in consensus interchangeable / 315 maxgas bundled interchangeable / maxgas-sold-as-enforced interchangeable、GasWanted 过了池门 是不是 already practical-gas checked interchangeable、应用应强制 是不是 already engine-enforced inequality interchangeable。可以跳过「看见有 GasUsed 就已经算进共识 interchangeable / 就已经按实用气验过 interchangeable / 就已经由引擎强制不等式 interchangeable」。不要另写怎样计量气。315 maxgas vs enforced bundled unbundling 在本页 item 2 完成；续 [`worked-example-maxgas-notcommitted-vs-bundled.md`](worked-example-maxgas-notcommitted-vs-bundled.md)（不变量 706 item 3，待写）。

## 本页不抄

- 怎样计量气、怎样在 Prepare 里卡上限、以太坊费用市场。
- MaxGas vs enforced bundled。那是不变量 315。
- MaxGas 不是已经在执行。那是不变量 315 item 1 余量 / 704。
- 已提交块不是已经按气验过。那是不变量 315 item 3 余量 / 706。
- MaxBytes 写成 -1。那是不变量 299。
- 四门已经结算。那是不变量 33。
