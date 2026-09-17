# 例：看见 Finalize 改了状态不是已经落盘；看见必须在 Commit 落盘不是已经在 Finalize 落了；看见记住上次成功 Commit 高度不是已经能跳步

**层次**：实现 / FinalizeBlock 落盘禁令。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) FinalizeBlock / Commit。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「Finalize 改了状态不是已经落盘 / 必须在 Commit 落盘不是已经在 Finalize 落了 / 记住上次成功 Commit 高度不是已经能跳步」，不是崩溃恢复那三步已经交差，也不是默认锁已经 RPC 安全。不要另写怎样落盘或怎样写 Commit。

## 官方三件事

规范把决定块之后的落盘写成三件独立的实现事，不是「看见 Finalize 改了状态就已经落盘、已经在 Finalize 落了、已经能从半截高度接着走」一件事：

1. **看见 `FinalizeBlock` 改了状态 / 看见决定块已经交给应用 不是已经落盘，也不是已经交差。**  
   官方写：共识算法决定一块之后，CometBFT 用 `FinalizeBlock` 把决定块交给应用，应用用它**转移状态**，但 **MUST NOT** 持久化。看见改了状态，不是已经写盘。看见决定块来了，不是已经 Commit。看见能转移，不是已经和半写已经原子同一句。
2. **看见必须在 `Commit` 落盘 / 看见 `Commit` 前返回 不是已经在 Finalize 落了，也不是已经解锁。**  
   官方写：持久化 **MUST** 在 `Commit` 里做。应用应在 `Commit` 里持久化自己的状态，**返回之前**做完。看见必须在 Commit 落盘，不是已经在 Finalize 落了。看见返回前写完，不是内存池锁已经放下。看见 Commit 绿了，不是已经能在 Commit 里等广播。
3. **看见记住上次成功 `Commit` 的高度 / 看见能告诉引擎从哪接 不是已经能单独比引擎高，也不是已经能跳步。**  
   官方写：应用必须记住最近一次成功跑完 `Commit` 的高度，好告诉 CometBFT 崩溃之后从哪接。看见记住了高度，不是已经允许应用比引擎高。看见能告诉从哪接，不是已经跳过重放。看见有这个高度，不是已经和启动 Info 对上是同一句。

怎样落盘、怎样写 Commit、怎样做 WAL 旋转是规范里的取值或做法，本页不抄。崩溃恢复三步是不变量 320，本页不抄。

## 官方为什么这样拆

- **Finalize 改了状态 ≠ 已经落盘：** 官方把转移状态和禁止在 Finalize 持久化分开。
- **必须在 Commit 落盘 ≠ 已经在 Finalize 落了：** 官方把唯一落盘点和 Finalize 禁令分开。
- **记住上次成功 Commit 高度 ≠ 已经能跳步：** 官方把记住高度和好告诉引擎从哪接、不许领先、不许跳步分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Finalize 改了状态 | 不是已经落盘 | 不是块进 store / Finalize 结果落盘已经 Commit（320） |
| 必须在 Commit 落盘 | 不是已经在 Finalize 落了 | 不是默认锁已经 RPC 安全 / Commit 里等广播已经能往下走（310） |
| 记住上次成功 Commit 高度 | 不是已经能跳步 | 不是半写已经原子（5） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「Finalize 改了状态就已经落盘、已经在 Finalize 落了、已经能从半截高度接着走」，必须分开 Finalize 改了是不是已经落盘、必须在 Commit 落盘是不是已经在 Finalize 落了、记住上次成功 Commit 高度是不是已经能跳步。可以跳过「看见 Finalize 改了就已经交差」。不要另写怎样落盘或怎样写 Commit。335 finpersist vs commit bundled unbundling 启动（683 item 1）；精读 [`worked-example-finpersist-notmustnot-vs-bundled.md`](worked-example-finpersist-notmustnot-vs-bundled.md)（不变量 683 item 1）。

## 本页不抄

- 怎样落盘、怎样写 Commit、怎样做 WAL 旋转。
- 应用比引擎高已经允许、块进 store 已经 Commit、启动 Info 对上已经能跳步。那是不变量 320。
- 默认锁已经 RPC 安全、Commit 前上锁已经解锁、Commit 里等广播已经能往下走。那是不变量 310。
- 半写已经原子。那是不变量 5。
