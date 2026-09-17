# 模式：把 Commit Usage persist signal 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Commit Usage。  
**例**：[Signal persist ≠ 已经在 Finalize 改了就已经落盘](../../tracks/implementation/worked-example-commitpersist-vs-finalize.md)。

## 三个名字

1. **Signal persist application state 不是已经在 Finalize 改了就已经落盘：** 看见叫 Commit 让应用落盘不是已经引擎 persist tx outputs / AppHash / ResultsHash interchangeable。
2. **Expected persist at end of this call 不是已经 Commit 不带参数就等于已经落盘：** 看见应在这次 Commit 返回前落盘不是已经 signal 就已经交差 interchangeable。
3. **Historical blocks for auditing / replay / light client 不是已经 retain_height 默认 0 就等于已经在剪：** 看见历史块还可能要用于审计 / 回放 / 轻客户端验不是已经能剪就等于已经没有历史 interchangeable。

## 为什么要分开叫

官方把 persist signal、expected persist at end of this call、Historical blocks may also be required 和 Finalize 已经落盘、Commit 空请求、retain_height 默认 0 写成三个名字。把它们叫成一个「看见叫了 Commit 就已经落盘」，会把应用 Commit 落盘、Commit 空请求、历史块用途 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Commit Usage，先数清问的是 Signal persist application state 是不是已经在 Finalize 改了就已经落盘、Expected persist at end of this call 是不是已经 Commit 不带参数就等于已经落盘，还是 Historical blocks required for auditing / replay / light client 是不是已经 retain_height 默认 0 就等于已经在剪，再决定要不要同一次发布。
