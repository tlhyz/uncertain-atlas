# 反模式：把 CheckTx 对照当前状态验 not already ExecuteTxState / not already processing block / not already settled 正式三事（391 余量） 说成已经按 ExecuteTxState 验过 / 已经参与处理块 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[CheckTx ≠ bundled（391）](../../tracks/implementation/worked-example-checktxtx-notexecstate-vs-bundled.md)。

## 卖法

把 CheckTx 请求余栏这句写成已经已经按 ExecuteTxState 验过 / 已经参与处理块 / 已经交差 interchangeable，或已经和 391 checktxtx-vs-recheck bundled / checktxtx-notexecstate-sold-as-bundled interchangeable。

## 为什么错

官方把 CheckTx 请求 tx / 对照当前状态验 / 回包 info 三条核心句写成三件独立的实现事。把它们卖成已经按 ExecuteTxState 验过 / 已经参与处理块 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx 对照当前状态验 正式三事（391 余量），必须分开 not already ExecuteTxState、not already processing block、not already settled 三件事，不要和 391 / 312 / 373 / 486 / 680 / 752 / 754 糊成一句。

## 和相邻反模式

- [checktxtx-sold-as-recheck](checktxtx-sold-as-recheck.md) 是 CheckTx 请求余栏 bundled（391），不是本页 item 2 单句边界。
- [chktxvalidate-sold-as-applied](chktxvalidate-sold-as-applied.md) 是 CheckTx Usage validate-no-apply（486），不是本页请求余栏 validate 边界。
