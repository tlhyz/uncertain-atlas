# 反模式：把 PrepareProposal Usage raw proposal / MUST remove 正式三事卖成 Prepare 改列表 bundled / Req 2 bundled / 引擎会帮你裁

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[raw proposal / MUST remove ≠ bundled](../../tracks/implementation/worked-example-prepareusage-rawmust-vs-bundled.md)。

## 卖法

- 「看见 preliminary txs called raw proposal / can modify this set / 看见 Prepare 请求里带了 txs 就已经 Prepare 改列表 bundled interchangeable / 已经从内存池删掉 / 已经只有 raw proposal interchangeable。」
- 「看见 MAY configure txs exceeding max_tx_bytes / MaxBytes=-1 include all mempool 就已经 Req 2 bundled interchangeable / 已经能回超限列表 interchangeable。」
- 「看见 MUST remove if size > max_tx_bytes 就已经引擎会帮你裁 interchangeable / 已经从内存池删掉 interchangeable。」

## 为什么错

官方把 raw proposal / MAY configure exceeding / MUST remove 写成三件独立的实现事。把它们卖成 Prepare 改列表 bundled、Req 2 bundled、引擎会帮你裁，会把 raw proposal、MAY configure、MUST remove 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposal Usage raw proposal / MUST remove 正式三事，必须分开 raw proposal / can modify this set、MAY configure exceeding、MUST remove 三个名字，不要把它们卖成 Prepare 改列表 bundled / Req 2 bundled / 引擎会帮你裁。

## 和相邻反模式

- [prepare-drop-sold-as-mempool](prepare-drop-sold-as-mempool.md) 是 Prepare 改列表 consequences 三事，不是本页 raw proposal 单句专用边界。
- [prepare-return-sold-as-pool](prepare-return-sold-as-pool.md) 是 Prepare 回包上限 Req 2 bundled 三事，不是本页 MUST remove Methods Usage 单句专用边界。
