# 模式：把 height / time / proposer_address 对上拟议头不是已经知道本头哈希 not already header-hash / not already execute / not already settled 正式三事（359 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**例**：[拟议头三列 not already header-hash ≠ bundled（359）](../../tracks/implementation/worked-example-prepfields-nothash-vs-bundled.md)。

## 三个名字

1. **对得上 不是 already header-hash：** 看见对得上 / `height` / `time` / `proposer_address` 对上拟议头 / 这三列对上，不是已经知道本头哈希 interchangeable / 已经 header-hash interchangeable / 已经有本头哈希交差 interchangeable，不是 359 preparefields bundled interchangeable / preparefields-sold-as-same interchangeable。

2. **头上有这些 不是 already execute：** 看见头上有这些 / 拟议头上有 height / time / proposer_address / 头上有这三列，不是已经是候选已经是 ExecuteTxState interchangeable / 已经 execute interchangeable / 已经是 ExecuteTxState 交差 interchangeable，不是 311 candidate interchangeable / 830 prepfields-notprocess interchangeable。

3. **拟议头 不是 already settled：** 看见拟议头 / 有拟议块头 / 这三列进了请求，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 831 prepfields-notthissigned interchangeable / 33 fourgates interchangeable。

官方把对得上、不是已经是 ExecuteTxState、不是已经交差写成三个名字。把它们叫成一个「看见对得上就已经知道本头哈希 interchangeable / 就已经是 ExecuteTxState interchangeable / 就已经交差 interchangeable」，会把 not already header-hash、not already execute、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 height / time / proposer_address 对上拟议头不是已经知道本头哈希 not already header-hash / not already execute / not already settled 正式三事（359 余量），先数清问的是对得上 是不是 already header-hash / 359 / preparefields-sold-as-same，是不是头上有这些 是不是 already execute，还是拟议头 是不是 already settled，再决定要不要同一次发布。359 prepare-fields vs same bundled unbundling 在本页 item 3 完成。
