# 反模式：把 同一批重复公钥 not already last wins / not already recoverable / not already settled 正式三事（318 余量） 卖成 已经按后一条改权 / 已经能恢复 / 已经交差

**层次**：实现 / ValidatorUpdate。  
**分类**：建议（产品）。  
**对应例**：[worked-example-validatorupdate-notdup-vs-bundled.md](../../tracks/implementation/worked-example-validatorupdate-notdup-vs-bundled.md)。

官方把 InitChain 空名单 / 同一批重复公钥 / power 写成 0 三条核心句写成三件独立的实现事。把它们卖成已经按后一条改权 / 已经能恢复 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看同一批重复公钥 正式三事（318 余量），必须分开 not already last wins、not already recoverable、not already settled 三件事，不要和 318 / 35 / 302 / 905 / 907 糊成一句。

## 和相邻反模式

- [validatorupdate-notempty-sold-as-bundled](validatorupdate-notempty-sold-as-bundled.md) 是 InitChain 空名单单句边界（905 item 1），不是本页同一批不得重复边界。
- H 的更新已经在 H+1 计票是不变量 35，不是本页同一批重复不可恢复边界。
