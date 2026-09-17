# 例：看见 Finalize 等价于 ABCI 1.0 那三步 is not already four gates interchangeable / not already settled interchangeable / not already no Prepare-Process interchangeable

**层次**：实现 / Finalize 等价于 ABCI 1.0 那三步 not already four gates / not already settled / not already no Prepare-Process 正式三事（363 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Finalize 等价于 ABCI 1.0 那三步 not already four gates / not already settled / not already no Prepare-Process 正式三事（363 余量）/ not 836 finalize-equiv-notgates interchangeable / not 363 finalize-equiv-vs-gates bundled interchangeable」，不是 Finalize 回包义务 bundled（363），也不是四门已经结算（33），也不是 finresp-notgates 那条别前缀（~600），也不是 Finalize 之后就已经交差（403）。不要另写怎样写 Finalize 回包。

## 官方三件事

1. **看见 Finalize 等价于 ABCI 1.0 的 `BeginBlock` / `DeliverTx` / `EndBlock` / 看见收成一门 这份收成 is not already 已经是四门已经结算 interchangeable / 33 four gates interchangeable，也不是已经 Finalize 回包义务 bundled（363） interchangeable / 836 finalize-equiv-notgates interchangeable / 837 finalize-equiv-notslashed interchangeable / 363 finalize-equiv item 2 定奖惩 interchangeable，也不是已经 Finalize 等价于 ABCI 1.0 那三步 not already four gates / not already settled / not already no Prepare-Process 正式三事 bundled（363 item 1 余量） interchangeable / 363 finalize-equiv item 1 interchangeable。**  
   官方写：这个方法等价于 ABCI 1.0 里 `BeginBlock`、`DeliverTx`、`EndBlock` 那一串调用。看见收成一门，不是已经是 CheckTx / Prepare / Process / Finalize 四门齐了 interchangeable——本页从 363 item 1 侧钉 not already four gates 单句。363 finalize-equiv vs gates bundled unbundling 在本页 item 1 启动。不是 finresp-notgates 那条别前缀（~600）。

2. **看见收成一门 / 看见等价 / 这份收成 is not already 已经交差 interchangeable，也不是已经 Finalize 回包义务 bundled（363） interchangeable / 836 finalize-equiv-notgates interchangeable / 363 finalize-equiv item 3 必须回四列 interchangeable / 838 finalize-equiv-notchanged interchangeable，也不是已经四门已经结算 interchangeable / 33 four gates interchangeable，也不是已经 Finalize 之后就已经交差 interchangeable / 403 finafter interchangeable。**  
   官方把看见等价和已经交差分开——363 bundled 第一件事常与 33 / 403 混成「看见收成一门就已经是四门已经结算或已经交差 interchangeable」，本页钉 not already settled 单句。

3. **看见收成一门 / 看见旧三步在 / 这份收成 is not already 已经没有 Prepare / Process interchangeable，也不是已经 Finalize 回包义务 bundled（363） interchangeable / 836 finalize-equiv-notgates interchangeable / 837 finalize-equiv-notslashed interchangeable，也不是已经 finresp-notgates 那条别前缀 interchangeable / ~600 finresp-notgates interchangeable。**  
   官方把旧三步还在和已经没有 Prepare / Process 分开。看见旧三步在，不是已经没有 Prepare / Process interchangeable。363 finalize-equiv vs gates bundled unbundling 在本页 item 1 启动。

怎样写 Finalize 回包、怎样算奖惩、怎样填四列是规范里的做法，本页不抄。

## 官方为什么这样拆

- **Finalize 等价于 ABCI 1.0 那三步 not already four gates ≠ 33 interchangeable：** 官方把收成一门和四门齐了分开。
- **看见等价 not already settled ≠ 已经交差 interchangeable：** 官方把看见等价和已经交差分开。
- **看见旧三步在 not already no Prepare-Process ≠ 已经没有 Prepare / Process interchangeable：** 官方把旧三步还在和已经没有 Prepare / Process 分开；363 finalize-equiv vs gates bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Finalize 等价于 ABCI 1.0 那三步 | 不是已经是四门已经结算 | 不是四门已经结算（33） |
| 看见等价 | 不是已经交差 | 不是 Finalize 之后就已经交差（403） |
| 看见旧三步在 | 不是已经没有 Prepare / Process | 不是 finresp-notgates 别前缀（~600） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 等价于 ABCI 1.0 那三步 not already four gates / not already settled / not already no Prepare-Process 正式三事（363 余量），必须分开是不是已经是四门已经结算、是不是已经交差、是不是已经没有 Prepare / Process。可以跳过「看见收成一门就已经是四门已经结算」。不要另写怎样写 Finalize 回包。363 finalize-equiv vs gates bundled unbundling 在本页 item 1 启动；续 [`worked-example-finalize-equiv-notslashed-vs-bundled.md`](worked-example-finalize-equiv-notslashed-vs-bundled.md)（不变量 837 item 2）。

## 本页不抄

- 怎样写 Finalize 回包、怎样算奖惩、怎样填四列。
- Finalize 回包义务 bundled。那是不变量 363。
- 可以用 decided_last_commit 定奖惩。那是不变量 363 item 2 余量 / 837。
- 四门已经结算。那是不变量 33。
- finresp-notgates 别前缀。那是不变量 ~600。
- Finalize 之后就已经交差。那是不变量 403。
