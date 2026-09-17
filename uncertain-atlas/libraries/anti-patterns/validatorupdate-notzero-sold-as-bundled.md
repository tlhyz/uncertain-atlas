# 反模式：把 power 写成 0 not already deleted outsider / not already no cap / not already settled 正式三事（318 余量） 卖成 已经删掉不在集合里的人 / 已经没有上限 / 已经交差

**层次**：实现 / ValidatorUpdate。  
**分类**：建议（产品）。  
**对应例**：[worked-example-validatorupdate-notzero-vs-bundled.md](../../tracks/implementation/worked-example-validatorupdate-notzero-vs-bundled.md)。

官方把 InitChain 空名单 / 同一批重复公钥 / power 写成 0 三条核心句写成三件独立的实现事。把它们卖成已经删掉不在集合里的人 / 已经没有上限 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 power 写成 0 正式三事（318 余量），必须分开 not already deleted outsider、not already no cap、not already settled 三件事，不要和 318 / 302 / 364 / 905 / 906 糊成一句。

## 和相邻反模式

- [validatorupdate-notdup-sold-as-bundled](validatorupdate-notdup-sold-as-bundled.md) 是同一批重复单句边界（906 item 2），不是本页 power 0 必须已在集合里才删边界。
- 同一高度换轮已经换了集合是不变量 302，不是本页 power 0 边界。
