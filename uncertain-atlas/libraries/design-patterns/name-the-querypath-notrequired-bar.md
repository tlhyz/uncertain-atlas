# 模式：把规范建议允许 /accounts / /votes 这类查询不是已经是正常运转必须有 not already required / not already replicated / not already fresh 正式三事（377 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Request。  
**例**：[写了类型路径 not already required ≠ bundled（377）](../../tracks/implementation/worked-example-querypath-notrequired-vs-bundled.md)。

## 三个名字

1. **写了类型路径 不是 already required：** 看见写了类型路径 / 规范建议允许 /accounts / /votes 这类查询 / 写了 /accounts 或 /votes，不是已经是正常运转必须有 interchangeable / 已经 required interchangeable / 已经是正常运转必须有交差 interchangeable，不是 377 querypath bundled interchangeable / querypath-sold-as-store interchangeable。

2. **建议允许 不是 already replicated：** 看见建议允许 / 规范建议允许 / 应当允许，不是已经复制到各节点 interchangeable / 已经 replicated interchangeable / 已经复制到各节点交差 interchangeable，不是 329 query replicated interchangeable / 879 querypath-notengine interchangeable。

3. **能查账户 不是 already fresh：** 看见能查账户 / 能查 /accounts / 能查类型，不是已经新鲜 interchangeable / 已经 fresh interchangeable / 已经新鲜交差 interchangeable，不是 878 querypath-notheight interchangeable / 371 queryheight interchangeable。

官方把写了类型路径、不是已经复制到各节点、不是已经新鲜写成三个名字。把它们叫成一个「看见写了类型路径就已经是正常运转必须有 interchangeable / 就已经复制到各节点 interchangeable / 就已经新鲜 interchangeable」，会把 not already required、not already replicated、not already fresh 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看规范建议允许 /accounts / /votes 这类查询不是已经是正常运转必须有 not already required / not already replicated / not already fresh 正式三事（377 余量），先数清问的是写了类型路径 是不是 already required / 377 / querypath-sold-as-store，是不是建议允许 是不是 already replicated，还是能查账户 是不是 already fresh，再决定要不要同一次发布。377 querypath-vs-store bundled unbundling 在本页 item 3 完成。
