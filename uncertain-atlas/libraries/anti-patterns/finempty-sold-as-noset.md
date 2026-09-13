# 反模式：把 FinalizeBlock 空更新保持当前值正式三事说成已经没有集合

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[validator_updates 空则保持当前集合 ≠ 已经没有集合](../../tracks/implementation/worked-example-finempty-vs-mustprovide.md)。

## 错在哪里

把 must provide app_hash / tx_results / validator_updates / consensus_param_updates 写成已经改了集合或已经交差；把 validator_updates may be empty … keep the current values 写成已经没有集合；把 consensus_param_updates may be empty … keep the current values 写成已经清掉参数或已经只改一项。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock 空更新保持当前值正式三事，必须分开必须回四列、validator_updates 空、consensus_param_updates 空三件事，不要和 363 / 318 / 319 / 382 糊成一句。
