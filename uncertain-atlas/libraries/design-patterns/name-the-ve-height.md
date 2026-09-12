# 模式：把 VoteExtensionsEnableHeight 三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / Application configuration required to switch to ABCI 2.0。  
**例**：[到了 H ≠ 已经 Prepare 带了扩展](../../tracks/implementation/worked-example-ve-height-vs-prepare.md)。

## 三个名字

1. **到了 H 不是已经 Prepare 带了扩展：** 看见已经叫了 ExtendVote 不是已经把扩展写进本高提议。
2. **H+1 带了扩展不是已经是本高度刚签的：** 看见 Prepare 列表里有扩展不是已经是这一高的 *e*。
3. **h < H 带了扩展不是已经合法：** 看见字段在不是已经切到 ABCI 2.0。

## 为什么要分开叫

官方把开始叫 ExtendVote、Prepare 开始带上一高的扩展、启用前带扩展的预提交写成三件事。把它们叫成一个「看见到了 H 就已经切到 ABCI 2.0」，会把验签、治理 panic 和验证人集合一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「到了 H 就已经 Prepare 带了扩展」，先数清问的是到了 H 不是已经 Prepare 带了扩展、H+1 带了扩展不是已经是本高度刚签的，还是 h < H 带了扩展不是已经合法，再决定要不要同一次发布。
