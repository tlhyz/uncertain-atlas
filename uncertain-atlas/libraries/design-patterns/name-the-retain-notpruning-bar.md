# 模式：把 retain_height 默认 0 不是已经在剪 not already pruning / not already settled / not already no-history 正式三事（366 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Commit Usage。  
**例**：[默认 0 全留 not already pruning ≠ bundled（366）](../../tracks/implementation/worked-example-retain-notpruning-vs-bundled.md)。

## 三个名字

1. **默认 0 全留 不是 already pruning：** 看见默认 0 全留 / `retain_height` 默认是 `0`、表示全留 / 字段在，不是已经在剪 interchangeable / 已经 pruning interchangeable / 已经在剪交差 interchangeable，不是 366 retain bundled interchangeable / retain-sold-as-kept interchangeable。

2. **没填 不是 already settled：** 看见没填 / 没填 retain_height / 字段在没回非零，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 335 finpersist interchangeable / 846 retain-notdeleted interchangeable。

3. **Commit 回了 不是 already no-history：** 看见 Commit 回了 / Commit 回了高度 / 回了字段，不是已经没有历史 interchangeable / 已经 no-history interchangeable / 已经没有历史交差 interchangeable，不是 847 retain-notgenesis interchangeable / 323 full-history interchangeable。

官方把默认 0 全留、不是已经交差、不是已经没有历史写成三个名字。把它们叫成一个「看见默认 0 全留就已经在剪 interchangeable / 就已经交差 interchangeable / 就已经没有历史 interchangeable」，会把 not already pruning、not already settled、not already no-history 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 retain_height 默认 0 不是已经在剪 not already pruning / not already settled / not already no-history 正式三事（366 余量），先数清问的是默认 0 全留 是不是 already pruning / 366 / retain-sold-as-kept，是不是没填 是不是 already settled，还是 Commit 回了 是不是 already no-history，再决定要不要同一次发布。366 retain-vs-kept bundled unbundling 在本页 item 1 启动。
