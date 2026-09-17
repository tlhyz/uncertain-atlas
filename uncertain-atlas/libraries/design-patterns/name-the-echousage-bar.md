# 模式：把 Echo Usage 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Echo Request / Response / Usage。  
**例**：[Echo a string to test implementation ≠ 已经 Flush](../../tracks/implementation/worked-example-echousage-vs-flush.md)。

## 三个名字

1. **Echo a string to test implementation 不是已经 Flush / 已经送到：** 看见 Methods Echo Usage 测 client/server，不是 Flush 冲队列 interchangeable。
2. **Request Message string to echo back 不是 Response Message interchangeable：** 看见请求要回显的字符串，不是回包入参那串或 Flush interchangeable。
3. **Response Message the input string 不是已经测实现就已经刷完：** 看见回包栏 the input string，不是 Usage 测实现交差 interchangeable。

## 为什么要分开叫

官方把 Echo Usage、Echo Request Message、Echo Response Message 和 Flush（374）、Commit 空请求 bundled Echo（399）、Echo 请求 Message vs Flush（394）写成三个名字。把它们叫成一个「看见 Echo 了就已经 Flush、已经是入参字段、已经刷完」，会把测实现、请求栏、回包栏三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Echo Usage，先数清问的是 Echo a string to test implementation 是不是已经 Flush / 已经送到、Request Message string to echo back 是不是 Response Message interchangeable / 已经是 Flush、Response Message the input string 是不是已经测实现就已经刷完 interchangeable，再决定要不要同一次发布。
