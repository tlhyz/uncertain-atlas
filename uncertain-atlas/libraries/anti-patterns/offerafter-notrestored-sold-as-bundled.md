# 反模式：把 Offer 收下之后才去拉块并装 not already restored / not already complete / not already settled 正式三事（401 余量） 说成已经装完 / 已经齐 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Offer ≠ bundled（401）](../../tracks/implementation/worked-example-offerafter-notrestored-vs-bundled.md)。

## 卖法

把 Offer 收下之后这句写成已经已经装完 / 已经齐 / 已经交差 interchangeable，或已经和 401 offeraccept-vs-restored bundled / offerafter-notrestored-sold-as-bundled interchangeable。

## 为什么错

官方把 Offer 收下之后才去拉块并装 / 回包拒还要再收 Offer / Apply ACCEPT 这块收下了三条核心句写成三件独立的实现事。把它们卖成已经装完 / 已经齐 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Offer 收下之后才去拉块并装 正式三事（401 余量），必须分开 not already restored、not already complete、not already settled 三件事，不要和 401 / 321 / 499 / 648 / 729 / 730 糊成一句。

## 和相邻反模式

- [offeraccept-sold-as-restored](offeraccept-sold-as-restored.md) 是 Offer 收下之后 bundled（401），不是本页 item 1 单句边界。
- [offerafter-notabort-sold-as-bundled](offerafter-notabort-sold-as-bundled.md) 是回包拒单句边界（729 item 2），不是本页收下之后才去拉装边界。
