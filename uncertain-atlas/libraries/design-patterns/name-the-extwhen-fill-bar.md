# 模式：把 ExtendVote When fill CanonicalVoteExtension 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote When step 4。  
**例**：[fill CanonicalVoteExtension ≠ bundled](../../tracks/implementation/worked-example-extwhen-fill-vs-bundled.md)。

## 三个名字

1. **sets extension into CanonicalVoteExtension.extension 不是 return extension bundled：** 看见 sets ExtendVoteResponse.extension as extension field value，不是 509 return extension interchangeable。
2. **populates other fields 不是 ExtendVoteRequest 栏 bundled：** 看见 populates Height/Round/ChainID in CanonicalVoteExtension，不是 410 Request 栏 interchangeable。
3. **signs populated CanonicalVoteExtension 不是 ExtendVote When 正式流程 bundled：** 看见 signs populated data structure，不是 438 填包装并签名 bundled / 构造 CanonicalVote interchangeable。

## 为什么要分开叫

官方把 sets extension field、populates other fields、signs populated structure、return extension bundled（509）、ExtendVote When 正式流程 bundled（438）、按原样签（358）写成三个名字。把它们叫成一个「看见回了 extension 就已经按原样签 interchangeable、已经验过扩展 interchangeable、已经 ExtendVote 回了 extension 就已经广播 Precommit interchangeable」，会把 fill、populate、sign 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote When fill CanonicalVoteExtension 正式三事，先数清问的是 sets extension field 是不是 return extension bundled interchangeable、populates other fields 是不是 ExtendVoteRequest 栏 bundled interchangeable、signs populated structure 是不是 ExtendVote When 正式流程 bundled interchangeable，再决定要不要同一次发布。
