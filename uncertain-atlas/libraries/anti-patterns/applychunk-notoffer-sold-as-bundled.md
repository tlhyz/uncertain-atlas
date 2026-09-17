# 反模式：把 ApplySnapshotChunk 回包 result not Offer result / not already restored / not Apply Result enum 正式三事（397 余量） 说成已经是 Offer 的结果 / 已经装完 / 已经 Apply Result 枚举

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[ApplySnapshotChunk ≠ bundled（397）](../../tracks/implementation/worked-example-applychunk-notoffer-vs-bundled.md)。

## 卖法

把 ApplySnapshotChunk 请求这句写成已经已经是 Offer 的结果 / 已经装完 / 已经 Apply Result 枚举 interchangeable，或已经和 397 applychunk-vs-loadchunk bundled / applychunk-notoffer-sold-as-bundled interchangeable。

## 为什么错

官方把 ApplySnapshotChunk 请求 chunk / sender / 回包 result 三条核心句写成三件独立的实现事。把它们卖成已经是 Offer 的结果 / 已经装完 / 已经 Apply Result 枚举，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ApplySnapshotChunk 回包 result 正式三事（397 余量），必须分开 not Offer result、not already restored、not Apply Result enum 三件事，不要和 397 / 396 / 738 / 321 / 398 / 740 / 741 糊成一句。

## 和相邻反模式

- [applychunk-sold-as-loadchunk](applychunk-sold-as-loadchunk.md) 是 ApplySnapshotChunk 请求 bundled（397），不是本页 item 3 单句边界。
- [applychunk-notsenders-sold-as-bundled](applychunk-notsenders-sold-as-bundled.md) 是 sender 单句边界（741 item 2），不是本页 result 边界。
