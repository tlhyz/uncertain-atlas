# 反模式：把 InitChain 请求 app_state_bytes not already verified / not already balances / not already settled 正式三事（388 余量） 说成已经验过应用状态 / 已经懂余额 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[InitChain ≠ bundled（388）](../../tracks/implementation/worked-example-initparams-notverified-vs-bundled.md)。

## 卖法

把 InitChain 请求余栏这句写成已经已经验过应用状态 / 已经懂余额 / 已经交差 interchangeable，或已经和 388 initparams-vs-empty bundled / initparams-notverified-sold-as-bundled interchangeable。

## 为什么错

官方把 InitChain 请求 consensus_params / validators / app_state_bytes 三条核心句写成三件独立的实现事。把它们卖成已经验过应用状态 / 已经懂余额 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain 请求 app_state_bytes 正式三事（388 余量），必须分开 not already verified、not already balances、not already settled 三件事，不要和 388 / 303 / 392 / 755 / 764 / 765 糊成一句。

## 和相邻反模式

- [initparams-sold-as-empty](initparams-sold-as-empty.md) 是 InitChain 请求余栏 bundled（388），不是本页 item 3 单句边界。
- [initapphash-notheader-sold-as-bundled](initapphash-notheader-sold-as-bundled.md) 是 InitChain 回包 app_hash 就已经是本头 AppHash（392/755），不是本页 app_state_bytes 边界。
