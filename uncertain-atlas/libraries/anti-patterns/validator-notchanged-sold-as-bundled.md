# 反模式：把 ValidatorUpdate 用公钥认人 not already VoteInfo Validator / not already changed set / not already selected 正式三事（364 余量） 卖成 已经是 VoteInfo 里那份 Validator / 已经改了集合 / 已经选型

**层次**：实现 / Validator 类型。  
**分类**：建议（产品）。  
**对应例**：[worked-example-validator-notchanged-vs-bundled.md](../../tracks/implementation/worked-example-validator-notchanged-vs-bundled.md)。

官方把 Validator 用 address 认人 / 不带 PubKey / ValidatorUpdate 用公钥认人三条核心句写成三件独立的实现事。把它们卖成已经是 VoteInfo 里那份 Validator / 已经改了集合 / 已经选型，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ValidatorUpdate 用公钥认人 正式三事（364 余量），必须分开 not already VoteInfo Validator、not already changed set、not already selected 三件事，不要和 364 / 363 / 35 / 365 / 831 / 833 / 834 糊成一句。

## 和相邻反模式

- [validator-notselected-sold-as-bundled](validator-notselected-sold-as-bundled.md) 是不带 PubKey 单句边界（834 item 2），不是本页 ValidatorUpdate 边界。
- 必须回四列就已经改了集合是不变量 363，不是本页 ValidatorUpdate 边界。
