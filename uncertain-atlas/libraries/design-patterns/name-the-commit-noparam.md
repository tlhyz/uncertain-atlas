# 模式：把 Commit 空请求三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Commit Request / Echo Response / Echo Usage。  
**例**：[Commit 不带参数 ≠ 已经落盘](../../tracks/implementation/worked-example-commitnoparam-vs-persist.md)。

## 三个名字

1. **Commit 不带参数不是已经落盘：** 看见能叫不是已经交差。
2. **Echo 回包 Message 是入参那串不是已经是入参字段：** 看见回了 Message 不是已经回显。
3. **Echo 用来测实现不是已经刷完：** 看见能测不是已经送到。

## 为什么要分开叫

官方把 Commit 不带参数、Echo 回包 `Message` 是入参那串、Echo 用来测实现写成三件事。把它们叫成一个「看见叫了 Commit 就已经落盘」，会把必须在 Commit 落盘、请求要回显的字符串和 Flush 冲排队一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见叫了 Commit 就已经落盘」，先数清问的是 Commit 不带参数不是已经落盘、Echo 回包 Message 是入参那串不是已经是入参字段，还是 Echo 用来测实现不是已经刷完，再决定要不要同一次发布。
