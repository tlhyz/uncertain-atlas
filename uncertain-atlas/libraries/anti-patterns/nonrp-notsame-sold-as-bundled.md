# 反模式：把要签原样数据可以用 non_rp 不是已经和 vote_extension 同一份 not already same-as-ve / not already empty-verify / not already settled 正式三事（358 余量）说成已经和 vote_extension 同一份 / 已经是空扩展仍验签 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[要签原样数据可以用 non_rp not already same-as-ve ≠ bundled（358）](../../tracks/implementation/worked-example-nonrp-notsame-vs-bundled.md)。

## 卖法

把有第二份 / 应用要签原样数据可以用 `non_rp` / 有第二份字段 写成已经和 vote_extension 同一份 interchangeable / 已经 same-as-ve interchangeable / 已经和第一份同一对象交差 interchangeable / 358 nonrp bundled interchangeable / nonrp-sold-as-protected interchangeable；把能空 / `non_rp_vote_extension` 可选也可以空 写成已经是空扩展仍验签 interchangeable / 已经 empty-verify interchangeable / 已经是 34 那种空扩展仍验签交差 interchangeable；把能用 / 可以用这份字段 / 不要包装也能签 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，或已经和 358 nonrp bundled / nonrp-sold-as-protected interchangeable / 829 nonrp-notsame interchangeable。

## 为什么错

官方把有第二份、不是已经是空扩展仍验签、不是已经交差写成三件独立的实现事。把它们卖成 already same-as-ve interchangeable / already empty-verify interchangeable / already settled interchangeable，会把 not already same-as-ve、not already empty-verify、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看要签原样数据可以用 non_rp 不是已经和 vote_extension 同一份 not already same-as-ve / not already empty-verify / not already settled 正式三事（358 余量），必须分开 not already same-as-ve、not already empty-verify、not already settled 三件事，不要和 358 / 353 / 34 / 827 / 828 糊成一句。

## 和相邻反模式

- [nonrp-sold-as-protected](nonrp-sold-as-protected.md) 是两份扩展两份签 bundled 全段，不是本页有第二份 item 3 单句边界。
- [verifywhen-sold-as-skipped](verifywhen-sold-as-skipped.md) 是空扩展仍会调 Verify 就已经跳过 Verify（353），不是本页 not already same-as-ve 边界。
- [nonrp-notprotected-sold-as-bundled](nonrp-notprotected-sold-as-bundled.md) 是 non_rp_extension 按原样签 not already replay-protected（358 item 2），不是本页 not already settled 边界。
