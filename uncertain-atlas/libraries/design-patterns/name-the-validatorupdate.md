# 模式：把 ValidatorUpdate 三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Updating the Validator Set。  
**例**：[InitChain 空名单 ≠ 已经没有集合](../../tracks/implementation/worked-example-validatorupdate-vs-set.md)。

## 三个名字

1. **InitChain 空名单不是已经没有集合：** 看见回空不是已经删掉创世名单。
2. **同一批重复公钥不是已经能恢复：** 看见两行不是已经按后一条改权。
3. **power 0 不是已经删掉不在集合里的人：** 看见写成 0 不是已经能对不在名单里的人生效。

## 为什么要分开叫

官方把回空改用创世、同一批不得重复、必须已在集合里才删写成三件事。把它们叫成一个「看见回了名单就已经换人」，会把生效高度、创世空名单和换轮一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「InitChain 已经回了名单」，先数清问的是回空不是已经没有集合、重复不是已经能恢复，还是 power 0 不是已经删掉不在集合里的人，再决定要不要同一次发布。
