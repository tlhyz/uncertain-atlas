# 反模式：看见 InitChain 回了空 ConsensusParams 就当成已经没有参数 / 看见 Finalize 没回就当成已经清掉 / 看见只改一个字段就当成已经只改这一项

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Updating Consensus Parameters。  
**例**：[InitChain 空参数 ≠ 已经没有参数](../../tracks/implementation/worked-example-consensusparams-vs-update.md)。

## 塌法

1. 看见 InitChain 回了空 ConsensusParams / 看见没回参数，就当成已经没有参数，或当成已经用了应用自己的空参数。
2. 看见 FinalizeBlock 回了空 / 看见没回 ConsensusParams，就当成已经清掉，或当成已经改了。
3. 看见只改了其中一个字段 / 看见 Block 只填了 MaxBytes，就当成已经只改这一项，或当成已经保持其余不变。

## 为什么会出事

官方写：InitChain 回空就用创世文件里的参数。Finalize 回空什么也不做。每一个不空的字段会整份套上；只改 `Block.MaxBytes` 却不写其余 Block 字段，那些字段会被更新成默认。

## 和相邻反模式

- [validatorupdate-sold-as-set](validatorupdate-sold-as-set.md) 是 InitChain 空验证者名单 ≠ 已经没有集合，不是本页这种空参数。
- [maxgas-sold-as-enforced](maxgas-sold-as-enforced.md) 是 MaxGas ≠ 已经在执行，不是本页这种只填一项被整份套上。
