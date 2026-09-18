# 例：看见 Finalize 含刚决定那块的字段不是已经是四门已经结算；看见 Finalize 实现必须确定、因为它在状态机复制里推进应用状态不是已经可以像 Prepare 那样；看见 Info 用来回应用状态信息不是已经是握手对齐

**层次**：实现 / Finalize 字段余量。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage / Info Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Finalize 含刚决定那块的字段不是已经是四门已经结算 / Finalize 实现必须确定、因为它在状态机复制里推进应用状态不是已经可以像 Prepare 那样 / Info 用来回应用状态信息不是已经是握手对齐」，不是 Finalize 等价于 ABCI 1.0 那三步就已经是四门已经结算，也不是 Finalize 算出的状态必须只依赖上一份状态和决定块就已经可以像 Prepare 那样。不要另写怎样写 Finalize 字段余量。

## 官方三件事

规范把 Finalize 含刚决定那块的字段、Finalize 实现必须确定因为它在状态机复制里推进应用状态、Info 用来回应用状态信息写成三件独立的实现事，不是「看见填了 Finalize 字段余量就已经是四门已经结算、已经可以像 Prepare 那样、已经是握手对齐」一件事：

1. **看见 Finalize 含刚决定那块的字段 / 看见填了字段 不是已经是四门已经结算，也不是已经跑过 Process。**  
   官方写：`FinalizeBlock` 含刚决定那块的字段。看见填了字段，不是已经是 Finalize 等价于 ABCI 1.0 那三步那种四门齐了。看见有刚决定那块，不是已经 Prepare / Process 同一套字段就已经跑过 Process。看见能填，不是已经交差。
2. **看见 Finalize 实现必须确定、因为它在状态机复制里推进应用状态 / 看见必须确定 不是已经可以像 Prepare 那样，也不是已经印进本头。**  
   官方写：`FinalizeBlock` 的实现必须确定，因为它在状态机复制的上下文里推进应用状态。看见必须确定，不是已经是 Req 11–12 那种算出的状态必须只依赖上一份状态和决定块。看见在复制里推进，不是已经 Prepare 没有确定性要求。看见能推进，不是已经交差。
3. **看见 Info 用来回应用状态信息 / 看见能回 不是已经是握手对齐，也不是已经是快照重放。**  
   官方写：Info 用来回应用状态信息。看见能回信息，不是已经是启动或恢复时握手对齐。看见写了应用状态，不是已经 QueryState 那种上次 Commit。看见能查，不是已经交差。

怎样写 Finalize 字段余量、怎样写确定性、怎样回 Info 是规范里的做法，本页不抄。Finalize 等价于 ABCI 1.0 那三步就已经是四门已经结算是不变量 363，本页不抄。

## 官方为什么这样拆

- **Finalize 含刚决定那块的字段 ≠ 已经是四门已经结算：** 官方把刚决定那块的字段和收成一门的三步分开。
- **Finalize 实现必须确定、因为它在状态机复制里推进应用状态 ≠ 已经可以像 Prepare 那样：** 官方把 Usage 这句必须确定和 Req 11–12 那句只依赖分开。
- **Info 用来回应用状态信息 ≠ 已经是握手对齐：** 官方把回应用状态信息和握手对齐分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Finalize 含刚决定那块的字段 | 不是已经是四门已经结算 | 不是 Finalize 等价于 ABCI 1.0 那三步就已经是四门已经结算（363） |
| Finalize 实现必须确定、因为它在状态机复制里推进应用状态 | 不是已经可以像 Prepare 那样 | 不是 Finalize 算出的状态必须只依赖上一份状态和决定块就已经可以像 Prepare 那样（342） |
| Info 用来回应用状态信息 | 不是已经是握手对齐 | 不是 Info 用来握手对齐就已经是快照重放（370） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 Finalize 字段余量就已经是四门已经结算、已经可以像 Prepare 那样、已经是握手对齐」，必须分开 Finalize 含刚决定那块的字段是不是已经是四门已经结算、Finalize 实现必须确定、因为它在状态机复制里推进应用状态是不是已经可以像 Prepare 那样、Info 用来回应用状态信息是不是已经是握手对齐。可以跳过「看见填了 Finalize 字段余量就已经是四门已经结算」。不要另写怎样写 Finalize 字段余量。407 finfields vs equiv bundled unbundling 完成（1109 item 1 / 1110 item 2 / 1111 item 3）；精读 [`worked-example-ffields-notfour-vs-bundled.md`](worked-example-ffields-notfour-vs-bundled.md)（不变量 1109 item 1）。

## 本页不抄

- 怎样写 Finalize 字段余量、怎样写确定性、怎样回 Info。
- Finalize 等价于 ABCI 1.0 那三步就已经是四门已经结算。那是不变量 363。
- Finalize 算出的状态必须只依赖上一份状态和决定块就已经可以像 Prepare 那样。那是不变量 342。
- Info 用来握手对齐就已经是快照重放。那是不变量 370。
