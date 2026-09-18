# 反模式：把 PrepareUsage raw not already Prepare-改列表 / not already deleted-from-mempool / not already only-raw 正式三事（503 余量） 写成已经 已经 Prepare 改列表 bundled / 已经从内存池删掉 / 已经只有 raw proposal

**层次**：实现 / PrepareUsage raw not already Prepare-改列表 / not already deleted-from-mempool / not already only-raw 正式三事（503 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**对应**：[`../tracks/implementation/worked-example-prepusage-notraw-vs-bundled.md`](../tracks/implementation/worked-example-prepusage-notraw-vs-bundled.md)。

把 PrepareUsage raw not already Prepare-改列表 / not already deleted-from-mempool / not already only-raw 正式三事（503 余量） 写成已经 已经 Prepare 改列表 bundled / 已经从内存池删掉 / 已经只有 raw proposal，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposal Usage raw proposal / MUST remove 正式三事（503 余量），必须分开 not already Prepare-改列表、not already Req-2、not already engine-trims 三件事，不要和 503 / 355 / 423 / 1305 / 1306 糊成一句。

也不是：

- [prepusage-notexceed-sold-as-bundled](prepusage-notexceed-sold-as-bundled.md) 是 notexceed 单句边界（1305），不是本页边界。
- [prepusage-notmust-sold-as-bundled](prepusage-notmust-sold-as-bundled.md) 是 notmust 单句边界（1306），不是本页边界。
- [rcpt-notrpc-sold-as-bundled](rcpt-notrpc-sold-as-bundled.md) 是 EIP-658 RPC 能告诉你成没成仍未是收据里已经有状态码边界（236/1303），不是本页 PrepareUsage 边界。
