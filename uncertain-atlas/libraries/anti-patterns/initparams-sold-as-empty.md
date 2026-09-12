# 反模式：看见 InitChain 请求 consensus_params 是起步共识参数就当成已经没有参数 / 看见 InitChain 请求 validators 是起步验证者名单就当成已经没有集合 / 看见 InitChain 请求 app_state_bytes 是序列化起步应用状态就当成已经验过应用状态

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Request。  
**例**：[InitChain 请求 consensus_params 是起步共识参数 ≠ 已经没有参数](../../tracks/implementation/worked-example-initparams-vs-empty.md)。

## 塌法

1. 看见 InitChain 请求 `consensus_params` 是起步共识参数 / 看见填了起步参数，就当成已经没有参数，或当成已经用了回包空参数。
2. 看见 InitChain 请求 `validators` 是起步验证者名单 / 看见填了起步名单，就当成已经没有集合，或当成已经用了回包空名单。
3. 看见 InitChain 请求 `app_state_bytes` 是序列化起步应用状态 / 看见填了 JSON 字节，就当成已经验过应用状态，或当成已经懂余额。

## 为什么会出事

官方写：`consensus_params` 是起步时共识关键参数。`validators` 是起步创世验证者，按投票权排序。`app_state_bytes` 是序列化起步应用状态，JSON 字节。

## 和相邻反模式

- [consensusparams-sold-as-updated](consensusparams-sold-as-updated.md) 是 InitChain 回了空 ConsensusParams 就已经没有参数，不是本页这种 InitChain 请求 consensus_params 是起步共识参数不是已经没有参数。
- [validatorupdate-sold-as-set](validatorupdate-sold-as-set.md) 是 InitChain 回了空名单就已经没有集合，不是本页这种 InitChain 请求 validators 是起步验证者名单不是已经没有集合。
- [appstate-sold-as-validated](appstate-sold-as-validated.md) 是创世 app_state 就已经验过应用状态，不是本页这种 InitChain 请求 app_state_bytes 是序列化起步应用状态不是已经验过应用状态。
