# 反模式：把 validator_updates 空则引擎保持当前集合不是已经没有集合 not already empty / not already changed / not already genesis 正式三事（382 余量）说成已经没有集合 / 已经改了集合 / 已经是 InitChain 空名单

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[空着 not already empty ≠ bundled（382）](../../tracks/implementation/worked-example-syncingheight-notempty-vs-bundled.md)。

## 卖法

把空着 / validator_updates 空则引擎保持当前集合 / validator_updates 或 consensus_param_updates 可以空 写成已经没有集合 interchangeable / 已经 empty interchangeable / 已经没有集合交差 interchangeable / 382 syncingheight bundled interchangeable / syncingheight-sold-as-history interchangeable；把没回人 / 没回 validator_updates / 保持当前值 写成已经改了集合 interchangeable / 已经 changed interchangeable / 已经改了集合交差 interchangeable；把能空 / Finalize 回包可以空着更新 / 空着不是 InitChain 那种空名单 写成已经是 InitChain 空名单 interchangeable / 已经 genesis interchangeable / 已经是创世空名单交差 interchangeable，或已经和 382 syncingheight bundled / syncingheight-sold-as-history interchangeable / 894 syncingheight-notempty interchangeable。

## 为什么错

官方把空着、不是已经改了集合、不是已经是 InitChain 空名单写成三件独立的实现事。把它们卖成 already empty interchangeable / already changed interchangeable / already genesis interchangeable，会把 not already empty、not already changed、not already genesis 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 validator_updates 空则引擎保持当前集合不是已经没有集合 not already empty / not already changed / not already genesis 正式三事（382 余量），必须分开 not already empty、not already changed、not already genesis 三件事，不要和 382 / 318 / 323 / 316 糊成一句。

## 和相邻反模式

- [syncingheight-sold-as-history](syncingheight-sold-as-history.md) 是 syncingheight bundled 全段，不是本页空着 item 2 单句边界。
- [syncingheight-nothistory-sold-as-bundled](syncingheight-nothistory-sold-as-bundled.md) 是填了目标 item 1 单句边界，不是本页 not already empty 边界。
- [validatorupdate-sold-as-set](validatorupdate-sold-as-set.md) 是 InitChain 空名单就已经没有集合（318），不是本页 not already genesis 单句。
- [exectxresult-sold-as-consensus](exectxresult-sold-as-consensus.md) 是结果列表就已经同一顺序（316），不是本页 not already changed 边界。
