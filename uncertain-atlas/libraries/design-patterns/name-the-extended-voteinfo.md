# 模式：把 ExtendedVoteInfo 三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ExtendedVoteInfo。  
**例**：[ExtendedVoteInfo 从本进程抽出 ≠ 已经从块里抽出](../../tracks/implementation/worked-example-extvoteinfo-vs-local.md)。

## 三个名字

1. **从本进程抽出不是已经从块里抽出：** 看见 Prepare 里有这份不是已经带了公钥。
2. **把验过的签交给应用不是已经按原样签：** 看见没给 non_rp 就签空切片不是已经必须填。
3. **扩展关掉则字段全空不是已经到了启用高度：** 看见空着不是已经交差。

## 为什么要分开叫

官方把 `ExtendedVoteInfo` 从本进程抽出、把验过的签交给应用、扩展关掉则字段全空写成三件事。把它们叫成一个「看见 Prepare 里有扩展就已经从块里抽出」，会把 VoteInfo 抽出、两份扩展两份签和启用高度一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Prepare 里有扩展就已经从块里抽出」，先数清问的是从本进程抽出不是已经从块里抽出、把验过的签交给应用不是已经按原样签，还是扩展关掉则字段全空不是已经到了启用高度，再决定要不要同一次发布。
