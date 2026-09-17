# 模式：把 Historical blocks required for auditing replay light client not Use retain_height with caution / not If all nodes remove historical blocks / not Commit Usage persist signal bundled 正式三事（491 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Commit Usage。  
**例**：[Historical blocks required for auditing replay light client not Commit Usage persist signal bundled ≠ bundled（491）](../../tracks/implementation/worked-example-commitretaincaution-notpersist-vs-bundled.md)。

## 三个名字

1. **Historical blocks required 不是 Use retain_height with caution：** 看见 Methods Usage 侧 other purposes / auditing / replay / light client，不是已经 with caution interchangeable，不是 677 commitretaincaution-notdefaultzero interchangeable / 366 retain-height bundled interchangeable。

2. **may also be required / other purposes 不是 If all nodes remove historical blocks：** 看见 Historical blocks may also be required，不是已经 all nodes remove interchangeable / 已经 permanently lost / no bootstrap unless state sync interchangeable，不是 678 commitretaincaution-notbootstrap interchangeable / 323 full-history interchangeable / 38 genesis-replay interchangeable。

3. **auditing / replay / light client 不是 Commit Usage persist signal bundled：** 看见 Historical blocks required for auditing replay light client，不是已经 persist signal bundled interchangeable / 已经 Signal persist application state interchangeable，不是 481 commitpersist bundled interchangeable / 665 infousage-notcommitpersist interchangeable / 497 infousage-persist interchangeable。

官方把 Commit Usage other purposes 单句、Use retain_height with caution（677）、If all nodes remove historical blocks（678）、Commit Usage persist signal bundled（481）写成三个名字。把它们叫成一个「看见 Historical blocks required 就已经 with caution interchangeable / 就已经 all nodes remove interchangeable / 就已经 persist signal bundled interchangeable」，会把 not Use retain_height with caution、not If all nodes remove historical blocks、not Commit Usage persist signal bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Historical blocks required for auditing replay light client not Use retain_height with caution / not If all nodes remove historical blocks / not Commit Usage persist signal bundled 正式三事（491 余量），先数清问的是 Historical blocks required 是不是 Use retain_height with caution / 677 / 366，是不是 may also be required 是不是 If all nodes remove / 678 / 323 / 38，还是 auditing / replay / light client 是不是 Commit Usage persist signal bundled / 481 / 665 / 497，再决定要不要同一次发布。491 commitretaincaution vs kept bundled unbundling 在本页 item 3 完成。
