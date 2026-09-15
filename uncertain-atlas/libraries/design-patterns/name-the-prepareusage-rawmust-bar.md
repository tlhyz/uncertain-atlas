# 模式：把 PrepareProposal Usage raw proposal / MUST remove 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**例**：[raw proposal / MUST remove ≠ bundled](../../tracks/implementation/worked-example-prepareusage-rawmust-vs-bundled.md)。

## 三个名字

1. **raw proposal / can modify this set 不是 Prepare 改列表 bundled：** 看见 Methods PrepareProposal Usage preliminary / raw proposal，不是 355 拿掉/加入/改追踪性 bundled interchangeable。
2. **MAY configure exceeding 不是 Req 2 bundled：** 看见 MAY include txs exceeding max_tx_bytes，不是 345 Req 2 bundled interchangeable。
3. **MUST remove if > max_tx_bytes 不是引擎会帮你裁：** 看见 MUST remove to respect limit in Response.txs，不是 345 引擎会帮你裁 interchangeable。

## 为什么要分开叫

官方把 raw proposal / MAY configure exceeding / MUST remove、Prepare 改列表 bundled（355）、Prepare 回包上限 Req 2 bundled（345）写成三个名字。把它们叫成一个「看见 Prepare 请求里带了 txs 就已经改列表 bundled interchangeable、已经能回超限、已经是引擎会帮你裁 interchangeable」，会把 raw proposal、MAY configure、MUST remove 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposal Usage raw proposal / MUST remove 正式三事，先数清问的是 raw proposal / can modify this set 是不是 Prepare 改列表 bundled interchangeable、MAY configure exceeding 是不是 Req 2 bundled interchangeable、MUST remove 是不是引擎会帮你裁 interchangeable，再决定要不要同一次发布。
