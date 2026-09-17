# 反模式：把 MaxBytes > 0 not already covering unbonding / not already enough to punish / not already settled 正式三事（331 余量） 卖成 已经盖住解绑 / 已经够罚 / 已经交差

**层次**：实现 / EvidenceParams.MaxBytes。  
**分类**：建议（产品）。  
**对应例**：[worked-example-evidence-maxbytes-notunbond-vs-bundled.md](../../tracks/implementation/worked-example-evidence-maxbytes-notunbond-vs-bundled.md)。

官方把填了证据 MaxBytes / > 0 / 证据 MaxBytes 三条核心句写成三件独立的实现事。把它们卖成已经盖住解绑 / 已经够罚 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 MaxBytes > 0 正式三事（331 余量），必须分开 not already covering unbonding、not already enough to punish、not already settled 三件事，不要和 331 / 46 / 63 / 920 / 922 糊成一句。

## 和相邻反模式

- [evidence-maxbytes-notunder-sold-as-bundled](evidence-maxbytes-notunder-sold-as-bundled.md) 是填了字段仍未落在块上限下面单句边界（920 item 1），不是本页合法下限还没盖住解绑边界。
- 默认证据窗已经够罚是不变量 46，不是本页 > 0 仍未盖住解绑边界。
