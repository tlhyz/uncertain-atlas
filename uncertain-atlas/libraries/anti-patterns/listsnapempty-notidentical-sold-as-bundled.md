# 反模式：把 ListSnapshots 本地清单 not already identical / not already restored / not already settled 正式三事（395 余量） 说成已经是同一份 / 已经装完 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[ListSnapshots ≠ bundled（395）](../../tracks/implementation/worked-example-listsnapempty-notidentical-vs-bundled.md)。

## 卖法

把 ListSnapshots 空请求这句写成已经已经是同一份 / 已经装完 / 已经交差 interchangeable，或已经和 395 listsnapempty-vs-discovery bundled / listsnapempty-notidentical-sold-as-bundled interchangeable。

## 为什么错

官方把 ListSnapshots 空请求要清单 / 本地清单 / 用来发现三条核心句写成三件独立的实现事。把它们卖成已经是同一份 / 已经装完 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ListSnapshots 本地清单 正式三事（395 余量），必须分开 not already identical、not already restored、not already settled 三件事，不要和 395 / 368 / 321 / 396 / 734 / 736 糊成一句。

## 和相邻反模式

- [listsnapempty-sold-as-discovery](listsnapempty-sold-as-discovery.md) 是 ListSnapshots 空请求 bundled（395），不是本页 item 2 单句边界。
- [listsnapempty-notcomplete-sold-as-bundled](listsnapempty-notcomplete-sold-as-bundled.md) 是空请求单句边界（734 item 1），不是本页本地清单边界。
