# 反模式：把 CheckTx Usage empty lane_id not priority 0 reserved / not deleted from pool / not no-lane means rejected 正式三事（482 余量） 说成已经 priority 0 不设道 / 已经从池里删掉 / 已经可选拒

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[empty ≠ bundled（482）](../../tracks/implementation/worked-example-chktxlane-notreserved-vs-bundled.md)。

## 卖法

把 CheckTx Usage lane_id 这句写成已经已经 priority 0 不设道 / 已经从池里删掉 / 已经可选拒 interchangeable，或已经和 482 chktxlane-vs-default bundled / chktxlane-notreserved-sold-as-bundled interchangeable。

## 为什么错

官方把 CheckTx Usage lane_id 三条核心句写成三件独立的实现事。把它们卖成已经 priority 0 不设道 / 已经从池里删掉 / 已经可选拒，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage empty lane_id 正式三事（482 余量），必须分开 not priority 0 reserved、not deleted from pool、not no-lane means rejected 三件事，不要和 482 / 367 / 373 / 705 / 706 糊成一句。

## 和相邻反模式

- [chktxlane-sold-as-nolane](chktxlane-sold-as-nolane.md) 是 CheckTx Usage lane_id bundled（482），不是本页 item 1 单句边界。
- [chktxlane-notassigned-sold-as-bundled](chktxlane-notassigned-sold-as-bundled.md) 是 assigned to default lane 单句边界（705 item 2），不是本页 empty 边界。
