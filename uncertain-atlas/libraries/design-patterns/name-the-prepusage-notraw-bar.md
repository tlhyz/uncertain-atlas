# 模式：点名 prepusage-notraw 杠

**层次**：实现 / PrepareUsage raw not already Prepare-改列表 / not already deleted-from-mempool / not already only-raw 正式三事（503 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**对应**：[`../tracks/implementation/worked-example-prepusage-notraw-vs-bundled.md`](../tracks/implementation/worked-example-prepusage-notraw-vs-bundled.md)。

- **初步交易列表叫 raw proposal 不是已经 Prepare 改列表 bundled：看见初步交易列表叫 raw proposal，不是已经 Prepare 改列表 bundled interchangeable / 1304 prepusage-notraw interchangeable。**
- **应用可以改这套 不是已经从内存池删掉：看见应用可以改这套，不是已经从内存池删掉 interchangeable / 1304 prepusage-notraw interchangeable。**
- **初步交易列表叫 raw proposal 不是已经只有 raw proposal：看见初步交易列表叫 raw proposal，不是已经只有 raw proposal interchangeable / 1304 prepusage-notraw interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposal Usage raw proposal / MUST remove 正式三事（503 余量），必须分开 not already Prepare-改列表、not already Req-2、not already engine-trims 三件事。
