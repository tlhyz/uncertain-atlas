# 模式：把 CheckTx 技术上可选、不参与处理块不是已经是四门已经结算 not already fourgates / not already settled / not already removed 正式三事（373 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage。  
**例**：[能回 not already fourgates ≠ bundled（373）](../../tracks/implementation/worked-example-checktxopt-notfourgates-vs-bundled.md)。

## 三个名字

1. **能回 不是 already fourgates：** 看见能回 / CheckTx 技术上可选、不参与处理块 / 能回 CheckTx，不是已经是四门已经结算 interchangeable / 已经 fourgates interchangeable / 已经是四门已经结算交差 interchangeable，不是 373 checktxopt bundled interchangeable / checktxopt-sold-as-block interchangeable。

2. **可选 不是 already settled：** 看见可选 / 技术上可选 / CheckTx 可选，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 33 four gates interchangeable / 316 Finalize Code interchangeable。

3. **没参与处理块 不是 already removed：** 看见没参与处理块 / 不参与处理块 / 没处理块，不是已经从池里删掉 interchangeable / 已经 removed interchangeable / 已经从池里删掉交差 interchangeable，不是 301 proposed-removed interchangeable / 373 checktxopt item 2 interchangeable。

官方把能回、不是已经交差、不是已经从池里删掉写成三个名字。把它们叫成一个「看见能回就已经是四门已经结算 interchangeable / 就已经交差 interchangeable / 就已经从池里删掉 interchangeable」，会把 not already fourgates、not already settled、not already removed 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx 技术上可选、不参与处理块不是已经是四门已经结算 not already fourgates / not already settled / not already removed 正式三事（373 余量），先数清问的是能回 是不是 already fourgates / 373 / checktxopt-sold-as-block，是不是可选 是不是 already settled，还是没参与处理块 是不是 already removed，再决定要不要同一次发布。373 checktxopt-vs-block bundled unbundling 在本页 item 1 启动。
