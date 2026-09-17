# 反模式：把 一轮最多一张 Precommit not already can sign another / not already is the extension / not already settled 正式三事（350 余量） 卖成 已经能再签一张 / 已经是扩展本身 / 已经交差

**层次**：实现 / 一轮一份扩展。  
**分类**：建议（产品）。  
**对应例**：[worked-example-extend-once-notresign-vs-bundled.md](../../tracks/implementation/worked-example-extend-once-notresign-vs-bundled.md)。

官方把一轮最多一张 Precommit / ExtendVote 只在即将广播非 nil Precommit 时才叫 / 一轮只能交出一份扩展 三条核心句写成三件独立的实现事。把它们卖成已经能再签一张 / 已经是扩展本身 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看一轮最多一张 Precommit 正式三事（350 余量），必须分开 not already can sign another、not already is the extension、not already settled 三件事，不要和 350 / 34 / 351 / 860 / 864 / 865 糊成一句。

## 和相邻反模式

- [process-also-notskip-sold-as-bundled](process-also-notskip-sold-as-bundled.md) 是提议者也会叫 Process（351/860），不是本页一轮一张边界。
- 验签拒收整张预提交就已经是块非法是不变量 34，不是本页一轮一张边界。
