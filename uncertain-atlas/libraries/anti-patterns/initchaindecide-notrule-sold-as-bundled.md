# 反模式：把 InitChain Usage app decide accept or different one not Response empty/not empty rule / not InitChain Usage remainder bundled / not genesis app_state already verified 正式三事（496 余量） 说成已经 Response 规则 / 已经 412 bundled / 已经验过应用状态

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[InitChain ≠ bundled（496）](../../tracks/implementation/worked-example-initchaindecide-notrule-vs-bundled.md)。

## 卖法

把 InitChain Usage 这句写成已经已经 Response 规则 / 已经 412 bundled / 已经验过应用状态 interchangeable，或已经和 496 initchainusage-decide-vs-emptyset bundled / initchaindecide-notrule-sold-as-bundled interchangeable。

## 为什么错

官方把 InitChain Usage 后三条核心句写成三件独立的实现事。把它们卖成已经 Response 规则 / 已经 412 bundled / 已经验过应用状态，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain Usage decide 正式三事（496 余量），必须分开 not Response rule、not remainder bundled、not genesis app_state already verified 三件事，不要和 496 / 495 / 412 / 303 / 699 / 700 糊成一句。

## 和相邻反模式

- [initchainusage-decide-sold-as-bundled](initchainusage-decide-sold-as-bundled.md) 是 InitChain Usage app decide bundled（496），不是本页 item 1 单句边界。
- [initchaindecide-notchanged-sold-as-bundled](initchaindecide-notchanged-sold-as-bundled.md) 是 both ValidatorUpdate 单句边界（699 item 2），不是本页 decide 边界。
