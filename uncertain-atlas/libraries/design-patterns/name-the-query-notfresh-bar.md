# 模式：把查到了不是已经新鲜 not already fresh / not already tip / not already decided-state 正式三事（329 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Query。  
**例**：[查到了 not already fresh ≠ bundled（329）](../../tracks/implementation/worked-example-query-notfresh-vs-bundled.md)。

## 三个名字

1. **查到了 不是 already fresh：** 看见查到了 / 本地有这份 / 查有结果，不是已经新鲜 interchangeable / 已经新鲜交差 interchangeable，不是 329 query bundled interchangeable / 33 four gates interchangeable / query-sold-as-replicated interchangeable。

2. **跟上了尖 不是 already tip：** 看见跟上了尖 / 当前尖 / 尖上这份，不是已经是当前尖 interchangeable / 已经尖交差 interchangeable，不是 325 queryproof interchangeable / 329 query item 1 interchangeable。

3. **决定块之后那份 不是 already decided-state：** 看见决定块之后那份 / 决定后状态 / 已决定状态，不是已经是决定块之后那份 interchangeable / 已经决定后交差 interchangeable，不是 314 querystate interchangeable / 329 query item 3 interchangeable。

官方把查到了单句、already fresh、already tip、already decided-state 写成三个名字。把它们叫成一个「看见查到了就已经新鲜 interchangeable / 就已经是当前尖 interchangeable / 就已经是决定块之后那份 interchangeable」，会把 not already fresh、not already tip、not already decided-state 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看查到了不是已经新鲜 not already fresh / not already tip / not already decided-state 正式三事（329 余量），先数清问的是查到了 是不是 already fresh / 329 / query-sold-as-replicated，是不是跟上了尖 是不是 already tip，还是决定块之后那份 是不是 already decided-state，再决定要不要同一次发布。329 query vs replicated bundled unbundling 在本页 item 2 续。
