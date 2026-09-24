# 例：看见快照全字段（含 Metadata）对上不是已经装完；看见引擎不解释 format / hash 不是已经轻验 AppHash；看见空快照也至少 1 块不是已经齐

**层次**：实现 / Snapshot 类型。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Snapshot。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「快照全字段（含 Metadata）对上不是已经装完 / 引擎不解释 format / hash 不是已经轻验 AppHash / 空快照也至少 1 块不是已经齐」，不是 Offer 收下就已经装完，也不是 ListSnapshots 回了就已经齐。不要另写怎样写 Snapshot 类型。368 snapshot-vs-identical bundled unbundling 启动（851）；精读 [`worked-example-snapident-notrestored-vs-bundled.md`](worked-example-snapident-notrestored-vs-bundled.md)（不变量 851 item 1）。

## 官方三件事

规范把快照全字段相等才算同一份、引擎不解释 format / hash、空快照也至少 1 块且网上报文有上限写成三件独立的实现事，不是「看见快照对上就已经装完、已经轻验 AppHash、已经齐」一件事：

1. **看见快照全字段（含 `Metadata`）对上才算同一份、同一份才能从各节点拉 chunk / 看见对上了 不是已经装完，也不是已经交差。**  
   官方写：一份快照只有全部字段都相等（包括 `Metadata`）才算各节点同一份。同一份才能从各节点拉 chunk。看见对上了，不是已经装完。看见能拉，不是已经齐。看见 `Metadata` 在，不是已经轻验 AppHash。
2. **看见 `format` 是应用自己的版本、引擎不解释 `format` / `hash`、只比较 `hash` / 看见有哈希 不是已经轻验 AppHash，也不是已经从创世重放。**  
   官方写：`format` 是应用自己的快照格式，用来给数据格式做版本、做不兼容改动。CometBFT 不解释这个字段。`hash` 是任意快照哈希，只在各节点同一份时相等。CometBFT 不解释哈希，只比较。看见有 format，不是已经选型。看见有哈希，不是已经轻验 AppHash。看见比过了，不是已经从创世重放。
3. **看见空快照也至少 1 块、网上一份快照报文最多 4 MB / 看见有块数 不是已经齐，也不是已经是共识常数。**  
   官方写：`chunks` 是快照里的块数，至少是 1，哪怕是空快照。网上发送时，一份快照报文最多 4 MB。看见写成 1，不是已经齐。看见有上限，不是已经是共识常数。看见能发，不是已经装完。

怎样编 `Snapshot`、怎样切块、怎样比较哈希是规范里的做法，本页不抄。Offer 收下就已经装完是不变量 321，本页不抄。

## 官方为什么这样拆

- **全字段（含 Metadata）对上 ≠ 已经装完：** 官方把同一份和已经装完分开。
- **引擎不解释 format / hash ≠ 已经轻验 AppHash：** 官方把比较哈希和轻验 AppHash 分开。
- **空快照也至少 1 块 ≠ 已经齐：** 官方把至少 1 块和已经齐分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 全字段（含 Metadata）对上 | 不是已经装完 | 不是 Offer 收下就已经装完（321） |
| 引擎不解释 format / hash | 不是已经轻验 AppHash | 不是 ListSnapshots 回了就已经齐（322） |
| 空快照也至少 1 块 | 不是已经齐 | 不是应用快照就已经从创世重放（38） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见快照对上就已经装完、已经轻验 AppHash、已经齐」，必须分开全字段（含 Metadata）对上是不是已经装完、引擎不解释 format / hash 是不是已经轻验 AppHash、空快照也至少 1 块是不是已经齐。可以跳过「看见快照对上就已经装完」。不要另写怎样写 Snapshot 类型。368 snapshot-vs-identical bundled unbundling 启动（851）。

## 本页不抄

- 怎样编 `Snapshot`、怎样切块、怎样比较哈希。
- Offer 收下就已经装完。那是不变量 321。
- ListSnapshots 回了就已经齐。那是不变量 322。
- 应用快照就已经从创世重放。那是不变量 38。
