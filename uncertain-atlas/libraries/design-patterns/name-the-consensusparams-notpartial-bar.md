# 模式：把只改一个字段不是已经只改这一项 not already only-that / not already rest-unchanged / not already field-merge 正式三事（319 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Updating Consensus Parameters。  
**例**：[只填一项 not already only-that ≠ bundled（319）](../../tracks/implementation/worked-example-consensusparams-notpartial-vs-bundled.md)。

## 三个名字

1. **只填一项 不是 already only-that：** 看见 Block 只填了 MaxBytes / 只改了其中一个字段，不是已经只改这一项 interchangeable / 已经只改这一项交差 interchangeable，不是 319 consensusparams bundled interchangeable / 33 four gates interchangeable / consensusparams-sold-as-updated interchangeable。

2. **没写字段 不是 already rest-unchanged：** 看见没写的 Block 字段 / 其余字段空着，不是已经保持原值 interchangeable / 已经保持其余不变 interchangeable，不是 319 consensusparams item 2 interchangeable / 717 consensusparams-notclear interchangeable。

3. **能整份套上 不是 already field-merge：** 看见不空字段会套上 / 空的 ConsensusParams 会被忽略，不是已经是按字段合并 interchangeable / 已经 field-wise merge interchangeable，不是 319 consensusparams item 1 interchangeable / 716 consensusparams-notempty interchangeable。

官方把只填一项单句、already only-that、already rest-unchanged、already field-merge 写成三个名字。把它们叫成一个「看见只改了其中一个字段就已经只改这一项 interchangeable / 就已经保持其余不变 interchangeable / 就已经是 field-wise merge interchangeable」，会把 not already only-that、not already rest-unchanged、not already field-merge 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看只改一个字段不是已经只改这一项 not already only-that / not already rest-unchanged / not already field-merge 正式三事（319 余量），先数清问的是只填一项 是不是 already only-that / 319 / consensusparams-sold-as-updated，是不是没写字段 是不是 already rest-unchanged，还是能整份套上 是不是 already field-merge，再决定要不要同一次发布。319 consensusparams vs update bundled unbundling 在本页 item 3 完成。
