# 模式：把不带 PubKey 不是已经选型 not already algo / not already no-pq / not already settled 正式三事（364 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Validator / ValidatorUpdate。  
**例**：[省了字段 not already algo ≠ bundled（364）](../../tracks/implementation/worked-example-valnopub-notalgo-vs-bundled.md)。

## 三个名字

1. **省了字段 不是 already algo：** 看见省了字段 / 不带 PubKey 是为了不在 ABCI 上传大后量子公钥 / 省了 PubKey 字段，不是已经选型 interchangeable / 已经 algo interchangeable / 已经选型交差 interchangeable，不是 364 validator bundled interchangeable / validator-sold-as-update interchangeable。

2. **提到后量子公钥 不是 already no-pq：** 看见提到后量子公钥 / 可能很大的后量子公钥 / 提到后量子钥，不是已经没有后量子钥 interchangeable / 已经 no-pq interchangeable / 已经没有后量子钥交差 interchangeable，不是 318 emptyset interchangeable / 839 valaddr-notpubkey interchangeable。

3. **ABCI 不传公钥 不是 already settled：** 看见 ABCI 不传公钥 / ABCI 上不传送公钥 / 不在 ABCI 上传公钥，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 841 valupdate-notset interchangeable / 33 fourgates interchangeable。

官方把省了字段、不是已经没有后量子钥、不是已经交差写成三个名字。把它们叫成一个「看见省了字段就已经选型 interchangeable / 就已经没有后量子钥 interchangeable / 就已经交差 interchangeable」，会把 not already algo、not already no-pq、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看不带 PubKey 不是已经选型 not already algo / not already no-pq / not already settled 正式三事（364 余量），先数清问的是省了字段 是不是 already algo / 364 / validator-sold-as-update，是不是提到后量子公钥 是不是 already no-pq，还是 ABCI 不传公钥 是不是 already settled，再决定要不要同一次发布。364 validator-vs-update bundled unbundling 在本页 item 2 续。
