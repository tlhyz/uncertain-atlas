# 模式：把 Query 回包 key 是对上的那份数据的键不是已经是 Query 高度 not already height / not already fresh / not already settled 正式三事（380 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Response。  
**例**：[回了键 not already height ≠ bundled（380）](../../tracks/implementation/worked-example-queryindex-notheight-vs-bundled.md)。

## 三个名字

1. **回了键 不是 already height：** 看见回了键 / Query 回包 key 是对上的那份数据的键 / 回了 key，不是已经是 Query 高度 interchangeable / 已经 height interchangeable / 已经是 Query 高度交差 interchangeable，不是 380 queryindex bundled interchangeable / queryindex-sold-as-store interchangeable。

2. **有键 不是 already fresh：** 看见有键 / 有对上的那份数据的键 / 有 key 字段，不是已经新鲜 interchangeable / 已经 fresh interchangeable / 已经新鲜交差 interchangeable，不是 371 queryheight interchangeable / 377 querypath interchangeable。

3. **能回 不是 already settled：** 看见能回 / 能回 key / 有 key 回包，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 887 queryindex-notstore interchangeable / 380 queryindex item 3 interchangeable。

官方把回了键、不是已经新鲜、不是已经交差写成三个名字。把它们叫成一个「看见回了键就已经是 Query 高度 interchangeable / 就已经新鲜 interchangeable / 就已经交差 interchangeable」，会把 not already height、not already fresh、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 回包 key 是对上的那份数据的键不是已经是 Query 高度 not already height / not already fresh / not already settled 正式三事（380 余量），先数清问的是回了键 是不是 already height / 380 / queryindex-sold-as-store，是不是有键 是不是 already fresh，还是能回 是不是 already settled，再决定要不要同一次发布。380 queryindex-vs-store bundled unbundling 在本页 item 2 续。
