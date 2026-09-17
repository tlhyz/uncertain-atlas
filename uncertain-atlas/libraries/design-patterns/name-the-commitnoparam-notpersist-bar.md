# 模式：把 Commit 不带参数 not already persist / not persist signal / not retain_height 正式三事（399 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Commit Request / Echo Response / Echo Usage。  
**例**：[Commit ≠ bundled（399）](../../tracks/implementation/worked-example-commitnoparam-notpersist-vs-bundled.md)。

## 三个名字

1. **不带参数 不是已经落盘：** 看见能叫，不是已经 335 interchangeable / 731 commitnoparam-notpersist interchangeable。
2. **看见能叫 不是已经 persist signal：** 看见不带参数，不是已经 481 / 701 interchangeable。
3. **看见能回 不是已经 retain_height：** 看见不带参数，不是已经 491 / 692 interchangeable。

官方把 Commit 不带参数 / Echo 回包 Message / Echo 用来测实现三条核心句拆成三个名字。把它们叫成一个「看见叫了 Commit 就已经落盘」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Commit 不带参数 正式三事（399 余量），先数清问的是不带参数是不是已经落盘 / 335、是不是已经 persist signal / 481 / 701、还是看见能回是不是已经 retain_height / 491 / 692，再决定要不要同一次发布。399 commitnoparam vs persist bundled unbundling 在本页 item 1 启动。
