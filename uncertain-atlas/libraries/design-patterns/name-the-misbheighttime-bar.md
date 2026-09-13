# 模式：把 Misbehavior height/time 栏正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Misbehavior Fields。  
**例**：[Misbehavior.height 是过错发生的高度 ≠ 已经 Prepare/Process 请求 height](../../tracks/implementation/worked-example-misbheighttime-vs-votetime.md)。

## 三个名字

1. **Misbehavior.height 是过错发生的高度不是已经 Prepare/Process 请求 height：** 看见 offense height 不是已经对上拟议头。
2. **Misbehavior.time 是那一高已提交块的时间戳不是已经验过票上 Timestamp：** 看见 committed-at-height time 不是已经票上时间 interchangeable。
3. **height 和 time 一起不是已经定了奖惩：** 看见对上了 height/time 不是已经 slashed。

## 为什么要分开叫

官方把 Misbehavior 里 `height` 和 `time` 栏写成三个名字。把它们叫成一个「看见 Misbehavior 里填了 height/time 就已经验过时间」，会把 offense height、committed block time、请求栏 height/time 一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Misbehavior 里填了 height/time 就已经验过时间」，先数清问的是 Misbehavior.height 是不是已经 Prepare/Process 请求 height、Misbehavior.time 是不是已经验过票上 Timestamp，还是 height 和 time 一起是不是已经定了奖惩，再决定要不要同一次发布。
