# 例：看见 Snapshot.height 是拍快照的高度（Commit 之后）不是已经是 Query 高度；看见 Snapshot.metadata 是任意应用元数据、例如块哈希或其他核对数据不是已经全字段对上；看见 Query 可以可选回默克尔证明不是已经对上 AppHash

**层次**：实现 / Snapshot 高度余量。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Snapshot / Query Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「Snapshot.height 是拍快照的高度（Commit 之后）不是已经是 Query 高度 / Snapshot.metadata 是任意应用元数据、例如块哈希或其他核对数据不是已经全字段对上 / Query 可以可选回默克尔证明不是已经对上 AppHash」，不是快照全字段（含 Metadata）对上就已经装完，也不是 Query 请求 prove 就已经对上 AppHash。不要另写怎样写 Snapshot 高度余量。

## 官方三件事

规范把 Snapshot.height 是拍快照的高度（Commit 之后）、Snapshot.metadata 是任意应用元数据例如块哈希或其他核对数据、Query 可以可选回默克尔证明写成三件独立的实现事，不是「看见填了 Snapshot 高度余量就已经是 Query 高度、已经全字段对上、已经对上 AppHash」一件事：

1. **看见 Snapshot `height` 是拍快照的高度（Commit 之后） / 看见填了 height 不是已经是 Query 高度，也不是已经装完。**  
   官方写：`height` 是拍这份快照的高度（在 `Commit` 之后）。看见填了 height，不是已经是 Query 那种含 Merkle 根的那块、代表 Height-1 提交后的状态。看见写成 Commit 之后，不是已经全字段对上就已经装完。看见有高度，不是已经交差。
2. **看见 Snapshot `metadata` 是任意应用元数据、例如块哈希或其他核对数据 / 看见填了 metadata 不是已经全字段对上，也不是已经增量验过。**  
   官方写：`metadata` 是任意应用元数据，例如 chunk 哈希或其他核对数据。看见填了 metadata，不是已经全字段（含 Metadata）对上才算同一份。看见有块哈希，不是已经在装回当中增量验过。看见能填，不是已经交差。
3. **看见 Query 可以可选回默克尔证明 / 看见能回证明 不是已经对上 AppHash，也不是已经勾了 prove。**  
   官方写：Query 可以可选回默克尔证明。看见能回证明，不是已经 Query 请求 `prove` 那种能回就回。看见有证明，不是已经 Query 回了 Proof 就对上 AppHash。看见能查，不是已经交差。

怎样写 Snapshot 高度余量、怎样填 metadata、怎样回证明是规范里的做法，本页不抄。快照全字段（含 Metadata）对上就已经装完是不变量 368，本页不抄。

## 官方为什么这样拆

- **Snapshot.height 是拍快照的高度（Commit 之后） ≠ 已经是 Query 高度：** 官方把拍快照的高度和 Query 那份高度分开。
- **Snapshot.metadata 是任意应用元数据、例如块哈希或其他核对数据 ≠ 已经全字段对上：** 官方把任意元数据和全字段对上才算同一份分开。
- **Query 可以可选回默克尔证明 ≠ 已经对上 AppHash：** 官方把可以回证明和已经对上分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Snapshot.height 是拍快照的高度（Commit 之后） | 不是已经是 Query 高度 | 不是这个 height 是含 Merkle 根的那块、代表 Height-1 提交后的状态就已经印进本头 AppHash（371） |
| Snapshot.metadata 是任意应用元数据、例如块哈希或其他核对数据 | 不是已经全字段对上 | 不是快照全字段（含 Metadata）对上就已经装完（368） |
| Query 可以可选回默克尔证明 | 不是已经对上 AppHash | 不是 Query 请求 prove 就已经对上 AppHash（383） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 Snapshot 高度余量就已经是 Query 高度、已经全字段对上、已经对上 AppHash」，必须分开 Snapshot.height 是拍快照的高度（Commit 之后）是不是已经是 Query 高度、Snapshot.metadata 是任意应用元数据、例如块哈希或其他核对数据是不是已经全字段对上、Query 可以可选回默克尔证明是不是已经对上 AppHash。可以跳过「看见填了 Snapshot 高度余量就已经是 Query 高度」。不要另写怎样写 Snapshot 高度余量。

## 本页不抄

- 怎样写 Snapshot 高度余量、怎样填 metadata、怎样回证明。
- 这个 height 是含 Merkle 根的那块、代表 Height-1 提交后的状态就已经印进本头 AppHash。那是不变量 371。
- 快照全字段（含 Metadata）对上就已经装完。那是不变量 368。
- Query 请求 prove 就已经对上 AppHash。那是不变量 383。
