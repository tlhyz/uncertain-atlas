# 模式：把 Query 回包 value 是对上的那份数据的值不是已经对上 AppHash not already matched / not already replicated / not already settled 正式三事（380 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Response。  
**例**：[回了值 not already matched ≠ bundled（380）](../../tracks/implementation/worked-example-queryindex-notmatched-vs-bundled.md)。

## 三个名字

1. **回了值 不是 already matched：** 看见回了值 / Query 回包 value 是对上的那份数据的值 / 回了 value，不是已经对上 AppHash interchangeable / 已经 matched interchangeable / 已经对上 AppHash 交差 interchangeable，不是 380 queryindex bundled interchangeable / queryindex-sold-as-store interchangeable。

2. **有字节 不是 already replicated：** 看见有字节 / 有 value 字节 / 有值内容，不是已经复制到各节点 interchangeable / 已经 replicated interchangeable / 已经复制到各节点交差 interchangeable，不是 377 querypath interchangeable / 325 queryprove interchangeable。

3. **能读 不是 already settled：** 看见能读 / 能读 value / 有 value 回包，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 888 queryindex-notheight interchangeable / 380 queryindex item 2 interchangeable。

官方把回了值、不是已经复制到各节点、不是已经交差写成三个名字。把它们叫成一个「看见回了值就已经对上 AppHash interchangeable / 就已经复制到各节点 interchangeable / 就已经交差 interchangeable」，会把 not already matched、not already replicated、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 回包 value 是对上的那份数据的值不是已经对上 AppHash not already matched / not already replicated / not already settled 正式三事（380 余量），先数清问的是回了值 是不是 already matched / 380 / queryindex-sold-as-store，是不是有字节 是不是 already replicated，还是能读 是不是 already settled，再决定要不要同一次发布。380 queryindex-vs-store bundled unbundling 在本页 item 3 完成。
