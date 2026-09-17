# 反模式：把 InitChain 请求 consensus_params not already no params / not already empty response / not already settled 正式三事（388 余量） 说成已经没有参数 / 已经用了回包空参数 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[InitChain ≠ bundled（388）](../../tracks/implementation/worked-example-initparams-notnoparams-vs-bundled.md)。

## 卖法

把 InitChain 请求余栏这句写成已经已经没有参数 / 已经用了回包空参数 / 已经交差 interchangeable，或已经和 388 initparams-vs-empty bundled / initparams-notnoparams-sold-as-bundled interchangeable。

## 为什么错

官方把 InitChain 请求 consensus_params / validators / app_state_bytes 三条核心句写成三件独立的实现事。把它们卖成已经没有参数 / 已经用了回包空参数 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain 请求 consensus_params 正式三事（388 余量），必须分开 not already no params、not already empty response、not already settled 三件事，不要和 388 / 319 / 495 / 765 / 766 糊成一句。

## 和相邻反模式

- [initparams-sold-as-empty](initparams-sold-as-empty.md) 是 InitChain 请求余栏 bundled（388），不是本页 item 1 单句边界。
- [initparams-notnoset-sold-as-bundled](initparams-notnoset-sold-as-bundled.md) 是 validators 单句边界（765 item 2），不是本页 consensus_params 边界。
