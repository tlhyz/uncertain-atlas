# 模式：把 ConsensusParams 三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Updating Consensus Parameters。  
**例**：[InitChain 空参数 ≠ 已经没有参数](../../tracks/implementation/worked-example-consensusparams-vs-update.md)。

## 三个名字

1. **InitChain 空参数不是已经没有参数：** 看见回空不是已经删掉创世参数。
2. **Finalize 没回不是已经清掉：** 看见空着不是已经改过。
3. **只改一个字段不是已经只改这一项：** 看见只填 MaxBytes 不是已经保持其余 Block 字段。

## 为什么要分开叫

官方把回空改用创世、Finalize 回空什么也不做、不空字段整份套上写成三件事。把它们叫成一个「看见回了参数就已经改完」，会把生效高度、气上限和空验证者名单一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「ConsensusParams 已经回了」，先数清问的是 InitChain 空着不是已经没有参数、Finalize 没回不是已经清掉，还是只填一项不是已经只改这一项，再决定要不要同一次发布。
