# 模式：把 CheckTx 回包 events 是给索引用的类型键值不是已经交差 not already settled / not already excluded / not already ordered 正式三事（381 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Response。  
**例**：[回了事件 not already settled ≠ bundled（381）](../../tracks/implementation/worked-example-checktxspace-notsettled-vs-bundled.md)。

## 三个名字

1. **回了事件 不是 already settled：** 看见回了事件 / CheckTx 回包 events 是给索引用的类型键值 / 回了 events，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 381 checktxspace bundled interchangeable / checktxspace-sold-as-code interchangeable。

2. **能按账户查 不是 already excluded：** 看见能按账户查 / 能按账户建索引 / 有账户索引，不是已经没进块 interchangeable / 已经 excluded interchangeable / 已经没进块交差 interchangeable，不是 373 checktxopt interchangeable / 890 checktxspace-notcode interchangeable。

3. **有类型键值 不是 already ordered：** 看见有类型键值 / 有索引类型键值 / 有 events 类型键值，不是已经是共识顺序 interchangeable / 已经 ordered interchangeable / 已经是共识顺序交差 interchangeable，不是 316 txresults interchangeable / 381 checktxspace item 3 interchangeable。

官方把回了事件、不是已经没进块、不是已经是共识顺序写成三个名字。把它们叫成一个「看见回了事件就已经交差 interchangeable / 就已经没进块 interchangeable / 就已经是共识顺序 interchangeable」，会把 not already settled、not already excluded、not already ordered 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx 回包 events 是给索引用的类型键值不是已经交差 not already settled / not already excluded / not already ordered 正式三事（381 余量），先数清问的是回了事件 是不是 already settled / 381 / checktxspace-sold-as-code，是不是能按账户查 是不是 already excluded，还是有类型键值 是不是 already ordered，再决定要不要同一次发布。381 checktxspace-vs-code bundled unbundling 在本页 item 2 续。
