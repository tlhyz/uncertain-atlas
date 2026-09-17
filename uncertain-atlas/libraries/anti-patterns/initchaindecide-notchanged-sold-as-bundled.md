# 反模式：把 InitChain Usage Both Validators are ValidatorUpdate not already changed set / not empty list means no set / not Validator without PubKey already has PubKey 正式三事（496 余量） 说成已经改了集合 / 已经空名单就没有集合 / 已经带了公钥

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[InitChain ≠ bundled（496）](../../tracks/implementation/worked-example-initchaindecide-notchanged-vs-bundled.md)。

## 卖法

把 InitChain Usage 这句写成已经已经改了集合 / 已经空名单就没有集合 / 已经带了公钥 interchangeable，或已经和 496 initchainusage-decide-vs-emptyset bundled / initchaindecide-notchanged-sold-as-bundled interchangeable。

## 为什么错

官方把 InitChain Usage 后三条核心句写成三件独立的实现事。把它们卖成已经改了集合 / 已经空名单就没有集合 / 已经带了公钥，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain Usage both ValidatorUpdate 正式三事（496 余量），必须分开 not already changed set、not empty list means no set、not Validator without PubKey already has PubKey 三件事，不要和 496 / 364 / 318 / 698 / 700 糊成一句。

## 和相邻反模式

- [initchainusage-decide-sold-as-bundled](initchainusage-decide-sold-as-bundled.md) 是 InitChain Usage app decide bundled（496），不是本页 item 2 单句边界。
- [initchaindecide-notrule-sold-as-bundled](initchaindecide-notrule-sold-as-bundled.md) 是 decide 单句边界（698 item 1），不是本页 both ValidatorUpdate 边界。
