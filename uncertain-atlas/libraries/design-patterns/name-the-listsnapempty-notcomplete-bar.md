# 模式：把 ListSnapshots 空请求 not already complete / not already asked neighbors / not Usage discover 正式三事（395 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ListSnapshots。  
**例**：[ListSnapshots ≠ bundled（395）](../../tracks/implementation/worked-example-listsnapempty-notcomplete-vs-bundled.md)。

## 三个名字

1. **空请求要清单 不是已经齐：** 看见填了空请求，不是已经 322 interchangeable / 734 listsnapempty-notcomplete interchangeable。
2. **看见填了空请求 不是已经问了邻居：** 看见能问，不是已经 322 interchangeable。
3. **看见能填 不是已经 Usage discover：** 看见空请求，不是已经 500 / 661 interchangeable。

官方把 ListSnapshots 空请求要清单 / 本地清单 / 用来发现三条核心句拆成三个名字。把它们叫成一个「看见填了空请求就已经齐」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ListSnapshots 空请求 正式三事（395 余量），先数清问的是空请求要清单是不是已经齐 / 322、是不是已经问了邻居 / 322、还是看见能填是不是已经 Usage discover / 500 / 661，再决定要不要同一次发布。395 listsnapempty vs discovery bundled unbundling 在本页 item 1 启动。
