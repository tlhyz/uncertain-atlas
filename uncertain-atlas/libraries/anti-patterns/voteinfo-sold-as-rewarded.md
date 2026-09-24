# 反模式：看见 VoteInfo 能按到场定奖惩就当成已经罚没 / 看见从拟议块或已决块抽出就当成已经带了公钥 / 看见按投票权降序排就当成已经进了块

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types VoteInfo / CommitInfo。  
**例**：[VoteInfo 能按到场定奖惩 ≠ 已经罚没](../../tracks/implementation/worked-example-voteinfo-vs-reward.md)。

## 塌法

1. 看见 VoteInfo 标明上一块有没有签、能按到场定奖惩 / 看见有 `block_id_flag`，就当成已经罚没，或当成已经交差。
2. 看见这份信息通常从拟议块或已决块抽出 / 看见块里有票，就当成已经带了公钥，或当成已经是 ValidatorUpdate。
3. 看见 `votes` 按投票权降序排、落盘后再从 store 装回 / 看见顺序在，就当成已经进了块，或当成已经交差。

## 为什么会出事

官方写：`VoteInfo` 标明验证者有没有签上一块，好按到场定奖惩。这份信息通常从拟议块或已决块抽出。`CommitInfo.votes` 按投票权从高到低排；集合写入 store 时顺序也落盘；造 `CommitInfo` 时从 store 再装集合。

## 和相邻反模式

- [voteinfo-notslashed-sold-as-bundled](voteinfo-notslashed-sold-as-bundled.md) 是 VoteInfo 能按到场定奖惩 not already slashed / not already decided-commit / not already settled 正式三事（365 item 1），不是本页 bundled 全段 alone。
- [voteinfo-notpubkey-sold-as-bundled](voteinfo-notpubkey-sold-as-bundled.md) 是从拟议块或已决块抽出 not already pubkey / not already update / not already changed-set 正式三事（365 item 2），不是本页 bundled 全段 alone。
- [voteinfo-notinblock-sold-as-bundled](voteinfo-notinblock-sold-as-bundled.md) 是按投票权降序排 not already in-block / not already settled / not already slashed 正式三事（365 item 3），不是本页 bundled 全段 alone。
- [finalizeequiv-sold-as-gates](finalizeequiv-sold-as-gates.md) 是必须回四列就已经改了集合，不是本页这种 VoteInfo 能按到场定奖惩不是已经罚没。
- [validator-sold-as-update](validator-sold-as-update.md) 是 Validator 用 address 认人就已经带了公钥，不是本页这种从拟议块或已决块抽出不是已经带了公钥。
- [state-sold-as-block](state-sold-as-block.md) 是本地 State 就已经进了块，不是本页这种按投票权降序排不是已经进了块。
