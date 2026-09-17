# 例：看见 validValue 非 nil 不是已经还会调 Prepare；看见自己是提议者不是已经每轮都会调 Prepare；看见没调 Prepare 不是已经又从池子装了一份 raw 提案

**层次**：实现 / validValue 跳过 Prepare。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「validValue 非 nil 不是已经还会调 Prepare / 自己是提议者不是已经每轮都会调 Prepare / 没调 Prepare 不是已经又从池子装了一份 raw 提案」，不是候选已经是 ExecuteTxState，也不是 Prepare 没有确定性要求。不要另写怎样设 validValue。

## 官方三件事

规范把 validValue 非 nil 不再调 Prepare、只有提议者且 validValue 为 nil 才调、那条路上才会从池子收交易并造头写成三件独立的实现事，不是「看见本轮直接用它就已经还会调 Prepare、已经每轮都会调、已经又装了一份 raw 提案」一件事：

1. **看见 validValue 非 nil / 看见本轮直接用它 不是已经还会调 Prepare，也不是已经能再改列表。**  
   官方写：若 *p* 在一轮 *r*、高度 *h* 有非 `nil` 的 *validValue*，共识算法用它当提案，**不**再调 `PrepareProposal`。看见直接用了，不是已经还会调。看见有 validValue，不是已经能再改列表。看见锁住了，不是已经交差。
2. **看见只有提议者且 validValue 为 nil 才会调 Prepare / 看见自己是提议者 不是已经每轮都会调 Prepare，也不是已经交差。**  
   官方写：验证者 *p* 进入一轮 *r*、高度 *h*，且 *p* 是提议者，**并且** *p* 的 *validValue* 为 `nil`，才会走 Prepare 这条路。看见是提议者，不是已经会调。看见进了这一轮，不是已经是 validValue 为 nil。看见规范写了 When，不是已经每轮都会叫。
3. **看见 validValue 非 nil 时不会再从池子按优先级收交易、不会再造头 / 看见没调 Prepare 不是已经又装了一份 raw 提案，也不是已经从提案拿掉 tx。**  
   官方写：只有走 Prepare 那条路时，引擎才从内存池按优先级收未决交易并造头。看见没调 Prepare，不是已经又收了一遍池子。看见用了 validValue，不是已经是一份新的 raw 提案。看见跳过了，不是已经从提案拿掉 tx。

怎样设 validValue、怎样从池子收交易、怎样造头是规范里的做法，本页不抄。候选已经是 ExecuteTxState 是不变量 311，本页不抄。

## 官方为什么这样拆

- **validValue 非 nil ≠ 已经还会调 Prepare：** 官方把直接用 validValue 和还会调 Prepare 分开。
- **自己是提议者 ≠ 已经每轮都会调 Prepare：** 官方把提议者和 validValue 为 nil 才调分开。
- **没调 Prepare ≠ 已经又装了一份 raw 提案：** 官方把跳过 Prepare 和从池子再收一遍分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| validValue 非 nil | 不是已经还会调 Prepare | 不是候选已经是 ExecuteTxState（311） |
| 自己是提议者 | 不是已经每轮都会调 Prepare | 不是 Prepare 没有确定性要求（338） |
| 没调 Prepare | 不是已经又装了一份 raw 提案 | 不是从提案拿掉 tx 就已经从内存池删掉（355） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见本轮直接用它就已经还会调 Prepare、已经每轮都会调、已经又装了一份 raw 提案」，必须分开 validValue 非 nil 是不是已经还会调 Prepare、自己是提议者是不是已经每轮都会调 Prepare、没调 Prepare 是不是已经又装了一份 raw 提案。可以跳过「看见本轮直接用它就已经还会调 Prepare」。不要另写怎样设 validValue。

## 本页不抄

- 怎样设 validValue、怎样从池子收交易、怎样造头。
- 候选已经是 ExecuteTxState。那是不变量 311。
- Prepare 没有确定性要求。那是不变量 338。
- 从提案拿掉 tx 就已经从内存池删掉。那是不变量 355。
