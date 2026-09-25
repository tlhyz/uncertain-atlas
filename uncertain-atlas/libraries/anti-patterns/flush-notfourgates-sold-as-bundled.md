# 反模式：把定期 Flush 是为了让异步请求真发出去不是已经是四门 not already fourgates / not already received / not already settled 正式三事（374 余量）说成已经是四门 / 已经收到 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[定期在冲 not already fourgates ≠ bundled（374）](../../tracks/implementation/worked-example-flush-notfourgates-vs-bundled.md)。

## 卖法

把定期在冲 / 定期 Flush 是为了让异步请求真发出去 / 定期在冲队列 写成已经是四门 interchangeable / 已经 fourgates interchangeable / 已经是四门交差 interchangeable / 374 flush bundled interchangeable / flush-sold-as-sent interchangeable；把发出去了 / 异步请求真发出去 / 发出去 写成已经收到 interchangeable / 已经 received interchangeable / 已经收到交差 interchangeable；把异步 / 异步请求 / 异步在冲 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，或已经和 374 flush bundled / flush-sold-as-sent interchangeable / 870 flush-notfourgates interchangeable。

## 为什么错

官方把定期在冲、不是已经收到、不是已经交差写成三件独立的实现事。把它们卖成 already fourgates interchangeable / already received interchangeable / already settled interchangeable，会把 not already fourgates、not already received、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看定期 Flush 是为了让异步请求真发出去不是已经是四门 not already fourgates / not already received / not already settled 正式三事（374 余量），必须分开 not already fourgates、not already received、not already settled 三件事，不要和 374 / 307 / 869 / 33 糊成一句。

## 和相邻反模式

- [flush-sold-as-sent](flush-sold-as-sent.md) 是 flush bundled 全段，不是本页定期在冲 item 2 单句边界。
- [flush-notsent-sold-as-bundled](flush-notsent-sold-as-bundled.md) 是叫了 not already sent（374 item 1），不是本页 not already fourgates 边界。
- [conn-sold-as-gates](conn-sold-as-gates.md) 是一条连接就已经是四门（307），不是本页 not already fourgates 单句。
- [checktx-sold-as-prepared](checktx-sold-as-prepared.md) 是四门已经结算（33），不是本页 not already settled 边界。
