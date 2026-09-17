# 反模式：把 validValue 非 nil not already will still call Prepare / not already can change list / not already settled 正式三事（356 余量） 卖成 已经还会调 Prepare / 已经能再改列表 / 已经交差

**层次**：实现 / validValue 跳过 Prepare。  
**分类**：建议（产品）。  
**对应例**：[worked-example-validvalue-notcall-vs-bundled.md](../../tracks/implementation/worked-example-validvalue-notcall-vs-bundled.md)。

官方把 validValue 非 nil 不再调 Prepare / 只有提议者且 validValue 为 nil 才调 / 没调 Prepare 不是又装 raw 提案三条核心句写成三件独立的实现事。把它们卖成已经还会调 Prepare / 已经能再改列表 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 validValue 非 nil 正式三事（356 余量），必须分开 not already will still call Prepare、not already can change list、not already settled 三件事，不要和 356 / 311 / 355 / 338 / 852 / 853 糊成一句。

## 和相邻反模式

- 候选已经是 ExecuteTxState 是不变量 311，不是本页 validValue 非 nil 边界。
- 从提案拿掉 tx 就已经从内存池删掉是不变量 355，不是本页还会调 Prepare 边界。
