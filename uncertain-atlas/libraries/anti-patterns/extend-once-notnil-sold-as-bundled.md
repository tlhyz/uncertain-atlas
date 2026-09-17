# 反模式：把 ExtendVote 只在即将广播非 nil Precommit 时才叫 not already signed nil / not already every vote calls / not already settled 正式三事（350 余量） 卖成 已经签了 nil 票 / 已经每张票都会叫 / 已经交差

**层次**：实现 / 一轮一份扩展。  
**分类**：建议（产品）。  
**对应例**：[worked-example-extend-once-notnil-vs-bundled.md](../../tracks/implementation/worked-example-extend-once-notnil-vs-bundled.md)。

官方把一轮最多一张 Precommit / ExtendVote 只在即将广播非 nil Precommit 时才叫 / 一轮只能交出一份扩展 三条核心句写成三件独立的实现事。把它们卖成已经签了 nil 票 / 已经每张票都会叫 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote 只在即将广播非 nil Precommit 时才叫 正式三事（350 余量），必须分开 not already signed nil、not already every vote calls、not already settled 三件事，不要和 350 / 338 / 34 / 863 / 865 糊成一句。

## 和相邻反模式

- [extend-once-notresign-sold-as-bundled](extend-once-notresign-sold-as-bundled.md) 是一轮一张单句边界（863 item 1），不是本页何时才叫边界。
- 同一块已经是同一份扩展是不变量 338，不是本页何时才叫边界。
