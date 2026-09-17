# 反模式：把 ApplySnapshotChunk 请求 chunk not already loading / not already complete / not Usage retrieve 正式三事（397 余量） 说成已经在拉块 / 已经齐 / 已经 Usage retrieve

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[ApplySnapshotChunk ≠ bundled（397）](../../tracks/implementation/worked-example-applychunk-notload-vs-bundled.md)。

## 卖法

把 ApplySnapshotChunk 请求这句写成已经已经在拉块 / 已经齐 / 已经 Usage retrieve interchangeable，或已经和 397 applychunk-vs-loadchunk bundled / applychunk-notload-sold-as-bundled interchangeable。

## 为什么错

官方把 ApplySnapshotChunk 请求 chunk / sender / 回包 result 三条核心句写成三件独立的实现事。把它们卖成已经在拉块 / 已经齐 / 已经 Usage retrieve，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ApplySnapshotChunk 请求 chunk 正式三事（397 余量），必须分开 not already loading、not already complete、not Usage retrieve 三件事，不要和 397 / 375 / 501 / 660 / 741 / 742 糊成一句。

## 和相邻反模式

- [applychunk-sold-as-loadchunk](applychunk-sold-as-loadchunk.md) 是 ApplySnapshotChunk 请求 bundled（397），不是本页 item 1 单句边界。
- [applychunk-notsenders-sold-as-bundled](applychunk-notsenders-sold-as-bundled.md) 是 sender 单句边界（741 item 2），不是本页 chunk 边界。
