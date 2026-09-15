# 反模式：把 ExtendVote Usage extension creation logic can be non-deterministic 正式三事卖成 ExtendVote Usage bundled / 已经必须同一份扩展 / 已经 Verify 必须确定

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[logic can be non-deterministic ≠ bundled](../../tracks/implementation/worked-example-extusage-nondet-vs-bundled.md)。

## 卖法

- 「看见造扩展的应用逻辑可以非确定 / 看见可以非确定 就已经必须同一份扩展 interchangeable / 已经是同一块就同一份 interchangeable。」
- 「看见逻辑可以变 就已经 ExtendVote Usage bundled interchangeable / 已经 not interpreted by consensus interchangeable。」
- 「看见可以非确定 就已经 Verify 必须确定 interchangeable / 已经 Process MUST deterministic interchangeable。」

## 为什么错

官方把 logic can be non-deterministic、logic can vary / same block does not imply same extension、no MUST deterministic for ExtendVote unlike Verify 写成三件独立的实现事。把它们卖成 ExtendVote Usage bundled、已经必须同一份扩展、已经 Verify 必须确定，会把 creation logic 非确定、logic can vary、ExtendVote 没有 MUST deterministic 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote Usage extension creation logic can be non-deterministic 正式三事，必须分开 logic can be non-deterministic、logic can vary / same block ≠ same extension、no MUST deterministic for ExtendVote 三个名字，不要把它们卖成 ExtendVote Usage bundled / 已经必须同一份扩展 / 已经 Verify 必须确定。

## 和相邻反模式

- [extusage-sold-as-deterministic](extusage-sold-as-deterministic.md) 是 437 bundled 三事专用；本页是 creation logic non-deterministic 单句边界。
- [extusage-zerolen-sold-as-bundled](extusage-zerolen-sold-as-bundled.md) 是 0-length on non-nil 专用，不是本页 non-deterministic 边界。
- [verifyrespstatus-sold-as-verifystatus](verifyrespstatus-sold-as-verifystatus.md) 是 Verify MUST deterministic 回包栏，不是本页 ExtendVote 侧 can be non-deterministic 边界。
