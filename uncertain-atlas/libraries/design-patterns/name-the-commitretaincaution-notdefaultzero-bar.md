# 模式：把 Commit Usage Use retain_height with caution not retain_height defaults to 0 retain all / not blocks below height may be removed / not Commit Usage persist signal bundled 正式三事（491 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Commit Usage。  
**例**：[Commit Usage Use retain_height with caution not retain_height defaults to 0 retain all ≠ bundled（491）](../../tracks/implementation/worked-example-commitretaincaution-notdefaultzero-vs-bundled.md)。

## 三个名字

1. **Use retain_height with caution 不是 retain_height defaults to 0 retain all：** 看见 Methods Usage 侧 caution 语气，不是已经 default 0 retain all interchangeable，不是 366 retain-height bundled interchangeable / 677 commitretaincaution-notdefaultzero interchangeable。

2. **要慎用 retain_height 不是 blocks below height may be removed：** 看见 caution 段落，不是已经 blocks below may be removed interchangeable / 已经回了高度就等于已经在剪 interchangeable，不是 366 retain bundled item 2 interchangeable / 678 commitretaincaution-notbootstrap interchangeable。

3. **with caution 单句 不是 Commit Usage persist signal bundled：** 看见 Use retain_height with caution，不是已经 persist signal bundled interchangeable / 已经 Signal persist application state interchangeable，不是 481 commitpersist bundled interchangeable / 679 commitretaincaution-notpersist interchangeable。

官方把 Commit Usage caution 语气单句、retain_height defaults to 0 retain all（366）、blocks below height may be removed、Commit Usage persist signal bundled（481）写成三个名字。把它们叫成一个「看见 Use retain_height with caution 就已经 retain_height 默认 0 全留 interchangeable / 就已经 blocks below may be removed interchangeable / 就已经 persist signal bundled interchangeable」，会把 not defaults to 0 retain all、not blocks below height may be removed、not Commit Usage persist signal bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Commit Usage Use retain_height with caution not retain_height defaults to 0 retain all / not blocks below height may be removed / not Commit Usage persist signal bundled 正式三事（491 余量），先数清问的是 Use retain_height with caution 是不是 retain_height defaults to 0 retain all / 366 / 335，是不是 caution 段落 是不是 blocks below height may be removed / 366 item 2 / 678，还是 with caution 单句 是不是 Commit Usage persist signal bundled / 481 / 679，再决定要不要同一次发布。491 commitretaincaution vs kept bundled unbundling 在本页 item 1 完成。
