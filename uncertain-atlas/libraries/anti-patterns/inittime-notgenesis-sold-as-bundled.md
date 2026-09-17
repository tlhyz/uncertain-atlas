# 反模式：把 InitChain 请求 time not already past genesis_time / not already producing blocks / not already settled 正式三事（387 余量） 说成已经过了 genesis_time / 已经开出块 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[InitChain ≠ bundled（387）](../../tracks/implementation/worked-example-inittime-notgenesis-vs-bundled.md)。

## 卖法

把 InitChain 请求这句写成已经已经过了 genesis_time / 已经开出块 / 已经交差 interchangeable，或已经和 387 inittime-vs-genesis bundled / inittime-notgenesis-sold-as-bundled interchangeable。

## 为什么错

官方把 InitChain 请求 time / chain_id / initial_height 三条核心句写成三件独立的实现事。把它们卖成已经过了 genesis_time / 已经开出块 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain 请求 time 正式三事（387 余量），必须分开 not already past genesis_time、not already producing blocks、not already settled 三件事，不要和 387 / 303 / 388 / 766 / 768 / 769 糊成一句。

## 和相邻反模式

- [inittime-sold-as-genesis](inittime-sold-as-genesis.md) 是 InitChain 请求 bundled（387），不是本页 item 1 单句边界。
- [initparams-notverified-sold-as-bundled](initparams-notverified-sold-as-bundled.md) 是 InitChain 请求余栏 app_state_bytes 就已经验过（388/766），不是本页 time 边界。
