# 反模式：把 InitChain 请求 validators not already no set / not already empty list / not already settled 正式三事（388 余量） 说成已经没有集合 / 已经用了回包空名单 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[InitChain ≠ bundled（388）](../../tracks/implementation/worked-example-initparams-notnoset-vs-bundled.md)。

## 卖法

把 InitChain 请求余栏这句写成已经已经没有集合 / 已经用了回包空名单 / 已经交差 interchangeable，或已经和 388 initparams-vs-empty bundled / initparams-notnoset-sold-as-bundled interchangeable。

## 为什么错

官方把 InitChain 请求 consensus_params / validators / app_state_bytes 三条核心句写成三件独立的实现事。把它们卖成已经没有集合 / 已经用了回包空名单 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain 请求 validators 正式三事（388 余量），必须分开 not already no set、not already empty list、not already settled 三件事，不要和 388 / 318 / 764 / 766 糊成一句。

## 和相邻反模式

- [initparams-sold-as-empty](initparams-sold-as-empty.md) 是 InitChain 请求余栏 bundled（388），不是本页 item 2 单句边界。
- [initparams-notnoparams-sold-as-bundled](initparams-notnoparams-sold-as-bundled.md) 是 consensus_params 单句边界（764 item 1），不是本页 validators 边界。
