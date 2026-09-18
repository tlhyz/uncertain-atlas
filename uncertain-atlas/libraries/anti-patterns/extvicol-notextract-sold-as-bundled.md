# 反模式：把 ExtendedVoteInfo.vote_extension not already extracted / not already packed / not already settled 正式三事（421 余量） 写成已经 已经从本进程抽出 / 已经会包进 CanonicalVoteExtension / 已经交差

**层次**：实现 / ExtendedVoteInfo.vote_extension not already extracted / not already packed / not already settled 正式三事（421 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ExtendedVoteInfo。  
**对应**：[`../tracks/implementation/worked-example-extvicol-notextract-vs-bundled.md`](../tracks/implementation/worked-example-extvicol-notextract-vs-bundled.md)。

把 ExtendedVoteInfo.vote_extension not already extracted / not already packed / not already settled 正式三事（421 余量） 写成已经 已经从本进程抽出 / 已经会包进 CanonicalVoteExtension / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 vote_extension 正式三事（421 余量），必须分开 not already extracted、not already packed、not already settled 三件事，不要和 421 / 369 / 418 / 1044 / 1045 糊成一句。

也不是：

- [finreqcol-notexec-sold-as-bundled](finreqcol-notexec-sold-as-bundled.md) 是 Finalize txs 仍未执行边界（422/1042），不是本页 vote_extension 仍未从本进程抽出边界。
- ExtendedVoteInfo 从本进程抽出就已经从块里抽出是不变量 369，不是本页是应用给的仍未包进 CanonicalVoteExtension 边界。
