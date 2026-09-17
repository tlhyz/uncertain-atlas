# 反模式：把 ApplySnapshotChunk 请求 sender not reject_senders / not already banned / not REJECT_SENDER 正式三事（397 余量） 说成已经拒了人 / 已经封了 / 已经 REJECT_SENDER

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[ApplySnapshotChunk ≠ bundled（397）](../../tracks/implementation/worked-example-applychunk-notsenders-vs-bundled.md)。

## 卖法

把 ApplySnapshotChunk 请求这句写成已经已经拒了人 / 已经封了 / 已经 REJECT_SENDER interchangeable，或已经和 397 applychunk-vs-loadchunk bundled / applychunk-notsenders-sold-as-bundled interchangeable。

## 为什么错

官方把 ApplySnapshotChunk 请求 chunk / sender / 回包 result 三条核心句写成三件独立的实现事。把它们卖成已经拒了人 / 已经封了 / 已经 REJECT_SENDER，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ApplySnapshotChunk 请求 sender 正式三事（397 余量），必须分开 not reject_senders、not already banned、not REJECT_SENDER 三件事，不要和 397 / 378 / 400 / 723 / 740 / 742 糊成一句。

## 和相邻反模式

- [applychunk-sold-as-loadchunk](applychunk-sold-as-loadchunk.md) 是 ApplySnapshotChunk 请求 bundled（397），不是本页 item 2 单句边界。
- [applychunk-notload-sold-as-bundled](applychunk-notload-sold-as-bundled.md) 是 chunk 单句边界（740 item 1），不是本页 sender 边界。
