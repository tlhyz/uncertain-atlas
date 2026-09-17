# 模式：把 Echo 回包 Message not request field / not already echoed / not Echo Usage response 正式三事（399 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Commit Request / Echo Response / Echo Usage。  
**例**：[Echo ≠ bundled（399）](../../tracks/implementation/worked-example-commitnoparam-notreqfield-vs-bundled.md)。

## 三个名字

1. **回包 Message 不是已经是入参字段：** 看见回了 Message，不是已经 394 interchangeable / 732 commitnoparam-notreqfield interchangeable。
2. **看见回了 Message 不是已经回显：** 看见能回，不是已经回显 interchangeable。
3. **看见能填 不是已经 Echo Usage Response：** 看见回包 Message，不是已经 492 / 675 interchangeable。

官方把 Commit 不带参数 / Echo 回包 Message / Echo 用来测实现三条核心句拆成三个名字。把它们叫成一个「看见叫了 Commit 就已经落盘」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Echo 回包 Message 正式三事（399 余量），先数清问的是回包 Message 是不是已经是入参字段 / 394、是不是已经回显、还是看见能填是不是已经 Echo Usage Response / 492 / 675，再决定要不要同一次发布。399 commitnoparam vs persist bundled unbundling 在本页 item 2 续。
