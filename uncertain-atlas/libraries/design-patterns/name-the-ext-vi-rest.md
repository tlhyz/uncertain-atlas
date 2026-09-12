# 模式：把 ExtendedVoteInfo 表余栏三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ExtendedVoteInfo。  
**例**：[ExtendedVoteInfo.validator 是发了这张票的验证者 ≠ 已经带了公钥](../../tracks/implementation/worked-example-extvirest-vs-voteinfo.md)。

## 三个名字

1. **ExtendedVoteInfo.validator 是发了这张票的验证者不是已经带了公钥：** 看见填了 validator 不是已经从本进程抽出。
2. **ExtendedVoteInfo.block_id_flag 标明投了上一块、nil、还是没收到票不是已经罚没：** 看见填了 block_id_flag 不是已经是 VoteInfo 的 block_id_flag。
3. **ExtendedVoteInfo.non_rp_extension_signature 是发送验证者造、CometBFT 验过的非重放保护扩展签不是已经把验过的签交给应用：** 看见填了 non_rp_extension_signature 不是已经是 extension_signature。

## 为什么要分开叫

官方把 ExtendedVoteInfo 表上 `validator` 是发了这张票的验证者、`block_id_flag` 标明投了上一块、nil、还是没收到票、`non_rp_extension_signature` 是发送验证者造、CometBFT 验过的非重放保护扩展签写成三件事。把它们叫成一个「看见填了 ExtendedVoteInfo 表余栏就已经带了公钥」，会把已经带了公钥、已经罚没和已经把验过的签交给应用一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 ExtendedVoteInfo 表余栏就已经带了公钥」，先数清问的是 ExtendedVoteInfo.validator 是发了这张票的验证者不是已经带了公钥、ExtendedVoteInfo.block_id_flag 标明投了上一块、nil、还是没收到票不是已经罚没，还是 ExtendedVoteInfo.non_rp_extension_signature 是发送验证者造、CometBFT 验过的非重放保护扩展签不是已经把验过的签交给应用，再决定要不要同一次发布。
