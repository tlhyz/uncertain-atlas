# 例：看见 syncing_to_height 同步或重放时是目标高、否则等于本高不是已经有完整历史；看见 validator_updates 空则引擎保持当前集合不是已经没有集合；看见 Finalize 回包 events 标成非确定不是已经必须确定

**层次**：实现 / Finalize 请求回包。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「syncing_to_height 同步或重放时是目标高、否则等于本高不是已经有完整历史 / validator_updates 空则引擎保持当前集合不是已经没有集合 / Finalize 回包 events 标成非确定不是已经必须确定」，不是切进共识就已经有从创世的完整历史，也不是 InitChain 空名单就已经没有集合。不要另写怎样写 Finalize 请求回包。

## 官方三件事

规范把 `syncing_to_height` 同步或重放时是目标高、否则等于本高、`validator_updates` 空则引擎保持当前集合、Finalize 回包 `events` 标成非确定写成三件独立的实现事，不是「看见填了同步高度就已经有完整历史、已经没有集合、已经必须确定」一件事：

1. **看见 `syncing_to_height` 同步或重放时是目标高、否则等于本高 / 看见填了目标 不是已经有完整历史，也不是已经是快照重放。**  
   官方写：节点在同步或重放块时，`syncing_to_height` 等于目标高度。否则 `syncing_to_height` 等于本高。看见填了目标，不是已经有从创世的完整历史。看见在同步，不是已经是快照重放。看见等于本高，不是已经交差。
2. **看见 `validator_updates` 空则引擎保持当前集合 / 看见空着 不是已经没有集合，也不是已经改了集合。**  
   官方写：`validator_updates` 或 `consensus_param_updates` 可以空。空着时，CometBFT 保持当前值。看见空着，不是已经没有集合。看见没回人，不是已经改了集合。看见能空，不是已经是 InitChain 那种空名单。
3. **看见 Finalize 回包 `events` 标成非确定 / 看见回了事件 不是已经必须确定，也不是已经交差。**  
   官方写：`events` 的 Deterministic 列是 No。看见回了事件，不是已经必须像状态那样只依赖上一份状态和决定块。看见标成非确定，不是已经交差。看见能按类型键值索引，不是已经是结果列表同一顺序。

怎样写 Finalize 请求、怎样空着更新、怎样编事件是规范里的做法，本页不抄。切进共识就已经有从创世的完整历史是不变量 323，本页不抄。

## 官方为什么这样拆

- **syncing_to_height 同步或重放时是目标高、否则等于本高 ≠ 已经有完整历史：** 官方把同步目标高和已经有完整历史分开。
- **validator_updates 空则引擎保持当前集合 ≠ 已经没有集合：** 官方把 Finalize 空更新和 InitChain 空名单分开。
- **Finalize 回包 events 标成非确定 ≠ 已经必须确定：** 官方把事件非确定和状态必须确定分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| syncing_to_height 同步或重放时是目标高、否则等于本高 | 不是已经有完整历史 | 不是切进共识就已经有从创世的完整历史（323） |
| validator_updates 空则引擎保持当前集合 | 不是已经没有集合 | 不是 InitChain 空名单就已经没有集合（318） |
| Finalize 回包 events 标成非确定 | 不是已经必须确定 | 不是 Finalize 算出的状态就必须只依赖上一份状态和决定块（342） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了同步高度就已经有完整历史、已经没有集合、已经必须确定」，必须分开 syncing_to_height 同步或重放时是目标高、否则等于本高是不是已经有完整历史、validator_updates 空则引擎保持当前集合是不是已经没有集合、Finalize 回包 events 标成非确定是不是已经必须确定。可以跳过「看见填了同步高度就已经有完整历史」。不要另写怎样写 Finalize 请求回包。

## 本页不抄

- 怎样写 Finalize 请求、怎样空着更新、怎样编事件。
- 切进共识就已经有从创世的完整历史。那是不变量 323。
- InitChain 空名单就已经没有集合。那是不变量 318。
- Finalize 算出的状态就必须只依赖上一份状态和决定块。那是不变量 342。
