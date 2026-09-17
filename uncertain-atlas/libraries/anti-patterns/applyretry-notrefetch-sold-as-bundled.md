# 反模式：把 ApplySnapshotChunk Result RETRY not refetch regardless / not already complete / not applysnapusage refetch 正式三事（398 余量） 说成已经 refetch 不论 result / 已经齐 / 已经 Usage refetch 交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[RETRY ≠ bundled（398）](../../tracks/implementation/worked-example-applyretry-notrefetch-vs-bundled.md)。

## 卖法

把 ApplySnapshotChunk Result 这句写成已经已经 refetch 不论 result / 已经齐 / 已经 Usage refetch 交差 interchangeable，或已经和 398 applyretry-vs-refetch bundled / applyretry-notrefetch-sold-as-bundled interchangeable。

## 为什么错

官方把 ApplySnapshotChunk Result 三条核心句写成三件独立的实现事。把它们卖成已经 refetch 不论 result / 已经齐 / 已经 Usage refetch 交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ApplySnapshotChunk Result RETRY 正式三事（398 余量），必须分开 not refetch regardless、not already complete、not applysnapusage refetch 三件事，不要和 398 / 378 / 502 / 720 / 721 糊成一句。

## 和相邻反模式

- [applyretry 父页 bundled](../../tracks/implementation/worked-example-applyretry-vs-refetch.md) 是 ApplySnapshotChunk 结果枚举 bundled（398），不是本页 item 1 单句边界。
- [applyretry-notswitch-sold-as-bundled](applyretry-notswitch-sold-as-bundled.md) 是 RETRY_SNAPSHOT 单句边界（720 item 2），不是本页 RETRY 边界。
