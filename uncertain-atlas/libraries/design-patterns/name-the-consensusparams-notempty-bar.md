# 模式：把 InitChain 空参数不是已经没有参数 not already no params / not already deleted genesis params / not already app empty params 正式三事（319 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Updating Consensus Parameters。  
**例**：[回了空 not already no params ≠ bundled（319）](../../tracks/implementation/worked-example-consensusparams-notempty-vs-bundled.md)。

## 三个名字

1. **回了空 不是 already no params：** 看见 InitChain 回了空 ConsensusParams / 参数空，不是已经没有参数 interchangeable / 已经空参数交差 interchangeable，不是 319 consensusparams bundled interchangeable / 33 four gates interchangeable / consensusparams-sold-as-updated interchangeable。

2. **没回参数 不是 already deleted genesis params：** 看见没回 ConsensusParams / InitChain 没回参数，不是已经删掉创世参数 interchangeable / 已经清掉创世参数 interchangeable，不是 319 consensusparams item 2 interchangeable / 717 consensusparams-notclear interchangeable。

3. **能设初始参数 不是 already app empty params：** 看见 InitChain 能设参数 / 应用可设参数，不是已经用了应用自己的空参数 interchangeable / 已经和 InitChain 空验证者名单同一句 interchangeable，不是 319 consensusparams item 3 interchangeable / 718 consensusparams-notpartial interchangeable。

官方把回了空单句、already no params、already deleted genesis params、already app empty params 写成三个名字。把它们叫成一个「看见回了空就已经没有参数 interchangeable / 就已经删掉创世参数 interchangeable / 就已经和 InitChain 空验证者名单同一句 interchangeable」，会把 not already no params、not already deleted genesis params、not already app empty params 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain 空参数不是已经没有参数 not already no params / not already deleted genesis params / not already app empty params 正式三事（319 余量），先数清问的是回了空 是不是 already no params / 319 / consensusparams-sold-as-updated，是不是没回参数 是不是 already deleted genesis params，还是能设初始参数 是不是 already app empty params，再决定要不要同一次发布。319 consensusparams vs update bundled unbundling 在本页 item 1 完成。
