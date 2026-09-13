# 模式：把 FinalizeBlock 空更新保持当前值正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[必须回四列 ≠ 已经改了集合](../../tracks/implementation/worked-example-finempty-vs-mustprovide.md)。

## 三个名字

1. **必须回四列不是已经改了集合：** 看见 must provide app_hash / tx_results / validator_updates / consensus_param_updates 不是已经交差。
2. **validator_updates 空则保持当前集合不是已经没有集合：** 看见 may be empty … keep the current values 不是已经 InitChain 空名单。
3. **consensus_param_updates 空则保持当前参数不是已经清掉参数：** 看见空 consensus_param_updates 不是已经 Finalize 没回就清掉 / 只改一项。

## 为什么要分开叫

官方把 FinalizeBlock 空更新保持当前值写成三个名字。把它们叫成一个「看见回了空更新就已经没有集合」，会把 must provide、keep current validator set 和 keep current params 一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见回了空更新就已经没有集合」，先数清问的是必须回四列是不是已经改了集合、validator_updates 空是不是已经没有集合，还是 consensus_param_updates 空是不是已经清掉参数，再决定要不要同一次发布。
