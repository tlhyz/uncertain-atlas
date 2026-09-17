# 反模式：把 拜占庭能提案一满块无效交易 not already pool-blocked / not already out-of-consensus / not already settled 正式三事（339 余量） 卖成 已经被池子挡住 / 已经进不了共识 / 已经交差

**层次**：实现 / CheckTx 弱过滤器。  
**分类**：建议（产品）。  
**对应例**：[worked-example-checktx-weak-notpool-vs-bundled.md](../../tracks/implementation/worked-example-checktx-weak-notpool-vs-bundled.md)。

官方把不该验排序相关有效性 / 拜占庭能提案一满块无效交易 / ProcessProposal 对付这种行为 三条核心句写成三件独立的实现事。把它们卖成已经被池子挡住 / 已经进不了共识 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看拜占庭能提案一满块无效交易 正式三事（339 余量），必须分开 not already pool-blocked、not already out-of-consensus、not already settled 三件事，不要和 339 / 33 / 313 / 929 / 931 糊成一句。

## 和相邻反模式

- [checktx-weak-notsort-sold-as-bundled](checktx-weak-notsort-sold-as-bundled.md) 是不该验排序仍不该写进 CheckTx 单句边界（929 item 1），不是本页拜占庭仍能提案无效块边界。
- 四门已经结算是不变量 33，不是本页池子挡不住拜占庭边界。
