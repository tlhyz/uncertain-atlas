# 反模式：把 FinalizeBlock empty consensus_param_updates keep current not H+1 effective 正式三事（458 余量）说成已经清掉参数 / 已经在 H+1 生效

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[empty consensus_param_updates keep current not H+1 effective ≠ bundled（458）](../../tracks/implementation/worked-example-finempty-notcparam-vs-bundled.md)。

## 错在哪里

把 consensus_param_updates may be empty … CometBFT will keep the current values 写成已经清掉参数 interchangeable，或已经 InitChain 空参数 interchangeable；把 empty keep current 写成已经在块 H 生效 / 已经改了 gas / size interchangeable，或已经和 471 fincparam / 333 effective delay / 432 回包末栏 interchangeable；把 empty keep current 写成已经是 FinalizeBlock 空更新 keep current bundled（458） interchangeable，或已经 finempty bundled interchangeable，或已经和 597 notmustprovide / 598 notnoset / 596 notempty / 477 finasresult interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock empty consensus_param_updates keep current not H+1 effective 正式三事（458 余量），必须分开 empty keep current not clear params、not H+1 effective already changed、not finempty bundled 三件事，不要和 458 / 597 / 598 / 471 / 319 / 333 糊成一句。

## 和相邻反模式

- [finempty-notmustprovide-sold-as-bundled](finempty-notmustprovide-sold-as-bundled.md) 是 597（458 item 1 余量）专用，不是本页 consensus_param_updates 单句边界。
- [finempty-sold-as-noset](finempty-sold-as-noset.md) 是 598（458 item 2 余量）专用，不是本页 empty consensus_param_updates 单句边界。
- [fincparam-sold-as-heffective](fincparam-sold-as-heffective.md) 是 471 consensus_param_updates H→H+1 专用，不是本页 empty keep current 单句边界。
