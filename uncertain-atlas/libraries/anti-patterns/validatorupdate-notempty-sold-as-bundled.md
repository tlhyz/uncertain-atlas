# 反模式：把 InitChain 空名单 not already no set / not already app empty set / not already settled 正式三事（318 余量） 卖成 已经没有集合 / 已经用了应用自己的空集 / 已经交差

**层次**：实现 / ValidatorUpdate。  
**分类**：建议（产品）。  
**对应例**：[worked-example-validatorupdate-notempty-vs-bundled.md](../../tracks/implementation/worked-example-validatorupdate-notempty-vs-bundled.md)。

官方把 InitChain 空名单 / 同一批重复公钥 / power 写成 0 三条核心句写成三件独立的实现事。把它们卖成已经没有集合 / 已经用了应用自己的空集 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain 空名单 正式三事（318 余量），必须分开 not already no set、not already app empty set、not already settled 三件事，不要和 318 / 303 / 364 / 906 / 907 糊成一句。

## 和相邻反模式

- [validator-notchanged-sold-as-bundled](validator-notchanged-sold-as-bundled.md) 是 Validator 用公钥认人（364/835），不是本页 InitChain 回空改用创世名单边界。
- 创世 validators 空已经没有集合是不变量 303，不是本页 InitChain 回空边界。
