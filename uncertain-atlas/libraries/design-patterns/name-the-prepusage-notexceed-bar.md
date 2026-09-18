# 模式：点名 prepusage-notexceed 杠

**层次**：实现 / PrepareUsage exceed not already Req-2 / not already can-return-oversize / not already no-cap 正式三事（503 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**对应**：[`../tracks/implementation/worked-example-prepusage-notexceed-vs-bundled.md`](../tracks/implementation/worked-example-prepusage-notexceed-vs-bundled.md)。

- **MAY 让请求超上限 不是已经 Req 2 bundled：看见MAY 让请求超上限，不是已经 Req 2 bundled interchangeable / 1305 prepusage-notexceed interchangeable。**
- **MaxBytes=-1 会交来整池 不是已经能回超限列表：看见MaxBytes=-1 会交来整池，不是已经能回超限列表 interchangeable / 1305 prepusage-notexceed interchangeable。**
- **MAY 让请求超上限 不是已经整池都给 Prepare 就没有上限：看见MAY 让请求超上限，不是已经整池都给 Prepare 就没有上限 interchangeable / 1305 prepusage-notexceed interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposal Usage raw proposal / MUST remove 正式三事（503 余量），必须分开 not already Prepare-改列表、not already Req-2、not already engine-trims 三件事。
