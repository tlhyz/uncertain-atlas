# 反模式：看见 ExtendedVoteInfo.validator 是发了这张票的验证者就当成已经带了公钥 / 看见 ExtendedVoteInfo.block_id_flag 标明投了上一块、nil、还是没收到票就当成已经罚没 / 看见 ExtendedVoteInfo.non_rp_extension_signature 是发送验证者造、CometBFT 验过的非重放保护扩展签就当成已经把验过的签交给应用

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ExtendedVoteInfo。  
**例**：[ExtendedVoteInfo.validator 是发了这张票的验证者 ≠ 已经带了公钥](../../tracks/implementation/worked-example-extvirest-vs-voteinfo.md)。

## 塌法

1. 看见 `ExtendedVoteInfo.validator` 是发了这张票的验证者 / 看见填了 validator，就当成已经带了公钥，或当成已经从本进程抽出。
2. 看见 `ExtendedVoteInfo.block_id_flag` 标明投了上一块、nil、还是没收到票 / 看见填了 block_id_flag，就当成已经罚没，或当成已经是 VoteInfo 的 block_id_flag。
3. 看见 `ExtendedVoteInfo.non_rp_extension_signature` 是发送验证者造、CometBFT 验过的非重放保护扩展签 / 看见填了 non_rp_extension_signature，就当成已经把验过的签交给应用，或当成已经是 extension_signature。

## 为什么会出事

官方写：`validator` 是发了这张票的验证者。`block_id_flag` 标明这个验证者投了上一块、投了 nil、还是票没收到。`non_rp_extension_signature` 是发送验证者造、CometBFT 验过的非重放保护扩展签。看见填了栏，不是已经带了公钥，也不是已经罚没，也不是已经把验过的签交给应用。

## 和相邻反模式

- [extvoteinfo-sold-as-local](extvoteinfo-sold-as-local.md) 是 ExtendedVoteInfo 从本进程抽出就已经从块里抽出，不是本页这种 ExtendedVoteInfo.validator 是发了这张票的验证者不是已经带了公钥。
- [voteinfo-sold-as-rewarded](voteinfo-sold-as-rewarded.md) 是 VoteInfo 能按到场定奖惩就已经罚没，不是本页这种 ExtendedVoteInfo.block_id_flag 标明投了上一块、nil、还是没收到票不是已经罚没。
- [extvitable-sold-as-usage](extvitable-sold-as-usage.md) 是 ExtendedVoteInfo.extension_signature 是发送验证者造、CometBFT 验过的扩展签就已经把验过的签交给应用，不是本页这种 ExtendedVoteInfo.non_rp_extension_signature 是发送验证者造、CometBFT 验过的非重放保护扩展签不是已经把验过的签交给应用。
