# 例：看见应用高度比引擎高不是已经允许；看见块进了 blockstore 不是已经 Commit；看见启动 Info 对上了不是已经能跳步

**层次**：实现 / Crash Recovery。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Crash Recovery。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「应用高度比引擎高不是已经允许 / 块进了 store 不是已经 Commit / 启动 Info 对上不是已经能跳步」，不是半写已经原子，也不是 WAL 已经 fsync。不要另写怎样落盘或怎样写 Commit。

## 官方三件事

规范把崩溃恢复写成三件独立的实现事，不是「看见块已经进 store 就已经交差、已经能单独比引擎高、已经能从任意高度接着走」一件事：

1. **看见应用高度比引擎高 / 看见应用先落了盘 不是已经允许，也不是已经能单独恢复。**  
   官方写：CometBFT 和应用**被指望一起崩**。不该出现应用已经持久化的高度，高于 CometBFT 已经持久化的最新高度。看见应用先写完，不是已经合法。看见两边高度不一样，不是已经能各醒各的。看见能单独重启应用，不是已经和半写已经原子同一句。
2. **看见块已经进 blockstore / 看见 Finalize 结果已经落盘 不是已经交差，也不是已经 Commit。**  
   官方写：一个高度算持久化，要走三步，最后一步才是应用的 `Commit`，也是应用**唯一**被指望持久化/提交自己状态的地方。三步是：块进 blockstore；CometBFT 存下 `FinalizeBlockResponse` 回的状态；应用在 `Commit` 里提交。看见块存了，不是已经交差。看见结果存了，不是应用已经提交。看见三步，不是已经原子。
3. **看见启动 Info / 看见对上了 不是已经是任意高度，也不是已经能跳步。**  
   官方写：醒来时 CometBFT 在 Info 连接上叫 `Info`，应用**必须**回与上次成功完成 `Commit` 的那一块一致的信息。只走到 `block_stored`：重放 `FinalizeBlock` 及之后。`block_stored` 加 `state_stored`：再执行一次 `FinalizeBlock` 来对结果，对不上就 panic。三步都齐：才进下一高度。乱序会 panic。第一块 Commit 之前、`InitChain` 之后崩了：应用应仍在高度 0，`InitChain` **会再叫一次**。看见 Info 绿了，不是已经能从半截高度接着走。看见对上了，不是已经跳过重放。看见 InitChain 叫过，不是已经不用再叫。

怎样落盘、怎样写 Commit、怎样做 WAL 旋转是规范里的取值或做法，本页不抄。半写原子是不变量 5，本页不抄。

## 官方为什么这样拆

- **应用比引擎高 ≠ 已经允许：** 官方把一起崩和不许应用领先分开。
- **块进 store ≠ 已经 Commit：** 官方把三步和只有 Commit 才让应用落盘分开。
- **启动 Info 对上 ≠ 已经能跳步：** 官方把必须对上上次 Commit、重放、乱序 panic、InitChain 再叫分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 应用高度比引擎高 | 不是已经允许 | 不是半写已经原子（5） |
| 块进 store / 结果落盘 | 不是已经 Commit | 不是 WAL 已经 fsync（298） |
| 启动 Info 对上 | 不是已经能跳步 | 不是启动对齐已经是快照重放（314） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「崩溃已经能恢复」，必须分开应用比引擎高是不是已经允许、块进 store 是不是已经 Commit、启动 Info 对上是不是已经能跳步。可以跳过「看见块已经进 store 就已经交差」。不要另写怎样落盘或怎样写 Commit。320 crash-steps vs commit bundled unbundling 完成（1019 item 1 / 1020 item 2 / 1021 item 3）；精读 [`worked-example-crashrec-notahead-vs-bundled.md`](worked-example-crashrec-notahead-vs-bundled.md)（不变量 1019 item 1）。

## 本页不抄

- 怎样落盘、怎样写 Commit、怎样做 WAL 旋转。
- 半写原子。那是不变量 5。
- WAL fsync。那是不变量 298。
- 启动对齐当快照重放。那是不变量 314。
