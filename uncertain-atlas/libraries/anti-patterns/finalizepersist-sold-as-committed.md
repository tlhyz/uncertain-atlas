# 反模式：看见 Finalize 改了状态就当成已经落盘 / 看见必须在 Commit 落盘就当成已经在 Finalize 落了 / 看见记住上次成功 Commit 高度就当成已经能跳步

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) FinalizeBlock / Commit。  
**例**：[Finalize 改了状态 ≠ 已经落盘](../../tracks/implementation/worked-example-finalize-persist-vs-commit.md)。

## 塌法

1. 看见 `FinalizeBlock` 改了状态 / 看见决定块已经交给应用，就当成已经落盘，或当成已经交差。
2. 看见必须在 `Commit` 落盘 / 看见 `Commit` 前返回，就当成已经在 Finalize 落了，或当成已经解锁。
3. 看见记住上次成功 `Commit` 的高度 / 看见能告诉引擎从哪接，就当成已经能单独比引擎高，或当成已经能跳步。

## 为什么会出事

官方写：Finalize 用来转移状态，但 MUST NOT 持久化。持久化 MUST 在 Commit 里做，返回之前做完。应用必须记住最近一次成功 Commit 的高度，好告诉引擎崩溃之后从哪接。记住高度不是已经允许领先，也不是已经跳过重放。

## 和相邻反模式

- [crashsteps-sold-as-committed](crashsteps-sold-as-committed.md) 是应用比引擎高 ≠ 已经允许 / 块进 store ≠ 已经 Commit / 启动 Info 对上 ≠ 已经能跳步，不是本页这种 Finalize 禁令。
- [commitlock-sold-as-rpc](commitlock-sold-as-rpc.md) 是默认锁 ≠ 已经 RPC 安全 / Commit 里等广播 ≠ 已经能往下走，不是本页。
- [half-written-state](half-written-state.md) 是半写 ≠ 已经原子，不是本页这种 MUST NOT 在 Finalize 落盘。
