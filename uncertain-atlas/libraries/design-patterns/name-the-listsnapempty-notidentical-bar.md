# 模式：把 ListSnapshots 本地清单 not already identical / not already restored / not already settled 正式三事（395 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ListSnapshots。  
**例**：[ListSnapshots ≠ bundled（395）](../../tracks/implementation/worked-example-listsnapempty-notidentical-vs-bundled.md)。

## 三个名字

1. **本地清单 不是已经是同一份：** 看见回了清单，不是已经 368 interchangeable / 735 listsnapempty-notidentical interchangeable。
2. **看见回了清单 不是已经装完：** 看见有本地清单，不是已经 321 interchangeable。
3. **看见能回 不是已经交差：** 看见本地清单，不是已经交差 / 396 interchangeable。

官方把 ListSnapshots 空请求要清单 / 本地清单 / 用来发现三条核心句拆成三个名字。把它们叫成一个「看见填了空请求就已经齐」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ListSnapshots 本地清单 正式三事（395 余量），先数清问的是本地清单是不是已经是同一份 / 368、是不是已经装完 / 321、还是看见能回是不是已经交差 / 396，再决定要不要同一次发布。395 listsnapempty vs discovery bundled unbundling 在本页 item 2 续。
