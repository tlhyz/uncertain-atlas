# 例：看见 GasUsed is not already consensus-checked interchangeable / not already counted interchangeable / not already settled interchangeable

**层次**：实现 / GasUsed not already consensus-checked / not already counted / not already settled 正式三事（315 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Gas。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、mempool。本页是「GasUsed not already consensus-checked / not already counted / not already settled 正式三事（315 余量）/ not 915 maxgas-notused interchangeable / not 315 maxgas-vs-enforced bundled interchangeable」，不是气 bundled（315），也不是仓库默认 MaxBytes 已经是第一轮 SLA（63），也不是四门已经结算（33）。不要另写怎样计量气或怎样在 Prepare 里卡上限。

## 官方三件事

1. **看见 GasWanted / 看见 GasUsed 这份回包 is not already 已经由 CometBFT 按实用气验过 interchangeable，也不是已经气 bundled（315） interchangeable / 915 maxgas-notused interchangeable / 914 maxgas-noton interchangeable / 315 maxgas item 1 MaxGas interchangeable，也不是已经 GasUsed not already consensus-checked / not already counted / not already settled 正式三事 bundled（315 item 2 余量） interchangeable / 315 maxgas item 2 interchangeable。**  
   官方写：回包里有 GasWanted 和 GasUsed。应用应强制 GasUsed <= GasWanted。当 MaxGas > -1 时，CometBFT 只强制：内存池里每笔 GasWanted <= MaxGas，提议一块时 GasWanted 之和 <= MaxGas。GasUsed 字段被 CometBFT 忽略。看见有 GasUsed，不是已经按实用气验过 interchangeable——本页从 315 item 2 侧钉 not already consensus-checked 单句。315 maxgas vs enforced bundled unbundling 在本页 item 2 续。

2. **看见 GasWanted 过了池门 / 看见有 GasUsed / 这份回包 is not already 已经算进共识 interchangeable，也不是已经气 bundled（315） interchangeable / 915 maxgas-notused interchangeable / 315 maxgas item 3 已提交 interchangeable / 916 maxgas-notblock interchangeable，也不是已经仓库默认 MaxBytes 已经是第一轮 SLA interchangeable / 63 maxbytes-sla interchangeable。**  
   官方把 GasUsed 被忽略和已经算进共识分开——315 bundled 第二件事常与 63 混成「看见有 GasUsed 就已经算进共识或已经是默认 SLA interchangeable」，本页钉 not already counted 单句。

3. **看见有 GasUsed / 看见 GasWanted 过了池门 / 这份回包 is not already 已经交差 interchangeable，也不是已经气 bundled（315） interchangeable / 915 maxgas-notused interchangeable / 914 maxgas-noton interchangeable，也不是已经四门已经结算 interchangeable / 33 four gates interchangeable。**  
   官方把有 GasUsed 和已经交差分开。看见有 GasUsed，不是已经交差 interchangeable。315 maxgas vs enforced bundled unbundling 在本页 item 2 续。

怎样计量气、怎样在 Prepare 里卡上限、以太坊费用市场是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **GasUsed not already consensus-checked ≠ 已经由 CometBFT 按实用气验过 interchangeable：** 官方把应用应守的不等式和引擎忽略 GasUsed 分开。
- **看见 GasWanted 过了池门 not already counted ≠ 已经算进共识 interchangeable：** 官方把池门 GasWanted 和共识按 GasUsed 验分开。
- **看见有 GasUsed not already settled ≠ 已经交差 interchangeable：** 官方把有 GasUsed 和已经交差分开；315 maxgas vs enforced bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| GasUsed | 不是已经算进共识 | 不是仓库默认 MaxBytes 已经是第一轮 SLA（63） |
| 看见 GasWanted 过了池门 | 不是已经按实用气验过 | 不是四门已经结算（33） |
| 看见有 GasUsed | 不是已经交差 | 不是 MaxGas 就已经在执行（914） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 GasUsed not already consensus-checked / not already counted / not already settled 正式三事（315 余量），必须分开是不是已经按实用气验过、是不是已经算进共识、是不是已经交差。可以跳过「看见有 GasUsed 就已经算进共识」。不要另写怎样计量气或怎样在 Prepare 里卡上限。315 maxgas vs enforced bundled unbundling 在本页 item 2 续；续 [`worked-example-maxgas-notblock-vs-bundled.md`](worked-example-maxgas-notblock-vs-bundled.md)（不变量 916 item 3）。

## 本页不抄

- 怎样计量气、怎样在 Prepare 里卡上限、以太坊费用市场。
- 气 bundled。那是不变量 315。
- MaxGas 就已经在执行。那是不变量 315 item 1 余量 / 914。
- 仓库默认 MaxBytes 已经是第一轮 SLA。那是不变量 63。
- 四门已经结算。那是不变量 33。
