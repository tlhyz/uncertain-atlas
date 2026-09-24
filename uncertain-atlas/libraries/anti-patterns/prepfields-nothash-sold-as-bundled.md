# 反模式：把 height / time / proposer_address 对上拟议头不是已经知道本头哈希 not already header-hash / not already execute / not already settled 正式三事（359 余量）说成已经知道本头哈希 / 已经是 ExecuteTxState / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[拟议头三列 not already header-hash ≠ bundled（359）](../../tracks/implementation/worked-example-prepfields-nothash-vs-bundled.md)。

## 卖法

把对得上 / `height` / `time` / `proposer_address` 对上拟议头 / 这三列对上 写成已经知道本头哈希 interchangeable / 已经 header-hash interchangeable / 已经有本头哈希交差 interchangeable / 359 preparefields bundled interchangeable / preparefields-sold-as-same interchangeable；把头上有这些 / 拟议头上有 height / time / proposer_address 写成已经是候选已经是 ExecuteTxState interchangeable / 已经 execute interchangeable / 已经是 ExecuteTxState 交差 interchangeable；把拟议头 / 有拟议块头 / 这三列进了请求 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，或已经和 359 preparefields bundled / preparefields-sold-as-same interchangeable / 832 prepfields-nothash interchangeable。

## 为什么错

官方把对得上、不是已经是 ExecuteTxState、不是已经交差写成三件独立的实现事。把它们卖成 already header-hash interchangeable / already execute interchangeable / already settled interchangeable，会把 not already header-hash、not already execute、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 height / time / proposer_address 对上拟议头不是已经知道本头哈希 not already header-hash / not already execute / not already settled 正式三事（359 余量），必须分开 not already header-hash、not already execute、not already settled 三件事，不要和 359 / 311 / 330 / 830 / 831 糊成一句。

## 和相邻反模式

- [preparefields-sold-as-same](preparefields-sold-as-same.md) 是 Prepare 请求字段 bundled 全段，不是本页对得上 item 3 单句边界。
- [candidate-sold-as-execute](candidate-sold-as-execute.md) 是候选已经是 ExecuteTxState（311），不是本页 not already header-hash 边界。
- [prepfields-notthissigned-sold-as-bundled](prepfields-notthissigned-sold-as-bundled.md) 是 local_last_commit 上一高 not already this-signed（359 item 2），不是本页 not already settled 边界。
