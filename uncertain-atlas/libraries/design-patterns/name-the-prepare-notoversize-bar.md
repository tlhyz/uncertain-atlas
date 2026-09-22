# 模式：把聚合体积可以超过 max_tx_bytes 不是已经能回超限列表 not already can-return-oversize / not already request-trimmed / not already settled 正式三事（345 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 2 [`PrepareProposal`, tx-size]。  
**例**：[聚合体积可以超过 max_tx_bytes not already can-return-oversize ≠ bundled（345）](../../tracks/implementation/worked-example-prepare-notoversize-vs-bundled.md)。

## 三个名字

1. **聚合体积可以超过 max_tx_bytes 不是 already can-return-oversize：** 看见聚合体积可以超过 `PrepareProposalRequest.max_tx_bytes` / 池子加起来比这次上限大 / 所有交易加起来可以超，不是已经能回超限列表 interchangeable / 已经 can-return-oversize interchangeable / 已经回超限交差 interchangeable，不是 345 preparereturn bundled interchangeable / preparereturn-sold-as-trimmed interchangeable。

2. **请求里带了上限 不是 already request-trimmed：** 看见请求里带了上限 / `max_tx_bytes` 在请求里 / 这次上限写在请求上，不是已经按这个上限裁过 interchangeable / 已经 request-trimmed interchangeable / 已经裁过交差 interchangeable，不是 337 maxbytescap interchangeable / 299 evidence-tx interchangeable。

3. **能看见超限的池 不是 already settled：** 看见能看见超限的池 / 池子比上限大还交来 / 超限池仍可见，不是已经交差 interchangeable / 已经 settled interchangeable / 已经回包交差 interchangeable，不是 788 prepare-notblocksubset interchangeable / 790 prepare-notenginecut interchangeable。

官方把池子可以超这次上限、请求里写了上限不是已经裁过、能看见超限的池不是已经交差写成三个名字。把它们叫成一个「看见聚合体积可以超过 max_tx_bytes 就已经能回超限列表 interchangeable / 就已经按请求裁过 interchangeable / 就已经交差 interchangeable」，会把 not already can-return-oversize、not already request-trimmed、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看聚合体积可以超过 max_tx_bytes 不是已经能回超限列表 not already can-return-oversize / not already request-trimmed / not already settled 正式三事（345 余量），先数清问的是聚合体积可以超过 max_tx_bytes 是不是 already can-return-oversize / 345 / preparereturn-sold-as-trimmed，是不是请求里带了上限 是不是 already request-trimmed，还是能看见超限的池 是不是 already settled，再决定要不要同一次发布。345 preparereturn vs pool bundled unbundling 在本页 item 2 续。
