# 反模式：把自己是提议者不是已经每轮都会调 Prepare not already will-call / not already vv-nil / not already every-round 正式三事（356 余量）说成已经会调 / 已经是 validValue 为 nil / 已经每轮都会叫

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[自己是提议者 not already will-call ≠ bundled（356）](../../tracks/implementation/worked-example-vv-noteveryround-vs-bundled.md)。

## 卖法

把自己是提议者 / 是提议者 / *p* 是提议者 写成已经会调 Prepare interchangeable / 已经 will-call interchangeable / 已经会调 Prepare 交差 interchangeable / 356 validvalue bundled interchangeable / validvalue-sold-as-prepared interchangeable；把进了这一轮 / 进入一轮 *r* 写成已经是 validValue 为 nil interchangeable / 已经 vv-nil interchangeable / 已经 validValue 为 nil 交差 interchangeable；把规范写了 When / When 写了调 Prepare / 规范写了才会调 写成已经每轮都会调 Prepare interchangeable / 已经 every-round interchangeable / 已经每轮都会调交差 interchangeable，或已经和 356 validvalue bundled / validvalue-sold-as-prepared interchangeable / 822 vv-noteveryround interchangeable。

## 为什么错

官方把是提议者、不是已经是 validValue 为 nil、不是已经每轮都会调写成三件独立的实现事。把它们卖成 already will-call interchangeable / already vv-nil interchangeable / already every-round interchangeable，会把 not already will-call、not already vv-nil、not already every-round 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看自己是提议者不是已经每轮都会调 Prepare not already will-call / not already vv-nil / not already every-round 正式三事（356 余量），必须分开 not already will-call、not already vv-nil、not already every-round 三件事，不要和 356 / 311 / 338 / 821 / 823 糊成一句。

## 和相邻反模式

- [validvalue-sold-as-prepared](validvalue-sold-as-prepared.md) 是 validValue 跳过 Prepare bundled 全段，不是本页是提议者 item 2 单句边界。
- [vv-notstillprepare-sold-as-bundled](vv-notstillprepare-sold-as-bundled.md) 是 validValue 非 nil not already still-prepare（356 item 1），不是本页 not already will-call 边界。
- [preparenondet-sold-as-deterministic](preparenondet-sold-as-deterministic.md) 是 Prepare 没有确定性要求（338），不是本页 not already every-round 边界。
