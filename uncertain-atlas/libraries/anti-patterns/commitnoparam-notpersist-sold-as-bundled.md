# 反模式：把 Commit 不带参数 not already persist / not persist signal / not retain_height 正式三事（399 余量） 说成已经落盘 / 已经 persist signal / 已经 retain_height

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Commit ≠ bundled（399）](../../tracks/implementation/worked-example-commitnoparam-notpersist-vs-bundled.md)。

## 卖法

把 Commit 空请求这句写成已经已经落盘 / 已经 persist signal / 已经 retain_height interchangeable，或已经和 399 commitnoparam-vs-persist bundled / commitnoparam-notpersist-sold-as-bundled interchangeable。

## 为什么错

官方把 Commit 不带参数 / Echo 回包 Message / Echo 用来测实现三条核心句写成三件独立的实现事。把它们卖成已经落盘 / 已经 persist signal / 已经 retain_height，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Commit 不带参数 正式三事（399 余量），必须分开 not already persist、not persist signal、not retain_height 三件事，不要和 399 / 335 / 481 / 701 / 491 / 692 / 732 / 733 糊成一句。

## 和相邻反模式

- [commitnoparam-sold-as-persist](commitnoparam-sold-as-persist.md) 是 Commit 空请求 bundled（399），不是本页 item 1 单句边界。
- [commitnoparam-notreqfield-sold-as-bundled](commitnoparam-notreqfield-sold-as-bundled.md) 是 Echo 回包单句边界（732 item 2），不是本页 Commit 不带参数边界。
