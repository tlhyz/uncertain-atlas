# 反模式：看见应用高度比引擎高就当成已经允许 / 看见块进了 blockstore 就当成已经 Commit / 看见启动 Info 对上了就当成已经能跳步

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Crash Recovery。  
**例**：[应用高度比引擎高 ≠ 已经允许](../../tracks/implementation/worked-example-crash-steps-vs-commit.md)。

## 塌法

1. 看见应用高度比引擎高 / 看见应用先落了盘，就当成已经允许，或当成已经能单独恢复。
2. 看见块已经进 blockstore / 看见 Finalize 结果已经落盘，就当成已经交差，或当成已经 Commit。
3. 看见启动 Info / 看见对上了，就当成已经是任意高度，或当成已经能跳步。

## 为什么会出事

官方写：两边被指望一起崩；不该出现应用持久化高度高于引擎。一个高度算持久化要走三步，最后一步才是应用的 Commit。醒来时 Info 必须对上上次成功 Commit；只存了块要重放 Finalize；乱序会 panic；第一块 Commit 之前崩了会再叫 InitChain。

## 和相邻反模式

- [half-written-state](half-written-state.md) 是半写 ≠ 已经原子，不是本页这种三步还没 Commit。
- [wal-sold-as-signed](wal-sold-as-signed.md) 是写下 ≠ 已经 fsync，不是本页。
- [querystate-sold-as-execute](querystate-sold-as-execute.md) 是启动对齐 ≠ 已经是快照重放，不是本页这种必须对上上次 Commit。
