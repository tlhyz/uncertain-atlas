# 反模式：把 OfferSnapshot Usage trust 正式三事卖成 Snapshot 字段都可信 / hash 比对就够 / 装块时就 Info 对了

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Only AppHash can be trusted ≠ Snapshot 字段都可信](../../tracks/implementation/worked-example-offersnaptrust-vs-metadata.md)。

## 卖法

- 「看见 Only AppHash can be trusted / 看见 Offer 了 AppHash 就已经 Snapshot.hash / metadata / 五个字段都可信。」
- 「看见 Any other data can be spoofed / employ additional verification / 看见 hash 比对 / metadata 对齐就已经防 DoS / 已经交差。」
- 「看见 verified AppHash automatically checked at end / 看见装 chunk 时 Info 对了 / 已经切进共识 / 已经装完。」

## 为什么错

官方把 Only AppHash can be trusted、Any other data can be spoofed / employ additional verification、verified AppHash automatically checked at the end 写成三件独立的实现事。把它们卖成 Snapshot 字段都可信、hash 比对就够、装块时就 Info 对了，会把轻验锚、另做验真、装回结束核对 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 OfferSnapshot Usage trust，必须分开 Only AppHash can be trusted、Any other data can be spoofed / employ additional verification、verified AppHash automatically checked at end 三个名字，不要把它们卖成 Snapshot 字段都可信 / hash 比对就够 / 装块时就 Info 对了。

## 和相邻反模式

- [snapshot-sold-as-identical](../../libraries/anti-patterns/snapshot-sold-as-identical.md) 是快照全字段对上就已经装完，不是本页 Only AppHash can be trusted。
- [snapshotverify-sold-as-early](../../libraries/anti-patterns/snapshotverify-sold-as-early.md) 是装完 Info 对了就已经在装过程中验过，不是本页 automatically checked at end。
- [offersnapusage-bootstrap-sold-as-bundled](offersnapusage-bootstrap-sold-as-bundled.md) 是 OfferSnapshot Usage bootstrap accept/reject 正式三事，不是本页 Only AppHash can be trusted。
