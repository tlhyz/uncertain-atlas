# 模式：把 If all nodes remove historical blocks not retain_height defaults to 0 retain all / not bootstrap from genesis unless state sync / not Historical blocks required for auditing replay light client 正式三事（491 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Commit Usage。  
**例**：[If all nodes remove historical blocks not retain_height defaults to 0 retain all ≠ bundled（491）](../../tracks/implementation/worked-example-commitretaincaution-notbootstrap-vs-bundled.md)。

## 三个名字

1. **If all nodes remove historical blocks 不是 retain_height defaults to 0 retain all：** 看见 Methods Usage 侧 all nodes remove 段落，不是已经 default 0 retain all interchangeable，不是 366 retain-height bundled interchangeable / 677 commitretaincaution-notdefaultzero interchangeable。

2. **permanently lost / no bootstrap unless state sync 不是 bootstrap from genesis：** 看见 no new nodes will be able to join and bootstrap，不是已经能从创世再装 interchangeable / 已经 retain_height 回了非零就等于已经在剪 interchangeable，不是 323 full-history interchangeable / 38 genesis-replay interchangeable / 366 retain bundled item 3 interchangeable。

3. **all nodes remove 段落 不是 Historical blocks required for auditing replay light client：** 看见 If all nodes remove historical blocks，不是已经 Historical blocks required interchangeable / 已经 persist signal bundled interchangeable，不是 481 commitpersist bundled interchangeable / 679 commitretaincaution-notpersist interchangeable。

官方把 Commit Usage all nodes remove 段落、retain_height defaults to 0 retain all（366）、bootstrap from genesis / full history（323 / 38）、Historical blocks required for auditing / replay / light client（481 / 679）写成三个名字。把它们叫成一个「看见 If all nodes remove historical blocks 就已经 retain_height 默认 0 全留 interchangeable / 就已经能从创世再装 interchangeable / 就已经 Historical blocks required interchangeable」，会把 not retain_height defaults to 0 retain all、not bootstrap from genesis unless state sync、not Historical blocks required 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 If all nodes remove historical blocks not retain_height defaults to 0 retain all / not bootstrap from genesis unless state sync / not Historical blocks required for auditing replay light client 正式三事（491 余量），先数清问的是 If all nodes remove 是不是 retain_height defaults to 0 retain all / 366 / 677，是不是 permanently lost / no bootstrap unless state sync 是不是 bootstrap from genesis / 323 / 38 / 366 item 3，还是 all nodes remove 段落 是不是 Historical blocks required / 481 / 679，再决定要不要同一次发布。491 commitretaincaution vs kept bundled unbundling 在本页 item 2 完成。
