# 例：看见 persists _v_ as the decision for height _h_ 不是已经 Application executes block _v_ / 已经交差；看见 calls FinalizeBlock with _v_'s data 不是已经 persist tx outputs / AppHash / ResultsHash；看见 The call is synchronous 不是已经异步 / 已经 +2/3 precommit 决定就已经会调 Finalize interchangeable

**层次**：实现 / FinalizeBlock When persist decision / synchronous call 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When steps 1–2。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「persist decision 不是已经 executes block v / 已经交差、calls FinalizeBlock 不是已经 persist outputs / 已经落盘、synchronous call 不是已经异步 / 已经决定触发 interchangeable」，不是 Finalize 何时调用 bundled 三事，不是 Application executes block v 三事，也不是 AppHash tx outputs ResultHash persist 三事。不要另写怎样 persist decision、怎样写同步调用。

## 官方三件事

规范把 FinalizeBlock When 第 1–2 步 persist decision / calls FinalizeBlock / synchronous call 写成三件独立的实现事，不是「看见决定了就已经 executes block v、已经 persist outputs、已经 +2/3 precommit 决定就已经会调 Finalize interchangeable」一件事：

1. **看见 _p_ persists _v_ as the decision for height _h_ / 看见把 _v_ 落成这一高的决定 不是已经 Application executes block _v_（466 第 3 步），也不是已经 Finalize + Commit 那种已经交差。**  
   官方 When 第 1 步写：_p_ persists _v_ as the decision for height _h_。看见 persist decision，不是已经 Application executes block _v_ 那种已经执行完（466 第 3 步）。看见把 _v_ 落成决定，不是已经 Finalize + Commit 那种已经交差——本页钉 persist decision，467 另钉 persist tx outputs / AppHash / ResultsHash。
2. **看见 _p_'s CometBFT calls `FinalizeBlock` with _v_'s data / 看见同步调 Finalize 不是已经 persist the transaction outputs, AppHash, and ResultsHash（467 第 5–6 步），也不是已经 decides block 触发条件（362）就已经是同一句 interchangeable。**  
   官方 When 第 2 步写：_p_'s CometBFT calls `FinalizeBlock` with _v_'s data. The call is synchronous。看见 calls FinalizeBlock，不是已经 persist tx outputs / AppHash / ResultsHash interchangeable。看见 with _v_'s data，不是已经 +2/3 precommit 同一 id(v) 才决定再调 Finalize（362）那种触发条件 interchangeable——362 钉何时决定，本页钉决定之后 persist + sync call。
3. **看见 The call is synchronous / 看见同步调用 不是已经异步 / 已经可以在返回后再改裁决，也不是已经 +2/3 precommit 决定就已经会调 Finalize interchangeable。**  
   官方写 The call is synchronous。看见同步，不是已经 ProcessProposal 调用是同步的、返回后不得再改裁决（354）那种已经 interchangeable——354 钉 Process 同步，本页钉 Finalize 同步 call。看见 synchronous call，不是已经 decides block 触发（362）就已经是同一句 interchangeable。看见调 Finalize，不是已经 executes block _v_ 就已经交差。

怎样 persist decision、怎样写同步调用是规范里的做法，本页不抄。Finalize 何时调用 bundled（362）是 +2/3 precommit 同一 id(v) 才决定再调 Finalize / 先把 v 落成决定 / 再同步调 Finalize 那套另一切片，Application executes block v（466）是 executes block v / persist decision / Process guarantee 那套另一切片，AppHash tx outputs ResultHash persist（467）是 calculates AppHash / hashes ResultHash / persists outputs 那套另一切片，Finalize 之后（403）是 Finalize 之后引擎才落盘 / 锁 mempool / 开下一高 那套另一切片，本页不抄。

## 官方为什么这样拆

- **persist decision ≠ executes block v / 已经交差：** 官方把 persist _v_ as decision 和 Application executes block _v_、Finalize + Commit 交差分开。
- **calls FinalizeBlock ≠ persist outputs / 已经落盘：** 官方把 calls FinalizeBlock with _v_'s data 和 persist tx outputs / AppHash / ResultsHash 分开。
- **synchronous call ≠ 异步 / 已经决定触发 interchangeable：** 官方把 The call is synchronous 和 Process 同步、+2/3 precommit 决定触发分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| persist decision | 不是已经 executes block v | 不是 Application executes block v（466） |
| calls FinalizeBlock | 不是已经 persist outputs | 不是 AppHash tx outputs ResultHash persist（467） |
| synchronous call | 不是已经决定触发 interchangeable | 不是 Finalize 何时调用 bundled（362） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「_p_ persists _v_ as the decision … calls FinalizeBlock … The call is synchronous」，必须分开 persist decision 是不是已经 executes block v / 已经交差、calls FinalizeBlock 是不是已经 persist outputs / 已经落盘、synchronous call 是不是已经 +2/3 precommit 决定 interchangeable。可以跳过「看见决定了就已经 executes block v」。不要另写怎样 persist decision。

## 本页不抄

- 怎样 persist decision、怎样写同步调用。
- Finalize 何时调用 bundled 三事。那是不变量 362。
- Application executes block v 三事。那是不变量 466。
- AppHash tx outputs ResultHash persist 三事。那是不变量 467。
- Finalize 之后引擎才落盘。那是不变量 403。
