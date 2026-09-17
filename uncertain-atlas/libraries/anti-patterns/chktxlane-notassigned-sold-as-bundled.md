# 反模式：把 CheckTx Usage assigned to default lane not default_lane identifier / not Priority consensus order / not Check passed is in proposal 正式三事（482 余量） 说成已经写了 default_lane 标识 / 已经排了优先 / 已经进了块

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[assigned ≠ bundled（482）](../../tracks/implementation/worked-example-chktxlane-notassigned-vs-bundled.md)。

## 卖法

把 CheckTx Usage lane_id 这句写成已经已经写了 default_lane 标识 / 已经排了优先 / 已经进了块 interchangeable，或已经和 482 chktxlane-vs-default bundled / chktxlane-notassigned-sold-as-bundled interchangeable。

## 为什么错

官方把 CheckTx Usage lane_id 三条核心句写成三件独立的实现事。把它们卖成已经写了 default_lane 标识 / 已经排了优先 / 已经进了块，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage assigned to default lane 正式三事（482 余量），必须分开 not default_lane identifier、not Priority consensus order、not Check passed is in proposal 三件事，不要和 482 / 317 / 33 / 704 / 706 糊成一句。

## 和相邻反模式

- [chktxlane-sold-as-nolane](chktxlane-sold-as-nolane.md) 是 CheckTx Usage lane_id bundled（482），不是本页 item 2 单句边界。
- [chktxlane-notreserved-sold-as-bundled](chktxlane-notreserved-sold-as-bundled.md) 是 empty lane_id 单句边界（704 item 1），不是本页 assigned 边界。
