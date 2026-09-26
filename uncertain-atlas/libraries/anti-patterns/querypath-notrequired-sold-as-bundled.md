# 反模式：把规范建议允许 /accounts / /votes 这类查询不是已经是正常运转必须有 not already required / not already replicated / not already fresh 正式三事（377 余量）说成已经是正常运转必须有 / 已经复制到各节点 / 已经新鲜

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[写了类型路径 not already required ≠ bundled（377）](../../tracks/implementation/worked-example-querypath-notrequired-vs-bundled.md)。

## 卖法

把写了类型路径 / 规范建议允许 /accounts / /votes 这类查询 / 写了 /accounts 或 /votes 写成已经是正常运转必须有 interchangeable / 已经 required interchangeable / 已经是正常运转必须有交差 interchangeable / 377 querypath bundled interchangeable / querypath-sold-as-store interchangeable；把建议允许 / 规范建议允许 / 应当允许 写成已经复制到各节点 interchangeable / 已经 replicated interchangeable / 已经复制到各节点交差 interchangeable；把能查账户 / 能查 /accounts / 能查类型 写成已经新鲜 interchangeable / 已经 fresh interchangeable / 已经新鲜交差 interchangeable，或已经和 377 querypath bundled / querypath-sold-as-store interchangeable / 880 querypath-notrequired interchangeable。

## 为什么错

官方把写了类型路径、不是已经复制到各节点、不是已经新鲜写成三件独立的实现事。把它们卖成 already required interchangeable / already replicated interchangeable / already fresh interchangeable，会把 not already required、not already replicated、not already fresh 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看规范建议允许 /accounts / /votes 这类查询不是已经是正常运转必须有 not already required / not already replicated / not already fresh 正式三事（377 余量），必须分开 not already required、not already replicated、not already fresh 三件事，不要和 377 / 329 / 879 / 878 糊成一句。

## 和相邻反模式

- [querypath-sold-as-store](querypath-sold-as-store.md) 是 querypath bundled 全段，不是本页写了类型路径 item 3 单句边界。
- [querypath-notheight-sold-as-bundled](querypath-notheight-sold-as-bundled.md) 是填了 data not already height（377 item 1），不是本页 not already required 边界。
- [querypath-notengine-sold-as-bundled](querypath-notengine-sold-as-bundled.md) 是写了 /store not already engine（377 item 2），不是本页 not already replicated 边界。
- [query-sold-as-replicated](query-sold-as-replicated.md) 是实现了 Query 就已经是正常运转必须有（329），不是本页 not already required 单句。
