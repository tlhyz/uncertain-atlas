# 反模式：把 CheckTx Usage lane_id in ResponseInfo range not Info table selection / not in-table means prioritized / not CheckTx response field bundled 正式三事（482 余量） 说成已经 Info 表选型 / 已经填了就排了优先 / 已经回包栏交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[lane_id ≠ bundled（482）](../../tracks/implementation/worked-example-chktxlane-notrange-vs-bundled.md)。

## 卖法

把 CheckTx Usage lane_id 这句写成已经已经 Info 表选型 / 已经填了就排了优先 / 已经回包栏交差 interchangeable，或已经和 482 chktxlane-vs-default bundled / chktxlane-notrange-sold-as-bundled interchangeable。

## 为什么错

官方把 CheckTx Usage lane_id 三条核心句写成三件独立的实现事。把它们卖成已经 Info 表选型 / 已经填了就排了优先 / 已经回包栏交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage lane_id in range 正式三事（482 余量），必须分开 not Info table selection、not in-table means prioritized、not CheckTx response field bundled 三件事，不要和 482 / 367 / 381 / 704 / 705 糊成一句。

## 和相邻反模式

- [chktxlane-sold-as-nolane](chktxlane-sold-as-nolane.md) 是 CheckTx Usage lane_id bundled（482），不是本页 item 3 单句边界。
- [chktxlane-notassigned-sold-as-bundled](chktxlane-notassigned-sold-as-bundled.md) 是 assigned to default lane 单句边界（705 item 2），不是本页 in range 边界。
