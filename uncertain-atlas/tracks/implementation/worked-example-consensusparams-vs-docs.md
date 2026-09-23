# 例：看见 ConsensusParams.version 不是已经知道看的是哪一份；看见同一字段号不是已经是同一个内嵌类型；看见 spec 内部写法不齐不是已经能挑一份照做

**层次**：实现 / 共识参数跨文档。  
**分类**：事实（规范现状）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ConsensusParams 与 [Core Data Structures](https://github.com/cometbft/cometbft/blob/main/spec/core/data_structures.md) ConsensusParams。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「看见 ConsensusParams.version 不是已经知道看的是哪一份 / 同一字段号不是已经是同一个内嵌类型 / spec 内部写法不齐不是已经能挑一份照做」，不是 ConsensusParams.abci 是 ABCI 相关参数就已经切到 ABCI 2.0，也不是 app_version 进每块头就已经印进本头 AppHash。不要另写怎样编 ConsensusParams。

## 官方三件事

同一个 `ConsensusParams` 在两个官方文档里被写成两套内嵌类型表，这是事实。把它读成三件独立的实现事，不是「看见字段号对上就已经是同一个对象」一件事：

1. **看见 `ConsensusParams.version` / 看见有这一栏 不是已经知道看的是哪一份文档。**  
   两份文档都列了这一栏、都叫 `version`。看见有这一栏，不是已经知道内嵌的是哪一份定义。看见名字对上，不是已经同一份表。
2. **看见字段号 5 / 看见号相同 不是已经是同一个内嵌类型。**  
   `abci++_methods.md` 把字段 5 写成 `abci`（`ABCIParams`），并在那里写明 `ABCIParams` **自 v1.0 起已弃用**；`data_structures.md` 的字段 5 是空档，改把字段 7 写成 `feature`（`FeatureParams`）。看见号相同，不是已经是同一个类型。看见一边有、一边没有，不是已经能按号对齐。
3. **看见 spec 内部写法不齐 / 看见两份都在 不是已经能挑一份照做，也不是已经不需要点名出处。**  
   两份都是官方文档。看见两份都在，不是已经能任选一份当唯一依据。看见不齐，不是已经可以自己补一个折中定义。看见能挑，不是已经不需要在实现里点名依据哪一份、哪一版。

怎样编 `ConsensusParams`、怎样处理字段 5 与 7、怎样做参数更新是规范里的做法，本页不抄。`ConsensusParams.abci` 是 ABCI 相关参数是不变量 386，本页不抄。`app_version` 进每块头是不变量 370，本页不抄。`app_version` 在 0.34 里叫 `app_version`、`VersionParams` 里叫 `app` 见下方边界表。

## 官方为什么这样拆

- **有这一栏 ≠ 知道看的是哪一份：** 同名列在不同文档里可以内嵌不同定义。
- **字段号相同 ≠ 同一个内嵌类型：** 一份写 `abci`、一份写 `feature`，号码还错开了。
- **写法不齐 ≠ 能挑一份照做：** 两份都是官方，必须点名出处与版本。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ConsensusParams.version 有这一栏 | 不是已经知道看的是哪一份 | 不是 ConsensusParams.version 就已经是 app_version 进了头（385） |
| 字段号 5 相同 | 不是已经是同一个内嵌类型 | 不是 ConsensusParams.abci 就已经切到 ABCI 2.0（386） |
| spec 内部写法不齐 | 不是已经能挑一份照做 | 不是 app_version 进每块头就已经印进本头 AppHash（370） |
| 本页不涉及 | — | 不是 `VersionParams.app` 就已经是 0.34 的 `app_version`（见下） |

**关于 `VersionParams.app` 的一条旁证：** `data_structures.md` 在 `VersionParams` 一节写明「The `app` parameter was named `app_version` in CometBFT 0.34」——**同一个字段改过名**。这与本页第 1 条是两种不同的坑：一个是同名不同义（跨文档），一个是同义不同名（跨版本）。不要在实现里把两者当同一条。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见字段号对上就已经是同一个对象」，必须分开 ConsensusParams.version 有这一栏是不是已经知道看的是哪一份、字段号 5 相同是不是已经是同一个内嵌类型、spec 内部写法不齐是不是已经能挑一份照做。**实现里必须点名依据哪一份文档、哪一版**；不要自己补折中定义。可以跳过「看见字段号对上就已经是同一个对象」。不要另写怎样编 ConsensusParams。

## 本页不抄

- 怎样编 `ConsensusParams`、怎样处理字段 5 与 7、怎样做参数更新。
- `ConsensusParams.abci` 是 ABCI 相关参数。那是不变量 386。
- `ConsensusParams.version` 是 ABCI 应用版本。那是不变量 385。
- `app_version` 进每块头。那是不变量 370。
