# 反模式：把 H+1 立刻用了新参数 not already validator H+2 / not already last_commit H+3 / not already settled 正式三事（333 余量） 卖成 已经是验证人集合那种 H+2 才计票 / 已经是 H+3 才带 last_commit / 已经交差

**层次**：实现 / ConsensusParams 生效延迟。  
**分类**：建议（产品）。  
**对应例**：[worked-example-params-delay-notvalset-vs-bundled.md](../../tracks/implementation/worked-example-params-delay-notvalset-vs-bundled.md)。

官方把本高回了 ConsensusParams / H+1 立刻用了新参数 / 参数更新写了 H+1 三条核心句写成三件独立的实现事。把它们卖成已经是验证人集合那种 H+2 才计票 / 已经是 H+3 才带 last_commit / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 H+1 立刻用了新参数 正式三事（333 余量），必须分开 not already validator H+2、not already last_commit H+3、not already settled 三件事，不要和 333 / 35 / 459 / 911 / 913 糊成一句。

## 和相邻反模式

- [params-delay-noteffective-sold-as-bundled](params-delay-noteffective-sold-as-bundled.md) 是本高回了单句边界（911 item 1），不是本页参数延迟 ≠ 集合延迟边界。
- 验证人集合 H+1 / H+2 / H+3 是不变量 35，不是本页参数 H+1 立刻生效边界。
