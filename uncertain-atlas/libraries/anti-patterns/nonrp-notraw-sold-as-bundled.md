# 反模式：把 vote_extension 会包进 CanonicalVoteExtension 不是已经按原样签 not already raw-signed / not already canon-vote / not already settled 正式三事（358 余量）说成已经按原样签 / 已经是 CanonicalVote / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[vote_extension 包进 CanonicalVoteExtension not already raw-signed ≠ bundled（358）](../../tracks/implementation/worked-example-nonrp-notraw-vs-bundled.md)。

## 卖法

把绑了 Height Round ChainID / `vote_extension` 会包进 `CanonicalVoteExtension` / 绑了这些字段 写成已经按原样签 interchangeable / 已经 raw-signed interchangeable / 已经按原样签交差 interchangeable / 358 nonrp bundled interchangeable / nonrp-sold-as-protected interchangeable；把有包装 / 进了 CanonicalVoteExtension 写成已经是票上那份 CanonicalVote interchangeable / 已经 canon-vote interchangeable / 已经是 CanonicalVote 交差 interchangeable；把签了 / 填完字段后签名 / 签名挂上 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，或已经和 358 nonrp bundled / nonrp-sold-as-protected interchangeable / 827 nonrp-notraw interchangeable。

## 为什么错

官方把绑了这些字段、不是已经是 CanonicalVote、不是已经交差写成三件独立的实现事。把它们卖成 already raw-signed interchangeable / already canon-vote interchangeable / already settled interchangeable，会把 not already raw-signed、not already canon-vote、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 vote_extension 会包进 CanonicalVoteExtension 不是已经按原样签 not already raw-signed / not already canon-vote / not already settled 正式三事（358 余量），必须分开 not already raw-signed、not already canon-vote、not already settled 三件事，不要和 358 / 34 / 350 / 828 / 829 糊成一句。

## 和相邻反模式

- [nonrp-sold-as-protected](nonrp-sold-as-protected.md) 是两份扩展两份签 bundled 全段，不是本页绑了这些字段 item 1 单句边界。
- [vote-extension-sold-as-block](vote-extension-sold-as-block.md) 是 CanonicalVoteExtension 就已经是 CanonicalVote（34），不是本页 not already raw-signed 边界。
- [checktx-sold-as-prepared](checktx-sold-as-prepared.md) 是四门已经结算（33），不是本页 not already settled 边界。
