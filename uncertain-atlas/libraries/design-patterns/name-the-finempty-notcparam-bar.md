# 模式：把 FinalizeBlock empty consensus_param_updates keep current not H+1 effective 正式三事（458 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[empty consensus_param_updates keep current not H+1 effective ≠ bundled（458）](../../tracks/implementation/worked-example-finempty-notcparam-vs-bundled.md)。

## 三个名字

1. **empty consensus_param_updates keep current not clear params 不是 nil / 319：** 看见 may be empty 不是已经清掉参数 interchangeable，不是 319 partial update interchangeable / 432 回包末栏 interchangeable / 335 finpersist interchangeable。
2. **empty keep current not H+1 effective at H 不是 471 fincparam：** 看见 keep current values 不是已经在块 H 生效 interchangeable，不是 471 fincparam interchangeable / 333 effective delay interchangeable / 35 集合 vs 参数延迟 interchangeable。
3. **empty consensus_param_updates keep current not finempty bundled 不是 597 / 598 / 596：** 看见 consensus_param_updates 空着不是已经 finempty bundled interchangeable，不是 597 notmustprovide interchangeable / 598 notnoset interchangeable / 596 notempty interchangeable / 477 finasresult interchangeable。

## 为什么要分开叫

官方把 empty consensus_param_updates keep current、H→H+1 生效 和 finempty bundled 写成三个名字。把它们叫成一个「看见 consensus_param_updates 空着 就已经清掉参数 / 已经 keep current 就已经在 H+1 生效 interchangeable」，会把 not clear params、not H+1 effective already changed、not finempty bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock empty consensus_param_updates keep current not H+1 effective 正式三事（458 余量），先数清问的是 empty keep current 是不是 already clear params / 319 / 432、是不是 already H+1 effective at H / 471 / 333、还是 already finempty bundled / 597 / 598 / 596，再决定要不要同一次发布。
