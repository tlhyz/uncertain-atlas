# 反模式：把 ExtendVote When fill CanonicalVoteExtension 正式三事卖成 return extension bundled / ExtendVote When 正式流程 / 按原样签

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[fill CanonicalVoteExtension ≠ bundled](../../tracks/implementation/worked-example-extwhen-fill-vs-bundled.md)。

## 卖法

- 「看见 sets ExtendVoteResponse.extension into CanonicalVoteExtension.extension 就已经 return extension bundled interchangeable / 已经按原样签 interchangeable。」
- 「看见 populates other fields in CanonicalVoteExtension 就已经 ExtendVoteRequest 栏 bundled interchangeable / 已经只有 extension 字节 interchangeable。」
- 「看见 signs populated CanonicalVoteExtension 就已经 ExtendVote When 正式流程 interchangeable / 已经广播 Precommit interchangeable / 已经验过扩展 interchangeable。」

## 为什么错

官方把 sets extension field、populates other fields、signs populated structure 写成三件独立的实现事。把它们卖成 return extension bundled、ExtendVote When 正式流程、按原样签，会把 fill、populate、sign 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote When fill CanonicalVoteExtension 正式三事，必须分开 sets extension field、populates other fields、signs populated structure 三个名字，不要把它们卖成 return extension bundled / ExtendVote When 正式流程 / 按原样签。

## 和相邻反模式

- [extwhen-return-sold-as-bundled](extwhen-return-sold-as-bundled.md) 是 ExtendVote When return extension 三事，不是本页 sets extension field 单句专用边界。
- [extwhenformal-sold-as-broadcast](extwhenformal-sold-as-broadcast.md) 是 ExtendVote When 正式流程三事，不是本页 signs populated CanonicalVoteExtension 单句专用边界。
- [nonrp-sold-as-protected](nonrp-sold-as-protected.md) 是 vote_extension 会包进 CanonicalVoteExtension 就已经按原样签，不是本页 populate other fields 单句专用边界。
