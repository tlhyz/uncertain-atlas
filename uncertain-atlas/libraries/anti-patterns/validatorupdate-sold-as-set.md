# 反模式：看见 InitChain 回了空名单就当成已经没有集合 / 看见重复公钥就当成已经能恢复 / 看见 power 0 就当成已经删掉不在集合里的人

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Updating the Validator Set。  
**例**：[InitChain 空名单 ≠ 已经没有集合](../../tracks/implementation/worked-example-validatorupdate-vs-set.md)。

## 塌法

1. 看见 InitChain 回了空名单 / 看见没回验证者，就当成已经没有集合，或当成已经用了应用自己的空集。
2. 看见一次更新里同一把公钥出现两次 / 看见重复，就当成已经按后一条改权，或当成已经能恢复。
3. 看见 power 写成 0 / 看见名单里没有这个人，就当成已经删掉，或当成已经能对不在集合里的人写 0。

## 为什么会出事

官方写：InitChain 回空就用创世文件里的验证者。同一批更新里重复公钥会让块执行不可恢复地失败。写成 0 时这个人必须已经在集合里才会被删掉；总投票权不得超过 MaxTotalVotingPower。

## 和相邻反模式

- [appstate-sold-as-validated](appstate-sold-as-validated.md) 是创世 validators 空 ≠ 已经没有集合，不是本页这种 InitChain 回空。
- [rejoin-sold-as-head](rejoin-sold-as-head.md) 是同一高度换轮 ≠ 已经换了集合，不是本页。
