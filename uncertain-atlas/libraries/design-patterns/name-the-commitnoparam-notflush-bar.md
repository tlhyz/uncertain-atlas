# 模式：把 Echo 用来测实现 not Flush / not already delivered / not Echo Usage test 正式三事（399 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Commit Request / Echo Response / Echo Usage。  
**例**：[Echo ≠ bundled（399）](../../tracks/implementation/worked-example-commitnoparam-notflush-vs-bundled.md)。

## 三个名字

1. **测实现 不是已经刷完：** 看见能测，不是已经 374 interchangeable / 733 commitnoparam-notflush interchangeable。
2. **看见能测 不是已经送到：** 看见能回，不是已经 374 interchangeable。
3. **看见能叫 不是已经 Echo Usage 测实现：** 看见测实现，不是已经 492 / 673 interchangeable。

官方把 Commit 不带参数 / Echo 回包 Message / Echo 用来测实现三条核心句拆成三个名字。把它们叫成一个「看见叫了 Commit 就已经落盘」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Echo 用来测实现 正式三事（399 余量），先数清问的是测实现是不是已经刷完 / 374、是不是已经送到 / 374、还是看见能叫是不是已经 Echo Usage 测实现 / 492 / 673，再决定要不要同一次发布。399 commitnoparam vs persist bundled unbundling 在本页 item 3 完成。
