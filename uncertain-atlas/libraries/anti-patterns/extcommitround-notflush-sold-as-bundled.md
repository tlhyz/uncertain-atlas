# 反模式：把 Echo 请求 Message not already Flush / not already delivered / not already settled 正式三事（394 余量） 说成已经是 Flush / 已经送到 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Echo ≠ bundled（394）](../../tracks/implementation/worked-example-extcommitround-notflush-vs-bundled.md)。

## 卖法

把 ExtendedCommitInfo 轮这句写成已经已经是 Flush / 已经送到 / 已经交差 interchangeable，或已经和 394 extcommitround-vs-commitinfo bundled / extcommitround-notflush-sold-as-bundled interchangeable。

## 为什么错

官方把 ExtendedCommitInfo.round / Finalize 请求 next_validators_hash / Echo 请求 Message 三条核心句写成三件独立的实现事。把它们卖成已经是 Flush / 已经送到 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Echo 请求 Message 正式三事（394 余量），必须分开 not already Flush、not already delivered、not already settled 三件事，不要和 394 / 374 / 399 / 732 / 749 / 750 糊成一句。

## 和相邻反模式

- [extcommitround-sold-as-commitinfo](extcommitround-sold-as-commitinfo.md) 是 ExtendedCommitInfo 轮 bundled（394），不是本页 item 3 单句边界。
- [extcommitround-notsamefields-sold-as-bundled](extcommitround-notsamefields-sold-as-bundled.md) 是 next_validators_hash 单句边界（750 item 2），不是本页 Echo Message 边界。
- [commitnoparam-notreqfield-sold-as-bundled](commitnoparam-notreqfield-sold-as-bundled.md) 是 Echo 回包 Message 就已经是入参字段（399/732），不是本页 Echo 请求 Message 边界。
