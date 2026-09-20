# 模式：把实现了 Query 不是已经是正常运转必须有 not already required / not already filter / not already proof 正式三事（329 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Query。  
**例**：[实现了 Query not already required ≠ bundled（329）](../../tracks/implementation/worked-example-query-notrequired-vs-bundled.md)。

## 三个名字

1. **实现了 Query 不是 already required：** 看见实现了 Query / 规范写了 Query / 有 Query，不是已经是正常运转必须有 interchangeable / 已经必须有交差 interchangeable，不是 329 query bundled interchangeable / 33 four gates interchangeable / query-sold-as-replicated interchangeable。

2. **邻居过滤 不是 already filter：** 看见邻居过滤 / 按 ID IP 过滤 / 过滤查询，不是已经是邻居过滤交差 interchangeable / 已经过滤交差 interchangeable，不是 326 peerfilter interchangeable / 329 query item 1 interchangeable。

3. **默克尔证明 不是 already proof：** 看见默克尔证明 / 有 Proof / 证明回了，不是已经是默克尔证明交差 interchangeable / 已经证明交差 interchangeable，不是 325 queryproof interchangeable / 329 query item 2 interchangeable。

官方把实现了 Query 单句、already required、already filter、already proof 写成三个名字。把它们叫成一个「看见实现了 Query 就已经是正常运转必须有 interchangeable / 就已经是邻居过滤 interchangeable / 就已经是默克尔证明 interchangeable」，会把 not already required、not already filter、not already proof 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看实现了 Query 不是已经是正常运转必须有 not already required / not already filter / not already proof 正式三事（329 余量），先数清问的是实现了 Query 是不是 already required / 329 / query-sold-as-replicated，是不是邻居过滤 是不是 already filter，还是默克尔证明 是不是 already proof，再决定要不要同一次发布。329 query vs replicated bundled unbundling 在本页 item 3 完成。
