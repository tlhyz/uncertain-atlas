# 模式：点名 whenret-notlist 杠

**层次**：实现 / PrepareWhenRet return-list not already raw-proposal / not already manipulate / not already Response-txs 正式三事（506 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When steps 4–5。  
**对应**：[`../tracks/implementation/worked-example-whenret-notlist-vs-bundled.md`](../tracks/implementation/worked-example-whenret-notlist-vs-bundled.md)。

- **把交易列表放进回包参数 不是已经 preliminary raw proposal bundled：看见把交易列表放进回包参数，不是已经 preliminary raw proposal bundled interchangeable / 1313 whenret-notlist interchangeable。**
- **改没改都算 不是已经 can manipulate transactions bundled：看见改没改都算，不是已经 can manipulate transactions bundled interchangeable / 1313 whenret-notlist interchangeable。**
- **把交易列表放进回包参数 不是已经 PrepareProposalResponse.txs 是可能改过的列表：看见把交易列表放进回包参数，不是已经 PrepareProposalResponse.txs 是可能改过的列表 interchangeable / 1313 whenret-notlist interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposal When return / use-as-proposal 正式三事（506 余量），必须分开 not already raw-proposal、not already Process-follows-Prepare、not already validValue-skip 三件事。
