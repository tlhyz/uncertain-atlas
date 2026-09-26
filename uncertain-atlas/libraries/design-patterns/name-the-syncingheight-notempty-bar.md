# 模式：把 validator_updates 空则引擎保持当前集合不是已经没有集合 not already empty / not already changed / not already genesis 正式三事（382 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock。  
**例**：[空着 not already empty ≠ bundled（382）](../../tracks/implementation/worked-example-syncingheight-notempty-vs-bundled.md)。

## 三个名字

1. **空着 不是 already empty：** 看见空着 / validator_updates 空则引擎保持当前集合 / validator_updates 或 consensus_param_updates 可以空，不是已经没有集合 interchangeable / 已经 empty interchangeable / 已经没有集合交差 interchangeable，不是 382 syncingheight bundled interchangeable / syncingheight-sold-as-history interchangeable。

2. **没回人 不是 already changed：** 看见没回人 / 没回 validator_updates / 保持当前值，不是已经改了集合 interchangeable / 已经 changed interchangeable / 已经改了集合交差 interchangeable，不是 318 validatorupdate interchangeable / 893 syncingheight-nothistory interchangeable。

3. **能空 不是 already genesis：** 看见能空 / Finalize 回包可以空着更新 / 空着不是 InitChain 那种空名单，不是已经是 InitChain 空名单 interchangeable / 已经 genesis interchangeable / 已经是创世空名单交差 interchangeable，不是 318 validatorupdate interchangeable / 382 syncingheight item 3 interchangeable。

官方把空着、不是已经改了集合、不是已经是 InitChain 空名单写成三个名字。把它们叫成一个「看见空着就已经没有集合 interchangeable / 就已经改了集合 interchangeable / 就已经是 InitChain 空名单 interchangeable」，会把 not already empty、not already changed、not already genesis 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 validator_updates 空则引擎保持当前集合不是已经没有集合 not already empty / not already changed / not already genesis 正式三事（382 余量），先数清问的是空着 是不是 already empty / 382 / syncingheight-sold-as-history，是不是没回人 是不是 already changed，还是能空 是不是 already genesis，再决定要不要同一次发布。382 syncingheight-vs-history bundled unbundling 在本页 item 2 续。
