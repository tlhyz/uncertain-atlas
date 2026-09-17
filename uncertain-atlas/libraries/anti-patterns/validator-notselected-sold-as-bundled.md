# 反模式：把 不带 PubKey not already selected / not already no PQ key / not already settled 正式三事（364 余量） 卖成 已经选型 / 已经没有后量子钥 / 已经交差

**层次**：实现 / Validator 类型。  
**分类**：建议（产品）。  
**对应例**：[worked-example-validator-notselected-vs-bundled.md](../../tracks/implementation/worked-example-validator-notselected-vs-bundled.md)。

官方把 Validator 用 address 认人 / 不带 PubKey / ValidatorUpdate 用公钥认人三条核心句写成三件独立的实现事。把它们卖成已经选型 / 已经没有后量子钥 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看不带 PubKey 正式三事（364 余量），必须分开 not already selected、not already no PQ key、not already settled 三件事，不要和 364 / 318 / 385 / 774 / 833 / 835 糊成一句。

## 和相邻反模式

- [validator-notpubkey-sold-as-bundled](validator-notpubkey-sold-as-bundled.md) 是 address 认人单句边界（833 item 1），不是本页不带 PubKey 边界。
- [initparams-notnoset-sold-as-bundled](initparams-notnoset-sold-as-bundled.md) 是 InitChain 空名单就已经没有集合（318），不是本页不带 PubKey 边界。
