# 反模式：把 没调 Prepare not already packed another raw proposal / not already dropped tx from proposal / not already settled 正式三事（356 余量） 卖成 已经又装了一份 raw 提案 / 已经从提案拿掉 tx / 已经交差

**层次**：实现 / validValue 跳过 Prepare。  
**分类**：建议（产品）。  
**对应例**：[worked-example-validvalue-notraw-vs-bundled.md](../../tracks/implementation/worked-example-validvalue-notraw-vs-bundled.md)。

官方把 validValue 非 nil 不再调 Prepare / 只有提议者且 validValue 为 nil 才调 / 没调 Prepare 不是又装 raw 提案三条核心句写成三件独立的实现事。把它们卖成已经又装了一份 raw 提案 / 已经从提案拿掉 tx / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看没调 Prepare 正式三事（356 余量），必须分开 not already packed another raw proposal、not already dropped tx from proposal、not already settled 三件事，不要和 356 / 355 / 311 / 851 / 852 糊成一句。

## 和相邻反模式

- [validvalue-notevery-sold-as-bundled](validvalue-notevery-sold-as-bundled.md) 是提议者单句边界（852 item 2），不是本页没调 Prepare 边界。
- 从提案拿掉 tx 就已经从内存池删掉是不变量 355，不是本页又装 raw 提案边界。
