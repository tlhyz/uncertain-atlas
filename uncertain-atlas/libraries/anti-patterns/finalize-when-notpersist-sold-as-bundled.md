# 反模式：把 先落决定再同步调 Finalize not already settled / not already persist app state / not already sync means done 正式三事（362 余量） 卖成 已经交差 / 已经落盘应用状态 / 同步调用就已经交差

**层次**：实现 / Finalize 何时调用。  
**分类**：建议（产品）。  
**对应例**：[worked-example-finalize-when-notpersist-vs-bundled.md](../../tracks/implementation/worked-example-finalize-when-notpersist-vs-bundled.md)。

官方把 +2/3 precommit 才决定再调 Finalize / 先落决定再同步调 Finalize / 回了 AppHash 和输出哈希进 ResultHash 三条核心句写成三件独立的实现事。把它们卖成已经交差 / 已经落盘应用状态 / 同步调用就已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看先落决定再同步调 Finalize 正式三事（362 余量），必须分开 not already settled、not already persist app state、not already sync means done 三件事，不要和 362 / 335 / 481 / 363 / 838 / 839 / 841 糊成一句。

## 和相邻反模式

- [finalize-when-notcall-sold-as-bundled](finalize-when-notcall-sold-as-bundled.md) 是 +2/3 precommit 才决定再调单句边界（839 item 1），不是本页先落决定边界。
- [finpersist-notpersist-sold-as-bundled](finpersist-notpersist-sold-as-bundled.md) 是 Finalize 改了就已经落盘（335），不是本页先落决定边界。
