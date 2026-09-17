# 反模式：把 ListSnapshots 空请求 not already complete / not already asked neighbors / not Usage discover 正式三事（395 余量） 说成已经齐 / 已经问了邻居 / 已经 Usage discover

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[ListSnapshots ≠ bundled（395）](../../tracks/implementation/worked-example-listsnapempty-notcomplete-vs-bundled.md)。

## 卖法

把 ListSnapshots 空请求这句写成已经已经齐 / 已经问了邻居 / 已经 Usage discover interchangeable，或已经和 395 listsnapempty-vs-discovery bundled / listsnapempty-notcomplete-sold-as-bundled interchangeable。

## 为什么错

官方把 ListSnapshots 空请求要清单 / 本地清单 / 用来发现三条核心句写成三件独立的实现事。把它们卖成已经齐 / 已经问了邻居 / 已经 Usage discover，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ListSnapshots 空请求 正式三事（395 余量），必须分开 not already complete、not already asked neighbors、not Usage discover 三件事，不要和 395 / 322 / 500 / 661 / 735 / 736 糊成一句。

## 和相邻反模式

- [listsnapempty-sold-as-discovery](listsnapempty-sold-as-discovery.md) 是 ListSnapshots 空请求 bundled（395），不是本页 item 1 单句边界。
- [listsnapempty-notidentical-sold-as-bundled](listsnapempty-notidentical-sold-as-bundled.md) 是本地清单单句边界（735 item 2），不是本页空请求边界。
