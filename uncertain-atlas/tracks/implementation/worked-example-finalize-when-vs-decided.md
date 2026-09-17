# 例：看见收到提案和全部块片并且 +2/3 precommit 同一 id(v) 才决定再调 Finalize 不是已经会调 Finalize；看见先把 v 落成这一高的决定再同步调 Finalize 不是已经交差；看见应用回了 AppHash 和各笔输出引擎把输出哈希进 ResultHash 不是已经印进本头

**层次**：实现 / Finalize 何时调用。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「收到提案和全部块片并且 +2/3 precommit 同一 id(v) 才决定再调 Finalize 不是已经会调 Finalize / 先把 v 落成这一高的决定再同步调 Finalize 不是已经交差 / 应用回了 AppHash 和各笔输出引擎把输出哈希进 ResultHash 不是已经印进本头」，不是 +2/3 prevote 才锁住再调 ExtendVote，也不是 Finalize 改了就已经落盘。不要另写怎样写 Finalize 何时调用。

## 官方三件事

规范把 +2/3 precommit 同一 `id(v)` 并且收齐块片才决定再调 Finalize、先把决定落盘再同步调用、应用回 AppHash 和各笔输出后引擎再哈希进 ResultHash 写成三件独立的实现事，不是「看见到了这一高就已经会调 Finalize、已经交差、已经印进本头」一件事：

1. **看见收到提案和全部块片、并且 +2/3 precommit 同一 `id(v)` 才决定再调 Finalize / 看见到了这一高 不是已经会调 Finalize，也不是已经是 +2/3 prevote 才锁住再调 ExtendVote。**  
   官方写：节点 *p* 处在高度 *h*，收到提议者 *q* 的提案 *v* 和全部块片，并且收到同一 `id(v)` 的 +2/3 precommit，才决定 *v*，再调 `FinalizeBlock`。看见到了这一高，不是已经会调。看见有提案，不是已经决定。看见规范写了 When，不是已经是 prevote 那条路。
2. **看见先把 *v* 落成这一高的决定、再同步调 Finalize / 看见决定了 不是已经交差，也不是已经落盘应用状态。**  
   官方写：*p* 先把 *v* 落成高度 *h* 的决定，再由 CometBFT 同步调 `FinalizeBlock`。看见决定了，不是已经交差。看见先落了决定，不是已经落盘应用状态。看见是同步的，不是已经交差。
3. **看见应用回了 AppHash 和各笔输出、引擎把输出哈希进 ResultHash / 看见回了 不是已经印进本头，也不是已经是本头 AppHash。**  
   官方写：应用算出并回 `_AppHash_`，以及各笔执行输出；CometBFT 把这些输出哈希进 `_ResultHash_`。看见回了，不是已经印进本头。看见有 ResultHash，不是已经是本头 AppHash。看见哈希了，不是已经交差。

怎样写 Finalize 何时调用、怎样落决定、怎样算 ResultHash 是规范里的做法，本页不抄。+2/3 prevote 才锁住再调 ExtendVote 是不变量 361，本页不抄。

## 官方为什么这样拆

- **+2/3 precommit 同一 id(v) 才决定再调 Finalize ≠ 已经会调 Finalize：** 官方把决定再调和已经会调分开。
- **先把 v 落成这一高的决定再同步调 Finalize ≠ 已经交差：** 官方把落决定和交差分开。
- **应用回了 AppHash 和各笔输出引擎哈希进 ResultHash ≠ 已经印进本头：** 官方把回了和印进本头分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| +2/3 precommit 同一 id(v) 才决定再调 Finalize | 不是已经会调 Finalize | 不是 +2/3 prevote 同一 id(v) 才锁住再调 ExtendVote（361） |
| 先把 v 落成这一高的决定再同步调 Finalize | 不是已经交差 | 不是 Finalize 改了就已经落盘（335） |
| 应用回了 AppHash 和各笔输出引擎哈希进 ResultHash | 不是已经印进本头 | 不是本头 AppHash 就已经是本高度交差（147） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见到了这一高就已经会调 Finalize、已经交差、已经印进本头」，必须分开 +2/3 precommit 同一 id(v) 才决定再调 Finalize 是不是已经会调 Finalize、先把 v 落成这一高的决定再同步调 Finalize 是不是已经交差、应用回了 AppHash 和各笔输出引擎哈希进 ResultHash 是不是已经印进本头。可以跳过「看见到了这一高就已经会调 Finalize」。不要另写怎样写 Finalize 何时调用。

## 本页不抄

- 怎样写 Finalize 何时调用、怎样落决定、怎样算 ResultHash。
- +2/3 prevote 同一 id(v) 才锁住再调 ExtendVote。那是不变量 361。
- Finalize 改了就已经落盘。那是不变量 335。
- 本头 AppHash 就已经是本高度交差。那是不变量 147。
