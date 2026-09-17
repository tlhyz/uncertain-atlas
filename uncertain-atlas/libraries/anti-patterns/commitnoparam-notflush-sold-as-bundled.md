# 反模式：把 Echo 用来测实现 not Flush / not already delivered / not Echo Usage test 正式三事（399 余量） 说成已经刷完 / 已经送到 / 已经 Echo Usage 测实现

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Echo ≠ bundled（399）](../../tracks/implementation/worked-example-commitnoparam-notflush-vs-bundled.md)。

## 卖法

把 Commit 空请求这句写成已经已经刷完 / 已经送到 / 已经 Echo Usage 测实现 interchangeable，或已经和 399 commitnoparam-vs-persist bundled / commitnoparam-notflush-sold-as-bundled interchangeable。

## 为什么错

官方把 Commit 不带参数 / Echo 回包 Message / Echo 用来测实现三条核心句写成三件独立的实现事。把它们卖成已经刷完 / 已经送到 / 已经 Echo Usage 测实现，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Echo 用来测实现 正式三事（399 余量），必须分开 not Flush、not already delivered、not Echo Usage test 三件事，不要和 399 / 374 / 492 / 673 / 731 / 732 糊成一句。

## 和相邻反模式

- [commitnoparam-sold-as-persist](commitnoparam-sold-as-persist.md) 是 Commit 空请求 bundled（399），不是本页 item 3 单句边界。
- [commitnoparam-notreqfield-sold-as-bundled](commitnoparam-notreqfield-sold-as-bundled.md) 是 Echo 回包单句边界（732 item 2），不是本页测实现边界。
