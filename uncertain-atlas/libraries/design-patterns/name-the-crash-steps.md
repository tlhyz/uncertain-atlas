# 模式：把崩溃恢复三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Crash Recovery。  
**例**：[应用高度比引擎高 ≠ 已经允许](../../tracks/implementation/worked-example-crash-steps-vs-commit.md)。

## 三个名字

1. **应用高度比引擎高不是已经允许：** 看见应用先落盘不是已经能单独恢复。
2. **块进 store 不是已经 Commit：** 看见 Finalize 结果落盘不是应用已经提交。
3. **启动 Info 对上不是已经能跳步：** 看见绿了不是已经能从半截高度接着走。

## 为什么要分开叫

官方把一起崩、三步里只有 Commit 让应用落盘、醒来必须对上上次 Commit 写成三件事。把它们叫成一个「看见块已经进 store 就已经交差」，会把半写原子、WAL 和启动对齐一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「崩溃已经能恢复」，先数清问的是应用比引擎高不是已经允许、块进 store 不是已经 Commit，还是启动 Info 对上不是已经能跳步，再决定要不要同一次发布。
